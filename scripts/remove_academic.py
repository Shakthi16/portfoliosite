import re

html_file = 'index.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<!-- 4\. ACADEMIC BACKGROUND -->.*?<div class="cinematic-divider my-20"></div>'

# Re.DOTALL allows . to match newlines
content = re.sub(pattern, '', content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed Academic Background section.")
