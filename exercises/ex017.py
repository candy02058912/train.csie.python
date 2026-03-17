"""
title: 練習題 017：偶數倒數計時器
score: 1
quest_html: 火箭準備升空！🔥 但通訊設備遇到干擾，<b>只有偶數秒</b>時才能成功發送「倒數訊號」，請寫一個包含 <code>while</code> 迴圈與 <code>if</code> 判斷的倒數計時系統。<br><br><b>任務需求：</b><br>1. 系統已經設定了起始秒數變數：<code>timer</code>。<br>2. 請建立一個 <code>while</code> 迴圈，條件是 <code>timer &gt; 0</code>。<br>3. 在迴圈內部：<br>📡 先使用 <code>if</code> 判斷 <code>timer</code> 是否為偶數（提示：使用餘數運算子 <code>% 2 == 0</code>）。<br>📡 如果是偶數，用 <code>print()</code> 印出：<code-snippet>倒數：{timer}</code-snippet><br>4. <b>【重要關鍵】</b>無論是不是偶數，最後都要記得將 <code>timer</code> 減 1 (即 <code>timer -= 1</code>)，否則時間永遠不會流動，會變成可怕的死當無限迴圈！<br>5. 當跌出迴圈時（即倒數結束），印出最後一發：<code-snippet>發射！</code-snippet><br><br><b>注意：</b>系統會在背後悄悄把起始 <code>timer</code> 換成不同的數字測試，請確認你的判斷邏輯正確。
"""

# ==== STARTER CODE ====
# 這裡設定預設起始秒數為 10
# 送出解答時系統會代入其他起始秒數測試喔！
timer = 10

# 請在下方開始編寫你的 while 迴圈與 if 判斷：




# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查學生是否有使用 While 與 If 敘述
        tree = ast.parse(studentCode)
        has_while = False
        has_if = False
        for node in ast.walk(tree):
            if isinstance(node, ast.While):
                has_while = True
            elif isinstance(node, ast.If):
                has_if = True
                
        if not has_while or not has_if:
            return "❌ 任務失敗！\n\n系統沒有偵測到 `while` 或 `if`。\n請務必結合這兩個語法完成挑戰，不能直接用 print 列印出數字偷矇過關喔！😜"
    except SyntaxError as e:
        return f"❌ 語法錯誤：{str(e)}"
        
    # [背景偷偷測試多種情境]
    import io
    import contextlib
    import re

    # 格式：(測試起始倒數, 預期應該印出的結果List)
    test_cases = [
        (10, ["倒數：10", "倒數：8", "倒數：6", "倒數：4", "倒數：2", "發射！"]),
        (5, ["倒數：4", "倒數：2", "發射！"]),
        (8, ["倒數：8", "倒數：6", "倒數：4", "倒數：2", "發射！"])
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
                safe_code_lines.append(f"{spaces}if ____loop_guard > 500: raise Exception('無限迴圈防護！倒數超過 500 次，時間似乎停止流動了 😱')")
                
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
                    f"📝 提示：\n"
                    f"1. 請檢查 `if` 餘數判斷 (`% 2 == 0`) 是否寫對。\n"
                    f"2. 請確認 `timer -= 1` 有沒有縮排在 `if` 外面、`while` 裡面，否則如果遇到奇數就它永遠不會扣秒數囉！"
                )
                
        except Exception as e:
            if "無限迴圈防護" in str(e):
                return "❌ 🚨 系統崩潰警告：引發了無限迴圈！🚨\n\n你的 `timer` 時間好像停止流亡了！\n這通常是因為你把 `timer -= 1` 的遞減動作包在 `if 偶數:` 判斷裡面了。\n這樣當 `timer` 等於奇數時，它就永遠扣不到血啦！請把它往左退一格縮排，獨立在 `if` 判斷的外面吧！"
            return f"❌ 執行錯誤 (測試起始秒數 {test_timer})：\n{str(e)}"
            
    return "SUCCESS"
