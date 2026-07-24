import re

with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "desk-loader" in line.lower() or "desk_loader" in line.lower() or "loader-terminal" in line.lower() or "desk-item" in line.lower():
        print(f"{i+1}: {line.strip()[:150]}")
