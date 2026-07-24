import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update section background to Sky & Cloud gradient with overflow-hidden
content = content.replace(
    'class="editorial-canvas font-sans relative z-20 overflow-hidden bg-[#FAFAFA] text-[#1F1F1F]" id="about"',
    'class="editorial-canvas font-sans relative z-20 overflow-hidden bg-gradient-to-b from-[#dbeafe] via-[#eff6ff] to-[#faf8f5] text-[#1F1F1F]" id="about"'
)
content = content.replace(
    'class="editorial-canvas font-sans relative z-20 overflow-hidden bg-gradient-to-b from-[#dbeafe] via-[#eff6ff] to-[#faf8f5] text-[#1F1F1F]" id="about"',
    'class="editorial-canvas font-sans relative z-20 overflow-hidden bg-gradient-to-b from-[#dbeafe] via-[#eff6ff] to-[#faf8f5] text-[#1F1F1F]" id="about"'
)

# 2. Add Floating Sky Cloud SVG Backdrop Graphics inside #about
CLOUD_BACKDROP = """<!-- Floating Sky Cloud Backdrop Graphics (Award-winning Sky Theme) -->
<div class="absolute top-[60px] left-[-40px] opacity-40 pointer-events-none z-0 animate-[float_18s_ease-in-out_infinite_alternate]">
  <svg width="340" height="180" viewBox="0 0 240 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M50 80C30 80 15 65 15 48C15 32 28 20 44 20C50 10 65 2 82 2C102 2 118 14 124 28C132 22 142 20 152 20C172 20 188 34 190 52C205 54 216 66 216 80C216 96 202 108 185 108H50Z" fill="white" fill-opacity="0.85" filter="drop-shadow(0px 20px 30px rgba(186,230,253,0.6))"/>
  </svg>
</div>

<div class="absolute top-[650px] right-[-60px] opacity-45 pointer-events-none z-0 animate-[float_22s_ease-in-out_infinite_alternate-reverse]">
  <svg width="420" height="220" viewBox="0 0 240 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M50 80C30 80 15 65 15 48C15 32 28 20 44 20C50 10 65 2 82 2C102 2 118 14 124 28C132 22 142 20 152 20C172 20 188 34 190 52C205 54 216 66 216 80C216 96 202 108 185 108H50Z" fill="white" fill-opacity="0.8" filter="drop-shadow(0px 25px 35px rgba(186,230,253,0.5))"/>
  </svg>
</div>

<div class="absolute top-[1350px] left-[-30px] opacity-35 pointer-events-none z-0 animate-[float_20s_ease-in-out_infinite_alternate]">
  <svg width="360" height="190" viewBox="0 0 240 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M50 80C30 80 15 65 15 48C15 32 28 20 44 20C50 10 65 2 82 2C102 2 118 14 124 28C132 22 142 20 152 20C172 20 188 34 190 52C205 54 216 66 216 80C216 96 202 108 185 108H50Z" fill="white" fill-opacity="0.8" filter="drop-shadow(0px 20px 30px rgba(186,230,253,0.5))"/>
  </svg>
</div>

<div class="absolute top-[2050px] right-[-50px] opacity-40 pointer-events-none z-0 animate-[float_24s_ease-in-out_infinite_alternate-reverse]">
  <svg width="380" height="200" viewBox="0 0 240 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M50 80C30 80 15 65 15 48C15 32 28 20 44 20C50 10 65 2 82 2C102 2 118 14 124 28C132 22 142 20 152 20C172 20 188 34 190 52C205 54 216 66 216 80C216 96 202 108 185 108H50Z" fill="white" fill-opacity="0.85" filter="drop-shadow(0px 20px 30px rgba(186,230,253,0.5))"/>
  </svg>
</div>
"""

if '<!-- Floating Sky Cloud Backdrop Graphics' not in content:
    content = content.replace(
        '<div class="relative w-full max-w-[1400px] mx-auto px-6 lg:px-12 z-10 hidden md:block" id="timeline-container" style="height: 2700px;">',
        CLOUD_BACKDROP + '\n<div class="relative w-full max-w-[1400px] mx-auto px-6 lg:px-12 z-10 hidden md:block" id="timeline-container" style="height: 2700px;">'
    )

