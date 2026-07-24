with open('git_version.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos_about = text.find('id="about"')
pos_about_end = text.find('</section>', pos_about) + len('</section>')

git_about_html = text[pos_about-100:pos_about_end]

import re
nodes = re.findall(r'<div[^>]*id=["\'](node-[^"\']+|trigger-[^"\']+|text-[^"\']+)["\'][^>]*>', git_about_html)
print(f"Nodes found in git_version.html #about ({len(nodes)} total):")
for n in nodes:
    print(" -", n)
