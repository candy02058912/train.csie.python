"""
title: 練習題 019：自動留言審查系統 (字串與 Continue)
score: 1
quest_html: 為了維護網路社群的友善環境，請幫忙寫一個自動留言審查系統！<br>當系統偵測到敏感字眼時，要跳過印出該文字，並發出警告。<br><br><b>任務需求：</b><br>1. 系統設定了一個字串變數 <code>comment = "這部影片太爛了"</code>。<br>2. 請先 <code>print()</code> 出一行提示文字：<code-snippet>--- 系統開始檢查留言 ---</code-snippet><br>3. 使用 <code>for</code> 迴圈遍歷 <code>comment</code> 中的每一個字元，變數名稱請設為 <b><code>char</code></b>。<br>4. 在迴圈內部使用 <code>if</code> 判斷：<br>&nbsp;&nbsp;&nbsp;&nbsp;🚫 如果 <code>char</code> 等於 <b>"爛"</b>，請印出：<code-snippet>🚩 偵測到敏感字眼：[嗶---]</code-snippet>，並執行 <b><code>continue</code></b> 跳過這一回合。<br>5. 在 <code>if</code> 判斷式之後（迴圈內部），正常印出變數 <b><code>char</code></b>。<br><br><b>💡 提示：</b><br><code>continue</code> 會讓程式直接跳回迴圈的開頭，執行下一個字元，因此寫在 <code>continue</code> 下方的 <code>print(char)</code> 就不會被執行到喔！
"""

# ==== STARTER CODE ====
comment = "這部影片太爛了"

print("--- 系統開始檢查留言 ---")

# Step 1: 請使用 for 迴圈
# for ... in ...:

    # Step 2: 判斷如果 char 是敏感字眼 "爛"
    
        # Step 3: 印出警告文字： 🚩 偵測到敏感字眼：[嗶---]
        
        # Step 4: 執行 continue 跳過本次迴圈，不執行後面的列印
        
    
    # Step 5: 如果不是敏感字眼，就正常印出 char



# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查
        tree = ast.parse(studentCode)
        has_for = False
        has_continue = False
        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                has_for = True
            elif isinstance(node, ast.Continue):
                has_continue = True
                
        if not has_for:
            return "❌ 任務失敗！系統沒有偵測到 `for` 迴圈。請用 `for char in comment:` 來檢查喔！"
        if not has_continue:
            return "❌ 任務失敗！這一題的重點是練習使用 `continue` 語法，請務必在偵測到敏感字眼時使用它。"
            
    except SyntaxError as e:
        return f"❌ 語法錯誤：{str(e)}"
        
    # [背景偷偷測試多種情境]
    import io
    import contextlib
    import re

    def get_expected_output(text):
        output = ["--- 系統開始檢查留言 ---"]
        for char in text:
            if char == "爛":
                output.append("🚩 偵測到敏感字眼：[嗶---]")
            else:
                output.append(char)
        return "\n".join(output)

    # 格式：測試字串
    test_cases = [
        "這部影片太爛了",
        "真的爛東西",
        "這影片還不錯"
    ]

    for test_text in test_cases:
        local_env = {}
        global_env = {'__builtins__': __builtins__}
        output = io.StringIO()
        
        # 使用正則取代 `comment = ...`
        patched_code = re.sub(
            r"^comment\s*=\s*.*$", 
            f"comment = '{test_text}'", 
            studentCode, 
            flags=re.MULTILINE
        )
        
        try:
            with contextlib.redirect_stdout(output):
                exec(patched_code, global_env, local_env)
            
            captured = output.getvalue().strip()
            expected = get_expected_output(test_text)
            
            # 清理輸出方便比對
            cleaned_captured = "\n".join([line.strip() for line in captured.split("\n") if line.strip()])
            cleaned_expected = "\n".join([line.strip() for line in expected.split("\n") if line.strip()])
            
            if cleaned_captured != cleaned_expected:
                return (
                    f"❌ 審查輸出不正確 (系統背景測試留言：\"{test_text}\")\n\n"
                    f"[系統預期的輸出]：\n{cleaned_expected}\n\n"
                    f"[你的實際輸出]：\n{cleaned_captured}\n\n"
                    f"📝 提示：請檢查是否有多印或漏印文字，以及 `continue` 是否放在正確的位置。"
                )
                
        except Exception as e:
            return f"❌ 執行錯誤 (測試留言：\"{test_text}\")：\n{str(e)}"
            
    return "SUCCESS"
