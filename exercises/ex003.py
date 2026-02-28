"""
title: 練習題 003：認識 Console（主控台）
quest_html: 寫程式時，我們經常需要「看到」程式執行的過程或結果，這時候就會用到 <code>print()</code>。它會將括號內的內容顯示在下方的「Console」（主控台）區域。請嘗試在下方印出這兩行文字：<br><code>Python is cool!</code><br><code>I love coding.</code>
"""

# ==== STARTER CODE ====
# 請在下方使用兩次 print() 分別印出指定的兩行文字
print("Python is cool!")

# ==== TEST CODE ====
import sys

def run_tests():
    try:
        # Get captured output
        output = sys.stdout.get_value().strip().split('\n')
        # Clean up any extra spaces
        output = [line.strip() for line in output if line.strip()]
        
        expected = ["Python is cool!", "I love coding."]
        
        if output == expected:
            return "SUCCESS"
        else:
            actual_str = "\n".join(output)
            expected_str = "\n".join(expected)
            return f"❌ Console 內容不正確。\n\n[預期應該是]：\n{expected_str}\n\n[你的輸出是]：\n{actual_str}"
    except Exception as e:
        return str(e)
