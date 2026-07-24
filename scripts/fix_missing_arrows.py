import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean CSS for .journey-path so it doesn't force solid stroke
OLD_CSS = re.search(r'<style>.*?</style>', content, re.DOTALL).group(0)

NEW_CSS = """<style>
      .interactive-node { transition: all 0.3s ease; }
      .interactive-node:hover { stroke-width: 4; cursor: pointer; fill: rgba(255,255,255,0.8); }
      .hover-card:hover ~ svg .interactive-node { transform: scale(1.1); transform-origin: center; }
      .journey-path {
        stroke: #94a3b8;
        stroke-width: 2.2px;
        stroke-dasharray: 8 8;
        stroke-linecap: round;
        stroke-linejoin: round;
      }
    </style>"""

content = content.replace(OLD_CSS, NEW_CSS)

# 2. Update setPath to preserve inline stroke-dasharray="8 8"
content = content.replace(
    "// keep dashed style intact\n            el.style.strokeDashoffset = '';",
    "el.style.strokeDasharray = '8 8';"
)

# 3. Update Scroll-draw config so paths reveal as dashed lines and start visible if scrolled into view
OLD_DRAW_LOGIC = re.search(r'// ─── Scroll-draw config \(Smooth progressive path draw\) ───.*?// ─── Achievements Horizontal scroll', content, re.DOTALL).group(0)

NEW_DRAW_LOGIC = """// ─── Scroll-draw config (Smooth progressive path draw) ───
        const segments = [
          { pathId: 'seg-0', nodeEndId: 'n0-end', triggerId: '#text-hero',      start: "top 90%", end: "top 30%" },
          { pathId: 'seg-1', nodeEndId: 'n1-end', triggerId: '#text-premium',   start: "top 90%", end: "top 30%" },
          { pathId: 'seg-2', nodeEndId: 'n2-end', triggerId: '#node-linkedin',  start: "top 90%", end: "top 30%" },
          { pathId: 'seg-3', nodeEndId: 'n3-end', triggerId: '#text-github',    start: "top 90%", end: "top 30%" },
          { pathId: 'seg-4', nodeEndId: 'n4-end', triggerId: '#trigger-crafting',start: "top 90%", end: "top 30%" }
        ];

        segments.forEach(seg => {
          const path = document.getElementById(seg.pathId);
          const nodeEnd = document.getElementById(seg.nodeEndId);
          if (!path) return;

          path.style.strokeDasharray = '8 8';
          const length = path.getTotalLength() || 1000;
          
          gsap.fromTo(path, 
            { strokeDashoffset: length },
            {
              strokeDashoffset: 0,
              ease: "none",
              scrollTrigger: {
                trigger: seg.triggerId,
                start: seg.start,
                end: seg.end,
                scrub: 0.3,
                onUpdate: (self) => {
                  if (nodeEnd) {
                    nodeEnd.style.opacity = self.progress > 0.8 ? '1' : '0';
                  }
                }
              }
            }
          );
        });

        // ─── Achievements Horizontal scroll"""

content = content.replace(OLD_DRAW_LOGIC, NEW_DRAW_LOGIC)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully fixed missing SVG paths so dashed lines are 100% visible and draw smoothly on scroll.")
