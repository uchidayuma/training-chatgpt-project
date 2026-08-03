# Agent Skills サンプル集

Agent Skills 研修で使用するサンプルスキル集です。
用途の違う2セットが入っています。

| ディレクトリ | 用途 | 本数 |
|---|---|---|
| [`chatgpt-project/`](#chatgpt-project--構成パターンを学ぶ5本) | 構成パターンを学ぶ教材。ChatGPT Projects で体験する題材と対応 | 5 |
| [`.opencode/skills/`](#opencodeskills--業務そのまま使える7本) | OpenCode に置いてそのまま動かす業務サンプル | 7 |

SKILL.md の書式はどちらも同じです。ChatGPT Projects で作ったものを
`.opencode/skills/` に置けばそのまま動きます（逆も同様）。

---

## `chatgpt-project/` — 構成パターンを学ぶ5本

シンプルな構成からフル活用まで、段階的なパターンを示しています。
**どのフォルダを、なぜ使うのか**を理解するための教材です。

| スキル | できること | 構成 | 学べるパターン |
|---|---|---|---|
| `complaint-email` | 顧客クレームへの返信メールを作成する | `references/` のみ | 最小構成 |
| `meeting-minutes` | 会議メモ・録音テキストから議事録を作成する | `references/` + `assets/` | 穴埋めテンプレートの使い方 |
| `weekly-report` | KPIデータから経営層向け週次レポートを作成する | `references/` + `scripts/` | 実行スクリプトの使い方 |
| `proposal-doc` | 顧客・社内向けの提案書・企画書を作成する | `references/` + `assets/` × 2 | 複数アセットの使い方 |
| `social-media-post` | X・LinkedIn等のビジネスSNS投稿文を作成する | `references/` + `assets/` + `scripts/` | フル活用パターン |

## `.opencode/skills/` — 業務でそのまま使える7本

構成パターンの学習用ではなく、**実務にそのまま近い粒度**で書かれたサンプルです。
`complaint-email` と `weekly-report` は `chatgpt-project/` にも同名のものがありますが、
別の内容なので注意してください。

| スキル | できること | 構成 |
|---|---|---|
| `complaint-email` ★ | 苦情・クレームへの謝罪と対応を含む返信メールを作成する（800字以内） | `references/` + `assets/` |
| `handover-document` ★ | 異動・退職・長期休暇時の業務引き継ぎ書を作成する（A4 2枚以内） | `references/` + `assets/` |
| `survey-analysis` ★ | アンケートの自由記述を感情スコアとカテゴリに分類し、集計と傾向サマリーを出す | `references/` + `assets/` + `scripts/` |
| `followup-email` | 商談・打ち合わせ後のお礼と議事確認・ネクストアクションを送る（600字以内） | `references/` + `assets/` |
| `weekly-report` | KPIデータを経営陣・上長向けの週次サマリーに変換する（300字以内） | `references/` + `assets/` |
| `proposal-outline` | PREP法に基づく5〜7章構成の提案書アウトラインを生成する | `references/` + `assets/` |
| `competitor-summary` | 競合比較表・自社の強み弱み・推奨アクションをまとめる | `references/` + `assets/` |

★ = 研修のハンズオンで出発点として紹介する3本

### 使い方

`.opencode/skills/` の中身を、OpenCode が読み込むフォルダにコピーします。

```
~/.config/opencode/skills/<スキル名>/
```

OpenCode は起動時にこのフォルダを自動でスキャンするため、
置くだけで指示の内容に応じて適切なスキルが選ばれます。

---

## フォルダの使い分け

| フォルダ | 用途 | 特徴 |
|---|---|---|
| `references/` | エージェントが読んで理解するドキュメント | ルール・定義・判断基準。出力物そのものにはならない |
| `assets/` | エージェントが使う素材・雛形 | コピーして穴埋めするテンプレート。出力の一部になる |
| `scripts/` | エージェントが実行するスクリプト | データ整形・バリデーションなど処理を自動化する |
