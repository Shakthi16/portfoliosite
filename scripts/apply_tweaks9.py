import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

pinterest_card = '''<!-- 4. Design Journey Ticket (Top Mid-Right) -->
      <div class="floating-sticker" style="top: 2%; right: 18%; z-index: 8; transform: rotate(2deg); scale: 0.85;">
        <div class="pinterest-card"
          style="width: 290px; padding: 30px; background: #ffffff; display: flex; flex-direction: column; box-shadow: 0 20px 40px rgba(0,0,0,0.15); border-radius: 24px; overflow: hidden; position: relative; border: 1px solid rgba(0,0,0,0.05);">
          <!-- Pinterest Red Pin / Accent -->
          <div style="position: absolute; top: 16px; right: 16px; width: 12px; height: 12px; border-radius: 50%; background: #e60023; box-shadow: inset -2px -2px 4px rgba(0,0,0,0.1);"></div>
          
          <div style="font-size: 22px; font-weight: 800; color: #111827; font-family: 'Manrope', sans-serif !important; letter-spacing: -0.5px; margin-bottom: 8px; line-height: 1.1;">
            CRAFTING DIGITAL<br>EXPERIENCES
          </div>
          
          <div style="font-size: 10px; font-weight: 800; color: #e60023; font-family: 'IBM Plex Mono', monospace !important; letter-spacing: 1.5px; margin-bottom: 20px;">
            THINK &bull; DESIGN &bull; BUILD
          </div>
          
          <div style="font-size: 14px; color: #4b5563; font-family: 'Outfit', sans-serif !important; line-height: 1.5; font-weight: 500; margin-bottom: 26px;">
            Turning complex problems into intuitive experiences.
          </div>
          
          <div style="font-size: 10px; font-family: 'IBM Plex Mono', monospace !important; color: #ffffff; background: #111827; display: inline-flex; align-items: center; justify-content: center; padding: 10px 18px; border-radius: 24px; font-weight: 700; width: max-content; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
            EST. 2022 — PRESENT
          </div>
        </div>
      </div>'''

content = re.sub(
    r'<!-- 4\. Design Journey Ticket.*?<div class="floating-sticker"[^>]*>.*?<div class="ticket-container".*?</div>\s*</div>\s*</div>',
    pinterest_card,
    content,
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updates applied: Swapped ticket for Pinterest-style minimalist card.")
