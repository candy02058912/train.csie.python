"""
title: 練習題 015：網購免運判定
score: 1
quest_html: 延續我們瘋狂購物的行程！這次商店有「<b>滿千免運</b>」或是「<b>VIP 免運</b>」的活動，請用語法 <code>if / else</code> 搭配邏輯運算子 (<code>and</code> 或 <code>or</code>) 寫一個驗證系統。<br><br><b>任務需求：</b><br>1. 題目提供了兩個變數：「消費金額 (<code>total</code>)」與「是否為 VIP (<code>vip</code>)」(字串 `Y` 或 `N`)。<br>2. 撰寫判斷邏輯：<br>📦 如果消費金額大於等於 <b>1000</b>，<u>或是</u> VIP 狀態為 <b>Y</b>，印出： <code-snippet>免運費！</code-snippet><br>📦 若兩者都不符合，印出：<code-snippet>需要運費 60 元。</code-snippet><br><br><b>注意：</b>送出解答時，系統會在背景代入各種消費組合偷偷測試你的程式碼喔！請確保邏輯正確無誤。
"""

# ==== STARTER CODE ====
# 這裡提供了一組預設的變數，送出解答時系統會放入其他情境來測試喔！
total = 1200
vip = "N"

# 請在下方開始編寫你的 if / else 與邏輯運算 (and / or)



# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查學生是否有使用 If 敘述
        tree = ast.parse(studentCode)
        has_if = False
        for node in ast.walk(tree):
            if isinstance(node, ast.If):
                has_if = True
                break
        if not has_if:
            return "❌ 任務失敗！\n\n系統沒有偵測到任何 `if` 判斷式。\n請務必使用 `if` 與 `else`，不能只用 `print()` 偷矇過關喔！😜"
    except SyntaxError as e:
        return f"❌ 語法錯誤：{str(e)}"
        
    # [背景偷偷測試多種情境]
    import io
    import contextlib

    # 格式：(total 數字, vip 字串, 預期結果)
    test_cases = [
        (1500, "N", "免運費！"),           # 滿千、非 VIP
        (500, "Y", "免運費！"),            # 未滿千、是 VIP
        (2000, "Y", "免運費！"),           # 滿千、是 VIP
        (200, "N", "需要運費 60 元。")     # 未滿千、非 VIP
    ]

    import re

    for total_val, vip_val, expected_msg in test_cases:
        local_env = {}
        global_env = {'__builtins__': __builtins__}
        output = io.StringIO()
        
        # 使用正則表達式取代學生程式碼中的變數賦值，進行背景情境測試
        patched_code = re.sub(
            r"^total\s*=\s*.*$", 
            f"total = {total_val}", 
            studentCode, 
            flags=re.MULTILINE
        )
        patched_code = re.sub(
            r"^vip\s*=\s*.*$", 
            f"vip = '{vip_val}'", 
            patched_code, 
            flags=re.MULTILINE
        )
        
        try:
            with contextlib.redirect_stdout(output):
                exec(patched_code, global_env, local_env)
            
            captured = output.getvalue().strip()
            cleaned = "\n".join([line.rstrip() for line in captured.split("\n")])
            
            if expected_msg not in cleaned:
                # 判斷是敗在什麼情境
                fail_reason = f"總金額 {total_val} 且 VIP={vip_val}"
                return (
                    f"❌ 判斷與輸出不完全正確。\n\n"
                    f"(系統在背景偷偷測試情境：{fail_reason})\n\n"
                    f"[系統預期包含]： {expected_msg}\n"
                    f"[你的實際輸出]： {captured}\n\n"
                    f"[提示]：請確定你有正確使用 `or` 邏輯運算子，以及 `total >= 1000` 與 `vip == \"Y\"` 的條件。"
                )
        except Exception as e:
            return f"❌ 執行錯誤 (測試 {total_val}, {vip_val})：\n{type(e).__name__}: {str(e)}"
            
    return "SUCCESS"
