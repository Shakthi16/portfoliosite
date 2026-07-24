with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', text)
print("ALL SECTIONS IN INDEX.HTML:")
for idx, s in enumerate(sections):
    print(f" {idx+1}. {s}")

print("\nTotal file length:", len(text))
