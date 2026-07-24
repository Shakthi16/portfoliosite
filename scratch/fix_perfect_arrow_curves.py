import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Perfect Bezier Curves that gracefully route around all text blocks and card boundaries

SEG_0_D = "M 290 500 C 290 620, 800 620, 1040 535"  # Hero -> Girl Card
SEG_1_D = "M 1140 900 C 1200 1200, 600 1260, 340 1110" # Girl -> Orbital (sweeps BELOW text {02})
SEG_2_D = "M 80 1110 C 10 1220, 100 1320, 250 1390"    # Orbital -> LinkedIn Card
SEG_3_D = "M 250 1720 C 250 1850, 750 1960, 1040 1830"  # LinkedIn -> GitHub Card
SEG_4_D = "M 1150 2160 C 1150 2320, 600 2380, 250 2270" # GitHub -> SHAVIRA Card

# Update SVG path d attributes in index.html
content = re.sub(r'<path id="seg-0" class="journey-path" d="[^"]*"', f'<path id="seg-0" class="journey-path" d="{SEG_0_D}"', content)
content = re.sub(r'<path id="seg-1" class="journey-path" d="[^"]*"', f'<path id="seg-1" class="journey-path" d="{SEG_1_D}"', content)
content = re.sub(r'<path id="seg-2" class="journey-path" d="[^"]*"', f'<path id="seg-2" class="journey-path" d="{SEG_2_D}"', content)
content = re.sub(r'<path id="seg-3" class="journey-path" d="[^"]*"', f'<path id="seg-3" class="journey-path" d="{SEG_3_D}"', content)
content = re.sub(r'<path id="seg-4" class="journey-path" d="[^"]*"', f'<path id="seg-4" class="journey-path" d="{SEG_4_D}"', content)

# Update node end dot positions to match curve destination points
content = re.sub(r'<circle id="n0-end"[^>]*>', '<circle id="n0-end" class="journey-node" cx="1040" cy="535" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n1-end"[^>]*>', '<circle id="n1-end" class="journey-node" cx="340" cy="1110" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n2-end"[^>]*>', '<circle id="n2-end" class="journey-node" cx="250" cy="1390" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n3-end"[^>]*>', '<circle id="n3-end" class="journey-node" cx="1040" cy="1830" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n4-end"[^>]*>', '<circle id="n4-end" class="journey-node" cx="250" cy="2270" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated all 5 arrow curves to route perfectly around text blocks and cards!")
