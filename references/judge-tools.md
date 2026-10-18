# judge-tools.md — judge 階梯之 L2/L3 工具對照（ADR-3）

> 機制正本在 chapters/02-judge-ladder.md（B 維護）；本檔只答「用什麼工具充當 L2 host 原生檢查／L3 領域回查」。
> 紀律：未親驗的接法一律標**待驗**；不得虛構命令輸出。每項判定仍走章 02 claim record。

## L2 — host 原生檢查

| host 機制 | 充當方式 | 狀態 |
|---|---|---|
| Claude Code hooks（如 PostToolUse） | 工具事件後跑檢查命令，輸出回饋 agent 當 judge 輸入 | 接法**待驗**（未於本專案實測） |
| CI／本地測試與 lint（pytest、tsc、ruff…） | 以可重跑命令＋可判讀輸出充當 L2 | 常規；命令須寫入驗證器 CMD 欄 |
| 官方 skill 機制（載入才計價） | frontmatter 僅 name+description 必需——本 skill 據此壓縮載入成本（SOURCE-URL: https://github.com/anthropics/skills/blob/main/spec/agent-skills-spec.md；https://github.com/anthropics/skills） | 已核（spec v1.1 全文） |

## L3 — 領域工具／資料回查

| 領域 | 工具／資料 | 判讀原則 |
|---|---|---|
| 測試 | pytest -x 等逐條輸出 | 湊綠防護：對照章 06 #2，驗證器獨立於被優化目標 |
| 版本／環境 | pip freeze、套件註冊表比對 | 對照章 01 環境清單逐項 |
| 資料回查 | 對一手源 grep 關鍵欄位（如世界紀錄成績頁） | 出處須在 references/sources.md 有條目 |

## run-dont-read（#72206 實測教訓）

獨立性優於加提示：乾淨 context＋**跑命令看輸出**，優於讀碼自證。每宣稱一條可否證命令（SOURCE-URL: https://github.com/anthropics/claude-code/issues/72206）。
同族：自生成 reference 不構成驗證——N/N pass 須被真工具循環檢驗（SOURCE-URL: https://github.com/anthropics/claude-code/issues/70231；證據等級：單一個案）。
證據等級：單一 issue 個案，非普遍實證；引用時隨此註記。

## 接法優序

1. 領域有現成可跑檢查→L2/L3 直接接（寫入驗證器 CMD）。
2. 無→host hooks 包一層檢查腳本（**待驗**，先小規模試）。
3. 皆無→退回人工 checkpoint（章 01），並記範例缺口。
