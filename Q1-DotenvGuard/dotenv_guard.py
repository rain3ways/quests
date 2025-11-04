import sys


"""
Goal: Print the "MISSING" keys (keys present in .env.example but absent in .env).
Exit with code 1 if there is at least one missing key; otherwise exit 0.
Ignore blank lines and lines starting with '#'.
Parse KEY and VALUE by the first '=' only; trim spaces around KEY and VALUE.
Keys are case-sensitive.
"""

example_keys = set()
f = open(".env.example", "r", encoding="utf-8")
for raw in f:
    line = raw.strip()
    if not line or line.startswith("#"):
        continue
    if "=" not in line:
        continue
    key = line.split("=", 1)[0].strip()
    if key:
        example_keys.add(key)
f.close()


env_keys = set()

e = open(".env", "r", encoding="utf-8")
for raw in e:
    line = raw.strip()
    if not line or line.startswith("#"):
        continue
    if "=" not in line:
        continue
    key = line.split("=", 1)[0].strip()
    if key:
        env_keys.add(key)
e.close()

missing = (example_keys - env_keys)

print("MISSING")
for k in missing:
    print(" " + k)

sys.exit(1 if missing else 0)