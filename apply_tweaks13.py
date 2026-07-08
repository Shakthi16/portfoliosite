import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Move master folder to left: 22%
content = re.sub(
    r'(<!-- 16\. Interactive folder -->\s*<div class="floating-sticker"\s*style="top:\s*)42(%;\s*left:\s*)34(%;\s*z-index:\s*12;\s*transform:\s*rotate\(0deg\);\s*scale:\s*1\.1;">)',
    r'\g<1>45\g<2>22\g<3>',
    content
)

# 2. Move Pinterest card slightly right and up
# Currently top: 5%; right: 18%; -> let's make it top: 2%; right: 12%;
content = re.sub(
    r'(<!-- 4\. Design Journey Ticket.*?<div class="floating-sticker"\s*style="top:\s*)5(%;\s*right:\s*)18(%;\s*z-index:\s*8;\s*transform:\s*rotate\(2deg\);\s*scale:\s*0\.75;">)',
    r'\g<1>2\g<2>12\g<3>',
    content
)

# 3. Swap the pop-out logos to Figma, Kali, Linux with NO white background
# Item 1: Figma
icon1 = '''<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg" style="width: 45px; height: 45px; filter: drop-shadow(0 8px 12px rgba(0,0,0,0.3));" />'''
content = re.sub(
    r'<a href="#projects" class="sub-folder-item"[^>]*>.*?</div>',
    r'<a href="#projects" class="sub-folder-item" style="text-decoration: none;">\n            ' + icon1,
    content,
    flags=re.DOTALL
)

# Item 2: Kali Linux (Dragon)
icon2 = '''<img src="https://upload.wikimedia.org/wikipedia/commons/2/2b/Kali-dragon-icon.svg" style="width: 45px; height: 45px; filter: drop-shadow(0 8px 12px rgba(0,0,0,0.3));" />'''
content = re.sub(
    r'<a href="#about" class="sub-folder-item"[^>]*>.*?</div>',
    r'<a href="#about" class="sub-folder-item" style="text-decoration: none;">\n            ' + icon2,
    content,
    flags=re.DOTALL
)

# Item 3: Linux (Tux)
icon3 = '''<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" style="width: 45px; height: 45px; filter: drop-shadow(0 8px 12px rgba(0,0,0,0.3));" />'''
content = re.sub(
    r'<a href="#skills" class="sub-folder-item"[^>]*>.*?</div>',
    r'<a href="#skills" class="sub-folder-item" style="text-decoration: none;">\n            ' + icon3,
    content,
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updates applied: Folder and card moved, pop-out logos swapped to Figma/Kali/Linux with no background.")
