import argparse
import sys
from pathlib import Path

"""
Goal: Print the "MISSING" keys (keys present in .env.example but absent in .env).
Exit with code 1 if there is at least one missing key; otherwise exit 0.
Ignore blank lines and lines starting with '#'.
Parse KEY and VALUE by the first '=' only; trim spaces around KEY and VALUE.
Keys are case-sensitive.
"""
parser = argparse.ArgumentParser(description="Compare .env.example and .env (loose mode)")
parser.add_argument("--example", default=".env.example", help="path to .env.example")
parser.add_argument("--env", default=".env", help="path to .env")
args = parser.parse_args()

example_path = args.example
env_path = args.env

# error when missing file, exit 2:
for p, kind in [(example_path, ".env.example"), (env_path, ".env:")]:
    if not Path(p).is_file():
        print(f"{kind} not found: {p}", file=sys.stderr)
        sys.exit(2)

example_keys = set()
with open(example_path, "r", encoding="utf-8") as f:
    for raw in f:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key = line.split("=", 1)[0].strip()
        if key:
            example_keys.add(key)

env_keys = set()

with open(env_path, "r", encoding="utf-8") as e:
    for raw in e:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key = line.split("=", 1)[0].strip()
        if key:
            env_keys.add(key)

missing = sorted(example_keys - env_keys)
extra = sorted(env_keys - example_keys)
ok = sorted(env_keys & example_keys)

print("MISSING")
for k in missing:
    print("  " + k)
print("EXTRA")
for k in extra:
    print("  " + k)
print("OK")
for k in ok:
    print("  " + k)

sys.exit(1 if (missing or extra) else 0)
