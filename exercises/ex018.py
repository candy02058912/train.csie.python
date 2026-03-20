"""
title: 練習題 018：猜數字
score: 1
quest_html: 終於來到這一步了！我們要用 <code>while</code> 迴圈來寫一個真正的「猜數字」遊戲。程式會一直詢問玩家，直到猜中為止。<br><br><b>任務需求：</b><br>1. 系統已經設定了答案 <code>ans = 42</code>。<br>2. 請建立一個 <b>無限迴圈</b> (<code>while True</code>)。<br>3. 在迴圈內部：<br>🚀 使用 <code>input()</code> 取得玩家輸入，並用 <code>int()</code> 轉換成整數，存入變數 <b><code>guess</code></b>。<br>🚀 根據 <code>guess</code> 與 <code>ans</code> 的關係印出提示：<br>📈 如果 <code>guess > ans</code>，印出：<code-snippet>太大了，再小一點。</code-snippet><br>📉 如果 <code>guess < ans</code>，印出：<code-snippet>太小了，再大一點。</code-snippet><br>🎉 如果 <code>guess == ans</code>，印出：<code-snippet>恭喜你猜中了！</code-snippet>，並執行 <b><code>break</code></b> 跳出迴圈。<br><br><b>💡 提示：</b><br>這是 <code>while</code> 迴圈最經典的用法：當我們不知道確切要跑幾次時，就用 <code>while True</code> 搭配 <code>break</code> 來控制！
"""

# ==== STARTER CODE ====
ans = 42

# 請在下方開始編寫你的 while 迴圈
# 提示：使用 while True: 以及 input()



# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查
        tree = ast.parse(studentCode)
        has_while = False
        has_break = False
        has_input = False
        
        for node in ast.walk(tree):
            if isinstance(node, ast.While):
                has_while = True
            elif isinstance(node, ast.Break):
                has_break = True
            elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'input':
                has_input = True
                
        if not has_while:
            return "❌ 任務失敗！偵測不到 `while` 迴圈。"
        if not has_input:
            return "❌ 任務失敗！這一題需要使用 `input()` 來取得玩家輸入的數字喔！"
        if not has_break:
            return "❌ 任務失敗！猜中答案後，別忘了使用 `break` 離開無限迴圈，否則程式會停不下來！"
            
    except SyntaxError as e:
        return f"❌ 語法錯誤：{str(e)}"
        
    import io
    import contextlib
    import re

    # 模擬測試場景
    # 格式：(正解, 玩家輸入序列, 預期印出的內容清單)
    test_cases = [
        (42, ["30", "50", "42"], ["太小了，再大一點。", "太大了，再小一點。", "恭喜你猜中了！"]),
        (10, ["15", "10"], ["太大了，再小一點。", "恭喜你猜中了！"]),
        (7, ["7"], ["恭喜你猜中了！"])
    ]

    for ans_val, user_inputs, expected_outputs in test_cases:
        output = io.StringIO()
        
        # 準備模擬 input 函式
        input_queue = list(user_inputs)
        def mock_input(prompt=""):
            if not input_queue:
                raise Exception("⚠️ 程式進入無限迴圈或讀取次數超過預期！請檢查 break 邏輯。")
            return input_queue.pop(0)

        # 準備執行環境
        if isinstance(__builtins__, dict):
            builtins_dict = __builtins__.copy()
        else:
            import builtins
            builtins_dict = vars(builtins).copy()

        global_env = {
            '__builtins__': builtins_dict,
            'input': mock_input,
            'int': int,
            'print': print,
            'ans': ans_val
        }

        # 使用正則取代 ans 的值，避免學生程式碼中的固定值覆蓋測試值
        patched_code = re.sub(
            r"^ans\s*=\s*.*$", 
            f"ans = {ans_val}", 
            studentCode, 
            flags=re.MULTILINE
        )

        # 注入無限迴圈防護罩
        safe_code_lines = []
        for line in patched_code.split("\n"):
            safe_code_lines.append(line)
            if "while " in line.strip() and not line.strip().startswith("#"):
                indent = len(line) - len(line.lstrip())
                spaces = " " * (indent + 4)
                safe_code_lines.insert(0, "____loop_guard = 0")
                safe_code_lines.append(f"{spaces}____loop_guard += 1")
                safe_code_lines.append(f"{spaces}if ____loop_guard > 100: raise Exception('無限迴圈防護！執行超過 100 次。')")
        
        safe_code = "\n".join(safe_code_lines)
        
        try:
            with contextlib.redirect_stdout(output):
                exec(safe_code, global_env)
            
            captured = output.getvalue().strip()
            actual_lines = [line.strip() for line in captured.split("\n") if line.strip()]
            
            if actual_lines != expected_outputs:
                return (
                    f"❌ 遊戲邏輯不正確 (測試答案：{ans_val}, 輸入：{', '.join(user_inputs)})\n\n"
                    f"[系統預期的對話]：\n" + "\n".join(expected_outputs) + "\n\n"
                    f"[你的實際輸出]：\n" + "\n".join(actual_lines)
                )
        except Exception as e:
            return f"❌ 執行錯誤 (測試答案 {ans_val})：\n{str(e)}"
            
    return "SUCCESS"
