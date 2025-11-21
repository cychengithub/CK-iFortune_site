# **雙引擎資料中心：Google整合TPU與NVIDIA GPU策略深度解析**

## **第一節：Google信條：一種系統級的AI基礎設施方法**

要理解Google在人工智慧硬體領域的策略，僅僅孤立地分析其張量處理單元（Tensor Processing Unit, TPU）是遠遠不夠的。其真正的核心競爭力源於一種深度整合的系統級方法，其中客製化晶片僅是一個更大、協同設計生態系統中的一環，該生態系統涵蓋了實體資料中心、網路架構和軟體調度。這種垂直整合的模式構成了Google最難以被複製的競爭優勢。

### **1.1 基礎：硬體與其棲息地的協同設計**

Google的獨特優勢在於其資料中心的設計與其客製化硬體開發同步進行。這種協同作用創造了競爭對手難以企及的效率。這種從基礎設施到晶片的整體設計理念，使其能夠在規模化部署中實現顯著的成本和效能優勢。

這種協同設計理念最顯著的體現是Google在散熱技術上的領先地位。早在Nvidia等競爭對手大規模推廣其液冷解決方案（如GB200）之前，Google就已經部署了數百萬個液冷TPU，總功耗超過1吉瓦（GW）。這使其在高密度運算熱管理方面取得了巨大的先發優勢。這種先進的液冷基礎設施，不僅僅是為了散熱，更是其整體能源效率策略的基石。它使得Google的資料中心在一年中的大部分時間裡無需依賴耗能巨大的冷水機組運行，從而在2023年實現了1.1的卓越電源使用效率（Power Usage Effectiveness, PUE）。

這個數字背後隱藏著巨大的戰略經濟價值。PUE為1.1意味著每輸送1瓦電力給晶片，僅需額外消耗約15%的電力用於散熱和設施運營。相比之下，微軟等競爭對手在相同條件下的設施開銷可能高達45%以上。在動輒數百兆瓦（MW）的AI叢集中，這種效率差異轉化為巨大的營運成本節省。當這種基礎設施效率與專為高「每瓦效能」（performance-per-watt）設計的TPU相結合時，運行大規模、持續性AI工作負載（如Google搜尋或Gemini模型推理）的總體擁有成本（Total Cost of Ownership, TCO）將遠低於那些在效率較低的第三方資料中心部署現成GPU的競爭者。這種TCO優勢不僅僅是一個環保指標，它是一種強大的經濟武器，讓Google能夠以更低的成本基礎來訓練更大的模型和提供推理服務，從而構築了一道不僅僅是晶片架構，而是整體基礎設施工程的護城河。這正是Google「AI基礎設施霸權」的精髓所在。新一代的TPU，如Ironwood，也延續了這一理念，採用了Google的第三代液冷基礎設施，顯示出對此協同設計哲學的長期、迭代承諾。

### **1.2 混合現實：調度異構加速器**

Google的資料中心並非僅由TPU構成，而是同時運行著龐大的NVIDIA GPU叢集。問題的關鍵在於Google如何管理這個包含自有客製化晶片和第三方硬體的「雙引擎」環境。答案在於其先進的營運層，它使得這種混合模式對內部和外部客戶都變得可行且高效。

Google Cloud平台明確地向客戶提供TPU和一系列廣泛的NVIDIA GPU選項，包括L4、H100、A100以及即將推出的Blackwell系統。這並非一個「非此即彼」的選擇，而是一種組合策略。為了有效管理這些高需求且數量有限的資源，Google開發了**動態工作負載排程器（Dynamic Workload Scheduler, DWS）**，它超越了傳統的「先到先得」資源分配模型。

DWS提供了兩種關鍵模式來應對不同的需求：

1. **日曆模式（Calendar mode）**：適用於需要高可預測性的工作負載，允許用戶提前預訂長達90天的共置GPU和TPU容量，類似於預訂機票或酒店。
2. **彈性啟動模式（Flex Start mode）**：適用於更具機會主義性質的短期作業（最長7天），用戶提交容量請求後，系統會在資源可用時自動配置並運行作業。

這個排程平台深度整合到Google Cloud的核心服務中，如Compute Engine、Google Kubernetes Engine (GKE)和Vertex AI，為管理兩種加速器類型提供了統一的介面。GKE進一步將硬體抽象化，允許用戶為不同的加速器類型（TPU或GPU）定義節點池，甚至可以創建**自訂運算類別（Custom Compute Classes）**，定義基於優先級的回退機制。例如，系統可以設定優先在TPU v6e Spot實例上排程作業，如果失敗或無可用資源，則自動回退到L4 GPU節點池。

這種使GPU和TPU在程式設計層面具備可替代性（fungibility）的系統，不僅僅是為客戶提供便利，它本身就是一個強大的戰略工具。透過DWS和GKE實現的營運抽象化，Google能夠優化其龐大的內部硬體資產。當全球H100 GPU供應短缺時，內部團隊和精明的客戶可以將工作負載轉移到TPU上。當新一代TPU在特定工作負載上（例如v5e的推理）展現出卓越的性價比時，DWS可以優先分配這些資源。這在Google內部創造了一個動態的資源市場，有效對沖了NVIDIA的定價能力和供應鏈波動風險。這種無縫轉換工作負載的能力，成為了Google在與供應商談判時的有力籌碼，也是最大化其數十億美元硬體投資回報的關鍵機制。它將一個異構的硬體環境從管理上的複雜性轉變為一項戰略性資產。

### **1.3 軟體抽象層：OpenXLA，通用翻譯器**

在彌合高階機器學習框架與TPU、GPU等不同硬體架構之間的鴻溝方面，軟體扮演了至關重要的角色。OpenXLA專案正是Google混合策略得以超越其內部生態系統、走向成功的關鍵。

在技術層面，所有在TPU上運行的程式碼都必須經過XLA（Accelerated Linear Algebra）編譯器進行編譯。然而，XLA的影響力遠不止於此。它已經發展成為一個名為OpenXLA的開源編譯器專案，由包括Google、NVIDIA、AWS、Meta和Intel在內的行業領導者共同協作開發。OpenXLA的核心功能是接收來自PyTorch、JAX和TensorFlow等主流框架的模型，並將其優化以在不同的硬體後端（包括GPU、CPU和TPU）上高效執行。

