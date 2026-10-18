# 06 · 失效模式（chapters/06-failure-modes.md）

每節三段：現象—實測出處—對沖回鏈（回鏈指章 01–05 錨點）。judge 機制本體在章 02（B 維護）；
此處只收失效與回鏈。

## 1. 假成功
現象：agent 自報完成，而產物不成立或狀態丟失（"falsely reported success"；譯：謊報成功。）。
實測出處：長會話 subagents 丟失 artifact 狀態（SOURCE-URL: https://www.reddit.com/r/ClaudeAI/comments/1qide7x/i_built_an_orchestration_system_that_keeps_claude/；摘要級）。
對沖回鏈：章 04 artifact 共享狀態層；章 02 judge——不信任自報，CMD 重跑。

## 2. 測試湊綠
現象：越有企圖心越不照計畫，"just makes up random stuff to get the tests to pass"（UncleEntity；譯：隨手編造來讓測試變綠。）。
實測出處：SOURCE-URL: https://news.ycombinator.com/item?id=50100345。單一評論，證據等級：個案。
對沖回鏈：章 02 judge 階梯——驗證器獨立於被優化目標；章 01 驗證器 CMD 式可否證。

## 3. 決策黑箱
現象：關鍵決策全委派、人類未看資料，事後才發現漏掉急迫決定。
實測出處：mjd 於 SOURCE-URL: https://news.ycombinator.com/item?id=50100345（三急迫決定句，逐字見章 01）。
對沖回鏈：章 01 人類 checkpoint 兩枚（目標確認、最終採納），不可省。

## 4. token 失控
現象：巢狀編排與無限重試燒爆預算。
實測出處：SOURCE-URL: https://dev.to/suraj_khaitan_f893c243958/i-built-100-claude-code-subagents-these-are-the-12-that-actually-earn-their-context-10nn（深層巢狀實測，摘要級）；SOURCE-URL: https://www.reddit.com/r/vibecoding/comments/1wgnijd/my_opusorchestrator_sonnetsubagent_claude_code/（重試須上限）。
對沖回鏈：章 04 每層預算欄＋retry budget。

## 5. roleplay 逃逸
現象：transcript 只剩形容詞；persona 描述被當成能力。
實測出處：SOURCE-URL: https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/（role play 洩漏警告）；SOURCE-URL: https://github.com/VoltAgent/awesome-claude-code-subagents（生態多為純 persona 條目）。
對沖回鏈：章 04 反 roleplay 四步＋逃逸訊號＋三必填欄。

## 6. 範例庫腐化
現象：案例缺效度欄；傳說細節訛傳照抄；體裁錯配引用。
實測出處：Dantzig 流傳版出入之考據（references/story-calibration.md；ledger-c）。
對沖回鏈：章 05 使用規則 3／5；references/exemplars.md 五欄位契約與校準註記。

## 7. 目標通膨
現象：把野心寫成修辭；宣稱缺效度基線（百分比、改善幅度憑空填寫）。
實測出處：maxcb 效度追問（SOURCE-URL: https://news.ycombinator.com/item?id=50100345）；L&L——非 specific difficult 即退化
（SOURCE-URL: https://med.stanford.edu/content/dam/sm/s-spire/documents/PD.locke-and-latham-retrospective_Paper.pdf）。
對沖回鏈：章 01 三件組＋效度欄 baseline 問句。

## 8. 降級成癮
現象：反覆降級以迴避困難；降級產物未驗證即採用、未回爐。
實測出處：低效能者視困難為威脅而迴避（敘事級；references/self-efficacy-sources.md；Bandura 摘要級）。
對沖回鏈：章 03 防範問句三連；降級產物回爐章 01。

## 9. M4 過度審查
現象：假設審查無限膨脹，編譯期癱瘓，遲遲不開工。
實測出處：機制本身無實證紀錄；證據等級敘事級（references/assumption-audit.md）。
對沖回鏈：章 01 假設審查塊硬上限 3 條、各配最便宜證偽動作。
