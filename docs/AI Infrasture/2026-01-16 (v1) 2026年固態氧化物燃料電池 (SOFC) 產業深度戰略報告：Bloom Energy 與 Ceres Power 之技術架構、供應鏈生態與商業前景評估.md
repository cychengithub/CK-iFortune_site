By Gemini 3.0 Pro with my questions
## 1. 執行摘要與戰略前言

### 1.1 報告背景與範疇

本報告係針對全球固態氧化物燃料電池 (Solid Oxide Fuel Cell, SOFC) 領域的兩大技術巨擘——Bloom Energy (NYSE: BE) 與 Ceres Power Holdings plc (LSE: CWR) 進行的深度盡職調查 (Due Diligence)。隨著 2024 年至 2025 年間人工智慧 (AI) 數據中心對電力需求的指數級增長，以及全球電網互連 (Interconnection) 的瓶頸日益嚴峻，具備「不依賴電網」(Off-grid) 與「高可靠性」(Always-on) 特質的 SOFC 技術已從邊緣輔助電源躍升為核心能源戰略資產。本報告將透過電化學原理、材料科學、製造工藝、供應鏈地緣政治及生命週期成本 (LCOE) 等多維度，對兩家公司進行詳盡的對比分析。

### 1.2 核心發現概覽

分析顯示，Bloom Energy 與 Ceres Power 代表了 SOFC 技術光譜的兩個極端，分別佔據了不同的戰略生態位：

- **Bloom Energy (電解質支撐技術 ESC)：** <font color="#245bdb">採取「垂直整合」與「極致效率」路線。其技術依賴高成本但高離子導電率的掃描穩定氧化鋯 (ScSZ) 電解質，運行於 800°C 高溫，實現了超過 60% 的電效率。</font>透過與 American Electric Power (AEP) 簽署的 26.5 億美元合約及與 Intel、CoreWeave 的數據中心合作，Bloom 已確立其作為「基載電力替代品」的市場地位。然而，<font color="#ff0000">其依賴單一供應源 (Single Source) 的風險及極長的冷啟動時間 (6-12小時) 限制了其在靈活性市場的應用。</font>
    
- **Ceres Power (金屬支撐技術 MSC)：** 採取「技術授權」與「強健性」路線。其專利的 SteelCell® 技術利用標準不鏽鋼與低溫 CGO 電解質 (500-600°C)，實現了快速啟動 (數十分鐘) 與優異的熱循環耐受性。<font color="#ff0000">雖然 2025 年 Bosch 宣布退出 SOFC 開發對其歐洲佈局造成打擊</font>，<font color="#245bdb">但韓國 Doosan Fuel Cell 的 50MW 工廠量產及與濰柴動力 (Weichai) 在中國的深度佈局，顯示其重心已向亞洲轉移</font>。
    

---

## 2. 宏觀能源環境：SOFC 的戰略機遇窗口

### 2.1 AI 運算與電網脫鉤的迫切性

2025 年標誌著能源市場的結構性轉變。傳統電網的擴容週期 (3-5 年) 已無法跟上 AI 數據中心 GPU 叢集的部署速度 (12-18 個月)。Bloom Energy 的「Time-to-Power」優勢——<font color="#245bdb">宣稱可在 50 天內完成部署</font>——成為其在 2025 年贏得 Oracle 與 AEP 巨額訂單的關鍵驅動力 1。SOFC 系統因具備天然氣重組能力，可利用現有的天然氣管網直接發電，繞過電力傳輸瓶頸，成為「氣電融合」的關鍵節點。

### 2.2 氫能經濟的橋接角色

SOFC 的高溫特性使其在氫能轉型中扮演雙重角色：

1. **燃料靈活性**：<font color="#245bdb">可從 100% 天然氣平滑過渡到混氫及 100% 氫氣，無需更換核心堆疊。</font>
    
2. **可逆操作 (Reversibility)**：Bloom 與 Ceres 均在開發固態氧化物電解槽 (SOEC) 模式。<font color="#245bdb">利用高溫廢熱進行水蒸氣電解</font>，其效率顯著高於低溫 PEM 或鹼性電解槽。
    

---

## 3. Bloom Energy：高溫電解質支撐技術 (ESC) 之深度解析

### 3.1 技術架構與材料科學

Bloom Energy Server 的核心技術路徑選擇了**電解質支撐電池 (<font color="#245bdb">Electrolyte-Supported Cell, ESC</font>)**，這是一種以陶瓷電解質為機械支撐結構的設計。此選擇決定了其後的材料體系與運作特性。

#### 3.1.1 核心材料：掃描穩定氧化鋯 (ScSZ) 的戰略豪賭

不同於業界普遍使用的釔安定氧化鋯 (YSZ)，Bloom Energy 選擇了成本更高但性能更優的 <font color="#245bdb">**ScSZ (Scandia Stabilized Zirconia)** </font>3。

- **電導率優勢**：在 800-850°C 的運作溫度下，ScSZ 的氧離子電導率約為 YSZ 的兩倍。由於 ESC 設計的電解質層較厚 (通常 >100 微米) 以提供機械強度，若使用 YSZ 會導致過高的歐姆極化 (Ohmic Polarization) 損失。<font color="#245bdb">ScSZ 的高導電率有效抵消了厚電解質帶來的內阻，使系統能維持高電壓效率。</font>
    
