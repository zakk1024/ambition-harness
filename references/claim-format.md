# claim-format — 宣稱記錄五欄契約（全庫格式正本）

本檔為全庫格式契約：各章引用本檔欄名與退出碼語意，不得改寫（X2 接縫規則）。機器驗收：`scripts/check_claims.py`——其退出碼數值語意由該腳本 docstring 自定義，本檔不重述數值。

## 記錄形態

每條宣稱＝一個以 `CLAIM:` 開頭的連續列區塊，欄位各佔一行、`KEY: value` 形態。五欄欄名逐字，禁自創同義欄（欄名寫錯＝條目 invisible，#70231 教訓，證據等級：單一個案）：

| CLAIM | CMD | OUT | VERDICT | SOURCE-URL（URL 或 n/a） |
|---|---|---|---|---|
| 一句可否證宣稱，先於驗證固定 | 可重跑命令 | CMD 實跑輸出關鍵行，勿轉述 | PASS、FAIL、UNVERIFIED 三值之一，禁省略 | 證據來源，須能在 `references/sources.md` 找到對應條目 |

## 值規則

- VERDICT 禁省略、禁自創第四值；二元真假容不下「核心屬實、修飾有出入」，故三值（ADR-4）。
- 無 CMD 或 CMD 不可重跑→強制記 UNVERIFIED；UNVERIFIED 為合法終態，不是恥辱欄。
- done 判定採消耗制（per-claim closure）：每宣稱閉合（PASS/FAIL）或顯式 UNVERIFIED；無數量門檻、通過率不作驗收（ADR-5）。
- 對照組生成步驟若條件於受評物輸出，不得計入通過率（ADR-4）。
- 欄位存在性檢查不分 VERDICT 值：UNVERIFIED 區塊同樣須 CMD／OUT／SOURCE-URL 齊備，三行模板（QUERY/WHERE/RESULT）是「附加」不是「替代」——合計七行，缺任一即 violation（parser 的 FIELDS 檢查先於 verdict 語意）。
- 內部產物證據（腳本輸出、patch diff、本地量測檔）的 SOURCE-URL 用 `file://` 絕對路徑直接指證據檔——parser 只驗欄位存在；外部文獻才需入 `references/sources.md`。
- claim record 寫完立即跑 `scripts/check_claims.py`，當 lint 用：預期首輪即抓缺欄，修完重跑至全 OK——人眼自查不可替代機器驗收，拖到 done 判定才跑只會把修正成本堆到終局。

## UNVERIFIED 三行模板（合法終態附件）

記 UNVERIFIED 時，區塊內另附三行，皆不可空：

    QUERY: <查詢詞>
    WHERE: <何處查：工具／站點／檔案>
    RESULT: <查到什麼；查無亦是合法結果>

## 正例（五欄齊全，可過 `scripts/check_claims.py`）

- CLAIM: 同 context 自審傾向回憶規則而非執行規則
  CMD: grep -n "回憶規則" chapters/02-judge-ladder.md
  OUT: chapters/02-judge-ladder.md: 結構性隔離——#72206 實測同 context 自審是「回憶規則而非執行規則」
  VERDICT: PASS
  SOURCE-URL: https://github.com/anthropics/claude-code/issues/72206

## 反例（踩兩坑）

- CLAIM: 未實跑即宣稱腳本通過
  CMD:
  OUT: 未留存任何輸出
  VERDICT: （留空——坑一）
  SOURCE-URL: n/a（內部自測，無外部文獻）

坑一：VERDICT 留空（非三值，等於未閉合）；坑二：無 CMD 卻未記 UNVERIFIED，宣稱懸空。一行修正：補 `VERDICT: UNVERIFIED` 並附三行模板，或實跑後補 CMD/OUT 再記 PASS。

## fixture 先行（驗證器自身的驗收）

任何作為 judge 的腳本／查詢，上線前先過必 FAIL 與必 PASS 兩 fixture（`tests/fixture-pass.md`、`tests/fixture-fail.md`；ADR-11）。對真實數據報 FAIL 時，先跑兩 fixture 分清腳本 bug 或數據洞——驗收器自身未驗，全鏈驗收失效。

## 循環 reference：三成因與對策

自生成 reference 自評 N/N 全過的循環（#70231，證據等級：單一個案）：成因一，reference 同 context 生成同 context 驗證→對策：上線前過 L1（新 context 子代理）；成因二，驗收判準由被驗物推導→對策：判準先於執行固定並寫入 claim record；成因三，欄名寫錯條目 invisible→對策：本檔欄名逐字＋機器驗。通過率因循環 reference 變難看是特性，不是缺陷。
