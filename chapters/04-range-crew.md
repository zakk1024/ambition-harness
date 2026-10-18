# 04 · Range — 做事的隊伍（chapters/04-range-crew.md）

> 觸發：state machine 的 crew 節。原文警告（改寫）：要「像放空者那樣做事」，不要「寫得像放空者」——
> role play 敘事會洩漏；做事靠帶工具的 subagent（SOURCE-URL: https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/）。
> 生態現況是 persona 庫（SOURCE-URL: https://github.com/VoltAgent/awesome-claude-code-subagents），多數條目僅 persona 描述；本 skill 要求更進一步：三必填欄。

## range 類判定（crew 節前置問句；操作型）

「僅 range 類」依以下兩問判定，答案須記錄（可附 grep CMD 入 claim record）：

1. 驗收未固定？——任務文無逐條寫死之驗收判準／可否證 CMD（grep 問句：任務文含「驗收」「必過」「判準」等固定條款？無→是）。
2. 範圍或路徑未定？——達成手段須選型、或預期執行中增刪子目標→是。

兩問皆「是」→ range 類，入 crew 節；任一「否」→非 range 類，跳過 crew（緊 spec 任務即此，不產 subagent 定義檔）。

## 反 roleplay 四步（先於組隊）

出處：Kelley & Littman《The Art of Innovation》「Turn nouns into verbs」；考據全程見
references/worked-example.md #7 與 ledger-c。

1. **名詞**：列領域名詞（這是誰的領域？）——persona 僅到此，用於選域。
2. **動詞**：名詞→動詞：該領域的人「做」什麼？
3. **程序**：每個動作→可執行程序（用什麼工具、讀什麼資料、產什麼檔）。
4. **可否證宣稱**：每個程序→一條可否證宣稱（CMD＋預期輸出；格式同 references/claim-format.md）。

**逃逸訊號**：transcript 只有形容詞（「專業地」「像資深 X」）而無動詞／程序／宣稱＝退化回 role play，
打回四步重寫。

## 原生 subagent 定義檔（crew 輸出物；範本見 references/subagent-templates.md）

三必填，缺一不屬本 skill 之 crew：
1. **工具**：可執行工具清單（指令／MCP／腳本）。
2. **資料來源**：讀什麼——不得只憑 prompt 內建知識。
3. **驗收方式**：每項產出的可否證宣稱（CMD 式）。

## 預算與狀態（crew 護欄）

- 每層**預算欄**＋**retry budget**：無限努力＝無限燒錢＋錯誤放大（SOURCE-URL: https://www.reddit.com/r/vibecoding/comments/1wgnijd/my_opusorchestrator_sonnetsubagent_claude_code/）；
  巢狀編排最易燒爆 token（SOURCE-URL: https://dev.to/suraj_khaitan_f893c243958/i-built-100-claude-code-subagents-these-are-the-12-that-actually-earn-their-context-10nn，摘要級）。
- **artifact 共享狀態層**：產物落盤路徑寫死在定義檔——防 subagent 於長會話丟失產物狀態且謊報成功
  （SOURCE-URL: https://www.reddit.com/r/ClaudeAI/comments/1qide7x/i_built_an_orchestration_system_that_keeps_claude/，摘要級）。成功宣稱一律走章 02 judge，不信任自報。

## 無 subagent 機制 host 的退化路徑

單 thread 多段＋明確工具呼叫清單：每段＝一個三必填成員的等價物（工具呼叫逐條列出、產物落盤、段末自驗）。
表達力弱於原生定義檔（ADR-6 Consequences）；僅退化用，不得宣稱等同。
