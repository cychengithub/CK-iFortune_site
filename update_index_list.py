import os

def final_update_index(base_dir="docs"):
    categories = {
        "AI Business": "🤖 人工智慧 AI Business",
        "AI Infrasture": "🤖 人工智慧 AI Infrasture",
        "AI Hardware & System": "🤖 人工智慧 AI Hardware & System",
        "AI Software & Service": "🤖 人工智慧 AI Software & Service",
        "Politics & Economics": "📊 政治總體經濟 Politics & Economics",
        "Investment": "📈 投資 Investment",
        "Semiconductor": "📟 半導體 Semiconductor",
        "Robotics EV & Automation": "🦾 機器人和電動車 Robotics & EV",
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

<img src="image.png" width="150">

> ## 🧠 **「智慧獲取財富」**
> **「知識不是用來收藏的，而是用來連結與生長的。」**

# <span style="color: red; font-weight: bold;">請直接點擊下方分類</span>，即可進入該領域的文章列表：

---
"""
    
    content = header
    for folder, title in categories.items():
        folder_path = os.path.join(base_dir, folder)
        if os.path.exists(folder_path):
            # 抓取檔案並依標題日期倒序排列
            files = [f for f in os.listdir(folder_path) if f.endswith(".md") and f != "index.md"]
            files.sort(reverse=True) 
            
            # 修正：直接使用原始資料夾名稱，MkDocs 能更好地解析
            content += f"## [{title}]({folder}/)\n"
            
            if files:
                for f in files[:5]:
                    name = f.replace(".md", "")
                    # 直接使用原始檔名，解決 404 問題
                    content += f"* [{name}]({folder}/{f})\n"
            else:
                content += "* (目前此分類尚無文章)\n"
            content += "\n---\n"

    with open(os.path.join(base_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ 首頁 index.md 已更新（路徑已優化）！")

if __name__ == "__main__":
    final_update_index()