with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
scripts = re.findall(r'<script>(.*?)</script>', text, re.DOTALL)
print(f"Found {len(scripts)} inline script blocks.")
for idx, s in enumerate(scripts):
    print(f"\n--- SCRIPT BLOCK {idx} ({len(s)} chars) ---")
    lines = s.strip().split('\n')
    print('\n'.join(lines[:10]))
    if len(lines) > 10:
        print(f"... [{len(lines)-10} more lines]")