這並非僅停留在理論層面。Google和NVIDIA已明確合作，將Google自家的大型模型框架PaxML（最初為TPU slice設計）進行優化，使其能夠利用經過OpenXLA編譯器優化的JAX，在NVIDIA H100和A100 GPU上運行。同樣，PyTorch/XLA套件是開發者在TPU上運行PyTorch模型的關鍵，它明確利用了OpenXLA，使得開發者只需少量程式碼修改即可完成遷移。

NVIDIA最大的優勢並非其硬體本身，而是其擁有17年歷史、創造了強大「鎖定效應」的CUDA軟體生態系統。使用CUDA編寫程式碼的開發者實質上被綁定在NVIDIA的硬體上。Google要從頭複製一個如此龐大的生態系統是不切實際的。因此，Google透過OpenXLA採取了另一種策略：將抽象層向上移動。透過推廣一個介於框架（PyTorch、JAX）和硬體之間的編譯器，Google試圖將硬體後端商品化。如果開發者使用JAX或PyTorch編寫的模型可以透過XLA高效地編譯到TPU、GPU或其他加速器上，那麼底層硬體的選擇就變成了一個基於性價比的部署決策，而非一個根本性的開發依賴。這直接挑戰了CUDA的鎖定效應。與NVIDIA在PaxML上的合作可謂是神來之筆：它不僅驗證了XLA作為一個嚴肅的、生產級的GPU工作負載工具，同時也為以GPU為中心的開發者最終遷移到TPU鋪平了道路，因為他們使用的框架和編譯器是相同的。

## **第二節：架構對比：TPU ASIC與GPU通用處理器**

本節將深入探討TPU和GPU在基礎架構理念上的技術差異。從核心運算單元到記憶體和網路子系統，我們將剖析每種加速器在不同領域表現出色的根本原因。

### **2.1 核心運算哲學：脈動陣列 vs. SIMT平行處理**

兩種加速器的效能特徵源於其核心處理單元的根本性差異。

**TPU**是一種專為特定應用設計的積體電路（Application-Specific Integrated Circuit, ASIC），其本質是一個為神經網路工作負載量身打造的「矩陣處理器」。**其核心是矩陣乘法單元（Matrix Multiply Unit, MXU），這是一個由128x128或256x256個乘法累加器組成的脈動陣列（systolic array）**。這種設計極其擅長處理深度學習中佔主導地位的大量低精度（如BF16、INT8）運算。脈動陣列架構的關鍵優勢在於，它可以在執行矩陣乘法期間將中間結果直接傳遞給下一個處理單元，從而最大限度地減少了對記憶體的存取，而記憶體存取恰恰是通用處理器中的一個主要瓶頸。

**GPU**則是一種通用目的的平行處理器，擁有數千個更小、更靈活的核心（如CUDA核心），並在單指令多執行緒（Single Instruction, Multiple Threads, SIMT）模型下運作。儘管現代GPU也配備了類似於小型MXU的專用張量核心（Tensor Cores），但其整體架構仍然保持了更高的靈活性，能夠處理圖形渲染、科學計算以及更不規則的計算模式。單個NVIDIA H100 GPU就擁有超過100個獨立的串流多處理器（Streaming Multiprocessors, SMs），使其非常適合同時運行數百個獨立的任務。

這兩種設計理念的背後，是一個根本性的權衡：**靈活性與效率的取捨**。Google將TPU設計為ASIC，犧牲了通用計算的靈活性，以換取在一個狹窄任務領域（張量運算）的極致效率。這也解釋了為何TPU不適合處理具有頻繁分支或大量逐元素運算的程式。相比之下，從圖形處理演變而來的GPU保留了其靈活性，使其成為「瑞士軍刀」，而TPU則是專注的「手術刀」。這一基礎設計選擇產生了連鎖效應：TPU在執行AI任務時更節能，因為它沒有支援其他功能的開銷。然而，GPU則受益於更廣泛的總體潛在市場（遊戲、高效能運算等），這為其龐大的研發投入提供了資金，從而也促進了其在AI領域的能力。

### **2.2 記憶體與互連子系統：ICI/環面網路 vs. NVLink/胖樹網路**

在大規模AI運算中，資料的儲存、存取和晶片間通訊往往是主要的效能瓶頸。TPU和GPU在此採用了截然不同的解決方案。

在**記憶體**方面，兩種架構都依賴高頻寬記憶體（High-Bandwidth Memory, HBM）。然而，在世代演進中，它們的設計出現了分歧。NVIDIA B200配備了192GB的HBM3e，頻寬高達8 TB/s 。Google Ironwood TPU同樣配備了192GB的HBM3e，頻寬為7.3 TB/s 。關鍵的區別在於Pod層級的設計：Ironwood透過光路交換機（Optical Circuit Switches, OCS）在其包含9,216個晶片的整個Pod中，創建了一個高達1.77 PB的、可直接定址的巨大共享記憶體池。這在NVIDIA的架構中並無直接對應的設計。

在**互連**技術上，Google採用了自訂的晶片間互連（Inter-Chip Interconnect, ICI）。從TPUv4開始，ICI被組織成一個三維環面（3D Torus）拓撲，將每個晶片與其六個最近的鄰居直接相連。這種拓撲結構具有成本效益，並為通訊提供了出色的局部性。NVIDIA則使用NVLink技術實現伺服器內部GPU之間的高速通訊（例如Blackwell上的第五代NVLink達到1.8 TB/s），並透過InfiniBand或乙太網，採用Clos網路或胖樹（fat-tree）網路拓撲來連接不同的伺服器。Google的TPUv4超級電腦利用自訂的光路交換機（OCS）來動態地重新配置3D環面網路，據稱這比大型InfiniBand GPU叢集所需的多層電氣交換更便宜、更節能、更可靠。

