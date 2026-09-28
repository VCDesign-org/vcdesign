#!/usr/bin/env python3
"""Checks for the static site under site/.

1. Internal links: every relative or root-absolute href/src points to an
   existing file, and every #fragment exists in the target page. Links to
   this repository on GitHub (blob/main/..., tree/main/...) point to an
   existing file or directory with the matching route.
2. Language parity: Japanese pages live at the root and English pages under
   en/, with the same structure. site/ja/ holds redirect pages only.
3. v1 vocabulary: v1 decision words are used only in the archive, the
   migration page, and the related-project pages kept with a v1 notice.

Standard library only. Run from the repository root:
    python3 .github/scripts/check_site.py
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

SITE = Path("site")

# Pages allowed to use v1 vocabulary (paths relative to site/, both languages).
V1_ALLOWED = ("legacy/", "migration/", "value-review/", "vms/")
V1_TERMS = [
    r"DeferToPool",
    r"small_go",
    r"scale_go",
    r"decision_size",
    r"tail_signals?",
    r"scale_gate",
    r"Judgment Closure",
    r"[Dd]ecision [Pp]osture",
    r"Decision Closure",
    r"Resolution Handshake",
    r"action:\s*fix",
    r"\bRCL\b",
    r"PDΔA",
]


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
        self.refresh = None
        self.text = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and "name" in a:
            self.ids.add(a["name"])
        for key in ("href", "src"):
            if a.get(key):
                self.links.append(a[key])
        if tag == "meta" and (a.get("http-equiv") or "").lower() == "refresh":
            self.refresh = a.get("content", "")
        if tag in ("script", "style"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.text.append(data)


def parse(path):
    c = Collector()
    c.feed(path.read_text(encoding="utf-8"))
    return c


REPO_URL = re.compile(r"^https://github\.com/VCDesign-org/vcdesign/(blob|tree)/main/([^#?]*)")


def check_repo_link(url):
    """Links into this repository must use blob/ for files and tree/ for
    directories, and the path must exist in this checkout."""
    m = REPO_URL.match(url)
    if not m:
        return None
    kind, path = m.group(1), unquote(m.group(2)).rstrip("/")
    target = Path(path)
    if not target.exists():
        return f"repository path does not exist: {path}"
    if kind == "blob" and target.is_dir():
        return f"directory linked with blob/ (use tree/): {path}"
    if kind == "tree" and target.is_file():
        return f"file linked with tree/ (use blob/): {path}"
    return None


def resolve(page, url):
    parts = urlsplit(url)
    if parts.scheme or parts.netloc or url.startswith(("mailto:", "tel:", "javascript:")):
        return None, None
    target = unquote(parts.path)
    if not target:
        return page, parts.fragment
    if target.startswith("/"):
        path = SITE / target.lstrip("/")
    else:
        path = (page.parent / target)
    if target.endswith("/") or path.is_dir():
        path = path / "index.html"
    return Path(*[p for p in path.parts]), parts.fragment


def norm(p):
    return Path(str(p.resolve()).replace(str(Path.cwd().resolve()) + "/", ""))


def main():
    errors = []
    pages = sorted(SITE.rglob("*.html"))
    parsed = {norm(p): parse(p) for p in pages}

    # 1. links and fragments
    for page, c in parsed.items():
        for url in c.links:
            problem = check_repo_link(url)
            if problem:
                errors.append(f"{page}: {problem} ({url})")
                continue
            target, frag = resolve(page, url)
            if target is None:
                continue
            t = norm(target)
            if not t.exists():
                errors.append(f"{page}: broken link {url}")
                continue
            if frag and t.suffix == ".html" and t in parsed and frag not in parsed[t].ids:
                errors.append(f"{page}: missing anchor #{frag} in {url}")
        if c.refresh is not None:
            m = re.search(r"url=(.+)$", c.refresh, re.I)
            if m:
                target, _ = resolve(page, m.group(1).strip())
                if target is not None and not norm(target).exists():
                    errors.append(f"{page}: redirect target missing {m.group(1)}")

    # 2. language parity (ja at root, en under en/)
    ja = {p.relative_to(SITE) for p in parsed if p.parts[1] not in ("en", "ja")}
    en = {p.relative_to(SITE / "en") for p in parsed if p.parts[1] == "en"}
    for rel in sorted(ja - en):
        errors.append(f"site/{rel}: no English counterpart at site/en/{rel}")
    for rel in sorted(en - ja):
        errors.append(f"site/en/{rel}: no Japanese counterpart at site/{rel}")
    for p, c in parsed.items():
        if p.parts[1] == "ja" and c.refresh is None:
            errors.append(f"{p}: pages under site/ja/ must be redirects")

    # 3. v1 vocabulary
    pattern = re.compile("|".join(V1_TERMS))
    for p, c in parsed.items():
        rel = str(p.relative_to(SITE))
        if rel.startswith("en/"):
            rel = rel[3:]
        if rel.startswith("ja/") or rel.startswith(V1_ALLOWED) or c.refresh is not None:
            continue
        text = " ".join(c.text)
        for m in pattern.finditer(text):
            errors.append(f"{p}: v1 vocabulary '{m.group(0)}' outside legacy/migration")

    if errors:
        print("Site check failed:")
        for e in errors:
            print("  " + e)
        return 1
    print(f"Site check passed ({len(parsed)} pages).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
