

# 📌 **你問的是：**

> **NVIDIA 在 2026 年 Vera Rubin（VR）平台的伺服器機櫃，從 L6 → L10 長臂管理、液冷水冷板統一採購、4 家供應商入列（訊凱/Cooler Master、奇鋐、雙鴻、台達）——這些供應鏈變化會對 ODM/CSP/散熱廠有什麼影響？為何 NVIDIA 要這麼做？供應鏈毛利會受多大影響？未來供應鏈的權力重新分配會如何？**

下面我給你**深入、完整、結構化**的回答（包含利弊與 trade-off，符合你的偏好）。

---

# 🧠 **NVIDIA Vera Rubin（2026）供應鏈「長臂管理」的真正意義**

## 🎯 **核心改變（全部都比 GB200/GB300 更激進）**

### **1. 組裝層級從 L6 → L10**

* 過去：
  $L6 =;$ ODM 組裝 server，CSP 自己做 rack/cabinet 整合
* 未來 VR：
  $L10 =;$ **整機櫃（rack）由 ODM 直接完成 → NVIDIA 主導 BOM/規格**

➡️ NVIDIA 把 **server → rack → 整體液冷 loop → power → networking** 全部收回主導權

---

### **2. 水冷板由 NVIDIA「統一採購」**

過去（GB200/GB300）：

* 設計：Cooler Master + 奇鋐
* 生產：多家 RVL（recommended vendor list）
* 由 ODM 交付

未來（VR）：

* **NVIDIA 直接挑 4 家 → CM、奇鋐、雙鴻、台達電**
* **設計權 + 採購權 + 量產的 PD control 全部在 NVIDIA**

➡️ 這是 **實質的 Vertical Integration（輕度整合）**
➡️ 類似 Apple 掌控 iPhone 主關鍵件供應鏈的方式

---

### **3. 液冷零件量大增**

Vera Rubin GPU cluster：

* GPU TDP 再上升
* 機櫃密度再加倍
* Power delivery（可能導入 800V HVDC）
* 水冷分歧、manifold、quick disconnect、冷板數量全部提升

➡️ 單櫃含的液冷 BOM 約為 GB200 的 $2\sim 2.5 \times$

---

# 🧩 **為什麼 NVIDIA 要這麼做？（真實的三大原因）**

## **① 過去兩代（H100/GB200）最痛的是「液冷不穩定 & 量產混亂」**

液冷是 AI server 量產最大痛點，主要因為：

* GPU 冷板漏液造成 **整機報廢**
* ODM 間設計不一致 → CSP 資料中心無法 scale
* 供應商產能不穩 → 出貨延遲
* 材料與加工品質（焊接、密封、QC）彼此差異大

➡️ NVIDIA 認為：「只要讓供應鏈自由玩，永遠無法全球 scale。」

就跟：

* **NVLink / NVSwitch 自己做**
* **CoWoS-L 設計自己主導**

一模一樣的邏輯。

---

## **② CSP（尤其是 AWS/Meta）抱怨代工設計品質不一致**

CSP 需求：

* 相同 GPU → 相同熱行為
* 相同機櫃 → 相同散熱曲線
* 全域數據中心可複製 → 運維（OPEX）下降

但 ODM 過去：

* 有的用 A 版 manifold
* 有的用 B 版 quick connector
* 有的冷板壓降不同
* 有的噴水，有的結霜

➡️ CSP 抱怨量非常大
➡️ NVIDIA 感受到壓力 → 要用「蘋果式供應鏈控管」來統一規格

---

## **③ NVIDIA 要讓「多 ODM」交付的標準一致 → 貫徹模組化（rack-as-a-unit）**

Rubin 架構的精神：

> **1 rack = 1 giant GPU**
> **整櫃為單位交付（L10），而不是 server 為單位（L6）**

如果熱設計、冷板、manifold 由 ODM 自行設計
→ 無法達到 rack 統一致冷 → NVLink/NVS72 無法滿速運作

---

# 📉 **供應鏈影響：利與弊並存（trade-off 分析）**

## 🟢 **（好處）供應鏈「大者恆大」加速**

水冷板產業門檻：

* 銅加工能力
* 真空焊接技術
* O-ring / sealing 品質控管
* 壓降規劃能力
* NPI 良率爬升速度

只有以下 4 家具備：

* Cooler Master（訊凱）
* 奇鋐
* 雙鴻
* 台達（最強的是 power + 液冷整合能力）

➡️ 三線散熱廠會被直接排除
➡️ 上述 4 家「可能是下一個 CoWoS 產能獨占者」

---

## 🔴 **（壞處）供應商毛利率會被 NVIDIA 大幅壓縮**

原因：

