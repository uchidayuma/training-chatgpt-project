#!/usr/bin/env python3
"""
KPIデータをマークダウン表形式に変換するスクリプト。
エージェントがweekly-reportスキルで週次レポートを作成する際に使用する。

使い方:
    python format-report.py
    # 起動後、プロンプトに従ってKPIデータを入力する
"""

def calc_ratio(actual, target):
    if target and target != 0:
        return f"{actual / target * 100:.1f}%"
    return "目標値未設定"

def calc_wow(actual, prev):
    if prev and prev != 0:
        diff = (actual - prev) / prev * 100
        sign = "+" if diff >= 0 else ""
        return f"{sign}{diff:.1f}%"
    return "前週データなし"

def format_kpi_table(kpi_list):
    header = "| 指標 | 実績値 | 目標比 | 前週比 | コメント |"
    sep    = "|---|---|---|---|---|"
    rows = [header, sep]
    for item in kpi_list:
        name    = item.get("name", "")
        actual  = item.get("actual", 0)
        target  = item.get("target")
        prev    = item.get("prev")
        comment = item.get("comment", "")
        rows.append(
            f"| {name} | {actual} | {calc_ratio(actual, target)} "
            f"| {calc_wow(actual, prev)} | {comment} |"
        )
    return "\n".join(rows)

def main():
    print("=== KPIレポート整形スクリプト ===")
    print("KPI指標を順番に入力してください。入力を終えるには空白のままEnterを押してください。\n")

    kpi_list = []
    while True:
        name = input("指標名（例：売上、受注件数）: ").strip()
        if not name:
            break
        actual = float(input(f"  {name} の実績値: "))
        target_str = input(f"  {name} の目標値（不明なら空白）: ").strip()
        prev_str   = input(f"  {name} の前週実績（不明なら空白）: ").strip()
        comment    = input(f"  コメント（任意）: ").strip()
        kpi_list.append({
            "name":    name,
            "actual":  actual,
            "target":  float(target_str) if target_str else None,
            "prev":    float(prev_str)   if prev_str   else None,
            "comment": comment,
        })
        print()

    if not kpi_list:
        print("データが入力されませんでした。")
        return

    print("\n--- 生成されたマークダウン表 ---\n")
    print(format_kpi_table(kpi_list))

if __name__ == "__main__":
    main()
