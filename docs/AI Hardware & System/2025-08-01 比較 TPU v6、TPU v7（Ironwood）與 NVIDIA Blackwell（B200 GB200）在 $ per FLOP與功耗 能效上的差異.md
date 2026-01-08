
**比較 TPU v6、TPU v7（Ironwood）與 NVIDIA Blackwell（B200/GB200）在「$/FLOP」與「功耗/能效」上的差異**

下面分成兩部分：①能用公開資料給出的**量化近似**；②目前**無法精確量化**之處與判讀方法。所有計算都標註出處與假設。

---

# ① 能做的「量化近似」

## A. 每 PFLOP-小時成本（$/PFLOP-hr）— 粗估

> 用雲端每晶片小時價格 ÷ 理論 FP16/BF16 峰值 FLOPS 粗算（僅比較量級，不等於實際 TCO）。
> 
- **TPU v6e（Trillium）**
    - 價格（Google 官方）：1 年約 **$1.89/晶片·hr**；3 年約 **$1.22/晶片·hr**（各區域有差）。 ([Google Cloud](https://cloud.google.com/tpu?utm_source=chatgpt.com))
    - 峰值（社群/廠商說明）：「約 **2 PFLOPS FP16**/chip」層級（指標性、非官方白皮書數；僅作量級參考）。 ([HorizonIQ](https://www.horizoniq.com/blog/tpu-vs-gpu/?utm_source=chatgpt.com))
    - → **$/PFLOP-hr 粗估**：
        - 1 年價：$1.89 ÷ 2 ≈ **$0.95 / PFLOP-hr**
        - 3 年價：$1.22 ÷ 2 ≈ **$0.61 / PFLOP-hr**
- **NVIDIA B200（Blackwell）**
    - 雲價（多方彙整）：**$3.75–$18.5/ GPU·hr**（依供應商/綁約差異很大；常見中位數 ~**$6–$8/hr**）。 ([Compute Prices](https://computeprices.com/gpus/b200?utm_source=chatgpt.com))
    - 峰值：單 **B200 ≈ 5 PFLOPS**（FP16/BF16）；單 **GB200 superchip（2×B200）≈ 10 PFLOPS**。 ([NVIDIA](https://www.nvidia.com/en-us/data-center/gb200-nvl72/?utm_source=chatgpt.com))
    - → **$/PFLOP-hr 粗估**（以 $8/hr 舉例）：$8 ÷ 5 ≈ **$1.6 / PFLOP-hr**（若拿低價 $4/hr，則 ≈ **$0.8**）

> 粗結論：在「長約且穩態」前提下，TPU v6e 的 $/PFLOP-hr 常可壓到 Blackwell 的 40–80% 左右；但 Blackwell 在某些雲/型號/促銷下也能壓低到相近的區間。定價高度波動，請以你所在區域與承諾期為主核實。 (Google Cloud)
> 

---

## B. 能效/功耗（Performance per Watt）— 已公開的相對訊號

- **TPU v6e（Trillium）**：官方宣稱 **較 v5e「能源效率 +67%」**，每晶片峰值算力 **+4.7×**、HBM/ICI 同步翻倍；這是**相對前代**的明確數字。 ([Google Cloud](https://cloud.google.com/blog/products/compute/trillium-sixth-generation-tpu-is-in-preview?utm_source=chatgpt.com))
- **NVIDIA Blackwell（B200/GB200）**：
    - 官方系統級對比：**NVL72（72×GB200）對 9×HGX H100（72×H100）宣稱推理 30×吞吐、總能耗約 1.2×**（等於**吞吐/功耗~25×**級的系統優化，含 FP4、張量路徑、軟體堆疊）。 ([Medium](https://adrianco.medium.com/deep-dive-into-nvidia-blackwell-benchmarks-where-does-the-4x-training-and-30x-inference-0209f1971e71?utm_source=chatgpt.com))
    - 第三方分析：就**單 GPU TFLOPS/W**提升，**GB200 對 H100 約 +47%**，未必能直接等同於 30×推理增益（後者含資料流/精度/軟體優化等因素）。 ([SemiAnalysis](https://semianalysis.com/2024/04/10/nvidia-blackwell-perf-tco-analysis/?utm_source=chatgpt.com))

> 粗結論：
> 
> - **TPU v6e**：對自家前代的**能效大幅進步**（+67%）；
> - **Blackwell 系統**：在**系統級推理**藉由**精度（FP4/8）+軟體（TensorRT、speculative、MoE）+互連**，呈現**超線性整體提升**。單「每晶片瓦特」提升幅度沒有 30×那麼誇張，但在**整櫃/整機**上非常有競爭力。 ([Medium](https://adrianco.medium.com/deep-dive-into-nvidia-blackwell-benchmarks-where-does-the-4x-training-and-30x-inference-0209f1971e71?utm_source=chatgpt.com))

---

# ② 目前無法精確量化／該怎麼判讀

- **TPU v7（Ironwood）**：Google 已在 2025 宣布第 7 代 TPU **主攻推理**、號稱「**最強與最節能**」但**尚未公開標準化 FLOPS 與功耗數字**（至少對外資料仍偏宣示層級）。能效/價格要等廣泛 GA 與定價後才能算出「$/PFLOP-hr」。 ([blog.google](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/?utm_source=chatgpt.com))
- *TPU v6e 的「2 PFLOPS/chip」**屬社群/廠商簡化估值，非 Google 白皮書；但用於「量級比較」足夠。若你要嚴格核算，需以**實測吞吐（tokens/s 或 step/s）**換算「$/token」或「Wh/token」。 ([HorizonIQ](https://www.horizoniq.com/blog/tpu-vs-gpu/?utm_source=chatgpt.com))
- **Blackwell $/FLOP**受地區、綁約、供應緊張、是否含 CPU/RAM/網路在同一 SKU 等影響極大；**$3.75–$18.5/hr**都有人報，必須**以你實際供應商報價為準**。 ([Compute Prices](https://computeprices.com/gpus/b200?utm_source=chatgpt.com))

---

# 實務建議：如何用「同一把尺」比

1. **統一精度**：用 **FP8 / BF16** 兩種常用精度各算一遍（FP4 只適合特定推理）。
2. **用「$/token」與「Wh/token」雙指標**：跑同一模型（例如 Llama-3/70B 或你自家模型）、同長度、同批次，量測**吞吐**→算「$/token」；讀取電錶或廠商功耗計**實測功耗**→算「Wh/token」。
3. **算「$/step」與「Wh/step」**（訓練）：固定 batch/global batch、seq_len、optimizer 設定，量測每秒 step，反推每一步訓練成本與能耗。
4. **把雲費率固化**：用你實際簽到的 1y/3y 價格，不要用官網標價；Blackwell 變動特別大。
5. **把軟體堆疊固定**：
    - Blackwell：**TensorRT-LLM、FP8、Eagle-3 speculative、MoE** 等最佳化開/關要一致。 ([Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/dgx-b200-blackwell-node-sets-world-record-breaking-over-1-000-tps-user?utm_source=chatgpt.com))
    - TPU：**XLA 穩定編譯、shape 綁定/有界動態、vLLM on TPU（推理）**等要按最佳實踐設定。 ([Google Cloud](https://cloud.google.com/blog/products/compute/trillium-sixth-generation-tpu-is-in-preview?utm_source=chatgpt.com))

---

## 總結

- **今天能量化的**：TPU v6e 在**$/PFLOP-hr 粗估**上常優於 Blackwell；對自家前代**能效 +67%**。Blackwell 在**系統級推理**靠低精度與軟體堆疊能達到**極高的吞吐/功耗比**。 ([Google Cloud](https://cloud.google.com/blog/products/compute/trillium-sixth-generation-tpu-is-in-preview?utm_source=chatgpt.com))
- **尚無法量化的**：**TPU v7（Ironwood）**的精確 FLOPS 與功耗尚未公開，需等 Google 釋出白皮書/定價或第三方大規模測試。 ([blog.google](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/?utm_source=chatgpt.com))

