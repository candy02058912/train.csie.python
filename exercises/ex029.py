"""
title: 練習題 029：吧台忙碌程度檢查
score: 1
quest_html: 店長想知道今天的產能如何。我們有一份 <code>order_counts</code> 清單，紀錄了每一張訂單點了幾杯飲料。請寫一個函式幫店長加總總杯數，並根據多寡判斷忙碌狀態。<br><br><b>任務需求：</b><br>1. 定義函式 <code>check_workload</code>，接收一個參數 <code>counts_list</code>。<br>2. 函式內部：<br>   - 使用 <b><code>for</code> 迴圈</b> 把 <code>counts_list</code> 所有的數字加總起來，存入變數 <code>total</code>。<br>   - <b>如果 <code>total</code> 大於等於 15</b>：<code>return</code> 字串 <code-snippet>今天超忙的！總量有 {total} 杯</code-snippet><br>   - <b>否則</b>：<code>return</code> 字串 <code-snippet>今天還可以，總量有 {total} 杯</code-snippet><br>3. 在函式的<b>外面</b>，呼叫函式並帶入 <code>order_counts</code>，然後用 <b><code>print()</code></b> 印出回傳的結果。
"""

# ==== STARTER CODE ====
order_counts = [3, 5, 2, 1, 8]

# 請在此處開始你的程式碼


# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查
        tree = ast.parse(studentCode)
        has_func = False
        has_for = False
        has_if = False
        has_return = False
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "check_workload":
                has_func = True
                for subnode in ast.walk(node):
                    if isinstance(subnode, ast.For):
                        has_for = True
                    if isinstance(subnode, ast.If):
                        has_if = True
                    if isinstance(subnode, ast.Return):
                        has_return = True
        
        if not has_func:
            return "❌ 任務失敗！你必須定義一個名為 `check_workload` 的函式。"
        if not has_for:
            return "❌ 任務失敗！函式內部必須使用 `for` 迴圈來加總數字。"
        if not has_if:
            return "❌ 任務失敗！函式內部必須使用 `if / else` 來判斷忙碌程度。"
        if not has_return:
            return "❌ 任務失敗！函式內必須使用 `return` 回傳結果文字。"
            
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
        'order_counts': [3, 5, 2, 1, 8]
    }
    output = io.StringIO()
    
    try:
        with contextlib.redirect_stdout(output):
            exec(studentCode, global_env)
        
        # 1. 驗證函式邏輯 (偷偷帶入多組測試情境)
        fn = global_env.get("check_workload")
        if not fn: return "❌ 找不到 `check_workload` 函式。"
        
        test_scenarios = [
            ([1, 2, 3], "今天還可以，總量有 6 杯"),
            ([10, 5], "今天超忙的！總量有 15 杯"),
            ([10, 10, 10], "今天超忙的！總量有 30 杯"),
            ([0], "今天還可以，總量有 0 杯")
        ]
        
        for inp, expected in test_scenarios:
            try:
                actual = fn(inp)
                if actual != expected:
                    return f"❌ 函式邏輯測試失敗！\n\n[測試輸入]：{inp}\n[預期回傳]：{expected}\n[你的回傳]：{actual}"
            except Exception as e:
                return f"❌ 函式執行測試時出錯 (輸入：{inp})：{str(e)}"

        # 2. 驗證 Console 輸出
        actual_output = output.getvalue().strip()
        actual_lines = [line.strip() for line in actual_output.split("\n") if line.strip()]
        
        expected_line = "今天超忙的！總量有 19 杯"
        
        if not actual_lines:
            return "❌ 測試失敗！你沒有使用 `print()` 印出結果。"
            
        if expected_line not in actual_lines:
             return (
                 f"❌ Console 內容不正確。請檢查你加總後的輸出格式是否完全一致。\n\n"
                 f"（提示：order_counts 加總後應該是 19）\n\n"
                 f"[預期應該包含]：\n{expected_line}\n\n"
                 f"[你的輸出是]：\n" + "\n".join(actual_lines)
             )
        
    except Exception as e:
        return f"❌ 執行錯誤：{str(e)}"
            
    return "SUCCESS"
