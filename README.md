# Agent Skills サンプル集

Agent Skills のフォルダ構成パターンを学ぶための研修用サンプルです。
5つのスキルが、シンプルな構成からフル活用まで段階的なパターンを示しています。

## スキル一覧

| スキル | 構成 | 学べるパターン |
|---|---|---|
| `complaint-email` | `references/` のみ | 最小構成 |
| `meeting-minutes` | `references/` + `assets/` | 穴埋めテンプレートの使い方 |
| `weekly-report` | `references/` + `scripts/` | 実行スクリプトの使い方 |
| `proposal-doc` | `references/` + `assets/` × 2 | 複数アセットの使い方 |
| `social-media-post` | `references/` + `assets/` + `scripts/` | フル活用パターン |

## フォルダの使い分け

| フォルダ | 用途 | 特徴 |
|---|---|---|
| `references/` | エージェントが読んで理解するドキュメント | ルール・定義・判断基準。出力物そのものにはならない |
| `assets/` | エージェントが使う素材・雛形 | コピーして穴埋めするテンプレート。出力の一部になる |
| `scripts/` | エージェントが実行するスクリプト | データ整形・バリデーションなど処理を自動化する |
