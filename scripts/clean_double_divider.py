with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the extra wave divider (lines 3869-3875)
double_divider_pattern = """<!-- TORN PAPER TOP LAYER DIVIDER (MATCHING IMAGE 3) -->
<div class="w-full bg-[#faf7f2] relative z-20 pointer-events-none -mb-1">
  <svg class="w-full h-8 md:h-12 text-[#f4efe6] fill-current" viewBox="0 0 1200 120" preserveAspectRatio="none">
    <path d="M0,0 C90,40 180,10 270,30 C360,50 450,20 540,40 C630,60 720,15 810,35 C900,55 990,20 1080,45 C1140,55 1170,25 1200,30 L1200,120 L0,120 Z"></path>
  </svg>
</div>"""

if double_divider_pattern in content:
    content = content.replace(double_divider_pattern, '')
    print("Successfully removed duplicate wave layer divider!")
else:
    # Fallback regex search for duplicate svg before deckle divider
    import re
    content = re.sub(r'<div class="w-full bg-\[#faf7f2\].*?</div>\s*(?=<!-- REALISTIC DECKLE-EDGE)', '', content, flags=re.DOTALL)
    print("Removed duplicate wave divider via regex!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
