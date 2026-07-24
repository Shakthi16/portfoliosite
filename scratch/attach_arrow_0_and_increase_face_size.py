import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Attach seg-0 directly to bottom of Hero Card (290, 360) and top of Girl Card (1140, 520)
SEG_0_D = "M 290 360 C 290 540, 900 540, 1140 520"
SEG_1_D = "M 1140 900 C 1220 1220, 620 1260, 340 1110"
SEG_2_D = "M 80 1110 C 10 1220, 100 1320, 250 1380"
SEG_3_D = "M 250 1720 C 250 1850, 850 1960, 1140 1820"
SEG_4_D = "M 1140 2160 C 1140 2320, 600 2380, 250 2260"

content = re.sub(r'<path id="seg-0" class="journey-path" d="[^"]*"', f'<path id="seg-0" class="journey-path" d="{SEG_0_D}"', content)
content = re.sub(r'<path id="seg-1" class="journey-path" d="[^"]*"', f'<path id="seg-1" class="journey-path" d="{SEG_1_D}"', content)
content = re.sub(r'<path id="seg-2" class="journey-path" d="[^"]*"', f'<path id="seg-2" class="journey-path" d="{SEG_2_D}"', content)
content = re.sub(r'<path id="seg-3" class="journey-path" d="[^"]*"', f'<path id="seg-3" class="journey-path" d="{SEG_3_D}"', content)
content = re.sub(r'<path id="seg-4" class="journey-path" d="[^"]*"', f'<path id="seg-4" class="journey-path" d="{SEG_4_D}"', content)

# Node end dots
content = re.sub(r'<circle id="n0-end"[^>]*>', '<circle id="n0-end" class="journey-node" cx="1140" cy="520" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n1-end"[^>]*>', '<circle id="n1-end" class="journey-node" cx="340" cy="1110" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n2-end"[^>]*>', '<circle id="n2-end" class="journey-node" cx="250" cy="1380" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n3-end"[^>]*>', '<circle id="n3-end" class="journey-node" cx="1140" cy="1820" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)
content = re.sub(r'<circle id="n4-end"[^>]*>', '<circle id="n4-end" class="journey-node" cx="250" cy="2260" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>', content)

# 2. Increase face.png sticker avatar size to 84px x 84px
LARGER_STICKER_AVATAR = """    <!-- TRAVELING FACE EMOJI STICKER ALONG ARROW PATHS -->
    <div id="path-traveler-avatar" class="absolute z-[80] pointer-events-none transition-transform duration-75" style="width: 84px; height: 84px; top: 0; left: 0; transform: translate(-50%, -50%); display: none;">
      <div class="relative w-full h-full flex items-center justify-center">
        <!-- Speed Dash Motion Trail -->
        <div class="absolute -left-4 top-1/2 -translate-y-1/2 flex flex-col gap-1 opacity-75 pointer-events-none">
          <div class="w-4 h-0.5 bg-gray-500/80 rounded-full"></div>
          <div class="w-2.5 h-0.5 bg-gray-500/80 rounded-full ml-1"></div>
          <div class="w-4 h-0.5 bg-gray-500/80 rounded-full"></div>
        </div>
        <!-- Larger Face Emoji Sticker with crisp white sticker border outline -->
        <img src="face.png" alt="Traveling Avatar" class="w-full h-full object-contain" style="filter: drop-shadow(1.2px 0 0 #ffffff) drop-shadow(-1.2px 0 0 #ffffff) drop-shadow(0 1.2px 0 #ffffff) drop-shadow(0 -1.2px 0 #ffffff) drop-shadow(0 5px 12px rgba(0,0,0,0.18));"/>
      </div>
    </div>"""

content = re.sub(r'<!-- TRAVELING FACE EMOJI STICKER ALONG ARROW PATHS -->.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
content = re.sub(r'<div id="path-traveler-avatar"[^>]*>.*?</div>\s*</div>', '', content, flags=re.DOTALL)

svg_end = content.find('</svg>', content.find('id="timeline-svg"'))
if svg_end != -1:
    idx = svg_end + len('</svg>')
    content = content[:idx] + '\n\n' + LARGER_STICKER_AVATAR + content[idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully attached arrow 0 to bottom of Hero Card and increased face.png size to 84px!")
