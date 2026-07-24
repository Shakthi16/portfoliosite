with open('restored_about_section.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
nodes = re.findall(r'id=["\'](node-[^"\']+|trigger-[^"\']+|text-[^"\']+)["\']', text)
print(f"Nodes found in restored_about_section.html ({len(nodes)} total):")
for n in nodes:
    print(" -", n)
