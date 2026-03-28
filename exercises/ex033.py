"""
title: 練習題 033：強化飲料類別
score: 1
quest_html: 隨著飲料店規模擴大，我們需要一套系統來記錄每杯飲料的細節。你已經學會建立基礎的飲料類別，現在請幫忙把<b>「點餐人」</b>加入這套系統，這樣群體訂購發派飲料時才不會搞混！<br><br><b>任務接力：</b><br>1. 修改下方現有類別 <code>Drink</code> 的初始化方法 <code>__init__</code>：<br>   - 參數請修改為包含：<code>name</code>、<b><code>who</code></b>、<code>sugar</code>、<code>ice</code>。<br>   - 在函式內新增屬性，將這杯飲料是誰點的存入 <code>self.who</code>。<br>2. 修改方法 <code>show_label(self)</code>：<br>   - 使用 <code>print()</code> 印出的格式改為：<code-snippet>{誰點的} 的 {名稱} ({糖度}/{冰塊})</code-snippet><br>3. 完成後觀察下方的測試程式碼是否成功執行！
"""

# ==== STARTER CODE ====
# 請修改 Drink 類別
class Drink:
    def __init__(self, name, sugar="正常甜", ice="正常冰"):
        # 這杯飲料自己「的」名字
        self.name = name
        # 這杯飲料自己「的」甜度
        self.sugar = sugar
        # 這杯飲料自己「的」冰量
        self.ice = ice

    def show_label(self):
        print(f"{self.name} ({self.sugar}/{self.ice})")

# --- 💡 以下測試程式碼請勿修改 ---
try:
    d1 = Drink("珍珠奶茶", "小明")
    d1.show_label() # 應印出：小明 的 珍珠奶茶 (正常甜/正常冰)

    d2 = Drink("美式咖啡", "小華", sugar="無糖", ice="去冰")
    d2.show_label() # 應印出：小華 的 美式咖啡 (無糖/去冰)
except TypeError as e:
    print(f"💡 提示：發生 TypeError！請檢查 `__init__` 是否已經加入了 `who` 參數喔！({e})")
except NameError:
    pass

# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：檢查類別與方法定義
        tree = ast.parse(studentCode)
        has_class = False
        has_init = False
        has_show_label = False
        init_defaults_count = 0
        has_self_assign = False
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == "Drink":
                has_class = True
                for subnode in node.body:
                    if isinstance(subnode, ast.FunctionDef):
                        if subnode.name == "__init__":
                            has_init = True
                            init_defaults_count = len(subnode.args.defaults)
                            # 檢查是否有 self.xxx = xxx 的賦值
                            for item in ast.walk(subnode):
                                if isinstance(item, ast.Attribute) and isinstance(item.value, ast.Name) and item.value.id == "self":
                                    has_self_assign = True
                        if subnode.name == "show_label":
                            has_show_label = True
        
        if not has_class:
            return "❌ 任務失敗！你必須定義一個名為 `Drink` 的類別。"
        if not has_init:
            return "❌ 任務失敗！類別內必須包含 `__init__` 初始化方法。"
        if not has_show_label:
            return "❌ 任務失敗！類別內必須包含 `show_label` 方法。"
        if init_defaults_count < 2:
            return f"❌ 任務失敗！`__init__` 方法必須為 `sugar` 與 `ice` 設定預設值。目前偵測到 {init_defaults_count} 個預設值。"
        if not has_self_assign:
            return "❌ 任務失敗！在 `__init__` 中，請使用 `self.屬性名 = 參數名` 來儲存資料。"
            
    except SyntaxError as e:
        return f"❌ 語法錯誤：{str(e)}"
        
    import io
    import contextlib

    # 準備執行環境
    if isinstance(__builtins__, dict):
        builtins_dict = __builtins__.copy()
    else:
        import builtins
        builtins_dict = vars(builtins).copy()

    global_env = {
        '__builtins__': builtins_dict,
        'print': print
    }
    output = io.StringIO()
    
    try:
        with contextlib.redirect_stdout(output):
            exec(studentCode, global_env)
        
        # 1. 驗證類別邏輯
        DrinkClass = global_env.get("Drink")
        if not DrinkClass: return "❌ 找不到 `Drink` 類別。"
        
        # 測試實例化
        try:
            test_obj = DrinkClass("測試飲料", "阿嬤", sugar="微糖", ice="少冰")
        except TypeError as e:
            return f"❌ 執行錯誤：在建立飲料時失敗了，是不是忘記在 `__init__` 加入 `who` 參數呢？ ({e})"
        
        if not hasattr(test_obj, 'name') or test_obj.name != "測試飲料":
            return "❌ 屬性設定錯誤：`self.name` 沒有正確儲存。"
        if not hasattr(test_obj, 'who') or test_obj.who != "阿嬤":
            return "❌ 屬性設定錯誤：`self.who` 沒有正確儲存。"
        
        # 2. 驗證 Console 輸出
        actual_output = output.getvalue().strip()
        actual_lines = [line.strip() for line in actual_output.split("\n") if line.strip()]
        
        expected_lines = [
            "小明 的 珍珠奶茶 (正常甜/正常冰)",
            "小華 的 美式咖啡 (無糖/去冰)"
        ]
        
        if len(actual_lines) < 2:
            return "❌ 測試失敗！輸出的行數不足，請確保下方的測試程式碼有正確被執行。"
            
        if actual_lines[-2:] != expected_lines:
             return (
                 f"❌ Console 內容不正確。請檢查你的 `show_label` 方法中的字串格式（注意括號與斜線）。\n\n"
                 f"[預期應該是最後兩行印出]：\n" + "\n".join(expected_lines) + "\n\n"
                 f"[你的最後兩行輸出是]：\n" + "\n".join(actual_lines[-2:])
             )
        
    except Exception as e:
        return f"❌ 執行錯誤：{str(e)}"
            
    return "SUCCESS"
