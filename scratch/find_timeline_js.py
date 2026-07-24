with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'.{0,100}timeline.{0,100}', text, re.IGNORECASE)
print(f"Found {len(matches)} matches for timeline:")
for m in matches[:15]:
    print("MATCH:", repr(m))
