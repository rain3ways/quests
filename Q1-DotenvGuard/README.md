# dotenv-guard (Week 0 - Nano)

## Purpose
Compare .env.example (template) vs .env (local) and report MISSING / EXTRA (and DIFF in --strict).

## Usage (I/O spec only; no impl yet)
- Inputs: --example, --env; flags: --loose (default) | --strict, --format text|json, --dry-run
- Outputs: section in order MISSING → EXTRA → OK (→ DIFF if --strict), A→Z sorting
- Exit codes: 0=clean | 1=issues | 2=I/O error | 3=parse error (duplicate keys)

## Samples
See SPEC_IO.md §7

## Roadmap
Week 1: parser; Week 2: reporter; Week 3: CI and fixtures.
