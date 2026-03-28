"""
cafe_checker.py — Cafe 模組與 Import 練習檢查器
用法：將你的 cafe.py 放在同一個資料夾，然後執行：
    uv run cafe_checker.py
"""

import ast
import sys
import os
import urllib.request
import urllib.parse
import json

# ── 設定 ──────────────────────────────────────────
TARGET_FILE = "cafe.py"
MENU_FILE = "menu.py"
EXERCISE_ID = "cafe_import"
GAS_URL = "https://script.google.com/macros/s/AKfycbwao2BkgYeb9TgQsdnKs3cnzKfsyloH1WC2BQHBh3ru8L3qxosQ-T6ZOApkWVDSuBuaeg/exec"
MENU_DOWNLOAD_URL = "https://py.candys.page/menu.py"
CAFE_DOWNLOAD_URL = "https://py.candys.page/cafe.py"


def download_file_if_missing(filename: str, url: str) -> bool:
    """自動從給定的網址下載檔案，如果已下載新檔案則回傳 True"""
    if os.path.exists(filename):
        return False
        
    print(f"📦 偵測到缺少 {filename}，正在為你自動從雲端下載...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode('utf-8')
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
        print(f"✅ 成功下載 {filename}！")
        return True
    except Exception as e:
        print(f"❌ 自動下載 {filename} 失敗：{e}")
        print(f"   請確定網路連線正常，或手動從 {url} 下載並命名為 {filename}")
        sys.exit(1)


def setup_environment():
    """檢查並下載所需檔案，如果有下載任何新檔案，則提示學生開始作答並結束程式"""
    downloaded_cafe = download_file_if_missing(TARGET_FILE, CAFE_DOWNLOAD_URL)
    downloaded_menu = download_file_if_missing(MENU_FILE, MENU_DOWNLOAD_URL)
    
    if downloaded_cafe or downloaded_menu:
        print("\n" + "=" * 50)
        print("🎉 環境準備完成！")
        print(f"   請打開資料夾中的 `{TARGET_FILE}`，依照裡面的註解完成任務。")
        print("   修改並存檔完畢後，再重新執行一次這個指令！")
        print("=" * 50)
        sys.exit(0)


# ── 工具函式 ──────────────────────────────────────
def read_source(filepath: str) -> str:
    """讀取學生的原始碼"""
    if not os.path.exists(filepath):
        print(f"\n❌ 找不到 {filepath}！")
        print(f"   請確認你目前的資料夾裡面有創立 {filepath} 並且跟這個檢查器放在一起。")
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def parse_ast(source: str) -> ast.Module:
    """解析原始碼為 AST"""
    try:
        return ast.parse(source)
    except Exception as e:
        print(f"\n❌ 你的程式碼有語法錯誤（SyntaxError）或執行錯誤！")
        print(f"   錯誤訊息：{e}")
        print(f"   請先修正錯誤再來檢查。")
        sys.exit(1)


# ── AST 檢查邏輯 ─────────────────────────────────

def check_task1_any_import(tree: ast.Module) -> bool:
    """【任務 1】檢查是否有任何關於 menu 的 import"""
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == "menu":
                    return True
        elif isinstance(node, ast.ImportFrom):
            if node.module == "menu":
                return True
    return False

# ── 執行期間狀態檢查 ────────────────────────────────

def check_task3_food_instance() -> bool:
    """【任務 3】檢查 my_food 是否為 menu.Food 的實例"""
    # 確保當前目錄在 sys.path 中，這樣 import menu 才會成功
    if os.getcwd() not in sys.path:
        sys.path.insert(0, os.getcwd())
        
    try:
        # 載入使用者的 cafe 模組
        if "cafe" in sys.modules:
            del sys.modules["cafe"] # 清除快取
        import cafe
    except Exception:
        return False
        
    my_food = getattr(cafe, "my_food", None)
    if my_food is None:
        return False
        
    cls_name = my_food.__class__.__name__
    if cls_name == "Food":
        if hasattr(my_food, "name") and my_food.name == "牛肉麵":
            if hasattr(my_food, "price") and my_food.price == 150:
                return True
    return False


def check_task4_drink_instance() -> bool:
    """【任務 4】檢查 my_drink 是否為 menu.Drink 的實例"""
    try:
        if "cafe" in sys.modules:
            del sys.modules["cafe"]
        import cafe
    except Exception:
        return False
        
    my_drink = getattr(cafe, "my_drink", None)
    if my_drink is None:
        return False
        
    cls_name = my_drink.__class__.__name__
    if cls_name == "Drink":
        if hasattr(my_drink, "name") and my_drink.name == "珍珠奶茶":
            if hasattr(my_drink, "sugar") and my_drink.sugar == "微糖":
                 if hasattr(my_drink, "ice") and my_drink.ice == "少冰":
                    return True
    return False


# ── 成績提交 ──────────────────────────────────────

def submit_grade(stu_id: str, stu_name: str):
    """透過 GET 請求將成績送出到 Google Apps Script"""
    params = urllib.parse.urlencode({
        "stuID": stu_id,
        "stuName": stu_name,
        "exID": EXERCISE_ID,
    })
    url = f"{GAS_URL}?{params}"

    try:
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if data.get("status") == "success":
                print(f"\n✅ {stu_name} 同學，{EXERCISE_ID} 的成績已成功傳送！")
            else:
                msg = data.get("message", "未知錯誤")
                print(f"\n⚠️ 傳送失敗：{msg}")
                print("   請確認資料正確性，或聯繫 Candy。")
    except Exception as e:
        print(f"\n⚠️ 網路連線錯誤：{e}")
        print("   請確認網路連線後再試一次。")


# ── 主流程 ────────────────────────────────────────

def main():
    print("=" * 50)
    print("☕ Cafe 模組與 Import 練習檢查器")
    print("=" * 50)

    # 0. 下載所需檔案並讀取原始碼
    setup_environment()
    
    # 確保 sys.path 包含當前目錄以供載入
    current_dir = os.path.abspath(os.path.dirname(__file__))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
        
    source = read_source(TARGET_FILE)
    tree = parse_ast(source)

    # 1. 執行檢查
    checks = [
        (
            "任務 1：使用 import 或是 from 匯入 menu 模組與類別",
            check_task1_any_import(tree),
            "💡 提示：請在程式碼中寫下 `import menu` 或是 `from menu import ...`",
        ),
        (
            "任務 2：建立一份牛肉麵存入 my_food",
            check_task3_food_instance(),
            "💡 提示：請確定變數 my_food 已經正確建立（名稱為牛肉麵、價格為150）",
        ),
        (
            "任務 3：建立一杯珍珠奶茶存入 my_drink",
            check_task4_drink_instance(),
            "💡 提示：請確定變數 my_drink 已經正確建立（名稱為珍珠奶茶、指定微糖與少冰）",
        ),
    ]

    all_passed = True
    print()

    for name, passed, hint in checks:
        if passed:
            print(f"  ✅ {name}")
        else:
            print(f"  ❌ {name}")
            print(f"     {hint}")
            all_passed = False

    # 結果
    if not all_passed:
        print("\n" + "-" * 50)
        print("😢 還有幾個地方需要修正，請參考提示再試一次！")
        print("   修改並存檔完畢後，再執行一次這個檢查器。")
        print("-" * 50)
        sys.exit(1)

    print("\n" + "=" * 50)
    print("🎉 恭喜！所有檢查都順利完成了！")
    print("=" * 50)

    # 收集學生資訊並提交成績
    print("\n請填寫資料以登記成績：")
    stu_id = input(">> 學號：").strip()
    stu_name = input(">> 姓名：").strip()

    if not stu_id or not stu_name:
        print("❌ 學號和姓名都要填寫喔！")
        sys.exit(1)

    submit_grade(stu_id, stu_name)


if __name__ == "__main__":
    main()
