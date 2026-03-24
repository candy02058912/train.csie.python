"""
typing_game_checker.py — 打字遊戲作業檢查器
用法：將你的 typing_game.py 放在同一個資料夾，然後執行：
    uv run typing_game_checker.py
"""

import ast
import sys
import os
import urllib.request
import urllib.parse
import json

# ── 設定 ──────────────────────────────────────────
TARGET_FILE = "typing_game.py"
EXERCISE_ID = "typing_game"
GAS_URL = "https://script.google.com/macros/s/AKfycbwao2BkgYeb9TgQsdnKs3cnzKfsyloH1WC2BQHBh3ru8L3qxosQ-T6ZOApkWVDSuBuaeg/exec"


# ── 工具函式 ──────────────────────────────────────
def read_source(filepath: str) -> str:
    """讀取學生的原始碼"""
    if not os.path.exists(filepath):
        print(f"\n❌ 找不到 {filepath}！")
        print(f"   請確認 {filepath} 跟這個檢查器放在同一個資料夾。")
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def parse_ast(source: str) -> ast.Module:
    """解析原始碼為 AST"""
    try:
        return ast.parse(source)
    except SyntaxError as e:
        print(f"\n❌ 你的程式碼有語法錯誤（SyntaxError）！")
        print(f"   第 {e.lineno} 行：{e.msg}")
        print(f"   請先修正語法錯誤再來檢查。")
        sys.exit(1)


# ── AST 檢查邏輯 ─────────────────────────────────

def check_limit_logic(source: str) -> tuple[int | None, int | None, int | None]:
    """
    【任務 1】透過模擬執行來檢查學生是否正確設定了 15s/30s/60s 的邏輯。
    """
    def get_limit_for_choice(c: str):
        # 截斷程式碼，只取 while 迴圈之前的初始化部分，避免進入遊戲主體
        lines = source.splitlines()
        init_code = []
        for line in lines:
            if line.strip().startswith("while ") or "time.time()" in line:
                break
            init_code.append(line)
        
        # 準備執行環境
        loc = {}
        def mock_input(prompt=""):
            if "編號" in prompt or "1/2/3" in prompt:
                return c
            # 若碰到其他的 input (如 ENTER 鍵)，就中斷
            raise EOFError("End of init")
            
        def mock_print(*args, **kwargs):
            pass
        
        env = {
            "input": mock_input,
            "print": mock_print,
            "time": __import__("time"),
            "random": __import__("random"),
            "keyword": __import__("keyword"),
            "__name__": "__main__",
        }
        
        try:
            exec("\n".join(init_code), env, loc)
        except (EOFError, Exception):
            pass
            
        return loc.get("limit")

    return get_limit_for_choice("1"), get_limit_for_choice("2"), get_limit_for_choice("3")


def check_while_condition(tree: ast.Module) -> bool:
    """
    【任務 2】檢查 while 迴圈的條件是 time.time() < end_time
    starter code 用的是 while True
    """
    for node in ast.walk(tree):
        if isinstance(node, ast.While):
            test = node.test
            # 應該是 Compare: time.time() < end_time
            if isinstance(test, ast.Compare):
                # 左邊: time.time()
                left = test.left
                if _is_time_time_call(left):
                    # 比較運算子: Lt
                    if len(test.ops) == 1 and isinstance(test.ops[0], ast.Lt):
                        # 右邊: end_time
                        if len(test.comparators) == 1:
                            comp = test.comparators[0]
                            if isinstance(comp, ast.Name) and comp.id == "end_time":
                                return True
    return False


def check_task3_if_condition(tree: ast.Module) -> bool:
    """
    【任務 3-1】檢查是否有 if u_in == target:
    """
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            if _is_comparison(node.test, "u_in", "target", is_variable=True):
                return True
    return False


def check_task3_increment(tree: ast.Module) -> bool:
    """
    【任務 3-2】檢查在正確的 if 判斷式中，是否有 correct += 1
    """
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            # 先找到正確的 if 判斷式 (或是包含 u_in == target 的判斷)
            if _is_comparison(node.test, "u_in", "target", is_variable=True):
                # 檢查其 body 裡是否有 correct += 1
                for stmt in node.body:
                    if _is_correct_increment(stmt):
                        return True
    return False


