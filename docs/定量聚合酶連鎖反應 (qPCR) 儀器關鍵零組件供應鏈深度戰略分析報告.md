
## **執行摘要 (Executive Summary)**

定量聚合酶連鎖反應（Quantitative Polymerase Chain Reaction, qPCR）儀器作為現代分子診斷的黃金標準，其市場在後疫情時代經歷了結構性的轉變。從實驗室的基礎研究工具到臨床診斷的核心設備，qPCR 儀器的性能與可靠性完全取決於其內部複雜且精密的零組件生態系統。本報告旨在提供一份詳盡的技術與供應鏈分析，深入探討構成 qPCR 儀器的四大關鍵子系統：熱循環引擎（Thermal Cycling Engine）、光學激發系統（Optical Excitation System）、光學濾波與光路管理（Optical Emission & Management）、以及光電偵測系統（Detection Assembly）。

本分析特別關注全球供應鏈的二元對立與融合趨勢：一方面是長期壟斷高階市場的歐美日傳統大廠（如 Hamamatsu、Ferrotec、Semrock），另一方面是憑藉半導體製造優勢與精密加工能力迅速崛起的台灣與亞洲供應鏈（如 Everlight、OtO Photonics、Asia Optical、VisEra）。分析顯示，產業正從依賴光電倍增管（PMT）與昂貴濾光片的「封閉式光學架構」，轉向採用高功率 LED、矽光電倍增管（SiPM）、CMOS 影像感測器以及模組化光譜引擎的「固態光學架構」。這一轉變不僅降低了製造成本，更推動了即時照護檢測（POCT）設備的微型化與普及化。

---

## **第一章：緒論——精準診斷的物理基礎與架構解構**

要深入剖析 qPCR 儀器的供應鏈，首先必須從物理層面解構其運作原理與工程挑戰。一台標準的 qPCR 儀器本質上是一個結合了精密熱力學控制與高靈敏度螢光光度計的複雜系統。其核心任務是在極短的時間內對微量樣品（通常為 10-50 微升）進行數十次的溫度循環，同時精確測量在特定波長下被激發的螢光訊號。

### **1.1 熱力學挑戰：均勻性與速率的博弈**

PCR 反應依賴三個關鍵溫度點：變性（Denaturation, \~95°C）、黏合（Annealing, \~55-60°C）與延伸（Extension, \~72°C）。工程上的最大挑戰在於「熱均勻性」（Thermal Uniformity）與「升降溫速率」（Ramp Rate）。

* **均勻性要求：** ==在 96 孔或 384 孔反應盤中，所有孔位的溫度差異必須控制在 ±0.1°C 以內 1。若邊緣效應導致溫度偏差，將直接影響擴增效率（Amplification Efficiency），導致定量結果的 Ct 值（Cycle Threshold）漂移，進而產生偽陰性或偽陽性結果。==  
* **速率要求：** 為了縮短檢測時間，現代快速 PCR 儀器要求升溫速率達到 3°C/sec 至 5°C/sec，甚至更高 1。這對加熱元件的功率密度與散熱系統的瞬態響應提出了極高要求。

### **1.2 光學挑戰：在強光背景下尋找微弱訊號**

qPCR 的光學偵測屬於典型的「螢光測量」，其訊噪比（SNR）極為關鍵。系統必須發射強大的激發光（Excitation）以激活樣品中的螢光團（Fluorophores，如 FAM、HEX、ROX、Cy5），同時必須極度有效地阻擋這些激發光進入偵測器，僅允許微弱的發射光（Emission）通過。==這通常要求光學濾波系統具備 OD6（Optical Density 6，即百萬分之一穿透率）以上的阻絕能力== 3。

---

## **第二章：熱循環引擎——熱電效應的極限與可靠性工程**

熱循環模組是 qPCR 儀器的「心臟」。不同於一般的恆溫培養箱，PCR 儀器的加熱元件必須承受數十萬次劇烈的溫度變化，這使得材料的熱膨脹係數（CTE）匹配成為可靠性的核心問題。目前，基於帕爾帖效應（Peltier Effect）的熱電致冷模組（Thermoelectric Cooler, TEC）是主流技術。

### **2.1 熱電模組（Peltier Modules）：循環疲勞與技術壁壘**

標準的熱電模組設計用於穩態冷卻（例如電子元件散熱或車用冰箱），若直接應用於 PCR 的快速熱循環，會因為陶瓷基板與銅導流條之間的焊點疲勞（Solder Joint Fatigue）而迅速失效。

#### **2.1.1 全球市場領導者與技術標準**

**Ferrotec（日本/全球）** 是此領域無可爭議的霸主。其專為 PCR 應用設計的 **70-Series Thermal Cycling Modules** 已成為產業標準 5。

* **技術深度解析：** Ferrotec 的循環模組（如型號 72008/199/160B）採用了特殊的彈性焊料與擴散阻絕層技術。在 PCR 循環中，模組會經歷從加熱（電流正向）到冷卻（電流反向）的劇烈切換，導致半導體晶粒（Pellets）承受巨大的剪切應力。Ferrotec 的技術能確保模組在 $\\Delta T\_{max}$ 高達 83°C 的條件下，承受超過 50 萬次的循環而不發生電阻顯著增加或陶瓷破裂 7。  
* **失效模式防護：** 其設計重點在於防止「熱循環疲勞」（Thermal Cycle Fatigue）導致的微裂紋擴展，這是普通 TEC 在 PCR 應用中壽命極短的主因 8。

**Laird Thermal Systems（美國/全球）** 則是主要的挑戰者，其 **PowerCycling PCX Series** 代表了另一種技術路徑 9。

* **柔性層創新（Soft Layer）：** Laird 在陶瓷基板與銅導流條之間引入了一層導熱但具備機械柔性的「軟層」（Soft Layer）。這層材料能吸收因熱脹冷縮產生的機械應力，從而保護陶瓷基板不致破裂 10。  
* **POCT 應用優化：** 針對長條形反應槽（如 2x8 孔的快篩設備），Laird 推出了 Elongated PCX 系列。長條形 TEC 在製造上極具挑戰，因為長軸方向的熱變形累積效應更嚴重，容易導致「弓形彎曲」（Bowing Effect），Laird 的製程控制克服了這一點，確保了與散熱器的緊密接觸 10。

**TE Technology（美國）** 則專注於控制器與模組的整合，強調使用高頻脈寬調變（PWM）控制來減少熱衝擊，防止因控制演算法不當造成的額外熱應力 11。

#### **2.1.2 台灣熱電模組供應鏈的崛起**

台灣在熱電材料領域已建立起具備高度競爭力的供應鏈，特別是在中階與可攜式 PCR 設備市場，提供了高性價比的替代方案。

