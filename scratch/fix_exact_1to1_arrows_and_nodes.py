import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update SVG viewBox and container height to 2950 for 1:1 exact alignment
content = re.sub(r'viewBox="0 0 1400 \d+"', 'viewBox="0 0 1400 2950"', content)
content = re.sub(r'style="height: \d+px;"', 'style="height: 2950px;"', content)
content = re.sub(r'min-height: \d+px;', 'min-height: 2950px;', content)

# 2. Exact 1:1 SVG Paths & End Node Dots
SEG_0_D = "M 290 360 C 290 540, 900 540, 1140 520"   # Hero bottom (290,360) -> Girl top (1140,520)
SEG_1_D = "M 1140 900 C 1220 1250, 620 1280, 340 1110" # Girl bottom (1140,900) -> Orbital right (340,1110)
SEG_2_D = "M 80 1110 C 10 1220, 100 1320, 250 1540"    # Orbital left (80,1110) -> LinkedIn top cyan tape (250,1540)
SEG_3_D = "M 250 1880 C 250 1960, 850 1960, 1140 2020" # LinkedIn bottom (250,1880) -> GitHub top amber tape (1140,2020) - arches ABOVE text {04}!
SEG_4_D = "M 1140 2360 C 1140 2440, 650 2440, 250 2500"# GitHub bottom (1140,2360) -> SHAVIRA top purple tape (250,2500) - arches ABOVE text {05}!

content = re.sub(r'<path id="seg-0" class="journey-path" d="[^"]*"', f'<path id="seg-0" class="journey-path" d="{SEG_0_D}"', content)
content = re.sub(r'<path id="seg-1" class="journey-path" d="[^"]*"', f'<path id="seg-1" class="journey-path" d="{SEG_1_D}"', content)
content = re.sub(r'<path id="seg-2" class="journey-path" d="[^"]*"', f'<path id="seg-2" class="journey-path" d="{SEG_2_D}"', content)
content = re.sub(r'<path id="seg-3" class="journey-path" d="[^"]*"', f'<path id="seg-3" class="journey-path" d="{SEG_3_D}"', content)
content = re.sub(r'<path id="seg-4" class="journey-path" d="[^"]*"', f'<path id="seg-4" class="journey-path" d="{SEG_4_D}"', content)

# Node End Dots anchored on washi tape clips
content = re.sub(r'<circle id="n0-end"[^>]*>', '<circle id="n0-end" class="journey-node" cx="1140" cy="520" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n1-end"[^>]*>', '<circle id="n1-end" class="journey-node" cx="340" cy="1110" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n2-end"[^>]*>', '<circle id="n2-end" class="journey-node" cx="250" cy="1540" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n3-end"[^>]*>', '<circle id="n3-end" class="journey-node" cx="1140" cy="2020" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n4-end"[^>]*>', '<circle id="n4-end" class="journey-node" cx="250" cy="2500" r="5" fill="#8b2252" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)

# 3. Clean 110px Sticker Avatar (No Motion Dashes)
AVATAR_CLEAN = """    <!-- TRAVELING FACE EMOJI STICKER ALONG ARROW PATHS -->
    <div id="path-traveler-avatar" class="absolute z-[80] pointer-events-none transition-transform duration-75" style="width: 110px; height: 110px; top: 0; left: 0; transform: translate(-50%, -50%); display: none;">
      <div class="relative w-full h-full flex items-center justify-center">
        <!-- Face Emoji Sticker with crisp white border outline -->
        <img src="face.png" alt="Traveling Avatar" class="w-full h-full object-contain" style="filter: drop-shadow(1.8px 0 0 #ffffff) drop-shadow(-1.8px 0 0 #ffffff) drop-shadow(0 1.8px 0 #ffffff) drop-shadow(0 -1.8px 0 #ffffff) drop-shadow(0 6px 14px rgba(0,0,0,0.18));"/>
      </div>
    </div>"""

content = re.sub(r'<!-- TRAVELING FACE EMOJI STICKER ALONG ARROW PATHS -->.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
content = re.sub(r'<div id="path-traveler-avatar"[^>]*>.*?</div>\s*</div>', '', content, flags=re.DOTALL)

svg_end = content.find('</svg>', content.find('id="timeline-svg"'))
if svg_end != -1:
    idx = svg_end + len('</svg>')
    content = content[:idx] + '\n\n' + AVATAR_CLEAN + content[idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully aligned 1:1 coordinates for all cards, washi tape end nodes, and curve clearances!")
