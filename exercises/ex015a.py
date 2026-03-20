"""
title: 練習題 015a：成年檢查器
score: 1
quest_html: 來繼續加強練習 <code>if</code> 語法唷！<br><br><b>任務需求：</b><br>1. 系統已經設定了變數 <code>age</code>。<br>2. 請建立一個 <code>if / else</code> 判斷：<br>✅ 如果 <code>age &gt;= 18</code>，印出：<code-snippet>你已經成年了！</code-snippet><br>❌ 否則，印出：<code-snippet>你還未成年喔。</code-snippet><br><br><b>💡 小撇步：</b>別忘了 <code>if</code> 跟 <code>else</code> 後面都要有冒號 <code>:</code> 喔！
"""

# ==== STARTER CODE ====
# 預設年齡為 20
age = 20

# 請在下方開始寫你的程式碼


# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查學生是否有使用 If 敘述與 Else
        tree = ast.parse(studentCode)
        has_if = False
        has_else = False
        for node in ast.walk(tree):
            if isinstance(node, ast.If):
                has_if = True
                if node.orelse:
                    has_else = True
                break
        if not has_if or not has_else:
            return "❌ 任務失敗！\n\n系統沒有偵測到完整的 `if / else` 結構。\n請務必使用 `else` 來處理未滿 18 歲的情況！"
    except SyntaxError as e:
        if ":" in str(e) or "expected ':'" in str(e):
            return "❌ 語法錯誤！\n\n檢查一下是不是忘記加冒號 `:` 了？`if` 跟 `else` 的結尾都需要各一個冒號喔！"
        return f"❌ 語法錯誤：{str(e)}"
        
    import io
    import contextlib
    import re

    test_cases = [
        (20, "你已經成年了！"),
        (18, "你已經成年了！"),
        (15, "你還未成年喔。")
    ]

    for age_val, expected_msg in test_cases:
        local_env = {}
        global_env = {'__builtins__': __builtins__}
        output = io.StringIO()
        
        patched_code = re.sub(
            r"^age\s*=\s*.*$", 
            f"age = {age_val}", 
            studentCode, 
            flags=re.MULTILINE
        )
        
        try:
            with contextlib.redirect_stdout(output):
                exec(patched_code, global_env, local_env)
            
            captured = output.getvalue().strip()
            if expected_msg not in captured:
                return f"❌ Console 內容不正確 (測試年齡：{age_val})\n\n[預期應該看到]：{expected_msg}\n[你的實際輸出]：{captured}"
        except Exception as e:
            return f"❌ 執行錯誤 (測試年齡 {age_val})：\n{str(e)}"
            
    return "SUCCESS"
