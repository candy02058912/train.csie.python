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
        # Only one test case for simplicity
        input_val = 5
        expected = 25
        actual = square(input_val)
        assert actual == expected, f"當輸入為 {input_val} 時，預期結果為 {expected}，但你的程式回傳了 {actual}"
        return "SUCCESS"
    except Exception as e:
        return str(e)
