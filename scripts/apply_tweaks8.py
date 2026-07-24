import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Move the interactive folder little down
content = re.sub(
    r'(<!-- 16\. Interactive folder -->\s*<div class="floating-sticker"\s*style="top:\s*)35(%;\s*left:\s*)26(%;\s*z-index:\s*12;\s*transform:\s*rotate\(0deg\);\s*scale:\s*1\.1;">)',
    r'\g<1>42\g<2>26\g<3>',
    content
)

# 2. Fix the Ticket Card Design
# Previous HTML block:
# <div style="font-size: 24px; font-weight: 800; color: #7f8c8d; line-height: 1; letter-spacing: -0.5px; margin-bottom: 12px; white-space: nowrap;">
#   CRAFTING<span style="color: #cf2e6c;">EXPERIENCES</span>
# </div>
# <div style="font-size: 8px; font-weight: 700; color: #ffffff; letter-spacing: 1px; margin-bottom: 15px; font-family: 'IBM Plex Mono', monospace;">
#   DESIGN • ENGINEERING • RESEARCH
# </div>

new_ticket_body = '''<div style="position: relative; z-index: 1;">
              <div style="font-size: 19px; font-weight: 800; color: #475569; line-height: 1.1; letter-spacing: -0.5px; margin-bottom: 12px;">
                CRAFTING DIGITAL<br><span style="color: #cf2e6c; font-size: 22px;">EXPERIENCES</span>
              </div>
              <div style="font-size: 8px; font-weight: 700; color: #ffffff; letter-spacing: 1px; margin-bottom: 15px; font-family: 'IBM Plex Mono', monospace;">
                THINK • DESIGN • BUILD
              </div>
              <div style="font-size: 11px; font-weight: 600; line-height: 1.4; margin-bottom: 22px; max-width: 80%;">
                Turning complex problems into intuitive experiences.
              </div>
              <div style="font-size: 9px; font-weight: 700; letter-spacing: 0.5px; font-family: 'IBM Plex Mono', monospace; display: inline-block;">
                EST. 2022 — PRESENT
              </div>
            </div>'''

content = re.sub(
    r'<div style="position: relative; z-index: 1;">.*?EST\. 2022 — PRESENT\s*</div>\s*</div>',
    new_ticket_body,
    content,
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updates applied: Folder moved down, ticket text and layout fixed.")
