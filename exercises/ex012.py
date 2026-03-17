"""
title: 練習題 012：旅日預算換算器
score: 1
quest_html: 準備去日本旅遊嗎？讓我們練習如何處理多行字串與數值格式化！<br><br><b>任務需求：</b><br>1. 題目提供了兩個<b>字串 (str)</b> 變數：<code>twd_budget_str</code> (台幣預算) 與 <code>exchange_rate_str</code> (日圓匯率)。<br>2. 請將這兩個變數轉換為<b>浮點數 (float)</b>。<br>3. 計算換算後的日圓金額，存入變數 <code>jpy_amount</code> (計算方式：台幣除以匯率)。<br><br><b>注意：</b>起始的程式碼已提供一個多行 f-string 輸出模板（包含小數點兩位格式 <code>:.2f</code>），請勿更動模板內容，只需完成計算邏輯即可。預期輸出為：<br><code-snippet>--------------------<br>旅日預算換算結果<br>--------------------<br>您的台幣預算：10000 元<br>換算後的日幣：47619.05 円<br>--------------------</code-snippet>
"""

# ==== STARTER CODE ====
twd_budget_str = "10000"
exchange_rate_str = "0.21"

# 請在此處開始寫你的程式碼 (記得要開一個 jpy_amount 的變數唷！)


# 請勿更動下方程式碼
print(f"""\
--------------------
旅日預算換算結果
--------------------
您的台幣預算：{twd_budget_str} 元
換算後的日幣：{jpy_amount:.2f} 円
--------------------\
""")


# ==== TEST CODE ====
import sys

def run_tests():
    # 本題測試邏輯：檢查變數型別與計算結果
    try:
        # 1. 檢查必要的變數
        required_vars = ['jpy_amount']
        for var in required_vars:
            if var not in globals():
                return f"❌ 找不到變數 `{var}`，請確保你有正確命名並賦值。"

        # 2. 定義預期結果
        val_twd = float(twd_budget_str)
        val_rate = float(exchange_rate_str)
        expected_jpy = val_twd / val_rate
        expected_line = "-" * 20
        
        # 3. 驗證變數結果
        if abs(jpy_amount - expected_jpy) > 0.01:
             return f"❌ 日幣金額計算不正確。\n\n[提示]：請確認你使用的是除法 (`/`) 且型別轉換正確。"

        # 4. 檢查輸出內容 (嚴格比對多行格式)
        # 注意：多行 f-string 的換行符號需與 print 內容完全一致
        # 利用 student 所跑出的 jpy_amount 來格式化 expected
        expected_receipt = (
            f"{expected_line}\n"
            f"旅日預算換算結果\n"
            f"{expected_line}\n"
            f"您的台幣預算：{twd_budget_str} 元\n"
            f"換算後的日幣：{jpy_amount:.2f} 円\n"
            f"{expected_line}"
        )
        
        captured_output = sys.stdout.get_value().strip()
        cleaned_captured = "\n".join([line.rstrip() for line in captured_output.split("\n")])

        if cleaned_captured == expected_receipt:
            return "SUCCESS"
        else:
            return (
                f"❌ Console 輸出格式不完全正確。\n\n"
                f"[系統預其內容為]：\n{expected_receipt}\n\n"
                f"[你的實際輸出]：\n{captured_output}\n\n"
                f"[提示]：請確保你沒有動到原本提供的 print 模板內容。"
            )
            
    except Exception as e:
        return f"❌ 測試系統執行時發生錯誤：{str(e)}"
