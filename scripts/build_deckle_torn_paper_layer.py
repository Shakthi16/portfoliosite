import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# -------------------------------------------------------------
# EXACT DECKLE-EDGE TORN PAPER FRINGE SVG (MATCHING IMAGE 2 & SMRITI RAWAT SITE)
# -------------------------------------------------------------
DECKLE_TORN_PAPER_TOP = """<!-- REALISTIC DECKLE-EDGE TORN PAPER SEPARATION DIVIDER (MATCHING IMAGE 2 EXACTLY) -->
<div class="w-full relative z-20 pointer-events-none -mb-1 bg-white">
  <svg class="w-full h-7 md:h-11 text-[#f4efe6] fill-current block" viewBox="0 0 1200 80" preserveAspectRatio="none">
    <path d="M0,0 L0,35 L15,38 L30,32 L45,41 L60,34 L75,39 L90,31 L105,37 L120,33 L135,42 L150,36 L165,40 L180,31 L195,38 L210,33 L225,41 L240,35 L255,39 L270,32 L285,38 L300,34 L315,40 L330,31 L345,39 L360,33 L375,41 L390,35 L405,38 L420,32 L435,40 L450,34 L465,39 L480,31 L495,38 L510,33 L525,42 L540,36 L555,40 L570,32 L585,39 L600,33 L615,41 L630,35 L645,38 L660,32 L675,40 L690,34 L705,39 L720,31 L735,38 L750,33 L765,42 L780,36 L795,40 L810,32 L825,39 L840,33 L855,41 L870,35 L885,38 L900,32 L915,40 L930,34 L945,39 L960,31 L975,38 L990,33 L1005,42 L1020,36 L1035,40 L1050,32 L1065,39 L1080,33 L1095,41 L1110,35 L1125,38 L1140,32 L1155,40 L1170,34 L1185,39 L1200,31 L1200,80 L0,80 Z"></path>
  </svg>
</div>"""

DECKLE_TORN_PAPER_BOTTOM = """<!-- REALISTIC DECKLE-EDGE TORN PAPER BOTTOM SEPARATION DIVIDER -->
<div class="w-full relative z-20 pointer-events-none -mt-1 bg-[#f4efe6]">
  <svg class="w-full h-7 md:h-11 text-white fill-current block" viewBox="0 0 1200 80" preserveAspectRatio="none">
    <path d="M0,0 L15,9 L30,3 L45,12 L60,5 L75,10 L90,2 L105,8 L120,4 L135,13 L150,7 L165,11 L180,2 L195,9 L210,4 L225,12 L240,6 L255,10 L270,3 L285,9 L300,5 L315,11 L330,2 L345,10 L360,4 L375,12 L390,6 L405,9 L420,3 L435,11 L450,5 L465,10 L480,2 L495,9 L510,4 L525,13 L540,7 L555,11 L570,3 L585,10 L600,4 L615,12 L630,6 L645,9 L660,3 L675,11 L690,5 L705,10 L720,2 L735,9 L750,4 L765,13 L780,7 L795,11 L810,3 L825,10 L840,4 L855,12 L870,6 L885,9 L900,3 L915,11 L930,5 L945,10 L960,2 L975,9 L990,4 L1005,13 L1020,7 L1035,11 L1050,3 L1065,10 L1080,4 L1095,12 L1110,6 L1125,9 L1140,3 L1155,11 L1170,5 L1185,10 L1200,2 L1200,80 L0,80 Z"></path>
  </svg>
</div>"""

# Replace top wave divider in index.html
content = re.sub(r'<!-- PAPER WAVE LAYER TRANSITION.*?</div>', DECKLE_TORN_PAPER_TOP, content, flags=re.DOTALL)
content = re.sub(r'<!-- REALISTIC DECKLE-EDGE TORN PAPER BOTTOM SEPARATION DIVIDER.*?</div>', DECKLE_TORN_PAPER_BOTTOM, content, flags=re.DOTALL)
content = re.sub(r'<!-- TORN PAPER BOTTOM LAYER DIVIDER.*?</div>', DECKLE_TORN_PAPER_BOTTOM, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully replaced smooth wave with authentic deckle-edge torn paper fringe matching Image 2!")
