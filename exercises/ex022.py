"""
title: 練習題 022：出門檢查清單
score: 1
quest_html: 學會了如何建立串列 (List) 之後，最常見的操作就是用 <b><code>for</code> 迴圈</b> 把裡面的東西一個一個拿出來處理。<br><br><b>任務需求：</b><br>1. 使用 <b><code>for</code> 迴圈</b> 印出：<code-snippet>記得帶{項目}！</code-snippet><br>2. 使用 <b>list comprehension</b> 建立 <code>reminders</code> 清單，內容格式為：<code-snippet>已帶{項目}</code-snippet><br>3. 印出 <code>reminders</code>，預期會看到：<br><code>['已帶手機', '已帶鑰匙', '已帶錢包', '已帶悠遊卡']</code>
"""

# ==== STARTER CODE ====
items = ["手機", "鑰匙", "錢包", "悠遊卡"]

# 1. 使用 for 迴圈印出提醒文字


# 2. 使用 list comprehension 建立新清單 reminders


# 3. 印出 reminders 變數


# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查
        tree = ast.parse(studentCode)
        has_for = False
        has_list_comp = False
        
        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                has_for = True
            
            if isinstance(node, ast.ListComp):
                has_list_comp = True
                
        if not has_for:
            return "❌ 任務失敗！偵測不到 `for` 迴圈。這一題也要練習用 `for ... in ...` 喔！"
        if not has_list_comp:
            return "❌ 任務失敗！偵測不到 list comprehension (例如：`[... for x in ... ]`)。"
            
    except SyntaxError as e:
        return f"❌ 語法錯誤：{str(e)}"
        
    import io
    import contextlib

    # 準備執行環境
    if isinstance(__builtins__, dict):
        builtins_dict = __builtins__.copy()
    else:
        import builtins
        builtins_dict = vars(builtins).copy()

    global_env = {
        '__builtins__': builtins_dict,
        'print': print,
        'items': ["手機", "鑰匙", "錢包", "悠遊卡"]
    }
    output = io.StringIO()
    
    try:
        with contextlib.redirect_stdout(output):
            exec(studentCode, global_env)
        
        # 1. 檢查 for 迴圈輸出
        captured = output.getvalue().strip()
        actual_lines = [line.strip() for line in captured.split("\n") if line.strip()]
        
        expected_for_output = [
            "記得帶手機！",
            "記得帶鑰匙！",
            "記得帶錢包！",
            "記得帶悠遊卡！"
        ]
        
        # 2. 檢查 reminders 清單
        if "reminders" not in global_env:
            return "❌ 找不到變數 `reminders`，請使用 list comprehension 建立它。"
        
        expected_reminders = ["已帶手機", "已帶鑰匙", "已帶錢包", "已帶悠遊卡"]
        if global_env["reminders"] != expected_reminders:
            return f"❌ `reminders` 清單內容不正確。\n\n[預期應該是]：\n{expected_reminders}\n\n[你的答案是]：\n{global_env['reminders']}"
            
        # 3. 檢查最後一行的輸出是否包含印出的 reminders
        expected_str1 = str(expected_reminders)
        expected_str2 = expected_str1.replace("'", '"')

        if not actual_lines:
            return "❌ 找不到任何輸出，請確保有使用 `print()` 函式印出結果。"

        if actual_lines[-1] not in (expected_str1, expected_str2):
            if actual_lines[-1] == expected_for_output[-1]:
                return "❌ 任務失敗！你好像只有完成前半部的迴圈輸出。請記得在最後面加上 `print(reminders)` 印出清單。"
            else:
                return f"❌ 任務失敗！最後一行的輸出不是預期的 `reminders` 清單。\n\n[預期應該是]：\n{expected_reminders}\n\n[你的答案是]：\n{actual_lines[-1]}"
        
    except Exception as e:
        return f"❌ 執行錯誤：{str(e)}"
            
    return "SUCCESS"
