"""
title: 練習題 011：網購結帳小幫手
score: 1
quest_html: 看到心儀的商品在特價時，最令人心動的就是結帳那一刻了！讓我們寫一個簡單的結帳系統，自動計算折扣、加入運費，並貼心地告訴使用者這次一共省下了多少錢吧！<br><br><b>任務需求：</b><br>1. 使用 <code>input()</code> 詢問商品原價總額，並轉換為<b>浮點數 (float)</b> 存入變數 <code>total</code>。<br>2. <b>計算折扣</b>：使用 <b><code>*=</code></b> 將 <code>total</code> 打 <b>85 折</b> (乘以 0.85)。<br>3. <b>計算運費</b>：使用 <b><code>+=</code></b> 將 <code>total</code> 加上 <b>60 元</b>運費。<br>4. <b>計算省下的錢</b>：將原價扣掉「打折後但尚未加運費」的金額，存入變數 <code>savings</code>。<br>5. <b>格式化輸出</b>：請依照以下格式輸出（分隔線請使用<b>字串運算 <code>"-" * 20</code></b> 生成）：<br><code-snippet>--------------------<br>網購結帳明細<br>--------------------<br>折扣後總額 (含運)：{total} 元<br>本次購買讓你省下了：{savings} 元<br>--------------------</code-snippet>
"""

# ==== STARTER CODE ====
# 1. 詢問原價總額並轉型
original_price = input("請輸入商品原價總額：")
total = original_price

# 2. 使用 *= 計算 85 折
# total ...

# 3. 計算省下的金額 (建議在加運費前計算)
# savings = ...

# 4. 使用 += 加上 60 元運費
# total ...

# 5. 輸出收據 (記得使用 "-" * 20 生成分隔線)
# line = ...
# print(line)
# print("網購結帳明細")
# ...


# ==== TEST CODE ====
import sys

def run_tests():
    # 這裡我們不使用 Mock Input，而是直接觀察學生執行後的成果
    # 因為在 Pyodide 環境中，這段測試會在學生手動跑完程式、輸入完數字後才執行
    
    try:
        # 1. 檢查必要的變數是否存在
        required_vars = ['original_price', 'total', 'savings']
        for var in required_vars:
            if var not in globals():
                return f"❌ 找不到變數 `{var}`，請確保你有正確命名並賦值。"

        # 2. 獲取學生輸入的原始價格進行動態計算
        # 我們假設學生已經在練習中正確將 original_price 轉為 float
        try:
            val_original = float(original_price)
        except (ValueError, TypeError):
            return "❌ `original_price` 的格式不正確，請確保你使用了 float() 轉換輸入。"

        # 5. 檢查 Console 輸出格式 (嚴格比對)
        expected_line = "-" * 20
        expected_receipt = (
            f"{expected_line}\n"
            f"網購結帳明細\n"
            f"{expected_line}\n"
            f"折扣後總額 (含運)：{total} 元\n"
            f"本次購買讓你省下了：{savings} 元\n"
            f"{expected_line}"
        )
        
        captured_output = sys.stdout.get_value().strip()
        
        # 簡單清理學生的輸出（去除每行結尾空白）以增加容錯
        cleaned_captured = "\n".join([line.rstrip() for line in captured_output.split("\n")])

        if cleaned_captured == expected_receipt:
            return "SUCCESS"
        else:
            return (
                f"❌ Console 輸出格式不完全正確。\n\n"
                f"[系統預期的收據內容為]：\n{expected_receipt}\n\n"
                f"[你的實際輸出內容為]：\n{captured_output}\n\n"
                f"[提示]：請確保所有文字、數值、甚至是每一行分隔線 `{expected_line}` 都完全符合任務要求。"
            )
            
    except Exception as e:
        return f"❌ 測試系統執行時發生錯誤：{str(e)}"
