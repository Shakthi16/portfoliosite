with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find #about section content
pos_about_start = text.find('<section', max(0, text.find('id="about"') - 200))
# Make sure we get the right section tag
# Find the section tag containing id="about"
for m in re.finditer(r'<section[^>]*>', text):
    if 'id="about"' in m.group():
        pos_about_tag_start = m.start()
        pos_about_tag_end = m.end()
        break

pos_about_section_end = text.find('</section>', pos_about_tag_start)

about_content = text[pos_about_tag_start:pos_about_section_end+10]
print("ABOUT section length:", len(about_content))
print("\nFirst 3000 chars of #about:")
print(about_content[:3000])