網路拓撲的選擇不僅僅是技術決策，它深刻地反映了兩家公司的核心商業模式和主要使用情境。Google最初為TPU設定的主要「客戶」是其自身，用於運行如搜尋排名和模型訓練等大規模、模式固定的工作負載。對於這類大型、同步、資料平行的作業，通訊模式（主要是近鄰通訊）是可預測的，因此3D環面網路極為高效。它最大限度地減少了昂貴的長距離佈線和交換設備，從而降低了整個超級電腦的建置成本。相比之下，NVIDIA的產品銷售給成千上萬的客戶，他們的工作負載千差萬別且不可預測。胖樹/Clos網路雖然因需要更多交換機而成本更高，但它能為叢集中任意兩個節點之間提供更均勻、無阻塞的頻寬。這更適合通用目的的超級計算，因為無法預測哪些節點之間需要通訊。因此，Google的網路是為其自有的規模化AI工廠進行了優化，而NVIDIA的網路則是為通用目的的AI基礎設施進行了優化。

### **2.3 效能、功耗與成本效益：量化比較**

本節將綜合各項研究中的效能指標，提供一個清晰、由數據驅動的比較，並透過下方的詳細表格進行支撐。

- **每瓦效能（Performance-per-Watt）**：這是TPU的一個關鍵優勢。第一代TPU在TOPS/Watt指標上就比同時代的GPU高出30至80倍。TPUv4的每瓦效能比TPUv3提升了2.7倍，而Ironwood更是將Trillium的每瓦效能翻了一倍。基準測試顯示，在達到相似效能時，TPUv4的功耗比A100低1.3至1.9倍。高階GPU的功耗可達700W至1000W（如B200），而TPU通常在175W至250W的範圍內。
- **每元效能（Performance-per-Dollar）**：對於雲端客戶而言，這項指標至關重要。Cloud TPU v5e在推理任務上的每元吞吐量效能比TPUv4高出2.5倍。Trillium在訓練任務上的每元效能比v5p高出2.5倍。Google自己的推理基準測試顯示，其系統（包括GPU和TPU）的效能比同類公有雲產品高出2至4倍，成本效益則高出2倍以上。
- **可擴展性（Scalability）**：TPU從設計之初就考慮了大規模Pod的擴展。TPUv4可擴展至4,096個晶片，v5p可擴展至8,960個晶片，而Ironwood更是達到了9,216個晶片。透過ICI實現的這種緊密集成，通常被認為在處理超大型訓練作業時，比使用外部網路擴展GPU叢集更具可預測性且更易於管理。

為了提供一個全面的視圖，下表整合了Google TPU與NVIDIA GPU各代產品的關鍵硬體規格。

| **特性** | **TPU v4** | **TPU v5p** | **Trillium (v6e)** | **Ironwood** | **NVIDIA A100** | **NVIDIA H100** | **NVIDIA B200** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **架構** | Custom | Custom | Custom | Custom | Ampere | Hopper | Blackwell |
| **製程** | 7 nm | N/A | N/A | N/A | TSMC 7N | TSMC 4N | TSMC 4N |
| **峰值運算 (BF16/FP16)** | 275 TFLOPS | 459 TFLOPS | ~926 TFLOPS | N/A | 312 TFLOPS | 1000 TFLOPS | 4.5 PFLOPS |
| **峰值運算 (FP8/INT8)** | 275 TOPS | 918 TOPS | ~1847 TOPS | 42.5 ExaFLOPS (Pod) | 624 TOPS | 2000 TOPS | 9 PFLOPS |
| **峰值運算 (FP4)** | N/A | N/A | N/A | N/A | N/A | N/A | 18 PFLOPS |
| **HBM 容量** | 32 GB | 95 GB | 32 GB | 192 GB | 80 GB | 80 GB | 192 GB |
| **HBM 頻寬** | 1.2 TB/s | 2.76 TB/s | ~1.6 TB/s | 7.3 TB/s | 2 TB/s | 3 TB/s | 8 TB/s |
| **互連技術** | ICI (3D Torus) | ICI (3D Torus) | ICI | ICI (OCS) | NVLink3 | NVLink4 | NVLink5 |
| **互連頻寬 (單晶片)** | 600 GB/s (雙向) | 1200 GB/s (雙向) | 800 GB/s (雙向) | 1.2 Tbps | 600 GB/s | 900 GB/s | 1.8 TB/s |
| **最大擴展規模** | 4,096 晶片 | 8,960 晶片 | 100,000+ 晶片 | **9,216 晶片** | N/A | 256 GPUs | 576 GPUs |
| **功耗 (TDP)** | 170-192 W | N/A | N/A | N/A | 400 W | 700 W | 1000 W |

*資料來源:*

## **第三節：戰略演算：TPU生態系統的優劣勢分析**

本節將從技術層面轉向戰略層面，分析Google決定自行研發AI晶片所帶來的商業影響。內容將涵蓋其內部效益、外部挑戰，以及與NVIDIA之間複雜的競爭與合作關係。

### **3.1 垂直整合的優勢：Google為何要打造TPU**

從Google的角度來看，TPU專案背後有多重核心動機。

首先是**成本控制與戰略獨立**。最直接的好處是減少對「昂貴的NVIDIA晶片」的依賴，避免支付所謂的「NVIDIA稅」。擁有TPU使Google在與NVIDIA的價格談判中掌握了更多籌碼。

其次是**為核心工作負載進行客製化**。Google開發TPU是為了滿足其自身龐大服務（如搜尋、相簿、翻譯和Gemini）對AI計算效率的特定需求。他們可以在晶片中加入專用硬體，例如用於加速推薦模型的SparseCores。這類模型對Google的業務至關重要，但對於一個通用GPU供應商來說，可能並非最高優先級。

最後是**供應鏈的掌控**。透過自行設計晶片（與Broadcom合作，由台積電製造），Google對其供應鏈擁有了更大的控制權，從而在NVIDIA晶片供應緊張的市場競爭中獲得了一定的緩衝。

