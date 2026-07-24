import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS for .journey-path so stroke is light slate blue-gray, dashed 8 8, opacity 0.85
CSS_DASHED_RULE = """<style>
      .interactive-node { transition: all 0.3s ease; }
      .interactive-node:hover { stroke-width: 4; cursor: pointer; fill: rgba(255,255,255,0.8); }
      .hover-card:hover ~ svg .interactive-node { transform: scale(1.1); transform-origin: center; }
      .journey-path {
        stroke: #64748b !important;
        stroke-width: 2.5px !important;
        stroke-dasharray: 8 8 !important;
        stroke-opacity: 0.85 !important;
        stroke-linecap: round !important;
        stroke-linejoin: round !important;
      }
    </style>"""

OLD_CSS = re.search(r'<style>.*?</style>', content, re.DOTALL).group(0)
content = content.replace(OLD_CSS, CSS_DASHED_RULE)

# 2. Update setPath to make sure strokeDashoffset is cleared so path is 100% visible
content = content.replace(
    "el.style.strokeDasharray = '8 8';",
    "el.style.strokeDashoffset = '0';"
)

# 3. Simplify Scroll-draw config so paths fade/light up smoothly on scroll without being hidden by broken dashoffset
OLD_DRAW_LOGIC = re.search(r'// ─── Scroll-draw config \(Smooth progressive path draw\) ───.*?// ─── Achievements Horizontal scroll', content, re.DOTALL).group(0)

NEW_DRAW_LOGIC = """// ─── Scroll-draw config (Fade and Node reveal on scroll) ───
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

          path.style.strokeDashoffset = '0';
          
          gsap.fromTo(path, 
            { opacity: 0.3 },
            {
              opacity: 1,
              ease: "none",
              scrollTrigger: {
                trigger: seg.triggerId,
                start: seg.start,
                end: seg.end,
                scrub: 0.3,
                onUpdate: (self) => {
                  if (nodeEnd) {
                    nodeEnd.style.opacity = self.progress > 0.5 ? '1' : '0';
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

print("Successfully updated dashed arrows to be 100% visible, crisp, and animated on scroll.")
