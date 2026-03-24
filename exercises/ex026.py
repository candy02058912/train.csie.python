"""
title: 練習題 026：in 運算子
score: 1
quest_html: 在 Python 裡，我們常常需要檢查某個東西「有沒有在」清單或字典裡面。<br>這時候 <b><code>in</code></b> 這個關鍵字非常好用！對於字典來說，它會去檢查 <b>key</b> 是否存在於字典中。<br><br><b>任務需求：</b><br>1. 我們有一份 <code>menu</code> 字典，以及客人點的飲料 <code>order</code>。<br>2. 請使用 <b><code>if</code> / <code>else</code></b> 搭配 <b><code>in</code></b> 運算子來檢查 <code>order</code> 是否存在於 <code>menu</code> 中。<br>3. <b>如果存在：</b>請印出 <code-snippet>您的飲料是 {價格} 元</code-snippet> (價格請從字典中讀取)<br>4. <b>如果不存在：</b>請印出 <code-snippet>抱歉，我們沒有賣 {order}</code-snippet>
"""

# ==== STARTER CODE ====
menu = {"紅茶": 30, "綠茶": 30, "珍奶": 50}
order = "烏龍茶"

# 請在下方寫下你的 if / else 判斷



# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查
        tree = ast.parse(studentCode)
        has_if = False
        has_in = False
        
        for node in ast.walk(tree):
            if isinstance(node, ast.If):
                has_if = True
            if isinstance(node, ast.Compare):
                # 檢查是否有用到 In 或是 NotIn 運算子
                for op in node.ops:
                    if isinstance(op, (ast.In, ast.NotIn)):
                        has_in = True

        if not has_if:
            return "❌ 任務失敗！你必須使用 `if / else` 來進行判斷。"
        if not has_in:
            return "❌ 任務失敗！這一題需要你練習使用 `in` 運算子來檢查 key 是否存在喔！"
            
    except SyntaxError as e:
        return f"❌ 語法錯誤：{str(e)}"
        
    import io
    import contextlib

    import re
    # 準備執行環境模板
    def test_with_order(test_order):
        if isinstance(__builtins__, dict):
            builtins_dict = __builtins__.copy()
        else:
            import builtins
            builtins_dict = vars(builtins).copy()

        global_env = {
            '__builtins__': builtins_dict,
            'print': print,
            'menu': {"紅茶": 30, "綠茶": 30, "珍奶": 50}
        }
        output = io.StringIO()
        
        # 動態將 studentCode 內的 order = "烏龍茶" 抽換成指定測試字串
        modified_code = re.sub(r'order\s*=\s*([\'"]).*?\1', f'order = "{test_order}"', studentCode, count=1)
        
        try:
            with contextlib.redirect_stdout(output):
                exec(modified_code, global_env)
            return output.getvalue().strip()
        except Exception as e:
            return f"❌ 執行錯誤：{str(e)}"
    
    # 測試情境 1: 預設的 烏龍茶 (不存在)
    res1 = test_with_order("烏龍茶")
    if res1.startswith("❌"): return res1
    
    actual_lines1 = [line.strip() for line in res1.split("\n") if line.strip()]
    if len(actual_lines1) == 0:
        return "❌ 測試失敗：當 order 是 '烏龍茶' 時，你沒有印出任何東西！"
    if actual_lines1[-1] != "抱歉，我們沒有賣 烏龍茶":
        return f"❌ 測試失敗：當 order 是 '烏龍茶' (不在菜單內) 時，輸出不正確。\n\n[預期應該是]：\n抱歉，我們沒有賣 烏龍茶\n\n[你的答案是]：\n{actual_lines1[-1]}"
        
    # 測試情境 2: 改變為 珍奶 (存在)
    res2 = test_with_order("珍奶")
    if res2.startswith("❌"): return res2
    
    actual_lines2 = [line.strip() for line in res2.split("\n") if line.strip()]
    if len(actual_lines2) == 0:
        return "❌ 測試失敗：當 order 變成菜單上有的東西時，你的程式碼沒有輸出！請確保不是把答案寫死了。"
    if actual_lines2[-1] != "您的飲料是 50 元":
        return f"❌ 測試失敗：當系統把 order 改成 '珍奶' 測試時，輸出不正確。\n這代表你的程式碼可能沒有正確從字典裡抓取對應的價格喔！\n\n[預期應該是]：\n您的飲料是 50 元\n\n[你的答案是]：\n{actual_lines2[-1]}"

    return "SUCCESS"
