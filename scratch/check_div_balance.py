with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Split by section
sections = re.split(r'(<section[^>]*>)', text)
for i in range(1, len(sections), 2):
    sec_tag = sections[i]
    sec_content = sections[i+1]
    sec_id_match = re.search(r'id=["\']([^"\']+)["\']', sec_tag)
    sec_id = sec_id_match.group(1) if sec_id_match else "unknown"
    
    # Count <div and </div>
    open_divs = len(re.findall(r'<div[\s>]', sec_content))
    close_divs = len(re.findall(r'</div>', sec_content))
    
    print(f"Section #{sec_id:<25} Open <div>: {open_divs:<4} Close </div>: {close_divs:<4} Difference: {open_divs - close_divs}")
