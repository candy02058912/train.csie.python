"""
title: 練習題 031：快速點餐系統
score: 1
quest_html: 吧台很忙，如果客人在點單時沒特別說甜度和冰塊，我們就預設給「全糖 / 正常冰」。在 Python 中，我們可以在定義函式時為參數設定<b>預設值 (Default Parameters)</b>，這樣呼叫時就可以少打一點字囉！<br><br><b>任務需求：</b><br>1. 定義函式 <code>quick_order</code>，接收三個參數：<code>name</code>, <code>sugar</code>, <code>ice</code>。<br>2. 為參數設定預設值：<code>sugar</code> 預設為 <code>"全糖"</code>，<code>ice</code> 預設為 <code>"正常冰"</code>。<br>3. 函式內部：使用 <code>return</code> 回傳如下格式的字串：<br><code-snippet>已下單：{name} ({sugar}/{ice})</code-snippet><br>4. 在函式外面，參考 Starter Code 的測試程式碼印出結果。
"""

# ==== STARTER CODE ====
# 1. 在下方定義 quick_order 函式並設定預設值


# --- 💡 以下測試程式碼請勿修改 ---
try:
    print(quick_order("阿薩姆紅茶"))
    print(quick_order("茉莉綠茶", sugar="無糖"))
    print(quick_order("珍珠奶茶", sugar="微糖", ice="去冰"))
except NameError:
    pass

# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：檢查參數預設值
        tree = ast.parse(studentCode)
        has_func = False
        default_count = 0
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "quick_order":
                has_func = True
                default_count = len(node.args.defaults)
        
        if not has_func:
            return "❌ 任務失敗！你必須定義一個名為 `quick_order` 的函式。"
        
        if default_count < 2:
            return f"❌ 任務失敗！你必須為 `sugar` 與 `ice` 超過兩個以上的參數設定預設值。目前偵測到 {default_count} 個預設值。"
            
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
        fn = global_env.get("quick_order")
        if not fn: return "❌ 找不到 `quick_order` 函式。"
        
        # 測試 1: 只帶名稱
        res1 = fn("紅茶")
        if res1 != "已下單：紅茶 (全糖/正常冰)":
            return f"❌ 預設值邏輯錯誤：當只輸入名稱時，回傳不正確。\n[預期]：已下單：紅茶 (全糖/正常冰)\n[實際]：{res1}"
            
        # 測試 2: 修改甜度
        res2 = fn("綠茶", sugar="無糖")
        if res2 != "已下單：綠茶 (無糖/正常冰)":
            return f"❌ 參數覆寫錯誤：當指定 sugar='無糖' 時，輸出不正確。\n[實際]：{res2}"

        # 2. 驗證 Console 最終三行輸出
        actual_output = output.getvalue().strip()
        actual_lines = [line.strip() for line in actual_output.split("\n") if line.strip()]
        
        expected_lines = [
            "已下單：阿薩姆紅茶 (全糖/正常冰)",
            "已下單：茉莉綠茶 (無糖/正常冰)",
            "已下單：珍珠奶茶 (微糖/去冰)"
        ]
        
        if len(actual_lines) < 3:
            return "❌ 測試失敗！輸出的行數不足，請確保下方的測試程式碼有正確被執行。"
            
        if actual_lines[-3:] != expected_lines:
             return (
                 f"❌ Console 內容不正確。請檢查你的 return 字串格式與空白符號。\n\n"
                 f"[預期應該是最後三行印出]：\n" + "\n".join(expected_lines) + "\n\n"
                 f"[你的最後三行輸出是]：\n" + "\n".join(actual_lines[-3:])
             )
        
    except Exception as e:
        return f"❌ 執行錯誤：{str(e)}"
            
    return "SUCCESS"
