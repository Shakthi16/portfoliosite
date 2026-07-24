with open('index.html', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'<section[^>]*id="([^"]+)"', html)
print("All section IDs in index.html in order:", matches)
