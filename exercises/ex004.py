"""
title: 練習題 004：認識註解
quest_html: 寫程式時，我們經常會在程式碼旁邊寫下筆記，這些筆記稱為「註解」。在 Python 中，只要在文字前面加上 <code>#</code> 符號，那一行就會被視為註解，電腦在執行程式時會自動忽略它。請嘗試把下方會報錯的文字變成註解，讓程式能夠順利執行。
"""

# ==== STARTER CODE ====
# 請把下一行的文字變成註解，以免程式發生錯誤！
這是一行會報錯的文字，請在最前面加上井字號把它變成註解

print("程式成功執行！恭喜你學會了註解！")

# ==== TEST CODE ====
import sys

def run_tests():
    try:
        # Get captured output
        output = sys.stdout.get_value().strip()
        
        expected = "程式成功執行！恭喜你學會了註解！"
        
        if output == expected:
            return "SUCCESS"
        else:
            return f"❌ 程式好像沒有正確印出預期的文字喔。\n你的輸出：\n{output}"
    except Exception as e:
        return str(e)
