import re

# Load complete uncorrupted about section HTML from restored_about_section.html
with open('restored_about_section.html', 'r', encoding='utf-8') as f:
    about_section_html = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# 1. Update #timeline-container in about_section_html to be 'block' (NOT 'hidden md:block')
about_section_html = about_section_html.replace(
    'class="relative w-full max-w-[1400px] mx-auto px-6 lg:px-12 z-10 hidden md:block"',
    'class="relative w-full max-w-[1400px] mx-auto px-6 lg:px-12 z-10 block"'
)

# 2. Ensure SVG path d attributes start attached to Hero Card bottom (290, 360) and top of Girl Card (1140, 520)
SEG_0_D = "M 290 360 C 290 540, 900 540, 1140 520"
SEG_1_D = "M 1140 900 C 1220 1220, 620 1260, 340 1110"
SEG_2_D = "M 80 1110 C 10 1220, 100 1320, 250 1380"
SEG_3_D = "M 250 1720 C 250 1850, 850 1960, 1140 1820"
SEG_4_D = "M 1140 2160 C 1140 2320, 600 2380, 250 2260"

about_section_html = re.sub(r'<path id="seg-0" class="journey-path" d="[^"]*"', f'<path id="seg-0" class="journey-path" d="{SEG_0_D}"', about_section_html)
about_section_html = re.sub(r'<path id="seg-1" class="journey-path" d="[^"]*"', f'<path id="seg-1" class="journey-path" d="{SEG_1_D}"', about_section_html)
about_section_html = re.sub(r'<path id="seg-2" class="journey-path" d="[^"]*"', f'<path id="seg-2" class="journey-path" d="{SEG_2_D}"', about_section_html)
about_section_html = re.sub(r'<path id="seg-3" class="journey-path" d="[^"]*"', f'<path id="seg-3" class="journey-path" d="{SEG_3_D}"', about_section_html)
about_section_html = re.sub(r'<path id="seg-4" class="journey-path" d="[^"]*"', f'<path id="seg-4" class="journey-path" d="{SEG_4_D}"', about_section_html)

# Node end dots
about_section_html = re.sub(r'<circle id="n0-end"[^>]*>', '<circle id="n0-end" class="journey-node" cx="1140" cy="520" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', about_section_html)
about_section_html = re.sub(r'<circle id="n1-end"[^>]*>', '<circle id="n1-end" class="journey-node" cx="340" cy="1110" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', about_section_html)
about_section_html = re.sub(r'<circle id="n2-end"[^>]*>', '<circle id="n2-end" class="journey-node" cx="250" cy="1380" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', about_section_html)
about_section_html = re.sub(r'<circle id="n3-end"[^>]*>', '<circle id="n3-end" class="journey-node" cx="1140" cy="1820" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', about_section_html)
about_section_html = re.sub(r'<circle id="n4-end"[^>]*>', '<circle id="n4-end" class="journey-node" cx="250" cy="2260" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', about_section_html)

# 3. Add 110px Prominent Face Sticker Avatar element inside about_section_html right after </svg>
STICKER_AVATAR = """    <!-- TRAVELING FACE EMOJI STICKER ALONG ARROW PATHS -->
    <div id="path-traveler-avatar" class="absolute z-[80] pointer-events-none transition-transform duration-75" style="width: 110px; height: 110px; top: 0; left: 0; transform: translate(-50%, -50%); display: none;">
      <div class="relative w-full h-full flex items-center justify-center">
        <!-- Speed Dash Motion Trail -->
        <div class="absolute -left-5 top-1/2 -translate-y-1/2 flex flex-col gap-1.5 opacity-80 pointer-events-none">
          <div class="w-5 h-0.5 bg-gray-500/80 rounded-full"></div>
          <div class="w-3 h-0.5 bg-gray-500/80 rounded-full ml-1"></div>
          <div class="w-5 h-0.5 bg-gray-500/80 rounded-full"></div>
        </div>
        <!-- Face Emoji Sticker with crisp white sticker border outline -->
        <img src="face.png" alt="Traveling Avatar" class="w-full h-full object-contain" style="filter: drop-shadow(1.8px 0 0 #ffffff) drop-shadow(-1.8px 0 0 #ffffff) drop-shadow(0 1.8px 0 #ffffff) drop-shadow(0 -1.8px 0 #ffffff) drop-shadow(0 6px 14px rgba(0,0,0,0.18));"/>
      </div>
    </div>"""

svg_end = about_section_html.find('</svg>', about_section_html.find('id="timeline-svg"'))
if svg_end != -1:
    idx = svg_end + len('</svg>')
    about_section_html = about_section_html[:idx] + '\n\n' + STICKER_AVATAR + about_section_html[idx:]

# 4. Replace section id="about" in index_content
pos_about = index_content.find('id="about"')
if pos_about != -1:
    sec_start = index_content.rfind('<section', 0, pos_about)
    sec_end = index_content.find('</section>', pos_about) + len('</section>')
    index_content = index_content[:sec_start] + about_section_html.strip() + index_content[sec_end:]
    print("Successfully replaced #about section with full uncorrupted HTML containing all 11 cards & text nodes!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Insertion complete!")
