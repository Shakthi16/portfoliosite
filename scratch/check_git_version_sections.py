with open('git_version.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', text)
print("Sections in git_version.html:")
for idx, s in enumerate(sections):
    print(f" {idx+1}. {s}")
