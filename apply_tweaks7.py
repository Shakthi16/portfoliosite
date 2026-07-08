import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Design Journey card to Event Ticket Style
ticket_html = '''<!-- 4. Design Journey Ticket (Top Mid-Right) -->
      <div class="floating-sticker" style="top: 2%; right: 18%; z-index: 8; transform: rotate(2deg); scale: 0.85;">
        <div class="ticket-container" style="display: flex; width: 340px; height: 160px; box-shadow: 0 15px 35px rgba(0,0,0,0.2); border-radius: 4px; overflow: hidden; font-family: 'Manrope', sans-serif;">
          
          <!-- Left Ticket Body -->
          <div style="flex: 1; background: #51c4b7; position: relative; padding: 20px 25px; color: #fff; overflow: hidden;">
            <!-- Background Shapes -->
            <svg style="position: absolute; top: -10px; right: -20px; width: 120px; height: 120px; z-index: 0;" viewBox="0 0 100 100">
              <path d="M10,0 C50,0 80,30 80,70 C80,100 50,100 0,100 Z" fill="#f4d142"/>
              <!-- diagonal lines -->
              <g stroke="#cf2e6c" stroke-width="2.5" transform="rotate(25 50 50)">
                <line x1="55" y1="20" x2="55" y2="80"/>
                <line x1="62" y1="20" x2="62" y2="80"/>
                <line x1="69" y1="20" x2="69" y2="80"/>
                <line x1="76" y1="20" x2="76" y2="80"/>
              </g>
              <circle cx="85" cy="85" r="5" stroke="#cf2e6c" stroke-width="3" fill="none"/>
            </svg>
            
            <div style="position: relative; z-index: 1;">
              <div style="font-size: 24px; font-weight: 800; color: #7f8c8d; line-height: 1; letter-spacing: -0.5px; margin-bottom: 12px; white-space: nowrap;">
                CRAFTING<span style="color: #cf2e6c;">EXPERIENCES</span>
              </div>
              <div style="font-size: 8px; font-weight: 700; color: #ffffff; letter-spacing: 1px; margin-bottom: 15px; font-family: 'IBM Plex Mono', monospace;">
                DESIGN • ENGINEERING • RESEARCH
              </div>
              <div style="font-size: 11px; font-weight: 600; line-height: 1.4; margin-bottom: 22px; max-width: 80%;">
                Turning complex problems into intuitive experiences.
              </div>
              <div style="font-size: 9px; font-weight: 700; letter-spacing: 0.5px; font-family: 'IBM Plex Mono', monospace; display: inline-block;">
                EST. 2022 — PRESENT
              </div>
            </div>
          </div>
          
          <!-- Right Ticket Stub -->
          <div style="width: 70px; background: #fff; border-left: 2px dashed #ccc; display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative;">
            <div style="transform: rotate(-90deg); font-size: 10px; font-weight: 700; color: #51c4b7; white-space: nowrap; letter-spacing: 1px; margin-bottom: 40px;">
              DESIGN JOURNEY
            </div>
            <!-- Barcode -->
            <svg width="40" height="50" style="position: absolute; right: 8px; top: 50%; transform: translateY(-50%);">
              <rect x="0" y="0" width="2" height="50" fill="#333"/>
              <rect x="4" y="0" width="4" height="50" fill="#333"/>
              <rect x="10" y="0" width="1" height="50" fill="#333"/>
              <rect x="13" y="0" width="3" height="50" fill="#333"/>
              <rect x="18" y="0" width="2" height="50" fill="#333"/>
              <rect x="22" y="0" width="5" height="50" fill="#333"/>
              <rect x="29" y="0" width="1" height="50" fill="#333"/>
              <rect x="32" y="0" width="4" height="50" fill="#333"/>
              <rect x="38" y="0" width="2" height="50" fill="#333"/>
            </svg>
          </div>
        </div>
      </div>'''

content = re.sub(
    r'<!-- 4\. Design Journey Ticket.*?<div class="floating-sticker"[^>]*>.*?<div class="pinterest-card".*?</div>\s*</div>\s*</div>',
    ticket_html,
    content,
    flags=re.DOTALL
)

# 2. Fix overlapping folders and update font style
# Space them out wider
content = re.sub(r'transform:\s*scale\(1\)\s*translate\(-120px,\s*-40px\);', r'transform: scale(1) translate(-170px, -20px);', content)
content = re.sub(r'transform:\s*scale\(1\)\s*translate\(0px,\s*-120px\);', r'transform: scale(1) translate(0px, -150px);', content)
content = re.sub(r'transform:\s*scale\(1\)\s*translate\(120px,\s*-40px\);', r'transform: scale(1) translate(170px, -20px);', content)

# Change .sub-folder-label font and style
new_label_css = '''    .sub-folder-label {
      font-family: 'Outfit', sans-serif !important;
      font-size: 13px;
      font-weight: 500;
      color: #1e3a8a !important;
      margin-top: 15px;
      background: #ffffff;
      padding: 6px 14px;
      border-radius: 20px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
      white-space: nowrap;
      border: 1px solid rgba(0,0,0,0.05);
    }'''

content = re.sub(
    r'\.sub-folder-label\s*\{[^}]*\}',
    new_label_css,
    content,
    flags=re.DOTALL
)

# 3. Update the song URL to a dreaming song
content = re.sub(
    r'<audio id="lofi-audio" src="[^"]+" loop></audio>',
    r'<audio id="lofi-audio" src="https://cdn.pixabay.com/download/audio/2022/01/26/audio_d0c6ff1cb8.mp3" loop></audio>',
    content
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updates applied: Ticket card styled, folders fanned properly, dreaming song added.")