TPU專案既是防禦性的，也是進攻性的。在防禦層面，它保護了Google核心業務的利潤率。如果Google所有服務的加速器都必須從NVIDIA購買，其銷售成本（COGS）將會大幅上升，從而影響盈利能力。這使其相較於完全依賴第三方硬體的競爭對手，擁有結構性的成本優勢。在進攻層面，Google Cloud可以利用其TCO優勢，以極具競爭力的價格提供TPU資源，從而吸引像Anthropic、Apple、Midjourney這樣的大規模AI客戶，與主要基於NVIDIA的AWS和Azure展開競爭。TPU因此成為Google Cloud的一個關鍵差異化因素。

### **3.2 護城河與孤島：生態系統的局限性**

儘管TPU帶來了諸多優勢，但其生態系統也面臨著顯著的障礙和劣勢。

最主要的劣勢在於軟體。NVIDIA的CUDA平台是業界標準，擁有17年的歷史、500萬開發者，並支援超過4000個應用程式，形成了堅固的護城河。開發者普遍偏愛GPU，因為它們具有更廣泛的實用性和更穩健的軟體支援。

此外，TPU主要針對TensorFlow和JAX進行了優化。雖然透過PyTorch/XLA也支援PyTorch，但其原生性不足，這導致了更陡峭的學習曲線，並且在設定上可能「頗為棘手」。

從歷史上看，TPU僅能透過Google Cloud Platform (GCP)使用，這造成了供應商鎖定。這與GPU形成了鮮明對比，後者不僅在各大雲端服務商均有提供，還可用於本地部署。

下表從質化角度總結了Google TPU與NVIDIA CUDA生態系統之間的差異，突顯了開發者和企業在做出選擇時需要權衡的因素。

| **方面** | **NVIDIA CUDA 生態系統** | **Google TPU 生態系統** |
| --- | --- | --- |
| **主要框架** | 廣泛支援所有主流框架 (PyTorch, TensorFlow, JAX等)，以CUDA為底層核心。 | 主要針對TensorFlow和JAX進行深度優化，透過PyTorch/XLA支援PyTorch。 |
| **硬體可用性** | 廣泛可用，涵蓋所有主要雲端平台、本地部署伺服器及個人工作站。 | 主要透過Google Cloud Platform提供，近期開始嘗試部署於第三方雲端服務商。 |
| **開發者社群與資源** | 極其龐大且成熟，擁有17年歷史，資源、論壇、文件極為豐富。 | 較小，主要圍繞Google的生態系統，資源集中在官方文件和支援管道。 |
| **應用廣度** | 通用目的，除AI外，還廣泛應用於圖形渲染、科學計算、遊戲等領域。 | 專用目的（ASIC），專為神經網路工作負載設計，不適合通用計算。 |
| **可移植性/供應商鎖定** | 高可移植性，可在不同雲端和本地環境之間遷移。 | 歷史上存在較強的GCP平台鎖定，OpenXLA旨在改善此狀況。 |
| **易用性/學習曲線** | 由於生態成熟和工具豐富，上手相對容易，已成為行業標準。 | 學習曲線較陡峭，特別是對於非TensorFlow/JAX用戶，需要適應XLA編譯流程。 |

*資料來源:*

### **3.3 雲端上的亦敵亦友：Google與NVIDIA的共生與競爭**

Google與NVIDIA之間的關係極其複雜，既是緊密的合作夥伴，又是直接的競爭對手。

一方面，Google是NVIDIA最大的客戶之一，大量採購GPU用於Google Cloud平台。事實上，Google的許多自有產品也是在NVIDIA GPU上建構和運行的。兩家公司最近還擴大了合作夥伴關係，Google在其雲平台上提供最新的NVIDIA硬體（H100、DGX GH200、Blackwell），並且，極具指標性意義的是，Google已將其自家的PaxML框架優化以支援NVIDIA GPU ，這是對GPU市場主導地位的務實承認。

另一方面，Google正積極地試圖削弱NVIDIA的市場地位。它正在接觸那些嚴重依賴NVIDIA的小型雲端服務供應商（CSP），如Fluidstack、Crusoe和CoreWeave，並提供激勵措施，鼓勵它們在其資料中心部署TPU。Google甚至向Fluidstack提供了高達32億美元的財務擔保。這無疑是對NVIDIA主要銷售通路的一次直接挑戰。

這種看似矛盾的行為（深度合作的同時激烈競爭）實質上是Google為降低其AI未來風險而採取的一種複雜的雙軌策略。合作陣線是其對NVIDIA當前市場主導地位的務實應對。為了在當今的雲端AI市場中競爭，Google**必須**提供一流的NVIDIA GPU，並確保其軟體能在上面良好運行。這是一個中短期的營收策略。而競爭陣線則是一個長期的戰略佈局。Google深刻認識到單一供應商壟斷關鍵技術的巨大風險。透過在市場上（甚至在競爭對手的資料中心裡）扶植一個可行的替代方案（TPU），它的目標是創造一個多極化的AI硬體世界。這將促進價格競爭，確保供應多樣性，並防止CUDA成為不可動搖的永久性標準。Google願意投入數十億美元（如32億美元的擔保）來建立這個替代生態系統，因為從長遠來看，一個完全由NVIDIA壟斷的市場，其戰略成本將會更高。

## **第四節：下一代產品：從Trillium的訓練能力到Ironwood的推理焦點**

本節將分析TPU架構的演進，並深入探討最新的Ironwood晶片。分析將指出，Ironwood代表了一次重大的戰略轉向，從以往主要關注訓練加速，轉向在規模化推理領域確立主導地位。

### **4.1 追溯傳承：通往Exascale訓練之路**

在深入探討最新一代產品之前，有必要簡要回顧其演進歷程，以提供必要的背景。

- **TPUv4**：確立了現代化的Pod架構，可在3D環面網路中擴展至4,096個晶片，提供1.1 exaflops的峰值運算能力。它引入了用於推薦模型的SparseCores和用於可重構網路的OCS 。
- **TPU v5p**：專注於進一步擴大規模，Pod規模擴大到8,960個晶片，每個晶片的峰值運算能力達到459 TFLOPS。它改進了3D環面架構，並提升了記憶體容量（95GB HBM）和頻寬（2.76 TB/s）。
- **Trillium (TPU v6e)**：實現了單晶片峰值運算能力相較於v5e高達4.7倍的巨大飛躍，同時HBM容量和ICI頻寬也翻了一倍。它在訓練效能和能源效率方面取得了顯著進步。

