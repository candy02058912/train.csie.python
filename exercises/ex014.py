"""
title: 練習題 014：手機電量警報器
score: 1
quest_html: 你的手機快沒電了嗎？讓我們用語法 <code>if / elif / else</code> 寫一個電量判斷系統！<br><br><b>任務需求：</b><br>1. 程式會先使用 <code>input()</code> 詢問目前電量，請記得將輸入的字串轉為<b>整數 (int)</b>，並存入變數 <code>battery</code> 中。<br>2. 請使用 <code>if</code>、<code>elif</code> 與 <code>else</code> 來判斷 <code>battery</code> 的數值，並 <b><code>print()</code></b> 出對應的訊息：<br>🔋 如果大於等於 <b>80</b>，印出：<code-snippet>電量充足！</code-snippet><br>🔋 如果大於等於 <b>40</b>，印出： <code-snippet>電量正常。</code-snippet><br>🔋 如果大於等於 <b>15</b>，印出： <code-snippet>電量偏低，建議充電。</code-snippet><br>🔋 若都不符合，印出： <code-snippet>電量極低，即將自動關機...</code-snippet>
"""

# ==== STARTER CODE ====
battery = input("請輸入目前電量 (0-100)：")


# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查學生是否有使用 If 敘述
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
        
    # [背景偷偷測試多種情境]
    import io
    import contextlib

    test_cases = [
        ("85", "電量充足！"),
        ("80", "電量充足！"),
        ("50", "電量正常。"),
        ("40", "電量正常。"),
        ("20", "電量偏低，建議充電。"),
        ("15", "電量偏低，建議充電。"),
        ("5", "電量極低，即將自動關機...")
    ]

    for test_input, expected_msg in test_cases:
        local_env = {}
        # 覆寫 input 函數來模擬使用者輸入
        def mock_input(prompt=""):
            return test_input
            
        global_env = {'__builtins__': __builtins__, 'input': mock_input}
        output = io.StringIO()
        
        try:
            with contextlib.redirect_stdout(output):
                exec(studentCode, global_env, local_env)
            
            captured = output.getvalue().strip()
            cleaned = "\n".join([line.rstrip() for line in captured.split("\n")])
            
            if expected_msg not in cleaned:
                return (
                    f"❌ 判斷與輸出不完全正確 (系統在背景偷偷測試電量 {test_input})。\n\n"
                    f"[系統預期包含]： {expected_msg}\n"
                    f"[你的實際輸出]： {captured}\n\n"
                    f"[提示]：請檢查大於等於 (`>=`) 的判斷邏輯是否正確，以及印出的文字是否有錯字或漏掉標點符號。"
                )
        except ValueError:
            return f"❌ 執行錯誤：在測試電量 '{test_input}' 時發生 ValueError。\n請確定你有正確使用 `int()` 把 `input` 轉換為整數喔！"
        except Exception as e:
            return f"❌ 執行錯誤 (測試電量 {test_input})：\n{type(e).__name__}: {str(e)}"
            
    return "SUCCESS"
