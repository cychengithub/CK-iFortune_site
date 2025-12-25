import os
import urllib.parse

def final_update_index(base_dir="docs"):
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
            
            # 關鍵修正：對路徑進行編碼以解決 404
            safe_folder = urllib.parse.quote(folder)
            content += f"\n## [{title}]({safe_folder}/)\n"
            
            if files:
                for f in files[:3]:
                    name = f.replace(".md", "")
                    safe_file = urllib.parse.quote(f)
                    content += f"* [{name}]({safe_folder}/{safe_file})\n"
            else:
                content += "* (目前此分類尚無文章)\n"
            content += "\n---\n"

    with open(os.path.join(base_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ 修正後的 index.md 已生成，請重新部署測試。")

if __name__ == "__main__":
    final_update_index()