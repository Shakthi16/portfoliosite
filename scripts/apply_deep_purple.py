import re

html_file = 'index.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all burgundy (#B14665) with deep purple (#421835)
content = re.sub(r'#B14665', '#421835', content, flags=re.IGNORECASE)

# Replace all rgb values of burgundy with rgb of deep purple
content = re.sub(r'rgba\(177,\s*70,\s*101', 'rgba(66, 24, 53', content, flags=re.IGNORECASE)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied deep purple (#421835) globally.")
