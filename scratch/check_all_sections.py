with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', text)
print("Sections in index.html:")
for s in sections:
    print(" -", s)
