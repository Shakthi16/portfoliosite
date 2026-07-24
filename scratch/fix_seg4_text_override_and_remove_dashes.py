import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update seg-4 d attribute so it swoops low below {05} text block without any overlap
SEG_4_D = "M 1140 2160 C 1140 2400, 600 2440, 250 2260"
content = re.sub(r'<path id="seg-4" class="journey-path" d="[^"]*"', f'<path id="seg-4" class="journey-path" d="{SEG_4_D}"', content)

# Also ensure seg-1 and seg-3 swoop low below {02} and {03}
SEG_1_D = "M 1140 900 C 1220 1250, 620 1280, 340 1110"
SEG_3_D = "M 250 1720 C 250 1920, 850 1960, 1140 1820"
content = re.sub(r'<path id="seg-1" class="journey-path" d="[^"]*"', f'<path id="seg-1" class="journey-path" d="{SEG_1_D}"', content)
content = re.sub(r'<path id="seg-3" class="journey-path" d="[^"]*"', f'<path id="seg-3" class="journey-path" d="{SEG_3_D}"', content)

# 2. Remove the 3 speed dash motion trail lines around face.png
STICKER_AVATAR_NO_DASHES = """    <!-- TRAVELING FACE EMOJI STICKER ALONG ARROW PATHS -->
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
    content = content[:idx] + '\n\n' + STICKER_AVATAR_NO_DASHES + content[idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated seg-4 curve to swoop low below {05} text and removed 3 motion dash lines around face.png!")
