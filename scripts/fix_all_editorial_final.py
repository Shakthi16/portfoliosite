import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update section #about background to use sky_clouds_bg.png blended illustration
content = re.sub(
    r'<section class="editorial-canvas font-sans relative z-20 overflow-hidden [^"]*" id="about"',
    '<section class="editorial-canvas font-sans relative z-20 overflow-hidden bg-[#dbeafe] text-[#1F1F1F]" id="about" style="min-height: 2700px; background-image: linear-gradient(to bottom, rgba(219, 234, 254, 0.7), rgba(240, 249, 255, 0.85), rgba(250, 248, 245, 0.95)), url(\'sky_clouds_bg.png\'); background-size: cover; background-position: center; background-repeat: no-repeat;"',
    content
)

# 2. Remove all floating SVG cloud vectors and old washi tape divs
content = re.sub(r'<!-- Floating Sky Cloud Backdrop Graphics.*?</div>\s*</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
content = re.sub(r'<div class="absolute -top-3 [^"]*"></div>\n?', '', content)

# 3. Update numbered badges to clean modern monochrome pills {01}, {02}, {03}, {04}, {05}
content = re.sub(
    r'<span class="inline-block px-3\.5 py-1 bg-lime-100/90 text-lime-800 font-mono text-xs font-bold rounded-full mb-3 shadow-xs border border-lime-200">\{01\}</span>',
    '<span class="inline-block px-3.5 py-1 bg-[#1e293b] text-white font-mono text-xs font-bold rounded-full mb-3 shadow-sm tracking-wider">{01}</span>',
    content
)
content = re.sub(
    r'<span class="inline-block px-3\.5 py-1 bg-pink-100/90 text-pink-800 font-mono text-xs font-bold rounded-full mb-3 shadow-xs border border-pink-200">\{02\}</span>',
    '<span class="inline-block px-3.5 py-1 bg-[#1e293b] text-white font-mono text-xs font-bold rounded-full mb-3 shadow-sm tracking-wider">{02}</span>',
    content
)
content = re.sub(
    r'<span class="inline-block px-3\.5 py-1 bg-cyan-100/90 text-cyan-800 font-mono text-xs font-bold rounded-full mb-3 shadow-xs border border-cyan-200">\{03\}</span>',
    '<span class="inline-block px-3.5 py-1 bg-[#1e293b] text-white font-mono text-xs font-bold rounded-full mb-3 shadow-sm tracking-wider">{03}</span>',
    content
)
content = re.sub(
    r'<span class="inline-block px-3\.5 py-1 bg-amber-100/90 text-amber-800 font-mono text-xs font-bold rounded-full mb-3 shadow-xs border border-amber-200">\{04\}</span>',
    '<span class="inline-block px-3.5 py-1 bg-[#1e293b] text-white font-mono text-xs font-bold rounded-full mb-3 shadow-sm tracking-wider">{04}</span>',
    content
)
content = re.sub(
    r'<span class="inline-block px-3\.5 py-1 bg-purple-100/90 text-purple-800 font-mono text-xs font-bold rounded-full mb-3 shadow-xs border border-purple-200">\{05\}</span>',
    '<span class="inline-block px-3.5 py-1 bg-[#1e293b] text-white font-mono text-xs font-bold rounded-full mb-3 shadow-sm tracking-wider">{05}</span>',
    content
)

# 4. Update SVG path attributes to sleek dark slate stroke lines
for i in range(5):
    content = re.sub(
        rf'<path id="seg-{i}" class="journey-path" d="" [^/>]*/>',
        f'<path id="seg-{i}" class="journey-path" d="" fill="none" stroke="#1e293b" stroke-width="2.2" stroke-opacity="0.85" stroke-linecap="round" stroke-linejoin="round" />',
        content
    )

# 5. Update buildJourneyPaths anchors and path routing to 100% avoid text overlap
OLD_BUILD_PATHS = re.search(r'// ─── Anchor points ───.*?// ─── Build paths now & on resize ───', content, re.DOTALL).group(0)

NEW_BUILD_PATHS = """// ─── Anchor points ─────────────────────────────────
          //   (selector, fraction_of_width, fraction_of_height)
          const H_bot  = vb('#node-hero',        0.5,  1.02);  // hero card bottom-center
          const G_top  = vb('#trigger-girl',     0.5, -0.02);  // girl card top-center
          const G_bot  = vb('#trigger-girl',     0.5,  1.02);  // girl card bottom-center
          const O_left = vb('#trigger-orbital',  -0.05, 0.5);  // orbital left edge
          const O_bot  = vb('#trigger-orbital',  0.5,  1.02);  // orbital bottom-center
          const LI_top = vb('#node-linkedin',    0.5, -0.02);  // linkedin top-center
          const LI_bot = vb('#node-linkedin',    0.5,  1.02);  // linkedin bottom-center
          const GH_top = vb('#node-github',      0.5, -0.02);  // github top-center
          const GH_bot = vb('#node-github',      0.5,  1.02);  // github bottom-center
          const SH_top = vb('#trigger-shavira',  0.5, -0.02);  // shavira top-center

          if (!H_bot || !G_top || !G_bot || !O_left || !O_bot || !LI_top || !LI_bot || !GH_top || !GH_bot || !SH_top) {
            console.warn('Journey arrows: some anchor elements not found.');
            return;
          }

          // ─── SEG 0: Hero → Girl ─────────────────────────────
          // Exiting down from Hero bottom, curving through open center area into Girl top-center
          {
            const cp1 = { x: H_bot.x, y: H_bot.y + 140 };
            const cp2 = { x: G_top.x, y: G_top.y - 140 };
            setPath('seg-0',
              `M ${H_bot.x} ${H_bot.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${G_top.x} ${G_top.y}`
            );
            mv('n0-end', G_top.x, G_top.y);
          }

          // ─── SEG 1: Girl → Orbital ────────────────────────
          // Exiting down from Girl bottom, dipping well BELOW text-premium, into Orbital bottom
          {
            const cp1 = { x: G_bot.x, y: G_bot.y + 360 };
            const cp2 = { x: O_bot.x + 200, y: O_bot.y + 40 };
            setPath('seg-1',
              `M ${G_bot.x} ${G_bot.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${O_bot.x} ${O_bot.y}`
            );
            mv('n1-end', O_bot.x, O_bot.y);
          }

          // ─── SEG 2: Orbital → LinkedIn ────────────────────
          // Exiting from Orbital left edge, looping down into LinkedIn top-center
          {
            const cp1 = { x: O_left.x - 120, y: O_left.y + 160 };
            const cp2 = { x: LI_top.x, y: LI_top.y - 80 };
            setPath('seg-2',
              `M ${O_left.x} ${O_left.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${LI_top.x} ${LI_top.y}`
            );
            mv('n2-end', LI_top.x, LI_top.y);
          }

          // ─── SEG 3: LinkedIn → GitHub ─────────────────────
          // Exiting from LinkedIn BOTTOM (below text-linkedin), sweeping across open space into GitHub top-center
          {
            const cp1 = { x: LI_bot.x, y: LI_bot.y + 140 };
            const cp2 = { x: GH_top.x, y: GH_top.y - 120 };
            setPath('seg-3',
              `M ${LI_bot.x} ${LI_bot.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${GH_top.x} ${GH_top.y}`
            );
            mv('n3-end', GH_top.x, GH_top.y);
          }

          // ─── SEG 4: GitHub → Shavira ──────────────────────
          // Exiting from GitHub BOTTOM (below text-github), sweeping across open space into Shavira top-center
          {
            const cp1 = { x: GH_bot.x, y: GH_bot.y + 140 };
            const cp2 = { x: SH_top.x, y: SH_top.y - 120 };
            setPath('seg-4',
              `M ${GH_bot.x} ${GH_bot.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${SH_top.x} ${SH_top.y}`
            );
            mv('n4-end', SH_top.x, SH_top.y);
          }
        }

        // ─── Build paths now & on resize ───"""

content = content.replace(OLD_BUILD_PATHS, NEW_BUILD_PATHS)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully applied sky_clouds_bg.png background, removed washi tape, updated badges, and fixed SEG 3/SEG 4 path anchors.")