* **Z-Max（台灣/日本）：** Z-Max 是一家專注於高可靠性熱電模組的製造商，在台灣與中國均有生產基地。其產品線特別針對 PCR 儀器常見的「結露」與「腐蝕」問題進行了優化。  
  * **GL 結構與防潮：** 針對 PCR 降溫階段（如 60°C 降至 50°C 或更低）容易產生冷凝水的問題，Z-Max 強調其模組的防潮密封（Humidity Protection Sealing），防止水氣滲入導致電化學遷移（Migration）與短路 12。其 GL 結構設計亦旨在分散熱應力。  
* **T-Global（高柏科技）：** 雖然以導熱介面材料（TIM）聞名，T-Global 亦供應標準尺寸（如 40x40mm, 30x30mm）的熱電晶片，這些尺寸與標準 96 孔盤的幾何形狀高度吻合，適合模組化 PCR 儀器的快速開發 13。  
* **P-Max：** 在學術與技術文獻中，P-Max 的熱電發電模組（TEG）與冷卻模組常被引用，特別是在探討最大功率輸出（$P\_{max}$）與內部電阻優化的研究中，顯示其在材料基礎研發上的投入 14。

### **2.2 精密反應槽（Reaction Block）與加工工藝**

熱電模組負責搬運熱能，但真正承載樣品的是反應槽（Block）。==反應槽的材質選擇與加工精度直接決定了熱傳導效率與孔間均勻性。==

* **材料物理特性：**  
  * **鋁合金：** 是最常見的材質，熱導率約 205 W/mK。其優點是成本低、易加工，但熱導率相對較低，限制了升降溫速率。  
  * **銀槽：** 高階機種（如 Eppendorf 或 Roche 的某些型號）使用純銀或鍍金銀槽，熱導率高達 406 W/mK，能實現極快的變溫，但成本極高且需特殊的表面處理以防腐蝕。  
* **台灣精密加工供應鏈：** 台灣發達的 CNC 加工產業在此環節扮演關鍵角色。  
  * Pyramids Technology（金三角科技）16： 專精於醫療級精密加工。在 PCR 反應槽的製造中，96 個孔位的深寬比、孔壁的光潔度以及孔底與 PCR 耗材（管子）的貼合度（Fit Tolerance）至關重要。微米級的誤差都會導致空氣間隙（Air Gap），形成熱阻，影響實驗結果。Pyramids 提供此類高精密度的加工服務。  
  * Intai Technology（櫻田科技）17： 作為醫療器材零組件的重要供應商，Intai 利用 5 軸 CNC 加工技術製造幾何形狀複雜的反應槽，透過輕量化設計減少熱容（Thermal Mass），從而提升升降溫速率。  
  * Han Chang（漢昌）18： 專注於鋁擠型與陽極處理。PCR 反應槽必須經過特殊的陽極氧化處理（Anodizing），以形成堅硬的氧化層。這不僅是為了防腐蝕（防止清潔用的漂白水損壞槽體），更是因為裸露的鋁金屬離子可能會抑制聚合酶的活性，影響反應效率。

### **2.3 熱管理系統整合**

除了核心的 TEC 與 Block，熱管理還包括散熱器與導熱介面材料。

* **系統整合：** 台灣的 Galaxy PCB（嘉立電子）19 與 Taiwan Electronic Cooling (TEC) Co., Ltd. 20 提供了從 PCB 設計到熱模組組裝的整合服務。PCR 儀器的散熱器設計必須能夠在 TEC 全功率製冷（加熱面產生大量廢熱）時，迅速將熱量移除，否則 TEC 的 $\\Delta T$ 將飽和，導致降溫失敗。

---

## **第三章：光學激發系統——從鹵素燈到固態照明的革命**

早期的 qPCR 儀器（如 ABI 7500）多採用鎢鹵素燈（Tungsten-Halogen Lamps）搭配濾光輪。然而，鹵素燈存在壽命短、產熱高、光譜漂移等問題。現代儀器已全面轉向固態照明（Solid-State Illumination），即高功率 LED。

### **3.1 激發光譜與物理要求**

qPCR 依賴特定波長的窄頻激發來匹配常用的螢光染料：

* **FAM/SYBR Green:** 激發波長約 470 nm（藍光）。  
* **HEX/VIC:** 激發波長約 530 nm（綠光）。  
* **ROX/Texas Red:** 激發波長約 585 nm（琥珀/紅光）。  
* **Cy5:** 激發波長約 640 nm（深紅光）。

LED 必須具備「高輻射通量」（High Radiant Flux），通常要求驅動電流 \>350mA 甚至 \>1A，以產生足夠的光子激發低濃度的 DNA 樣品。

### **3.2 全球 LED 領導廠商**

* **Lumileds (Luxeon):** 其 Luxeon C 與 Z 系列是多色 LED 的標竿。特別是其「Lime」（萊姆綠）與「Cyan」（青色）LED，填補了傳統 RGB LED 在綠光波段的效率凹陷（Green Gap），對多重 PCR（Multiplex PCR）至關重要 21。  
* **Osram (ams OSRAM):** OSLON SSL 系列以其緊湊的封裝與極高的光通量密度著稱，廣泛應用於緊湊型光學模組 23。

### **3.3 台灣 LED 供應鏈的生醫轉型**

台灣作為全球 LED 製造重鎮，其供應鏈正積極從通用照明轉向高附加價值的生醫儀器市場。

#### **3.3.1 億光電子 (Everlight Electronics)**

24

億光是 qPCR 激發光源的關鍵供應商，其 **EAHP3535 系列**（3.5mm x 3.5mm 陶瓷封裝）直接對標 Cree XP 與 Osram OSLON 系列，但在性價比與供應穩定性上具備優勢。

* **特定波長優勢：**  
  * **450-470 nm (Blue):** 專為 FAM 染料激發設計。EAHP3535 數據表顯示其具備極高的輻射通量穩定性，這對於定量分析至關重要，因為光源強度的波動會直接導致定量誤差 26。  
  * **660 nm (Deep Red):** 億光的 **HPND3535CZ0112**（原主打植物照明）在 Cy5 激發上表現卓越。其輻射效率（Radiant Efficiency）高達 71%，在 700mA 驅動下可輸出 1070mW 的功率 27。如此高的電光轉換效率大幅降低了光學模組的散熱需求，這對於緊湊型或手持式 PCR 儀器是決定性的優勢。  
  * **車規級可靠性：** 該系列通過 AEC-Q101 認證，意味著其抗硫化、抗濕氣能力遠優於一般消費級 LED，符合醫療儀器對長壽命的要求 24。

#### **3.3.2 雷笛克/隆達電子 (Lextar, Ennostar Group)**

28

隸屬於富采控股（Ennostar）的隆達電子，展現了垂直整合的優勢。