- **專利壁壘**：Bloom 擁有多項關於 ScSZ 摻雜配方 (如摻雜 Ceria 以穩定相變) 的專利 3，構成了其材料科學的護城河。
    
- **供應鏈隱憂**：<font color="#ff0000">Scandium (鈧) 是一種稀土元素，主要副產於鈦白粉或鈾礦開採，全球產量稀少且供應鏈高度集中於中國與俄羅斯。這使得 Bloom 在原材料採購上面臨潛在的地緣政治風險。</font>
    

#### 3.1.2 電極工程與專利墨水

Bloom 的陽極與陰極採用獨特的「墨水 (Ink)」配方，透過網版印刷塗佈於 ScSZ 電解質兩側 4。

- **陽極 (Anode)**：採用氧化鎳 (NiO) 與 ScSZ 的金屬陶瓷 (Cermet) 墨水。在還原氣氛下，NiO 還原為金屬鎳，形成多孔結構。Bloom 的專利墨水配方特別針對抗積碳 (Coking) 進行了優化，這對於直接使用天然氣燃料至關重要。
    
- **陰極 (Cathode)**：採用鑭鍶亞錳 (LSM) 或鑭鍶鈷鐵 (LSCF) 體系。由於高溫運作下，連接板中的鉻 (Cr) 易揮發並毒化陰極，Bloom 的陰極墨水包含了抗鉻毒化的特殊添加劑。
    

### 3.2 系統熱力學與內部重組機制

Bloom 系統的高效率 (>60% LHV) 源於其精妙的熱管理策略，特別是**吸熱重組 (Endothermic Reforming)** 的利用。

#### 3.2.1 內部重組 (Internal Reforming) 的虛與實

雖然市場宣傳稱 Bloom 依賴內部重組，但技術細節顯示其採用的是**「預重組 + 內部重組」**的混合模式。

- **混合機制**：<font color="#245bdb">天然氣首先經過一個位於熱箱 (Hot Box) 內的**燃料處理器 (Fuel Processor)**。Bloom 曾收購或深度合作的 **Catacel** (現屬 Johnson Matthey) 提供了關鍵的**金屬箔片結構化催化劑 (Structure Catalyst)** 6。這種催化劑具有極高的熱傳導率，能利用堆疊排出的廢熱將部分甲烷轉化為氫氣與一氧化碳。</font>
    
- **熱平衡**：<font color="#245bdb">剩餘的甲烷進入陽極腔室，在陽極表面進行直接內部重組。由於重組反應是強吸熱反應，它有效吸收了電池發電產生的焦耳熱，使電池內部溫度場更均勻，減少了對外部冷卻空氣的需求，從而大幅降低了寄生功耗 (Parasitic Loss)。</font>
    

#### 3.2.2 冷啟動與熱循環限制

ESC 結構的厚陶瓷板具有較大的熱容量，且陶瓷材料對熱應力 (Thermal Stress) 極為敏感。

- **啟動時間**：資料顯示，Bloom 系統從冷機狀態升溫至工作溫度 (800°C) 需要 **6 至 12 小時**，甚至更久 8。
    
- **排放峰值**：在啟動初期，由於催化劑尚未達到工作溫度，會產生短暫的揮發性有機物 (VOC) 與一氧化碳排放峰值，這在環境評估報告中被特別標註 9。
    
- **運作模式**：因此，<font color="#245bdb">Bloom Energy Server 被設計為 **Base Load (基載)** 電源，不建議頻繁啟停。這限制了其在需要快速調峰的應用場景中的競爭力</font>。
    

### 3.3 供應鏈生態與製造戰略

Bloom 堅持垂直整合 (Vertical Integration) 策略，<font color="#245bdb">自行組裝核心的 "Hot Box</font>"，但關鍵零組件高度依賴特定的戰略供應商。

#### 3.3.1 關鍵組件供應商矩陣

| **組件名稱**                | **關鍵供應商**                                     | **供應商角色與技術細節**                                                                      | **風險評估**                                                                                            |
| ----------------------- | --------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **互連板 (Interconnects)** | **Universal Metal Corporation (UMC)** 10      | 提供連接單電池的高精密金屬板。需使用特殊的鐵素體不鏽鋼 (如 Crofer 22 APU)，並鍍有導電尖晶石塗層以防止鉻揮發。                     | **單一來源風險**：<font color="#245bdb">Bloom 的 SEC 文件多次提及依賴單一來源供應商 11，UMC 的產能與品質直接決定了 Bloom 的出貨上限。</font> |
| **燃料處理催化劑**             | **Johnson Matthey (Catacel)** 6               | 提供 Stackable Structural Reactor (SSR) 技術，這是一種金屬箔片折疊成的蜂窩狀催化劑載體，比傳統陶瓷球床具有更好的熱傳導與抗震性。  | <font color="#245bdb">技術高度專用，替換難度高。</font>                                                          |
| **熱箱組裝與輔助系統**           | **SK Ecoplant** 12                            | Bloom 的韓國合作夥伴，不僅是投資方，更合資在韓國仁川建立了組裝廠，負責亞太地區的 Hot Box 組裝與 Power Module 整合。            | 戰略綁定深，有助於分散美國本土製造壓力。                                                                                |
| **電力電子與散熱**             | **Unimicron (欣興電子)**, **高力 (Kaori)** 等台灣廠商 14 | 提供逆變器中的功率模組基板、散熱解決方案及特定的陶瓷元件。<font color="#245bdb">台灣供應鏈約佔其物料清單 (BOM) 的 30%。</font> | 供應鏈成熟度高，風險相對可控。                                                                                     |
|                         |                                               |                                                                                     |                                                                                                     |

