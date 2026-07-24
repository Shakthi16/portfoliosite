with open('E:\\portfoliosite\\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Let's check for any duplicate id attributes in the HTML tags
ids = re.findall(r'id="([^"]+)"', content)
from collections import Counter
id_counts = Counter(ids)
duplicates = {k: v for k, v in id_counts.items() if v > 1}
print("Duplicate IDs in HTML:")
for k, v in duplicates.items():
    print(f"ID '{k}' occurs {v} times.")

# Let's check for sections
sections = re.findall(r'<section\s+[^>]*id="([^"]+)"', content)
print("\nSections in HTML:")
for s in sections:
    print(f"- {s}")
