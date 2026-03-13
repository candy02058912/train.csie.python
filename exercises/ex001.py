"""
title: 練習題 001：Hello World!
score: 1
quest_html: 請在下方印出 <code>Hello World!</code> 字樣：<code-snippet>Hello World!</code-snippet>
"""

# ==== STARTER CODE ====
# 請更改下方程式碼，讓輸出結果為 "Hello World!"
print("Hi! I'm Candy!")

# ==== TEST CODE ====
import sys

def run_tests():
    try:
        # Since sys.stdout is replaced by CaptureOutput in the template, 
        # we can get the current value to check what was printed.
        output = sys.stdout.get_value().strip()
        expected = "Hello World!"
        
        if output == expected:
            return "SUCCESS"
        else:
            return f"❌ Console 內容不正確。\n\n[預期應該是]：\n{expected}\n\n[你的輸出是]：\n{output}"
    except Exception as e:
        return str(e)
