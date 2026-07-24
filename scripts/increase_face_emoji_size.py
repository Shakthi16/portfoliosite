import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update size of path-traveler-avatar from 58px to 105px with scaled trail lines
OLD_AVATAR = r'<div id="path-traveler-avatar"[^>]*>.*?</div>\s*</div>'

NEW_AVATAR = """<div id="path-traveler-avatar" class="absolute z-[80] pointer-events-none transition-transform duration-75" style="width: 105px; height: 105px; top: 0; left: 0; transform: translate(-50%, -50%); display: none;">
      <div class="relative w-full h-full">
        <!-- Speed Dash Motion Trail -->
        <div class="absolute -left-5 top-1/2 -translate-y-1/2 flex flex-col gap-1.5 opacity-75 pointer-events-none">
          <div class="w-5 h-1 bg-gray-600/70 rounded-full"></div>
          <div class="w-3.5 h-1 bg-gray-600/70 rounded-full ml-1.5"></div>
          <div class="w-5 h-1 bg-gray-600/70 rounded-full"></div>
        </div>
        <img src="face.png" alt="Traveling Avatar" class="w-full h-full object-contain filter drop-shadow-lg"/>
      </div>
    </div>"""

content = re.sub(OLD_AVATAR, NEW_AVATAR, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully increased face emoji size to 105px with scaled motion trail!")
