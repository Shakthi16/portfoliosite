import re

html_file = 'index.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# All the purples to replace
purples = [
    r'#421835', r'#a4768f', r'#5B2C4A', r'#d17697', 
    r'#7a3a5e', r'#2d1023', r'#4f2940', r'#c49eb3', 
    r'#582a4b', r'#a855f7'
]

# Create a combined regex pattern
pattern = re.compile('|'.join(purples), re.IGNORECASE)

# Replace all purples with Burgundy (#B14665)
content = pattern.sub('#B14665', content)

# Also fix any rgba values that were associated with purple
content = re.sub(r'rgba\(66,\s*24,\s*53', 'rgba(177, 70, 101', content, flags=re.IGNORECASE)
content = re.sub(r'rgba\(168,\s*85,\s*247', 'rgba(177, 70, 101', content, flags=re.IGNORECASE)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Burgundy globally.")
