"""
title: 練習題 015b：猜數字 (前置)
score: 1
quest_html: 這次我們要來玩猜數字！雖然還沒有學會讓程式一直跑的迴圈 (loop)，但我們可以先練習「猜一次」的判斷邏輯。<br>系統已經設定好了一個答案 <code>ans</code> 還有你猜的數字 <code>guess</code>。<br><br><b>任務需求：</b><br>1. 系統已經設定了變數 <code>ans</code> (正確答案) 和 <code>guess</code> (你猜的數字)。<br>2. 撰寫判斷邏輯：<br>📈 如果 <code>guess > ans</code>，印出：<code-snippet>太大了，再小一點。</code-snippet><br>📉 如果 <code>guess < ans</code>，印出：<code-snippet>太小了，再大一點。</code-snippet><br>🎉 否則 (代表猜中了)，印出：<code-snippet>恭喜你猜中了！</code-snippet><br><br><b>💡 小撇步：</b>別忘記 <code>if</code> 和 <code>elif</code> 後面要接條件，最後的 <code>else</code> 不需要條件，且這三行後面都要加冒號 <code>:</code>！
"""

# ==== STARTER CODE ====
# 答案是 42，你猜 30
ans = 42
guess = 30

# 請在下方開始寫你的程式碼
    
# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查學生是否有使用 elif 與 else
        tree = ast.parse(studentCode)
        has_if = False
        has_elif = False
        has_else = False
        for node in ast.walk(tree):
            if isinstance(node, ast.If):
                has_if = True
                # Check for nested if in orelse (which represents elif)
                orelse = node.orelse
                while orelse and len(orelse) == 1 and isinstance(orelse[0], ast.If):
                    has_elif = True
                    orelse = orelse[0].orelse
                if orelse:
                    has_else = True
                break
        
        if not has_if or not has_elif or not has_else:
            return "❌ 任務失敗！\n\n系統沒偵測到完整的 `if / elif / else` 結構。\n請務必依照題目流程完成所有區間的判斷喔！"
    except SyntaxError as e:
        if ":" in str(e) or "expected ':'" in str(e):
            return "❌ 語法錯誤！\n\n檢查一下是不是漏掉冒號 `:` 了？每個判斷條件與 `else` 的結尾都需要冒號喔！"
        return f"❌ 語法錯誤：{str(e)}"
        
    import io
    import contextlib
    import re

    test_cases = [
        (42, 42, "恭喜你猜中了！"),
        (42, 50, "太大了，再小一點。"),
        (42, 30, "太小了，再大一點。")
    ]

    for ans_val, guess_val, expected_msg in test_cases:
        local_env = {}
        global_env = {'__builtins__': __builtins__}
        output = io.StringIO()
        
        # Patch ans AND guess
        patched_code = re.sub(
            r"^ans\s*=\s*.*$", 
            f"ans = {ans_val}", 
            studentCode, 
            flags=re.MULTILINE
        )
        patched_code = re.sub(
            r"^guess\s*=\s*.*$", 
            f"guess = {guess_val}", 
            patched_code, 
            flags=re.MULTILINE
        )
        
        try:
            with contextlib.redirect_stdout(output):
                exec(patched_code, global_env, local_env)
            
            captured = output.getvalue().strip()
            if expected_msg not in captured:
                return f"❌ Console 內容不正確 (測試數字：答案={ans_val}, 你猜={guess_val})\n\n[預期應該看到]：{expected_msg}\n[你的實際輸出]：{captured}"
        except Exception as e:
            return f"❌ 執行錯誤 (測試數字：答案={ans_val}, 你猜={guess_val})：\n{str(e)}"
            
    return "SUCCESS"
