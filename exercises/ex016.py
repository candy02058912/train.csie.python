"""
title: 練習題 016：火箭發射倒數
score: 1
quest_html: 讓我們用 <code>while</code> 迴圈來寫一個最基礎的火箭發射倒數器吧！這能幫你熟悉迴圈的基本結構。<br><br><b>任務需求：</b><br>1. 系統已經設定了起始秒數變數：<code>timer</code>。<br>2. 請建立一個 <code>while</code> 迴圈，條件是 <code>timer &gt; 0</code>。<br>3. 在迴圈內部：<br>🚀 第一步：用 <code>print()</code> 印出：<code-snippet>倒數：{timer}</code-snippet><br>🚀 第二步：將 <code>timer</code> 減 1 (也就是 <code>timer -= 1</code>)。這是讓迴圈能順利結束的關鍵！<br>4. 當迴圈結束後，印出：<code-snippet>發射！</code-snippet><br><br><b>注意：</b>系統會在背後悄悄把起始 <code>timer</code> 換成不同的數字測試，請確保你的程式碼能通用於不同的秒數。
"""

# ==== STARTER CODE ====
# 這裡設定預設起始秒數為 10
# 送出解答時系統會代入其他起始秒數測試喔！
timer = 10

# 請在下方開始編寫你的 while 迴圈：


# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查學生是否有使用 While 敘述
        tree = ast.parse(studentCode)
        has_while = False
        for node in ast.walk(tree):
            if isinstance(node, ast.While):
                has_while = True
                break
        if not has_while:
            return "❌ 任務失敗！\n\n系統沒有偵測到任何 `while` 迴圈。\n請建立一個 while 迴圈來完成倒數，不能直接用 print 列印出數字偷矇過關喔！😜"
    except SyntaxError as e:
        return f"❌ 語法錯誤：{str(e)}"
        
    # [背景偷偷測試多種情境]
    import io
    import contextlib
    import re

    # 格式：(測試起始倒數, 預期應該印出的結果List)
    test_cases = [
        (4, ["倒數：4", "倒數：3", "倒數：2", "倒數：1", "發射！"]),
        (2, ["倒數：2", "倒數：1", "發射！"])
    ]

    for test_timer, expected_prints in test_cases:
        local_env = {}
        global_env = {'__builtins__': __builtins__}
        output = io.StringIO()
        
        # 使用正則表達式取代學生程式碼中 `timer = ...` 的值
        # 進行動態起始秒數測試
        patched_code = re.sub(
            r"^timer\s*=\s*.*$", 
            f"timer = {test_timer}", 
            studentCode, 
            flags=re.MULTILINE
        )
        
        # 實作無限迴圈防護罩
        safe_code_lines = []
        for line in patched_code.split("\n"):
            safe_code_lines.append(line)
            if "while " in line.strip() and not line.strip().startswith("#"):
                indent = len(line) - len(line.lstrip())
                spaces = " " * (indent + 4)
                safe_code_lines.insert(0, "____loop_guard = 0")
                safe_code_lines.append(f"{spaces}____loop_guard += 1")
                safe_code_lines.append(f"{spaces}if ____loop_guard > 100: raise Exception('無限迴圈防護！倒數超過 100 次，時間似乎停止流動了 😱')")
                
        safe_code = "\n".join(safe_code_lines)
        
        try:
            with contextlib.redirect_stdout(output):
                exec(safe_code, global_env, local_env)
            
            captured = output.getvalue().strip()
            # 濾除所有空行
            actual_lines = [line.strip() for line in captured.split("\n") if line.strip()]
            
            if actual_lines != expected_prints:
                expected_str = "\n".join(expected_prints)
                actual_str = "\n".join(actual_lines)
                
                return (
                    f"❌ 倒數輸出不正確 (系統背景測試起始秒數：{test_timer})\n\n"
                    f"[系統預期的輸出順序應該是]：\n{expected_str}\n\n"
                    f"[你的實際輸出順序是]：\n{actual_str}\n\n"
                    f"📝 提示：請確定你每一次都有印出正確的文字，並且確認 `timer` 每回合都有減 1。"
                )
                
        except Exception as e:
            if "無限迴圈防護" in str(e):
                return "❌ 🚨 系統崩潰警告：引發了無限迴圈！🚨\n\n你的時間永遠停住了！\n這通常是因為你忘記在迴圈裡加上 `timer -= 1`。\n請加在迴圈的最後面，讓 `timer` 每回合都變小！"
            return f"❌ 執行錯誤 (測試起始秒數 {test_timer})：\n{str(e)}"
            
    return "SUCCESS"
