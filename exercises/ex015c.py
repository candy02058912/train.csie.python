"""
title: 練習題 015c：冒險者大門
score: 1
quest_html: 這是 <code>if</code> 語法的終極挑戰！你需要同時處理多個條件，並使用<b>邏輯運算子 (and / or)</b>。<br><br><b>任務需求：</b><br>1. 系統設定了兩個變數：剩餘體力 <code>stamina</code> 與是否擁有鑰匙 <code>has_key</code> (True 或 False)。<br>2. 撰寫大門開啟邏輯：<br>🔑 如果體力大於 50 <u>且</u> 擁有鑰匙，印出：<code-snippet>成功使用鑰匙開啟寶庫！</code-snippet><br>🛡️ 否則，如果你體力大於或等於 90，印出：<code-snippet>體力充沛，成功撞破大門！</code-snippet><br>🚫 以上皆非，印出：<code-snippet>大門仍牢牢地鎖著。</code-snippet><br><br><b>💡 注意：</b>所有的 <code>if</code>、<code>elif</code>、<code>else</code> 後面一定要加冒號 <code>:</code>。
"""

# ==== STARTER CODE ====
# 預設數值
stamina = 60
has_key = True

# 請在下方開始寫你的程式碼


# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查
        tree = ast.parse(studentCode)
        has_if = False
        has_elif = False
        has_else = False
        has_logical = False
        
        for node in ast.walk(tree):
            if isinstance(node, ast.If):
                has_if = True
                orelse = node.orelse
                while orelse and len(orelse) == 1 and isinstance(orelse[0], ast.If):
                    has_elif = True
                    orelse = orelse[0].orelse
                if orelse:
                    has_else = True
            elif isinstance(node, ast.BoolOp):
                has_logical = True
                    
        if not (has_if and has_elif and has_else):
             return "❌ 任務失敗！\n\n系統沒偵測到完整的 `if / elif / else` 結構。\n請務必完整實作寶庫開啟、撞門以及失敗這三種情境！"
        if not has_logical:
             return "❌ 任務失敗！\n\n這道題需要使用邏輯運算子 (如 `and`) 來同時檢查體力與鑰匙喔！"
             
    except SyntaxError as e:
        if ":" in str(e) or "expected ':'" in str(e):
            return "❌ 語法錯誤！\n\n冒號 `:` 又消失了嗎？`if` 系列語法的結尾一定要有冒號喔！"
        return f"❌ 語法錯誤：{str(e)}"
        
    import io
    import contextlib
    import re

    test_cases = [
        (60, True, "成功使用鑰匙開啟寶庫！"), # 鑰匙優先
        (95, True, "成功使用鑰匙開啟寶庫！"), # 鑰匙優先 (雖然體力也夠撞門)
        (95, False, "體力充沛，成功撞破大門！"), # 無鑰匙但夠撞門
        (90, False, "體力充沛，成功撞破大門！"), 
        (70, False, "大門仍牢牢地鎖著。"), # 無鑰匙也不夠撞門
        (40, True, "大門仍牢牢地鎖著。") # 有鑰匙但體力不支
    ]

    for s_val, k_val, expected_msg in test_cases:
        local_env = {}
        global_env = {'__builtins__': __builtins__}
        output = io.StringIO()
        
        patched_code = re.sub(
            r"^stamina\s*=\s*.*$", 
            f"stamina = {s_val}", 
            studentCode, 
            flags=re.MULTILINE
        )
        patched_code = re.sub(
            r"^has_key\s*=\s*.*$", 
            f"has_key = {k_val}", 
            patched_code, 
            flags=re.MULTILINE
        )
        
        try:
            with contextlib.redirect_stdout(output):
                exec(patched_code, global_env, local_env)
            
            captured = output.getvalue().strip()
            if expected_msg not in captured:
                return f"❌ Console 內容不正確 (測試體力：{s_val}, 鑰匙：{k_val})\n\n[預期應該看到]：{expected_msg}\n[你的實際輸出]：{captured}"
        except Exception as e:
            return f"❌ 執行錯誤 (測試 {s_val}, {k_val})：\n{str(e)}"
            
    return "SUCCESS"