#### 3.3.2 2025 年重大商業進展

- **AEP 900MW 協議**：2025 年底，Bloom 與 AEP 簽署了歷史性協議，包含 100MW 的確認訂單與 900MW 的選擇權，總價值達 26.5 億美元 1。這意味著 Bloom 的技術已通過公用事業級的嚴格驗證。
    
- **Oracle 與 CoreWeave 合作**：針對 AI 數據中心，Bloom 展示了在 50-90 天內完成部署的能力，解決了科技巨頭的燃眉之急。
    

---

## 4. Ceres Power：中低溫金屬支撐技術 (MSC) 之深度解析

### 4.1 技術架構：SteelCell® 的顛覆性設計

Ceres Power 選擇了一條截然不同的技術路徑——**金屬支撐電池 (Metal-Supported Cell, MSC)**，<font color="#245bdb">旨在解決傳統 SOFC 成本高、啟動慢、易碎裂的痛點。</font>

#### 4.1.1 核心材料：CGO 電解質與不鏽鋼基板

<font color="#245bdb">Ceres 的技術核心在於將功能性陶瓷層「印刷」在廉價的不鏽鋼基板上。</font>

- **CGO (Gadolinium-Doped Ceria) 電解質**：
    
    - **低溫導電性**：Ceres 採用摻釔的氧化鈰 (CGO) 作為電解質 16。與 YSZ 需要 800°C 才能導電不同，CGO 在 **500-600°C** 區間即具有極高的氧離子電導率。
        
    - **技術權衡**：CGO 在還原氣氛（陽極側）下會產生部分電子導電性 (Electronic Leakage)，這會導致開路電壓 (OCV) 略低於 YSZ 系統，從而在一定程度上限制了其電效率上限 (約 50-60%)，但換來了低溫操作的巨大優勢。
        
    - **稀土供應鏈**：<font color="#ff0000">CGO 的關鍵原料包括氧化鈰 (Cerium Oxide) 與氧化釔 (Gadolinium Oxide)，這兩者均為稀土元素。報告指出，稀土供應鏈（採礦、分離）高度集中於中國 17，這對 Ceres 的全球授權夥伴構成潛在的供應鏈安全挑戰。</font>
        
- **鐵素體不鏽鋼基板**：
    
    - **機械強度**：SteelCell® 建立在打孔的鐵素體不鏽鋼上，這賦予了電池極高的機械強韌性，使其能耐受振動與衝擊，適合車用與船用市場。
        
    - **成本優勢**：使用標準工業鋼材大幅降低了材料成本。
        

#### 4.1.2 密封工藝：雷射焊接 (Laser Welding)

低溫操作與金屬基板的結合，使得 Ceres 能夠採用**雷射焊接**進行電池堆的密封 19。

- **技術對比**：Bloom 必須使用易脆的玻璃陶瓷密封劑來應對陶瓷間的連接；Ceres 則利用雷射將金屬基板與金屬互連板直接焊接。這種金屬-金屬密封氣密性極佳，且能承受數千次的熱循環 (Thermal Cycling)，是實現快速啟停的關鍵工藝。
    

### 4.2 系統熱力學：外部重組與快速響應

#### 4.2.1 外部重組 (External Reforming) 的必要性

<font color="#245bdb">由於 SteelCell® 運作於 500-600°C，此溫度低於甲烷水蒸氣重組的高效區間 (>700°C)。因此，Ceres 的系統架構通常需要依賴**外部重組器 (External Reformer)** </font>19。

- **系統複雜度**：這增加了一個額外的高溫組件，需要獨立的燃燒器來提供重組所需的熱量，增加了 BoP (Balance of Plant) 的複雜度與體積。
    
- **控制策略**：然而，這種解耦設計使得堆疊的溫度控制更加獨立與精確，有利於負載跟隨 (Load Following)。
    

#### 4.2.2 快速啟動特性

得益於金屬基板的低熱容量 (Thermal Mass) 與強韌性，Ceres 系統具備極為優異的啟動性能。

- **啟動時間**：資料顯示，Ceres 系統可從冷機狀態在 **30 分鐘內** (部分文獻指 10-20 分鐘) 達到工作狀態 22。
    
- **戰略意義**：這使得 Ceres 技術不僅能做基載，還能作為**可調度電力 (Dispatchable Power)**，與間歇性的再生能源 (風光) 互補，或應用於頻繁啟停的增程電動車 (Range Extender) 與船舶輔助動力。
    

