---
name: ambition-harness
description: Use when an open-ended task should be raised from task-level to outcome-level, when results must be verified by
  something other than the model that produced them, or when a crew of tool-bearing subagents is needed. Compiles the request
  into <invariant + falsifiable verifier + environment manifest>, runs an outside-judge ladder with per-claim verdicts, and
  makes subagents do the work rather than role-play it. Skip for tight specs with fixed acceptance criteria, trivial tasks,
  or crunch situations - adding harder goals there only adds risk.
argument-hint: "[outcome or task] [--quick] [--no-crew] [--judge=ctx-agent|tests|domain|human]"
---

## When to load / When to skip

- 載入：開放範圍任務、無既定判準；結果必須由非產出者驗證；需要多面具工具的 subagent crew。
- 跳過：緊 spec 已有固定驗收（照單執行即可）；瑣碎任務；crunch／時限壓力——此時加碼目標只添風險，且「承諾於時限壓力下崩塌」為假說（待 agent 實測），非實證。
- 本檔僅觸發樣態、Fast path、狀態機常駐 context；其餘一律按狀態機節點載入（ADR-1/ADR-12）。

## Fast path（三分鐘版）

1. 第一動作＝目標編譯器，把請求譯成三件組（詳 chapters/01-goal-compiler.md）：
  - 不變量：outcome 而非 task（例：fix crashes → keep apps crash-free）；
  - 驗證器：CMD 式可否證（命令＋預期輸出），不得以描述文字充數、不得自行虛構驗證器；缺項指名缺什麼、去哪補；
  - 環境清單：遙測存取／版本對照／重現環境。
2. 任何降級產物（含學習目標）亦必回爐本編譯器（ADR-2/ADR-7）。
3. judge 最低層＝新 context 子代理盲審：只看產物、不看 doer 論述。承重原文：
  > "I implore you to insist on outside validation. Ideally that's a tool the model can run to get feedback immediately."
  > （譯：我懇請你堅持外部驗證——理想上是一個模型能執行、立即回饋的工具。——Felix Rieseberg, How to be more ambitious；research/ledger-a.md 已核條目）
4. 兩個人類 checkpoint 不可省：目標確認、最終採納（references/decision-checkpoints.md）。代理條款：doer 為 subagent／無人類在環時，checkpoint 得由指派鏈上層（指派者）代簽，並於 claim record 註明代簽者；無人可代簽者記 UNVERIFIED＋三行（QUERY／WHERE／RESULT），不得靜默視為已核。
5. 旗標僅三（O-1）：`--quick` 降級路徑（免完整流程，驗證器欄仍強制）；`--no-crew` 跳過 crew 節；`--judge=ctx-agent|tests|domain|human` 指定 judge 層。組合規則：三旗標任意並用皆合法。`--quick`×`--judge=`：--quick 僅縮減流程節點，不降級 --judge 指定層——指定層於存留節點照常執行，無法執行時相關宣稱記 UNVERIFIED＋三行；任何組合下驗證器欄（CMD 式）皆強制。`--no-crew` 用於非 range 任務＝無作用（no-op），非錯誤。

## The state machine

流程：編譯 → 假設審查 → 執行 → judge → 失敗？協定 → done 判定 → crew（僅 range 類）。任一節失效先查 chapters/06-failure-modes.md。

