import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS rules for .journey-path to guarantee stroke-dasharray: 8px 8px !important;
CSS_DASHED_RULE = """
      .journey-path {
        stroke: #94a3b8 !important;
        stroke-width: 2.2px !important;
        stroke-dasharray: 8px 8px !important;
        stroke-linecap: round !important;
        stroke-linejoin: round !important;
      }
"""

if '.journey-path {' not in content:
    content = content.replace('</style>', CSS_DASHED_RULE + '\n    </style>', 1)

# 2. Fix JS setPath(id, d) so it does NOT wipe strokeDasharray
content = content.replace(
    "el.style.strokeDasharray  = '';",
    "// keep dashed style intact"
)

# 3. Clean existing tape divs if any
content = re.sub(r'<div class="absolute -top-4 [^"]*"></div>\n?', '', content)
content = re.sub(r'<div class="absolute -top-5 [^"]*"></div>\n?', '', content)

# 4. Insert visible paper washi tape strips on top of each card outer wrapper

# Card 1: Hero Card (Lime Tape)
content = re.sub(
    r'<div class="absolute top-\[80px\] left-\[80px\] w-\[420px\] z-20 hover-card rotate-\[-1\.5deg\] hover:rotate-0 transition-transform duration-500" id="node-hero">',
    '<div class="absolute top-[80px] left-[80px] w-[420px] z-20 hover-card rotate-[-1.5deg] hover:rotate-0 transition-transform duration-500" id="node-hero" style="overflow: visible;">\n  <div class="absolute -top-5 left-1/2 -translate-x-1/2 w-14 h-8 z-40 pointer-events-none" style="background: rgba(132, 204, 22, 0.88); transform: translateX(-50%) rotate(-3deg); box-shadow: 0 2px 8px rgba(0,0,0,0.15); border-left: 2px dashed rgba(255,255,255,0.5); border-right: 2px dashed rgba(255,255,255,0.5);"></div>',
    content
)

# Card 2: Girl Card (Hot-Pink Tape)
content = re.sub(
    r'<div class="absolute top-\[540px\] right-\[80px\] w-\[360px\] z-20 hover-card rotate-\[1\.5deg\] hover:rotate-0 transition-transform duration-500" id="trigger-girl">',
    '<div class="absolute top-[540px] right-[80px] w-[360px] z-20 hover-card rotate-[1.5deg] hover:rotate-0 transition-transform duration-500" id="trigger-girl" style="overflow: visible;">\n  <div class="absolute -top-5 left-1/2 -translate-x-1/2 w-14 h-8 z-40 pointer-events-none" style="background: rgba(236, 72, 153, 0.88); transform: translateX(-50%) rotate(4deg); box-shadow: 0 2px 8px rgba(0,0,0,0.15); border-left: 2px dashed rgba(255,255,255,0.5); border-right: 2px dashed rgba(255,255,255,0.5);"></div>',
    content
)

# Card 3: LinkedIn Card (Cyan Tape)
content = re.sub(
    r'<div class="absolute top-\[1400px\] left-\[80px\] w-\[340px\] z-30 hover-card rotate-\[-1\.2deg\] hover:rotate-0 transition-transform duration-500" id="node-linkedin">',
    '<div class="absolute top-[1400px] left-[80px] w-[340px] z-30 hover-card rotate-[-1.2deg] hover:rotate-0 transition-transform duration-500" id="node-linkedin" style="overflow: visible;">\n  <div class="absolute -top-5 left-1/2 -translate-x-1/2 w-14 h-8 z-40 pointer-events-none" style="background: rgba(6, 182, 212, 0.88); transform: translateX(-50%) rotate(-3deg); box-shadow: 0 2px 8px rgba(0,0,0,0.15); border-left: 2px dashed rgba(255,255,255,0.5); border-right: 2px dashed rgba(255,255,255,0.5);"></div>',
    content
)

# Card 4: GitHub Card (Amber Tape)
content = re.sub(
    r'<div class="absolute top-\[1840px\] right-\[80px\] w-\[340px\] z-30 hover-card rotate-\[1\.5deg\] hover:rotate-0 transition-transform duration-500" id="node-github">',
    '<div class="absolute top-[1840px] right-[80px] w-[340px] z-30 hover-card rotate-[1.5deg] hover:rotate-0 transition-transform duration-500" id="node-github" style="overflow: visible;">\n  <div class="absolute -top-5 left-1/2 -translate-x-1/2 w-14 h-8 z-40 pointer-events-none" style="background: rgba(245, 158, 11, 0.88); transform: translateX(-50%) rotate(3deg); box-shadow: 0 2px 8px rgba(0,0,0,0.15); border-left: 2px dashed rgba(255,255,255,0.5); border-right: 2px dashed rgba(255,255,255,0.5);"></div>',
    content
)

# Card 5: Shavira Card (Purple Tape)
content = re.sub(
    r'<div class="absolute top-\[2280px\] left-\[80px\] w-\[340px\] z-30 hover-card rotate-\[-1\.5deg\] hover:rotate-0 transition-transform duration-500" id="trigger-shavira">',
    '<div class="absolute top-[2280px] left-[80px] w-[340px] z-30 hover-card rotate-[-1.5deg] hover:rotate-0 transition-transform duration-500" id="trigger-shavira" style="overflow: visible;">\n  <div class="absolute -top-5 left-1/2 -translate-x-1/2 w-14 h-8 z-40 pointer-events-none" style="background: rgba(168, 85, 247, 0.88); transform: translateX(-50%) rotate(-4deg); box-shadow: 0 2px 8px rgba(0,0,0,0.15); border-left: 2px dashed rgba(255,255,255,0.5); border-right: 2px dashed rgba(255,255,255,0.5);"></div>',
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully enforced dashed SVG paths and visible washi paper tape strips.")
