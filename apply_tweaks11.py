import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Reduce the scale of the Pinterest card
# Find: <!-- 4. Design Journey Ticket (Top Mid-Right) -->
# <div class="floating-sticker" style="top: 2%; right: 18%; z-index: 8; transform: rotate(2deg); scale: 0.85;">
# Change scale: 0.85; to scale: 0.65; and move it up slightly to top: 0%;

content = re.sub(
    r'(<!-- 4\. Design Journey Ticket.*?<div class="floating-sticker"\s*style="top:\s*)2(%;\s*right:\s*)18(%;\s*z-index:\s*8;\s*transform:\s*rotate\(2deg\);\s*scale:\s*)0\.85(;">)',
    r'\g<1>0\g<2>18\g<3>0.7\g<4>',
    content
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updates applied: Reduced Pinterest card size.")
