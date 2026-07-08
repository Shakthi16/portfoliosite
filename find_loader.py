import re

with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "loader" in line.lower() or "preloader" in line.lower():
        print(f"{i+1}: {line.strip()[:100]}")