| 節點 | 規則（錨點） | 按節點載入 |
|---|---|---|
| 編譯 | 三件組；先鎖困難目標，僅「新領域且無已驗策略」問句為真才改學習目標（ADR-7） | chapters/01-goal-compiler.md；references/goal-setting-rules.md、references/prompt-compiler.md |
| 假設審查 | ≤3 假設、各配最便宜證偽；全文敘事級證據 | chapters/01-goal-compiler.md；references/assumption-audit.md |
| 執行語氣 | ADR-10 分層：流程／驗收層用鷹架，執行敘事層留白；步驟層數上限可設定（預設 5，經驗值） | chapters/03-execution-voice.md；references/inner-game-voice.md |
| 案例支援 | 按體裁檢索 1–2 例；先例效應是燃料不是方法；無驗證欄不得入庫 | chapters/05-evidence-cases.md；references/exemplars.md、references/story-calibration.md |
| judge | 四層階梯；任務類型→最低層對照表；judge 通過判準與 doer 完成條件分離段落（O-2）；fixture 先行（ADR-11）；盲審派工 brief 硬條款見 references/subagent-templates.md 範本 2 | chapters/02-judge-ladder.md；references/claim-format.md、references/judge-tools.md、references/worked-example.md |
| 失敗？協定 | 歸因重訓＋微成功子步驟，兩者缺一不可；子步驟規模可設定（預設 15 分鐘等效，經驗值；ADR-8） | chapters/03-execution-voice.md；references/self-efficacy-sources.md |
| done 判定 | 消耗制：每宣稱閉合（PASS/FAIL）或顯式 UNVERIFIED＋三行查無記錄；無數量門檻（ADR-5） | scripts/check_claims.py；references/claim-format.md |
| 報進度 | 狀態與下一步一律從台帳／驗證器現況重推（ckpt status、gate 輸出、檔案 mtime、exit code），不從對話摘要、前次宣稱或 doer 自報轉述——摘要是改寫，不是證據；下一步須指名仍未閉合的宣稱 | — |
| 人類 checkpoint | 兩枚不可省：①目標確認（編譯後、執行前）②最終採納（done 後）；subagent 依代理條款（Fast path 4） | references/decision-checkpoints.md |
| crew | 僅 range 類：subagent 定義檔三必填（工具／資料／驗收）＋預算、retry、artifact 共享層；反 roleplay 四步——「don't write like a short seller, do what a short seller does」（譯：別寫得像做空者，要做事像做空者。——Rieseberg；research/ledger-a.md 已核條目） | chapters/04-range-crew.md；references/subagent-templates.md |
| 引文紀律 | 一切 SOURCE-URL 須可回溯正典；引言須原文＋中譯＋出處齊備 | references/sources.md |

### 修復輪紀律（品質結果制）

收斂判準＝最終品質（全部實證閉合），非流程完成；修復輪次無上限。

- 每輪修復後全套重驅：selftest＋歷史 case 全回歸，數字逐位核對——任何變動須能指出成因，否則按回歸處理。
- 浮動 fail 判定式：單檔恆綠＋全套炸顆每輪不同、百 ms 級快速失敗＝並行高載時序敏感，非產品缺陷。先單檔重跑釘排產品因素，再放寬非同步輪詢/等待預算、調降 test runner 併發；產品碼不動——把雜音補丁寫進產品碼即是固化雜音。
- 宣稱「穩定綠」的收斂門檻＝連續兩輪全套全綠；存在浮動 fail 時，單輪綠不構成穩定證據。
- UNVERIFIED 根治＝產出真貨（最小實測資料／fixture）使其可驗，非改寫宣稱；真貨須標明定位（如 fixture 校準不入績效序列）。
- 修復出處以 `judge#N` 標記寫入 claim record 逐輪可追溯；涉契約／語義／結構之重大改動，修後須再盲審，小幅修復重驅即閉。
- fixture 欄位必須符合被測程式的輸入契約——先手算期望輸出再信 PASS：契約錯位的寬鬆匹配會靜默假陽性。
- 單元直呼內層函式≠路徑已測：改 dispatch／映射後，造經公開 CLI 的最小 E2E fixture 實測該路徑。
- 殘留掃描用寬鬆 pattern：修掉舊數字／舊字串後先 `grep -n '<數字或詞根>'` 掃全檔，逐行分類命中（真宣稱 vs 單位字樣如 AES256、位元組數），再以可重現集合重算該數字；窄 pattern（`'56 個 video id'`）會漏掉同數字的其他措辭。
- 收斂檔（closure）不算證據：每一列須附「改檔後重跑」的 CMD 與逐字輸出；「兩處都已改」這類自述曾與事實不符。

## Self-check

- Q 每個目標是否已編譯為〈不變量＋CMD 式驗證器＋環境清單〉三件組，驗證器為可否證命令而非描述文字？
- Q 每個 judge 通過判準是否寫在獨立段落、未引用 doer 完成宣稱，且對照表已指派最低層？
- Q 每條宣稱是否已有五欄記錄、VERDICT 三值之一（不得以 partial 充數），且 done 時無未閉合條目？
- Q 失敗後是否已同時完成歸因重訓與一個服務原目標且可驗證的微成功子步驟（兩者缺一不可）？
- Q 每個 subagent 定義檔是否齊備工具、資料來源、驗收方式三必填，並設預算欄與 artifact 共享狀態層？
- Q 每個引用案例是否具三件組、效度、三值判定欄，傳說級者附校準註記？
- Q 修復輪是否全套重驅、歷史數字逐位核對，且每處變動均有成因解釋？
- Q 修掉舊字串後是否以寬鬆 pattern 掃全檔、逐行分類命中，並以可重現集合重算該數字？
