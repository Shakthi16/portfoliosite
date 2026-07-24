import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update SVG path attributes to Light Dashed stroke lines (Image 2 style)
for i in range(5):
    content = re.sub(
        rf'<path id="seg-{i}" class="journey-path" d="" [^/>]*/>',
        f'<path id="seg-{i}" class="journey-path" d="" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="7 7" stroke-opacity="0.85" stroke-linecap="round" stroke-linejoin="round" />',
        content
    )

# 2. Add realistic top-center colored paper tape strips to all 5 box cards

# Card 1: Hero Card (Lime Tape top-center)
content = re.sub(
    r'<div class="absolute top-\[80px\] left-\[80px\] w-\[420px\] z-20 hover-card rotate-\[-1\.5deg\] hover:rotate-0 transition-transform duration-500" id="node-hero">',
    '<div class="absolute top-[80px] left-[80px] w-[420px] z-20 hover-card rotate-[-1.5deg] hover:rotate-0 transition-transform duration-500" id="node-hero">\n<div class="absolute -top-4 left-1/2 -translate-x-1/2 w-10 h-8 bg-[#84cc16]/80 backdrop-blur-[1px] shadow-sm rotate-[-2deg] z-30 pointer-events-none rounded-xs border-t border-b border-white/40 opacity-90"></div>',
    content
)

# Card 2: Girl Card (Hot-Pink Tape top-center)
content = re.sub(
    r'<div class="absolute top-\[540px\] right-\[80px\] w-\[360px\] z-20 hover-card rotate-\[1\.5deg\] hover:rotate-0 transition-transform duration-500" id="trigger-girl">',
    '<div class="absolute top-[540px] right-[80px] w-[360px] z-20 hover-card rotate-[1.5deg] hover:rotate-0 transition-transform duration-500" id="trigger-girl">\n<div class="absolute -top-4 left-1/2 -translate-x-1/2 w-10 h-8 bg-[#ec4899]/80 backdrop-blur-[1px] shadow-sm rotate-[3deg] z-30 pointer-events-none rounded-xs border-t border-b border-white/40 opacity-90"></div>',
    content
)

# Card 3: LinkedIn Card (Cyan Tape top-center)
content = re.sub(
    r'<div class="absolute top-\[1400px\] left-\[80px\] w-\[340px\] z-30 hover-card rotate-\[-1\.2deg\] hover:rotate-0 transition-transform duration-500" id="node-linkedin">',
    '<div class="absolute top-[1400px] left-[80px] w-[340px] z-30 hover-card rotate-[-1.2deg] hover:rotate-0 transition-transform duration-500" id="node-linkedin">\n<div class="absolute -top-4 left-1/2 -translate-x-1/2 w-10 h-8 bg-[#06b6d4]/80 backdrop-blur-[1px] shadow-sm rotate-[-3deg] z-30 pointer-events-none rounded-xs border-t border-b border-white/40 opacity-90"></div>',
    content
)

# Card 4: GitHub Card (Amber Tape top-center)
content = re.sub(
    r'<div class="absolute top-\[1840px\] right-\[80px\] w-\[340px\] z-30 hover-card rotate-\[1\.5deg\] hover:rotate-0 transition-transform duration-500" id="node-github">',
    '<div class="absolute top-[1840px] right-[80px] w-[340px] z-30 hover-card rotate-[1.5deg] hover:rotate-0 transition-transform duration-500" id="node-github">\n<div class="absolute -top-4 left-1/2 -translate-x-1/2 w-10 h-8 bg-[#f59e0b]/80 backdrop-blur-[1px] shadow-sm rotate-[2.5deg] z-30 pointer-events-none rounded-xs border-t border-b border-white/40 opacity-90"></div>',
    content
)

# Card 5: Shavira Card (Purple Tape top-center)
content = re.sub(
    r'<div class="absolute top-\[2280px\] left-\[80px\] w-\[340px\] z-30 hover-card rotate-\[-1\.5deg\] hover:rotate-0 transition-transform duration-500" id="trigger-shavira">',
    '<div class="absolute top-[2280px] left-[80px] w-[340px] z-30 hover-card rotate-[-1.5deg] hover:rotate-0 transition-transform duration-500" id="trigger-shavira">\n<div class="absolute -top-4 left-1/2 -translate-x-1/2 w-10 h-8 bg-[#a855f7]/80 backdrop-blur-[1px] shadow-sm rotate-[-2deg] z-30 pointer-events-none rounded-xs border-t border-b border-white/40 opacity-90"></div>',
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully added top-center paper tape strips to box cards and set light-dashed SVG arrow lines.")
