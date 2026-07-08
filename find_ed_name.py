import re

with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "ed-name" in line.lower() or "ed-tagline" in line.lower():
        print(f"{i+1}: {line.strip()[:150]}")
