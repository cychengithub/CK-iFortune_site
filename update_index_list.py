import os
import urllib.parse # 必須引入此模組來處理 URL 編碼

def final_update_index(base_dir="docs"):
    # 資料夾清單（請確保與您的實際目錄名稱完全一致）
    categories = {
        "AI Business": "🤖 人工智慧 AI Business",
        "AI Infrasture": "🤖 人工智慧 AI Infrasture",
        "AI Hardware System": "🤖 人工智慧 AI Hardware & System",
        "AI Software Service": "🤖 人工智慧 AI Software & Service",
        "Politics Economics": "📊 政治總體經濟 Politics & Economics",
        "Investment": "📈 投資 Investment",
        "Semiconductor": "📟 半導體 Semiconductor",
        "Robotics EV Automation": "🦾 機器人和電動車 Robotics & EV",
        "Crypto": "🪙 加密貨幣 Crypto",
        "Commodity Energy": "⚡ 綠能與能源技術 Green & Energy Technology",
        "Bio Life Science Healthcare": "🧬 醫藥 & 生物科技 Bio & Life Science",
        "Life Art": "🎨 生活與藝術 Life & Art"
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
            files = [f for f in os.listdir(folder_path) if f.endswith(".md") and f != "index.md"]
            files.sort(reverse=True) 
            
            # 修正 1：對資料夾名稱進行 URL 編碼
            safe_folder = urllib.parse.quote(folder)
            content += f"## [{title}]({safe_folder}/)\n"
            
            if files:
                for f in files[:5]: # 顯示最新 5 篇
                    name = f.replace(".md", "")
                    # 修正 2：對檔案名稱進行 URL 編碼，解決 404 問題
                    safe_file = urllib.parse.quote(f)
                    content += f"* [{name}]({safe_folder}/{safe_file})\n"
            else:
                content += "* (目前此分類尚無文章)\n"
            content += "\n---\n"

    with open(os.path.join(base_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ 首頁 index.md 已更新（路徑已自動轉碼，解決 404 問題）！")

if __name__ == "__main__":
    final_update_index()