with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

paths = re.findall(r'<path id="seg-\d"[^>]*>', text)
print("Found SVG Arrow Paths:")
for p in paths:
    print(" -", p)

print("\nMarker definition present:", '<marker id="arrow-tip"' in text)
print("Journey path CSS style present:", '.journey-path' in text)
print("Traveling avatar present:", 'id="path-traveler-avatar"' in text)
