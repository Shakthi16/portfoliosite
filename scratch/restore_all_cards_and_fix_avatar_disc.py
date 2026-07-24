import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open('restored_about_section.html', 'r', encoding='utf-8') as f:
    restored_about_html = f.read()

# 1. Replace section id="about" in content with restored_about_html
pos_about = content.find('id="about"')
if pos_about != -1:
    sec_start = content.rfind('<section', 0, pos_about)
    sec_end = content.find('</section>', pos_about) + len('</section>')
    content = content[:sec_start] + restored_about_html.strip() + content[sec_end:]
    print("Successfully replaced #about section with all 11 cards & text nodes from restored_about_section.html!")

# 2. Precise 60px Circular White Badge Disc around face.png
CIRCULAR_AVATAR_DISC = """    <!-- TRAVELING FACE EMOJI STICKER ALONG ARROW PATHS -->
    <div id="path-traveler-avatar" class="absolute z-[80] pointer-events-none transition-transform duration-75" style="width: 60px; height: 60px; top: 0; left: 0; transform: translate(-50%, -50%); display: none;">
      <div class="relative w-full h-full flex items-center justify-center">
        <!-- Speed Dash Motion Trail -->
        <div class="absolute -left-3.5 top-1/2 -translate-y-1/2 flex flex-col gap-1 opacity-70 pointer-events-none">
          <div class="w-3.5 h-0.5 bg-gray-500/70 rounded-full"></div>
          <div class="w-2.5 h-0.5 bg-gray-500/70 rounded-full ml-1"></div>
          <div class="w-3.5 h-0.5 bg-gray-500/70 rounded-full"></div>
        </div>
        <!-- Circular White Translucent Badge Disc with 2px White Border & Soft Shadow -->
        <div class="w-full h-full rounded-full bg-white/85 backdrop-blur-md border-2 border-white shadow-[0_4px_12px_rgba(0,0,0,0.15)] flex items-center justify-center p-1.5 overflow-hidden">
          <img src="face.png" alt="Traveling Avatar" class="w-full h-full object-contain filter brightness-[1.05] contrast-[1.05]"/>
        </div>
      </div>
    </div>"""

# Remove old avatar elements if present
content = re.sub(r'<!-- TRAVELING FACE EMOJI STICKER ALONG ARROW PATHS -->.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
content = re.sub(r'<div id="path-traveler-avatar"[^>]*>.*?</div>\s*</div>', '', content, flags=re.DOTALL)

# Insert circular avatar disc right after timeline-svg </svg>
svg_end = content.find('</svg>', content.find('id="timeline-svg"'))
if svg_end != -1:
    insert_idx = svg_end + len('</svg>')
    content = content[:insert_idx] + '\n\n' + CIRCULAR_AVATAR_DISC + content[insert_idx:]
    print("Successfully inserted 60px Circular White Badge Disc around face.png!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Restoration complete!")