# 3. Update SVG paths to be dashed connecting curve lines (Image 1 style)
content = re.sub(
    r'<path id="seg-0" class="journey-path" d=""\s+fill="none" stroke="[^"]*" stroke-width="[^"]*" stroke-opacity="[^"]*"',
    '<path id="seg-0" class="journey-path" d="" fill="none" stroke="#475569" stroke-width="2.2" stroke-dasharray="10 10" stroke-opacity="0.85"',
    content
)
content = re.sub(
    r'<path id="seg-1" class="journey-path" d=""\s+fill="none" stroke="[^"]*" stroke-width="[^"]*" stroke-opacity="[^"]*"',
    '<path id="seg-1" class="journey-path" d="" fill="none" stroke="#475569" stroke-width="2.2" stroke-dasharray="10 10" stroke-opacity="0.85"',
    content
)
content = re.sub(
    r'<path id="seg-2" class="journey-path" d=""\s+fill="none" stroke="[^"]*" stroke-width="[^"]*" stroke-opacity="[^"]*"',
    '<path id="seg-2" class="journey-path" d="" fill="none" stroke="#475569" stroke-width="2.2" stroke-dasharray="10 10" stroke-opacity="0.85"',
    content
)
content = re.sub(
    r'<path id="seg-3" class="journey-path" d=""\s+fill="none" stroke="[^"]*" stroke-width="[^"]*" stroke-opacity="[^"]*"',
    '<path id="seg-3" class="journey-path" d="" fill="none" stroke="#475569" stroke-width="2.2" stroke-dasharray="10 10" stroke-opacity="0.85"',
    content
)
content = re.sub(
    r'<path id="seg-4" class="journey-path" d=""\s+fill="none" stroke="[^"]*" stroke-width="[^"]*" stroke-opacity="[^"]*"',
    '<path id="seg-4" class="journey-path" d="" fill="none" stroke="#475569" stroke-width="2.2" stroke-dasharray="10 10" stroke-opacity="0.85"',
    content
)

# 4. Add tactile color washi tape clips & numbered badges {01}, {02}, {03}, {04}, {05}

# Hero cardwas tape + rot
content = re.sub(
    r'<div class="absolute top-\[120px\] right-\[80px\] w-\[480px\] z-20 text-center" id="text-hero">\s*<h1',
    '<div class="absolute top-[120px] right-[80px] w-[480px] z-20 text-center" id="text-hero">\n<span class="inline-block px-3.5 py-1 bg-lime-100/90 text-lime-800 font-mono text-xs font-bold rounded-full mb-3 shadow-xs border border-lime-200">{01}</span>\n<h1',
    content
)
content = re.sub(
    r'<div class="absolute top-\[80px\] left-\[80px\] w-\[420px\] z-20 hover-card" id="node-hero">',
    '<div class="absolute top-[80px] left-[80px] w-[420px] z-20 hover-card rotate-[-1.5deg] hover:rotate-0 transition-transform duration-500" id="node-hero">\n<div class="absolute -top-3 left-10 w-16 h-7 bg-lime-300/90 shadow-md rotate-[-6deg] z-30 pointer-events-none rounded-xs border-t border-b border-white/50"></div>',
    content
)

# Step 02: Girl card tape & text-premium {02} badge
content = re.sub(
    r'<div class="absolute top-\[940px\] left-\[480px\] w-\[440px\] z-20 text-left" id="text-premium">\s*<h2',
    '<div class="absolute top-[940px] left-[480px] w-[440px] z-20 text-left" id="text-premium">\n<span class="inline-block px-3.5 py-1 bg-pink-100/90 text-pink-800 font-mono text-xs font-bold rounded-full mb-3 shadow-xs border border-pink-200">{02}</span>\n<h2',
    content
)
content = re.sub(
    r'<div class="absolute top-\[540px\] right-\[80px\] w-\[360px\] z-20 hover-card" id="trigger-girl">',
    '<div class="absolute top-[540px] right-[80px] w-[360px] z-20 hover-card rotate-[1.5deg] hover:rotate-0 transition-transform duration-500" id="trigger-girl">\n<div class="absolute -top-3 right-12 w-16 h-7 bg-pink-400/90 shadow-md rotate-[5deg] z-30 pointer-events-none rounded-xs border-t border-b border-white/50"></div>',
    content
)

