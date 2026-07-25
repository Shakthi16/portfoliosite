import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# 1. Clean garbled CP1252/UTF-8 symbols across the file
replacements = {
    'ΓÖí': '♡',
    'ΓÇó': '•',
    'Γÿ╛': '✦',
    'ΓÖí': '♡',
    '≡ƒôÄ': '📌',
    '┬⌐': '©',
    'ΓÇö': '—',
}

for bad_symbol, good_symbol in replacements.items():
    html = html.replace(bad_symbol, good_symbol)

# 2. Fix "today's focus" Note Card Z-index & Positioning (Line ~3550)
old_today_focus = '''      <!-- 3. "today's focus" Note -->
      <div class="floating-sticker" style="top: 42%; left: 8%; z-index: 8; transform: rotate(2deg); scale: 0.85;">'''

new_today_focus = '''      <!-- 3. "today's focus" Note -->
      <div class="floating-sticker" style="top: 48%; left: 8%; z-index: 40; transform: rotate(2deg); scale: 0.85;">'''

if old_today_focus in html:
    html = html.replace(old_today_focus, new_today_focus)
    print("Updated today's focus z-index and top offset!")
else:
    # Regex fallback if exact whitespace differs
    html = re.sub(
        r'<!-- 3\. "today\'s focus" Note -->\s*<div class="floating-sticker" style="[^"]*">',
        '<!-- 3. "today\'s focus" Note -->\n      <div class="floating-sticker" style="top: 48%; left: 8%; z-index: 40; transform: rotate(2deg); scale: 0.85;">',
        html
    )

# 3. Remove the torn paper layer divider between #home and #about-journal
layer_pattern = r'<!-- REALISTIC DECKLE-EDGE TORN PAPER SEPARATION DIVIDER \(TOP\) -->\s*<div class="w-full relative z-30 pointer-events-none -mb-1 overflow-hidden">[\s\S]*?</div>'

if re.search(layer_pattern, html):
    html = re.sub(layer_pattern, '', html)
    print("Removed torn paper layer divider between homepage and journal!")

# 4. Save clean UTF-8
with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESSFULLY CLEANED UTF-8 SYMBOLS, FIXED CARD LAYERING, AND REMOVED TORN LAYER!")
