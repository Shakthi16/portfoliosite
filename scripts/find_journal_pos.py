with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = re.findall(r'<section[^>]*>', content)
print("Sections found:", len(matches))
for m in matches[:10]:
    print(m)

# Find where journal or about is
pos = content.find('journal')
print("'journal' pos:", pos)

pos_about = content.find('id="about"')
print("'id=\"about\"' pos:", pos_about)

pos_smriti = content.find('smriti-book')
print("'smriti-book' pos:", pos_smriti)
