import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace anchors and SEG 1 path calculation in buildJourneyPaths
OLD_PATHS_BLOCK = """          // ─── Anchor points ─────────────────────────────────
          //   (selector, fraction_of_width, fraction_of_height)
          const H_bot  = vb('#node-hero',        0.5,  1.02);  // hero card bottom-center
          const G_top  = vb('#trigger-girl',     0.5, -0.02);  // girl card top-center
          const G_bot  = vb('#trigger-girl',     0.5,  1.02);  // girl card bottom-center
          const O_top  = vb('#trigger-orbital',  0.5, -0.02);  // orbital top-center
          const O_bot  = vb('#trigger-orbital',  0.5,  1.02);  // orbital bottom-center
          const LI_top = vb('#node-linkedin',    0.5, -0.02);  // linkedin top-center
          const LI_r   = vb('#node-linkedin',    1.02, 0.5);   // linkedin right-center
          const GH_top = vb('#node-github',      0.5, -0.02);  // github top-center
          const GH_l   = vb('#node-github',      -0.02, 0.5);  // github left-center
          const SH_top = vb('#trigger-shavira',  0.5, -0.02);  // shavira top-center  // crafting text left

          if (!H_bot || !G_top || !G_bot || !O_top || !O_bot || !LI_top || !LI_r || !GH_top || !GH_l || !SH_top) {
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
          // Exiting down from Girl bottom, curving left above text-premium in the open horizontal gap, into Orbital top
          {
            const cp1 = { x: G_bot.x, y: G_bot.y + 70 };
            const cp2 = { x: O_top.x + 100, y: O_top.y - 70 };
            setPath('seg-1',
              `M ${G_bot.x} ${G_bot.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${O_top.x} ${O_top.y}`
            );
            mv('n1-end', O_top.x, O_top.y);
          }"""

NEW_PATHS_BLOCK = """          // ─── Anchor points ─────────────────────────────────
          //   (selector, fraction_of_width, fraction_of_height)
          const H_bot  = vb('#node-hero',        0.5,  1.02);  // hero card bottom-center
          const G_top  = vb('#trigger-girl',     0.5, -0.02);  // girl card top-center
          const G_bot  = vb('#trigger-girl',     0.5,  1.02);  // girl card bottom-center
          const O_r    = vb('#trigger-orbital',  1.02, 0.5);   // orbital right edge
          const O_bot  = vb('#trigger-orbital',  0.5,  1.02);  // orbital bottom-center
          const LI_top = vb('#node-linkedin',    0.5, -0.02);  // linkedin top-center
          const LI_r   = vb('#node-linkedin',    1.02, 0.5);   // linkedin right-center
          const GH_top = vb('#node-github',      0.5, -0.02);  // github top-center
          const GH_l   = vb('#node-github',      -0.02, 0.5);  // github left-center
          const SH_top = vb('#trigger-shavira',  0.5, -0.02);  // shavira top-center

          if (!H_bot || !G_top || !G_bot || !O_r || !O_bot || !LI_top || !LI_r || !GH_top || !GH_l || !SH_top) {
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
          // Exiting down from Girl bottom, sweeping LOWER below text-premium, into Orbital right edge
          {
            const cp1 = { x: G_bot.x, y: G_bot.y + 280 };
            const cp2 = { x: O_r.x + 180, y: O_r.y + 70 };
            setPath('seg-1',
              `M ${G_bot.x} ${G_bot.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${O_r.x} ${O_r.y}`
            );
            mv('n1-end', O_r.x, O_r.y);
          }"""

content = content.replace(OLD_PATHS_BLOCK, NEW_PATHS_BLOCK)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully lowered SEG 1 curve below text-premium.")