* **3030 與 3535 封裝：** Lextar 的 **PC33U62** 與 **PC35U16** 系列提供了高密度的光子輸出 30。  
* **Mini-LED 與 Micro-LED 潛力：** Lextar 正積極推動 Mini-LED 在醫療顯示與儀器上的應用 32。在下一代「數位 PCR」（dPCR）中，可能需要對成千上萬個微滴（Droplets）進行獨立照明，Lextar 的高密度 Mini-LED 陣列技術有望取代掃描式雷射，實現全盤同時激發。  
* **UVC 殺菌整合：** Lextar 在 275nm UVC LED 領域的技術領先，這類光源正被整合進 PCR 工作站（Workstation）內部，用於實驗後的氣溶膠污染清除（Decontamination），防止交叉污染 33。

#### **3.3.3 光寶科技 (Lite-On Technology)**

34

光寶科技提供 **LTL 與 LTPL** 系列高功率 LED。其 **CoB (Chip on Board)** 封裝技術允許將多顆不同波長的晶片整合在極小的基板上，這對於使用「光纖束」（Fiber Optic Bundles）導光的系統非常有利，可以從單一點光源輸出多色激發光 36。

---

## **第四章：光學濾波與光路管理——訊噪比的守門員**

激發光照射樣品後，螢光團會產生史托克斯位移（Stokes Shift），發射出波長較長但強度極弱的螢光。==光學系統的核心任務就是將這微弱的訊號從強大的激發背景光中分離出來，這完全依賴於光學濾光片（Optical Filters）==。

### **4.1 螢光濾光片：技術規格與製程**

現代 qPCR 儀器幾乎全數採用 **硬鍍膜（Hard-Coated / Sputtered）干涉濾光片**。相較於早期的軟鍍膜（Soft-Coated），硬鍍膜採用離子束濺射（Ion Beam Sputtering, IBS）製程，膜層緻密，不會因受潮而老化，且能承受高功率 LED 的照射而不發生熱漂移。

#### **4.1.1 全球「三巨頭」**

* ==**Semrock (IDEX Health & Science):**== 業界的黃金標準。其 "BrightLine" 系列濾光片定義了高階 qPCR 的規格 37。Semrock 擅長製造「多頻帶」（Multiband）濾光片，允許在單一濾光片上同時穿透 FAM、HEX、ROX 的訊號，實現無機械動作的多重檢測 39。  
* **Chroma Technology:** 另一大巨頭，其 **ET (Exciton Transmission)** 系列提供極陡峭的截止邊緣（Steep Edges），能在極窄的波長間隔內實現 \>OD6 的阻絕，最大化訊號獲取 39。  
* **Omega Optical:** 美國老牌供應商，常提供具成本競爭力的替代方案。

#### **4.1.2 亞洲濾光片供應鏈的挑戰與突破**

雖然高階市場仍由歐美主導，但台灣與中國的供應商正憑藉優異的鍍膜技術切入中階市場。

* **Global Hitronics (海創光電/台灣銷售網絡)：** 該公司明確針對 qPCR 市場推出了螢光濾光片系列。其數據表宣稱在 350-850nm 範圍內具備 **OD≥6** 的阻絕能力 4。  
  * **戰略意義：** OD6 代表僅百萬分之一的背景光能穿透。在以往，這是 Semrock 等大廠的專利。Global Hitronics 能以更低的成本提供此規格，使其成為可攜式與定點照護 PCR 儀器的理想選擇 4。  
* Pylong Technologies (Optolong / 宇隆光電) 42： 原本以天文濾鏡（抗光害濾鏡）聞名，Optolong 成功轉型至生醫領域。  
  * **技術遷移：** 天文觀測與螢光偵測有著相同的物理需求——在極黑背景下尋找微弱光點。Optolong 掌握了離子束輔助沈積（IAD）技術，能製造用於 FISH（螢光原位雜合）與 qPCR 的高對比度濾鏡，涵蓋 DAPI, FITC, TRITC 等波段 42。  
* Shapeoptics (新加坡/台灣) 44： 提供直徑 8mm-15mm 的標準生醫濾光片，專攻生化分析儀與微盤讀取儀（Microplate Readers）。其規格明確標示 **穿透率 \>93%** 與 **阻絕 \>OD6**，直接對標歐美一線產品 46。  
* Auxcera (奧特光學) 48： 專精於「超窄頻帶」（Ultra Narrow BandPass）與「陷波」（Notch）濾光片。在 5-plex 或 6-plex 的高階多重 PCR 中，激發光譜極易重疊，Auxcera 的技術能有效分離多重光源，解決串擾（Crosstalk）問題。

### **4.2 光路元件與精密透鏡**

將 LED 的光準直並均勻照射到反應盤，以及將螢光聚焦到偵測器，需要高精度的透鏡模組。

* Asia Optical (亞光) 49： 著名的相機鏡頭大廠。其核心競爭力在於 **精密玻璃模造（Precision Glass Molding, PGM）** 非球面透鏡。  
  * **應用：** 在 qPCR 光路中，非球面透鏡能有效修正球差，確保光束的準直度，這對於全盤成像（Whole Plate Imaging）系統至關重要，能保證邊緣孔位的照明均勻度。亞光近期推出的血管篩檢儀等醫療設備，顯示其已具備整機醫療光學的設計能力 51。  
* Calin Technology (佳凌科技) 52： 專精於 **模造玻璃（GMO）** 與高精度塑膠透鏡。其在醫療內視鏡鏡頭上的技術積累，使其具備製造微型透鏡的能力，這對於需要對每個反應孔進行獨立光學耦合的微流道 PCR 系統非常關鍵 53。  
* Young Optics (揚明光學) 54： 中強光電集團子公司，是 **DLP (Digital Light Processing)** 投影引擎的領導者。  
  * **前瞻應用：** 在數位 PCR (dPCR) 與空間生物學（Spatial Biology）領域，DLP 技術正被用於「結構光照明」（Structured Illumination），以精確激活特定區域的樣本。Young Optics 供應基於 TI DLP 晶片的光學模組，是高階科研儀器的關鍵供應商 54。

---

## **第五章：光電偵測系統——光子捕獲的極限**

偵測器負責將濾波後的螢光訊號轉換為電訊號。這是決定儀器靈敏度（Sensitivity）與動態範圍（Dynamic Range）的最後一哩路。

### **5.1 光電倍增管 (PMT)：傳統王者的堅持**

**==Hamamatsu Photonics (濱松光子)==** 57 在此領域擁有絕對統治地位。PMT 是真空管技術，能提供 $10^6$ 的增益，意味著單個光子就能產生可測量的電流。

