import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Move the interactive folder up
# Find: <!-- 16. Interactive folder --> ... style="top: 55%; left: 22%;
# Replace with: style="top: 35%; left: 26%;
content = re.sub(
    r'(<!-- 16\. Interactive folder -->\s*<div class="floating-sticker"\s*style="top:\s*)55(%;\s*left:\s*)22(%;\s*z-index:\s*12;\s*transform:\s*rotate\(-3deg\);\s*scale:\s*1\.1;">)',
    r'\g<1>35\g<2>26\g<3>',
    content
)

# 2. Replace the Design Journey ticket with Pinterest style card
pinterest_card = '''<!-- 4. Design Journey Ticket (Top Mid-Right) -->
      <div class="floating-sticker" style="top: 2%; right: 18%; z-index: 8; transform: rotate(2deg); scale: 0.85;">
        <div class="pinterest-card"
          style="width: 280px; padding: 25px; background: #ffffff; display: flex; flex-direction: column; box-shadow: 0 16px 40px rgba(0,0,0,0.12); border-radius: 20px; overflow: hidden; position: relative;">
          <div
            style="position: absolute; top: 12px; right: 12px; width: 10px; height: 10px; border-radius: 50%; background: #ef4444; box-shadow: inset -2px -2px 4px rgba(0,0,0,0.2); z-index: 10;">
          </div>
          <div
            style="font-size: 14px; font-weight: 800; color: #111827; font-family: 'Manrope', sans-serif !important; letter-spacing: 0.05em; margin-bottom: 8px; text-transform: uppercase;">
            CRAFTING DIGITAL EXPERIENCES</div>
          <div
            style="font-size: 9px; font-weight: 700; color: #3b82f6; font-family: 'IBM Plex Mono', monospace !important; letter-spacing: 0.08em; margin-bottom: 16px; text-transform: uppercase;">
            DESIGN &bull; ENGINEERING &bull; RESEARCH</div>
          <div
            style="font-size: 13px; color: #4b5563; font-family: 'Outfit', sans-serif !important; line-height: 1.5; font-weight: 500; margin-bottom: 20px;">
            Turning complex problems<br>into intuitive experiences.</div>
          <div
            style="font-size: 9px; font-family: 'IBM Plex Mono', monospace !important; color: #ffffff; background: #111827; display: inline-flex; align-items: center; justify-content: center; padding: 8px 12px; border-radius: 20px; font-weight: 700; width: max-content;">
            EST. 2022 — PRESENT</div>
        </div>
      </div>'''

content = re.sub(
    r'<!-- 4\. Design Journey Ticket.*?<div class="floating-sticker".*?<div class="ticket-pass".*?</div>\s*</div>\s*</div>',
    pinterest_card,
    content,
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updates applied: Folder moved up, Design Journey card converted to Pinterest style.")
