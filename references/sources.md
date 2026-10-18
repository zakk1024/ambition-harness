# sources.md — 正典化出處庫（C 維護）

> 唯一轉錄來源：research/ledger-a・b・c.md；只轉錄、不新增事實。Tier 對照：ledger primary→A（一手）、secondary→B（二手）。全庫 SOURCE-URL 須可對應本檔（V24／自驗抽查）。引言紀律：宣稱、出處、逐字核三者齊，才加引號。

## 本體（章節引用核心）

### Rieseberg〈How to be more ambitious: a tutorial for humans with models〉
URL: https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/
Tier: A
判定：核心文本，全文已讀；四分法、altitude 前提（crash report 存取、commit↔version 對照、三平台重現）與 outside validation 直引均已核。

### HN 討論串 #50100345
URL: https://news.ycombinator.com/item?id=50100345
Tier: A
判定：逐樓已讀；mjd 決策 checkpoint 反論、UncleEntity 湊綠、maxcb 效度追問皆出此。

### anthropics/claude-code issue #72206
URL: https://github.com/anthropics/claude-code/issues/72206
Tier: A
判定：一手 issue；獨立性優於加提示；乾淨 context＋run-dont-read 實測。證據等級：單一個案。

### anthropics/claude-code issue #70231
URL: https://github.com/anthropics/claude-code/issues/70231
Tier: A
判定：一手 issue；自生成 reference 不構成驗證；N/N pass 於真工具循環被推翻。證據等級：單一個案。

### Locke & Latham 2002（American Psychologist 57(9):705–717）
URL: https://med.stanford.edu/content/dam/sm/s-spire/documents/PD.locke-and-latham-retrospective_Paper.pdf
Tier: A
判定：一手文獻全文已讀；d≈.42–.80、四機制、調節變項皆出此；文內轉引之次級文獻未回取。

### Bandura 1977〈Self-efficacy〉（Psychological Review 84(2):191–215）
URL: https://pubmed.ncbi.nlm.nih.gov/847061/
Tier: A
判定：僅讀摘要與二級轉述，全文未讀——已標註於 self-efficacy-sources.md；相關未決待辦見同檔。

### anthropics/skills repo
URL: https://github.com/anthropics/skills
Tier: A
判定：README 已讀；官方 skills 範式與範例結構。

### agent skills spec v1.1
URL: https://github.com/anthropics/skills/blob/main/spec/agent-skills-spec.md
Tier: A
判定：全文已讀；frontmatter 僅 name+description 必需；載入才計價（漸進揭露）。

### VoltAgent/awesome-claude-code-subagents
URL: https://github.com/VoltAgent/awesome-claude-code-subagents
Tier: A
判定：repo 結構與 README 已讀；persona 庫生態實況（多數條目僅 persona 描述）。

### r/ClaudeAI 1qide7x（orchestration system）
URL: https://www.reddit.com/r/ClaudeAI/comments/1qide7x/i_built_an_orchestration_system_that_keeps_claude/
Tier: A
判定：OP 自述摘要級；403 未讀全文——僅摘要可引。

### r/vibecoding 1wgnijd（Opus orchestrator）
URL: https://www.reddit.com/r/vibecoding/comments/1wgnijd/my_opusorchestrator_sonnetsubagent_claude_code/
Tier: A
判定：高讚回覆摘要；403 未讀全文——重試須上限之教訓出自此。

### Terry Tao 〈math 2.0〉網誌
URL: https://terrytao.wordpress.com/2026/10/10/math-2-0/
Tier: A
判定：本人網誌全文已讀；"astounding in some directions, while inadequate in others" 逐字核。

### World Athletics：Sawe 倫敦賽報
URL: https://worldathletics.org/competitions/world-athletics-label-road-races/news/sawe-two-hour-assefa-world-record-london-marathon
Tier: A
判定：官方賽報；1:59:30、Kejelcha 1:59:41、賽期 2026-04-26，名次完整。

### Wikipedia：Roger Bannister
URL: https://en.wikipedia.org/wiki/Roger_Bannister
Tier: B
判定：節錄核對；1954-05-06 3:59.4 與 46 天後 Landy 3:57.9（IAAF 記 3:58.0）自洽；計時系統歧義未決——強表述列待驗欄。

### Wikipedia：George Dantzig
URL: https://en.wikipedia.org/wiki/George_Dantzig
Tier: B
判定：節錄；核心情節屬實且自附訛傳警示；引 College Math J 17 (1986) 292–314 訪談（Albers, Reid & Dantzig）。

### 美國國家藝廊藏品頁：Goya Modo de volar
URL: https://www.nga.gov/artworks/39846-modo-de-volar-way-flying
Tier: A
判定：館方資料；accession 1951.10.55；年代須精確表述（in or after 1816；Harris 1964 no.260；本館印本約 1854–63 試印）。

