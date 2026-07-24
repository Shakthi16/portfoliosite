import re

with open('restored_about_section.html', 'r', encoding='utf-8') as f:
    about_html = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    index_text = f.read()

# 1. Update #timeline-container display to 'block'
about_html = about_html.replace(
    'class="relative w-full max-w-[1400px] mx-auto px-6 lg:px-12 z-10 hidden md:block"',
    'class="relative w-full max-w-[1400px] mx-auto px-6 lg:px-12 z-10 block"'
)

# 2. Perfect Curve Paths Routing Deep Below All Text Blocks
SEG_0_D = "M 290 360 C 290 540, 900 540, 1140 520"
SEG_1_D = "M 1140 900 C 1220 1280, 620 1300, 340 1110"
SEG_2_D = "M 80 1110 C 10 1220, 100 1320, 250 1380"
SEG_3_D = "M 250 1720 C 250 1960, 850 1980, 1140 1820"
SEG_4_D = "M 1140 2160 C 1140 2480, 600 2520, 250 2260"

about_html = re.sub(r'<path id="seg-0" class="journey-path" d="[^"]*"', f'<path id="seg-0" class="journey-path" d="{SEG_0_D}"', about_html)
about_html = re.sub(r'<path id="seg-1" class="journey-path" d="[^"]*"', f'<path id="seg-1" class="journey-path" d="{SEG_1_D}"', about_html)
about_html = re.sub(r'<path id="seg-2" class="journey-path" d="[^"]*"', f'<path id="seg-2" class="journey-path" d="{SEG_2_D}"', about_html)
about_html = re.sub(r'<path id="seg-3" class="journey-path" d="[^"]*"', f'<path id="seg-3" class="journey-path" d="{SEG_3_D}"', about_html)
about_html = re.sub(r'<path id="seg-4" class="journey-path" d="[^"]*"', f'<path id="seg-4" class="journey-path" d="{SEG_4_D}"', about_html)

# Node End Dots
about_html = re.sub(r'<circle id="n0-end"[^>]*>', '<circle id="n0-end" class="journey-node" cx="1140" cy="520" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', about_html)
about_html = re.sub(r'<circle id="n1-end"[^>]*>', '<circle id="n1-end" class="journey-node" cx="340" cy="1110" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', about_html)
about_html = re.sub(r'<circle id="n2-end"[^>]*>', '<circle id="n2-end" class="journey-node" cx="250" cy="1380" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', about_html)
about_html = re.sub(r'<circle id="n3-end"[^>]*>', '<circle id="n3-end" class="journey-node" cx="1140" cy="1820" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', about_html)
about_html = re.sub(r'<circle id="n4-end"[^>]*>', '<circle id="n4-end" class="journey-node" cx="250" cy="2260" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', about_html)

# 3. Clean 110px Sticker Avatar (No Motion Dashes)
AVATAR_CLEAN = """    <!-- TRAVELING FACE EMOJI STICKER ALONG ARROW PATHS -->
    <div id="path-traveler-avatar" class="absolute z-[80] pointer-events-none transition-transform duration-75" style="width: 110px; height: 110px; top: 0; left: 0; transform: translate(-50%, -50%); display: none;">
      <div class="relative w-full h-full flex items-center justify-center">
        <!-- Face Emoji Sticker with crisp white border outline -->
        <img src="face.png" alt="Traveling Avatar" class="w-full h-full object-contain" style="filter: drop-shadow(1.8px 0 0 #ffffff) drop-shadow(-1.8px 0 0 #ffffff) drop-shadow(0 1.8px 0 #ffffff) drop-shadow(0 -1.8px 0 #ffffff) drop-shadow(0 6px 14px rgba(0,0,0,0.18));"/>
      </div>
    </div>"""

svg_end = about_html.find('</svg>', about_html.find('id="timeline-svg"'))
if svg_end != -1:
    idx = svg_end + len('</svg>')
    about_html = about_html[:idx] + '\n\n' + AVATAR_CLEAN + about_html[idx:]

# 4. Clean Replacement of section id="about" in index_text
pos_about_start = index_text.find('<section', index_text.find('id="about"') - 200)
pos_about_end = index_text.find('</section>', index_text.find('id="about"')) + len('</section>')

index_text = index_text[:pos_about_start] + about_html.strip() + index_text[pos_about_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_text)

print("Successfully replaced section id='about' cleanly with all 11 cards and deep curve clearance below text!")
