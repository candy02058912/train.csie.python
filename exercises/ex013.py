"""
title: 練習題 013：True/False 大對決
score: 1
quest_html: <b>大腦體操時間！</b>請試著在腦中模擬 Python 的運作，判斷下列 10 個比較運算式會得到 <code>True</code> 還是 <code>False</code>。<br><br>提示：注意<b>優先順序</b>，先算括號內的，再算外面的。
"""

# ==== STARTER CODE ====
# 請直接填入 True 或 False，不要偷偷讓 Python 幫你算唷～

# 第 1 題： 3 == 5
ans_01 = 

# 第 2 題： 10 > 5
ans_02 = 

# 第 3 題： 7 <= 7
ans_03 = 

# 第 4 題： "apple" != "Apple"
ans_04 = 

# 第 5 題： 100 >= 99.9
ans_05 = 

# 第 6 題： 10 % 3 == 1
ans_06 = 

# 第 7 題： 5 ** 2 > 20
ans_07 = 

# 第 8 題： 1 == "1"
ans_08 = 

# 第 9 題： (5 + 5) != "10"
ans_09 = 

# 第 10 題： (3 <= 5) != (3 >= 5)
ans_10 = 


# ==== TEST CODE ====
import ast

def run_tests():
    # 定義第 1 到第 10 題的正確解答
    expected_answers = {
        'ans_01': False,
        'ans_02': True,
        'ans_03': True,
        'ans_04': True,
        'ans_05': True,
        'ans_06': True,
        'ans_07': True,
        'ans_08': False,
        'ans_09': True,
        'ans_10': True
    }
    
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查學生是否直接輸入了比較運算子
        # studentCode 是 Pyodide 執行時，注入到 global scope 的變數，包含學生寫的原始碼字串
        if 'studentCode' in globals():
            try:
                tree = ast.parse(studentCode)
                for node in ast.walk(tree):
                    # 如果發現 Compare 節點 (包含 >, <, ==, !=, >=, <=)
                    if isinstance(node, ast.Compare):
                        return "❌ 系統偵測到你使用了比較運算子 ( ==, >, <, != 等 )。\n請務必自己用大腦算出 True 或 False 填入等號右邊，不能讓 Python 幫你算喔！😜"
            except SyntaxError as e:
                return f"❌ 語法錯誤：{str(e)}"
        
        # 檢查答案是否正確
        for var_name, expected_val in expected_answers.items():
            if var_name not in globals():
                 return f"❌ 找不到變數 `{var_name}`，請不要刪除任何一題的變數喔！"
            
            student_val = globals()[var_name]
            
            # 首先確保型別真的是 bool，以免學生輸入 "True" (字串) 或 1 (整數)
            if type(student_val) is not bool:
                 return f"❌ {var_name} 的型別錯誤！"
                 
            # 檢查 True/False 是否正確
            if student_val is not expected_val:
                 # 若錯誤，動態抓出題號以便提示
                 q_num = var_name[-2:]
                 return f"❌ 第 {q_num} 題答錯囉！請再仔細想一想！"
        
        # 全部都答對才給過
        return "SUCCESS"
        
    except Exception as e:
        return f"❌ 測試系統執行時發生錯誤：{str(e)}"
