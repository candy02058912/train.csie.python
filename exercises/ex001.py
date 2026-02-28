"""
title: 練習題：計算平方
quest_html: 請完成函式 <code>square(n)</code>，讓它回傳數字的平方值。
"""

# ==== STARTER CODE ====
def square(n):
    # 在這裡寫你的程式碼
    return n * n

# ==== TEST CODE ====
def run_tests():
    try:
        assert square(5) == 25, f"Expected square(5) to be 25, but got {square(5)}"
        assert square(0) == 0, f"Expected square(0) to be 0, but got {square(0)}"
        return "SUCCESS"
    except Exception as e:
        return f"Error: {str(e)}"
run_tests()
