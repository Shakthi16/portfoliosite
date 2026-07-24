with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'timeline-scroll', text)]
print(f"Total occurrences of timeline-scroll: {len(matches)}")
for idx, pos in enumerate(matches):
    print(f"--- OCCURRENCE {idx} ---")
    print(text[max(0, pos-40):min(len(text), pos+150)])
