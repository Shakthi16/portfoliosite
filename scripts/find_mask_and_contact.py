with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
pos_mask = content.find('text-mask')
print("text-mask pos:", pos_mask)
if pos_mask != -1:
    print(content[pos_mask-200:pos_mask+600])

pos_shakti = content.find('SHAKTHI')
print("SHAKTHI pos:", pos_shakti)
while pos_shakti != -1:
    print("Match at", pos_shakti)
    print(content[max(0, pos_shakti-100):min(len(content), pos_shakti+200)])
    print("-" * 30)
    pos_shakti = content.find('SHAKTHI', pos_shakti+1)
