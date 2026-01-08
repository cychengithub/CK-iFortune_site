import os

def update_pages_configurations(base_dir="docs"):
    for root, dirs, files in os.walk(base_dir):
        # 排除根目錄，只處理子資料夾
        if root == base_dir:
            continue
            
        pages_file = os.path.join(root, ".pages")
        
        # 強制寫入排序規則：按標題(日期)排序，並反向(最新在前)
        content = [
            "sort_by: title\n",
            "sort_reverse: true\n"
        ]
        
        with open(pages_file, "w", encoding="utf-8") as f:
            f.write("order: desc\n")
            f.writelines(content)
        print(f"✅ 已修正並設定排序: {pages_file}")

if __name__ == "__main__":
    update_pages_configurations()