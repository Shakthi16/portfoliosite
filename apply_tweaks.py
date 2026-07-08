import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Increase interactive folder size
content = re.sub(
    r'(<!-- 16\. Interactive folder -->\s*<div class="floating-sticker"\s*style="[^"]*?)scale:\s*0\.7;',
    r'\g<1>scale: 1.1;',
    content, count=1
)

# 2. Change interactive folder to blue
content = re.sub(r'<stop offset="0%" stop-color="#9e5684" />', r'<stop offset="0%" stop-color="#60a5fa" />', content)
content = re.sub(r'<stop offset="100%" stop-color="#7a3a5e" />', r'<stop offset="100%" stop-color="#3b82f6" />', content)
content = re.sub(r'<stop offset="0%" stop-color="#7a3a5e" />', r'<stop offset="0%" stop-color="#3b82f6" />', content)
content = re.sub(r'<stop offset="100%" stop-color="#421835" />', r'<stop offset="100%" stop-color="#1d4ed8" />', content)

# 3. Move Tech Stack right
content = re.sub(
    r'(<!-- 12\. Tech Stack Grid.*?)right:\s*28%;',
    r'\g<1>right: 15%;',
    content, flags=re.DOTALL, count=1
)

# 4. Change the font of the roles line
content = re.sub(
    r"font-family:\s*'Outfit',\s*sans-serif\s*!important;\s*font-size:\s*11px;\s*font-weight:\s*500;",
    r"font-family: 'Manrope', sans-serif !important; font-size: 10px; font-weight: 600;",
    content
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updates applied: folder size, folder color, tech stack position, roles font.")
