with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Check open vs close section tags
open_sections = len(re.findall(r'<section', text))
close_sections = len(re.findall(r'</section>', text))

print(f"Open sections: {open_sections}, Close sections: {close_sections}")

# List all section IDs in order
sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', text)
print("\nSection IDs in index.html:")
for idx, s in enumerate(sections):
    print(f" {idx+1}. {s}")