從TPUv4到Trillium的演進，清晰地展示了一個連貫的戰略目標：為訓練日益龐大的基礎模型，建構更大、更快、更高效的系統。每一代產品都在晶片數量、運算密度和互連頻寬上有所提升，這些都是降低大規模訓練運行時間和成本的關鍵變數。這是Google為了跟上模型規模指數級增長而採取的必然步驟。

### **4.2 Ironwood的轉向：為推理時代而設計**

本節的核心是基於Hot Chips 2025發布會的內容，對Ironwood TPU進行深入分析。

Ironwood的設計標誌著一次戰略性的轉變。它被明確定義為Google**第一款**專為大規模AI推理而設計的TPU，目標是大型語言模型（LLM）、專家混合（Mixture-of-Experts）模型和推理模型。這與前幾代更側重於訓練的設計理念截然不同。

其架構上的創新體現了這一點：

- **大規模擴展性與共享記憶體**：SuperPod可擴展至9,216個晶片。最突出的特點是透過光路交換機在整個Pod中實現了高達1.77 PB的可直接定址HBM共享記憶體。這是一個創紀錄的共享記憶體容量，對於儲存龐大推理模型的狀態至關重要。
- **架構創新**：Ironwood是Google首款多運算晶粒（multi-compute chiplet）設計。它配備了第四代SparseCore，並重新聚焦於記憶體子系統，每個晶片搭載8組HBM3e（總容量192GB，頻寬7.3 TB/s）。
- **功耗效率與穩定性**：Google宣稱其每瓦效能是Trillium的2倍，是TPUv4的近6倍。此外，它還包含了平滑功耗波動的功能，以減輕資料中心電網的負擔——這對於規模化部署至關重要。
- **可靠性、可用性、可服務性（RAS）**：Ironwood高度重視RAS特性，包括內建自檢、靜默資料損壞檢測，甚至為了備援而額外配置了機架（9216個晶片而非2的冪次方8192個），以確保系統能夠長時間無故障運行。

「推理時代」的經濟現實與訓練時代截然不同。訓練一個模型是一項巨大但一次性（或不頻繁）的資本支出。而推理則是一項與用戶互動量成正比的、24/7不間斷的營運支出。要在這個新時代取勝，最重要的指標不僅僅是峰值效能，更是每瓦效能和每元效能，即總體擁有成本（TCO）。Ironwood的所有特性都指向優化這個TCO公式。巨大的共享記憶體減少了昂貴的資料移動；極致的功耗效率直接降低了電費；先進的RAS特性則最大限度地減少了停機時間，因為在生產服務中，停機即意味著收入損失。Google的賭注是，透過建構一個超專用、大規模可擴展且極致高效的推理引擎，它能以遠低於通用硬體（如GPU）的成本，為其自有產品（Gemini、搜尋）和雲端客戶提供服務。Ironwood是Google為應對AI領域漫長而艱鉅的營運成本之戰而打造的武器。

### **4.3 競爭前景：Ironwood vs. Blackwell**

本節將Ironwood置於與NVIDIA最新產品的競爭背景中進行分析。

NVIDIA的Blackwell (B200)架構是一個通用目的的AI巨獸。它採用雙晶粒設計，擁有2080億個電晶體，配備192GB的HBM3e（8 TB/s頻寬），功耗高達1000W 。它引入了如FP4等新的低精度格式，將8-GPU系統的推理效能提升至144 petaFLOPS（稀疏）。它透過第五代NVLink（1.8 TB/s）和InfiniBand擴展至大規模叢集。

相比之下，Ironwood在一個9,216晶片的Pod中提供42.5 Exaflops（FP8）的運算能力，功耗為10MW 。

這反映了兩種截然不同的哲學。Blackwell是NVIDIA打造最強大、最靈活AI晶片的策略，旨在應對從訓練到推理、從初創公司到超大規模資料中心的任何工作負載。而Ironwood則是Google的策略，即建構一個超專用的系統，以無與倫比的TCO效率專注於一件事——大規模推理。

Ironwood與Blackwell之間的比較揭示了AI硬體市場潛在的兩極分化。NVIDIA憑藉其廣泛的客戶基礎，正在打造終極的「商業晶片」——一個單一、強大的架構（Blackwell），可以為任何AI任務服務。而Google，以其主要的內部客戶和對大規模雲端部署的關注，則押注於專業化。其背後的假設是，對於那些最終將在運算量上佔據市場主導地位的、最大規模、最成熟的AI應用，專用ASIC（Ironwood）在TCO上將永遠勝過通用GPU。這是一個典型的技術市場動態。Google賭的是AI的未來更像是智慧型手機SoC那樣專業化、高批量的世界；而NVIDIA賭的則是它更像x86 CPU那樣通用化的世界。最終的贏家將取決於未來大多數AI運算週期是用於少數幾種大規模推理任務，還是用於種類繁多、不斷變化的訓練和推理工作負載。

## **第五節：結論：異構AI運算的未來**

本節將綜合報告的各項發現，並對Google、NVIDIA以及更廣泛的AI產業的戰略影響提出前瞻性觀點。

### **5.1 發現綜述**

本報告的核心論點可以總結如下：Google的實力根植於其系統級的垂直整合方法。TPU與GPU的共存部署是透過複雜的軟體層（GKE、DWS、XLA）進行管理的，這種管理將異構性轉化為一項戰略資產。TPU架構以犧牲靈活性為代價換取極致效率，這反映了Google自身的主要使用情境。與NVIDIA之間「亦敵亦友」的關係是一種精心計算的策略，旨在應對當前的市場現實，同時為一個風險更低的未來進行佈局。而向Ironwood的演進，標誌著一次重大的戰略轉向，旨在贏得即將到來的、圍繞推理TCO的經濟戰。

### **5.2 戰略展望與建議**