### Math.StackExchange #533146（Dantzig 考據）
URL: https://math.stackexchange.com/questions/533146/dantzigs-unsolved-homework-problems
Tier: B
判定：高票考據：famous vs most famous 出入；兩題之正式文獻出處。

## 附錄（交叉／佐證／待深讀）

### r/ClaudeCode 1wvhzr2（orchestrator+doers 拓撲）
URL: https://www.reddit.com/r/ClaudeCode/comments/1wvhzr2/my_claude_code_subagent_setup_orchestrator_doers/
Tier: B
判定：標題級拓撲證據；403 僅節錄，未讀全文。

### r/ClaudeAI 1x6fcdq（原文轉貼討論）
URL: https://www.reddit.com/r/ClaudeAI/comments/1x6fcdq/how_to_be_more_ambitious_felixrieseberg/
Tier: A
判定：實戰反應節錄；佐證原文傳播與社群接收。

### r/Marathon_Training 1sw49jd
URL: https://www.reddit.com/r/Marathon_Training/comments/1sw49jd/
Tier: B
判定：sub-2 社群傳播佐證；節錄。

### r/Ultramarathon 1sw48co（Sawe 賽後討論）
URL: https://www.reddit.com/r/Ultramarathon/comments/1sw48co/sabastian_sawe_runs_first_sub2hour_marathon_race/
Tier: A
判定：社群親歷交叉確認 1:59:30 與合法賽事首例。

### Wikipedia：2026 London Marathon
URL: https://en.wikipedia.org/wiki/2026_London_Marathon
Tier: B
判定：賽期 2026-04-26 與前三名；佐證用。

### Sportico：Sawe 世界紀錄報導
URL: https://www.sportico.com/leagues/other-sports/2026/mens-marathon-world-record-sabastian-sawe-adidas-nike-1234891251/
Tier: B
判定：sanctioned 賽事首破 2 之媒體論述；節錄。

### BBC Sport：倫敦馬拉松賽報
URL: https://www.bbc.com/sport/athletics/articles/crm1m7e0zwzo
Tier: B
判定：亞軍 Assefa 亦破 2 之佐證；節錄。

### dev.to：100 個 subagents 實測
URL: https://dev.to/suraj_khaitan_f893c243958/i-built-100-claude-code-subagents-these-are-the-12-that-actually-earn-their-context-10nn
Tier: B
判定：摘要級；深層巢狀與 token 燒爆實測。

### Gizmodo：業餘天文學家發現行星
URL: https://gizmodo.com/did-claude-help-an-amateur-astronomer-discover-a-new-planet-2000824393
Tier: B
判定：僅經原文轉引；案例入庫前須回讀一手（未決，勿入庫）。

### Patrick Collison 〈Fast〉
URL: https://patrickcollison.com/fast
Tier: B
判定：僅經原文轉引；敘事素材，未逐條核。

### Wikipedia：Self-efficacy
URL: https://en.wikipedia.org/wiki/Self-efficacy
Tier: B
判定：主體章節已讀；mastery 最有效、相似性調節、低效能者威脅迴避。

### Sloww：《Inner Game of Tennis》書摘
URL: https://www.sloww.co/inner-game-tennis/
Tier: B
判定：多處直引；Self 1／Self 2、意象與自然信任。

### Graham Mann：同書章節筆記
URL: https://grahammann.net/book-notes/the-inner-game-of-tennis-timothy-gallwey
Tier: B
判定：章節級書摘；與 Sloww 交叉驗證用。

### Lattice：Lattiverse 2026 公告
URL: https://lattice.com/blog/everything-we-announced-at-lattiverse-2026
Tier: B
判定：僅證 permission to fail 成流行語；弱證據，標敘事級。

### Artnet：米開朗基羅十四行詩手稿
URL: https://news.artnet.com/art-world/art-bites-michelangelo-sistine-chapel-poem-2435098
Tier: B
判定：轉介一手書信與詩稿；節錄。

### The Conversation：米開朗基羅不愛畫西斯汀
URL: https://theconversation.com/michelangelo-hated-painting-the-sistine-chapel-and-never-aspired-to-be-a-painter-to-begin-with-275788
Tier: B
判定：學者評論引同手稿；交叉來源。

### Small Wars Journal：Kelley 評介
URL: https://smallwarsjournal.com/2015/03/11/improving-the-military-with-a-little-innovation
Tier: B
判定：逐段引《The Art of Innovation》技法；書名作者核實無誤。

### HN #50043026（Tao 文轉貼）
URL: https://news.ycombinator.com/item?id=50043026
Tier: B
判定：頂樓引 PDF 同句；社群側佐證。
