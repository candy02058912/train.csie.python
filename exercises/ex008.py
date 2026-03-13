"""
title: 練習題 008 - 狗狗年齡轉換器
score: 1
quest_html: 雖然你已經學會了 <code>input()</code>，但有一個新手最常踩到的坑：無論你輸入的是數字還是文字，Python 都會把它當成「字串 (String)」。<br><br>如果你輸入 "10" 然後直接乘以 7，Python 會給你 <code>"10101010101010"</code> (把字串重複七次)！<br><br>請修正程式碼，讓它能正確計算出狗狗年齡（人類年齡 * 7）
"""

# ==== STARTER CODE ====
age = input("請問你今年幾歲？")

dog_age = age * 7

print(f"轉換成狗狗年齡後，你大約是：{dog_age} 歲")

# ==== TEST CODE ====
def run_tests():
    try:
        # 學生程式碼在外部執行時，age 已經由使用者輸入過
        # 我們直接檢查結果是否符合人年齡的 7 倍
        
        expected_dog_age = int(age) * 7
        
        if dog_age == expected_dog_age:
            return "SUCCESS"
        elif dog_age == str(age) * 7:
            return "❌ 算錯囉！程式輸出了重複的字串。\n\n[提示]：\n請記得把輸入 (input) 轉成數字 (int)。"
        else:
            return f"❌ 數字計算不正確喔。\n\n[預期應該是]：\n{expected_dog_age}\n\n[你的計算結果是]：\n{dog_age}"
            
    except ValueError:
        return "❌ 程式發生錯誤：轉換數字失敗。請確保你只對數字字串使用 int()。"
    except Exception as e:
        return f"執行測試時發生錯誤：{str(e)}"

