with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'timeline-pin-section|timeline-scroll', text)]
for idx, pos in enumerate(matches):
    print(f"--- MATCH {idx} ---")
    print(text[max(0, pos-100):min(len(text), pos+300)])
