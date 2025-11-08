# dotenv-guard — SPEC I/O (Week 0 • Nano)

## 1) Purpose
`dotenv-guard` compares `.env.example` (public template) with `.env` (local secrets) and reports configuration mismatches so projects run consistently across machines.

Scope for Week 0 (Nano): define I/O only. No implementation yet.

---

## 2) Inputs (CLI)
- Required files:
  - `--example <path>` (default: `.env.example`)
  - `--env <path>`     (default: `.env`)
- Optional flags:
  - `--strict`   : report `DIFF` when values differ from example defaults
  - `--loose`    : default mode; only cares about `MISSING` and `EXTRA`
  - `--dry-run`  : print report only; never writes to disk
  - `--format text|json` (default: `text`)

---

## 3) Parsing Rules
- Accept lines in the form `KEY=VALUE`.
- Ignore blank lines and comments starting with `#`.
- Trim surrounding whitespace around KEY and VALUE.
- Keys are **case-sensitive** (`APP_ENV` ≠ `App_Env`).
- Multi-line and variable interpolation (e.g., `${VAR}`) are **out of scope** for Week 0.

---

## 4) Output Specification
- Default format: **text**.
- Print sections in this order: `MISSING`, `EXTRA`, then `OK` (and `DIFF` if `--strict`).
- Within each section, list keys one per line, **sorted A→Z**.
- Example (loose mode):
MISSING
    DATABASE_URL
EXTRA
    DEBUG_TOOLBAR
OK
    APP_ENV
    LOG_LEVEL
    PORT
    SECRET_KEY
- Example (strict mode):
MISSING
    DATABASE_URL
EXTRA
    DEBUG_TOOLBAR
OK
    APP_ENV
    PORT
DIFF
    LOG_LEVEL
    SECRET_KEY
- JSON format example:
```json
{
    "missing": ["DATABASE_URL"],
    "extra": ["DEBUG_TOOLBAR"],
    "ok": ["APP_ENV", "PORT"],
    "diff": ["LOG_LEVEL", "SECRET_KEY"]
}
```
---

## 5) Exit Codes
- `0`: No issues (no `MISSING`/`EXTRA`; and no `DIFF` in strict mode).
- `1`: Has `MISSING` or `EXTRA` (or `DIFF` in strict mode).
- `2`: I/O error (e.g., file not found, permissions).
- `3`: Parse error (e.g., duplicate keys detected in a single file).

---

## 6) Errors & Messages
- `ENOEXAMPLE`: `.env.example not found: <path>`
- `ENOENV`: `.env not found: <path>`
- `DUP_KEY`: `duplicate key(s) detected: KEY1, KEY2`
- `PARSE_WARN`: `ignored N line(s) not in KEY=VALUE format`

---

## 7) Sample Cases (for manual testing)
### 7.1 `.env.example`
APP_ENV=development
PORT=8000
LOG_LEVEL=INFO
SECRET_KEY=<FILL_ME>
DATABASE_URL=postgresql://<USER>:<PASS>@localhost:5432/phoenix
### 7.2 `.env` (local)
APP_ENV=development
PORT=8000
LOG_LEVEL=DEBUG
SECRET_KEY=...your_generated_secret...
DEBUG_TOOLBAR=1
### 7.3 Expected (loose mode)
MISSING
    DATABASE_URL
EXTRA
    DEBUG_TOOLBAR
OK
    APP_ENV
    LOG_LEVEL
    PORT
    SECRET_KEY
### 7.4 Expected (strict mode)
MISSING
    DATABASE_URL
EXTRA
    DEBUG_TOOLBAR
OK
    APP_ENV
    PORT
DIFF
    LOG_LEVEL
    SECRET_KEY

---

## 8) Non-Goals (Week 0)
- No automatic fixes (does not write to `.env`).
- No multi-file merge (`.env.local` etc.).
- No variable interpolation or multi-line values.
- No network or external service calls.

---

## 9) Definition of Done (DoD) - Week 0 • Nano
- `SPEC_IO.md` exists with all sections above.
- Contains at least one concrete sample input/output (Section 7)
- Ready to commit under `quests/Q1-DotenvGuard`.
