import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Exact Bezier Curves Matching User's Image 1 & Image 2

# seg-0: Hero Card bottom -> Girl Card top pink tape
SEG_0_D = "M 290 360 C 290 540, 900 540, 1140 520"

# seg-1: Girl Card bottom -> Central Orbital right edge (sweeps below text {02})
SEG_1_D = "M 1140 900 C 1220 1250, 620 1280, 340 1110"

# seg-2: Central Orbital left edge -> LinkedIn Card top
SEG_2_D = "M 80 1110 C 10 1220, 100 1320, 250 1380"

# seg-3: LinkedIn Card bottom -> GitHub Card top (arches ABOVE text {04})
SEG_3_D = "M 250 1720 C 250 1920, 750 1920, 1040 2020"

# seg-4: GitHub Card bottom -> SHAVIRA Card top-right dot (arches HIGH ABOVE text {05} exactly as in Image 1!)
SEG_4_D = "M 1150 2360 C 1150 2020, 750 2020, 420 2220"

content = re.sub(r'<path id="seg-0" class="journey-path" d="[^"]*"', f'<path id="seg-0" class="journey-path" d="{SEG_0_D}"', content)
content = re.sub(r'<path id="seg-1" class="journey-path" d="[^"]*"', f'<path id="seg-1" class="journey-path" d="{SEG_1_D}"', content)
content = re.sub(r'<path id="seg-2" class="journey-path" d="[^"]*"', f'<path id="seg-2" class="journey-path" d="{SEG_2_D}"', content)
content = re.sub(r'<path id="seg-3" class="journey-path" d="[^"]*"', f'<path id="seg-3" class="journey-path" d="{SEG_3_D}"', content)
content = re.sub(r'<path id="seg-4" class="journey-path" d="[^"]*"', f'<path id="seg-4" class="journey-path" d="{SEG_4_D}"', content)

# Node End Dots matching exact curve endpoints
content = re.sub(r'<circle id="n0-end"[^>]*>', '<circle id="n0-end" class="journey-node" cx="1140" cy="520" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n1-end"[^>]*>', '<circle id="n1-end" class="journey-node" cx="340" cy="1110" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n2-end"[^>]*>', '<circle id="n2-end" class="journey-node" cx="250" cy="1380" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n3-end"[^>]*>', '<circle id="n3-end" class="journey-node" cx="1040" cy="2020" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n4-end"[^>]*>', '<circle id="n4-end" class="journey-node" cx="420" cy="2220" r="5" fill="#8b2252" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated seg-3 to arch above text {04} and seg-4 to arch high above text {05} matching Image 1!")
