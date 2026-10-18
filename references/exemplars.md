# exemplars.md — 案例庫資料本體（ADR-9）

> 使用規則見 chapters/05-evidence-cases.md；校準註記模板見 references/story-calibration.md。
> 入庫契約（五欄位）：①三件組 ②效度數據（無則「待補測」）③三值判定 ④體裁標籤 ⑤校準註記（傳說級必附）。無驗證欄不得入庫。

## 例 1 · crash-free（工程／altitude 樣板）
- 三件組：不變量 keep apps crash-free；驗證器＝crash report 對版本逐項歸零（CMD 隨專案定）；環境＝遙測＋commit↔version 對照＋三平台重現艦（SOURCE-URL: https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/）。
- 效度數據：待補測——原文未給 %；社群亦追問 "And did it work? What % fewer crashes?"（譯：有效嗎？當機少了幾％？）（SOURCE-URL: https://news.ycombinator.com/item?id=50100345）。
- VERDICT: PASS（案例結構屬實；改善幅度未測，不得虛填）。
- 體裁標籤：軟體維運／長期專案。
- 校準註記：非傳說級；引用時不得添加未測數字。

## 例 2 · Bannizer 四分鐘（先例效應／vicarious 錨）
- 三件組：不變量「先例一出、群體門檻即崩」之敘事錨；驗證器＝日期差核算（CMD：date 差值）；環境＝公開賽事紀錄。
- 效度數據：1954-05-06 Iffley Road 3:59.4；"Just 46 days later, on 21 June 1954"（譯：僅 46 天後，1954 年 6 月 21 日。）Landy 於 Turku 3:57.9（IAAF 記錄 3:58.0）——SOURCE-URL: https://en.wikipedia.org/wiki/Roger_Bannister。
- VERDICT: PASS——**皆為正式紀錄**（弱表述，R-3；精確計時系統考不派工）。
- 體裁標籤：運動／紀錄突破。
- 校準註記：**待驗欄**——3:59.4 為人工計時；兩套計時系統與進位規則之年代歧義未驗。引用止於弱表述＋日期，不得加碼。

## 例 3 · Sawe 2026 倫敦 sub-2（當代 watch-someone-do-it）
- 三件組：不變量「合法賽事首見 sub-2」；驗證器＝官方名次頁核對（CMD：curl＋grep 名次欄）；環境＝World Athletics 賽報。
- 效度數據：2026-04-26 倫敦 1:59:30；同場 Kejelcha 1:59:41——SOURCE-URL: https://worldathletics.org/competitions/world-athletics-label-road-races/news/sawe-two-hour-assefa-world-record-london-marathon；交叉 SOURCE-URL: https://www.reddit.com/r/Ultramarathon/comments/1sw48co/sabastian_sawe_runs_first_sub2hour_marathon_race/、https://en.wikipedia.org/wiki/2026_London_Marathon。
- VERDICT: PASS。
- 體裁標籤：運動／紀錄突破（與例 2 同標籤——檢索新舊各取一，先例＋當代對照）。
- 校準註記：Kipchoge 2019 為表演賽條件（1:59:40.2），不得與正式紀錄混寫（SOURCE-URL: https://www.sportico.com/leagues/other-sports/2026/mens-marathon-world-record-sabastian-sawe-adidas-nike-1234891251/，節錄）。

## 例 4 · Dantzig 1939（傳說級；expectancy 敘事錨）
- 三件組：不變量「不知難→不受自我設限」之 expectancy 錨；驗證器＝出處對質（本檔＋sources.md 對應條目）；環境＝傳記文獻。
- 效度數據：核心情節（遲到、Neyman 板上兩題、數日後交、六週後告知）經維基逐點核——SOURCE-URL: https://en.wikipedia.org/wiki/George_Dantzig；考據交叉 SOURCE-URL: https://math.stackexchange.com/questions/533146/dantzigs-unsolved-homework-problems。
- VERDICT: PASS（核心屬實、修飾有出入——三值判定容「屬實有保留」，ADR-4）。
- 體裁標籤：科學家軼事／學習與期望。
- 校準註記（傳說級必附；模板見 story-calibration.md）：①流傳版「two of the most famous」為訃聞級放大，本人 1986 訪談僅稱 famous；②第二題 Abraham Wald 幾同時獨立解出、1951 與 Dantzig 合著——非獨佔神話。引用時本註記隨行。

## 例 5 · Goya〈Modo de volar〉（考據級引用示範；accession 錨）
- 三件組：不變量「館藏與年代精確表述」；驗證器＝accession 對查（CMD：對 NGA 藏品頁 grep 編號）；環境＝館方資料庫。
- 效度數據：NGA Rosenwald Collection accession 1951.10.55，與藏品檔名 modo_de_volar_a_way_of_flying_1951.10.55.jpg 吻合——SOURCE-URL: https://www.nga.gov/artworks/39846-modo-de-volar-way-flying。
- VERDICT: PASS。
- 體裁標籤：藝術／考據示範。
- 校準註記：年代禁單一年份——畫稿 in or after 1816；Los Proverbios（Disparates）第 13 版，Harris 1964 no.260；本館藏印本為死後約 1854–63 試印。accession 級精確度＝本庫引用樣板。

## 範例缺口（回饋區；章 05 規則 4）
- （空）格式：需要體裁｜落空原因｜日期。
