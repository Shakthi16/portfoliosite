import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update seg-4 curve so it arches HIGH ABOVE {05} text exactly as shown in Image 1!
# GitHub bottom (1150, 2160) -> Arch UP over {05} text -> Top right dot of SHAVIRA card (420, 2220)
SEG_4_D = "M 1150 2160 C 1150 1980, 750 1980, 420 2220"

# seg-3: LinkedIn bottom -> Arch UP over {04} text -> Amber tape on GitHub (1150, 1820)
SEG_3_D = "M 250 1720 C 250 1620, 750 1620, 1150 1820"

content = re.sub(r'<path id="seg-3" class="journey-path" d="[^"]*"', f'<path id="seg-3" class="journey-path" d="{SEG_3_D}"', content)
content = re.sub(r'<path id="seg-4" class="journey-path" d="[^"]*"', f'<path id="seg-4" class="journey-path" d="{SEG_4_D}"', content)

# 2. Node End Dot n4-end anchored at (420, 2220) matching Image 1 exactly!
content = re.sub(r'<circle id="n4-end"[^>]*>', '<circle id="n4-end" class="journey-node" cx="420" cy="2220" r="5" fill="#8b2252" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated seg-4 to arch high above {05} text matching Image 1 exactly!")
