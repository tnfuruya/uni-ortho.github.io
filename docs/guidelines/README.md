# ホームページ倫理審査指針（参照用）

## 同梱 PDF

| ファイル | 内容 |
|----------|------|
| `hp_ethics_guidelines.pdf` | **日本矯正歯科学会ホームページ倫理審査指針**（2022年3月現在）／倫理・裁定委員会 |

厚生労働省「医療広告ガイドライン」等に沿った学会独自の審査基準です。改定がある場合は [日本矯正歯科学会](https://www.jos.gr.jp/) のお知らせ等で最新版を確認してください。

## 入手元（共有いただいた URL）

http://www.hioo.jp/files/7016/7501/7468/hp_ethics_guidelines.pdf

学会公式以外のミラーである可能性があるため、運用上は学会掲載の PDF と差分がないか確認することを推奨します。

## Cursor で AI に読ませるとき

1. チャット入力欄で **`@docs/guidelines/hp_ethics_guidelines.pdf`** を指定する（または本 `README.md` を指定し、必要なら PDF も併記する）。
2. 継続的に HTML を触るときは、プロジェクトの **`.cursor/rules/jos-homepage-ethics.mdc`** が要点を補助します（詳細は常に PDF および厚労省ガイドライン本体に照らすこと）。

## Git に載せたくない場合

院内方針でリポジトリに PDF を置けない場合は、この `docs/guidelines/` を `.gitignore` に追加し、各自の PC のみに PDF を置いて `@` 参照してください。
