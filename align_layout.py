import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. ID Card
content = re.sub(
    r'<!-- 1\. ID CARD.*?<div class="floating-sticker"\s*style="top:[^>]*>',
    '<!-- 1. ID CARD (Top Left Corner) -->\n      <div class="floating-sticker"\n        style="top: -2%; left: 0%; z-index: 10; transform: rotate(-5deg); scale: 0.8; transform-origin: top left;">',
    content, flags=re.DOTALL
)

# 2. Desk Setup Image
content = re.sub(
    r'<!-- 2\. Desk Setup Image.*?<div class="floating-sticker" style="top:[^>]*>',
    '<!-- 2. Desk Setup Image (Top Left, beside ID card) -->\n      <div class="floating-sticker" style="top: 0%; left: 15%; z-index: 7; transform: rotate(3deg); scale: 0.8;">',
    content, flags=re.DOTALL
)

# 3. "today\'s focus" Note (Swapping order in my mental map, but we replace by comment)
content = re.sub(
    r'<!-- 3\. "today\'s focus" Note.*?<div class="floating-sticker" style="top:[^>]*>',
    '<!-- 3. "today\'s focus" Note -->\n      <div class="floating-sticker" style="top: 42%; left: 8%; z-index: 8; transform: rotate(2deg); scale: 0.85;">',
    content, flags=re.DOTALL
)

# 4. Design Journey Ticket
content = re.sub(
    r'<!-- 4\. Design Journey Ticket.*?<div class="floating-sticker" style="top:[^>]*>',
    '<!-- 4. Design Journey Ticket (Top Mid-Right) -->\n      <div class="floating-sticker" style="top: 2%; right: 18%; z-index: 8; transform: rotate(2deg); scale: 0.8;">',
    content, flags=re.DOTALL
)

# 5. What Drives Me Note
content = re.sub(
    r'<!-- 5\. What Drives Me Note.*?<div class="floating-sticker" style="top:[^>]*>',
    '<!-- 5. What Drives Me Note (Top Far Right) -->\n      <div class="floating-sticker" style="top: 2%; right: -2%; z-index: 6; transform: rotate(-2deg); scale: 0.8;">',
    content, flags=re.DOTALL
)

# 6. GIRL.PNG
content = re.sub(
    r'<!-- 6\. GIRL\.PNG.*?<div class="floating-sticker" style="top:[^>]*>',
    '<!-- 6. GIRL.PNG (Placed next to \'Sri\') -->\n      <div class="floating-sticker" style="top: 38%; right: 28%; z-index: 10; transform: rotate(0deg); scale: 0.9;">',
    content, flags=re.DOTALL
)

# 7. "currently building" Pink Note
content = re.sub(
    r'<!-- 7\. "currently building" Pink Note.*?<div class="floating-sticker"\s*style="bottom:[^>]*>',
    '<!-- 7. "currently building" Pink Note (Bottom Mid-Left) -->\n      <div class="floating-sticker"\n        style="top: 48%; left: 1%; z-index: 9; transform: rotate(-4deg); scale: 0.8; transform-origin: bottom left;">',
    content, flags=re.DOTALL
)

# 8. "LESSONS I'M STILL LEARNING" Note
content = re.sub(
    r'<!-- 8\. "LESSONS I\'M STILL LEARNING" Note.*?<div class="floating-sticker" style="bottom:[^>]*>',
    '<!-- 8. "LESSONS I\'M STILL LEARNING" Note (Bottom Center-Left) -->\n      <div class="floating-sticker" style="bottom: 5%; left: 12%; z-index: 7; transform: rotate(3deg); scale: 0.85;">',
    content, flags=re.DOTALL
)

# 9. Terminal Window
content = re.sub(
    r'<!-- 9\. Terminal Window.*?<div class="floating-sticker"\s*style="bottom:[^>]*>',
    '<!-- 9. Terminal Window (Bottom Left) -->\n      <div class="floating-sticker"\n        style="bottom: 5%; left: 0%; z-index: 10; transform: rotate(-2deg); transform-origin: bottom left; scale: 0.8;">',
    content, flags=re.DOTALL
)

# 10. Dark Quote Note
content = re.sub(
    r'<!-- 10\. Dark Quote Note.*?<div class="floating-sticker"\s*style="bottom:[^>]*>',
    '<!-- 10. Dark Quote Note (Bottom Mid-Left) -->\n      <div class="floating-sticker"\n        style="top: 18%; left: 12%; z-index: 12; transform: rotate(2deg); transform-origin: bottom center; scale: 0.85;">',
    content, flags=re.DOTALL
)

# 11. AGNI C2 Card - REMOVE
content = re.sub(
    r'<!-- 11\. AGNI C2 Card.*?<!-- 12\. Tech Stack Grid',
    '<!-- 12. Tech Stack Grid',
    content, flags=re.DOTALL
)

# 12. Tech Stack Grid
content = re.sub(
    r'<!-- 12\. Tech Stack Grid.*?<div class="floating-sticker"\s*style="bottom:[^>]*>',
    '<!-- 12. Tech Stack Grid (Bottom Center-Right) -->\n      <div class="floating-sticker"\n        style="bottom: 12%; right: 28%; z-index: 10; transform: rotate(-1deg); transform-origin: bottom right; scale: 0.8;">',
    content, flags=re.DOTALL
)

# 13. MacPaint Palette
content = re.sub(
    r'<!-- 13\. MacPaint Palette.*?<div class="floating-sticker"\s*style="bottom:[^>]*>',
    '<!-- 13. MacPaint Palette -->\n      <div class="floating-sticker"\n        style="bottom: 35%; right: 18%; z-index: 200 !important; transform: rotate(0deg); scale: 0.8;">',
    content, flags=re.DOTALL
)

# 14. 3 Polaroids
content = re.sub(
    r'<!-- 14\. 3 Polaroids.*?<div class="floating-sticker" style="top:[^>]*>',
    '<!-- 14. 3 Polaroids (Far Mid Right) -->\n      <div class="floating-sticker" style="top: 30%; right: 0%; width: 220px; height: 300px; z-index: 10; transform: rotate(2deg); scale: 0.8;">',
    content, flags=re.DOTALL
)

# 15. Music Player
content = re.sub(
    r'<!-- 15\. Music Player.*?<div class="floating-sticker" style="bottom:[^>]*>',
    '<!-- 15. Music Player (Bottom Right, safely above vinyl) -->\n      <div class="floating-sticker" style="bottom: 8%; right: 12%; z-index: 25; transform: rotate(-3deg); scale: 0.85;">',
    content, flags=re.DOTALL
)

# 16. Interactive folder
content = re.sub(
    r'<!-- 16\. Interactive folder.*?<div class="floating-sticker" style="bottom:[^>]*>',
    '<!-- 16. Interactive folder -->\n      <div class="floating-sticker" style="top: 55%; left: 22%; z-index: 12; transform: rotate(-3deg); scale: 0.7;">',
    content, flags=re.DOTALL
)

# 17. Vinyl Record
content = re.sub(
    r'<!-- 17\. Vinyl Record.*?<div class="floating-sticker" style="bottom:[^>]*>',
    '<!-- 17. Vinyl Record -->\n      <div class="floating-sticker" style="bottom: -5%; right: -5%; z-index: 5; transform: rotate(0deg); scale: 0.85;">',
    content, flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Layout realigned to match screenshot and AGNI C2 removed.")
