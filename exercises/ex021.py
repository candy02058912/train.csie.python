"""
title: 練習題 021：我的購物清單
score: 1
quest_html: 歡迎來到 list 的世界！List 就像是一個可以裝很多東西的箱子，而且裡面的內容可以隨時更換、新增。<br><br><b>💡 List 的重點：</b><br>1. 使用中括號 <code>[]</code> 建立（宣告）<br>2. <b>Index 從 0 開始</b>！第一個是 <code>[0]</code>，第二個是 <code>[1]</code><br>3. <b>mutable (可變)</b>：可以直接修改裡面的內容，例如 <code>shop[0] = "梨子"</code><br>4. <code>len(shop)</code>：可以看這個清單總共有幾個內容 (length)<br>5. <code>shop.append("糖果")</code>：可以在清單的<b>最末尾</b>添加新東西<br><br><b>任務需求：</b><br>請依照順序完成以下操作：<br>1. 建立一個名為 <b><code>shop</code></b> 的清單，內含兩個字串："蘋果" 和 "香蕉"<br>2. 把 "糖果" 加到清單中<br>3. 將清單中<b>第 0 個</b>內容修改為 "榴槤"<br>4. 印出清單中的<b>最後一個</b>內容<br>5. 印出清單目前的<b>長度</b>。<br><br><b>💡 提示：</b>從 0 開始！從 0 開始！從 0 開始！(很重要所以說三次 XD)
"""

# ==== STARTER CODE ====
# 1. 建立一個名為 shop 的 list，包含 "蘋果" 和 "香蕉"


# 2. 新增 "糖果"


# 3. 修改第 0 個內容為 "榴槤"


# 4. 印出最後一個內容


# 5. print 長度



# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查
        tree = ast.parse(studentCode)
        has_append = False
        has_len = False
        has_negative_index = False
        has_index_assign = False
        has_declaration = False
        
        for node in ast.walk(tree):
            # Check for list declaration: shop = ["蘋果", "香蕉"]
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'shop':
                        if isinstance(node.value, ast.List):
                            has_declaration = True
                    if isinstance(target, ast.Subscript):
                        has_index_assign = True

            # Check for append() call
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == 'append':
                has_append = True
            # Check for len() call
            elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'len':
                has_len = True
            
            # Check for negative index [-1]
            if isinstance(node, ast.Subscript):
                 if isinstance(node.slice, ast.UnaryOp) and isinstance(node.slice.op, ast.USub):
                     if isinstance(node.slice.operand, ast.Constant) and node.slice.operand.value == 1:
                         has_negative_index = True
                 elif isinstance(node.slice, ast.Constant) and node.slice.value == -1:
                     has_negative_index = True

        if not has_declaration:
            return "❌ 任務失敗！沒偵測到 `shop` 清單的宣告。請先建立 `shop = [...]`。"
        if not has_append:
            return "❌ 任務失敗！沒偵測到 `append()`。請用它來新增 \"糖果\" 喔！"
        if not has_index_assign:
            return "❌ 任務失敗！記得用 `shop[0] = ...` 的語法來修改內容。"
        if not has_negative_index:
            return "❌ 任務失敗！請練習使用負數索引 `[-1]` 來讀取最後一個內容。"
        if not has_len:
            return "❌ 任務失敗！請使用 `len()` 函式來獲取清單長度。"
            
    except SyntaxError as e:
        return f"❌ 語法錯誤：{str(e)}"
        
    import io
    import contextlib
    import re

    # 準備執行環境
    if isinstance(__builtins__, dict):
        builtins_dict = __builtins__.copy()
    else:
        import builtins
        builtins_dict = vars(builtins).copy()

    global_env = {
        '__builtins__': builtins_dict,
        'print': print,
        'len': len
    }
    output = io.StringIO()
    
    try:
        with contextlib.redirect_stdout(output):
            exec(studentCode, global_env)
        
        # 檢查最後的 shop 狀態
        final_shop = global_env.get('shop')
        if not isinstance(final_shop, list):
            return "❌ 執行錯誤：找不到 `shop` 清單或型別不正確。"
            
        if "糖果" not in final_shop:
             return "❌ 內容不正確：清單中似乎沒有 \"糖果\"，你有正確使用 `append` 嗎？"
        if final_shop[0] != "榴槤":
             return f"❌ 內容不正確：第 0 個內容應該是 \"榴槤\"，但系統看到的是 \"{final_shop[0] if final_shop else '空'}\"。"
        
        captured = output.getvalue().strip()
        actual_lines = [line.strip() for line in captured.split("\n") if line.strip()]
        
        # 預期輸出：
        # 最後一個內容 (糖果)
        # 長度 (3)
        expected_outputs = ["糖果", "3"]
        
        if actual_lines != expected_outputs:
             return (
                 f"❌ Console 輸出不正確\n\n"
                 f"[系統預期看到的輸出]：\n糖果\n3\n\n"
                 f"[你的實際輸出]：\n" + "\n".join(actual_lines) + "\n\n"
                 f"📝 提示：請確認你有印出最後一個內容以及清單長度。"
             )
    except Exception as e:
        return f"❌ 執行錯誤：{str(e)}"
            
    return "SUCCESS"
