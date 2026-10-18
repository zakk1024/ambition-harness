# worked-example.md — 考據實作示範（C 考據表全記錄；素材僅取 ledger-c）

> 用途：章 02 claim record（格式契約見 references/claim-format.md，B 維護）之示範語料——
> 「屬實有保留」如何以三值判定容納（ADR-4）。依審A-c#2：本檔為考據敘事，僅要求 VERDICT 欄存在；欄位仍照五欄齊填以作示範。表格式列（列首 |）不匹配驗證器列 regex，check_claims.py 對本檔回 claims=0——屬驗收面豁免（機驗對表格無路徑），非錯誤。
> Goya 為年代表述錨：禁單一年份。Dantzig 為版本出入錨：核心與流傳版分寫。

| # | CLAIM（宣稱） | CMD（可否證查核） | OUT（觀察） | VERDICT | SOURCE-URL |
|---|---|---|---|---|---|
| 1 | Dantzig 1939 核心情節屬實；「most famous」與獨解兩處屬流傳強化 | 對質維基正文五情節點＋math.SE 考據 | 五點吻合；訪談版僅稱 famous；Wald 幾同時解、1951 合著 | PASS | https://en.wikipedia.org/wiki/George_Dantzig／https://math.stackexchange.com/questions/533146/dantzigs-unsolved-homework-problems |
| 2 | Bannister 1954-05-06 3:59.4；46 天後 Landy 更快——弱表述「皆為正式紀錄」 | 日期差核算＋賽事紀錄比對 | 1954-06-21 Turku 3:57.9（IAAF 記 3:58.0）；計時系統歧義未決 | PASS | https://en.wikipedia.org/wiki/Roger_Bannister |
| 3 | Sawe 2026-04-26 倫敦 1:59:30＝合法賽事首見 sub-2 | 官方賽報名次與時間核對 | 1:59:30；Kejelcha 1:59:41 同場；Kipchoge 為表演賽另計 | PASS | https://worldathletics.org/competitions/world-athletics-label-road-races/news/sawe-two-hour-assefa-world-record-london-marathon／https://www.reddit.com/r/Ultramarathon/comments/1sw48co/sabastian_sawe_runs_first_sub2hour_marathon_race/ |
| 4 | Tao 對 AI 數學能力之評語為逐字引 | 對本人網誌原文逐字比對 | "astounding in some directions, while inadequate in others"（譯：某些方向驚人，另些方向不足。）吻合 | PASS | https://terrytao.wordpress.com/2026/10/10/math-2-0/ |
| 5 | Michelangelo 自認非畫家、不情願畫西斯汀；仍於 1512 完成 | 對書信與十四行詩手稿轉介 | "I am not a painter"（譯：我不是畫家。）語境吻合；1512 完工不變——自嘲修辭與史實並存 | PASS | https://news.artnet.com/art-world/art-bites-michelangelo-sistine-chapel-poem-2435098／https://theconversation.com/michelangelo-hated-painting-the-sistine-chapel-and-never-aspired-to-be-a-painter-to-begin-with-275788 |
| 6 | Goya 〈Modo de volar〉藏 NGA，accession 1951.10.55 | NGA 藏品頁對查編號與檔名 | 1951.10.55 與檔名 modo_de_volar_..._1951.10.55.jpg 吻合；年代須帶約數 | PASS | https://www.nga.gov/artworks/39846-modo-de-volar-way-flying |
| 7 | Kelley & Littman「名詞→動詞」技法出《The Art of Innovation》 | 對書評逐段引文核對 | 技法、章節歸屬、書名作者無誤；評介屬二手轉述 | PASS | https://smallwarsjournal.com/2015/03/11/improving-the-military-with-a-little-innovation |

引用規則：轉引此表時 VERDICT 與校準註記隨行（出處見 references/sources.md 對應條目；例 1 之出入細節另見 story-calibration.md）。