* **適用場景：** ==儘管體積大、需要高壓（\~1000V）、易損壞，但 Roche LightCycler 與 ABI 的高階機型仍堅持使用 PMT，因為其在極低光強下的信噪比仍是固態元件難以企及的。==

### **5.2 固態革命：光電二極體與 SiPM**

隨著半導體技術進步，固態偵測器正逐漸取代 PMT，特別是在體積與成本敏感的機型中。

#### **5.2.1 ==矽光電二極體 (Silicon Photodiodes, PD)==**

這是==標準型 PCR 儀（如 Bio-Rad CFX96）最常用的偵測器==。

* Excelitas 59: 提供 PIN 光電二極體，針對藍/綠光波段進行了靈敏度優化。  
* Taiwan Asia Semiconductor (TASC / 台亞半導體) 61： 前身為光磊科技。TASC 製造的矽光電二極體晶片（PD Chips）感測範圍涵蓋 400-1100nm。其 **PD-00xx** 系列是大規模生產的標準感測元件，為開放式架構的 PCR 儀器提供了低成本且性能穩定的選擇。

#### **5.2.2 矽光電倍增管 (SiPM) 與 APD**

SiPM 是由成千上萬個工作在蓋革模式（Geiger Mode）下的 APD 組成的陣列，具備類似 PMT 的高增益，但工作電壓僅需 30V-50V，且堅固耐用。

* Onsemi (安森美) 63: 其 **C-Series** 與 **J-Series** SiPM 是醫療影像（如 PET 掃描）的標竿，現正被導入緊湊型 qPCR 儀器，以實現「單光子級」的靈敏度 65。  
* Hamamatsu MPPC 66: 濱松自家的 SiPM 產品（稱為 MPPC），在手持式診斷設備中廣泛應用。

### **5.3 CMOS 影像感測器：全盤成像的崛起**

傳統 PCR 儀器多採用機械掃描（Scanning），==現代趨勢則是利用相機對整個 96 孔盤進行一次性成像（Imaging）。==

* Sony 68: 其 **IMX** 系列（如 IMX273, IMX178）具備全域快門（Global Shutter），是高通量讀取儀的首選。Sony 的 **SenSWIR** 技術（InGaAs）更開啟了 NIR-II（1000nm 以上）偵測的大門，未來可能應用於更多重通道的 PCR 系統 69。  
* VisEra Technologies (采鈺科技) 70： 台積電與 OmniVision 的合資公司，專精於 **晶圓級光學（Wafer-Level Optics）** 與 **彩色濾光片（Color Filters）**。  
  * **關鍵技術突破：奈米光柱（Nano-Light Pillars, NLP）：** VisEra 開發種類似超穎表面（Metasurface）的結構，直接在 CMOS 畫素上構建奈米光柱。這項技術能將藍光與綠光的量子效率（Quantum Efficiency, QE）提升 40% 71。這對於 qPCR 來說是革命性的，因為 FAM 與 HEX 正好位於此波段。這意味著普通的 CMOS 感測器在經過 NLP 處理後，無需昂貴的製冷系統即可偵測到微量的 qPCR 螢光訊號。  
* PixArt Imaging (原相科技) 72： 以光學滑鼠感測器起家，原相已跨足 **智慧動態偵測（Smart Motion Detection）** 與健康管理感測。其低功耗全域快門感測器（如 **PS5262LT**）非常適合電池供電的可攜式 PCR 設備。全域快門能消除果凍效應，這對於手持式或野外震動環境下的診斷設備尤為重要。  
* Artilux (光程研創) 74： **GeSi (鍺矽)** 光子技術的先驅。雖然目前主要應用於 3D 感測，但其感測器在 SWIR（短波紅外線）波段的優異表現具有巨大的生醫潛力。在 1000nm 以上的「生物光學窗口」，生物組織的自發螢光（Autofluorescence）極低，背景雜訊極小。Artilux 的 GeSi 感測器若應用於未來的 qPCR，將能實現極高信噪比的檢測，且比傳統 InGaAs 感測器成本更低 74。

---

## **第六章：模組化光學引擎與 ODM 整合趨勢**

產業的另一個顯著趨勢是從購買離散元件（LED、濾光片、感測器）轉向採購已校準的「光學引擎」（Optical Engines）。

### **6.1 OtO Photonics (台灣超微光學)**

76

OtO Photonics 代表了這種模組化趨勢的極致。

* **SmartEngine (SE) 系列：** 不同於傳統的濾光片系統，OtO 提供的是微型 **光譜儀（Spectrometer）**。系統使用線型 CCD/CMOS 感測器（來自 Sony/Hamamatsu/Toshiba）配合光柵，捕捉發射光的 *完整光譜* 77。  
* **qPCR 應用優勢：** 光譜儀引擎可以通過軟體演算法進行「解卷積」（De-convolution），區分光譜重疊嚴重的螢光團（例如區分 FAM 與 SYBR Green，或分離 5-plex 以上的緊密染料）。這消除了物理濾光片的限制，縮小了體積。其 SE 系列提供低至 0.2nm 的解析度與優異的熱穩定性，非常適合高精度的醫療分析 78。

### **6.2 封裝與系統整合**

* Tong Hsing Electronic Industries (同欣電子) 80： 全球最大的 CIS（CMOS 影像感測器）第三方封裝廠。他們為主要感測器大廠提供陶瓷基板與打線接合（Wire Bonding）服務，這對於要求高可靠性與耐濕熱的醫療電子至關重要。在醫療內視鏡與生物晶片封裝領域，同欣電扮演著關鍵的幕後推手角色。  
* Chunghwa Leading Photonics Tech (CLPT / 中華立鼎光電) 82： 中華電信子公司，專注於 InGaAs 感測器。隨著 PCR 往紅外波段發展，CLPT 提供的 InGaAs 光電二極體與線性陣列，將成為未來 NIR-PCR 市場的重要元件來源。

---

## **第七章：供應鏈戰略總結**

### **7.1 qPCR 關鍵零組件的地緣政治與技術版圖**

分析顯示，qPCR 供應鏈呈現鮮明的二元結構：

1. **高階/傳統效能（High-Performance/Legacy）：** 美國與日本（Hamamatsu, Ferrotec, Semrock, Lumileds）仍掌握著最高靈敏度 PMT、最耐用熱電模組與最深阻絕濾光片的關鍵 IP。頂級儀器（如 Roche LightCycler, Thermo QuantStudio, Bio-Rad CFX）的核心性能仍高度依賴此供應鏈。  
2. **高量/新興架構（High-Volume/New-Architecture）：** 台灣與中國已建立起平行的生態系統。台灣在 **半導體感測（VisEra, TASC, Artilux）**、**LED 光源（Everlight, Lextar）** 以及 **精密光學整合（OtO Photonics, Asia Optical）** 方面表現卓越。此供應鏈正在推動「定點照護」（Point-of-Care）革命——即製造更小、更便宜、但性能足夠的固態 PCR 儀器，實現分子診斷的普及化。

