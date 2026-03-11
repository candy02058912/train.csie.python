"""
title: 練習題 005：複習與除錯
score: 1
quest_html: 這是一個複習題！寫程式時，只要打錯一個符號，電腦就會看不懂而發生錯誤（Syntax Error）。下面這段程式碼有一個小小的語法錯誤，請仔細觀察並把它修正，讓程式能夠順利執行！
"""

# ==== STARTER CODE ====
# 這裡有一段有語法錯誤的程式，仔細看看符號是不是有打錯呢？
print("歡迎回到 Python 的世界，可以猜得出我出了什麼問題嗎？"]

# ==== TEST CODE ====
import sys

def run_tests():
    try:
        # Get captured output
        output = sys.stdout.get_value().strip()
        
        expected = "歡迎回到 Python 的世界，可以猜得出我出了什麼問題嗎？"
        
        if output == expected:
            return "SUCCESS"
        else:
            return f"❌ 程式好像沒有正確印出預期的文字喔。\n[預期應該是]：\n{expected}\n\n[你的輸出是]：\n{output}"
    except Exception as e:
        return str(e)