### 4.3 商業模式與合作夥伴生態系：授權模式的雙面刃

Ceres Power 採取「輕資產、純授權」模式，其商業成功完全取決於合作夥伴的量產進度。

#### 4.3.1 核心夥伴進展

1. **Doosan Fuel Cell (韓國) - 量產先鋒**：
    
    - **里程碑**：2025 年 7 月，Doosan 位於韓國群山的 50MW 工廠正式投產，開始量產基於 Ceres 技術的 SOFC 系統 24。這是 Ceres 技術邁向大規模商業化的最重要驗證。
        
    - **市場**：瞄準韓國 CHPS (清潔氫能組合標準) 市場及船用電源。
        
2. **Weichai Power (濰柴動力, 中國) - 深度佈局**：
    
    - **合作**：雙方成立合資公司，並於 2025 年簽署了新的製造授權協議，專注於中國市場的固定式電力與商用車增程器 26。
        
    - **供應鏈**：濰柴在中國建立了從粉末到系統的垂直供應鏈，利用中國在稀土與鋼鐵製造上的成本優勢，目標將系統成本降至極低水平。
        

#### 4.3.2 Bosch (博世) 的戰略退出 - 重大風險警示

<font color="#ff0000">2025 年初，Ceres 的長期戰略夥伴 Bosch 宣布**終止其 SOFC 系統開發計畫**，轉而全心投入 PEM 電解槽業務</font> 27。

- **影響分析**：Bosch 原計畫在德國 Bamberg 建立 200MW 產能，是 Ceres 歐洲戰略的核心。Bosch 的退出意味著 Ceres 在歐洲失去了製造引擎，其未來的權利金收入將高度集中於亞洲夥伴 (Doosan, Weichai)，地緣政治風險顯著上升。
    

---

## 5. Bloom Energy 與 Ceres Power 技術與經濟性深度比較

### 5.1 技術參數對比矩陣

下表總結了兩者在關鍵技術維度上的差異：

|**比較維度**|**Bloom Energy (ES-5710 等型號)**|**Ceres Power (SteelCell® 授權系統)**|**技術洞察與戰略意涵**|
|---|---|---|---|
|**電池架構**|**電解質支撐 (ESC)**|**金屬支撐 (MSC)**|**Bloom**: 陶瓷骨架，追求極致效率與壽命，但易碎。<br><br>  <br><br>**Ceres**: 不鏽鋼骨架，追求強韌性與低成本製造。|
|**運作溫度**|**800 - 850°C**|**500 - 620°C**|**Bloom**: 高溫有利於內部重組與高品位廢熱利用 (工業蒸汽)。<br><br>  <br><br>**Ceres**: 低溫允許使用廉價鋼材與密封件，降低材料成本。|
|**電解質材料**|**ScSZ** (掃描穩定氧化鋯)|**CGO** (摻釔氧化鈰)|**Bloom**: 高成本 ScSZ 換取高效率。<br><br>  <br><br>**Ceres**: 低溫 CGO 換取快速啟動，但犧牲部分電壓效率。|
|**發電效率 (LHV)**|**> 60%** (初期 ~52%)|**50% - 60%**|**Bloom**: 對燃料成本敏感的數據中心首選。<br><br>  <br><br>**Ceres**: 透過 CHP (熱電聯產) 綜合效率可達 85% 以上。|
|**啟動時間**|**6 - 12 小時 (冷啟動)**|**10 - 30 分鐘 (冷啟動)**|**Bloom**: 必須 24/7 連續運作 (Baseload)。<br><br>  <br><br>**Ceres**: 可作為備援電力或調峰電力。|
|**功率密度**|中等 (受限於厚電解質)|高 (受限於堆疊散熱)|Ceres 的金屬堆疊體積更緊湊，適合空間受限場景 (如船舶)。|
|**衰退率**|未公開，推測需每 5-7 年更換堆疊|**< 0.2% / 1000小時** 29|Ceres 的低溫與金屬密封理論上具有更好的抗熱循環衰退能力。|

### 5.2 經濟性分析：LCOE 與 CAPEX

基於 Lazard 2025 LCOE 報告 30 及產業數據進行分析：

#### 5.2.1 資本支出 (CAPEX)

- **Bloom Energy**: 2024/2025 年數據顯示，<font color="#245bdb"><font color="#245bdb">其系統平均售價 (ASP) 約為 **$3,363/kW**，產品製造成本約 **$2,360/kW** 8</font>。</font><font color="#ff0000">雖然 Bloom 致力於成本下降，但 ScSZ 材料與複雜的熱箱組裝使其降本曲線相對平緩。</font>
    
- **Ceres Power**:<font color="#245bdb"> 其合作夥伴 (如 Doosan) 的量產目標是將系統成本降至 **$1,200 - $1,500/kW**</font> 32。金屬基板與標準化生產工藝賦予了 Ceres 體系更強的長期降本潛力。
    

#### 5.2.2 均一化能源成本 (LCOE)

