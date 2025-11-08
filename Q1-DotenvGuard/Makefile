# Minimal Makefile for
PY ?= python3

# Paths (default to the quest folder)
EXAMPLE	?= ./.env.example
ENV		?= ./.env
OKENV	?= ./.env.ok

SCRIPT	?= ./dotenv_guard.py

.PHONY: test test-ok run build help hook lint fmt

help:
	@echo "Targets:"
	@echo " make test		- expect non-zero if MISSING or EXTRA exists (using $(ENV))"
	@echo " make test-ok	- expect zero exit when using $(OKENV) (optional fixture)"
	@echo " make run		- run the script with default paths"
	@echo " make build		- no-op for Python (always succeed)"
	@echo " make hook		- install & autoupdate pre-commit hooks"
	@echo " make fmt		- format code via ruff-format"
	@echo " make lint		- lint (and fix) via ruff"

test:
	@$(PY) $(SCRIPT) --example $(EXAMPLE) --env $(ENV); \
	rc=$$?; \
	if [ $$rc -eq 1 ] || [ $$rc -eq 0 ]; then :; else echo "unexpected exit code $$rc"; exit 2; fi; \
	if [ $$rc -eq 0 ]; then echo "[FAIL] expected non-zero (no issues detected)"; exit 1; fi; \
	echo "[PASS] test (missing/extra were detected)"

test-ok:
	@$(PY) $(SCRIPT) --example $(EXAMPLE) --env $(OKENV); \
	rc=$$?; \
	if [ "$$rc" -ne 0 ]; then echo "[FAIL] expected zero exit with ok env (got $$rc)"; exit 1; fi; \
	echo "[PASS] test-ok (no issues detected)"

run:
	@$(PY) $(SCRIPT) --example $(EXAMPLE) --env $(ENV) || true

build:
	@echo "Nothing to build for Python script, skipping."

hook:
	@pre-commit install && pre-commit autoupdate

fmt:
	@pre-commit run ruff-format --all-files

lint:
	@pre-commit run ruff --all-files