**第三方TPU的博弈**：Google近期將TPU部署到如Fluidstack等外部資料中心的舉動，是其迄今為止最具侵略性的策略。如果成功，它可能開始為NVIDIA主導的生態系統創造一個真正的、多雲的替代方案。然而，這一策略面臨著CUDA護城河的巨大阻力。其成功將在很大程度上取決於OpenXLA編譯器堆疊的成熟度和效能。

**未來是混合的**：本分析強烈表明，大規模AI運算的未來並非贏家通吃的局面，而是一個異構的環境。工作負載將根據其特定需求（延遲、吞吐量、精度）以及底層硬體的即時成本和可用性，在不同類型的加速器之間進行動態排程。那些能夠建構出最佳調度與軟體抽象層（如Google的DWS和OpenXLA）的公司，將擁有顯著的競爭優勢。

**結論性思考**：Google的雙引擎策略是一項長期的、耗資數十億美元的賭注。它賭的是，在AI革命的成熟階段，以盡可能低的TCO運行大規模、專業化工作負載的經濟性，將最終戰勝通用硬體的靈活性。Ironwood與Blackwell之間的競爭，不僅僅是兩款晶片之間的較量，更是兩種對計算未來截然不同願景的碰撞。

### **引用的著作**

1. Multi-Datacenter Training: OpenAI's Ambitious Plan To Beat Google's Infrastructure, https://semianalysis.com/2024/09/04/multi-datacenter-training-openais/ 2. Energy-Efficient GPU vs. TPU Allocation - Artech Digital, https://www.artech-digital.com/blog/energy-efficient-gpu-vs-tpu-allocation 3. GPU and TPU Comparative Analysis Report | by ByteBridge - Medium, https://bytebridge.medium.com/gpu-and-tpu-comparative-analysis-report-a5268e4f0d2a 4. Google AI Infrastructure Supremacy: Systems Matter More Than ..., https://semianalysis.com/2023/04/12/google-ai-infrastructure-supremacy/ 5. Google Ironwood TPU Swings for Reasoning Model Leadership at ..., https://www.servethehome.com/google-ironwood-tpu-swings-for-reasoning-model-leadership-at-hot-chips-2025/ 6. Google Cloud and NVIDIA Expand Partnership to Advance AI ..., https://nvidianews.nvidia.com/news/google-cloud-and-nvidia-expand-partnership-to-advance-ai-computing-software-and-services 7. Performance per dollar of GPUs and TPUs for AI inference | Google ..., https://cloud.google.com/blog/products/compute/performance-per-dollar-of-gpus-and-tpus-for-ai-inference 8. GPU machine types | Compute Engine Documentation - Google Cloud, https://cloud.google.com/compute/docs/gpus 9. GPU-Accelerated Google Cloud Platform - NVIDIA, https://www.nvidia.com/en-us/data-center/gpu-cloud-computing/google-cloud-platform/ 10. NVIDIA and Google Cloud bring Generative AI to enterprises, https://cloud.google.com/blog/products/ai-machine-learning/nvidia-and-google-cloud-bring-generative-ai-to-enterprises 11. Understanding Google Cloud's Dynamic Workload Scheduler | by Maciej Strzelczyk, https://medium.com/google-cloud/understanding-google-clouds-dynamic-workload-scheduler-fa181624ab6a 12. Dynamic Workload Scheduler Calendar mode reserves GPUs and TPUs - Google Cloud, https://cloud.google.com/blog/products/compute/dynamic-workload-scheduler-calendar-mode-reserves-gpus-and-tpus 13. Introducing Dynamic Workload Scheduler | Google Cloud Blog, https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler 14. Tensor Processing Units (TPUs) - Google Cloud, https://cloud.google.com/tpu 15. Improve Resource Obtainability (GPUs, TPUs) with Dynamic Workload Scheduler on GCP, https://www.youtube.com/watch?v=1D04EhhDvhg 16. About TPUs in GKE | Google Kubernetes Engine (GKE), https://cloud.google.com/kubernetes-engine/docs/concepts/tpus 17. vLLM GPU/TPU Fungibility - GKE AI Labs, https://gke-ai-labs.dev/docs/tutorials/gpu-tpu/fungibility-recipes/ 18. How to Set Up a GPU-Enabled Kubernetes Cluster on GKE for AI & ML Workloads - vCluster, https://www.vcluster.com/blog/gcp-gke-gpu-cluster 19. Introduction to Cloud TPU | Google Cloud, https://cloud.google.com/tpu/docs/intro-to-tpu 20. OpenXLA Project, https://openxla.org/ 21. OpenXLA Dev Lab 2024: Building Groundbreaking ML Systems Together, https://opensource.googleblog.com/2024/05/openxla-dev-lab-2024-building-grouundbreaking-systems-together.html 22. PyTorch/XLA 2.6 helps improve AI model performance | Google Cloud Blog, https://cloud.google.com/blog/products/application-development/pytorch-xla-2-6-helps-improve-ai-model-performance 23. Google challenges NVIDIA with TPU expansion to cloud providers, https://www.chosun.com/english/industry-en/2025/09/05/ANA3P7MYNNEELH5CLI5VKGSOQU/ 24. [D] Why does it seem like Google's TPU isn't a threat to nVidia's GPU? - Reddit, https://www.reddit.com/r/MachineLearning/comments/1g1okem/d_why_does_it_seem_like_googles_tpu_isnt_a_threat/ 25. TPU vs GPU: Pros and Cons | OpenMetal IaaS, https://openmetal.io/docs/product-guides/private-cloud/tpu-vs-gpu-pros-and-cons/ 26. Tensor Processing Unit - Wikipedia, https://en.wikipedia.org/wiki/Tensor_Processing_Unit 27. TPU architecture | Google Cloud, https://cloud.google.com/tpu/docs/system-architecture-tpu-vm 28. Training Large-Scale Recommendation Models with TPUs - Snap Inc., https://eng.snap.com/training-models-with-tpus 29. TPU vs GPU: What's the Difference in 2025? - CloudOptimo, https://www.cloudoptimo.com/blog/tpu-vs-gpu-what-is-the-difference-in-2025/ 30. How to Think About GPUs | How To Scale Your Model - GitHub Pages, https://jax-ml.github.io/scaling-book/gpus/ 31. TPU vs GPU: Choosing the Right Hardware for Your AI Projects | DigitalOcean, https://www.digitalocean.com/resources/articles/tpu-vs-gpu 32. TPU vs. GPU: Differences Explained - phoenixNAP, https://phoenixnap.com/kb/tpu-vs-gpu 33. Understanding TPUs vs GPUs in AI: A Comprehensive Guide - DataCamp, https://www.datacamp.com/blog/tpu-vs-gpu-ai 34. TPUs vs. GPUs: What's the Difference? - Pure Storage Blog, https://blog.purestorage.com/purely-educational/tpus-vs-gpus-whats-the-difference/ 35. NVIDIA Blackwell B200 GPU – Technical Analysis - Server Simply, https://www.serversimply.com/blog/technical-analysis-of-the-blackwell-b200 36. NVIDIA Tensor Core GPUs Comparison - NVIDIA B200 vs B100 vs H200 vs H100 vs A100 [ Updated ] - Bizon-tech, https://bizon-tech.com/blog/nvidia-b200-b100-h200-h100-a100-comparison 37. TPU v4 - Google Cloud, https://cloud.google.com/tpu/docs/v4 38. Resiliency at Scale: Managing Google's TPUv4 Machine Learning Supercomputer - USENIX, https://www.usenix.org/system/files/nsdi24-zu.pdf 39. All About the NVIDIA Blackwell GPUs: Architecture, Features, Chip Specs - Hyperstack, https://www.hyperstack.cloud/blog/thought-leadership/everything-you-need-to-know-about-the-nvidia-blackwell-gpus 40. Accelerating the deployment of TPU, competition between Google and NVIDIA in the AI chip sector intensifies. - Moomoo, https://www.moomoo.com/news/post/57992678/accelerating-the-deployment-of-tpu-competition-between-google-and-nvidia 41. Quantifying the performance of the TPU, our first machine learning chip | Google Cloud Blog, https://cloud.google.com/blog/products/gcp/quantifying-the-performance-of-the-tpu-our-first-machine-learning-chip 42. TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings - arXiv, http://arxiv.org/pdf/2304.01433 43. Google TPU V4 : Specifications, Architecture, Working, Differences & Its Applications, https://www.elprocus.com/google-tpu-v4/ 44. Trillium TPU is GA | Google Cloud Blog, https://cloud.google.com/blog/products/compute/trillium-tpu-is-ga 45. TPU v5p - Google Cloud, https://cloud.google.com/tpu/docs/v5p 46. [D] Google just released a new generation of TPUs. Who actually uses TPUs in production?, https://www.reddit.com/r/MachineLearning/comments/1k0fg57/d_google_just_released_a_new_generation_of_tpus/ 47. AI Hypercomputer TPUs - TPU options | Google Cloud Skills Boost, https://www.cloudskillsboost.google/paths/2806/course_templates/1405/documents/568755 48. Announcing Trillium, the sixth generation of Google Cloud TPU : r/mlscaling - Reddit, https://www.reddit.com/r/mlscaling/comments/1csigfy/announcing_trillium_the_sixth_generation_of/ 49. NVIDIA H100 Tensor Core GPU Datasheet - Megware, https://www.megware.com/fileadmin/user_upload/LandingPage%20NVIDIA/nvidia-h100-datasheet.pdf 50. H100 white paper - Jingchao's Website, https://jingchaozhang.github.io/H100-white-paper/ 51. NVIDIA DGX B200 - PNY Technologies, https://www.pny.com/en-eu/nvidia/dgx/b200 52. NVIDIA's Blackwell architecture: breaking down the B100, B200, and GB200, https://www.cudocompute.com/blog/nvidias-blackwell-architecture-breaking-down-the-b100-b200-and-gb200 53. [News] Google Reportedly Courts Smaller CSPs to Host TPUs, Taking Aim at NVIDIA, https://www.trendforce.com/news/2025/09/04/news-google-reportedly-courts-smaller-csps-to-host-tpus-taking-aim-at-nvidia/ 54. TPU vs GPU: What's the real difference? - Telnyx, https://telnyx.com/learn-ai/tpu-vs-gpu 55. TPU vs GPU: Which AI Hardware Should You Choose? - HorizonIQ, https://www.horizoniq.com/blog/tpu-vs-gpu/ 56. TPU vs GPU in AI: A Comprehensive Guide to Their Roles and Impact on Artificial Intelligence - Wevolver, https://www.wevolver.com/article/tpu-vs-gpu-in-ai-a-comprehensive-guide-to-their-roles-and-impact-on-artificial-intelligence