def _is_correct_increment(stmt) -> bool:
    """檢查 stmt 是否為 correct += 1 或 correct = correct + 1"""
    if isinstance(stmt, ast.AugAssign):
        if (isinstance(stmt.target, ast.Name) and stmt.target.id == "correct"
                and isinstance(stmt.op, ast.Add)
                and isinstance(stmt.value, ast.Constant) and stmt.value.value == 1):
            return True
    if isinstance(stmt, ast.Assign):
        for t in stmt.targets:
            if isinstance(t, ast.Name) and t.id == "correct":
                if isinstance(stmt.value, ast.BinOp):
                    if (isinstance(stmt.value.op, ast.Add)
                            and isinstance(stmt.value.left, ast.Name) and stmt.value.left.id == "correct"
                            and isinstance(stmt.value.right, ast.Constant) and stmt.value.right.value == 1):
                        return True
    return False


def check_accuracy_calculation(tree: ast.Module) -> bool:
    """
    檢查是否有計算 accuracy 的邏輯
    """
    source_has_accuracy = False
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id == "accuracy":
            source_has_accuracy = True
            break
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == "accuracy":
                    source_has_accuracy = True
                    break
    return source_has_accuracy


# ── AST 輔助函式 ─────────────────────────────────


def _is_comparison(test, left_name: str, right_val, is_variable=False) -> bool:
    """檢查 test 是否為 left_name == right_val 的比較"""
    if isinstance(test, ast.Compare):
        if len(test.ops) == 1 and isinstance(test.ops[0], ast.Eq):
            left = test.left
            if isinstance(left, ast.Name) and left.id == left_name:
                if len(test.comparators) == 1:
                    comp = test.comparators[0]
                    if is_variable:
                        return isinstance(comp, ast.Name) and comp.id == right_val
                    else:
                        return isinstance(comp, ast.Constant) and comp.value == right_val
    return False


def _is_time_time_call(node) -> bool:
    """檢查是否為 time.time() 呼叫"""
    if isinstance(node, ast.Call):
        func = node.func
        if isinstance(func, ast.Attribute):
            if func.attr == "time" and isinstance(func.value, ast.Name) and func.value.id == "time":
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
                print(f"\n✅ {stu_name} 同學，typing_game 的成績已成功傳送！")
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
    print("🎮 Typing Game 作業檢查器")
    print("=" * 50)

    # 讀取並解析原始碼
    source = read_source(TARGET_FILE)
    tree = parse_ast(source)

    # 1. 執行模擬檢查 (任務 1)
    l1, l2, l3 = check_limit_logic(source)
    limit_passed = (l1 == 15 and l2 == 30 and l3 == 60)
    
    # 建立限額邏輯的錯誤訊息
    limit_hint = "💡 提示：請確認模式 1 為 15s, 模式 2 為 30s, 模式 3 為 60s。"
    if not limit_passed:
        if l2 != 30: limit_hint = "💡 提示：模式 2 應該要設定 limit = 30（你現在是 {}）".format(l2)
        elif l3 != 60: limit_hint = "💡 提示：模式 3 應該要設定 limit = 60（你現在是 {}）".format(l3)

    # 執行各項檢查
    checks = [
        (
            "任務 1：挑戰模式設定 (15s / 30s / 60s)",
            limit_passed,
            limit_hint,
        ),
        (
            "任務 2：修改 while 迴圈的條件",
            check_while_condition(tree),
            "💡 提示：把 while True 改成 while time.time() < end_time",
        ),
        (
            "任務 3-1：判斷輸入與目標是否一致 (if u_in == target:)",
            check_task3_if_condition(tree),
            "💡 提示：在 input 之後，使用 if 來比較 u_in 是不是等於 target。",
        ),
        (
            "任務 3-2：答對時加分 (correct += 1)",
            check_task3_increment(tree),
            "💡 提示：在 if 判斷式成立的區塊內，將 correct 的數值加 1。",
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
        print("😢 還有幾個地方需要修正，加油！")
        print("   修改完成後，再執行一次這個檢查器。")
        print("-" * 50)
        sys.exit(1)

    print("\n" + "=" * 50)
    print("🎉 恭喜！所有檢查都通過了！")
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
