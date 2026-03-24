# 注意！檔案名稱一定要叫 typing_game.py！
# 說明：這是一個練習打字的遊戲，但還沒有完全寫完，一共有三個任務要解開。
# 提示：要改的地方都在 TODO: 的下方，請不要改到其他地方。
# 測試/送出程式碼請跑: uv run https://py.candys.page/typing_game_checker.py
import random
import time
import keyword

# 準備關鍵字題庫
all_keywords = keyword.kwlist

print("=== 💻 成為 Python Keyword 大師 💻 ===")
print("模式 1 [15s] 正在趕時間")
print("模式 2 [30s] 我剛好有 30 秒")
print("模式 3 [60s] 認真練一下")

choice = input(">> 請輸入編號 (1/2/3): ")

# --- 【任務 1】設定挑戰時間 ---
limit = None
# 提示：如果 choice 是 '1'，limit 就是 15；如果是 '2'，limit 就是 30...
if choice == '1':
    limit = 15
# TODO: 請補上 choice 選擇其他模式的邏輯

# 遊戲計時初始化
correct = 0 # 答對題數
attempts = 0 # 總出題次數

print(f"\n倒數 {limit} 秒挑戰開始！")
input(">> 按下 ENTER 鍵開始計時...")

# 計時器初始化
start_time = time.time() # 開始時間
end_time = start_time + limit # 結束時間

# --- 【任務 2】設定遊戲迴圈 ---
# 提示：time.time() 可以神奇地拿到現在的時間，所以當現在時間小於 end_time (結束時間)，就可以繼續遊玩
# TODO: 請完成 while 的 __________ 條件
while time.time() ___________:
    
    # 隨機選一個關鍵字
    target = random.choice(all_keywords)
    print(f"\n請輸入: {target}")
    
    # 使用者的輸入
    u_in = input(">> ")
    
    # --- 【任務 3】判斷對錯 ---
    # TODO: 檢查使用者輸入是否跟 target 相等
    if ________:
        # TODO: 答對題數加 1
        print("✅ 正確")
    else:
        print("❌ 錯誤")


    attempts += 1

# 計算正確率
accuracy = (correct / attempts * 100) if attempts > 0 else 0

# 根據答對題數給予稱號
if correct >= 12:
    rank = "Senior 工程師 (恭喜，你現在可以出一張嘴叫別人寫了)"
elif correct >= 8:
    rank = "Mid-Level 工程師 (已經可以一邊開會一邊寫 Code 而不被發現)"
elif correct >= 4:
    rank = "Junior 工程師 (離看懂自己的程式碼又進了一步)"
else:
    rank = "實習工程師 (目前的專業是幫前輩訂下午茶，加油！)"

# 輸出最終結果
print("\n" + "="*50)
print(f"● 挑戰模式: {limit} 秒")
print(f"● 正確個數: {correct}")
print(f"● 你的等級: {rank}")
print("="*50)