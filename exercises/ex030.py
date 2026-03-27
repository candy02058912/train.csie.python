"""
title: 練習題 030：吧台標籤機
score: 1
quest_html: 隨著程式碼變多，我們希望它更專業且容易維護。<b>Type Hints (型別提示)</b> 可以標註資料的型別，讓讀程式的人一眼就看懂要傳什麼進去、會拿到什麼出來。這次我們要來挑戰加上清單的標註方式！<br><br><b>任務需求：</b><br>1. 定義函式 <code>format_labels</code>。<br>2. 使用「型別提示」標註：參數 <code>drinks</code> 必須標明為「字串清單」，且函式的回傳值也必須標明為「字串清單」。<br>　👉 <i>提示：可以上網查或問 AI「Python 如何在函式標註字串清單類型？」</i><br>3. 函式內部：<br>   - 使用迴圈處理 <code>drinks</code>，將每個名稱前加上編號與點，例如：<code-snippet>"1. 珍珠奶茶"</code-snippet><br>   - <b>💡 小技巧：</b>你可以搜尋 <code>enumerate()</code> 的用法，它能讓你更輕鬆地同時拿取 index 與 value。<br>   - 回傳處理好的新清單。
"""

# ==== STARTER CODE ====
# 請在下方開始定義函式 format_labels


# --- 以下程式碼請勿修改 ---
drinks_list = ["珍珠奶茶", "四季春", "紅茶"]
print(format_labels(drinks_list))


# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查型別標註
        tree = ast.parse(studentCode)
        has_func = False
        has_type_hint_arg = False
        has_type_hint_return = False
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "format_labels":
                has_func = True
                
                # 檢查參數型別標註
                for arg in node.args.args:
                    if arg.arg == "drinks" and arg.annotation:
                        # 檢查是否標註為 list[str]
                        anno = arg.annotation
                        if isinstance(anno, ast.Subscript) and isinstance(anno.value, ast.Name) and anno.value.id == "list":
                             has_type_hint_arg = True
                
                # 檢查回傳型別標註
                if node.returns:
                    anno = node.returns
                    if isinstance(anno, ast.Subscript) and isinstance(anno.value, ast.Name) and anno.value.id == "list":
                        has_type_hint_return = True
        
        if not has_func:
            return "❌ 任務失敗！你必須定義一個名為 `format_labels` 的函式。"
        if not has_type_hint_arg:
            return "❌ 任務失敗！請在參數 `drinks` 後面加上型別提示 `: list[str]`。如果不確定怎麼寫，可以嘗試搜尋「python list type hint list[str]」。"
        if not has_type_hint_return:
            return "❌ 任務失敗！請加上回傳值的型別提示 `-> list[str]`。"
            
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
        fn = global_env.get("format_labels")
        if not fn: return "❌ 找不到 `format_labels` 函式。"
        
        test_inp = ["A", "B"]
        expected_res = ["1. A", "2. B"]
        actual_res = fn(test_inp)
        if actual_res != expected_res:
            return f"❌ 函式回傳內容不正確。\n[預期回傳]：{expected_res}\n[你的回傳]：{actual_res}"

        # 2. 驗證 Console 輸出
        actual_output = output.getvalue().strip()
        actual_lines = [line.strip() for line in actual_output.split("\n") if line.strip()]
        
        final_expected = str(['1. 珍珠奶茶', '2. 四季春', '3. 紅茶'])
        
        if not actual_lines:
            return "❌ 測試失敗！你沒有印出任何結果。"
            
        # Check if the list representation is in the last line
        if final_expected not in actual_lines[-1] and final_expected.replace("'", '"') not in actual_lines[-1]:
             return (
                 f"❌ Console 內容不正確。請檢查你輸出的清單內容。\n\n"
                 f"[預期應該印出]：\n{final_expected}\n\n"
                 f"[你的實際輸出]：\n{actual_lines[-1]}"
             )
        
    except Exception as e:
        return f"❌ 執行錯誤：{str(e)}"
            
    return "SUCCESS"
