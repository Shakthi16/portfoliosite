import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix giant white box on home page by fixing position: relative to position: absolute on ID card sticker
content = content.replace(
    'style="top: 0%; left: 0%; z-index: 10; transform: rotate(-3deg); scale: 0.95; transform-origin: top left; width: 230px; position: relative;"',
    'style="position: absolute; top: 2%; left: 2%; z-index: 10; transform: rotate(-3deg); scale: 0.95; transform-origin: top left; width: 230px;"'
)

# 2. Reshape all 5 arrow curves so they route through OPEN SPACE without going over any text blocks
SEG_0_D = "M 290 440 C 290 560, 900 560, 1140 520"     # Hero bottom -> Hot-Pink Tape on Girl Card (1140, 520)
SEG_1_D = "M 1140 900 C 1140 1180, 500 1180, 210 980"   # Girl Card bottom -> Top of Orbital (210, 980) - passes BELOW text {02}
SEG_2_D = "M 210 1240 C 210 1320, 220 1360, 250 1380"  # Orbital bottom -> Cyan Tape on LinkedIn Card (250, 1380)
SEG_3_D = "M 250 1720 C 250 2020, 850 2020, 1150 1820" # LinkedIn bottom -> Amber Tape on GitHub Card (1150, 1820) - passes BELOW text {04}
SEG_4_D = "M 1150 2160 C 1150 2480, 650 2480, 250 2260"# GitHub bottom -> Purple Tape on SHAVIRA Card (250, 2260) - passes BELOW text {05}

content = re.sub(r'<path id="seg-0" class="journey-path" d="[^"]*"', f'<path id="seg-0" class="journey-path" d="{SEG_0_D}"', content)
content = re.sub(r'<path id="seg-1" class="journey-path" d="[^"]*"', f'<path id="seg-1" class="journey-path" d="{SEG_1_D}"', content)
content = re.sub(r'<path id="seg-2" class="journey-path" d="[^"]*"', f'<path id="seg-2" class="journey-path" d="{SEG_2_D}"', content)
content = re.sub(r'<path id="seg-3" class="journey-path" d="[^"]*"', f'<path id="seg-3" class="journey-path" d="{SEG_3_D}"', content)
content = re.sub(r'<path id="seg-4" class="journey-path" d="[^"]*"', f'<path id="seg-4" class="journey-path" d="{SEG_4_D}"', content)

# 3. Anchored End Dots directly on Washi Tape Clips
content = re.sub(r'<circle id="n0-end"[^>]*>', '<circle id="n0-end" class="journey-node" cx="1140" cy="520" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n1-end"[^>]*>', '<circle id="n1-end" class="journey-node" cx="210" cy="980" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n2-end"[^>]*>', '<circle id="n2-end" class="journey-node" cx="250" cy="1380" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n3-end"[^>]*>', '<circle id="n3-end" class="journey-node" cx="1150" cy="1820" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n4-end"[^>]*>', '<circle id="n4-end" class="journey-node" cx="250" cy="2260" r="5" fill="#8b2252" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully fixed ID card white box on home page and reshaped all arrow curves through open spaces!")
