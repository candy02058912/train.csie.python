"""
title: 練習題 014：手機電量警報器
score: 1
quest_html: 你的手機快沒電了嗎？讓我們用語法 <code>if / elif / else</code> 寫一個電量判斷系統！<br><br><b>任務需求：</b><br>1. 程式會先使用 <code>input()</code> 詢問目前電量，請記得將輸入的字串轉為<b>整數 (int)</b>，並存入變數 <code>battery</code> 中。<br>2. 請使用 <code>if</code>、<code>elif</code> 與 <code>else</code> 來判斷 <code>battery</code> 的數值，並 <b><code>print()</code></b> 出對應的訊息：<br>&nbsp;&nbsp;&nbsp;&nbsp;🔋 如果大於等於 <b>80</b>： 印出 <code-snippet>電量充足！</code-snippet><br>&nbsp;&nbsp;&nbsp;&nbsp;🔋 如果大於等於 <b>40</b>： 印出 <code-snippet>電量正常。</code-snippet><br>&nbsp;&nbsp;&nbsp;&nbsp;🔋 如果大於等於 <b>15</b>： 印出 <code-snippet>電量偏低，建議充電。</code-snippet><br>&nbsp;&nbsp;&nbsp;&nbsp;🔋 若都不符合： 印出 <code-snippet>電量極低，即將自動關機...</code-snippet><br><br><b>注意：</b>請確實使用 <code>if</code> 語法，如果只是偷吃步直接 <code>print</code> 答案，測試系統是不會讓你過關的喔！
"""

# ==== STARTER CODE ====
battery = input("請輸入目前電量 (0-100)：")


# ==== TEST CODE ====
import ast
import sys

def run_tests():
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查學生是否有使用 If 敘述
        if 'studentCode' in globals():
            try:
                tree = ast.parse(studentCode)
                has_if = False
                for node in ast.walk(tree):
                    if isinstance(node, ast.If):
                        has_if = True
                        break
                if not has_if:
                    return "❌ 任務失敗！\n\n系統沒有偵測到任何 `if` 判斷式。\n請務必使用 `if`、`elif` 與 `else` 來根據電量印出對應的文字，不能只用 `print()` 偷矇過關喔！😜"
            except SyntaxError as e:
                return f"❌ 語法錯誤：{str(e)}"

        # 1. 檢查變數
        if 'battery' not in globals():
            return "❌ 找不到變數 `battery`，請確保你有將輸入的值轉型並存入。"
            
        student_battery = globals()['battery']
        if type(student_battery) is not int:
            return "❌ `battery` 的型別錯誤，請記得使用 `int()` 進行轉型喔！"

        # 2. 動態決定系統預期輸出的訊息
        expected_msg = ""
        if student_battery >= 80:
            expected_msg = "電量充足！"
        elif student_battery >= 40:
            expected_msg = "電量正常。"
        elif student_battery >= 15:
            expected_msg = "電量偏低，建議充電。"
        else:
            expected_msg = "電量極低，即將自動關機..."
            
        # 3. 檢查 Console 輸出內容
        captured_output = sys.stdout.get_value().strip()
        cleaned_captured = "\n".join([line.rstrip() for line in captured_output.split("\n")])

        if expected_msg in cleaned_captured:
            return "SUCCESS"
        else:
            return (
                f"❌ 判斷與輸出不完全正確 (以電量 {student_battery} 計算)。\n\n"
                f"[系統預其印出]： {expected_msg}\n"
                f"[你的實際輸出]： {captured_output}\n\n"
                f"[提示]：請檢查大於等於 (`>=`) 的判斷邏輯是否正確，以及印出的文字是否有錯字或漏掉標點符號。"
            )

    except Exception as e:
        return f"❌ 測試系統執行時發生錯誤：{str(e)}"
