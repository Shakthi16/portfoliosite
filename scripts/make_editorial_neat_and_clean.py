import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove jittering CSS driftArrows animation and clean CSS rules for .journey-path
OLD_CSS = re.search(r'<style>.*?</style>', content, re.DOTALL).group(0)

NEW_CSS = """<style>
      .interactive-node { transition: all 0.3s ease; }
      .interactive-node:hover { stroke-width: 4; cursor: pointer; fill: rgba(255,255,255,0.8); }
      .hover-card:hover ~ svg .interactive-node { transform: scale(1.1); transform-origin: center; }
      .journey-path {
        stroke: #64748b !important;
        stroke-width: 2.2px !important;
        stroke-linecap: round !important;
        stroke-linejoin: round !important;
      }
    </style>"""

content = content.replace(OLD_CSS, NEW_CSS)

# 2. Update buildJourneyPaths anchors so destination dots land on card corners (away from tape clips!)
OLD_BUILD_ANCHORS = re.search(r'// ─── Anchor points ───.*?// ─── SEG 0:', content, re.DOTALL).group(0)

NEW_BUILD_ANCHORS = """// ─── Anchor points ─────────────────────────────────
          //   (selector, fraction_of_width, fraction_of_height)
          const H_bot  = vb('#node-hero',        0.5,   1.02);  // hero card bottom-center
          const G_top  = vb('#trigger-girl',     0.18, -0.02);  // girl card top-left (away from tape!)
          const G_bot  = vb('#trigger-girl',     0.5,   1.02);  // girl card bottom-center
          const O_left = vb('#trigger-orbital',  -0.05, 0.5);   // orbital left edge
          const O_bot  = vb('#trigger-orbital',  0.5,   1.02);  // orbital bottom-center
          const LI_top = vb('#node-linkedin',    0.18, -0.02);  // linkedin top-left (away from tape!)
          const LI_bot = vb('#node-linkedin',    0.5,   1.02);  // linkedin bottom-center
          const GH_top = vb('#node-github',      0.82, -0.02);  // github top-right (away from tape!)
          const GH_bot = vb('#node-github',      0.5,   1.02);  // github bottom-center
          const SH_top = vb('#trigger-shavira',  0.18, -0.02);  // shavira top-left (away from tape!)

          if (!H_bot || !G_top || !G_bot || !O_left || !O_bot || !LI_top || !LI_bot || !GH_top || !GH_bot || !SH_top) {
            console.warn('Journey arrows: some anchor elements not found.');
            return;
          }

          // ─── SEG 0:"""

content = content.replace(OLD_BUILD_ANCHORS, NEW_BUILD_ANCHORS)

# 3. Update GSAP scroll-draw logic so paths draw out smoothly from start to finish without jittering
OLD_DRAW_LOGIC = re.search(r'// ─── Scroll-draw config ───.*?// ─── Achievements Horizontal scroll', content, re.DOTALL).group(0)

NEW_DRAW_LOGIC = """// ─── Scroll-draw config (Smooth progressive path draw) ───
        const segments = [
          { pathId: 'seg-0', nodeEndId: 'n0-end', triggerId: '#text-hero',      start: "top 80%", end: "top 40%" },
          { pathId: 'seg-1', nodeEndId: 'n1-end', triggerId: '#text-premium',   start: "top 75%", end: "top 35%" },
          { pathId: 'seg-2', nodeEndId: 'n2-end', triggerId: '#node-linkedin',  start: "top 80%", end: "top 40%" },
          { pathId: 'seg-3', nodeEndId: 'n3-end', triggerId: '#text-github',    start: "top 75%", end: "top 35%" },
          { pathId: 'seg-4', nodeEndId: 'n4-end', triggerId: '#trigger-crafting',start: "top 75%", end: "top 35%" }
        ];

        segments.forEach(seg => {
          const path = document.getElementById(seg.pathId);
          const nodeEnd = document.getElementById(seg.nodeEndId);
          if (!path) return;

          const length = path.getTotalLength();
          path.style.strokeDasharray = length + ' ' + length;
          path.style.strokeDashoffset = length;

          gsap.to(path, {
            strokeDashoffset: 0,
            ease: "none",
            scrollTrigger: {
              trigger: seg.triggerId,
              start: seg.start,
              end: seg.end,
              scrub: 0.5,
              onUpdate: (self) => {
                if (nodeEnd) {
                  if (self.progress > 0.85) {
                    nodeEnd.style.opacity = '1';
                  } else {
                    nodeEnd.style.opacity = '0';
                  }
                }
              }
            }
          });
        });

        // ─── Achievements Horizontal scroll"""

content = content.replace(OLD_DRAW_LOGIC, NEW_DRAW_LOGIC)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully cleaned up layout anchors and implemented smooth progressive path draw animation.")
