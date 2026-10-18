# prompt-compiler.md — ADR-2 提示語庫（第一動作＝章 01）

> 邏輯在章 01；本檔只放可複製骨架。宣稱記錄格式引用 references/claim-format.md（B 維護），此處不重定義。

## 骨架 P0 · 目標編譯

    不變量：from <任務動詞> → to <可驗收結果狀態>
    驗證器 CMD：<一條可重跑命令> ＋ 預期輸出 <…>（描述性驗收句不合格——決策 10）
    環境清單：<逐項；含 crash report／版本對照／重現環境等存取前提>
    缺項：<缺什麼｜去哪補：工具／文件／誰授權>

## 骨架 P1 · 學習目標分支（僅判定問句為真時）

    判定問句：此任務對執行者是否新領域且無已驗證策略？（證據：<…>）
    改寫：learning goal＝<可驗證的習得標準＋驗證方式>
    回爐：重過 P0 三件組（降級產物同）

## 骨架 P2 · 假設審查塊（≤3 條，敘事級）

    假設 N：<一句話>｜最便宜證偽：<一次查詢／一條命令>

## 骨架 CP · 人類 checkpoint（兩枚，模板見 decision-checkpoints.md）

    CP-1 目標確認：呈三件組＋缺項＋假設塊 → 人類核可才開工
    CP-2 最終採納：呈 judge 結論＋claim 摘要＋殘留風險 → 人類採納

## 語氣慣用法（掛點備忘）

- within-goal 期望：明確告知「此題可行、有成功先例」——依據 L&L 轉引 Locke, Motowidlo & Bobko 1986
  （SOURCE-URL: https://med.stanford.edu/content/dam/sm/s-spire/documents/PD.locke-and-latham-retrospective_Paper.pdf；轉引，未取原文）。佐證敘事錨：Dantzig（不知難而力戰）——references/exemplars.md 例 4。
- 執行敘事用意象＋判準＋信任（references/inner-game-voice.md）；驗收句一律鷹架格式。
