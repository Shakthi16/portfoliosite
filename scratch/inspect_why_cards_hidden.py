with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_about = text.find('id="about"')
pos_about_end = text.find('</section>', pos_about) + len('</section>')

about_html = text[pos_about-100:pos_about_end]

print(f"About section length: {len(about_html)} chars")

import re
nodes = re.findall(r'<div[^>]*id=["\'](node-[^"\']+|trigger-[^"\']+|text-[^"\']+)["\'][^>]*>', about_html)
print("Nodes found inside #about:")
for n in nodes:
    print(" -", n)