- <font color="#245bdb">儘管 Bloom 的 CAPEX 較高，</font><font color="#245bdb">但憑藉 **60% 以上的高電效率**與 **98% 的高容量因數 (Capacity Factor)**，其 LCOE 在天然氣價格穩定的地區極具競爭力。對於數據中心客戶而言，Bloom 的電力成本 (約 $0.10-$0.12/kWh) 往往低於電網高峰電價，且提供了無法量化的「供電確定性」價值。</font>
    
- <font color="#245bdb">Ceres 的 LCOE 優勢在於熱電聯產 (CHP) 模式。若能有效利用廢熱，其綜合能源成本可低於純電網供電。</font>
    

### 5.3 供應鏈風險綜合評估

|**風險類別**|**Bloom Energy**|**Ceres Power**|
|---|---|---|
|**原材料風險**|**極高 (Scandium)**：高度依賴俄羅斯/中國供應鏈。|**中高 (Rare Earths)**：CGO 依賴稀土，且需特殊鋼材供應。|
|**製造風險**|**產能瓶頸**：自身擴產速度決定營收上限。Fremont 工廠需應對 GW 級訂單。|**夥伴依賴**：Bosch 退出顯示了授權模式的脆弱性。Doosan 若執行不力將導致營收斷層。|
|**地緣政治**|**相對安全**：製造重心在美國與韓國 (SK)，符合美國供應鏈回流政策。|**風險較高**：製造重心向中國 (Weichai) 轉移，可能面臨未來的貿易壁壘或技術出口限制。|

---

## 6. 結論與戰略建議

### 6.1 總結

Bloom Energy 與 Ceres Power 雖同屬 SOFC 領域，但已演化為兩種截然不同的物種。**Bloom Energy 是「能源界的 Intel」**，追求高性能、垂直整合與高利潤的企業級市場；**Ceres Power 是「能源界的 ARM」**，提供底層架構授權，依靠生態系的繁榮來獲取收益。

### 6.2 對投資者與採購方的建議

- **對於 AI 數據中心運營商**：**Bloom Energy** 是目前唯一經過大規模驗證、能提供 MW 級基載電力的成熟方案。其高昂的 CAPEX 可被「快速上線」帶來的巨大 AI 業務營收所抵消。AEP 的 900MW 協議進一步驗證了其在電網級應用的可靠性。
    
- **對於尋求靈活能源解決方案的工業用戶**：**Ceres Power** 的技術（透過 Doosan 或 Weichai 產品）更適合需要熱電聯產、空間有限或需頻繁啟停的場景。其較低的預期成本使其在中小型商業應用中更具吸引力。
    
- **風險監控**：
    
    - 關注 Bloom Energy 的 **ScSZ 供應鏈穩定性**及其在特拉華州與加州的擴產進度。
        
    - 關注 Ceres Power 在 **Bosch 退出後的歐洲戰略空白**如何填補，以及 Doosan 韓國工廠的實際產能爬坡數據。
        

---

#### 引用的著作

