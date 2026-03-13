"""
title: 練習題 008：狗狗年齡轉換器
score: 1
quest_html: 雖然你已經學會了 <code>input()</code>，但有一個新手最常踩到的坑：無論你輸入的是數字還是文字，Python 都會把它當成「字串 (String)」。<br><br>如果你輸入 "10" 然後直接乘以 7，Python 會給你 <code>"10101010101010"</code> (把字串重複七次)！<br><br>請修正程式碼，讓它能正確計算出狗狗年齡（人類年齡 * 7）
"""

# ==== STARTER CODE ====
age = input("請問你今年幾歲？")

dog_age = age * 7

print(f"轉換成狗狗年齡後，你大約是：{dog_age} 歲")

# ==== TEST CODE ====
def run_tests():
    # 準備測試用的模擬輸入
    global _MOCK_INPUTS
    _MOCK_INPUTS = ["10"] # 模擬學生輸入 10
    
    try:
        # 執行學生的程式碼
        # 注意：這會使用我們在 template 定義的 custom_input
        exec(studentCode, globals())
        
        # 檢查變數 dog_age
        # 如果學生沒轉型，10 * 7 會變成 "10101010101010" (字串)
        # 如果學生有轉型，會是 70 (整數)
        if dog_age == 70:
            return "SUCCESS"
        elif dog_age == "10101010101010":
            return "❌ 算錯囉！程式輸出了重複的字串。\n\n[提示]：\n請記得把輸入 (input) 轉成數字 (int)。"
        else:
            return f"❌ 數字計算不正確喔。\n\n[預期應該是]：\n70\n\n[你的計算結果是]：\n{dog_age}"
            
    except ValueError:
        return "程式發生錯誤：轉換數字失敗。請確保你只對數字字串使用 int()。"
    except Exception as e:
        return f"執行時發生錯誤：{str(e)}"
