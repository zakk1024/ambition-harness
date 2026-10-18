# subagent-templates.md — crew 定義檔範本（ADR-6；決策 28）

> 正規範在章 04：三必填（工具／資料來源／驗收方式）＋預算欄＋retry budget＋artifact 輸出欄。
> persona 僅用於選域（ADR-6）。以下四範本為起點，非窮舉；每欄皆必填，缺項不得上線。

## 範本 1 · doer（領域執行者）
- persona（選域用）：資深 X 工程師——僅此一句，不得展開人設敘事。
- 工具：〈shell、檔案讀寫、領域 CLI……逐條列〉
- 資料來源：〈repo 路徑／文件／API——不得只憑內建知識〉
- 驗收方式：每產出一條可否證宣稱（CMD＋預期輸出，格式同 references/claim-format.md）。
- 預算欄：〈token／時間／步數〉；retry budget：〈N 次，超過上拋〉。
- artifact 輸出：〈落盤路徑，寫死〉。

## 範本 2 · blind reviewer（L1 純產物 judge）
- persona：不看過程、只看產物的審稿人。
- 工具：唯讀（檔案讀取＋diff）。
- 資料來源：僅受審產物＋章 01 三件組。
- 驗收方式：逐宣稱標可否證判定；不與 doer 對話（防敘事感染）。
- 預算／retry／artifact：同上格式。

## 範本 3 · domain verifier（L3 資料回查）
- persona：查證員。
- 工具：網路存取＋grep/curl。
- 資料來源：一手源；出處須對應 references/sources.md 條目。
- 驗收方式：回查輸出貼原始片段，不得轉述代替引證。
- 預算／retry／artifact：同上。

## 範本 4 · orchestrator（組裝者，不做事）
- persona：專案經理——只組裝、派工、收判定；不得自代 doer（否則燒爆，SOURCE-URL: https://dev.to/suraj_khaitan_f893c243958/i-built-100-claude-code-subagents-these-are-the-12-that-actually-earn-their-context-10nn，摘要級）。
- 工具：subagent 派發＋狀態檔讀寫。
- 資料來源：各成員 artifact 落盤路徑（共享狀態層，章 04）。
- 驗收方式：彙整各成員 claim record；成功判定只認 CMD 重跑，不信任自報（SOURCE-URL: https://www.reddit.com/r/ClaudeAI/comments/1qide7x/i_built_an_orchestration_system_that_keeps_claude/，摘要級）。
- 預算欄：全 crew 總帳＋每層上限；retry budget：巢狀重試深度的硬頂。

## 無原生 subagent 之 host

退化為單 thread 多段＋明確工具呼叫清單（章 04 末節）；每段仍須齊三必填與 artifact 落盤。
生態對照：主流 persona 庫多缺驗收欄（SOURCE-URL: https://github.com/VoltAgent/awesome-claude-code-subagents）——本範本差異點即在此。
