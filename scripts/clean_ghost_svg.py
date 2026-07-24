import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the hidden ghost SVG block that has duplicate old path IDs
content = re.sub(
    r'<!-- Cute Star Cluster SVG Template -->.*?</svg>',
    '',
    content,
    flags=re.DOTALL
)

# 2. Count remaining duplicates
print('path-0 count:', content.count('id="path-0"'))
print('dot-0-start count:', content.count('id="dot-0-start"'))
print('timeline-svg count:', content.count('id="timeline-svg"'))
print('seg-0 count:', content.count('id="seg-0"'))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
