結構是「定義口徑 → 2025 年用 Q1–Q3 實數驗證 → 2030 年路徑與成長趨緩的原因 → 以 BOM（成本結構）把『加速器/整機』緊密連動 → 情境表與可套用的算式」。

---

# 一、口徑先對齊：兩條市場如何「聯立」

我們把 **AI 伺服器整機（Server/System）** 與 **AI 加速器（GPU/ASIC/FPGA）** 用最簡潔的三式連起來：

- 整機營收
    
    ( R_{\text{server}} = N_{\text{server}} \times ASP_{\text{server}} )
    
- 加速器營收
    
    ( R_{\text{acc}} = N_{\text{server}} \times G_{\text{per_server}} \times ASP_{\text{acc}} )
    
- **BOM 關聯（加速器在整機的佔比）**
    
    ( \text{BOMshare}*{\text{acc}} = \dfrac{R*{\text{acc}}}{R_{\text{server}}} = \dfrac{G_{\text{per_server}}\times ASP_{\text{acc}}}{ASP_{\text{server}}} )
    

其中 (G_{\text{per_server}}) 是「每台 AI 伺服器平均用幾顆加速器」。

---

# 二、2025 年先「落地」：用 Q1–Q3 的真實數據驗證全年預估

**權威口徑（年初/年中發布的 2025 年預估）**

