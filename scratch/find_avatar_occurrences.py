with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'path-traveler-avatar', text)]
print(f"Found {len(matches)} occurrences of path-traveler-avatar")
for idx, pos in enumerate(matches):
    print(f"--- OCCURRENCE {idx} ---")
    print(text[max(0, pos-50):min(len(text), pos+300)])