好的，很樂意以我身為 Google AI 專家的角度，為您深入解析這個問題。

要理解 TPU 的精髓，我們不能僅僅比較規格表上的數字。這關乎於一個根本性的設計哲學差異：我們在 Google 打造 TPU，並非想製造一個更快的 GPU，而是要為大規模、高效率的機器學習，從根本上重新思考運算架構。

### TPU 的核心工作原理：為矩陣而生的脈動陣列

GPU 的核心是一種通用平行處理器，它擁有數千個靈活的 CUDA 核心，採用「單指令多執行緒」（SIMT）模型運作，使其像一把瑞士軍刀，能處理圖形、科學計算和 AI 等多樣化任務 [1, 2]。

相比之下，TPU 是一種專用積體電路（ASIC），其心臟是**脈動陣列（Systolic Array）**，也就是我們的**矩陣乘法單元（Matrix Multiply Unit, MXU）** [2, 3]。您可以將它想像成一個為神經網路中無處不在的矩陣乘法運算量身打造的「工廠產線」[4]。

它的工作原理極其高效 [3, 5]：

1. 資料（權重和啟動值）像心跳的脈搏一樣，有節奏地流入這個由成千上萬個微小處理元件（PE）組成的網格中。
2. 每個 PE 執行一個簡單的乘法累加運算，然後立即將中間結果傳遞給相鄰的下一個 PE，無需將資料寫回主記憶體 [3, 6]。
3. 這種設計最大限度地減少了對記憶體的存取，而記憶體存取恰恰是通用處理器中最耗時、最耗能的瓶頸之一 [3, 6]。

