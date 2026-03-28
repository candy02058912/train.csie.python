"""
title: 練習題 032：結帳收銀機
score: 1
quest_html: 飲料店在結帳時，系統需要同時算出「原價」與「打九折後的折扣價」。在 Python 中，我們只要在 <code>return</code> 後面用逗號隔開多個變數，就能一次把答案都給出去！呼叫時也可以用多個變數來接收。<br><br><b>任務需求：</b><br>1. 定義函式 <code>calculate_price</code>，接收兩個參數：<code>price</code> (單價) 與 <code>count</code> (數量)。<br>2. 函式內部：<br>   - 算出原價 (price * count)，存入變數 <code>total</code>。<br>   - 算出九折價 (total * 0.9)，存入變數 <code>discount</code>。<br>   - 使用 <code>return</code> 同時回傳這兩個數值（用逗號隔開）。<br>3. 在函式的<b>外面</b>，呼叫 <code>calculate_price(50, 3)</code> 並使用兩個變數同時接收回傳值。<br>4. 使用 <code>print()</code> 印出這兩個變數，預期會看到：<code-snippet>150 135.0</code-snippet>
"""

# ==== STARTER CODE ====
# 1. 在下方定義 calculate_price 函式，回傳兩個數值


# 2. 在外面呼叫函式，並用兩個變數接收回傳值


# 3. 印出這兩個變數


# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：檢查多重回傳與解包
        tree = ast.parse(studentCode)
        has_func = False
        has_multi_return = False
        has_unpacking = False
        
        for node in ast.walk(tree):
            # 檢查函式定義
            if isinstance(node, ast.FunctionDef) and node.name == "calculate_price":
                has_func = True
                for subnode in ast.walk(node):
                    if isinstance(subnode, ast.Return) and isinstance(subnode.value, ast.Tuple):
                        if len(subnode.value.elts) >= 2:
                            has_multi_return = True
            
            # 檢查外界是否有解包賦值
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, (ast.Tuple, ast.List)) and len(target.elts) >= 2:
                        # 檢查是否在呼叫 calculate_price
                        if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == "calculate_price":
                            has_unpacking = True
        
        if not has_func:
            return "❌ 任務失敗！你必須定義一個名為 `calculate_price` 的函式。"
        if not has_multi_return:
            return "❌ 任務失敗！函式內部必須使用 `return a, b` 的格式同時回傳兩個數值。"
        if not has_unpacking:
            return "❌ 任務失敗！呼叫函式時，請練習使用 `x, y = ...` 的語法來接收多個回傳值。"
            
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
        
        # 1. 驗證函式邏輯
        fn = global_env.get("calculate_price")
        if not fn: return "❌ 找不到 `calculate_price` 函式。"
        
        res = fn(100, 2)
        if not isinstance(res, tuple) or len(res) != 2:
            return "❌ 函式回傳格式錯誤，預期應該回傳包含兩個數值的 tuple。"
        if res[0] != 200 or res[1] != 180.0:
            return f"❌ 函式計算邏輯不正確。\n[輸入]：100, 2\n[預計回傳]：(200, 180.0)\n[你的回傳]：{res}"

        # 2. 驗證 Console 輸出
        actual_output = output.getvalue().strip()
        actual_lines = [line.strip() for line in actual_output.split("\n") if line.strip()]
        
        expected_line = "150 135.0"
        
        if not actual_lines:
            return "❌ 測試失敗！你沒有印出結果。"
            
        if expected_line not in actual_lines:
             return (
                 f"❌ Console 內容不正確。請檢查你呼叫函式帶入的參數（應為 50, 3）以及印出的內容。\n\n"
                 f"[預期應該印出]：\n{expected_line}\n\n"
                 f"[你的實際輸出]：\n{actual_lines[-1]}"
             )
        
    except Exception as e:
        return f"❌ 執行錯誤：{str(e)}"
            
    return "SUCCESS"
