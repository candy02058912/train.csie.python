"""
title: 練習題 028：封裝製作飲料流程
score: 1
quest_html: 在程式的世界裡，呼叫函式就像是「點餐」，而 <code>return</code> 就像是吧台「出餐」把做好的飲料交到你手上。<br><br><b>任務需求：</b><br>1. 定義一個函式，命名為 <code>make_drink</code>。<br>2. 此函式接收三個參數：<code>name</code>, <code>sugar</code>, <code>ice</code>。<br>3. 在函式內部，請使用 <code>return</code> 回傳這條字串：<code-snippet>飲料做好了！這是您的 {name} ({sugar}/{ice})</code-snippet><br>4. 在函式的<b>外面</b>，練習呼叫這個函式兩次，並用 <code>print()</code> 將回傳的結果印出來：<br>第一杯：<code-snippet>"珍珠奶茶", "半糖", "少冰"</code-snippet><br>第二杯：<code-snippet>"四季春", "無糖", "去冰"</code-snippet>
"""

# ==== STARTER CODE ====


# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查
        tree = ast.parse(studentCode)
        has_func = False
        has_return = False
        arg_count = 0
        call_count = 0
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "make_drink":
                has_func = True
                arg_count = len(node.args.args)
                # 檢查函式內是否有 return
                for subnode in ast.walk(node):
                    if isinstance(subnode, ast.Return):
                        has_return = True
            
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == "make_drink":
                    call_count += 1
        
        if not has_func:
            return "❌ 任務失敗！你必須定義一個名為 `make_drink` 的函式。"
        
        if not has_return:
            return "❌ 任務失敗！函式內部必須使用 `return` 回傳結果，而不是直接印出喔！"

        if arg_count != 3:
            return f"❌ 任務失敗！函式 `make_drink` 需要 3 個參數，但你目前設定了 {arg_count} 個。"
            
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
        'print': print
    }
    output = io.StringIO()
    
    try:
        with contextlib.redirect_stdout(output):
            exec(studentCode, global_env)
        
        # 1. 驗證函式執行結果
        if "make_drink" not in global_env:
             return "❌ 找不到 `make_drink` 函式。"
             
        test_res = global_env["make_drink"]("測試飲料", "微糖", "去冰")
        expected_test = "飲料做好了！這是您的 測試飲料 (微糖/去冰)"
        if test_res != expected_test:
            return f"❌ 函式回傳內容不正確。\n[預期回傳]：{expected_test}\n[你的回傳]：{test_res}"

        # 2. 驗證 Console 輸出
        actual_output = output.getvalue().strip()
        actual_lines = [line.strip() for line in actual_output.split("\n") if line.strip()]
        
        expected_outputs = [
            "飲料做好了！這是您的 珍珠奶茶 (半糖/少冰)",
            "飲料做好了！這是您的 四季春 (無糖/去冰)"
        ]
        
        if len(actual_lines) < 2:
            return "❌ 測試失敗！你沒有在外面使用 `print()` 印出兩次結果。"
            
        if actual_lines[-2:] != expected_outputs and actual_lines != expected_outputs:
             return (
                 f"❌ Console 內容不正確。\n\n"
                 f"[預期應該是]：\n" + "\n".join(expected_outputs) + "\n\n"
                 f"[你的輸出是]：\n" + "\n".join(actual_lines)
             )
        
    except Exception as e:
        return f"❌ 執行錯誤：{str(e)}"
            
    return "SUCCESS"