### **7.2 採購與研發建議**

* **熱循環系統：** 不可妥協於熱電模組。若設計 PCR 儀，務必選用額定為 *Thermal Cycling* 的模組（如 Ferrotec 70-Series 或 Laird PCX）。使用標準冷卻用 Peltier 將導致設備在數月內因熱疲勞而失效。  
* **光學濾波：** 對於成本敏感型專案，Shapeoptics 與 Global Hitronics 等亞洲供應商提供的 OD6 濾光片已能滿足絕大多數 PCR 應用，性價比極高。  
* **偵測系統：** 未來在於 CMOS。VisEra 的奈米光柱技術與 Sony 的 SenSWIR 技術表明，標準影像感測器的靈敏度正逼近專用光電二極體，這將使「全盤成像式」PCR 系統在成本上遠低於「掃描式」系統，成為市場主流。

### **附錄：關鍵零組件供應商矩陣**

| 零組件類別 | 全球市場領導者 (高階/傳統) | 台灣/亞洲創新者 (高量/整合) | 關鍵技術規格 / 趨勢 |
| :---- | :---- | :---- | :---- |
| **激發光源 (LED)** | **Lumileds** (USA/Global) **Osram** (Germany) **Luminus** (USA) | **Everlight** (Taiwan) \- 3535 Series **Lextar** (Taiwan) \- Mini-LED **Lite-On** (Taiwan) \- CoB | 輻射通量穩定性; 特定波長 (470/530/640nm); 熱阻管理 |
| **濾光片 (Filters)** | **Semrock (IDEX)** (USA) \- Hard Coated **Chroma** (USA) **Omega** (USA) | **Global Hitronics** (China/TW) \- OD6 **Pylong (Optolong)** (China) \- 天文轉生醫 **Shapeoptics** (SG/TW) | 阻絕度 \>OD6; 穿透率 \>93%; 邊緣陡峭度; 硬鍍膜耐用性 |
| **偵測器 (Sensors)** | **Hamamatsu** (Japan) \- PMT/SiPM **Excelitas** (USA) \- APD/PD **Onsemi** (USA) \- SiPM | **VisEra** (Taiwan) \- 奈米光柱 (NLP) **TASC** (Taiwan) \- 光電二極體 **OtO Photonics** (Taiwan) \- 光譜儀 **PixArt** (Taiwan) \- 低功耗全域快門 | 500-700nm 量子效率 (QE); 低暗電流; 增益 (SiPM/PMT) |
| **熱循環引擎 (TEC)** | **Ferrotec** (Japan) \- 70 Series (Cycling) **Laird** (USA/Global) \- PCX Series | **Z-Max** (Taiwan/Japan) \- 防潮結構 **T-Global** (Taiwan) **P-Max** (Taiwan) | **循環壽命** (\>50 萬次); 軟層應力釋放; PWM 控制相容性 |
| **精密加工 (Block)** | **歐美在地工廠** | **Pyramids Tech** (Taiwan) \- 醫療級 **Intai Tech** (Taiwan) **Han Chang** (Taiwan) \- 陽極處理 | 熱導率; 平整度公差; 生物相容性陽極處理 |
| **光學模組/透鏡** | **Jenoptik** (Germany) **Basler** (Germany) | **Asia Optical** (Taiwan) \- 玻璃模造 **Calin Tech** (Taiwan) \- 內視鏡/微型 **Young Optics** (Taiwan) \- DLP/引擎 | 非球面模造; 低自發螢光玻璃; 模組對位精度 |

#### **引用的著作**

