"""
title: 練習題 010：角色狀態報表
score: 1
quest_html: 實習生寫了一個角色資料系統，但他對型別的概念一團糟！<br>請修正變數的給值方式，確保型別符合預期：<br>1. <code>name</code> 為字串 <code>"Candy"</code>。<br>2. <code>level</code> 為整數 <code>25</code>。<br>3. <code>character_class</code> 為字串 <code>"魔術師"</code>。<br>4. <code>magic_resistance</code> 為浮點數 <code>15.0</code>。<br>5. <code>account_active</code> 為布林值 <code>True</code>。
"""

# ==== STARTER CODE ====
name = "Candy"
level = "25"
character_class = 魔術師
magic_resistance = 15
account_active = "True"

# --- 請勿更改下方程式碼 ---
print("角色狀態報表")
print(f"{name} 是一位等級 {level} 的 {character_class}。")
print(f"他們的魔法抗性為 {magic_resistance}。")
print(f"帳號目前啟用中：{account_active}")

print("=========================")
print("報表生成完畢")
print("資料型別檢查：")
print(f"name: {type(name).__name__}, level: {type(level).__name__}, character_class: {type(character_class).__name__}")
print(f"magic_resistance: {type(magic_resistance).__name__}")
print(f"account_active: {type(account_active).__name__}")

# ==== TEST CODE ====
import sys
def run_tests():
    try:
        output = sys.stdout.get_value().strip()
        expected = """角色狀態報表
Candy 是一位等級 25 的 魔術師。
他們的魔法抗性為 15.0。
帳號目前啟用中：True
=========================
報表生成完畢
資料型別檢查：
name: str, level: int, character_class: str
magic_resistance: float
account_active: bool"""
        
        if output == expected:
            return "SUCCESS"
        else:
            return f"❌ Console 內容不正確。\n\n[預期應該是]：\n{expected}\n\n[你的輸出是]：\n{output}"
    except Exception as e:
        return str(e)
