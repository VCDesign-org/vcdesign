# vcdesign.org の反映手順

vcdesign.org は、手元の `site/` を rsync でレンタルサーバーへ同期して公開している。
GitHub の main へのマージだけではサイトは切り替わらない。**マージのあと、この手順でアップロードしたときに切り替わる。**

```bash
rsync -avz --delete \
  -e "ssh -i ~/.ssh/mykey2.pem -p 8022 -o IdentitiesOnly=yes" \
  --exclude ".git" \
  --exclude "node_modules" \
  --exclude "_tools" \
  --exclude ".DS_Store" \
  --exclude "README.md" \
  ./site/ r3762884@www336.onamae.ne.jp:~/public_html/vcdesign.org/
```

`--delete` があるため、**`site/` にないファイルはサーバーから消える**。
サーバーにだけ置いたファイル（検索エンジンの所有権確認ファイル、`.htaccess` など）があれば、先に `site/` に入れるか `--exclude` に足す。

---

## 1. マージ前（PR の段階）

1. CI が通っていることを確認する。手元でも同じ検査を実行できる。

   ```bash
   yamllint -c .yamllint specs/**/*.yaml
   python3 specs/schemas/tenure_check.py --self-test
   python3 specs/schemas/tenure_check.py specs/examples
   bash .github/scripts/validate_docs.sh     # サイトのリンク・日英の対応・v1 語彙の検査を含む
   ```

2. ブラウザで確認する。

   ```bash
   python3 -m http.server -d site 8000
   # http://localhost:8000/     日本語トップ
   # http://localhost:8000/en/  英語トップ
   # http://localhost:8000/ja/  旧 URL → / へ転送されること
   ```

## 2. マージ後のアップロード

1. main を最新にする。

   ```bash
   git switch main
   git pull origin main
   ```

2. `site/` に余計なファイルがないことを確かめる。`site/.gitignore` で無視しているファイル（`repo/` など）も rsync ではアップロードされる。

   ```bash
   git status --short --ignored site/
   # 何も表示されなければよい（.DS_Store は rsync で除外される）
   ```

3. サーバー上の現行サイトを控えておく（戻すため）。

   ```bash
   ssh -i ~/.ssh/mykey2.pem -p 8022 -o IdentitiesOnly=yes r3762884@www336.onamae.ne.jp \
     'tar czf ~/vcdesign-backup-$(date +%Y%m%d%H%M).tgz -C ~/public_html vcdesign.org'
   ```

4. **ドライラン**で、消えるファイルを確認する（`-n` を付けると何も変更しない）。

   ```bash
   rsync -avzn --delete \
     -e "ssh -i ~/.ssh/mykey2.pem -p 8022 -o IdentitiesOnly=yes" \
     --exclude ".git" --exclude "node_modules" --exclude "_tools" \
     --exclude ".DS_Store" --exclude "README.md" \
     ./site/ r3762884@www336.onamae.ne.jp:~/public_html/vcdesign.org/ | grep '^deleting'
   ```

   v2 への切り替えで消えるのは次の16ファイルだけのはず。これ以外の `deleting` が出たら、サーバーにだけ置いたファイルなので、止めて確認する。

   ```text
   deleting images/VCDesign.jpg                       （どのページからも未使用）
   deleting images/flowchart.jpg                      （同上）
   deleting images/overview-diagram.jpg               （同上）
   deleting ja/core_change_proposal.txt               （作業メモ）
   deleting ja/css/diagnostics.css                    （未使用）
   deleting ja/css/main.css                           （日本語ページはルートの css/ を使う）
   deleting ja/css/page-shell.css
   deleting ja/css/reading.css
   deleting ja/images/VCDesign.jpg                    （未使用）
   deleting ja/images/flowchart.jpg
   deleting ja/images/overview-diagram.jpg
   deleting ja/legacy/validation/20260125-report1.pdf （/legacy/validation/ の同じ PDF に一本化）
   deleting ja/legacy/validation/20260125-report2.pdf
   deleting ja/research/deepresearch-2026-01.pdf      （/research/ の同じ PDF に一本化）
   deleting ja/research/deepresearch-2026-03.pdf
   deleting ja/vc-ad/2026-01deepreserch.pdf           （/vc-ad/ の同じ PDF に一本化）
   ```

