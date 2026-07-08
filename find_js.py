import re

with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "desk-item" in line.lower() or "gsap" in line.lower():
        if "desk-item" in line.lower():
            print(f"{i+1}: {line.strip()[:150]}")
