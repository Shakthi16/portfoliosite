with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
pos_about = content.find('id="about"')
if pos_about != -1:
    sec_start = content.rfind('<section', 0, pos_about)
    sec_end = content.find('</section>', pos_about) + len('</section>')
    about_html = content[sec_start:sec_end]
    
    # Find all card elements or IDs
    ids = re.findall(r'id="([^"]+)"', about_html)
    print("IDs in #about:", ids)
