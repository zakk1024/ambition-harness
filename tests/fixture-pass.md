# fixture-pass — 必 PASS 案例（ADR-11）

預期：`python3 scripts/check_claims.py tests/fixture-pass.md` 退出碼 0。
預期輸出（兩行）：

    CLAIMCHECK: #1 "fixture-pass 單條五欄齊全應通過" verdict=PASS status=OK
    CLAIMCHECK: file=tests/fixture-pass.md claims=1 violations=0

設計：單條宣稱、五欄齊全、VERDICT 三值之一、PASS 且 CMD 非空——驗證器對完備記錄不得誤報。

- CLAIM: fixture-pass 單條五欄齊全應通過
  CMD: python3 scripts/check_claims.py tests/fixture-pass.md
  OUT: CLAIMCHECK: file=... claims=1 violations=0
  VERDICT: PASS
  SOURCE-URL: n/a（本庫自測，無外部文獻）
