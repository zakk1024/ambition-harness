# Changelog

All notable changes to this skill are recorded here. Version numbers are
`MAJOR.MINOR.PATCH`: MAJOR when the state machine or the claim contract changes,
MINOR for new rules, references or scripts, PATCH for wording and fixes.

## 2.0.0 — 2026-11-06

Trigger: a four-round blind audit of a real project (medaesthetics-recon) found
that a closure document claimed two fixes that were not both present. The judge
caught the residue with a broad scan. Those lessons are now rules.

### Added

- `SKILL.md`: **修復輪紀律（品質結果制）** section — full-suite rerun after each
  repair, stable-green criterion (two consecutive green runs), UNVERIFIED remedy
  by producing real evidence, `judge#N` provenance, fixture input-contract rule,
  public-CLI E2E rule, residue scan with a broad pattern, and "a closure document
  is not evidence".
- `SKILL.md`: **報進度** node — status and next step are recomputed from the
  ledger, verifier output, file mtimes and exit codes; never from a chat summary,
  an earlier claim or a doer's self-report.
- `SKILL.md`: judge row now points to the hard clauses in
  `references/subagent-templates.md` 範本 2; Self-check gains two questions
  (no `partial` verdicts; residue scan).
- `chapters/06-failure-modes.md`: failure mode 10 **殘留漏掃**, with the measured
  case (`S4-media.md:27` still said 56 while the closure said both were fixed).
- `references/subagent-templates.md`: 範本 2 hard clauses — write whitelist (one
  new report file, no edits to the artifact under review), self-run evidence,
  rerunnable commands with `file:line`, verifier self-run with raw output and exit
  code, verdict-first report format, parent re-check of the judge's numbers, and
  recovery when a judge hits its call cap before writing the report. Adds
  範本 5 council chair.
- `references/claim-format.md`: field-presence check applies to UNVERIFIED too;
  internal evidence uses `file://` absolute paths; run `scripts/check_claims.py`
  as a lint right after writing the record.
- `references/judge-tools.md`: single-file HTML smoke test
  (`scripts/smoke_html_cdp.mjs`) and its discipline — fixture the verifier first,
  exit-code semantics, cleanup guard, and "a scanner bug is not a doer FAIL".
- `scripts/smoke_html_cdp.mjs`: headless Chrome CDP smoke test for single-file
  HTML deliverables.
- `VERSION`, `CHANGELOG.md`.

### Changed

- `README.md`: core-line badge 54 → 71, version badge 2.0.0.

## 1.0.0 — 2026-10-18

Initial public release: goal compiler (invariant + falsifiable verifier +
environment manifest), four-layer judge ladder, claim record format, range-crew
templates, and the thin-core layout.
