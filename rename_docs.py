import os
import re

def batch_rename_files(base_dir="docs"):
    # 正規表達式：尋找標題後方帶有 (YYYY-MM-DD) 格式的檔案
    # 捕獲組 1: 標題內容
    # 捕獲組 2: 日期內容
    pattern = re.compile(r"^(.*)\s\((\d{4}-\d{2}-\d{2})\)\.md$")

    print(f"開始掃描資料夾: {base_dir} ...")
    
    # 遞迴掃描所有子資料夾
    for root, dirs, files in os.walk(base_dir):
        for filename in files:
            match = pattern.match(filename)
            if match:
                original_title = match.group(1).strip()
                date_str = match.group(2)
                
                # 新檔名格式：YYYY-MM-DD 原標題.md
                new_filename = f"{date_str} {original_title}.md"
                
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_filename)
                
                try:
                    os.rename(old_path, new_path)
                    print(f"✅ 已更名: {filename} -> {new_filename}")
                except Exception as e:
                    print(f"❌ 錯誤: 無法更名 {filename}, 原因: {e}")

if __name__ == "__main__":
    # 執行前建議先備份您的 docs 資料夾
    batch_rename_files()
    print("\n所有符合格式的檔案已處理完畢！")