with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r'contact', content, re.IGNORECASE)]
print("Found 'contact' matches:", len(matches))
for pos in matches[:5]:
    print("Pos:", pos)
    print(content[max(0, pos-100):min(len(content), pos+300)])
    print("="*40)