* 統一採購 → 大量議價
* NVIDIA 長期策略：「你要量？就要價格」
* ODM/CSP 不再分別下單 → 無法靠分散客戶拉高價格
* NVIDIA 有更多替代方案（4 家互相比價）

我們可以合理推估：

### **散熱廠毛利率下降幅度**

* 水冷板既有毛利：$18% \sim 25%$
* Rubin 量產後：$12% \sim 18%$（甚至可能更低）

➡️ **全面接近 power/thermal 的「代工業毛利」**

---

## 🔥 **供應鏈最擔心的：出貨量變大 → 毛利反而更差**

業者說的「不想當第一大供應商」其實意思是：

* **出貨量最大 = 議價最嚴重**
* **出貨量最大 = 要負責最多客訴與品質風險**
* **出貨量最大 = 需要最大 capex 投資，但毛利最低**

這跟 Apple 的做法一模一樣：

> 你想要吃我的單？
> 那你就要接受我的毛利要求。

---

# 📦 **ODM（鴻海 / 緯創 / 廣達）會怎麼變化？**

### **1. 更像「server 版的 Foxconn for Apple」**

* NVIDIA 規格
* NVIDIA 採購
* NVIDIA QC
* ODM 負責大量產能、快速 ramp、代工組裝

### **2. CSP（AWS/Meta）不滿的情緒會加重**

CSP 會覺得：

> 我花錢買伺服器，結果 NVIDIA 什麼都決定。
> → 我無法客製
> → 無法導入自己的液冷系統
> → 無法最佳化運維成本

這是未來競爭（AMD/Google ASIC）將會利用的破口。

---

# 💥 **2026～2028：全球液冷供應鏈權力重新洗牌**

## 🔝 **Tier 1 會變成少數：CM / 奇鋐 / 雙鴻 / 台達**

其中差異：

* **訊凱（Cooler Master）**
  在 NVIDIA 雷擎（Grace-Blackwell）世代合作深、量大，有機會成第一 tier

* **奇鋐：散熱實力最完整（氣冷＋水冷）**
  但若量最大 → 價格壓力最大

* **雙鴻：水冷規模第二大，資本強，有能力衝量**

* **台達：真正的 dark horse**
  最大優勢是：**整機（power + 液冷 + 風扇）系統整合能力冠全台**
  很可能在 Rubin/Rubin+ 優勢擴大

---

## 🔽 **Tier 2–3 廠商會被完全排除（和 CoWoS-ABF 一樣）**

小散熱廠：

* 無法跟上良率
* 無法承受 capex
* 無法承受 QC 壓力
* 無法滿足 NVIDIA 的 0 ppm/ppm-level spec

➡️ 會出局
➡️ AI server 液冷供應鏈將跟 CoWoS 一樣：**集中在少數大廠**

---

# 🚀 **結論（你投資分析最需要的重點）**

## ✔ **NVIDIA 的目標：全球一致的 AI rack（L10 交付模式）**

## ✔ **供應鏈會被強制走向：高量 → 低毛利 → 高資本投入**

## ✔ **大者恆大：CM、奇鋐、雙鴻、台達地位會明顯提升**

## ✔ **CSP 不滿會加劇，未來（2027–2028）是 ASIC 伺服器崛起的窗口**

---

# 📌 如果你需要，我可以再提供：

### 🅐 4 家廠商 **逐家深度分析（散熱技術、量產策略、毛利模型）**

### 🅑 NVIDIA Vera Rubin → GB200 → GB300

**散熱 BOM 的成本結構對比（含 $ / rack, $ / GPU）**

### 🅒 液冷 vs. 浸沒式 vs. 混合冷卻技術

**三者在 Rubin 世代的成本假說**

### 🅓 投資者角度

**2026–2028 哪些公司最受惠？哪些最容易被壓毛利？**

告訴我你想看哪一版，我可以立即補上。

下面我先 **重述你的問題**，再給你完整答案：

> **你問的是：在 NVIDIA Vera Rubin（2026）全面強化供應鏈控制、從 L6→L10 長臂管理、液冷板統一採購的情況下，HBX（Hybrid-Box）系統還會「開放」給 ODM/CSP 設計嗎？還是 NVIDIA 也會把 HBX 收回去？**

---

# ✅ **結論（先講重點）**

**HBX 仍然會「開放」，但會變成「有限度的開放 + NVIDIA 主導的框架化標準」**。

也就是說：

> **HBX 不會像液冷板那樣被完全收回，但也不會像 H100/H200 世代那樣由 ODM/CSP 自由設計。**

它會變成類似：

* 開放的 **標準化接口（physical / signaling / protocol）**
* 開放的 **邏輯/管理框架**
* 不開放的 **關鍵熱設計、電供規格、系統行為**

