import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Make timeline-container ALWAYS VISIBLE (remove 'hidden md:block', set to 'block')
content = content.replace(
    'class="relative w-full max-w-[1400px] mx-auto px-6 lg:px-12 z-10 hidden md:block"',
    'class="relative w-full max-w-[1400px] mx-auto px-6 lg:px-12 z-10 block"'
)

# 2. Increase face.png sticker avatar size to 110px x 110px
PROMINENT_STICKER_AVATAR = """    <!-- TRAVELING FACE EMOJI STICKER ALONG ARROW PATHS -->
    <div id="path-traveler-avatar" class="absolute z-[80] pointer-events-none transition-transform duration-75" style="width: 110px; height: 110px; top: 0; left: 0; transform: translate(-50%, -50%); display: none;">
      <div class="relative w-full h-full flex items-center justify-center">
        <!-- Speed Dash Motion Trail -->
        <div class="absolute -left-5 top-1/2 -translate-y-1/2 flex flex-col gap-1.5 opacity-80 pointer-events-none">
          <div class="w-5 h-0.5 bg-gray-500/80 rounded-full"></div>
          <div class="w-3 h-0.5 bg-gray-500/80 rounded-full ml-1"></div>
          <div class="w-5 h-0.5 bg-gray-500/80 rounded-full"></div>
        </div>
        <!-- Prominent Face Emoji Sticker with crisp white border outline -->
        <img src="face.png" alt="Traveling Avatar" class="w-full h-full object-contain" style="filter: drop-shadow(1.8px 0 0 #ffffff) drop-shadow(-1.8px 0 0 #ffffff) drop-shadow(0 1.8px 0 #ffffff) drop-shadow(0 -1.8px 0 #ffffff) drop-shadow(0 6px 14px rgba(0,0,0,0.18));"/>
      </div>
    </div>"""

content = re.sub(r'<!-- TRAVELING FACE EMOJI STICKER ALONG ARROW PATHS -->.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
content = re.sub(r'<div id="path-traveler-avatar"[^>]*>.*?</div>\s*</div>', '', content, flags=re.DOTALL)

svg_end = content.find('</svg>', content.find('id="timeline-svg"'))
if svg_end != -1:
    idx = svg_end + len('</svg>')
    content = content[:idx] + '\n\n' + PROMINENT_STICKER_AVATAR + content[idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully made timeline-container always visible and enlarged face.png to 110px!")
