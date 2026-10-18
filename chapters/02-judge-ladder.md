# 02 — Judge：外部裁判階梯（Depth）

載入時機：任何宣稱需要「產出者以外的某物」來驗收時。本章為 judge 機制唯一正本；宣稱記錄格式見 `references/claim-format.md`，各 host 檢查命令見 `references/judge-tools.md`，fixture 見 `tests/`。

## 四層階梯

| 層 | 手段 | 承重理由 |
|---|---|---|
| L1 | 新 context 子代理（盲審者：只看產物，不看 doer 論述） | 結構性隔離——#72206 實測同 context 自審是「回憶規則而非執行規則」；第一層的價值在新 context，非「另一個模型」 |
| L2 | host 原生檢查（測試、typecheck、build） | 機器裁判：可重跑、不可辯論 |
| L3 | 領域工具／資料回查 | 以外部資料對質宣稱，而非回憶 |
| L4 | 人類複核 | 最終採納權；高風險不可逆處不可省 |

用法：按任務類型取下表「最低足夠層」，更高層永遠可用。對照表的存在是為了防止停留在最廉的第一層（決策 6）。

### L1 退化路徑（host 無 spawn 權限時）

- 新 session、只貼產物與判準＝滿足 L1（結構性隔離仍在）。
- subagent／無 spawn 權 host：「新 session」得以同 host 新子行程替代——獨立程序、全新 context、不攜 doer 論述，僅經落盤檔案交接產物；三條件缺一即退回下行。
- 同一 context 內「假裝換人」自我複審＝不計入驗證，該宣稱記 UNVERIFIED。

### judge 全層不可用（保底）

L1–L4 皆無法執行時：相關宣稱一律記 UNVERIFIED＋三行（references/claim-format.md〈UNVERIFIED 三行模板〉），RESULT 註明缺哪幾層；資源恢復後重審。此為跨章保底（claim-format），非本章替代路徑。

## 任務類型→最低 judge 層（對照表）

| 任務類型 | 最低層 | 備註 |
|---|---|---|
| 程式碼變更 | L2 | 測試＋build 綠才算閉合；L1 不替代測試 |
| 事實宣稱 | L3 | 對質來源；無來源可查即記 UNVERIFIED |
| 文件敘事 | L1 | 新 context 盲審即足 |
| 高風險不可逆（刪檔、發布、付款） | L4 | 人類 checkpoint 不可省 |

本表可按任務增刪列；刪列須留一行刪除理由，不得靜默改表。

## 純提示詞增補

在原 context 加一句「請嚴格驗證」之類的提示詞增補，不計入驗證步驟——證據等級：單一個案（#72206），非普遍實證。方向依據：同 context 自審傾向回憶規則而非執行規則；待第二個獨立實測出現方可升級此句強度。

## Judge 通過判準

judge 判 PASS 只依據產物本身與可重跑證據：

- claim record 的 CMD 欄命令確實執行，OUT 欄留有實跑輸出，且輸出與預先固定的判準相符；
- 判準在執行前寫定（於本節規則或 claim record 內），不得事後為符合結果而改寫；
- judge 段不得引用 doer 的完成宣稱、進度敘述或自我評分——那些屬下一節，僅為 doer 側義務。

## Doer 完成條件

doer 側的「我做完了」不是驗證。doer 完成時的義務只有：交付五欄齊備的 claim record（格式見 `references/claim-format.md`），並確保 CMD 在記錄環境可重跑。doer 的完成宣稱本身永遠不構成 judge 證據。

## 宣稱記錄與 done（消耗制）

- 每宣稱一條五欄記錄；VERDICT ∈ PASS、FAIL、UNVERIFIED，禁省略、禁自創第四值。
- done＝每宣稱閉合（PASS/FAIL）或顯式 UNVERIFIED（附 QUERY/WHERE/RESULT 三行）；不設計數門檻——通過率難看是真實，灌水不是（ADR-5）。
- 對照組生成步驟若條件於受評物輸出，不得計入通過率（ADR-4）。

## 循環 reference：三成因與隔離

自生成 reference 自評全過的循環（#70231，證據等級：單一個案）三成因，逐一對應隔離手段：

1. reference 由同一 context 生成並同 context 驗證——隔離：reference 作為驗收依據前先過 L1。
2. 驗收判準由被驗物推導（循環定義）——隔離：判準先於執行固定，寫入 claim record。
3. 欄名寫錯致條目 invisible——隔離：五欄欄名逐字（見 claim-format），並以 `scripts/check_claims.py` 機驗。

## fixture 先行

任何作為 judge 的腳本／查詢，上線前先過必 FAIL 與必 PASS 兩 fixture：`tests/fixture-pass.md`（必退出碼 0）與 `tests/fixture-fail.md`（必退出碼 1）（ADR-11）。對真實數據報 FAIL 時，先重跑兩 fixture，分清「腳本 bug」或「數據洞」，再修——不得跳過歸因直接改數據或改腳本。

## 進階附註：換 provider 複核

以不同 provider 複核高風險結論——直覺級建議、無實證；不入階梯、不作驗收項。無論 provider 異同，新 context 仍是必要條件（見 L1）。
