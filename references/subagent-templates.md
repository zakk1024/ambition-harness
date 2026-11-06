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
- 工具：唯讀＋shell——讀檔、grep、重跑受審件的驗證腳本；不得寫入受審檔（無 shell 的唯讀 reviewer 只能複述，無法重跑證據）。
- 資料來源：僅受審產物＋章 01 三件組。
- 驗收方式：逐宣稱標可否證判定；不與 doer 對話（防敘事感染）。
- 預算／retry／artifact：同上格式。
- 派工 brief 必含條款（缺一條即 brief 不合格）：
  - 寫入白名單：只准新增一個報告檔（絕對路徑寫死），不得改任何既有檔；發現錯誤寫進報告、不動手修——受審件在審查中被改，判定與產物就對不上。
  - 證據自跑：每個結論附子代理自己跑出的命令與原始輸出；「已完成／全綠／PASS n/n」等 doer 字樣不得單獨充當證據。
  - 可重跑性：每條 finding 附 file:line 與陌生人可直接貼進 shell 的命令（不得依賴其 cwd、不得含未展開的 $VAR、不得留全形標點）。
  - 驗證器自跑：要求它親自跑受審件的驗證腳本，貼原始輸出與 exit code。
  - 回報格式：VERDICT 先行，findings 分 HIGH/MED/LOW/NIT；最終訊息只回 verdict、逐項 PASS/FAIL、統計與報告路徑，不貼全文。
  - 上層再核：子代理回報同屬自述——轉述給人類前，上層自己重跑關鍵驗證器並核對它報的數字。
  - 落檔補救：子代理若在寫報告前撞步數／call 上限，父代理把它最終訊息中的逐字判定謄入指定報告檔（不改內容、不補話），再自行重跑每一項——判定不得只留在通知訊息裡。

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

## 範本 5 · council chair（秘書制——子代理互相隔離、無即時討論通道時的收斂席）
- council 形態：N 席 blind reviewer 平行（各只讀受審產物，落盤己見前不得讀他席；平行缺席＝正常，勿等待）＋本席收斂。
- persona：只裁決、不發明的整合者。
- 工具：檔案讀寫＋grep 自檢。
- 資料來源：全部盲評產物＋原始受審件；禁新增無來源事實——新事實須帶來源，否則標 [待驗]。
- 驗收方式：逐衝突裁決留痕（引雙方原句→resolution：採X／合成／defer+理由）；末節附機器自檢輸出（如 `grep -c` 計數實測）。
- artifact：單一整合檔，路徑寫死；預算／retry 同上格式。

## 無原生 subagent 之 host

退化為單 thread 多段＋明確工具呼叫清單（章 04 末節）；每段仍須齊三必填與 artifact 落盤。
生態對照：主流 persona 庫多缺驗收欄（SOURCE-URL: https://github.com/VoltAgent/awesome-claude-code-subagents）——本範本差異點即在此。
