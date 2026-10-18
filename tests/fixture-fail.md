# fixture-fail — 必 FAIL（退出碼 1）案例（ADR-11）

預期：`python3 scripts/check_claims.py tests/fixture-fail.md` 退出碼 1。
預期輸出（關鍵三行）：

    CLAIMCHECK: #1 "空 VERDICT 應報違規" verdict=NONE status=VIOLATION: VERDICT 留空
    CLAIMCHECK: #2 "PASS 無 CMD 應報違規" verdict=PASS status=VIOLATION: 缺欄 CMD
    CLAIMCHECK: file=tests/fixture-fail.md claims=2 violations=2

設計（兩坑）：#1 VERDICT 留空——非三值、未閉合；#2 PASS 卻無 CMD——宣稱懸空。驗證器對此兩坑必須各報一違規；恆真條件由本案例把關。

- CLAIM: 空 VERDICT 應報違規
  CMD: python3 scripts/check_claims.py tests/fixture-fail.md
  OUT: CLAIMCHECK: #1 ... status=VIOLATION: VERDICT 留空
  VERDICT:
  SOURCE-URL: n/a（本庫自測，無外部文獻）

- CLAIM: PASS 無 CMD 應報違規
  OUT: CLAIMCHECK: #2 ... status=VIOLATION: 缺欄 CMD
  VERDICT: PASS
  SOURCE-URL: n/a（本庫自測，無外部文獻）
