with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'id=["\'](node-hero|text-hero|trigger-girl|trigger-orbital|text-premium|node-linkedin|text-linkedin|node-github|text-github|trigger-shavira|trigger-crafting)["\']', text)

for m in matches:
    pos = m.start()
    print(text[pos-40:pos+150])
    print("-" * 50)
