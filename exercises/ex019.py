"""
title: 練習題 019：實習生闖禍罰寫
score: 1
quest_html: AI 實習生因為又寫出了無限迴圈，被經理處罰要在終端機罰寫「我以後會檢查迴圈終止條件」 10 次...<br><br><b>任務需求：</b><br>1. 系統給定了一個變數 <code>times = 10</code> 代表要罰寫的總次數。<br>2. 請使用 <code>for</code> 迴圈與 <code>range()</code> 函式來建立一個能重複執行 <code>times</code> 次的迴圈。<br>3. 迴圈的計數變數請命名為 <code>i</code>。<br>4. 在迴圈中，使用 <code>print()</code> 印出以下完整字串：<code-snippet>第 X 次：我以後會檢查迴圈終止條件</code-snippet><br><br><b>💡 終極提示 (Zero-Indexing)：</b><br>在 Python 裡，<code>range(10)</code> 產生的數字是從 <b>0</b> 開始的 (0, 1, 2... 9)。所以如果你直接印出 <code>{i}</code>，畫面會顯示「第 0 次...」，這並不符合人類的閱讀習慣！<br>因此我們要在印出的時候把變數加上 1，也就是使用 <code>{i+1}</code> 來校正喔！
"""

# ==== STARTER CODE ====
# 給定罰寫次數
times = 10

# 請在下方開始編寫你的 for 迴圈
# 記得要善用 range(times) 喔！



# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查學生是否有使用 For 敘述
        tree = ast.parse(studentCode)
        has_for = False
        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                has_for = True
                break
                
        if not has_for:
            return "❌ 任務失敗！\n\n系統沒有偵測到 `for` 迴圈。\n身為優秀的工程師，請務必使用 `for i in range(...)` 來幫忙實習生完成罰寫，不要手動 print() 10 次，那樣手會很痠的！😜"
    except SyntaxError as e:
        return f"❌ 語法錯誤：{str(e)}"
        
    # [背景偷偷測試多種情境]
    import io
    import contextlib
    import re

    # 準備用來驗證的答案產生器
    def generate_expected(count):
        return [f"第 {x} 次：我以後會檢查迴圈終止條件" for x in range(1, count + 1)]

    # 格式：(測試罰寫次數, 預期的清單)
    test_cases = [
        (10, generate_expected(10)),
        (3, generate_expected(3)),
    ]

    for test_times, expected_prints in test_cases:
        local_env = {}
        global_env = {'__builtins__': __builtins__}
        output = io.StringIO()
        
        # 使用正則取代 `times = 10`
        patched_code = re.sub(
            r"^times\s*=\s*.*$", 
            f"times = {test_times}", 
            studentCode, 
            flags=re.MULTILINE
        )
        
        try:
            with contextlib.redirect_stdout(output):
                exec(patched_code, global_env, local_env)
            
            captured = output.getvalue().strip()
            # 濾除所有空行
            actual_lines = [line.strip() for line in captured.split("\n") if line.strip()]
            
            if actual_lines != expected_prints:
                expected_str = "\n".join(expected_prints)
                actual_str = "\n".join(actual_lines)
                
                return (
                    f"❌ 輸出字串不正確 (系統背景測試罰寫次數：{test_times})\n\n"
                    f"[系統預期的輸出順序應該是]：\n{expected_str}\n\n"
                    f"[你的實際輸出順序是]：\n{actual_str}\n\n"
                    f"📝 提示：\n"
                    f"1. 請檢查 `print` 裡面的字串使否完全複製正確，有沒有漏掉標點符號或打成半形冒號？\n"
                    f"2. 請確認你有使用 `{{i+1}}` 來把計數器加一，否則會跑出「第 0 次」喔！"
                )
                
        except Exception as e:
            return f"❌ 執行錯誤 (測試罰寫次數 {test_times})：\n{str(e)}"
            
    return "SUCCESS"
