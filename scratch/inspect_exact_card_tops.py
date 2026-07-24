with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
items = re.findall(r'<div[^>]*class="[^"]*absolute[^"]*"[^>]*id="([^"]+)"[^>]*style="([^"]*)"', text)
if not items:
    items = re.findall(r'<div[^>]*id="([^"]+)"[^>]*class="[^"]*absolute[^"]*"', text)

pos_about = text.find('id="about"')
pos_about_end = text.find('</section>', pos_about)

about_sub = text[pos_about:pos_about_end]

cards = re.findall(r'id=["\'](node-[^"\']+|trigger-[^"\']+|text-[^"\']+)["\'][^>]*class=["\']([^"\']+)["\']', about_sub)
print("Card elements in #about:")
for c in cards:
    # Find style or top position
    p = about_sub.find(f'id="{c[0]}"')
    print(c[0], "-->", about_sub[p:p+120])
