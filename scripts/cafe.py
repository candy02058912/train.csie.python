"""
多檔案專案：模組與 Import 練習
請完成下方兩個任務，並執行 uv run cafe_checker.py 檢查。
"""

# 【任務 1】：將 menu.py 標籤庫匯入到這個檔案中
# 你可以自由選擇要使用 `import menu` 還是 `from menu import ...`
# 提示：寫下你的 import 語法：



# 【任務 2】：點一份食物
# 請依照你剛剛 import 的方式，建立一個 Food 並存放在變數 my_food 中
# 名稱為 "牛肉麵"，價格為 150
my_food = None


# 【任務 3】：點一杯飲料
# 請依照你剛剛 import 的方式，建立一個 Drink 並存放在變數 my_drink 中
# 名稱為 "珍珠奶茶"，甜度 "微糖"，冰塊 "少冰"
my_drink = None


# --- 💡 以下測試與展示請勿修改 ---
if __name__ == "__main__":
    print("\n=== 今日點餐明細 ===")
    if 'my_food' in locals() and my_food is not None:
        my_food.show_label()
    if 'my_drink' in locals() and my_drink is not None:
        my_drink.show_label()
