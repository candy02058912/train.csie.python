"""
title: 練習題 002：修好 Bug！
quest_html: 哎呀！Sam 受傷了，但是目前的程式碼好像有點問題。原本設定好的傷害值 <code>sword_damage</code> 似乎沒有正確扣除。請修改程式碼，讓最後印出的 <code>end_health</code> 能正確顯示 Sam 受傷後的剩餘血量。
"""

# ==== STARTER CODE ====
sword_damage = 10
start_health = 100
# 這裡好像怪怪的？請修復下方的計算式
end_health = start_health

# 請勿更動下方的程式碼
print(f"Sam's health is: {start_health}")
print(f"Sam takes {sword_damage} damage...")
print(f"Sam's health is: {end_health}")

# ==== TEST CODE ====
import sys

def run_tests():
    try:
        # We check the variables in the global scope after student execution
        if end_health == 90:
            return "SUCCESS"
        else:
            return f"Sam 的剩餘血量應該要是 90，但你的程式計算結果為 {end_health}。"
    except Exception as e:
        return str(e)
