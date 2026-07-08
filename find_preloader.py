import re

with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "preloader" in line.lower() or "loading" in line.lower():
        print(f"{i+1}: {line.strip()[:150]}")
