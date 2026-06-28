"""
Usage（使い方）:
  python batch_analyze.py <入力フォルダ> [出力フォルダ]

  入力フォルダ内にある .txt ファイルを全件読み込み、
  survey-analysis スキルの手順に従ってアンケート分析を依頼し、
  結果を出力フォルダに {元ファイル名}_result.md として保存します。

  出力フォルダを省略した場合は、入力フォルダ内の output/ に保存します。

例:
  python batch_analyze.py ./surveys
  python batch_analyze.py ./surveys ./results
"""

import os
import sys
from pathlib import Path


def read_txt_files(input_dir: Path) -> list[tuple[Path, str]]:
    """指定フォルダ内の .txt ファイルをすべて読み込む"""
    files = sorted(input_dir.glob("*.txt"))
    results = []
    for file_path in files:
        try:
            content = file_path.read_text(encoding="utf-8")
            results.append((file_path, content))
        except Exception as e:
            print(f"[エラー] {file_path.name} の読み込みに失敗しました: {e}")
    return results


def build_prompt(survey_text: str, file_name: str) -> str:
    """survey-analysis スキルへの入力プロンプトを構築する"""
    return f"""以下のアンケートテキストを分析してください。

■ 分析対象のアンケートテキスト：
{survey_text}

■ 分類軸：満足度 / 要望 / 不満 / その他
■ 対象サービス・商品名：{file_name}
■ 用途：改善施策検討用

各コメントを「No. | 原文（抜粋） | 分類カテゴリ | 感情スコア」の表形式で整理し、
分類別の件数集計（件数・割合%）と、全体傾向のサマリー（200字以内）を出力してください。
"""


def write_result(output_dir: Path, original_file: Path, result_text: str) -> None:
    """分析結果をMarkdownファイルとして保存する"""
    output_file = output_dir / f"{original_file.stem}_result.md"
    output_file.write_text(result_text, encoding="utf-8")
    print(f"[保存] {output_file}")


def analyze_with_agent(prompt: str) -> str:
    """
    エージェント（AI）にプロンプトを送信して結果を受け取る。
    実際の実行は OpenCode のエージェントが担当する。
    このスクリプトはプロンプトを標準出力に書き出し、エージェントに処理させる。
    """
    # OpenCode 環境では、このスクリプトをエージェントが読み込み、
    # 各ファイルのプロンプトを順次処理する。
    # スタンドアロン実行時は、プロンプトをそのまま返す（デバッグ用）。
    return f"[未処理] 以下のプロンプトをエージェントに渡してください:\n\n{prompt}"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_dir = Path(sys.argv[1])
    if not input_dir.is_dir():
        print(f"[エラー] 入力フォルダが見つかりません: {input_dir}")
        sys.exit(1)

    output_dir = Path(sys.argv[2]) if len(sys.argv) >= 3 else input_dir / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    txt_files = read_txt_files(input_dir)
    if not txt_files:
        print(f"[情報] {input_dir} 内に .txt ファイルが見つかりませんでした。")
        sys.exit(0)

    print(f"[開始] {len(txt_files)} 件のファイルを処理します。出力先: {output_dir}")

    success_count = 0
    error_count = 0

    for file_path, content in txt_files:
        print(f"\n[処理中] {file_path.name}")
        try:
            prompt = build_prompt(content, file_path.stem)
            result = analyze_with_agent(prompt)
            write_result(output_dir, file_path, result)
            success_count += 1
        except Exception as e:
            print(f"[エラー] {file_path.name} の処理中にエラーが発生しました: {e}")
            error_count += 1

    print(f"\n[完了] 成功: {success_count} 件 / エラー: {error_count} 件")
    if error_count > 0:
        print("[確認] エラーが発生したファイルを確認し、再実行してください。")


if __name__ == "__main__":
    main()
