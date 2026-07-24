import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update text-premium position: top-[940px] left-[480px] w-[440px]
content = re.sub(
    r'<div class="[^"]*" id="text-premium">',
    '<div class="absolute top-[940px] left-[480px] w-[440px] z-20 text-left" id="text-premium">',
    content
)

# 2. Update text-linkedin position: top-[1400px] left-[480px] w-[480px]
content = re.sub(
    r'<div class="[^"]*" id="text-linkedin">',
    '<div class="absolute top-[1400px] left-[480px] w-[480px] z-20 text-left" id="text-linkedin">',
    content
)

# 3. Update text-github position: top-[1840px] right-[480px] w-[480px]
content = re.sub(
    r'<div class="[^"]*" id="text-github">',
    '<div class="absolute top-[1840px] right-[480px] w-[480px] z-20 text-left" id="text-github">',
    content
)

# 4. Update trigger-crafting position: top-[2280px] left-[480px] w-[480px]
content = re.sub(
    r'<div class="[^"]*" id="trigger-crafting">',
    '<div class="absolute top-[2280px] left-[480px] w-[480px] z-20 text-left" id="trigger-crafting">',
    content
)

# 5. Update buildJourneyPaths anchors and path routing in JS
OLD_BUILD_PATHS = re.search(r'// ─── Anchor points ───.*?// ─── Build paths now & on resize ───', content, re.DOTALL).group(0)

NEW_BUILD_PATHS = """// ─── Anchor points ─────────────────────────────────
          //   (selector, fraction_of_width, fraction_of_height)
          const H_bot  = vb('#node-hero',        0.5,  1.02);  // hero card bottom-center
          const G_top  = vb('#trigger-girl',     0.5, -0.02);  // girl card top-center
          const G_bot  = vb('#trigger-girl',     0.5,  1.02);  // girl card bottom-center
          const O_left = vb('#trigger-orbital',  -0.05, 0.5);  // orbital left edge
          const O_bot  = vb('#trigger-orbital',  0.5,  1.02);  // orbital bottom-center
          const LI_top = vb('#node-linkedin',    0.5, -0.02);  // linkedin top-center
          const LI_r   = vb('#node-linkedin',    1.02, 0.5);   // linkedin right-center
          const GH_top = vb('#node-github',      0.5, -0.02);  // github top-center
          const GH_l   = vb('#node-github',      -0.02, 0.5);  // github left-center
          const SH_top = vb('#trigger-shavira',  0.5, -0.02);  // shavira top-center

          if (!H_bot || !G_top || !G_bot || !O_left || !O_bot || !LI_top || !LI_r || !GH_top || !GH_l || !SH_top) {
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
          // Exiting right from LinkedIn card, dipping below text-linkedin into GitHub top-center
          {
            const cp1 = { x: LI_r.x + 200, y: LI_r.y + 180 };
            const cp2 = { x: GH_top.x, y: GH_top.y - 100 };
            setPath('seg-3',
              `M ${LI_r.x} ${LI_r.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${GH_top.x} ${GH_top.y}`
            );
            mv('n3-end', GH_top.x, GH_top.y);
          }

          // ─── SEG 4: GitHub → Shavira ──────────────────────
          // Exiting left from GitHub card, dipping below text-github into Shavira top-center
          {
            const cp1 = { x: GH_l.x - 200, y: GH_l.y + 180 };
            const cp2 = { x: SH_top.x, y: SH_top.y - 100 };
            setPath('seg-4',
              `M ${GH_l.x} ${GH_l.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${SH_top.x} ${SH_top.y}`
            );
            mv('n4-end', SH_top.x, SH_top.y);
          }
        }

        // ─── Build paths now & on resize ───"""

content = content.replace(OLD_BUILD_PATHS, NEW_BUILD_PATHS)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully moved side text elements and routed SVG paths below all text.")
