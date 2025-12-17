import os

def final_update_index(base_dir="docs"):
    # 嚴格對應您的資料夾名稱，不做任何路徑修改
    categories = {
        "Politics & Economics": "📊 政治總體經濟 Politics & Economics",
        "Investment": "📈 投資 Investment",
        "AI Technology": "🤖 人工智慧 AI Technology",
        "Robotics EV & Automation": "🦾 機器人和電動車 Robotics & EV",
        "Semiconductor": "📟 半導體 Semiconductor",
        "Crypto": "🪙 加密貨幣 Crypto",
        "Green & Energy Technology": "⚡ 綠能與能源技術 Green & Energy Technology",
        "Bio & Life Science": "🧬 醫藥 & 生物科技 Bio & Life Science",
        "Life & Art": "🎨 生活與藝術 Life & Art"
    }
    
    header = """---
hide:
  - toc
---
# 👋 歡迎來到 CK Intelligent Fortune 數位花園

> ## 🧠 **「智慧獲取財富」**
> **「知識不是用來收藏的，而是用來連結與生長的。」**

# <span style="color: red; font-weight: bold;">請直接點擊下方分類</span>，即可進入該領域的文章列表：

---
"""
    
    content = header
    for folder, title in categories.items():
        # folder 現在直接就是資料夾名稱，例如 "Politics & Economics"
        folder_path = os.path.join(base_dir, folder)
        
        if os.path.exists(folder_path):
            # 取得最新 3 篇文章，排除 index.md
            files = [f for f in os.listdir(folder_path) if f.endswith(".md") and f != "index.md"]
            files.sort(reverse=True)
            
            # 生成可點擊的大標題連結
            # 注意：Markdown 連結若路徑有空格，需使用 %20 或括號包圍，這裡程式會處理
            safe_path = folder.replace(" ", "%20")
            content += f"\n## [{title}]({safe_path}/)\n"
            
            # 在主頁列出最新文章標題
            if files:
                for f in files[:3]:
                    name = f.replace(".md", "")
                    # 文章連結也要處理空格
                    safe_file_path = f.replace(" ", "%20")
                    content += f"* [{name}]({safe_path}/{safe_file_path})\n"
            else:
                content += "* (目前此分類尚無文章)\n"
        else:
            print(f"⚠️ 警告：找不到資料夾 {folder_path}，請檢查路徑拼字。")

    with open(os.path.join(base_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ 首頁 index.md 已依照您的資料夾名稱更新完成！")

if __name__ == "__main__":
    final_update_index()