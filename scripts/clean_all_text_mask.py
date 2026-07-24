with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Remove any remaining <section ... id="text-mask-section"> blocks
content = re.sub(r'<section[^>]*id="text-mask-section"[^>]*>.*?</section>', '', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Remaining 'text-mask-section' in HTML elements?", '<section' in content and 'id="text-mask-section"' in content)
