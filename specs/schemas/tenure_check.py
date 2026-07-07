#!/usr/bin/env python3
"""VCDesign tenure check: 責任空白リスクの検出.

schema_case.yaml (v0.2) の tenure フィールドに基づき、case インスタンスを走査して
「責任の所在が拡散しつつある」状態を洗い出す。背景は core/value-tenure-model.md。

設計判断（2026-07 決定）: reaffirmation は事象駆動である。
  - custody 交代の後に reaffirmation が無い       → WARN（事象駆動の再確認義務）
  - 純粋な時間経過による減衰（既定 180 日）       → INFO（弱いシグナル。exit code に影響しない）
  カレンダー駆動の減衰を WARN にすると、review_triggers で退けた「儀式化」が
  reaffirmation に移るだけになるため、時間減衰は注意喚起に留める。
  review_trigger 発火時の reaffirmation 義務は decision log 側の invariant
  （schema_log.yaml）で扱い、本スクリプトの対象外。

検出レベル:
  ERROR: owner が空 / custody_chain エントリの必須項目欠落 /
         custody_chain があるのに re_derivation_basis が無い
  WARN:  custody 交代後に reaffirmation が無い /
         引き渡しの再導出確認（re_derivation_confirmed）が yes でない /
         custody_chain の末尾と現在の owner の不一致 /
         active な case に review_triggers が無い
  INFO:  last_reaffirmed が古い（--max-age-days、既定 180 日） /
         交代の無い active case に last_reaffirmed が無い

使い方:
  python3 specs/schemas/tenure_check.py [paths...] [--max-age-days N]
  python3 specs/schemas/tenure_check.py --self-test
  （path 省略時は specs/examples を走査。ERROR があれば exit 1）
"""

import argparse
import datetime
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

CUSTODY_REQUIRED = ("from", "to", "date", "reason")
FIXTURES_DIR = Path(__file__).parent / "fixtures"


def iter_case_dicts(node, path="$"):
    """case_id と owner を持つ mapping を case インスタンスとみなして再帰探索する。"""
    if isinstance(node, dict):
        if "case_id" in node and "owner" in node:
            yield path, node
        else:
            for key, value in node.items():
                yield from iter_case_dicts(value, f"{path}.{key}")
    elif isinstance(node, list):
        for index, item in enumerate(node):
            yield from iter_case_dicts(item, f"{path}[{index}]")


def as_date(value):
    if isinstance(value, datetime.datetime):
        return value.date()
    if isinstance(value, datetime.date):
        return value
    if isinstance(value, str):
        try:
            return datetime.date.fromisoformat(value[:10])
        except ValueError:
            return None
    return None


def actor_name(value):
    if isinstance(value, dict):
        return value.get("actor") or value.get("name")
    if isinstance(value, str):
        return value
    return None


def check_case(case, location, max_age_days, today):
    errors, warnings, infos = [], [], []
    case_id = case.get("case_id", "?")

    def err(msg):
        errors.append(f"[ERROR] {location} ({case_id}): {msg}")

    def warn(msg):
        warnings.append(f"[WARN]  {location} ({case_id}): {msg}")

    def info(msg):
        infos.append(f"[INFO]  {location} ({case_id}): {msg}")

    owner = case.get("owner")
    if not owner or (isinstance(owner, dict) and not actor_name(owner)):
        err("owner が空です。責任の空白（A1 違反リスク）。current owner を明示してください")

    custody = case.get("custody_chain") or []
    latest_transfer = None
    for i, entry in enumerate(custody):
        if not isinstance(entry, dict):
            err(f"custody_chain[{i}] が mapping ではありません")
            continue
        missing = [f for f in CUSTODY_REQUIRED if not entry.get(f)]
        if missing:
            err(f"custody_chain[{i}] に必須項目がありません: {', '.join(missing)}")
        confirmed = entry.get("re_derivation_confirmed")
        if confirmed not in (True, "yes"):
            warn(
                f"custody_chain[{i}] の re_derivation_confirmed が yes ではありません"
                "（引き受け先が判断を再導出できることを確認してください）"
            )
        entry_date = as_date(entry.get("date"))
        if entry_date and (latest_transfer is None or entry_date > latest_transfer):
            latest_transfer = entry_date

    if custody and not case.get("re_derivation_basis"):
        err(
            "custody_chain があるのに re_derivation_basis がありません"
            "（invariant: case_with_custody_chain_must_have_re_derivation_basis）"
        )

    if custody:
        last_to = actor_name(custody[-1].get("to")) if isinstance(custody[-1], dict) else None
        owner_name = actor_name(owner)
        if last_to and owner_name and last_to != owner_name:
            warn(
                f"custody_chain の末尾（{last_to}）と owner（{owner_name}）が一致しません。"
                "記録されていない交代（custody_gap）の可能性"
            )

    is_active = case.get("current_state") in (None, "active", "drifting", "deferred")
    if is_active:
        if not case.get("review_triggers"):
            warn(
                "review_triggers がありません。見直しが事象駆動で定義されていない"
                "（metric: review_trigger_missing）"
            )

        reaffirmed = case.get("last_reaffirmed")
        reaffirmed_at = as_date(reaffirmed.get("at")) if isinstance(reaffirmed, dict) else None

        # 事象駆動の義務（WARN）: custody 交代の後には reaffirmation が必要
        if latest_transfer and (reaffirmed_at is None or reaffirmed_at < latest_transfer):
            warn(
                f"custody 交代（{latest_transfer}）後の reaffirmation がありません。"
                "引き受け先による有効性確認は事象駆動の義務です（metric: custody_gap）"
            )
        elif not reaffirmed:
            # 交代の無い安定 case では、reaffirmation 欠如は弱いシグナルに留める
            info("last_reaffirmed がありません（弱いシグナル。安定した決定は事象が無いのが健全）")
        elif reaffirmed_at is None:
            warn("last_reaffirmed.at が日付として読めません")
        elif (today - reaffirmed_at).days > max_age_days:
            # 純粋な時間減衰は弱いシグナル。WARN にすると reaffirmation が儀式化する
            info(
                f"last_reaffirmed が {(today - reaffirmed_at).days} 日前です"
                f"（閾値 {max_age_days} 日。弱いシグナル: reaffirmation_decay）"
            )

    return errors, warnings, infos