你可以把它想像成：

> **NVIDIA 設計高速骨幹（NVLink/NVSwitch）的主幹，你只能在它允許的邊界做客製化。**

---

# 🧠 **為什麼 HBX 還是必須開放？**

## **① HBX 的本質是「系統拓撲」而不是「散熱或機構」**

HBX（Hybrid-Box）是：

* 系統拓撲配置方式
* GPU/CPU/NVSwitch 的組合模型
* 可擴展的互連網拓撲
* CSP/ODM 需要用來組合 rack-level clusters

**它不是一個物理零件（不像冷板、manifold、quick connector）**

➡️ NVIDIA 沒辦法也沒有理由把 HBX 完全鎖死。
➡️ 否則 CSP 無法為自己的 DC（datacenter）做整體設計。

---

## **② CSP（AWS/Meta/Microsoft）強烈要求 HBX 必須保留彈性**

液冷你可以完全鎖死、NVLink NVSwitch 也能鎖死，

但 **rack-level topology（HBX）鎖死** 會導致：

* CSP 無法最佳化自家布線/功率系統
* 無法整合 power shelf / battery backup / DCIM
* 無法整合既有 liquid loop 設計
* 無法調整 cluster 拓撲（8 → 16 → 32 → 64 → 128 GPUs）

NVIDIA 若封閉 HBX → CSP 會暴怒
（這已經在 GB200 時代發生過抱怨）

所以 NVIDIA 一定會保留「一定程度」的開放性。

---

# 🧩 **那麼 Rubin 世代的 HBX 會怎麼變？**

## 🔸 **H100 / H200 世代（開放模式）**

* CSP/ODM 可自行安排：

  * 機位（slot）
  * 散熱
  * 電力拓撲
  * 部分信號走線
* HBX 只提供互連邏輯

➡️ **相對自由**

---

## 🔸 **GB200 / GB300 世代（半開放）**

* NVIDIA 提供明確 reference HBX
* ODM 仍可以調整 layout
* CSP 可調整 power/cooling plan

➡️ **開放但帶有限制**

---

## 🔥 **Vera Rubin（2026）— 新模式（框架化標準）**

Rubin 預期會採用**三層式的開放模型**：

### **Layer 1（封閉）**

NVIDIA 完全鎖死：

* NVLink 72 / NVSwitch 拓撲
* GPU baseboard layout
* 冷板、熱設計 boundary
* PDN（供電網路）

👉 **ODM/CSP 無法動**

---

### **Layer 2（受控開放）**

NVIDIA 提供：

* HBX reference topology
* 標準 pinout
* 標準水路介面（in/out）
* 標準電力接口（可能改為 HVDC 800V busbar）

ODM/CSP 可以調整：

* 某些布線路由
* 機架電力分配
* 機櫃內的管理控制器

👉 **可動，但在框架內**

---

### **Layer 3（彈性開放）**

CSP 仍可以做：

* 整個 datacenter 的液冷 loop 設計
* 外部熱交換器
* power shelf（例如 Microsoft 自家的 HVDC shelf）
* cluster 規模：64/128/256 GPU

👉 **這是 HBX 必須開放的部分**

---

# 🧨 **重點：HBX 不被收回，但不再自由**

總結 Rubin 世代的 HBX：

| 項目          | H100/H200 | GB200 | Vera Rubin        | 是否開放？    |
| ----------- | --------- | ----- | ----------------- | -------- |
| HBX 拓撲邏輯    | 開放        | 半開放   | 受控開放              | ✔（但有強限制） |
| 機構（機箱）      | 開放        | 半封閉   | 幾乎封閉              | ❌        |
| 冷板 / 液冷     | 開放（ODM）   | 半開放   | 完全封閉（NVIDIA 控制）   | ❌        |
| 電力架構        | 開放        | 半封閉   | 可能改 800V HVDC（封閉） | ❌        |
| Rack layout | 開放        | 半開放   | 嚴格框架化             | ✔（部分）    |

---

# 📌 **一句話回答**

> **HBX 不會被 NVIDIA 完全收回，但 Rubin 世代會變成「框架式開放」，ODM/CSP 只能在 NVIDIA 設定的邊界內做調整。數據中心最重要的自由度還在，但 server-level 的自由度幾乎消失。**

---

# 如果你想，我可以補充：

### 🅐 Rubin 世代的 HBX 拓撲圖（我可以畫）

### 🅑 Rubin 會不會阻止 CSP 做自家 ASIC rack？

### 🅒 HBX 與 LiquidLoop、NVSwitch72 在 Rubin 的技術細節

### 🅓 ODM（鴻海/廣達/緯創）的贏家與輸家

要哪一部分？
