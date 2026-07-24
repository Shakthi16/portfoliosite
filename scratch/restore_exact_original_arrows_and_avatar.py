import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Restore exact SVG element & viewBox
SVG_EXACT_HTML = """    <!-- THE ARROW SYSTEM SVG -->
    <svg class="absolute inset-0 w-full h-full pointer-events-none z-[50]" id="timeline-svg" viewBox="0 0 1400 2700" preserveAspectRatio="xMidYMid meet">
      <defs>
        <!-- Arrowhead marker -->
        <marker id="arrow-tip" viewBox="0 0 12 12" refX="9" refY="6" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 2 2 L 9 6 L 2 10" fill="none" stroke="#475569" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
        </marker>

        <!-- Glow filter for nodes -->
        <filter id="glow-sm" x="-100%" y="-100%" width="300%" height="300%">
          <feGaussianBlur stdDeviation="3" result="blur"/>
          <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
      </defs>

      <!-- SEG 0: Hero card → Girl illustration -->
      <path id="seg-0" class="journey-path" d="M 290 508 C 290 648, 874.8 420, 874.8 532.8" fill="none" stroke="#475569" stroke-width="2.8" stroke-dasharray="8 8" stroke-opacity="0.95" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow-tip)" />
      <circle id="n0-end" class="journey-node" cx="874.8" cy="532.8" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>

      <!-- SEG 1: Girl illustration → Orbital -->
      <path id="seg-1" class="journey-path" d="M 980 900 C 980 1260, 410 1150, 210 1110" fill="none" stroke="#475569" stroke-width="2.8" stroke-dasharray="8 8" stroke-opacity="0.95" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow-tip)" />
      <circle id="n1-end" class="journey-node" cx="210" cy="1110" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>

      <!-- SEG 2: Orbital → LinkedIn card -->
      <path id="seg-2" class="journey-path" d="M 67 1110 C -53 1270, 141.2 1320, 141.2 1393.6" fill="none" stroke="#475569" stroke-width="2.8" stroke-dasharray="8 8" stroke-opacity="0.95" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow-tip)" />
      <circle id="n2-end" class="journey-node" cx="141.2" cy="1393.6" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>

      <!-- SEG 3: LinkedIn card → GitHub card -->
      <path id="seg-3" class="journey-path" d="M 250 1726.4 C 250 1866.4, 1258.8 1716, 1258.8 1834.6" fill="none" stroke="#475569" stroke-width="2.8" stroke-dasharray="8 8" stroke-opacity="0.95" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow-tip)" />
      <circle id="n3-end" class="journey-node" cx="1258.8" cy="1834.6" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>

      <!-- SEG 4: GitHub card → Shavira card -->
      <path id="seg-4" class="journey-path" d="M 1150 2166.4 C 1150 2306.4, 141.2 2156.4, 141.2 2273.6" fill="none" stroke="#475569" stroke-width="2.8" stroke-dasharray="8 8" stroke-opacity="0.95" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow-tip)" />
      <circle id="n4-end" class="journey-node" cx="141.2" cy="2273.6" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>
    </svg>"""

# Replace SVG element in index.html
content = re.sub(r'<!-- THE ARROW SYSTEM SVG -->.*?<\/svg>', SVG_EXACT_HTML, content, flags=re.DOTALL)
content = re.sub(r'<svg[^>]*id="timeline-svg"[^>]*>.*?<\/svg>', SVG_EXACT_HTML, content, flags=re.DOTALL)

# 2. Exact Face Emoji Sticker Styling matching Image 5 (Crisp 1.5px white border outline around face.png silhouette)
STICKER_AVATAR_HTML = """    <!-- TRAVELING FACE EMOJI STICKER ALONG ARROW PATHS -->
    <div id="path-traveler-avatar" class="absolute z-[80] pointer-events-none transition-transform duration-75" style="width: 58px; height: 58px; top: 0; left: 0; transform: translate(-50%, -50%); display: none;">
      <div class="relative w-full h-full flex items-center justify-center">
        <!-- Speed Dash Motion Trail -->
        <div class="absolute -left-3.5 top-1/2 -translate-y-1/2 flex flex-col gap-1 opacity-70 pointer-events-none">
          <div class="w-3.5 h-0.5 bg-gray-500/70 rounded-full"></div>
          <div class="w-2.5 h-0.5 bg-gray-500/70 rounded-full ml-1"></div>
          <div class="w-3.5 h-0.5 bg-gray-500/70 rounded-full"></div>
        </div>
        <!-- Face Emoji Sticker with crisp white sticker border outline around face.png silhouette -->
        <img src="face.png" alt="Traveling Avatar" class="w-full h-full object-contain" style="filter: drop-shadow(1px 0 0 #ffffff) drop-shadow(-1px 0 0 #ffffff) drop-shadow(0 1px 0 #ffffff) drop-shadow(0 -1px 0 #ffffff) drop-shadow(0 4px 8px rgba(0,0,0,0.18));"/>
      </div>
    </div>"""

content = re.sub(r'<!-- TRAVELING FACE EMOJI STICKER ALONG ARROW PATHS -->.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
content = re.sub(r'<div id="path-traveler-avatar"[^>]*>.*?</div>\s*</div>', '', content, flags=re.DOTALL)

svg_end_idx = content.find('</svg>', content.find('id="timeline-svg"'))
if svg_end_idx != -1:
    idx = svg_end_idx + len('</svg>')
    content = content[:idx] + '\n\n' + STICKER_AVATAR_HTML + content[idx:]

# 3. CSS for .journey-path
OLD_CSS = r'\.journey-path\s*\{[^}]*\}'
NEW_CSS = """.journey-path {
      stroke: #475569 !important;
      stroke-width: 2.8px !important;
      stroke-dasharray: 8 8 !important;
      stroke-opacity: 0.95 !important;
      stroke-linecap: round !important;
      stroke-linejoin: round !important;
      fill: none !important;
    }"""

content = re.sub(OLD_CSS, NEW_CSS, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully restored exact original arrow curve paths and face sticker silhouette styling!")
