with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_about = text.find('id="about"')
pos_about_end = text.find('</section>', pos_about) + len('</section>')

about_html = text[pos_about-100:pos_about_end]

import re

# Find all div elements with id
divs = re.findall(r'<div[^>]*id=["\']([^"\']+)["\'][^>]*>', about_html)
print("All divs with ID inside #about:")
for d in divs:
    print(" -", d)

# Check if node-hero HTML is present
if 'node-hero' in about_html:
    pos_nh = about_html.find('node-hero')
    print("\nnode-hero snippet:")
    print(about_html[pos_nh-50:pos_nh+400])
else:
    print("\nnode-hero NOT FOUND in #about!")