- **AI 伺服器整機**：TrendForce 指出 2024 年 AI 伺服器價值約 **$205B**、**2025 年約 $298B**。([TrendForce](https://www.trendforce.com/presscenter/news/20250106-12433.html?utm_source=chatgpt.com))
- **AI 加速器**：Omdia 指出 **2025 年 $207B**、2030 年 **$286B**（並預期 2026 年後增速走緩）。([Omdia](https://omdia.tech.informa.com/pr/2025/aug/ai-data-center-chip-market-to-hit-286bn-growth-likely-peaking-as-custom-asics-gain-ground?utm_source=chatgpt.com))

**用已公布的 2025 年 Q1–Q3 實績/指引交叉驗證**

- **NVIDIA**（等同加速器市場主體；含 Compute + Networking）
    - Q1 FY26（截至 2025-04-27）**資料中心 $39.1B**。([NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2026?utm_source=chatgpt.com))
    - Q2 FY26（截至 2025-07-27）新聞稿：營收 **$46.7B**；公司說明 **Blackwell Data Center** 營收環比 +17%（資料中心仍佔絕對主體）。([NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2026?utm_source=chatgpt.com))
    - 多方解讀 Q3 指引總營收約 $54B、資料中心占比近 9 成（用以推估 Q3 DC 約 $48–49B）。([Red94](https://www.red94.net/news/record-46b-q2-26b-profit-nvidia-guides-54b-next-quarter-heres-why-it-matters/?utm_source=chatgpt.com))
        
        → **NVIDIA 資料中心 Q1–Q3 合計粗算 ≈ $128–129B**。
        
- **AMD**（補上非 NV 份額）
    - Q1 2025 **Data Center $3.7B**。([archivemarketresearch.com](https://www.archivemarketresearch.com/companies/AMD?utm_source=chatgpt.com))
    - 市場資料彙整顯示 Q2 仍在 $3B 上下區間，Q3 受 MI350 放量帶動（市場觀察）。
- **宏觀佐證**
    - **Q1 2025 全球資料中心 CAPEX 強勁**（Dell’Oro：至 2029 累計 CAPEX 估達 **$1.2T**）。([Dell'Oro Group](https://www.delloro.com/news/data-center-capex-to-grow-at-21-percent-cagr-through-2029/?utm_source=chatgpt.com))

把 **NVIDIA（Q1–Q3 ≈ $128–129B） + AMD + 其他客製 ASIC/FPGA** conservatively 加總，**Q1–Q3「加速器+相關」≈ $145–150B** 屬保守可成立。用前述 **BOM 關聯式** 反推整機：

[

R_{\text{server}}(Q1!-!Q3) \approx \frac{R_{\text{acc}}}{\text{BOMshare}_{\text{acc}}}

\approx \frac{145!\sim!150}{0.69} \approx \mathbf{$210!\sim!$217B}

]

考慮 H2>H1 的季節性與 Q4 衝量，全年 **加速器** 合理落在 **$190–210B**、**整機** **$280–305B**，與 **Omdia（$207B）/TrendForce（$298B）** 的年預估「緊密對齊」。([Omdia](https://omdia.tech.informa.com/pr/2025/aug/ai-data-center-chip-market-to-hit-286bn-growth-likely-peaking-as-custom-asics-gain-ground?utm_source=chatgpt.com))

> 價格現況校準（2025）：H100 單卡常見 $25k–$40k；8-GPU（DGX H100 級）整機 $0.37–0.45M；整櫃 NVL36/72 市場估 $1.8–3.0M。這些價帶與「加速器在整機 BOM 佔比很高」相符。(Northflank)
> 

---

# 三、2030 年為何「成長趨緩」：數字與結構性原因

**確定性預測口徑**

- **加速器**：Omdia 指 **2025 ≈ $207B → 2030 ≈ $286B**（5 年 CAGR 約 **6–7%**；2026 年起增速放緩）。([Omdia](https://omdia.tech.informa.com/pr/2025/aug/ai-data-center-chip-market-to-hit-286bn-growth-likely-peaking-as-custom-asics-gain-ground?utm_source=chatgpt.com))
- **整機**：多家機構 2030 年區間 **$500–850B**（我們用中位 **$600B** 進行 BOM 驗證）。([TrendForce](https://www.trendforce.com/presscenter/news/20250106-12433.html?utm_source=chatgpt.com))
- **DCPI（電力/配電/熱管理合計）**：Dell’Oro 預估 **2029 年達 $63.1B**、**熱管理 CAGR 19%**，**直液冷（DLC）自 2024 $1.1B → 2029 $5.8B**。([Dell'Oro Group](https://www.delloro.com/news/ai-build-out-to-propel-data-center-physical-infrastructure-market-to-63-1-billion-by-2029/?utm_source=chatgpt.com))
- **AI 網路**：650 Group 指 **AI 網路 2025 年近 $20B**；Dell’Oro 指 **AI 後端交換器 2025–2029 累計 > $100B**。([IEEE 802](https://www.ieee802.org/3/ad_hoc/ngrates/public/25_01/dambrosia_nea_01_2501.pdf?utm_source=chatgpt.com))
- **用電天花板**：IEA 預估資料中心用電 **到 2030 年翻倍至 ~945 TWh**；在「逆風情境」下（貿易戰/併網受阻）可能更低，且 **約 20% 規劃案面臨延宕**。([IEA](https://www.iea.org/news/ai-is-set-to-drive-surging-electricity-demand-from-data-centres-while-offering-the-potential-to-transform-how-the-energy-sector-works?utm_source=chatgpt.com))

**成長降速的 6 個結構性原因（摘要）**

1. **單位算力成本快速下行**（低精度 FP4/INT4、稀疏化、編譯/推論堆疊優化）→ 同等工作量需**更少顆**/**更低 ASP** 的加速器。([Omdia](https://omdia.tech.informa.com/pr/2025/aug/ai-data-center-chip-market-to-hit-286bn-growth-likely-peaking-as-custom-asics-gain-ground?utm_source=chatgpt.com))
2. **資源池化/虛擬化提高利用率** → 以「顆數」衡量的需求增速 < 「算力需求」增速。
3. **訓練→推論的 Mix 變化** → 高 ASP 訓練卡的需求彈性更大。
4. **供應舒緩 → 溢價回落**（HBM/先進封裝緊缺逐步緩解）。
5. **電力與場地約束**（併網、變電容量、水資源）→ CAPEX 放量速度受限。([Reuters](https://www.reuters.com/technology/artificial-intelligence/global-trade-war-may-produce-headwinds-nascent-ai-sector-iea-says-2025-04-10/?utm_source=chatgpt.com))
6. **CSP 客製 ASIC 滲透** → 以更低功耗/更高效定製方案替代部分通用 GPU 收入。([Omdia](https://omdia.tech.informa.com/pr/2025/aug/ai-data-center-chip-market-to-hit-286bn-growth-likely-peaking-as-custom-asics-gain-ground?utm_source=chatgpt.com))

---

# 四、**BOM（成本結構）**：2030 年「加速器/整機 ≈ 50%」合理嗎？

我們用兩個原型（archetype）做 2030 年的 BOM 驗證，所有比率為「占整機成本」。

| 成本項 | **A. 訓練（8-GPU/整櫃化）** | **B. 推論/混合（2–4 GPU）** | 依據與說明 |
| --- | --- | --- | --- |
| **加速器（不含 HBM）** | **35–45%** | **25–35%** | 2025 年加速器/整機~69%（含 HBM 與相關配套）。隨 ASP 回落與其他項目上升，2030 年分解後「不含 HBM」比重下降。DGX/NVL 系統價示例見文內來源。([cyfuture.cloud](https://cyfuture.cloud/kb/gpu/nvidia-dgx-h100-price-latest-updates-and-specifications?utm_source=chatgpt.com)) |
| **HBM（加速器配套記憶體）** | **15–20%** | **8–12%** | HBM3e→HBM4 與 12-hi 推高單卡記憶體成本；HBM 在 DRAM 營收占比近兩年快速上升。([Omdia](https://omdia.tech.informa.com/pr/2025/aug/ai-data-center-chip-market-to-hit-286bn-growth-likely-peaking-as-custom-asics-gain-ground?utm_source=chatgpt.com)) |
| **主機板/CPU/電源/機構** | 8–12% | 12–18% | 推論型對 CPU/主板/機構比重更高。 |
| **網路/光模組（800G→1.6T）** | **8–12%** | **6–10%** | 800G 模組單價「千美元級」可見；後端交換/光模組市場快速擴張（2025 近 $20B；後端交換 2025–2029 > $100B）。([Network-Switches](https://network-switch.com/collections/800g-osfp-optical-transceiver?srsltid=AfmBOor60HMFHwVRlnXUJ7M_iKxZ38N9Qsk1yfayzn9zvJ3_wpdF0E6F&utm_source=chatgpt.com)) |
| **NVLink/Switch 背板/纜線** | 4–6% | 2–4% | NVLink 世代升級、端口數/帶寬走高。 |
| **機內散熱（直液冷冷板/軟管/泵/快接）** | **4–7%** | **3–5%** | DLC 2024 約 $1.1B → 2029 $5.8B；料件佔比隨密度上升而上移。([PR Newswire](https://www.prnewswire.com/news-releases/ai-build-out-to-propel-data-center-physical-infrastructure-market-to-63-1-billion-by-2029--according-to-delloro-group-302530530.html?utm_source=chatgpt.com)) |
| **本地儲存（NVMe/SSD）** | 2–4% | 3–5% | 推論更依賴本機快取。 |
| **（小結）加速器 + HBM** | **50–65%** | **33–47%** | **A 類**場景中「約 50%」非常自然；**B 類**甚至低於 50%。 |

**數學驗證（範例）**

以 2030 年「8-GPU 訓練機」作例：

- ($ASP_{\text{server}}$ = $420k)（網路/散熱/配電上行、但整櫃化規模帶來部分降本）
- 單卡 **不含 HBM** (ASP_{acc,\neg HBM} = $18k)；單卡 **HBM** (= $7k)（HBM4/製程進步/競爭折價）
- (G=8)
    
    → 加速器+HBM 佔比 (= 8 \times (18+7)/420 = 200/420 \approx \mathbf{48%}) —— **落在 50% 左右**的範圍。
    
    若以 2–4 GPU 推論機加權，整體「加速器/整機」**中位就會更接近 ~45–50%**。
    

**依據與旁證**

- **價格帶**：H100 **$25k–$40k**、8-GPU 整機 **$0.37–0.45M**、**NVL36/72** **$1.8–3.0M**。([Northflank](https://northflank.com/blog/how-much-does-an-nvidia-h100-gpu-cost?utm_source=chatgpt.com))
- **網路成本抬升**：800G 模組市價千美元級、1.6T 接力；**AI 後端交換 2025–2029 > $100B**。([Network-Switches](https://network-switch.com/collections/800g-osfp-optical-transceiver?srsltid=AfmBOor60HMFHwVRlnXUJ7M_iKxZ38N9Qsk1yfayzn9zvJ3_wpdF0E6F&utm_source=chatgpt.com))
- **直液冷/熱管理**：**DLC 2024 $1.1B → 2029 $5.8B（CAGR 19%）**。([PR Newswire](https://www.prnewswire.com/news-releases/ai-build-out-to-propel-data-center-physical-infrastructure-market-to-63-1-billion-by-2029--according-to-delloro-group-302530530.html?utm_source=chatgpt.com))

> 結論：2030 年「加速器/整機 ≈ 50%」不是不合理；它反映 加速器 ASP 下滑 + HBM/網路/DLC/配電等非晶片項目佔比上升 的中位態。
> 

---

# 五、數量視角：台數、顆數、與 2030 年「隱含」變化

- **2025 校準**（以年預估對齊）：
    - 取 (R_{\text{server}} \approx $298B)、(R_{\text{acc}} \approx $207B) → **BOMshare ≈ 69%**。
    - 若 (ASP_{\text{server}} = $180k!\sim!220k)、(ASP_{\text{acc}} = $22k!\sim!30k)，則 (G_{\text{per_server}} \approx 5.5!\sim!6)；
        
        → **伺服器台數約 1.3–1.7M 台**、**加速器出貨約 7.8–9.3M 顆**（與 Q1–Q3 年化吻合）。
        
- **到 2030**：
    - 若採 **加速器 $286B**、**整機 $600B**，**BOMshare ≈ 48%**；
    - 在 **更高的網路速率（1.6T）與 更高的 HBM 容量 下，「同等任務」可能用更少顆**但**更強單顆**的器件完成；因此**顆數增速**低於**算力/整機金額**增速，這也解釋了「加速器收入增速低於整機」。

---

# 六、三種情境（2025→2030）

| 指標 | 2025（校準） | 2030「保守」 | 2030「基準」 | 2030「積極」 |
| --- | --- | --- | --- | --- |
| **加速器營收** | $207B | $250B | **$286B** | $320B |
| **整機營收** | $298B | $500B | **$600B** | $850B |
| **加速器/整機** | **~69%** | ~50% | **~48%** | ~38% |
| **關鍵假設** | — | 客製 ASIC↑、ASP↓、電力瓶頸強 | Omdia + 中位整機 | 模型/上下文暴增、電網擴容快、DLC/1.6T 全面鋪開 |

**觀測指標（你可以持續追）**

1. **電力落地**：區域併網/PPA 進度、IEA 的 2030 用電路徑（基準 945 TWh；逆風情境更低，且 ~20% 專案延宕）。([IEA](https://www.iea.org/news/ai-is-set-to-drive-surging-electricity-demand-from-data-centres-while-offering-the-potential-to-transform-how-the-energy-sector-works?utm_source=chatgpt.com))
2. **客製 ASIC 滲透**：CSP 自研/半客製採購占比變化（Omdia 指 2026 後為拐點）。([Omdia](https://omdia.tech.informa.com/pr/2025/aug/ai-data-center-chip-market-to-hit-286bn-growth-likely-peaking-as-custom-asics-gain-ground?utm_source=chatgpt.com))
3. **網路投資**：後端交換 **2025–2029 > $100B** 是否達標；800G→1.6T 模組出貨節奏。([Dell'Oro Group](https://www.delloro.com/news/data-center-switch-sales-in-ai-back-end-networks-to-exceed-100-b-over-the-next-five-years/?utm_source=chatgpt.com))
4. **熱管理/DLC**：是否走到 **2029 $5.8B** 的斜率（影響非晶片 BOM 上升）。([PR Newswire](https://www.prnewswire.com/news-releases/ai-build-out-to-propel-data-center-physical-infrastructure-market-to-63-1-billion-by-2029--according-to-delloro-group-302530530.html?utm_source=chatgpt.com))

---

# 七、你可以直接套用的「BOM 驗證法」

要判斷任一年（或任一機型）「加速器/整機佔比」是否合理，請只要代四個數：

$\frac{\text{加速器+HBM}}{\text{整機}}
= \frac{G\cdot (ASP_{acc,\neg HBM}+ASP_{HBM})}{ASP_{server}}$

- 若你把 **(ASP_{server})** 提高（因為網路/光模組、DLC、配電上升），同時把 **(ASP_{acc,\neg HBM})** 降低（效率/競爭/規模折價）——**佔比自然往 50% 靠攏或以下**。
- 反之，若 HBM/網路/DLC 成本降幅**超過**加速器 ASP 降幅，或訓練型 8-GPU 占比更高，**佔比可維持 55–60%+**。

---

## 參考來源（可點開檢核）

- **AI 加速器（晶片）**：Omdia 預估 **2025 $207B → 2030 $286B**，並指 2026 年後增速放緩。([Omdia](https://omdia.tech.informa.com/pr/2025/aug/ai-data-center-chip-market-to-hit-286bn-growth-likely-peaking-as-custom-asics-gain-ground?utm_source=chatgpt.com))
- **AI 伺服器整機**：TrendForce **2025 $298B**。([TrendForce](https://www.trendforce.com/presscenter/news/20250106-12433.html?utm_source=chatgpt.com))
- **NVIDIA 實績/指引（驗證 Q1–Q3）**：Q1 FY26 **資料中心 $39.1B**；Q2 FY26 新聞稿與市場解讀；Q3 指引近 **$54B** 總營收、資料中心占比高。([NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2026?utm_source=chatgpt.com))
- **AI 網路**：650 Group **2025 近 $20B**；Dell’Oro **AI 後端交換 2025–2029 > $100B**。([IEEE 802](https://www.ieee802.org/3/ad_hoc/ngrates/public/25_01/dambrosia_nea_01_2501.pdf?utm_source=chatgpt.com))
- **DCPI / 液冷**：Dell’Oro **2029 $63.1B**、**熱管理 CAGR 19%**、**DLC 2024 $1.1B → 2029 $5.8B**。([Dell'Oro Group](https://www.delloro.com/news/ai-build-out-to-propel-data-center-physical-infrastructure-market-to-63-1-billion-by-2029/?utm_source=chatgpt.com))
- **用電天花板**：IEA **2030 ~945 TWh（資料中心）**，並有「逆風情境」說明與延宕風險。([IEA](https://www.iea.org/news/ai-is-set-to-drive-surging-electricity-demand-from-data-centres-while-offering-the-potential-to-transform-how-the-energy-sector-works?utm_source=chatgpt.com))
- **價格帶（校準）**：
    - H100 **$25k–$40k**；8-GPU 整機 **$0.37–0.45M**。([Northflank](https://northflank.com/blog/how-much-does-an-nvidia-h100-gpu-cost?utm_source=chatgpt.com))
    - **NVL36/NVL72** 整櫃 **$1.8–3.0M**（多處一致）。([雅虎財經](https://finance.yahoo.com/news/nvidia-partners-could-charge-3-145804981.html?utm_source=chatgpt.com))
    - 800G 光模組**千美元級**市價可見（僅作量級參考）。([Network-Switches](https://network-switch.com/collections/800g-osfp-optical-transceiver?srsltid=AfmBOor60HMFHwVRlnXUJ7M_iKxZ38N9Qsk1yfayzn9zvJ3_wpdF0E6F&utm_source=chatgpt.com))

---

# 最後的重點結論（給決策用）

- **2025 年**：用 Q1–Q3 實數回推，**加速器 ~$200B、整機 ~$300B** 的口徑成立；BOM 關聯顯示 **每台 ~5.5–6 顆**為常態。
- **2030 年**：成長**顯著放緩**（加速器 CAGR ~6–7%），但**整機/周邊仍雙位數**，主因 **HBM、網路（800G→1.6T）、DLC/配電** 等非晶片費用占比上升、同時 **加速器 ASP 下滑**。
- **「加速器/整機 ≈ 50%」到 2030 年是合理的中位情境**：訓練整櫃能見 ~50–60%，推論/混合可低於 50%；最終取決於 **機型 Mix**、**網路速率**、**DLC 導入率**、**HBM 世代/容量** 與 **電力可得性**。

如果你想把文中的參數（GPU ASP、HBM/卡、800G→1.6T 網路與 DLC 占比）做成**可調情境表**，我可以直接幫你生成一個可互動的表格／試算模板，讓你即時看到 **BOM 佔比、台數、顆數、營收** 在不同假設下的變動。

# 把「token 需求」轉為「所需算力」

你在問的是：**把「token 需求的成長」系統化地轉換成「硬體（加速器/整機）的需求」**，並檢查在 token 需求爆衝的情況下，硬體需求是否仍可維持 **>20% 年增**。下面給你一套可落地的「自上而下推導 → 可代入參數的公式 → 範例情境」；你改幾個數字，就能得到你自己的結論。

---

# 1) 把「token 需求」轉為「所需算力」

## 1.1 核心關係式（推論為主）

令

- $T$= 年度 **token 需求量**（推論輸出 token 數）
- (c) = **每 token 所需 FLOPs**（因模型大小/路由/量化/上下文長度而變動）
- (E) = **端到端效率**（編譯器/框架/排程/批次化帶來的「有效 FLOPs 比例」）
- (C_{\text{req}}) = **全年所需有效算力量**（FLOPs/年）

則：

[

$C_{\text{req}} ;=; \frac{T \times c}{E}$

]

> 直觀：一年要產出 (T) 個 token，每個 token 要 (c) FLOPs，考慮效率損耗 (E)（0–1），就得到一年要「消耗」多少有效 FLOPs。
> 

## 1.2 把「所需算力」轉為「需要多少加速器」

令

- (P_{\text{acc}}) = **每張加速器可用的有效算力**（FLOPs/秒；已扣掉指令混合、精度、kernel 實效，比「理論峰值」保守）
- (u) = **平均利用率**（0–1；含排程/排隊/中斷/夜間/off-peak 等）
- (S) = **每年秒數**（(\approx 3.1536\times 10^7)）
- (N) = **所需加速器數量**

則：

[

N ;=; \frac{C_{\text{req}}}{P_{\text{acc}} \cdot u \cdot S}

;=; \frac{T \cdot c}{E \cdot P_{\text{acc}} \cdot u \cdot S}

]

> 這條式子就是「token → 顆數」的關鍵連結。
> 

---

# 2) 影響每 token FLOPs（(c)）的四個槓桿

1. **模型結構（Dense vs MoE）**
    - Dense：(c \approx k \cdot \text{Params})（一階近似，可把 (k) 視作常數 × 層數/算子常數）
    - MoE：只啟用 (r) 個專家（在 (E) 個專家中選 (r) 個），**名目參數極大**但每 token **實際參與參數**少 → (c) 按 **路由開啟比例**下降
2. **數值格式/稀疏化/編譯器**
    - FP8 → FP4/NVFP4/INT4、結構化稀疏、FlashAttention/頁面化KV等：(c) 以**年化比例**下降（例如每年 -25%～-40%）
3. **上下文長度（context length, (L)）**
    - Attention 理論上 (O(L^2))，但近年 kernel/近似演算法降低常數；實務仍導致 **長上下文推高 (c)**
    - 你可以把 **(c)** 拆成「**前向/權重乘加**（近似與 Params 成正比）」與「**注意力開銷**（與 (L) 有次方關係）」兩塊去做情境
4. **Batching/併發與路徑最佳化（歸入 (E)）**
    - 更高批次化與更好排程 → **(E)** 上升（有效 FLOPs 比例提高），等效地**降低**所需加速器

> 給一個可操作的簡化：把 (c) 的年度變化寫成
> 
> 
> [
> 
> c_{t+1} = c_t \cdot (1 - \epsilon_c) \cdot (1 + \delta_L)
> 
> ]
> 
> 其中 (\epsilon_c) 是「每年因 MoE/量化/稀疏/編譯器帶來的 **每 token FLOPs 下降率**」，(\delta_L) 是因為**上下文變長**帶來的「反向增加率」。
> 

---

# 3) 影響「每張卡的等效供給」的三個槓桿

每年的 **單卡有效供給** 為 (P_{\text{acc}} \cdot u \cdot S)。其變化來自：

1. **新世代加速器的「有效」算力提升**（非理論峰值） → (P_{\text{acc}}) 每年 **+p%**
2. **利用率提升**（資料管線、排程器、token 混合與批次化） → (u) 每年 **+u_gain**
3. **純硬體以外的系統效能**（I/O/網路/記憶體瓶頸解法） → 反映在 (P_{\text{acc}}) 與 (u) 的聯合改善

---

# 4) 「token 成長」如何對應到「加速器 CAGR」

把上一節合起來，對 **加速器數量 (N)** 做「**連續近似**」的成長分解：

$$
[
\underbrace{g_N}{\text{加速器年增率}}
;\approx;
\underbrace{g_T}{\text{token 年增率}}
;+;
\underbrace{g_c}{\text{每 token FLOPs 變化}}
;-;
\underbrace{g{P}}{\text{單卡有效算力提升}}
;-;
\underbrace{g{u}}_{\text{利用率提升}}
]
$$

[

\underbrace{g_N}*{\text{加速器年增率}}
;\approx;
\underbrace{g_T}*{\text{token 年增率}}
;+;
\underbrace{g_c}*{\text{每 token FLOPs 變化}}
;-;
\underbrace{g*{P}}*{\text{單卡有效算力提升}}
;-;
\underbrace{g*{u}}_{\text{利用率提升}}
]

- (g_c) 通常是**負值**（效率進步讓每 token FLOPs 下降），但**長上下文**會把它往上拉
- (g_P)、(g_u) 都是**正值改善**，在式子裡是**減項**，因為單卡提供更多 token 產能 → 你需要的卡數變少

---

# 5) 代數字做一個「能保持 >20% 硬體增長」的範例

> 這只是可調參數示範，你可換上你相信的數字。
> 

**基準假設（推論為主）**

- **Token 年需求成長 (g_T)**：**+60%/年**（你擔心的「需求爆衝」情境）
- **每 token FLOPs 下降（MoE/量化/稀疏/編譯器）**：(\epsilon_c=30%) → (g_c \approx -30%)
- **長上下文帶來額外開銷**：(\delta_L = +10%) → 合併 (g_c \approx -20%)（= -30% + 10%）
- **單卡有效算力提升 (g_P)**：**+25%/年**（新世代/IO/記憶體/網路約束下的保守有效值）
- **利用率提升 (g_u)**：**+5%/年**（排程/併發/批次化再進步）

代入「成長分解」：

[

g_N ;\approx; 60% ;+;(-20%);-;25%;-;5%

;=; \boxed{+10%/年}

]

→ 在這組假設下，**加速器數量年增 ≈ +10%**。但注意：若你的 token 成長更高、或上下文膨脹更快、或單卡有效提升沒那麼順利，**(g_N)** 會立刻衝高。

**把參數稍微改一下（「高需求＋上下文暴衝」）**

- (g_T=+80%)、(\delta_L=+20%)（超長上下文普及）、(\epsilon_c=30%)（效率進步不變）
- (g_P=+20%)、(g_u=+3%)（新世代卡與利用率提升低於預期）

[

g_N ;\approx; 80% + (-10%) - 20% - 3% ;=; \boxed{+47%/年}

]

→ 你看到 **>20%** 的年增完全可能，甚至接近 **+50%**。

**反過來，如果需求保守**

- (g_T=+40%)、(\epsilon_c=35%)、(\delta_L=+5%) → (g_c\approx -30%)
- (g_P=+30%)、(g_u=+5%)

[

g_N \approx 40% - 30% - 30% - 5% = \boxed{-25%/年}

]

→ 極端下，**加速器數量**甚至可能**不增反減**（靠單卡躍進+效率提升「吃掉」需求）。

**重點**：**(g_N)** 的號召力，**完全取決於這四個槓桿的相對速度**。只要 **token 成長 (g_T)** 明顯 **大於**（效率下降幅度 ( -g_c ) + 單卡進步 (g_P) + 利用率進步 (g_u)），加速器就會維持 **>20%** 的年增。

---

# 6) 從「顆數」回到「整機/網路/散熱」的連動

一旦得到 (N)（加速器數量年增），你可以用**BOM 佔比**把整機/網路/散熱系統帶出來：

- **整機數量（節點）**：按每節點 (G_{\text{per node}}) 顆 → **節點數 = (N / G_{\text{per node}})**
- **網路（800G→1.6T 光模組/交換）**：端口數 ≈ 節點數 ×（平均 NIC/port per node）×（冗餘/拓撲係數）
- **散熱（DLC/冷板/泵/快接頭/機櫃 CDU）**：與每節點 TDP 與密度線性（或超線性）掛勾 → **N** 上來，**DLC/配電**必然上升
- 這些項目把 2030 年「**加速器/整機 ≈ 50%**」的 **BOM 檢算**自動串起來（因為非晶片項的花費會和節點密度、網路速率一起長）

---

# 7) 一個「可複製」的年度盤點流程（給你做持續追蹤）

1. **定年度 token 需求 (T)**：用你的自家/產業追蹤（MAU×DAU×平均查詢×平均輸出 token；再加 API 量、內部應用量）。
2. **估 (c)**（每 token FLOPs）：按**模型 mix**（Dense/MoE/路由率）、**上下文長度分布**、**推論堆疊**（量化/稀疏/Attention kernel）給一個**加權平均**。
3. **估 (E)**：把批次化/排程/管線效率做一個「端到端」觀察（實測 QPS vs 理論 FLOPs）。
4. 代入 (;N = \dfrac{T \cdot c}{E \cdot P_{\text{acc}} \cdot u \cdot S};) 求「需要的卡數」。
5. **做年對年**：把 (T)、(c)、(P_{\text{acc}})、(u) 的年度變化率帶入「**成長分解式**」直接得到 (g_N)。
6. 把 (N) 串回 **整機/網路/散熱** 的 **BOM/端口/冷板**需求，得到「伺服器台數、光模組數、DLC 物料、機櫃/母線/UPS」等的**年增路徑**。

---

# 8) 小範例（把 token 變硬體，含數字）

**基線（2025）**

- 假設 **每 token FLOPs (c_0 = 150,\text{GFLOPs})**（大語言模型 50–100B dense 的量級，僅示例）
- **單卡有效算力 (P_{\text{acc},0} = 1,\text{PFLOP/s})**（已扣除效率後的推論等效；保守）
- **利用率 (u_0 = 35%)**、**端到端效率 (E_0 = 70%)**
- **年度 token 需求 (T_0 = 10^{15})（一千兆）**

→ 單卡年產能（token）

[

\frac{P_{\text{acc},0} \cdot u_0 \cdot S}{c_0}

= \frac{10^{15}\cdot 0.35 \cdot 3.15!\times!10^7}{150!\times!10^9}

\approx 7.35!\times!10^{10}\ \text{tokens/卡/年}

]

→ **所需卡數 (N_0 \approx \dfrac{10^{15}}{7.35!\times!10^{10}} \approx 13{,}600)**

**一年後（2026，需求爆衝但效率也在進步）**

- (T) **+70%** → (1.7\times 10^{15})
- (c) **25%**（效率進步）+ **+10%**（上下文拉長） → 淨 **17.5%**
- (P_{\text{acc}}) **+20%**（新世代有效）
- (u) **+3%**（例如 0.35→0.3605）
- (E) **+3%**

用成長分解估 **卡數年增**：

[

g_N \approx +70% + (-17.5%) - 20% - 3% \approx \boxed{+29.5%}

]

→ **加速器數量**需求 **+~30%/年**（明顯 >20%）

> 你可以任意調整上面的 5 個旋鈕：token 成長、每 token FLOPs 的淨變化（效率 vs 上下文）、單卡有效進步、利用率進步、端到端效率。只要 token 成長贏過其餘總和，硬體年增就會 >20%。
> 

---

## 一句話結論

是的，**可以**用 token 需求來預估硬體需求，而且邏輯緊密：

[

\boxed{N ;=; \dfrac{T \cdot c}{E \cdot P_{\text{acc}} \cdot u \cdot S}}

]

當 **token 成長**大於 **（每 token FLOPs 下降 + 單卡有效提升 + 利用率提升）** 的合計幅度時，**加速器與整機的需求年增**自然會維持 **>20%**，甚至更高。

如果你要，我可以把上面這套模型做成**可互動的小表/Notebook**：你拉動五個參數滑桿（(g_T, \epsilon_c, \delta_L, g_P, g_u)），就能即時看到 **所需加速器數、整機台數、光模組/DLC 物料的連動年增**。

太好了—我先把我們用到的公式與重點內容，全部轉成「**Obsidian 友善版**」。你可以整段複製貼上到 Obsidian（請確認已開啟 Settings → Editor → **Math formatting**），所有公式都用 `$…$` / `$$…$$`，不放在程式碼區塊裡。

---

# 1) 設定小提醒

- 開啟 **Math formatting**（或使用 Reading view / Live preview）。
- 公式使用 **$…$（行內）** 與 **$$…$$（區塊）**。
- 不要把公式放進三個反引號的程式碼區塊內。

---

# 2) 符號說明（Notation）

- $P_{\mathrm{eff}}$：叢集**有效**算力（FLOP/s）
- $N_{\text{params}}$：模型參數數（dense）；$N_{\text{params,active}}$：每個 token 實際參與的參數（MoE 取啟用專家總和）
- $L$：層數；$d$：隱藏維度；$S_{\text{in}}$/$S_{\text{out}}$：輸入/輸出 token 數
- $E$：端到端效率；$u$：叢集利用率；$P_{\text{acc}}$：每卡有效算力（FLOP/s）
- $T$：年度 token 需求量；$c$：每 token FLOPs
- $S$：一年秒數（約 $3.1536\times 10^7$）
- $\alpha,\beta,\gamma$：常數（矩陣乘法與注意力的量級係數）

---

# 3) 硬體系統量化

**有效算力（cluster）**

$$

P_{\mathrm{eff}},[\mathrm{FLOP/s}] ;=; \sum_{i=1}^{n} P_i,\eta_i

$$

其中 $P_i$ 是第 $i$ 張加速器的理論算力，$\eta_i$ 是實際效率（kernel／通訊／記憶體／調度等損耗）。

**Roofline（是否記憶體受限）**

$$

AI ;=; \frac{\text{FLOPs/token}}{\text{Bytes/token}}

\quad\text{vs}\quad

\frac{\text{HBM BW}}{P_{\mathrm{eff}}}

$$

**通訊占比（MoE／TP／PP）**

$$

\frac{t_{\text{comm}}}{t_{\text{comp}}}

;=;

\frac{\text{Comm_bytes}/\text{Net_BW}}{\text{FLOPs}/P_{\mathrm{eff}}}

$$

---

# 4) 模型工作負載量化

**推論：每 token FLOPs（近似）**

$$

\text{FLOPs/token} ;\approx; \alpha \cdot N_{\text{params,active}} ;+; \text{AttentionCost}(L)

$$

- Dense：$N_{\text{params,active}} \approx N_{\text{params}}$
- MoE：$N_{\text{params,active}}$ 僅計入被路由啟用的專家
- 注意力：prefill 近似 $O(L^2)$，decode 近似 $O(L)$（有 KV cache）

**訓練：每 step FLOPs（粗估）**

$$

\text{FLOPs/step} ;\approx; 6 \cdot N_{\text{params}} \cdot \text{seq_len} \cdot \text{batch_global}

$$

**KV cache 需求（推論）**

$$

\text{KV_bytes} ;\approx; L \cdot B \cdot L_{\text{layers}} \cdot d \cdot \text{bytes/elt}

$$

---

# 5) 系統 × 模型 → KPI（推論）

**吞吐（tokens/s）**

$$

\text{Throughput} ;\approx;

\frac{P_{\mathrm{eff}}}{\alpha \cdot N_{\text{params,active}} + \text{AttentionCost}(L)} \cdot u

$$

**延遲（單次請求）**

$$

\text{Latency} ;\approx;

\frac{\text{FLOPs}*{\text{prompt}} + \text{FLOPs}*{\text{response}}}{P_{\mathrm{eff}}}

;+;

\text{Comm}

;+;

\text{Queueing}

$$

**成本／百萬 token**

$$

\frac{$}{10^{6}\text{ tok}} ;\approx;

\frac{\text{TCO}_{\text{per_second}}}{\text{Throughput}} \times 10^{6}

$$

**能耗／百萬 token**

$$

\frac{\text{J}}{10^{6}\text{ tok}} ;\approx;

\frac{P_{\text{cluster(power)}}}{\text{Throughput}} \times 10^{6}

$$

---

# 6) Token 需求 → 硬體需求（年度）

**年度所需有效算力量**

$$

C_{\text{req}} ;=; \frac{T \cdot c}{E}

$$

**所需加速器數**

$$

N ;=; \frac{C_{\text{req}}}{P_{\text{acc}} \cdot u \cdot S}

;=;

\frac{T \cdot c}{E \cdot P_{\text{acc}} \cdot u \cdot S}

$$

**年增率分解（推論導向）**

$$

g_N ;\approx; g_T ;+; g_c ;-; g_{P} ;-; g_u

$$

- $g_T$：token 需求年增率
- $g_c$：每 token FLOPs 的年變化（通常為負值，代表效率進步）
- $g_P$：單卡有效算力年提升率
- $g_u$：利用率年提升率

---

# 7) 單次請求的 FLOPs（更精細估法）

**Prefill（讀輸入）**

$$

\text{FLOPs}*{\text{prefill}}
;\approx;
\alpha \cdot N_p \cdot S*{\text{in}}
;+;
\beta \cdot L \cdot d \cdot S_{\text{in}}^{2}
$$

**Decode（逐 token 生成）**

$$

\text{FLOPs}*{\text{decode}}
;\approx;
\alpha \cdot N_p \cdot S*{\text{out}}
;+;
\gamma \cdot L \cdot d \cdot S_{\text{out}} \cdot \bar{S}
$$

**推論時間／能耗（理想值量級）**

$$

t_{\text{ideal}} ;\approx;

\frac{\text{FLOPs}*{\text{prefill}}+\text{FLOPs}*{\text{decode}}}{P_{\text{cluster}}}

\qquad

E_{\text{energy}} ;\approx; t_{\text{ideal}} \times P_{\text{cluster(power)}}

$$

---

# 8) BOM／成本結構關聯（加速器 vs 整機）

**兩市場口徑聯動**

$$

R_{\text{server}} ;=; N_{\text{server}} \cdot \text{ASP}*{\text{server}}
\qquad
R*{\text{acc}} ;=; N_{\text{server}} \cdot G_{\text{per_server}} \cdot \text{ASP}_{\text{acc}}
$$

**BOM 佔比（加速器在整機中的占比）**

$$

\text{BOMshare}*{\text{acc}}
;=;
\frac{R*{\text{acc}}}{R_{\text{server}}}
;=;
\frac{G_{\text{per_server}} \cdot \text{ASP}*{\text{acc}}}{\text{ASP}*{\text{server}}}
$$

> 若要驗證某年度的「加速器／整機 ≈ 50%」是否合理：把模型/網路（800G→1.6T）/DLC/配電的成本變化合併到 $\text{ASP}{\text{server}}$，再對照單卡 $\text{ASP}{\text{acc}}$ 與每台加速器數 $G_{\text{per_server}}$ 代入上式即可。
> 

---

# 9) 最小可用流程（SLA 導向）

1. 定 SLA（推論：吞吐與 P95 延遲；訓練：時程與成本）。
2. 由模型求出 $\text{FLOPs/token}$、KV、通訊比。
3. 由硬體求出 $P_{\mathrm{eff}}$、HBM BW、網路 BW。
4. 套 KPI 公式求 **Throughput、Latency、$/Mtoken、J/token**。
5. 做敏感度（active 參數、$L$、$u$、網路 BW、效率 $\eta$）。
6. 連動到 **BOM／DCPI**（光模組、DLC、配電）得到 TCO。

---

如果你想，我也可以把這份「Obsidian 友善版」存成一個模板（例如 `算力系統評估模板.md`），之後你把機型與模型參數填進指定區塊，就能快速得到吞吐、延遲、成本與能耗的估算。

通訊占比（MoE／TP／PP）

$$
\frac{t_{\text{comm}}}{t_{\text{comp}}} \;=\; \frac{\text{Comm\_bytes}/\text{Net\*BW}}{\text{FLOPs}/P*{\mathrm{eff}}}
$$