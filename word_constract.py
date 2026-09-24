import json
import os

JSON_FILE = 'words.json'

def load_existing_words():
    """載入現有的 words.json 資料"""
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("⚠️ 警告：words.json 格式有誤，將建立新的單字列表。")
            return []
    return []

def save_words(words_list):
    """將單字列表寫入 words.json"""
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(words_list, f, ensure_ascii=False, indent=2)

def main():
    words = load_existing_words()
    print("=== 📖 單字庫批量快速寫入工具 ===")
    print(f"目前 words.json 已有 {len(words)} 個單字。\n")

    # 步驟 1：先設定年級
    print("請選擇本次要輸入的單字年級：")
    print("[1] 一年級  [2] 二年級  [3] 三年級 (預設: 1)")
    level_input = input("選擇年級 (1/2/3): ").strip()
    
    level_map = {"1": "一年級", "2": "二年級", "3": "三年級"}
    current_level = level_map.get(level_input, "一年級")
    
    print(f"\n✅ 已設定模式：連續建立【{current_level}】單字")
    print("提示：在輸入「英文單字」時直接按 Enter 即可結束並存檔。\n")

    count = 0
    while True:
        print("-" * 30)
        word = input("英文單字 (Word): ").strip()
        # 若單字欄位直接 Enter，則結束輸入
        if not word:
            print("\n👋 結束輸入。")
            break

        meaning = input("中文意思 (Meaning): ").strip()

        # 自動帶入剛才設定好的年級
        new_entry = {
            "word": word,
            "meaning": meaning,
            "level": current_level
        }
        words.append(new_entry)
        count += 1
        print(f"➕ 已加入: {word} ({meaning}) [{current_level}]")

    if count > 0:
        save_words(words)
        print(f"\n🎉 成功將 {count} 個【{current_level}】新單字儲存至 {JSON_FILE}！(總計 {len(words)} 個單字)")
    else:
        print("未新增任何單字。")

if __name__ == "__main__":
    main()