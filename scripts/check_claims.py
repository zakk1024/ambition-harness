#!/usr/bin/env python3
"""check_claims.py — ambition-harness 宣稱記錄驗證器（ADR-4／ADR-5）

用法：
    python3 check_claims.py <file.md> [<file2.md> ...]

掃描檔中以 `CLAIM:` 開頭的宣稱記錄區塊，逐條驗：
  1. 五欄齊備：CLAIM／CMD／OUT／VERDICT／SOURCE-URL；
  2. VERDICT 屬三值 {PASS, FAIL, UNVERIFIED}，留空或自創值即違規；
  3. VERDICT 為 PASS 或 FAIL 時，CMD 不得為空；
  4. VERDICT 為 UNVERIFIED 時，須附 QUERY:／WHERE:／RESULT: 三行且非空。

done 判定採消耗制（per-claim closure）：每宣稱閉合（PASS／FAIL）或顯式
UNVERIFIED；不設計數門檻，通過率不作驗收。

退出碼（exit code）定義：
    0  所有宣稱記錄格式完備（全部閉合，或顯式 UNVERIFIED 且三行齊備）
    1  存在格式違規：缺欄／VERDICT 留空或非三值／PASS-FAIL 無 CMD／UNVERIFIED 缺三行
    2  用法或 IO 錯誤：未給檔案、檔案不存在，或檔內無任何宣稱記錄

多檔聚合（rc 不變式）：違規（1）優先於參數／IO 錯誤（2）——任一檔有違規即回 1，
僅全庫無違規時才回 2／0；單檔行為不變（pass=0／fail=1／參數錯=2）。

欄值正規化（明文，非靜默）：各欄值「首尾」連續星號（Markdown 強調記號）於解析時剝除
——*see docs*→see docs；欄值中段星號不動。含強調記號之存證請知悉此規則。

機讀輸出：每列前綴 CLAIMCHECK:，違規明細同行接於 status=VIOLATION 之後。
無 python3 時之人工核對退化：逐條肉眼核對五欄齊備、VERDICT 為三值之一、PASS/FAIL 條目 CMD 非空、UNVERIFIED 條目 QUERY/WHERE/RESULT 三行齊。
"""

import re
import sys

PREFIX = "CLAIMCHECK"
VERDICTS = {"PASS", "FAIL", "UNVERIFIED"}
FIELDS = ("CMD", "OUT", "VERDICT", "SOURCE-URL")
LINE = re.compile(
    r"^\s{0,3}(?:[-*+]\s+)?\**\s*"
    r"(CLAIM|CMD|OUT|VERDICT|SOURCE-URL|QUERY|WHERE|RESULT)"
    r"\**\s*[:：]\s?(.*)$"
)


def parse(text):
    """回傳宣稱記錄 list；每條為 dict（含列區塊內先後出現的欄位）。"""
    claims = []
    cur = None
    for raw in text.splitlines():
        m = LINE.match(raw)
        if not m:
            continue
        key = m.group(1)
        # 明文規則：剝除欄值首尾連續星號（Markdown 強調記號，*x*→x）；中段不動。
        # 語意見本檔 docstring〈欄值正規化〉——非靜默改值。
        val = re.sub(r"^\*+|\*+$", "", m.group(2).strip()).strip()
        if key == "CLAIM":
            cur = {"CLAIM": val, "_no": len(claims) + 1}
            claims.append(cur)
        elif cur is not None:
            cur[key] = val
    return claims


def verdict_of(claim):
    m = re.match(r"([A-Za-z]+)", claim.get("VERDICT", ""))
    return m.group(1).upper() if m else ""


def check(claim):
    """回傳 (verdict, 違規訊息 list)。"""
    errs = []
    for f in FIELDS:
        if f not in claim:
            errs.append("缺欄 %s" % f)
    verd = verdict_of(claim)
    if not verd:
        errs.append("VERDICT 留空")
    elif verd not in VERDICTS:
        errs.append("VERDICT 非三值: %s" % claim.get("VERDICT", ""))
    if verd in ("PASS", "FAIL") and "CMD" in claim and not claim["CMD"].strip():
        errs.append("PASS/FAIL 但 CMD 空值")
    if verd == "UNVERIFIED":
        for k in ("QUERY", "WHERE", "RESULT"):
            if k not in claim:
                errs.append("UNVERIFIED 缺 %s 行" % k)
            elif not claim[k].strip():
                errs.append("UNVERIFIED %s 空值" % k)
    return verd, errs


def main(argv):
    if len(argv) < 2:
        print("USAGE: python3 check_claims.py <file.md> [...]", file=sys.stderr)
        return 2
    saw_viol = False
    saw_err = False
    for path in argv[1:]:
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError as exc:
            print("%s: IO-ERROR %s: %s" % (PREFIX, path, exc), file=sys.stderr)
            saw_err = True
            continue
        claims = parse(text)
        if not claims:
            print("%s: file=%s claims=0（檔內無宣稱記錄）" % (PREFIX, path))
            saw_err = True
            continue
        n_viol = 0
        for c in claims:
            verd, errs = check(c)
            if errs:
                n_viol += 1
                status = "VIOLATION: " + "；".join(errs)
            else:
                status = "OK"
            print('%s: #%d "%s" verdict=%s status=%s'
                  % (PREFIX, c["_no"], c["CLAIM"][:40], verd or "NONE", status))
        print("%s: file=%s claims=%d violations=%d" % (PREFIX, path, len(claims), n_viol))
        if n_viol:
            saw_viol = True
    if saw_viol:  # 違規語意優先：rc=1 不被 rc=2 蓋（多檔聚合，見 docstring）
        return 1
    return 2 if saw_err else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
