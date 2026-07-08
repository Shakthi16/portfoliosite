import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# We will completely replace everything from "<!-- 4. Design Journey Ticket" up to the girl image "<!-- 7."
# This cleans up the broken HTML from the previous regex failure.

start_marker = "<!-- 4. Design Journey Ticket (Top Mid-Right) -->"
end_marker = "<!-- 7. \"currently building\" Pink Note (Bottom Mid-Left) -->"

new_section = '''<!-- 4. Design Journey Ticket (Top Mid-Right) -->
      <div class="floating-sticker" style="top: 5%; right: 18%; z-index: 8; transform: rotate(2deg); scale: 0.75;">
        <div class="pinterest-card"
          style="width: 440px; height: 180px; background: #ffffff; display: flex; flex-direction: row; box-shadow: 0 24px 50px rgba(0,0,0,0.12); border-radius: 28px; overflow: hidden; position: relative; border: 1px solid rgba(0,0,0,0.05);">
          
          <!-- Left Image Header -->
          <div style="width: 160px; height: 100%; position: relative;">
            <img src="https://images.unsplash.com/photo-1557672172-298e090bd0f1?q=80&w=600" style="width: 100%; height: 100%; object-fit: cover;" alt="Abstract Design" />
            <!-- Pinterest Red Pin / Accent floating over image -->
            <div style="position: absolute; top: 18px; left: 18px; width: 32px; height: 32px; border-radius: 50%; background: rgba(255,255,255,0.95); box-shadow: 0 8px 16px rgba(0,0,0,0.15); display: flex; align-items: center; justify-content: center; backdrop-filter: blur(8px);">
              <div style="width: 10px; height: 10px; border-radius: 50%; background: #e60023;"></div>
            </div>
          </div>
          
          <!-- Right Content Area -->
          <div style="flex: 1; padding: 25px 30px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-size: 19px; font-weight: 800; color: #111827; font-family: 'Manrope', sans-serif !important; letter-spacing: -0.5px; margin-bottom: 6px; line-height: 1.1;">
              CRAFTING DIGITAL EXPERIENCES
            </div>
            
            <div style="font-size: 9px; font-weight: 800; color: #e60023; font-family: 'IBM Plex Mono', monospace !important; letter-spacing: 1.5px; margin-bottom: 12px;">
              THINK &bull; DESIGN &bull; BUILD
            </div>
            
            <div style="font-size: 12.5px; color: #4b5563; font-family: 'Outfit', sans-serif !important; line-height: 1.4; font-weight: 500; margin-bottom: 18px;">
              Turning complex problems into intuitive experiences.
            </div>
            
            <div style="font-size: 9px; font-family: 'IBM Plex Mono', monospace !important; color: #ffffff; background: #111827; display: inline-flex; align-items: center; justify-content: center; padding: 8px 16px; border-radius: 24px; font-weight: 700; width: max-content; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
              EST. 2022 — PRESENT
            </div>
          </div>
        </div>
      </div>

      <!-- 5. What Drives Me Note (Top Far Right) -->
      <div class="floating-sticker" style="top: 2%; right: -2%; z-index: 6; transform: rotate(-2deg); scale: 0.8;">
        <div
          style="position: absolute; top: 15px; right: 40%; transform: rotate(15deg); width: 45px; height: 16px; background: rgba(220, 200, 210, 0.9); box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-top: 1px solid rgba(255,255,255,0.5); z-index: 5;">
        </div>
        <div
          style="width: 320px; height: 320px; background: url('notes.png') center/contain no-repeat; padding: 75px 40px 30px 145px; box-sizing: border-box; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.05)); display: flex; flex-direction: column;">
          <div
            style="font-family: 'Brittany Signature', cursive !important; font-size: 26px; color: #421835; margin-bottom: 5px; text-align: left; text-shadow: 0 1px 2px rgba(255,255,255,0.5);">
            what drives me</div>
          <div
            style="font-size: 10px; color: #582a4b; font-family: 'Manrope', sans-serif !important; line-height: 2.2; text-align: left; padding-right: 10px; max-width: 140px;">
            I blend creativity with strategy, aesthetics with logic, and empathy with security — to build digital
            experiences that matter.
          </div>
        </div>
      </div>

      <!-- 6. GIRL.PNG (Placed next to 'Sri') -->
      <div class="floating-sticker" style="top: 50%; right: 12%; z-index: 10; transform: rotate(0deg); scale: 0.5;">
        <img src="girl.png" alt="Aesthetic Girl Illustration"
          style="width: 170px; opacity: 0.95; mix-blend-mode: multiply; pointer-events: none;" />
      </div>

      '''

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_section + content[end_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updates applied: HTML cleaned, Horizontal Card implemented, Girl illustration aggressively scaled down and moved.")