# Step 03: LinkedIn card tape & text-linkedin {03} badge
content = re.sub(
    r'<div class="absolute top-\[1400px\] left-\[480px\] w-\[480px\] z-20 text-left" id="text-linkedin">\s*<h2',
    '<div class="absolute top-[1400px] left-[480px] w-[480px] z-20 text-left" id="text-linkedin">\n<span class="inline-block px-3.5 py-1 bg-cyan-100/90 text-cyan-800 font-mono text-xs font-bold rounded-full mb-3 shadow-xs border border-cyan-200">{03}</span>\n<h2',
    content
)
content = re.sub(
    r'<div class="absolute top-\[1400px\] left-\[80px\] w-\[340px\] z-30 hover-card" id="node-linkedin">',
    '<div class="absolute top-[1400px] left-[80px] w-[340px] z-30 hover-card rotate-[-1.2deg] hover:rotate-0 transition-transform duration-500" id="node-linkedin">\n<div class="absolute -top-3 left-12 w-16 h-7 bg-cyan-300/90 shadow-md rotate-[-3deg] z-30 pointer-events-none rounded-xs border-t border-b border-white/50"></div>',
    content
)

# Step 04: GitHub card tape & text-github {04} badge
content = re.sub(
    r'<div class="absolute top-\[1840px\] right-\[480px\] w-\[480px\] z-20 text-left" id="text-github">\s*<h2',
    '<div class="absolute top-[1840px] right-[480px] w-[480px] z-20 text-left" id="text-github">\n<span class="inline-block px-3.5 py-1 bg-amber-100/90 text-amber-800 font-mono text-xs font-bold rounded-full mb-3 shadow-xs border border-amber-200">{04}</span>\n<h2',
    content
)
content = re.sub(
    r'<div class="absolute top-\[1840px\] right-\[80px\] w-\[340px\] z-30 hover-card" id="node-github">',
    '<div class="absolute top-[1840px] right-[80px] w-[340px] z-30 hover-card rotate-[1.5deg] hover:rotate-0 transition-transform duration-500" id="node-github">\n<div class="absolute -top-3 right-10 w-16 h-7 bg-amber-300/90 shadow-md rotate-[4deg] z-30 pointer-events-none rounded-xs border-t border-b border-white/50"></div>',
    content
)

# Step 05: Shavira card tape & trigger-crafting {05} badge
content = re.sub(
    r'<div class="absolute top-\[2280px\] left-\[480px\] w-\[480px\] z-20 text-left" id="trigger-crafting">\s*<h2',
    '<div class="absolute top-[2280px] left-[480px] w-[480px] z-20 text-left" id="trigger-crafting">\n<span class="inline-block px-3.5 py-1 bg-purple-100/90 text-purple-800 font-mono text-xs font-bold rounded-full mb-3 shadow-xs border border-purple-200">{05}</span>\n<h2',
    content
)
content = re.sub(
    r'<div class="absolute top-\[2280px\] left-\[80px\] w-\[340px\] z-30 hover-card" id="trigger-shavira">',
    '<div class="absolute top-[2280px] left-[80px] w-[340px] z-30 hover-card rotate-[-1.5deg] hover:rotate-0 transition-transform duration-500" id="trigger-shavira">\n<div class="absolute -top-3 left-10 w-16 h-7 bg-purple-300/90 shadow-md rotate-[-4deg] z-30 pointer-events-none rounded-xs border-t border-b border-white/50"></div>',
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully applied Sky backdrop, dashed connecting lines, colored washi tape clips, and numbered badges.")