正是這種專一的設計，犧牲了通用性，換來了在 AI 核心任務上無與倫比的效率 [2]。

### TPU v5p 與 Trillium (v6) 的設計優點

基於脈動陣列的核心，我們在 v5p 和 Trillium 上建構了幾個關鍵的系統級優勢：

1. **為極致擴展而生的網路架構**：我們從一開始就將 TPU 設計為一個龐大的、協同工作的整體。我們使用自訂的**晶片間互連（Inter-Chip Interconnect, ICI）** 將數千個晶片組織成一個**三維環面（3D Torus）**網路拓撲 [7, 8, 9]。這意味著每個晶片都與其鄰居有直接、高速的連接。對於大規模、同步的 AI 訓練任務（這類任務的通訊模式是可預測的），這種架構比 GPU 叢集常用的、更昂貴且複雜的胖樹（Fat-Tree）網路更具成本效益和效率 [10, 11, 12]。
    - **TPU v5p**：可將多達 8,960 個晶片連接成一個 Pod，每個晶片的 ICI 頻寬高達 4,800 Gbps [7, 8]。
    - **Trillium (v6e)**：在此基礎上，將 ICI 頻寬和高頻寬記憶體（HBM）的容量與頻寬都**翻了一倍**，並能將多達 256 個晶片組成一個 Pod，再透過我們的 Jupiter 資料中心網路擴展至數百個 Pod，連接數萬個晶片 [13, 14, 15]。
2. **無與倫比的每瓦效能與每元效能**：這是我們最引以為傲的優勢。由於 TPU 的 ASIC 設計只專注於 AI 運算，沒有通用 GPU 的額外開銷，因此能源效率極高 [16, 2]。
    - **TPU v5p**：在訓練大型語言模型時，其速度比上一代 v4 快 2.8 倍 [8]。
    - **Trillium (v6e)**：實現了巨大的飛躍，單晶片峰值運算效能是 v5e 的 **4.7 倍**，能源效率提升了 67% [13, 14, 15]。這直接轉化為更低的訓練成本和更快的模型迭代速度。
3. **專用硬體加速**：我們能夠在晶片中整合針對特定 AI 任務的專用硬體。例如，Trillium 搭載了第三代 **SparseCore**，專門用於加速處理在推薦系統和搜尋等業務中至關重要、但 GPU 難以高效處理的超大規模嵌入模型 [13, 14]。

### 與 NVIDIA H100 及 B200 的比較

將 TPU 與 NVIDIA 的頂級 GPU 進行比較，更能凸顯我們設計理念的差異。

| **特性** | **Google TPU v5p** | **Google Trillium (v6e)** | **NVIDIA H100** | **NVIDIA B200** |
| --- | --- | --- | --- | --- |
| **核心架構** | 專用 ASIC (脈動陣列) | 專用 ASIC (脈動陣列) | 通用 GPU (SIMT) | 通用 GPU (SIMT) |
| **峰值運算 (BF16/FP16)** | 459 TFLOPS [7] | ~926 TFLOPS [14] | 1,000 TFLOPS [17] | 4.5 PFLOPS (4,500 TFLOPS) [18] |
| **HBM 容量 (單晶片)** | 95 GB [7] | 32 GB [14] | 80 GB [17] | 192 GB [18] |
| **HBM 頻寬 (單晶片)** | 2.76 TB/s [7] | ~3.2 TB/s (v5e 的 2 倍) [14] | 3 TB/s [17] | 8 TB/s [18] |
| **晶片間互連** | ICI (3D Torus) [7] | ICI (3D Torus) [13] | NVLink (胖樹網路) [9] | NVLink 5 (胖樹網路) [18] |
| **最大擴展規模** | 8,960 晶片 (Pod) [8] | 數萬晶片 (多 Pod) [14] | 256 GPUs (NVLink Switch) [17] | 576 GPUs [19] |

**分析與解讀：**

- **原始效能 vs. 系統效率**：從單晶片峰值運算來看，NVIDIA Blackwell B200 的數字確實驚人 [18, 19]。然而，AI 的戰場不僅僅是單晶片的競賽，更是大規模叢集的系統工程。在最新的 MLPerf 訓練基準測試中，NVIDIA 的系統在縮短訓練時間方面依然領先 [20]。但我們的 TPU v5p 在 GPT-3 訓練任務中展現了近乎完美的線性擴展效率（約 99.9%），從 512 個晶片擴展到 6144 個晶片時效能幾乎沒有損耗 [21]。這證明了我們 3D Torus 網路架構在超大規模同步訓練中的優越性。
- **通用性 vs. 專用性**：NVIDIA 的成功在於其強大的 CUDA 生態系統和 GPU 的通用性，這為開發者提供了極大的靈活性 [22]。而我們的策略是透過 **OpenXLA** 編譯器，在 PyTorch、JAX 和 TensorFlow 等主流框架與底層硬體之間建立一個抽象層 [13, 23]。這使得開發者可以專注於模型開發，而將硬體選擇變成一個基於成本和效率的部署決策，從而挑戰 CUDA 的鎖定效應。
- **成本是最終的護城河**：對於雲端客戶和我們自己的大規模服務（如搜尋、Gemini）而言，總體擁有成本（TCO）至關重要。TPU 在每元效能上持續領先 [8, 15, 24]。一個 8 晶片的 TPU v5e 叢集在 Llama2-70B 上能達到可觀的吞吐量，而其每小時的成本可能僅為同等規模 H100 叢集的十分之一 [25]。這才是 TPU 真正的戰略優勢。

**總結來說**，NVIDIA H100 和 B200 是極其強大的通用 AI 加速器，在原始效能和生態系統方面處於領先地位。然而，Google TPU v5p 和 Trillium 代表了另一條演化路徑：透過軟硬體協同設計，為特定但至關重要的 AI 工作負載，提供無可比擬的系統級擴展性、能源效率和成本效益。這場競賽的未來，將不僅僅取決於誰的晶片最快，更取決於誰能為 AI 的規模化應用提供最經濟、最高效的整體解決方案。