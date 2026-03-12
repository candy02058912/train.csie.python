"""
title: 練習題 007：型別練習
score: 1
quest_html: 老師想要知道同學 A 的平均分數，到底是幾分呢？
"""

# ==== STARTER CODE ====
# 應該要輸出平均分數，而不是這整串算式
print("(100 + 80 + 65 + 80) / 4")

# ==== TEST CODE ====
import sys

def run_tests():
    try:
        # Get captured output
        output = sys.stdout.get_value().strip()
        
        expected = "81.25"
        
        if output == expected:
            return "SUCCESS"
        else:
            return f"❌ 程式好像沒有正確印出預期的文字喔。\n[預期應該是]：\n{expected}\n\n[你的輸出是]：\n{output}"
    except Exception as e:
        return str(e)
