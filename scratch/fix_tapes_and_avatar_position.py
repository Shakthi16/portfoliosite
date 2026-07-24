import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update SVG Container & viewBox to 2700px height (matching restored_about_section.html)
content = re.sub(r'viewBox="0 0 1400 \d+"', 'viewBox="0 0 1400 2700"', content)
content = re.sub(r'style="height: \d+px;"', 'style="height: 2700px;"', content)
content = re.sub(r'min-height: \d+px;', 'min-height: 2700px;', content)

# 2. Perfect Arrow Curves Connecting DIRECTLY to Washi Tapes on Top of Cards
SEG_0_D = "M 290 440 C 290 560, 900 560, 1140 520"     # Hero bottom -> Hot-Pink Tape on Girl Card (1140, 520)
SEG_1_D = "M 1140 900 C 1220 1200, 620 1220, 210 980"   # Girl Card bottom -> Top of Orbital (210, 980)
SEG_2_D = "M 210 1240 C 210 1320, 180 1360, 250 1380"  # Orbital bottom -> Cyan Tape on LinkedIn Card (250, 1380)
SEG_3_D = "M 250 1720 C 250 1980, 850 1980, 1150 1820" # LinkedIn bottom -> Amber Tape on GitHub Card (1150, 1820)
SEG_4_D = "M 1150 2160 C 1150 2420, 650 2420, 250 2260"# GitHub bottom -> Purple Tape on SHAVIRA Card (250, 2260)

content = re.sub(r'<path id="seg-0" class="journey-path" d="[^"]*"', f'<path id="seg-0" class="journey-path" d="{SEG_0_D}"', content)
content = re.sub(r'<path id="seg-1" class="journey-path" d="[^"]*"', f'<path id="seg-1" class="journey-path" d="{SEG_1_D}"', content)
content = re.sub(r'<path id="seg-2" class="journey-path" d="[^"]*"', f'<path id="seg-2" class="journey-path" d="{SEG_2_D}"', content)
content = re.sub(r'<path id="seg-3" class="journey-path" d="[^"]*"', f'<path id="seg-3" class="journey-path" d="{SEG_3_D}"', content)
content = re.sub(r'<path id="seg-4" class="journey-path" d="[^"]*"', f'<path id="seg-4" class="journey-path" d="{SEG_4_D}"', content)

# 3. Node End Dots Anchored Exactly on Washi Tape Clips
content = re.sub(r'<circle id="n0-end"[^>]*>', '<circle id="n0-end" class="journey-node" cx="1140" cy="520" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n1-end"[^>]*>', '<circle id="n1-end" class="journey-node" cx="210" cy="980" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n2-end"[^>]*>', '<circle id="n2-end" class="journey-node" cx="250" cy="1380" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n3-end"[^>]*>', '<circle id="n3-end" class="journey-node" cx="1150" cy="1820" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n4-end"[^>]*>', '<circle id="n4-end" class="journey-node" cx="250" cy="2260" r="5" fill="#8b2252" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)

# 4. Avatar position sitting ON TOP (above) the dashed line (translate(-50%, -85%))
AVATAR_ABOVE_LINE = """    <!-- TRAVELING FACE EMOJI STICKER ALONG ARROW PATHS -->
    <div id="path-traveler-avatar" class="absolute z-[80] pointer-events-none transition-transform duration-75" style="width: 110px; height: 110px; top: 0; left: 0; transform: translate(-50%, -85%); display: none;">
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
    content = content[:idx] + '\n\n' + AVATAR_ABOVE_LINE + content[idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully connected all arrows directly to the tape clips on top of cards and set face avatar to sit above line!")