def collect_files(paths):
    for raw in paths:
        p = Path(raw)
        if p.is_dir():
            yield from sorted(p.rglob("*.yaml"))
            yield from sorted(p.rglob("*.yml"))
        elif p.is_file():
            yield p
        else:
            print(f"[WARN]  path not found: {p}", file=sys.stderr)


def scan(paths, max_age_days, today):
    all_errors, all_warnings, all_infos, case_count = [], [], [], 0
    for file in collect_files(paths):
        try:
            documents = list(yaml.safe_load_all(file.read_text(encoding="utf-8")))
        except yaml.YAMLError as exc:
            all_errors.append(f"[ERROR] {file}: YAML parse error: {exc}")
            continue
        for doc in documents:
            for path, case in iter_case_dicts(doc):
                case_count += 1
                errors, warnings, infos = check_case(
                    case, f"{file}:{path}", max_age_days, today
                )
                all_errors.extend(errors)
                all_warnings.extend(warnings)
                all_infos.extend(infos)
    return all_errors, all_warnings, all_infos, case_count


def self_test(max_age_days):
    """fixtures/clean-case.yaml が findings 0、fixtures/dirty-case.yaml が検出されることを確認する。"""
    today = datetime.date.today()
    failed = False

    errors, warnings, _infos, count = scan([FIXTURES_DIR / "clean-case.yaml"], max_age_days, today)
    if count != 1 or errors or warnings:
        print(f"self-test FAIL: clean fixture expected 0 error / 0 warning, got {len(errors)} / {len(warnings)}")
        for line in errors + warnings:
            print("  " + line)
        failed = True
    else:
        print("self-test: clean fixture OK (0 error, 0 warning)")

    errors, warnings, infos, count = scan([FIXTURES_DIR / "dirty-case.yaml"], max_age_days, today)
    if count != 2 or len(errors) < 3 or len(warnings) < 3 or len(infos) < 1:
        print(
            "self-test FAIL: dirty fixture expected 2 cases with >=3 errors, >=3 warnings, >=1 info, "
            f"got {len(errors)} / {len(warnings)} / {len(infos)} over {count} case(s)"
        )
        failed = True
    else:
        print(
            f"self-test: dirty fixture OK ({len(errors)} errors, {len(warnings)} warnings, "
            f"{len(infos)} infos detected)"
        )

    sys.exit(1 if failed else 0)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", default=["specs/examples"])
    parser.add_argument("--max-age-days", type=int, default=180)
    parser.add_argument("--self-test", action="store_true",
                        help="fixtures で clean=0 findings / dirty=検出 を確認する")
    args = parser.parse_args()

    if args.self_test:
        self_test(args.max_age_days)

    today = datetime.date.today()
    all_errors, all_warnings, all_infos, case_count = scan(
        args.paths or ["specs/examples"], args.max_age_days, today
    )

    for line in all_errors + all_warnings + all_infos:
        print(line)
    print(
        f"tenure_check: {case_count} case(s) scanned, "
        f"{len(all_errors)} error(s), {len(all_warnings)} warning(s), {len(all_infos)} info(s)"
    )
    sys.exit(1 if all_errors else 0)


if __name__ == "__main__":
    main()
