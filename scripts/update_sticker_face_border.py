import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OLD_AVATAR = r'<div id="path-traveler-avatar"[^>]*>.*?</div>\s*</div>'

NEW_AVATAR = """<div id="path-traveler-avatar" class="absolute z-[80] pointer-events-none transition-transform duration-75" style="width: 105px; height: 105px; top: 0; left: 0; transform: translate(-50%, -50%); display: none;">
      <div class="relative w-full h-full flex items-center justify-center">
        <!-- Face Emoji with Die-Cut White Sticker Border Outline -->
        <img src="face.png" alt="Traveling Avatar" class="w-full h-full object-contain" style="filter: drop-shadow(2px 0 0 #ffffff) drop-shadow(-2px 0 0 #ffffff) drop-shadow(0 2px 0 #ffffff) drop-shadow(0 -2px 0 #ffffff) drop-shadow(1.5px 1.5px 0 #ffffff) drop-shadow(-1.5px -1.5px 0 #ffffff) drop-shadow(1.5px -1.5px 0 #ffffff) drop-shadow(-1.5px 1.5px 0 #ffffff) drop-shadow(0 8px 16px rgba(0,0,0,0.16));"/>
      </div>
    </div>"""

content = re.sub(OLD_AVATAR, NEW_AVATAR, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully removed motion lines and added white die-cut sticker border outline around face emoji!")
