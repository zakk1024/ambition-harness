# 01 · Altitude — 目標編譯器（chapters/01-goal-compiler.md）

> 狀態機入口。skill 第一動作＝本編譯器（ADR-2）。三件組未齊前不得開工。
> 宣稱記錄格式見 references/claim-format.md（B 維護；本檔僅引用其契約，不重寫）。

## 三件組：〈不變量＋驗證器＋環境清單〉

1. **不變量（Invariant）**：任務→結果改寫，句式「from〈任務動詞〉→ to〈可驗收的結果狀態〉」。
   樣板例：from fix crashes → to keep apps crash-free（改善百分比另計，見效度欄）。
2. **驗證器（Verifier）**：一律 CMD 式可否證——一條可重跑命令＋預期輸出。「三欄非空」存在性檢查已退役
   （決策 10／ADR-2）；描述性驗收句視同未編譯。
3. **環境清單（Environment manifest）**：驗證器賴以成立的環境前置，逐項列出。altitude 級標準前置
   （原文前提）：crash report 存取、commit↔version 對照、跨平台重現環境
   （SOURCE-URL: https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/）。

**缺項處置**：寫不出 CMD 式驗證器者降級為 task，並指名缺什麼、去哪補（哪個工具／哪份資料／誰授權）。
**不得虛構驗證器**：命令必須真實可跑；虛構欄位視同未編譯。原文根據（逐字）：
"I implore you to insist on outside validation. Ideally that's a tool the model can run to get feedback immediately."
（譯：我懇請你堅持外部驗證——理想上是一個模型能執行、立即回饋的工具。）
（SOURCE-URL: https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/）

## crash-free 解剖（三件套如何承載 altitude）

| 三件套 | 內容 | 落點 |
|---|---|---|
| 遙測 | crash report 存取權——agent 讀得到原始當機資料 | 環境清單 |
| 版本對照 | commit↔released version 對照（定位哪版引入） | 環境清單 |
| 重現艦 | 三平台重現環境（真環境複現，非憑描述推斷） | 驗證器 CMD 執行處 |

**效度欄**：altitude 宣稱須附 baseline 對照問句——"And did it work? What % fewer crashes?"（譯：有效嗎？當機少了幾％？）
（SOURCE-URL: https://news.ycombinator.com/item?id=50100345）。無 baseline 時驗證器只判狀態、不判改善；不得虛填百分比。

## 學習目標分支（B-M1／ADR-7）

流程固定先鎖困難績效目標：specific difficult 優於 do-your-best（效度 d≈.42–.80；一手文獻 L&L 2002，
SOURCE-URL: https://med.stanford.edu/content/dam/sm/s-spire/documents/PD.locke-and-latham-retrospective_Paper.pdf）。僅當判定問句為真，才改寫 learning goal：

> **判定問句**：此任務對執行者是否屬「新領域且無已驗證策略」？判定權在本問句，不在自由心證。
> **自證問句（self-check 鏡像）**：我宣稱「新領域」的證據是什麼？

改寫後須註明驗證方式，**並回爐本編譯器補齊三件組**——任何降級產物（學習目標、縮小範圍）皆同，ADR-2。
假說標記（修補 #3）：agent 在壓力下系統性偏簡目標——外插自人類文獻，假說，待 agent 實測。

## 假設審查塊（B-M4／決策 22）

編譯尾部列**至多 3 條**最可能翻車的假設，各配「最便宜的證偽動作」（一次查詢／一條命令可否證者優先）。
證據等級：敘事級（認知根據 Nickerson 1998、Lord, Lepper & Preston 1984 待取原文，
見 references/assumption-audit.md）。不作定量宣稱。上限 3 條為硬約束，防編譯期癱瘓（章 06 #9）。

## 人類 checkpoint（ADR-2；模板全文見 references/decision-checkpoints.md）

兩個不可省：①**目標確認**——三件組經人類核可才進執行；②**最終採納**——done 判定後由人類採納。
依據：outcome 全委派已被指為邀請難堪的錯誤；人類應先自答 "Work out which three decisions are most
urgent"（mjd，SOURCE-URL: https://news.ycombinator.com/item?id=50100345）。（譯：先想清楚最急的三個決定，再放手）
