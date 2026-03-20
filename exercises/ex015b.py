"""
title: 練習題 015b：分數等級判定
score: 1
quest_html: 這次我們要練習更多的條件分支：<code>if / elif / else</code>！這能幫你同時判斷多個區間。<br><br><b>任務需求：</b><br>1. 系統已經設定了變數 <code>score</code> (代表分數)。<br>2. 撰寫判斷邏輯：<br>🏅 如果 <code>score &gt;= 90</code>，印出：<code-snippet>表現優秀！</code-snippet><br>🆗 如果 <code>score &gt;= 60</code> (且小於 90)，印出：<code-snippet>及格了。</code-snippet><br>🆘 否則 (小於 60)，印出：<code-snippet>還要加油喔。</code-snippet><br><br><b>💡 小撇步：</b>別忘了 <code>if</code>、<code>elif</code> 和 <code>else</code> 那三行後面都要各加一個冒號 <code>:</code> 喔！
"""

# ==== STARTER CODE ====
# 預設分數為 85
score = 85

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
        (95, "表現優秀！"),
        (90, "表現優秀！"),
        (75, "及格了。"),
        (60, "及格了。"),
        (40, "還要加油喔。")
    ]

    for score_val, expected_msg in test_cases:
        local_env = {}
        global_env = {'__builtins__': __builtins__}
        output = io.StringIO()
        
        patched_code = re.sub(
            r"^score\s*=\s*.*$", 
            f"score = {score_val}", 
            studentCode, 
            flags=re.MULTILINE
        )
        
        try:
            with contextlib.redirect_stdout(output):
                exec(patched_code, global_env, local_env)
            
            captured = output.getvalue().strip()
            if expected_msg not in captured:
                return f"❌ Console 內容不正確 (測試分數：{score_val})\n\n[預期應該看到]：{expected_msg}\n[你的實際輸出]：{captured}"
        except Exception as e:
            return f"❌ 執行錯誤 (測試分數 {score_val})：\n{str(e)}"
            
    return "SUCCESS"
