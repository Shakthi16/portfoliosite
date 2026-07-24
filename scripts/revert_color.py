import re

html_file = 'index.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace text colors with the deep purple (#421835)
content = re.sub(r'color:\s*#B14665', 'color: #421835', content, flags=re.IGNORECASE)
content = re.sub(r'text-\[#B14665\]', 'text-[#421835]', content, flags=re.IGNORECASE)

# Replace background and stroke/fill colors with the lighter mauve/purple (#a4768f)
content = re.sub(r'background:\s*#B14665', 'background: #a4768f', content, flags=re.IGNORECASE)
content = re.sub(r'bg-\[#B14665\]', 'bg-[#a4768f]', content, flags=re.IGNORECASE)
content = re.sub(r'stroke="#B14665"', 'stroke="#a4768f"', content, flags=re.IGNORECASE)
content = re.sub(r'fill="#B14665"', 'fill="#a4768f"', content, flags=re.IGNORECASE)
content = re.sub(r'background-color:\s*#B14665', 'background-color: #a4768f', content, flags=re.IGNORECASE)
content = re.sub(r'rgba\(177,\s*70,\s*101', 'rgba(66, 24, 53', content, flags=re.IGNORECASE)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Colors reverted successfully.")
