import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Space out the subfolders much further
# Folder 1: translate(-75px, -70px) -> translate(-120px, -60px)
content = re.sub(
    r'transform:\s*scale\(1\)\s*translate\(-75px,\s*-70px\);',
    r'transform: scale(1) translate(-120px, -40px);',
    content
)

# Folder 2: translate(-25px, -95px) -> translate(0px, -120px)
content = re.sub(
    r'transform:\s*scale\(1\)\s*translate\(-25px,\s*-95px\);',
    r'transform: scale(1) translate(0px, -120px);',
    content
)

# Folder 3: translate(25px, -95px) -> translate(120px, -60px)
content = re.sub(
    r'transform:\s*scale\(1\)\s*translate\(25px,\s*-95px\);',
    r'transform: scale(1) translate(120px, -40px);',
    content
)

# And remove the rotation on the main wrapper so everything is straight and readable
content = re.sub(
    r'(<!-- 16\. Interactive folder -->\s*<div class="floating-sticker"\s*style="top: 35%; left: 26%; z-index: 12;) transform: rotate\(-3deg\);',
    r'\g<1> transform: rotate(0deg);',
    content
)

# Also ensure sub-folder-label sits right below the icon with some space
content = re.sub(
    r'margin-top:\s*6px;',
    r'margin-top: 12px;',
    content
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updates applied: Folders fanned out wider, main folder un-rotated, labels spaced out.")
