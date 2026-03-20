"""
title: 練習題 022：出門檢查清單
score: 1
quest_html: 學會了如何建立串列 (List) 之後，最常見的操作就是用 <b><code>for</code> 迴圈</b> 把裡面的東西一個一個拿出來處理。<br><br><b>任務需求：</b><br>系統已經幫你準備好了一個出門必備物品清單 <code>items</code>。<br>請使用 <b><code>for</code> 迴圈</b> 遍歷 (逐一讀取) 這個清單，並依序印出：<br><code-snippet>記得帶{項目}！</code-snippet><br><br><b>預期輸出結果：</b><br>記得帶手機！<br>記得帶鑰匙！<br>記得帶錢包！<br>記得帶悠遊卡！
"""

# ==== STARTER CODE ====
items = ["手機", "鑰匙", "錢包", "悠遊卡"]

# 請使用 for 迴圈逐一印出提醒文字



# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查
        tree = ast.parse(studentCode)
        has_for = False
        has_list_ref = False
        
        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                has_for = True
                # Check if it iterates over 'items'
                if isinstance(node.iter, ast.Name) and node.iter.id == 'items':
                    has_list_ref = True
                
        if not has_for:
            return "❌ 任務失敗！偵測不到 `for` 迴圈。這一題要練習用 `for ... in ...` 喔！"
        if not has_list_ref:
            return "❌ 任務失敗！你的 `for` 迴圈似乎沒有在讀取 `items` 清單。"
            
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
        
        captured = output.getvalue().strip()
        actual_lines = [line.strip() for line in captured.split("\n") if line.strip()]
        
        expected_outputs = [
            "記得帶手機！",
            "記得帶鑰匙！",
            "記得帶錢包！",
            "記得帶悠遊卡！"
        ]
        
        if actual_lines != expected_outputs:
             return (
                 f"❌ 輸出內容不正確\n\n"
                 f"[系統預期的對話]：\n" + "\n".join(expected_outputs) + "\n\n"
                 f"[你的實際輸出]：\n" + "\n".join(actual_lines) + "\n\n"
                 f"📝 提醒：請檢查字體是否完全一致（包含驚嘆號）。"
             )
    except Exception as e:
        return f"❌ 執行錯誤：{str(e)}"
            
    return "SUCCESS"