1. After announcing a $2.65 billion agreement with American Electric Power, Bloom Energy shares surged 18.5% - VT Markets, 檢索日期：1月 16, 2026， [https://www.vtmarkets.com/live-updates/after-announcing-a-2-65-billion-agreement-with-american-electric-power-bloom-energy-shares-surged-18-5/](https://www.vtmarkets.com/live-updates/after-announcing-a-2-65-billion-agreement-with-american-electric-power-bloom-energy-shares-surged-18-5/)
    
2. Bloom Energy Surges 13% as AEP Commits $2.65 Billion for AI Data Center Fuel Cells, 檢索日期：1月 16, 2026， [https://fintool.com/news/bloom-energy-aep-2-65-billion-fuel-cell-deal](https://fintool.com/news/bloom-energy-aep-2-65-billion-fuel-cell-deal)
    
3. US8999601B2 - Electrolyte supported cell designed for longer life and higher power - Google Patents, 檢索日期：1月 16, 2026， [https://patents.google.com/patent/US8999601B2/en](https://patents.google.com/patent/US8999601B2/en)
    
4. Bloom Energy Server - Wikipedia, 檢索日期：1月 16, 2026， [https://en.wikipedia.org/wiki/Bloom_Energy_Server](https://en.wikipedia.org/wiki/Bloom_Energy_Server)
    
5. Everything You Need to Know About Solid Oxide Fuel Cells - Bloom Energy, 檢索日期：1月 16, 2026， [https://www.bloomenergy.com/blog/everything-you-need-to-know-about-solid-oxide-fuel-cells/](https://www.bloomenergy.com/blog/everything-you-need-to-know-about-solid-oxide-fuel-cells/)
    
6. Pathways to Commercial Success - Department of Energy, 檢索日期：1月 16, 2026， [https://www.energy.gov/sites/prod/files/2014/03/f12/pathways.pdf](https://www.energy.gov/sites/prod/files/2014/03/f12/pathways.pdf)
    
7. US8877399B2 - SOFC hot box components - Google Patents, 檢索日期：1月 16, 2026， [https://patents.google.com/patent/US8877399B2/ja](https://patents.google.com/patent/US8877399B2/ja)
    
8. Scattergood Modernization Project Alternatives: Summary of Findings - LADWP.com, 檢索日期：1月 16, 2026， [https://www.ladwp.com/sites/default/files/2025-03/Scattergood%20Moderniazation%20Alternative%20Study%20Final.pdf](https://www.ladwp.com/sites/default/files/2025-03/Scattergood%20Moderniazation%20Alternative%20Study%20Final.pdf)
    
9. BEST AVAILABLE EMISSIONS REDUCTION ASSESSMENT—PDX109 | Oregon.gov, 檢索日期：1月 16, 2026， [https://www.oregon.gov/deq/ghgp/Documents/AmazonPDX109-BAERassessment.pdf](https://www.oregon.gov/deq/ghgp/Documents/AmazonPDX109-BAERassessment.pdf)
    
10. Impexron GMBH, 檢索日期：1月 16, 2026， [https://www.impexron-gmbh.de/catalog.pdf](https://www.impexron-gmbh.de/catalog.pdf)
    
11. SBIR Awards.csv, 檢索日期：1月 16, 2026， [https://data.www.sbir.gov/awarddatapublic/award_data.csv](https://data.www.sbir.gov/awarddatapublic/award_data.csv)
    
12. 2021 Sustainability Report | Bloom Energy, 檢索日期：1月 16, 2026， [https://www.bloomenergy.com/wp-content/uploads/2021-bloom-energy-sustainability-report.pdf](https://www.bloomenergy.com/wp-content/uploads/2021-bloom-energy-sustainability-report.pdf)
    
13. schedule 14a - SEC.gov, 檢索日期：1月 16, 2026， [https://www.sec.gov/Archives/edgar/data/1664703/000120677422000941/be3994581-def14a.htm](https://www.sec.gov/Archives/edgar/data/1664703/000120677422000941/be3994581-def14a.htm)
    
14. Bloom Energy: Why Taiwanese Firms Comprise 30 Percent of Fuel Cell Maker's Supply Chain｜Industry - CommonWealth Magazine, 檢索日期：1月 16, 2026， [https://english.cw.com.tw/article/article.action?id=3781](https://english.cw.com.tw/article/article.action?id=3781)
    
15. Bloom Energy surges as AEP signs $2.65B fuel cell deal - Seeking Alpha, 檢索日期：1月 16, 2026， [https://seekingalpha.com/news/4537718-bloom-energy-surges-as-aep-signs-265b-fuel-cell-deal](https://seekingalpha.com/news/4537718-bloom-energy-surges-as-aep-signs-265b-fuel-cell-deal)
    
16. Ceres Power Holdings plc, 檢索日期：1月 16, 2026， [https://www.ceres.tech/media/o4wpgfqg/admission.pdf](https://www.ceres.tech/media/o4wpgfqg/admission.pdf)
    
17. Rare Earth Elements – a Novelty in Energy Security - jeeng.net, 檢索日期：1月 16, 2026， [https://www.jeeng.net/pdf-119810-49567?filename=49567.pdf](https://www.jeeng.net/pdf-119810-49567?filename=49567.pdf)
    
18. Supply chain analysis and material demand forecast in strategic technologies and sectors in the EU – A foresight study - Internal Market, Industry, Entrepreneurship and SMEs, 檢索日期：1月 16, 2026， [https://single-market-economy.ec.europa.eu/system/files/2023-03/Raw%20Materials%20Foresight%20Study%202023.pdf](https://single-market-economy.ec.europa.eu/system/files/2023-03/Raw%20Materials%20Foresight%20Study%202023.pdf)
    
19. Metal-Supported Solid Oxide Fuel Cells: A Review of Recent Developments and Problems, 檢索日期：1月 16, 2026， [https://www.mdpi.com/1996-1073/16/12/4700](https://www.mdpi.com/1996-1073/16/12/4700)
    
20. Ceres Power Catalyst of change - Dassault Systèmes, 檢索日期：1月 16, 2026， [https://www.3ds.com/fileadmin/Industries/High-Tech/Pdf/articles/cm13-ceres-power-high-tech-article.pdf](https://www.3ds.com/fileadmin/Industries/High-Tech/Pdf/articles/cm13-ceres-power-high-tech-article.pdf)
    
21. Improved performance of solid oxide fuel cell operating on biogas using tin anode-infiltration - University of Birmingham, 檢索日期：1月 16, 2026， [https://etheses.bham.ac.uk/6790/1/Troskialina16PhD.pdf](https://etheses.bham.ac.uk/6790/1/Troskialina16PhD.pdf)
    
22. (PDF) Review of the Application of Metal-Supported Solid Oxide Fuel Cell in the Transportation Field - ResearchGate, 檢索日期：1月 16, 2026， [https://www.researchgate.net/publication/390825062_Review_of_the_Application_of_Metal-Supported_Solid_Oxide_Fuel_Cell_in_the_Transportation_Field](https://www.researchgate.net/publication/390825062_Review_of_the_Application_of_Metal-Supported_Solid_Oxide_Fuel_Cell_in_the_Transportation_Field)
    
23. An Evaluation of Turbocharging and Supercharging Options for High-Efficiency Fuel Cell Electric Vehicles - MDPI, 檢索日期：1月 16, 2026， [https://www.mdpi.com/2076-3417/8/12/2474](https://www.mdpi.com/2076-3417/8/12/2474)
    
24. Doosan's SOFC Pivot: Inside the 2025 Data Center Push - EnkiAI, 檢索日期：1月 16, 2026， [https://enkiai.com/fuel-cells/doosans-sofc-pivot-inside-the-2025-data-center-push](https://enkiai.com/fuel-cells/doosans-sofc-pivot-inside-the-2025-data-center-push)
    
25. Ceres Power 2025: Fuel Cell Commercial Breakout Begins - EnkiAI, 檢索日期：1月 16, 2026， [https://enkiai.com/fuel-cells/ceres-power-2025-fuel-cell-commercial-breakout-begins](https://enkiai.com/fuel-cells/ceres-power-2025-fuel-cell-commercial-breakout-begins)
    
26. Weichai sign manufacturing licence for SOFC power - Ceres Power Holdings plc, 檢索日期：1月 16, 2026， [https://www.ceres.tech/newsroom/news-and-insights/weichai-sign-manufacturing-licence-for-sofc-power/](https://www.ceres.tech/newsroom/news-and-insights/weichai-sign-manufacturing-licence-for-sofc-power/)
    
27. Bosch Hydrogen Strategy 2025: Dominating a $5.3B Market - EnkiAI, 檢索日期：1月 16, 2026， [https://enkiai.com/bosch/bosch-hydrogen-strategy-2025-dominating-a-5-3b-market](https://enkiai.com/bosch/bosch-hydrogen-strategy-2025-dominating-a-5-3b-market)
    
28. Ceres Power Analysis 2025: Inside the SOFC/SOEC Pivot - EnkiAI, 檢索日期：1月 16, 2026， [https://enkiai.com/fuel-cells/ceres-power-analysis-2025-inside-the-sofc-soec-pivot](https://enkiai.com/fuel-cells/ceres-power-analysis-2025-inside-the-sofc-soec-pivot)
    
29. TECHNOLOGY REVIEW – SOLID OXIDE CELLS 2019 - Energiforsk, 檢索日期：1月 16, 2026， [https://energiforsk.se/media/26740/technology-review-solid-oxide-cells-2019-energiforskrapport-2019-601.pdf](https://energiforsk.se/media/26740/technology-review-solid-oxide-cells-2019-energiforskrapport-2019-601.pdf)
    
30. Levelized Cost of Energy+ (LCOE+) - Lazard, 檢索日期：1月 16, 2026， [https://www.lazard.com/research-insights/levelized-cost-of-energyplus-lcoeplus/](https://www.lazard.com/research-insights/levelized-cost-of-energyplus-lcoeplus/)
    
31. LEVELIZED COST OF ENERGY+ - Lazard, 檢索日期：1月 16, 2026， [https://www.lazard.com/media/uounhon4/lazards-lcoeplus-june-2025.pdf](https://www.lazard.com/media/uounhon4/lazards-lcoeplus-june-2025.pdf)
    
32. Ceres Power Fuels Investors' Illusions With Misleading Promises - Grizzly Research, 檢索日期：1月 16, 2026， [https://grizzlyreports.com/ceres/](https://grizzlyreports.com/ceres/)
    


## Scandium 稀土元素的礦源以及提煉來源

Scandium (鈧) 是一種稀有的過渡金屬，通常不單獨成礦，而是作為其他礦物加工過程中的副產品被提煉出來。由於 Bloom Energy 的 SOFC 電解質 (ScSZ) 高度依賴此元素，其供應鏈的安全性至關重要。

根據研究資料，Scandium 的主要礦源與提煉來源如下：

**1. 主要礦源 (Mining Sources)**

- **菲律賓 (鎳礦副產品)：** 這是 Bloom Energy 供應鏈中最具戰略意義的來源。日本住友金屬礦山 (Sumitomo Metal Mining) 在菲律賓 Taganito Bay 的高壓酸浸 (HPAL) 鎳礦工廠中，建立了從鎳鈷尾礦中回收鈧的設施。
    
- **中國與俄羅斯 (鈦/鈾副產品)：** 傳統上，全球大部分的鈧是來自中國與俄羅斯，主要作為鈦白粉 (Titanium Dioxide) 生產或鈾礦加工過程中的副產品被提取。中國曾控制全球約 85% 的精煉鈧供應。
    
- **加拿大 (鈦鐵礦副產品)：** 礦業巨頭 Rio Tinto (力拓) 在加拿大魁北克省的 Sorel-Tracy 營運一座工廠，利用其創新的模組化技術，從鈦鐵礦冶煉產生的廢渣中提取氧化鈧。
    
- **澳洲 (開發中專案)：** 澳洲擁有多個富含鈧的紅土鎳鈷礦專案，例如 Sunrise Energy Metals 和 Metallica Minerals (SCONI 專案)。這些專案被視為未來西方世界擺脫對中國依賴的潛在關鍵。
    

**2. 提煉與精煉來源 (Refining Sources)**

- **日本：** 住友金屬礦山將菲律賓生產的中間產物（草酸鈧）運回日本播磨 (Harima) 的工廠進行最終精煉，轉化為高純度的氧化鈧 (Sc$_2$O$_3$)。資料指出，這條「菲律賓開採 -> 日本精煉」的路線是 Bloom Energy 的主要供應管道。
    
- **中國：** 中國擁有全球最大的稀土分離與精煉產能。然而，2025 年中國實施了新的出口管制，將鈧列為軍民兩用物資，這迫使西方企業加速尋找替代的精煉來源。
    
- **加拿大：** Rio Tinto 在魁北克的工廠具備將廢渣直接提煉為年產能約 3 噸的 99.99% 高純度氧化鈧的能力，是北美首個商業化鈧氧化物生產設施。
    

總結對 Bloom Energy 的影響：

Bloom Energy 是全球最大的鈧消費者之一（曾一度佔全球需求量的 80%）。為了規避地緣政治風險，Bloom 已明確採取供應商多樣化策略，將重心從中國轉移至日本、菲律賓及其他擁有強大監管框架的地區。

## 高力

高力熱處理 (Kaori Heat Treatment, 8996.TW) 在 Bloom Energy 供應鏈中的地位極為核心，甚至可以說是 Bloom Energy 硬體製造中最重要的非美系合作夥伴之一。

根據研究資料，高力實際上提供的不僅僅是單一零件，而是 Bloom Energy Server 系統中核心的心臟地帶——**「熱箱 (Hot Box)」的關鍵總成與核心熱交換組件**。

以下是高力具體提供的零組件細節與技術價值：

### 1. 核心產品：Hot Box (熱箱) 機構件與總成

這是高力對 Bloom Energy 最主要的出貨產品。

- **定義**：<font color="#245bdb">Hot Box 是 SOFC 系統的核心反應室，內部封裝了燃料電池堆疊 (Stack)。由於 SOFC 運作溫度高達 800-850°C，這個箱體必須具備極高的隔熱性、氣密性與結構強度。</font>
    
- **高力的角色**：高力利用其核心的「金屬熱處理」與「精密焊接」技術，製造 Hot Box 的金屬外殼與內部複雜的流道結構，並負責將相關組件組裝成一個模組出貨給 Bloom。這是一個高單價、高技術門檻的次系統。
    

### 2. 關鍵組件：高溫板式熱交換器 (High-Temperature Plate Heat Exchangers)

這是 Hot Box 內部最關鍵的「次零件」，也是高力的「老本行」。

- **功能**：SOFC 需要將進入的冷燃料 (天然氣) 和冷空氣預熱到 700°C 以上才能開始反應。為了達到 Bloom 宣稱的 60% 高效率，系統必須回收高溫廢氣的熱能來預熱進氣。
    
- **技術門檻**：<font color="#245bdb">一般的熱交換器無法承受 800°C 的高溫且容易洩漏（導致燃料與空氣混合引發爆炸）。高力採用專利的**真空硬銲 (Vacuum Brazing)** 技術，製造出能耐受極高溫、體積小且氣密性完美的板式熱交換器。</font>
    
- **具體配置**：一個 Hot Box 內部通常包含多組熱交換器，分別用於：
    
    - **陰極回熱器 (Cathode Recuperator)**：利用廢熱加熱進入的空氣。
        
    - **陽極回熱器 (Anode Recuperator)**：利用廢熱加熱進入的燃料。
        

### 3. 燃料重組器組件 (Fuel Reformer Assemblies)

- Bloom 的系統宣稱可以直接使用天然氣，這需要一個「重組 (Reforming)」過程將甲烷轉化為氫氣。
    
- 雖然催化劑本身可能由 Johnson Matthey 提供，<font color="#245bdb">但**重組器的物理結構 (Reactor structure)**——即讓氣體流動並與催化劑接觸的金屬載體與流道板，通常也由具備精密流道設計能力的高力製造。</font>
    

### 4. 反應爐機構件 (Balance of Plant components inside Hot Box)

- 包含用於導流氣體的**分歧管 (Manifolds)** 與其他耐高溫的結構件。這些零件必須由特殊的耐高溫合金製成，並經過特殊的抗氧化處理，這正是高力熱處理技術的強項。
    

### 總結：為什麼是高力？

Bloom Energy 之所以高度依賴高力（甚至曾投資高力），是因為 **「真空硬銲」** 技術。在 SOFC 的高溫環境下，傳統的橡膠密封墊片會瞬間熔化，普通的焊接容易產生熱應力裂痕。<font color="#245bdb">高力的硬銲技術能將多層金屬板「融」為一體，形成如同一塊實心金屬般的強度，卻內部中空可供氣體流動，這是製造 SOFC 熱交換器與反應室最可靠的工藝之一。</font>

**簡單來說，Bloom Energy 負責「發電的陶瓷片 (電池堆)」，<font color="#245bdb">而高力負責製造「讓這些陶瓷片能安全在高溫下運作的那個金屬盒子與散熱系統」。**</font>

