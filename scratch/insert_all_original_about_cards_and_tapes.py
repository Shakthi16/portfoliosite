import re

with open('restored_about_section.html', 'r', encoding='utf-8') as f:
    restored_about = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    index_text = f.read()

# Make sure timeline-container has class block so desktop cards render on all viewports
restored_about = restored_about.replace(
    'class="relative w-full max-w-[1400px] mx-auto px-6 lg:px-12 z-10 hidden md:block"',
    'class="relative w-full max-w-[1400px] mx-auto px-6 lg:px-12 z-10 block"'
)

# Set exact arrow paths connecting directly to the top tape clips of each card:
SEG_0_D = "M 290 440 C 290 560, 900 560, 1140 520"     # Hero bottom -> Hot-Pink Tape on Girl Card (1140, 520)
SEG_1_D = "M 1140 900 C 1220 1200, 620 1220, 210 980"   # Girl Card bottom -> Top of Orbital (210, 980)
SEG_2_D = "M 210 1240 C 210 1320, 180 1360, 250 1380"  # Orbital bottom -> Cyan Tape on LinkedIn Card (250, 1380)
SEG_3_D = "M 250 1720 C 250 1980, 850 1980, 1150 1820" # LinkedIn bottom -> Amber Tape on GitHub Card (1150, 1820)
SEG_4_D = "M 1150 2160 C 1150 2420, 650 2420, 250 2260"# GitHub bottom -> Purple Tape on SHAVIRA Card (250, 2260)

restored_about = re.sub(r'<path id="seg-0" class="journey-path" d="[^"]*"', f'<path id="seg-0" class="journey-path" d="{SEG_0_D}"', restored_about)
restored_about = re.sub(r'<path id="seg-1" class="journey-path" d="[^"]*"', f'<path id="seg-1" class="journey-path" d="{SEG_1_D}"', restored_about)
restored_about = re.sub(r'<path id="seg-2" class="journey-path" d="[^"]*"', f'<path id="seg-2" class="journey-path" d="{SEG_2_D}"', restored_about)
restored_about = re.sub(r'<path id="seg-3" class="journey-path" d="[^"]*"', f'<path id="seg-3" class="journey-path" d="{SEG_3_D}"', restored_about)
restored_about = re.sub(r'<path id="seg-4" class="journey-path" d="[^"]*"', f'<path id="seg-4" class="journey-path" d="{SEG_4_D}"', restored_about)

# End node dots on top of washi tape clips:
restored_about = re.sub(r'<circle id="n0-end"[^>]*>', '<circle id="n0-end" class="journey-node" cx="1140" cy="520" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', restored_about)
restored_about = re.sub(r'<circle id="n1-end"[^>]*>', '<circle id="n1-end" class="journey-node" cx="210" cy="980" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', restored_about)
restored_about = re.sub(r'<circle id="n2-end"[^>]*>', '<circle id="n2-end" class="journey-node" cx="250" cy="1380" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', restored_about)
restored_about = re.sub(r'<circle id="n3-end"[^>]*>', '<circle id="n3-end" class="journey-node" cx="1150" cy="1820" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', restored_about)
restored_about = re.sub(r'<circle id="n4-end"[^>]*>', '<circle id="n4-end" class="journey-node" cx="250" cy="2260" r="5" fill="#8b2252" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', restored_about)

# Traveler avatar riding ABOVE the dashed line (translate(-50%, -85%))
AVATAR_ABOVE_LINE = """    <!-- TRAVELING FACE EMOJI STICKER ALONG ARROW PATHS -->
    <div id="path-traveler-avatar" class="absolute z-[80] pointer-events-none transition-transform duration-75" style="width: 110px; height: 110px; top: 0; left: 0; transform: translate(-50%, -85%); display: none;">
      <div class="relative w-full h-full flex items-center justify-center">
        <!-- Face Emoji Sticker with crisp white border outline -->
        <img src="face.png" alt="Traveling Avatar" class="w-full h-full object-contain" style="filter: drop-shadow(1.8px 0 0 #ffffff) drop-shadow(-1.8px 0 0 #ffffff) drop-shadow(0 1.8px 0 #ffffff) drop-shadow(0 -1.8px 0 #ffffff) drop-shadow(0 6px 14px rgba(0,0,0,0.18));"/>
      </div>
    </div>"""

svg_end = restored_about.find('</svg>', restored_about.find('id="timeline-svg"'))
if svg_end != -1:
    idx = svg_end + len('</svg>')
    restored_about = restored_about[:idx] + '\n\n' + AVATAR_ABOVE_LINE + restored_about[idx:]

# Find section id="about" in index_text and replace cleanly
pos_about_start = index_text.find('<section', index_text.find('id="about"') - 200)
pos_about_end = index_text.find('</section>', index_text.find('id="about"')) + len('</section>')

index_text = index_text[:pos_about_start] + restored_about.strip() + index_text[pos_about_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_text)

print("Successfully replaced section id='about' with ALL original cards, tape clip anchors, and avatar above line!")
