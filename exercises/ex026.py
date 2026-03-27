"""
title: 練習題 026：飲料杯數統計
score: 1
quest_html: 在進入更複雜的點單系統之前，吧台需要先學會如何統計每一種飲料的需求量。我們有一個只包含飲料名稱的清單 <code>drinks</code>，請使用字典 (Dict) 幫忙統計每種飲料各有幾杯。<br><br><b>任務需求：</b><br>1. 準備一個空字典 <code>counts</code> 用來裝統計結果。<br>2. 用 <b><code>for</code> 迴圈</b> 逐一把 <code>drinks</code> 裡面的飲料拿出來。<br>3. 在迴圈內，檢查該飲料有沒有在字典裡（<b>提示：你可以使用 <code>in</code> 來檢查</b>）。如果沒有，就設為 1 杯；如果已經有了，就加 1 杯。<br>4. 迴圈結束後，印出 <code>counts</code> 字典，預期會看到：<code-snippet>{'珍珠奶茶': 4, '四季春': 2, '紅茶': 1, '烏龍奶': 2}</code-snippet>
"""

# ==== STARTER CODE ====
drinks = [
    "珍珠奶茶", "四季春", "珍珠奶茶",
    "烏龍奶", "紅茶", "珍珠奶茶", "烏龍奶",
    "四季春", "珍珠奶茶"
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
        has_dict_init = False
        has_for = False
        has_in = False
        
        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                has_for = True
            if isinstance(node, ast.Assign):
                if isinstance(node.value, ast.Dict):
                    has_dict_init = True
            if isinstance(node, ast.Compare):
                # 檢查是否有用到 In 或是 NotIn 運算子
                for op in node.ops:
                    if isinstance(op, (ast.In, ast.NotIn)):
                        has_in = True

        if not has_dict_init:
            return "❌ 任務失敗！你必須宣告一個空字典來收集統計資料 (例如 `counts = {}`)。"
        if not has_for:
            return "❌ 任務失敗！你需要用一個 `for` 迴圈來處理 drinks 清單喔！"
        if not has_in:
            return "❌ 任務失敗！建議使用 `in` 運算子來檢查飲料是否已經存在於字典中。"
            
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
        'drinks': ["珍珠奶茶", "四季春", "珍珠奶茶", "烏龍奶", "紅茶", "珍珠奶茶", "烏龍奶", "四季春", "珍珠奶茶"]
    }
    output = io.StringIO()
    
    try:
        with contextlib.redirect_stdout(output):
            exec(studentCode, global_env)
        
        captured = output.getvalue().strip()
        actual_lines = [line.strip() for line in captured.split("\n") if line.strip()]
        
        expected_dict = {'珍珠奶茶': 4, '四季春': 2, '烏龍奶': 2, '紅茶': 1}
        
        # Check dictionary state
        if "counts" not in global_env:
            return "❌ 找不到變數 `counts`，請確認你有宣告 `counts = {}`。"
            
        if global_env["counts"] != expected_dict:
            return f"❌ `counts` 統計結果不正確。\n\n[預計出來的字典內容]：\n{expected_dict}\n\n[你算出來的結果]：\n{global_env['counts']}"
            
        # Verify the actual formatted output
        if not actual_lines:
            return "❌ 找不到任何輸出，請確保在迴圈外面有使用 `print(counts)` 印出結果。"
            
        # just check if output matches string representation (order might not matter in Py3.7+ but dict string format does)
        # the simplest way is to check eval
        try:
            student_output_dict = ast.literal_eval(actual_lines[-1])
            if student_output_dict != expected_dict:
                return f"❌ 最後一行的輸出不是預期的字典內容。\n\n[預期應該是]：\n{expected_dict}\n\n[你的答案是]：\n{actual_lines[-1]}"
        except:
             return f"❌ 最後一行的輸出格式錯誤，請確保你直接印出整個 counts 字典 (例如 `print(counts)`)。\n[你的答案是]：\n{actual_lines[-1]}"
            
    except Exception as e:
        return f"❌ 執行錯誤：{str(e)}"
            
    return "SUCCESS"