5. 本番のアップロードを実行する（上のスクリプト）。

## 3. アップロード後の確認

```bash
for u in / /en/ /value-continuity/ /core/ /decision/ /examples/ /ai/ /migration/ /projects/ /vc-ad/ /legacy/ \
         /en/core/ /en/decision/ /en/legacy/ /tddd/ /value-review/ /vms/ /vms/marketing/ /re-derivation-layer/ \
         /legacy/v1/ /legacy/boa/ /research/deepresearch-2026-01.pdf /sitemap.xml \
         /ja/ /ja/vms/ /ja/legacy/boa/ /reality-fit/ /constitution/ /vc-ad/why.html; do
  printf '%s %s\n' "$(curl -s -o /dev/null -w '%{http_code}' "https://vcdesign.org$u")" "$u"
done
# すべて 200 であること。/ja/… /reality-fit/ /constitution/ /vc-ad/why.html は転送用ページ（200）で、
# ブラウザで開くと新しい場所へ移る。
```

ブラウザでも、日本語トップ、英語トップ、スマートフォン表示、`/ja/` からの転送を一度ずつ確かめる。

## 4. 戻し方

どちらかで戻す。

- **控えから戻す**（3 で取った tar を使う）

  ```bash
  ssh -i ~/.ssh/mykey2.pem -p 8022 -o IdentitiesOnly=yes r3762884@www336.onamae.ne.jp \
    'cd ~/public_html && mv vcdesign.org vcdesign.org.v2 && tar xzf ~/vcdesign-backup-YYYYMMDDHHMM.tgz'
  ```

- **git から戻す**：マージ直前のコミットを取り出して、同じ rsync を実行する。

  ```bash
  git switch --detach <マージコミット>^1
  # 上の rsync を実行
  git switch main
  ```

## 5. 任意：消えた PDF の旧 URL を転送する

`/ja/research/*.pdf` などの旧 URL は、HTML の転送ページを置けないため、アップロード後は 404 になる。
転送したい場合は、サーバーが `.htaccess` を読むことを確かめたうえで、次の内容を `site/.htaccess` として追加する
（`--delete` で消えないよう、サーバーに直接置かず `site/` に入れる）。

```apache
Redirect 301 /ja/research/deepresearch-2026-01.pdf /research/deepresearch-2026-01.pdf
Redirect 301 /ja/research/deepresearch-2026-03.pdf /research/deepresearch-2026-03.pdf
Redirect 301 /ja/legacy/validation/20260125-report1.pdf /legacy/validation/20260125-report1.pdf
Redirect 301 /ja/legacy/validation/20260125-report2.pdf /legacy/validation/20260125-report2.pdf
Redirect 301 /ja/vc-ad/2026-01deepreserch.pdf /vc-ad/2026-01deepreserch.pdf
```

追加後に `curl -sI https://vcdesign.org/ja/research/deepresearch-2026-01.pdf` が `301` を返すことを確認する。
`500` になった場合は `site/.htaccess` を消して、もう一度アップロードする。

## 構成（v2 以降）

| 場所 | 内容 |
| --- | --- |
| `site/` | 日本語（ルート） |
| `site/en/` | 英語。日本語と同じ構成 |
| `site/ja/` | 旧 URL の転送ページだけ |
| `site/legacy/`、`site/en/legacy/` | 過去の資料（歴史的ドキュメントの注意書きが必須。CI で検査） |
| `site/assets/site.css` | v2 のページの共通スタイル |
| `site/css/`、`site/en/css/` | 関連プロジェクトと過去の資料のページが使う、以前からのスタイル |

新しいページを足すときは、日本語と英語の両方に同じパスで置く（CI が対応を検査する）。
v1 の語彙は、`legacy/`、`migration/`、`value-review/`、`vms/` の外では使わない（CI が検査する）。
