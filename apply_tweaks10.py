import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the Pinterest card to add a modern image header
new_pinterest_card = '''<div class="pinterest-card"
          style="width: 300px; background: #ffffff; display: flex; flex-direction: column; box-shadow: 0 24px 50px rgba(0,0,0,0.12); border-radius: 28px; overflow: hidden; position: relative; border: 1px solid rgba(0,0,0,0.05);">
          <!-- Header Image -->
          <div style="height: 140px; width: 100%; position: relative;">
            <img src="https://images.unsplash.com/photo-1557672172-298e090bd0f1?q=80&w=600" style="width: 100%; height: 100%; object-fit: cover;" alt="Abstract Design" />
            <!-- Pinterest Red Pin / Accent floating over image -->
            <div style="position: absolute; top: 18px; right: 18px; width: 36px; height: 36px; border-radius: 50%; background: rgba(255,255,255,0.95); box-shadow: 0 8px 16px rgba(0,0,0,0.15); display: flex; align-items: center; justify-content: center; backdrop-filter: blur(8px);">
              <div style="width: 12px; height: 12px; border-radius: 50%; background: #e60023;"></div>
            </div>
          </div>
          
          <div style="padding: 25px 30px;">
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
    r'<div class="pinterest-card".*?EST\. 2022 — PRESENT\s*</div>\s*</div>\s*</div>',
    new_pinterest_card + '\n      </div>',
    content,
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updates applied: Card upgraded with modern visual header.")
