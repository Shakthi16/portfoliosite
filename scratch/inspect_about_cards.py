with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

print("node-hero in index.html:", 'id="node-hero"' in text)
print("trigger-girl in index.html:", 'id="trigger-girl"' in text)
print("trigger-orbital in index.html:", 'id="trigger-orbital"' in text)
print("node-linkedin in index.html:", 'id="node-linkedin"' in text)
print("node-github in index.html:", 'id="node-github"' in text)
print("trigger-shavira in index.html:", 'id="trigger-shavira"' in text)

pos = text.find('id="about"')
if pos != -1:
    print("\nAbout section snippet (first 1000 chars):")
    print(text[pos:pos+1000])
