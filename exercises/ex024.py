"""
title: 練習題 024：字典基礎操作
score: 1
quest_html: 實習生小明剛學會 Python 的字典 (dict)，他在整理一份課程資料 <code>course_info</code> 時遇到了一些困難。<br>請依照程式碼下方的步驟提示，幫他完成所有的資料操作吧！
"""

# ==== STARTER CODE ====
course_info = {
    "name": "Python 基礎課程",
    "teacher": "Candy",
    "students": 30,
    "note": "記得帶筆電"
}

# 1. 取得 course_info 字典的長度，並將結果存入變數 info_len


# 2. 取得字典中 key 為 "teacher" 的值，存入變數 teacher_name


# 3. 使用 get() 取得 key 為 "assistant" 的值
# 若不存在預設給定字串 "Pooh"，存入變數 assistant_name


# 4. 新增一筆資料，key 為 "location"，value 為 "臺灣大學資訊系統訓練班"


# 5. 將 key 為 "students" 的值修改為數值 50


# 6. 刪除 key 為 "note" 的資料


# ==== TEST CODE ====
import ast

def run_tests():
    if 'studentCode' not in globals():
        return "❌ 系統錯誤：無法讀取你的程式碼。"
        
    try:
        # [防作弊機制]：使用 AST (語法樹) 檢查
        tree = ast.parse(studentCode)
        has_len = False
        has_get = False
        has_del = False
        
        for node in ast.walk(tree):
            # Check for len()
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'len':
                has_len = True
            
            # Check for .get()
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == 'get':
                has_get = True
                
            # Check for del
            if isinstance(node, ast.Delete):
                has_del = True

        if not has_len:
            return "❌ 任務失敗！請使用 `len()` 函式來獲取字典長度。"
        if not has_get:
            return "❌ 任務失敗！請使用 `.get()` 方法來取得 'assistant' 的值。"
        if not has_del:
            return "❌ 任務失敗！請使用 `del` 來刪除資料。"
            
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
        'print': print,
        'len': len
    }
    
    try:
        exec(studentCode, global_env)
        
        # 1. 檢查 info_len
        if "info_len" not in global_env:
            return "❌ 找不到變數 `info_len`，請檢查是否有宣告變數並指派正確的值。"
        elif global_env["info_len"] != 4:
            return f"❌ `info_len` 的值不正確。\n\n[預期應該是]：\n4\n\n[你的答案是]：\n{global_env['info_len']}"
            
        # 2. 檢查 teacher_name
        if "teacher_name" not in global_env:
            return "❌ 找不到變數 `teacher_name`，請檢查是否有正確擷取 key 為 'teacher' 的值。"
        elif global_env["teacher_name"] != "Candy":
            return f"❌ `teacher_name` 的值不正確。\n\n[預期應該是]：\nAlan\n\n[你的答案是]：\n{global_env['teacher_name']}"
            
        # 3. 檢查 assistant_name
        if "assistant_name" not in global_env:
            return "❌ 找不到變數 `assistant_name`，請檢查是否有使用 get() 並指派給對應變數。"
        elif global_env["assistant_name"] != "Pooh":
            return f"❌ `assistant_name` 的值不正確。記得使用 get() 並給定預設值 'Pooh'。\n\n[預期應該是]：\nPooh\n\n[你的答案是]：\n{global_env['assistant_name']}"
            
        # 檢查 course_info 最後狀態
        if "course_info" not in global_env:
            return "❌ `course_info` 變數不見了！請勿刪除原始的字典變數。"
            
        course_info_final = global_env["course_info"]
        
        # 4. 檢查 location 新增
        if course_info_final.get("location") != "臺灣大學資訊系統訓練班":
            return f"❌ `course_info` 沒有成功新增資料。預期要有 key='location', value='臺灣大學資訊系統訓練班'。目前字典狀態是：\n{course_info_final}"
            
        # 5. 檢查 students 修改
        if course_info_final.get("students") != 50:
            return f"❌ `course_info` 的 'students' 沒有成功修改成 50 (注意型別要是整數唷)。目前字典狀態是：\n{course_info_final}"
            
        # 6. 檢查 note 刪除
        if "note" in course_info_final:
            return f"❌ `course_info` 裡面的 'note' 沒有被成功刪除。目前字典狀態是：\n{course_info_final}"
            
    except Exception as e:
        return f"❌ 執行錯誤：{str(e)}"
            
    return "SUCCESS"
