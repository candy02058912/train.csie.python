"""
title: 練習題 009：遊戲分數統計
score: 1
quest_html: 我們將模擬一個遊戲分數統計系統。請使用<b>「組合賦值運算子」</b>（如 <code>+=</code>, <code>*=</code>, <code>/=</code>）來更新變數，並最後使用 <b>F-String</b> 來輸出結果。<br><br><b>任務步驟：</b><br>1. 將四場比賽的分數加到 <code>total_score</code>。<br>2. 老師決定給予表現傑出的同學 50% 的加分，請對 <code>total_score</code> 使用 <code>*=</code> 乘以 1.5。<br>3. 計算平均分數，請將 <code>total_score</code> 除以 4，並用 <code>/=</code> 更新回 <code>total_score</code>。<br>4. 使用 <code>print()</code> 搭配 <code>f-string</code> 輸出：<code-snippet>最終平均分數為：{分數}</code-snippet> (請輸出原始數字即可，不用四捨五入)。
"""

# ==== STARTER CODE ====
game_one_score = 90
game_two_score = 80
game_three_score = 60
game_four_score = 100

total_score = 0

# 在這以下開始寫程式碼


# ==== TEST CODE ====
import sys

def run_tests():
    try:
        if total_score == 123.75:
            # 檢查輸出格式
            output = sys.stdout.get_value().strip()
            expected_text = "最終平均分數為：123.75"
            if expected_text in output:
                return "SUCCESS"
            else:
                return f"❌ Console 內容不正確。\n\n[預期應該包含]：\n{expected_text}\n\n[你的輸出是]：\n{output}"
        else:
            return f"❌ 數字計算不正確喔。\n\n[預期應該是]：\n123.75\n\n[你的計算結果是]：\n{total_score}\n\n[提示]：請檢查是否正確使用了 +=, *= 和 /=。"
            
    except Exception as e:
        return f"執行測試時發生錯誤：{str(e)}"
