#!/usr/bin/env python3
"""
SNS投稿文の文字数をプラットフォーム別にチェックするスクリプト。
エージェントがsocial-media-postスキルで投稿文を作成した後、
文字数制限への適合を確認するために使用する。

使い方:
    python check-length.py
    # 起動後、プロンプトに従って投稿文とプラットフォームを入力する
"""

LIMITS = {
    "x":         {"label": "X（旧Twitter）",  "limit": 140,  "unit": "文字（日本語）"},
    "linkedin":  {"label": "LinkedIn",         "limit": 3000, "unit": "文字"},
    "instagram": {"label": "Instagram",        "limit": 2200, "unit": "文字"},
    "facebook":  {"label": "Facebook",         "limit": 63206,"unit": "文字"},
}

def check(text, platform_key):
    platform = LIMITS.get(platform_key.lower())
    if not platform:
        return None, None, None

    length = len(text)
    limit  = platform["limit"]
    remaining = limit - length
    return platform["label"], length, remaining

def main():
    print("=== SNS投稿文 文字数チェッカー ===\n")

    print("プラットフォームを選んでください:")
    for key, val in LIMITS.items():
        print(f"  {key:<12} → {val['label']}（上限 {val['limit']} {val['unit']}）")
    platform_key = input("\nプラットフォーム: ").strip()

    print("\n投稿文を貼り付けてください（入力終了は空行のみでEnter）:")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    text = "\n".join(lines)

    label, length, remaining = check(text, platform_key)
    if label is None:
        print("エラー: 対応していないプラットフォームです。")
        return

    print(f"\n--- 結果 ---")
    print(f"プラットフォーム: {label}")
    print(f"文字数:           {length} 文字")

    if remaining >= 0:
        print(f"残り文字数:       {remaining} 文字  ✅ 制限内")
    else:
        print(f"超過文字数:       {abs(remaining)} 文字  ❌ 文字数オーバー — 短縮してください")

if __name__ == "__main__":
    main()
