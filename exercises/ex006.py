"""
title: 練習題 006：再修一個！
score: 1
quest_html: 嘗試修好下面的程式吧！
"""

# ==== STARTER CODE ====
print("我可以跑嗎？')
prnt("我也可以跑嗎？")

# ==== TEST CODE ====
import sys

def run_tests():
    try:
        # Get captured output
        output = sys.stdout.get_value().strip()
        
        expected = "我可以跑嗎？\n我也可以跑嗎？"
        
        if output == expected:
            return "SUCCESS"
        else:
            return f"❌ 程式好像沒有正確印出預期的文字喔。\n[預期應該是]：\n{expected}\n\n[你的輸出是]：\n{output}"
    except Exception as e:
        return str(e)
