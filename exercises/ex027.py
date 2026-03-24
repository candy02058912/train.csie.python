"""
title: 練習題 027：飲料統計
score: 1
quest_html: 這是結合了 <code>split()</code>、字串格式化以及 <b>字典 (Dict) 統計</b> 的進階挑戰！飲料店接到了許多訂單，但它們都是逗號分隔的字串，我們需要把它們整理成吧台人員看得懂的統計清單。<br><br><b>任務需求：</b><br>1. 準備一個空字典 <code>summary</code> 來裝統計結果。<br>2. 用 <b><code>for</code> 迴圈</b> 逐一讀取 <code>orders</code> 中的每一筆訂單字串。<br>3. 在迴圈內，使用 <b><code>.split(',')</code></b> 將字串切開。<br>4. 提取出飲料名稱、甜度、冰塊，並組合成標籤字串（<b>將它存入變數，作為字典統計用的 key</b>），格式為：<code-snippet>{飲料名稱}({甜度}/{冰塊})</code-snippet>　👉 <i>例如：<code>"珍珠奶茶(半糖/少冰)"</code></i><br>5. 檢查這個標籤 key 有沒有在 <code>summary</code> 字典裡，進行數量統計（沒看過就設為 1，看過就 +1）。<br>6. 最後在迴圈外印出標題 <code-snippet>=== 今日吧台清單 ===</code-snippet>，再用另一個 <b><code>for</code> 迴圈</b> 走訪 <code>summary.items()</code>，印出每一筆飲料的統計結果：<code-snippet>🥤 {標籤}：{數量} 杯</code-snippet>
"""

# ==== STARTER CODE ====
orders = [
    "1,珍珠奶茶,半糖,少冰",
    "2,四季春,無糖,去冰",
    "3,珍珠奶茶,半糖,少冰",
    "4,珍珠奶茶,微糖,正常冰",
    "5,四季春,無糖,去冰"
]

# 請在下方開始編寫你的程式碼


# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST 檢查
        tree = ast.parse(studentCode)
        has_split = False
        has_dict_init = False
        for_count = 0
        
        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                for_count += 1
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == 'split':
                has_split = True
            if isinstance(node, ast.Assign):
                if isinstance(node.value, ast.Dict):
                    has_dict_init = True

        if not has_dict_init:
            return "❌ 任務失敗！你必須宣告一個空字典來收集統計資料 (例如 `summary = {}`)。"
        if not has_split:
            return "❌ 任務失敗！你必須使用 `split()` 來切割 CSV 字串。"
        if for_count < 2:
            return "❌ 任務失敗！你需要用一個 `for` 迴圈來處理訂單，最後還要用另一個 `for` 迴圈來印出統計結果喔！"
            
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
        'orders': [
            "1,珍珠奶茶,半糖,少冰",
            "2,四季春,無糖,去冰",
            "3,珍珠奶茶,半糖,少冰",
            "4,珍珠奶茶,微糖,正常冰",
            "5,四季春,無糖,去冰"
        ]
    }
    output = io.StringIO()
    
    try:
        with contextlib.redirect_stdout(output):
            exec(studentCode, global_env)
        
        captured = output.getvalue().strip()
        actual_lines = [line.strip() for line in captured.split("\n") if line.strip()]
        
        expected_outputs = [
            "=== 今日吧台清單 ===",
            "🥤 珍珠奶茶(半糖/少冰)：2 杯",
            "🥤 四季春(無糖/去冰)：2 杯",
            "🥤 珍珠奶茶(微糖/正常冰)：1 杯"
        ]
        
        # Check title output
        if "=== 今日吧台清單 ===" not in actual_lines:
            return "❌ 找不到標題 `=== 今日吧台清單 ===`，別忘了印出它喔！"
            
        # Verify the actual formatted output
        if actual_lines[-4:] != expected_outputs and actual_lines != expected_outputs:
             return (
                 f"❌ Console 最後輸出的統計結果不正確\n"
                 f"請確認你印出的內容與符號是否完全符合最終結果。\n\n"
                 f"[預期的輸出]：\n" + "\n".join(expected_outputs) + "\n\n"
                 f"[你的輸出]：\n" + "\n".join(actual_lines)
             )
    except Exception as e:
        return f"❌ 執行錯誤：{str(e)}"
            
    return "SUCCESS"
