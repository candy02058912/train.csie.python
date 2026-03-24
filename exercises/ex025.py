"""
title: 練習題 025：飲料訂單
score: 1
quest_html: 在現代的 Python (3.7 版本以上) 中，字典 (Dictionary) 是<b>「有序的」</b>，這代表你「先加進去的資料，用迴圈拿出來的時候也會在前面」！<br><br>我們來幫飲料店處理訂單吧！<br><br><b>任務需求：</b><br>1. 依序將這三筆資料加入 <code>orders</code> 字典中：<br> - key: <code-snippet>Alice</code-snippet>, value: <code-snippet>珍奶</code-snippet><br> - key: <code-snippet>Bob</code-snippet>, value: <code-snippet>綠茶</code-snippet><br> - key: <code-snippet>Candy</code-snippet>, value: <code-snippet>烏龍茶</code-snippet><br>2. 老闆想知道有哪些人點飲料。請用 <b><code>for</code> 迴圈</b> 走訪字典的 <b>key</b> 並逐一印出人名。<br>3. 負責泡飲料的店員想知道要做哪些飲料。請用 <b><code>.values()</code></b> 走訪字典的 <b>value</b> 並逐一印出飲料名。<br>4. 最後做訂單總覽。請用 <b><code>.items()</code></b> 走訪字典的 <b>key 和 value</b>，並逐一印出：<code-snippet>{人名} 點了 {飲料}</code-snippet>
"""

# ==== STARTER CODE ====
orders = {}

# 1. 依序新增三筆訂單 (Alice, Bob, Candy)


# 2. 使用 for ... in orders: 逐一印出人名 (key)


# 3. 使用 for ... in orders.values(): 逐一印出飲料 (value)


# 4. 使用 for ... in orders.items(): 逐一印出 "{人名} 點了 {飲料}"


# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查
        tree = ast.parse(studentCode)
        for_count = 0
        has_values_call = False
        has_items_call = False
        
        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                for_count += 1
            
            # Check for .values() and .items()
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr == 'values':
                    has_values_call = True
                elif node.func.attr == 'items':
                    has_items_call = True

        if for_count < 3:
            return "❌ 任務失敗！請確保你至少寫了三個 `for` 迴圈來完成步驟 2, 3, 4。"
        if not has_values_call:
            return "❌ 任務失敗！步驟 3 必須使用 `orders.values()` 來取得所有飲料。"
        if not has_items_call:
            return "❌ 任務失敗！步驟 4 必須使用 `orders.items()` 來同時取得人名和飲料。"
            
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
        
        # 1. 檢查 orders 字典的內容和順序
        if "orders" not in global_env:
            return "❌ 找不到變數 `orders`，請確認沒有刪掉原本的變數。"
            
        final_orders = global_env["orders"]
        expected_dict = {"Alice": "珍奶", "Bob": "綠茶", "Candy": "烏龍茶"}
        
        if final_orders != expected_dict:
            return f"❌ 第一步新增訂單失敗。\n\n[預期字典內容]：\n{expected_dict}\n\n[你的字典內容]：\n{final_orders}"
            
        # 在 Python 3.7+ 中，轉成 list 的 key 順序必須就是插入順序
        if list(final_orders.keys()) != ["Alice", "Bob", "Candy"]:
            return "❌ 字典的順序不對！請確保你是按照 Alice -> Bob -> Candy 的順序把資料放進去喔！"
        
        # 2. 檢查 Print 輸出
        captured = output.getvalue().strip()
        actual_lines = [line.strip() for line in captured.split("\n") if line.strip()]
        
        expected_outputs = [
            "Alice", "Bob", "Candy",          # Step 2
            "珍奶", "綠茶", "烏龍茶",            # Step 3
            "Alice 點了 珍奶",                  # Step 4
            "Bob 點了 綠茶",
            "Candy 點了 烏龍茶"
        ]
        
        if actual_lines != expected_outputs:
             return (
                 f"❌ Console 輸出不正確\n\n"
                 f"請確認你迴圈印出的順序與內容是否完全符合步驟。\n"
                 f"[預期的順序應該是]：\n" + "\n".join(expected_outputs) + "\n\n"
                 f"[你的實際輸出]：\n" + "\n".join(actual_lines)
             )
    except Exception as e:
        return f"❌ 執行錯誤：{str(e)}"
            
    return "SUCCESS"
