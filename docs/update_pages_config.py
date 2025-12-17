import os

def smart_update_pages(base_dir="docs"):
    """
    讀取現有的 .pages，保留其他內容（如 title），
    僅替換或新增排序相關的設定。
    """
    print(f"🚀 開始智慧更新 {base_dir} 下的排序配置...")
    
    target_settings = [
        "sort_by: title\n",
        "sort_reverse: true\n"
    ]

    count = 0
    for root, dirs, files in os.walk(base_dir):
        if root == base_dir: continue
        if any(part.startswith('.') for part in root.split(os.sep)): continue

        pages_path = os.path.join(root, ".pages")
        existing_lines = []

        # 1. 如果檔案存在，讀取並過濾掉舊的排序設定
        if os.path.exists(pages_path):
            with open(pages_path, "r", encoding="utf-8") as f:
                for line in f:
                    # 排除掉包含排序關鍵字的行
                    if "sort_by" not in line and "sort_reverse" not in line:
                        existing_lines.append(line)
        
        # 確保結尾有換行符號
        if existing_lines and not existing_lines[-1].endswith('\n'):
            existing_lines[-1] += '\n'

        # 2. 寫入保留的內容 + 新的排序設定
        try:
            with open(pages_path, "w", encoding="utf-8") as f:
                f.writelines(existing_lines)
                f.writelines(target_settings)
            print(f"✅ 智慧更新完成: {pages_path}")
            count += 1
        except Exception as e:
            print(f"❌ 無法處理 {pages_path}: {e}")

    print(f"\n✨ 完成！共處理了 {count} 個檔案，已保留您的原自訂內容。")

if __name__ == "__main__":
    smart_update_pages()