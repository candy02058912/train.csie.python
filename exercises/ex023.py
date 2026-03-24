"""
title: 練習題 023：處理 CSV 資料
score: 1
quest_html: 在真實世界中，常常會拿到用逗號分隔的資料（也就是所謂的 CSV 格式）。這時候字串的 <code>.split()</code> 和 <code>.join()</code> 就會是你的好幫手了！<br><br><b>任務需求：</b><br>1. 系統有一筆飲料訂單字串 <code>order_csv</code>，請用 <b><code>.split(",")</code></b> 以逗號切割，存成一個清單變數 <code>order_list</code>。<br>2. 訂單中含有不必要的空格，請將 <code>order_list</code> 的<b>第三個元素（索引 2）</b>修改為沒有空格的：<code-snippet>微糖</code-snippet><br>3. 我們需要把格式換成用斜線分隔，請用 <b><code>" / ".join(...)</code></b> 將改好的 <code>order_list</code> 重新組合，並存成字串變數 <code>new_format</code>。<br>4. 最後把 <code>new_format</code> 印出來，預期結果為：<br><code-snippet>Alice / 珍奶 / 微糖 / 去冰</code-snippet>
"""

# ==== STARTER CODE ====
order_csv = "Alice,珍奶, 微糖,去冰"

# 請在下方開始編寫你的程式碼


# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查
        tree = ast.parse(studentCode)
        has_split = False
        has_join = False
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr == 'split':
                    has_split = True
                elif node.func.attr == 'join':
                    has_join = True

        if not has_split:
            return "❌ 任務失敗！你必須使用 `split()` 來切割字串。"
        if not has_join:
            return "❌ 任務失敗！你必須使用 `join()` 來重新組合字串。"
            
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
        'order_csv': "Alice,珍奶, 微糖,去冰"
    }
    output = io.StringIO()
    
    try:
        with contextlib.redirect_stdout(output):
            exec(studentCode, global_env)
        
        # 1. 檢查 order_list
        if "order_list" not in global_env:
            return "❌ 找不到變數 `order_list`，請確認你是否有建立此一清單變數。"
            
        final_list = global_env["order_list"]
        expected_list = ["Alice", "珍奶", "微糖", "去冰"]
        
        if final_list != expected_list:
            if final_list == ["Alice", "珍奶", " 微糖", "去冰"]:
                return "❌ `order_list` 的內容未完成修改。記得將第三個元素（也就是索引值 2）的空格去除掉變成 \"微糖\" 喔！"
            return f"❌ `order_list` 內容不正確。\n\n[預期應該是]：\n{expected_list}\n\n[你的答案是]：\n{final_list}"
            
        # 2. 檢查 new_format
        if "new_format" not in global_env:
            return "❌ 找不到變數 `new_format`，請確認你是否有用 `join` 建立此變數。"
            
        if global_env["new_format"] != "Alice / 珍奶 / 微糖 / 去冰":
             return f"❌ `new_format` 字串內容不正確。\n\n[預期應該是]：\nAlice / 珍奶 / 微糖 / 去冰\n\n[你的答案是]：\n{global_env['new_format']}"
             
        # 3. 檢查 Print
        captured = output.getvalue().strip()
        actual_lines = [line.strip() for line in captured.split("\n") if line.strip()]
        
        expected_outputs = ["Alice / 珍奶 / 微糖 / 去冰"]
        
        if len(actual_lines) == 0:
            return "❌ 請記得完成「第 4 步」，把改好格式的訂單印出來喔！"
            
        if actual_lines[-1] != expected_outputs[0]:
             return (
                 f"❌ Console 最後輸出的內容不正確\n"
                 f"請確認你印出的內容是否符合最終結果。\n"
                 f"[預期的輸出]：\n{expected_outputs[0]}\n\n"
                 f"[你的輸出]：\n{actual_lines[-1]}"
             )
    except Exception as e:
        return f"❌ 執行錯誤：{str(e)}"
            
    return "SUCCESS"
