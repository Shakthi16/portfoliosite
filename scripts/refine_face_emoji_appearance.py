import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OLD_AVATAR = r'<div id="path-traveler-avatar"[^>]*>.*?</div>\s*</div>'

NEW_AVATAR = """<div id="path-traveler-avatar" class="absolute z-[80] pointer-events-none transition-transform duration-75" style="width: 140px; height: 140px; top: 0; left: 0; transform: translate(-50%, -50%); display: none;">
      <div class="relative w-full h-full flex items-center justify-center">
        <!-- Face Emoji: Larger, Brighter, Crystal Clear & Delicate Light White Border -->
        <img src="face.png" alt="Traveling Avatar" class="w-full h-full object-contain" style="filter: brightness(1.08) contrast(1.05) drop-shadow(0.8px 0 0 rgba(255,255,255,0.95)) drop-shadow(-0.8px 0 0 rgba(255,255,255,0.95)) drop-shadow(0 0.8px 0 rgba(255,255,255,0.95)) drop-shadow(0 -0.8px 0 rgba(255,255,255,0.95)) drop-shadow(0 6px 14px rgba(0,0,0,0.15));"/>
      </div>
    </div>"""

content = re.sub(OLD_AVATAR, NEW_AVATAR, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated face emoji size to 140px, increased brightness/clarity, and refined to a light 0.8px white border!")