1. Independent Temp Control Sensors PCR Thermal Cycler for Sale \- Scitek Global, 檢索日期：11月 20, 2025， [https://www.scitekglobal.com/control-sensors-pcr-thermal-cycler.html](https://www.scitekglobal.com/control-sensors-pcr-thermal-cycler.html)  
2. PCR Thermal Cyclers | Rotalab Scientific Instruments, 檢索日期：11月 20, 2025， [https://www.rotalab.com/en/products/nucleic-acid-detection-analysis-instruments/polymerase-chain-reaction-pcr-instrument.html](https://www.rotalab.com/en/products/nucleic-acid-detection-analysis-instruments/polymerase-chain-reaction-pcr-instrument.html)  
3. Fluorescence Bandpass Filters \- Edmund Optics, 檢索日期：11月 20, 2025， [https://www.edmundoptics.com/f/fluorescence-bandpass-filters/13973/](https://www.edmundoptics.com/f/fluorescence-bandpass-filters/13973/)  
4. OEM and ODM Optical Fluorescence Filters For Life Sciences ..., 檢索日期：11月 20, 2025， [https://www.global-hitronics.com/optical-fluorescence-filters-for-life-sciences\_p3.html](https://www.global-hitronics.com/optical-fluorescence-filters-for-life-sciences_p3.html)  
5. Thermoelectric Modules \- Thermoelectric, 檢索日期：11月 20, 2025， [https://www.ferrotec.com/products/thermal/modules/](https://www.ferrotec.com/products/thermal/modules/)  
6. Thermal Cycling Thermo-electric Modules | Ferrotec Corporation, 檢索日期：11月 20, 2025， [https://product.ferrotec.co.jp/en/product/electronic\_device/thermo/thermal\_cycling/](https://product.ferrotec.co.jp/en/product/electronic_device/thermo/thermal_cycling/)  
7. Cycling Thermoelectric Modules |Ferrotec-nord.com, 檢索日期：11月 20, 2025， [https://www.ferrotec-nord.com/cycling-thermoelectric-modules/](https://www.ferrotec-nord.com/cycling-thermoelectric-modules/)  
8. Thermoelectric Module Reliability, 檢索日期：11月 20, 2025， [https://thermal.ferrotec.com/technology/thermoelectric-reference-guide/thermalref10/](https://thermal.ferrotec.com/technology/thermoelectric-reference-guide/thermalref10/)  
9. Next Generation Thermoelectrics Designed for Real-Time PCR \- Electronics Cooling, 檢索日期：11月 20, 2025， [https://www.electronics-cooling.com/wp-content/uploads/2021/05/Next-gen-thermoelectrics-for-real-time-PCR-appnote-051021.pdf](https://www.electronics-cooling.com/wp-content/uploads/2021/05/Next-gen-thermoelectrics-for-real-time-PCR-appnote-051021.pdf)  
10. Modern Thermoelectrics Designed for Point of Care Testing (POCT) \- Tark Thermal Solutions, 檢索日期：11月 20, 2025， [https://tark-solutions.com/sites/default/files/ckfinder/files/resources/Application-Notes/Modern-Thermoelectrics-for-POC-testing/Modern-thermoelectrics-designed-for-point-of-care-appnote-020422.pdf](https://tark-solutions.com/sites/default/files/ckfinder/files/resources/Application-Notes/Modern-Thermoelectrics-for-POC-testing/Modern-thermoelectrics-designed-for-point-of-care-appnote-020422.pdf)  
11. Digital Temperature Controllers for Precise Thermal Management \- TE Technology, 檢索日期：11月 20, 2025， [https://tetech.com/temperature-controllers/](https://tetech.com/temperature-controllers/)  
12. Z-MAX Thermoelectric Cooler/ Device / USA UK INDIA, 檢索日期：11月 20, 2025， [https://perltier-element.de/technical/technical5.html](https://perltier-element.de/technical/technical5.html)  
13. Thermoelectric Cooling Chip \- T-Global Technology, 檢索日期：11月 20, 2025， [https://www.tglobalcorp.com/products-detail/thermoelectric-cooling-chip/](https://www.tglobalcorp.com/products-detail/thermoelectric-cooling-chip/)  
14. Enhanced Energy Harvesting from Thermoelectric Modules: Strategic Manipulation of Element Quantity and Geometry for Optimized Power Output \- MDPI, 檢索日期：11月 20, 2025， [https://www.mdpi.com/1996-1073/17/21/5453](https://www.mdpi.com/1996-1073/17/21/5453)  
15. Fabrication and Characterization of Flexible Thermoelectric Generators Using Micromachining and Electroplating Techniques \- PMC \- NIH, 檢索日期：11月 20, 2025， [https://pmc.ncbi.nlm.nih.gov/articles/PMC6843447/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6843447/)  
16. Precision Medical Machining | Pyramids Technology : OEM Medical Services, 檢索日期：11月 20, 2025， [https://www.pyramids-tw.com/msg/application-medical.html](https://www.pyramids-tw.com/msg/application-medical.html)  
17. CNC Machining for Medical Devices | INTAI Technology Corporation \- Capabilities, 檢索日期：11月 20, 2025， [https://www.intai.com.tw/en/capability/metal-process/metal-machining](https://www.intai.com.tw/en/capability/metal-process/metal-machining)  
18. Aluminium surface finishing | Precision Aluminum CNC Machining \- Han Chang, 檢索日期：11月 20, 2025， [https://www.hcintalm.com.tw/en/Capability/al-extrusion-nctprocessing.html](https://www.hcintalm.com.tw/en/Capability/al-extrusion-nctprocessing.html)  
19. TEC Modules TEC Assembly | 銀河製版印刷有限公司, 檢索日期：11月 20, 2025， [https://glxpcb.com/%E7%86%B1%E9%9B%BB/?lang=en](https://glxpcb.com/%E7%86%B1%E9%9B%BB/?lang=en)  
20. TEC | Taiwan Electronic Cooling Co.,Ltd., Heat Sink, cooler, cold plate manufacturer, thermal solution provider, 檢索日期：11月 20, 2025， [https://www.twcooling.com/about\_tec.htm](https://www.twcooling.com/about_tec.htm)  
21. High Power LEDs | High Lumen Ouptut LEDs \- Lumileds, 檢索日期：11月 20, 2025， [https://lumileds.com/products/high-power-leds/](https://lumileds.com/products/high-power-leds/)  
22. High Power, Computer-Controlled, LED-Based Light Sources for Fluorescence Imaging and Image-Guided Surgery \- PubMed Central, 檢索日期：11月 20, 2025， [https://pmc.ncbi.nlm.nih.gov/articles/PMC2766513/](https://pmc.ncbi.nlm.nih.gov/articles/PMC2766513/)  
23. Color LEDs \- ams OSRAM, 檢索日期：11月 20, 2025， [https://ams-osram.com/products/leds/color-leds](https://ams-osram.com/products/leds/color-leds)  
24. EL TOP VIEW LED \- 67-11S-C80600H-59A63DB4C52535-2T-AM \- Everlight Europe, 檢索日期：11月 20, 2025， [https://www.everlighteurope.com/custom/files/datasheets/DSE-0025263.pdf](https://www.everlighteurope.com/custom/files/datasheets/DSE-0025263.pdf)  
25. EVERLIGHT: A Leader in LED Industry, 檢索日期：11月 20, 2025， [https://en.everlight.com/](https://en.everlight.com/)  
26. EAHP3535BA0 \- Datasheet.su, 檢索日期：11月 20, 2025， [https://pdf6.datasheet.su/324.pdf](https://pdf6.datasheet.su/324.pdf)  
27. SMD High Power LED \- HPND3535CZ0112 (EU) Series, 檢索日期：11月 20, 2025， [https://www.everlight.com/wp-content/plugins/ItemRelationship/product\_files/pdf/HPND3535CZ0112%20(EU)%20Series%20Datasheet\_DHE-0004085\_V2.pdf](https://www.everlight.com/wp-content/plugins/ItemRelationship/product_files/pdf/HPND3535CZ0112%20\(EU\)%20Series%20Datasheet_DHE-0004085_V2.pdf)  
28. Lextar awarded 2022 SDIA Award for the AM Micro LED Transparent Display technology, 檢索日期：11月 20, 2025， [https://www.lextar.com/en-global/news\_center/detail/2022SDIA/?page=2](https://www.lextar.com/en-global/news_center/detail/2022SDIA/?page=2)  
29. Lextar Electronics Released Iris and Facial Double Biometric IR LEDModule, 檢索日期：11月 20, 2025， [https://www.lextar.com/en-global/news\_center/detail/20170928/2017?page=1](https://www.lextar.com/en-global/news_center/detail/20170928/2017?page=1)  
30. PC35U16 V1 KSF \- Lextar, 檢索日期：11月 20, 2025， [https://www.lextar.com/upload/media/product/lighting/LMP28300.5W/PC35U16V1KSF202302.pdf](https://www.lextar.com/upload/media/product/lighting/LMP28300.5W/PC35U16V1KSF202302.pdf)  
31. PC33U62 V0 \- Lextar, 檢索日期：11月 20, 2025， [https://www.lextar.com/upload/media/product/lighting/LMP3030EMC/PC33U62V0datasheet202303.pdf](https://www.lextar.com/upload/media/product/lighting/LMP3030EMC/PC33U62V0datasheet202303.pdf)  
32. Lextar Boosts Mini LED and Wearable Devices Applications in 2H18 \- LEDinside, 檢索日期：11月 20, 2025， [https://www.ledinside.com/news/2025/11/lextar\_boosts\_mini\_led\_and\_wearable\_device\_applications\_in2h18](https://www.ledinside.com/news/2025/11/lextar_boosts_mini_led_and_wearable_device_applications_in2h18)  
33. Lextar UVC technology helps to upgrade epidemic prevention with complete disinfection \- News Center-Lextar, 檢索日期：11月 20, 2025， [https://www.lextar.com/en-global/news\_center/detail/UVC/?page=2](https://www.lextar.com/en-global/news_center/detail/UVC/?page=2)  
34. LITE-ON TECHNOLOGY CORPORATION \- RS Online, 檢索日期：11月 20, 2025， [https://docs.rs-online.com/b688/0900766b81561fa4.pdf](https://docs.rs-online.com/b688/0900766b81561fa4.pdf)  
35. LED HIGH POWER C08 Product Series \- Liteon Opto, 檢索日期：11月 20, 2025， [https://optoelectronics.liteon.com/upload/media/light/Datasheet/LiteOn%20C08%20General%20DS\_130723.pdf](https://optoelectronics.liteon.com/upload/media/light/Datasheet/LiteOn%20C08%20General%20DS_130723.pdf)  
36. LED HIGH POWER \- CoB Product Series \- uri=media.digikey, 檢索日期：11月 20, 2025， [https://media.digikey.com/pdf/Data%20Sheets/Lite-On%20PDFs/LiteOn%20CoB%20General%20DS\_130318-2.pdf](https://media.digikey.com/pdf/Data%20Sheets/Lite-On%20PDFs/LiteOn%20CoB%20General%20DS_130318-2.pdf)  
37. Optical Filters \- Idex-hs.com, 檢索日期：11月 20, 2025， [https://www.idex-hs.com/store/products/semrock\_optical\_filters/individual\_optical\_filters/33?bandpass=Single-band%2BMultiband%2BTunable](https://www.idex-hs.com/store/products/semrock_optical_filters/individual_optical_filters/33?bandpass=Single-band%2BMultiband%2BTunable)  
38. Semrock Optical Filters Resources \- Idex-hs.com, 檢索日期：11月 20, 2025， [https://www.idex-hs.com/resources/resources-detail/semrock-optical-filters-resources](https://www.idex-hs.com/resources/resources-detail/semrock-optical-filters-resources)  
39. Filters for Polymerase Chain Reaction (PCR) \- Chroma Technology Corp, 檢索日期：11月 20, 2025， [https://www.chroma.com/applications/filters-for-pcr-applications](https://www.chroma.com/applications/filters-for-pcr-applications)  
40. The 49006 ET \- Cy5 bandpass filter set consists of excitation, emission, and dichroic filters designed for brightness and contrast. \- Chroma Technology, 檢索日期：11月 20, 2025， [https://www.chroma.com/products/sets/49006-et-cy5](https://www.chroma.com/products/sets/49006-et-cy5)  
41. PCR-global-hitronics.com, 檢索日期：11月 20, 2025， [https://www.global-hitronics.com/pcr\_n9](https://www.global-hitronics.com/pcr_n9)  
42. Optolong Optics Ltd, 檢索日期：11月 20, 2025， [https://optics.org/buyers/company/C000021092](https://optics.org/buyers/company/C000021092)  
43. Optical Filter | Fluorescence Filter | Optical Bandpass Filter, 檢索日期：11月 20, 2025， [https://optolongfilter.com/](https://optolongfilter.com/)  
44. Biomedical Filters \- 锡科光电科技有限公司, 檢索日期：11月 20, 2025， [https://shapeoptics.com/biomedical-filters/](https://shapeoptics.com/biomedical-filters/)  
45. Fluorescence Filter | \- Shape Optics, 檢索日期：11月 20, 2025， [https://sot.com.sg/fluorescence-filter/](https://sot.com.sg/fluorescence-filter/)  
46. 483nm CWL, 12.5mm Dia, 31nm Bandwidth, OD 6 Fluorescence Filter \- Edmund Optics, 檢索日期：11月 20, 2025， [https://www.edmundoptics.com/p/483nm-cwl-125mm-dia-31nm-bandwidth-od-6-fluorescence-filter/21554/](https://www.edmundoptics.com/p/483nm-cwl-125mm-dia-31nm-bandwidth-od-6-fluorescence-filter/21554/)  
47. Fluorescence Filter \- 锡科光电科技有限公司, 檢索日期：11月 20, 2025， [https://shapeoptics.com/fluorescence-filter/](https://shapeoptics.com/fluorescence-filter/)  
48. Optical Filter for Biomedical \- Products \- Auxcera, 檢索日期：11月 20, 2025， [https://en.auxcera.com/detail.php?id=185](https://en.auxcera.com/detail.php?id=185)  
49. Asia Optical Company 2025 Profile: Stock Performance & Earnings | PitchBook, 檢索日期：11月 20, 2025， [https://pitchbook.com/profiles/company/165191-14](https://pitchbook.com/profiles/company/165191-14)  
50. Asia Optical \- 亞洲光學股份有限公司, 檢索日期：11月 20, 2025， [https://www.asia-optical.com/index.php?lang=en](https://www.asia-optical.com/index.php?lang=en)  
51. Asia Optical launches medical device Pasesa, 檢索日期：11月 20, 2025， [https://www.digitimes.com/news/a20210304PR202.html](https://www.digitimes.com/news/a20210304PR202.html)  
52. About, 檢索日期：11月 20, 2025， [https://www.calin.com.tw/en/about/list/4](https://www.calin.com.tw/en/about/list/4)  
53. CALIN Technology Eliminated Weld Lines on a Projector Lens Using Moldex3D, 檢索日期：11月 20, 2025， [https://www.moldex3d.com/assets/2016/09/Customer-Success-2016-09.pdf](https://www.moldex3d.com/assets/2016/09/Customer-Success-2016-09.pdf)  
54. YGOP \- Young Optics Inc. \- Texas Instruments, 檢索日期：11月 20, 2025， [https://www.ti.com/partner/YGOP](https://www.ti.com/partner/YGOP)  
55. Optical Products \- Integrated Design and Manufacture | Young ..., 檢索日期：11月 20, 2025， [https://www.youngoptics.com/en](https://www.youngoptics.com/en)  
56. YO Endoscopic Micro-Lenses with Wide Depth of Field and Large FOV \- Young Optics, 檢索日期：11月 20, 2025， [https://www.youngoptics.com/en/top-96-product85](https://www.youngoptics.com/en/top-96-product85)  
57. Photodetectors used for positron emission tomography detectors: a... | Download Scientific Diagram \- ResearchGate, 檢索日期：11月 20, 2025， [https://www.researchgate.net/figure/Photodetectors-used-for-positron-emission-tomography-detectors-a-photomultiplier-tube\_fig1\_304811147](https://www.researchgate.net/figure/Photodetectors-used-for-positron-emission-tomography-detectors-a-photomultiplier-tube_fig1_304811147)  
58. About PMTs | Photomultiplier tubes (PMTs) \- Hamamatsu Photonics, 檢索日期：11月 20, 2025， [https://www.hamamatsu.com/eu/en/product/optical-sensors/pmt/about\_pmts.html](https://www.hamamatsu.com/eu/en/product/optical-sensors/pmt/about_pmts.html)  
59. Photodiode Arrays \- Excelitas Technologies, 檢索日期：11月 20, 2025， [https://www.excelitas.com/product-category/photodiode-arrays](https://www.excelitas.com/product-category/photodiode-arrays)  
60. Silicon PIN Photodiodes \- Excelitas, 檢索日期：11月 20, 2025， [https://www.excelitas.com/product-category/silicon-pin-photodiodes](https://www.excelitas.com/product-category/silicon-pin-photodiodes)  
61. Semiconductor Product \- TASC, 檢索日期：11月 20, 2025， [https://en.tascsemi.com/product-information/photoelectric-products/](https://en.tascsemi.com/product-information/photoelectric-products/)  
62. Sensing Devices-Photodiode \- TASC, 檢索日期：11月 20, 2025， [https://en.tascsemi.com/product-information/photoelectric-products/sensing-devices/sensing-element-photodiode/](https://en.tascsemi.com/product-information/photoelectric-products/sensing-devices/sensing-element-photodiode/)  
63. Silicon Photomultipliers (SiPM) \- onsemi, 檢索日期：11月 20, 2025， [https://www.onsemi.com/products/sensors/photodetectors-sipm-spad/silicon-photomultipliers-sipm](https://www.onsemi.com/products/sensors/photodetectors-sipm-spad/silicon-photomultipliers-sipm)  
64. MICROC-SERIES \- Silicon Photomultipliers (SiPM), Low-Noise, Blue-Sensitive \- onsemi, 檢索日期：11月 20, 2025， [https://www.onsemi.com/pdf/datasheet/microc-series-d.pdf](https://www.onsemi.com/pdf/datasheet/microc-series-d.pdf)  
65. Introduction to the Silicon Photomultiplier (SiPM) AND9770/D \- onsemi, 檢索日期：11月 20, 2025， [https://www.onsemi.com/pub/collateral/and9770-d.pdf](https://www.onsemi.com/pub/collateral/and9770-d.pdf)  
66. Photomultiplier tubes (PMTs) \- Hamamatsu Photonics, 檢索日期：11月 20, 2025， [https://www.hamamatsu.com/jp/en/product/optical-sensors/pmt.html](https://www.hamamatsu.com/jp/en/product/optical-sensors/pmt.html)  
67. Applications | MPPC (SiPMs) / SPADs \- Hamamatsu Photonics, 檢索日期：11月 20, 2025， [https://www.hamamatsu.com/jp/en/product/optical-sensors/mppc/application.html](https://www.hamamatsu.com/jp/en/product/optical-sensors/mppc/application.html)  
68. Datasheet for Sony IMX287LLR CMOS Sensor \- Vision Dimension, 檢索日期：11月 20, 2025， [https://www.vision-dimension.com/media/pdf/f2/9b/a2/The-Imaging-Source-DMK-37AUX287\_Sensor-Information-Sheet\_imx287llr\_1-0-en\_US.pdf](https://www.vision-dimension.com/media/pdf/f2/9b/a2/The-Imaging-Source-DMK-37AUX287_Sensor-Information-Sheet_imx287llr_1-0-en_US.pdf)  
69. Short-Wavelength InfraRed Image Sensor Technology SenSWIR \- Sony Semiconductor Solutions, 檢索日期：11月 20, 2025， [https://www.sony-semicon.com/en/technology/industry/senswir.html](https://www.sony-semicon.com/en/technology/industry/senswir.html)  
70. VisEra Technologies Company Limited, 檢索日期：11月 20, 2025， [https://www.viseratech.com/](https://www.viseratech.com/)  
71. CMOS image sensor with nano light pillars for optical performance enhancement, 檢索日期：11月 20, 2025， [https://www.viseratech.com/research-detail/Conference\_4/](https://www.viseratech.com/research-detail/Conference_4/)  
72. PIXART \- CODICO.com, 檢索日期：11月 20, 2025， [https://www.codico.com/en/manufacturers/pixart](https://www.codico.com/en/manufacturers/pixart)  
73. Introduction to the Latest PS5262 sensor of PixArt's CMOS Image Sensor Product Line, 檢索日期：11月 20, 2025， [https://www.youtube.com/watch?v=kHTTbJyIwYg](https://www.youtube.com/watch?v=kHTTbJyIwYg)  
74. GeSi \- Artilux, 檢索日期：11月 20, 2025， [https://www.artiluxtech.com/innovation/gesi](https://www.artiluxtech.com/innovation/gesi)  
75. Artilux Announces Groundbreaking GeSi SPAD Research Published in Nature Journal, 檢索日期：11月 20, 2025， [https://www.artiluxtech.com/resources/news/1021](https://www.artiluxtech.com/resources/news/1021)  
76. OtO Photonics \- SmartEngine (SE) Series Product sheet, 檢索日期：11月 20, 2025， [https://www.sun-ins.com/lineup5/oto/product/se/SE\_series\_EN\_206.pdf](https://www.sun-ins.com/lineup5/oto/product/se/SE_series_EN_206.pdf)  
77. SmartEngine 180-1100nm \- AP Technologies, 檢索日期：11月 20, 2025， [https://www.aptechnologies.co.uk/products/spectrometers/smartengine-180-1100nm](https://www.aptechnologies.co.uk/products/spectrometers/smartengine-180-1100nm)  
78. OTO PHOTONICS INC. \- 台灣超微光學, 檢索日期：11月 20, 2025， [https://en.otophotonics.com/](https://en.otophotonics.com/)  
79. SmartEngine Series \- 台灣超微光學, 檢索日期：11月 20, 2025， [https://en.otophotonics.com/smartengine](https://en.otophotonics.com/smartengine)  
80. TONG HSING, 檢索日期：11月 20, 2025， [https://www.theil.com/en/](https://www.theil.com/en/)  
81. CMOS Image Sensor Packagers Tong Hsing and Kingpark Merge | Maker Pro, 檢索日期：11月 20, 2025， [https://maker.pro/blog/cmos-image-sensor-packagers-tong-hsing-and-kingpark-merge](https://maker.pro/blog/cmos-image-sensor-packagers-tong-hsing-and-kingpark-merge)  
82. Chunghwa Leading Photonics Tech Ltd., 檢索日期：11月 20, 2025， [https://www.clpt.com.tw/index](https://www.clpt.com.tw/index)