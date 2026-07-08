import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Spread out bottom elements to prevent collision between Agni and Paint
content = content.replace(
    '<!-- 11. AGNI C2 Card (Bottom Center) -->\n  <div class="floating-sticker" style="bottom: 2%; left: 38%;',
    '<!-- 11. AGNI C2 Card (Bottom Center) -->\n  <div class="floating-sticker" style="bottom: 2%; left: 32%;'
)

content = content.replace(
    '<!-- 13. MacPaint Palette (Moved slightly left of Tech Stack so it doesn\'t clip polaroids on right) -->\n  <div class="floating-sticker" style="bottom: 5%; right: 40%;',
    '<!-- 13. MacPaint Palette (Moved slightly left of Tech Stack so it doesn\'t clip polaroids on right) -->\n  <div class="floating-sticker" style="bottom: 5%; left: 55%;'
)

# 2. Fan out the interactive folders wider so the labels don't collide
content = content.replace(
    'transform: translate(-50px, -60px) rotate(-15deg);',
    'transform: translate(-75px, -80px) rotate(-15deg);'
)

content = content.replace(
    'transform: translate(0px, -75px) rotate(0deg);',
    'transform: translate(0px, -100px) rotate(0deg);'
)

content = content.replace(
    'transform: translate(50px, -60px) rotate(15deg);',
    'transform: translate(75px, -80px) rotate(15deg);'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed collisions between bottom cards and folder labels.")
