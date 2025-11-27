import re
import os

def convert_obsidian_links(content):
    """將 Obsidian 連結 ![[...]] 轉換為標準 Markdown 連結 ![](...)"""
    # 正規表達式：捕捉 ![[ 和 ]] 之間的內容，包括圖片
    pattern = r'!\[\[(.*?)\]\]'
    # 替換：使用標準 Markdown 格式，並將捕捉的內容 (\1) 作為路徑
    replacement = r'![](\1)'
    
    # 為了 web 相容性，將路徑中的反斜線 \ 替換為正斜線 /
    content = content.replace('\\', '/')

    return re.sub(pattern, replacement, content)

def process_publishing_files(directory="docs"):
    """遞迴處理 docs/ 目錄下所有 Markdown 檔案"""
    files_converted = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.md', '.markdown')):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = convert_obsidian_links(content)
                
                # 如果內容有變更，則寫回檔案
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    files_converted += 1
    
    print(f"Python 連結翻譯完成，共修改 {files_converted} 個檔案。")

if __name__ == "__main__":
    process_publishing_files()