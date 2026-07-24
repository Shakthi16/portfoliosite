import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ══════════════════════════════════════════════════
# STEP 1: Replace entire SVG with premium paths
# ══════════════════════════════════════════════════
# 
# ViewBox: 1400 × 2200
# Card layout (in viewBox coordinates):
#   Hero      : top=100, left=100, w=450  → bottom-center ≈ (325, 510)
#   Girl      : top=650, right=100, w=380 → left edge x=920, top-left=(920,660), bottom=(920,1050)
#   Orbital   : top=800, left=200, w=300  → center=(350,950), right edge=(500,950), bottom=(350,1100)
#   "I build" : top=850, left=600, w=350  → top=(600,850), center-left=(600,920)
#   LinkedIn  : top=1250, left=80, w=340, h=320 → right-center=(420,1410), top=(250,1250)
#   Crafting  : top=1500, center x≈700, w=400  → left=(500,1570), right=(900,1570)
#   Shavira   : top=1600, right=80, w=340 → left=(980,1760), top-left=(980,1600)

NEW_SVG = '''<svg class="absolute inset-0 w-full h-full pointer-events-none z-[50]" id="timeline-svg" viewBox="0 0 1400 2200" preserveAspectRatio="xMidYMid meet">
      <defs>
        <!-- Arrowhead marker -->
        <marker id="arrow-tip" viewBox="0 0 12 12" refX="9" refY="6"
                markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 2 2 L 9 6 L 2 10" fill="none" stroke="#1F1F1F"
                stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </marker>

        <!-- Glow filter for nodes -->
        <filter id="glow-sm" x="-100%" y="-100%" width="300%" height="300%">
          <feGaussianBlur stdDeviation="3" result="blur"/>
          <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
        <filter id="glow-lg" x="-150%" y="-150%" width="400%" height="400%">
          <feGaussianBlur stdDeviation="6" result="blur"/>
          <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
      </defs>

      <!--
        PATHS: 5 elegant Bézier segments forming one continuous journey.
        All paths start fully hidden (strokeDashoffset = full length via JS).
        They are revealed progressively as the user scrolls.

        PATH 0: Hero card bottom → Girl card left edge
          Start: (325, 510) — bottom-center of hero card
          End:   (920, 760) — left-center of girl card
          Large sweeping clockwise arc that drops then curves right.

        PATH 1: Girl card bottom → Orbital circle (via S-curve under "I build" text)
          Start: (920, 1050) — bottom-left of girl card
          End:   (500, 955)  — right edge of orbital circle
          S-curve passing behind the "I build" heading.

        PATH 2: Orbital bottom → LinkedIn card top
          Start: (350, 1100) — bottom of orbital
          End:   (250, 1250) — top-left of linkedin card
          Short graceful arc curving left and down.

        PATH 3: LinkedIn right → Crafting text left
          Start: (420, 1410) — right-center of linkedin card
          End:   (500, 1570) — left edge of crafting text block
          Diagonal arc passing through open space.

        PATH 4: Crafting text right → Shavira card top
          Start: (900, 1570) — right edge of crafting text
          End:   (980, 1630) — top-left of shavira card
          Short elegant connector curving right.
      -->

      <!-- ─── SEGMENT 0: Hero → Girl ─── -->
      <path id="seg-0" class="journey-path"
        d="M 325 510
           L 325 570
           C 325 750, 200 780, 380 760
           C 560 740, 780 660, 920 760"
        fill="none" stroke="#1F1F1F" stroke-width="1.3" stroke-opacity="0.82"
        stroke-linecap="round" stroke-linejoin="round"
        marker-end="url(#arrow-tip)" />

      <!-- nodes along seg-0 -->
      <circle id="n0a" class="journey-node" cx="325" cy="510" r="4"
        fill="white" stroke="#421835" stroke-width="2" opacity="0"/>
      <circle id="n0b" class="journey-node" cx="380" cy="760" r="4"
        fill="white" stroke="#421835" stroke-width="2" opacity="0"/>
      <circle id="n0c" class="journey-node" cx="920" cy="760" r="5"
        fill="#421835" stroke="none" filter="url(#glow-sm)" opacity="0"/>

      <!-- ─── SEGMENT 1: Girl → Orbital ─── -->
      <path id="seg-1" class="journey-path"
        d="M 920 1050
           C 780 1100, 680 1080, 620 1020
           C 560 960, 580 900, 600 870
           C 620 840, 580 870, 500 955"
        fill="none" stroke="#1F1F1F" stroke-width="1.3" stroke-opacity="0.82"
        stroke-linecap="round" stroke-linejoin="round"
        marker-end="url(#arrow-tip)" />

      <circle id="n1a" class="journey-node" cx="920" cy="1050" r="4"
        fill="white" stroke="#421835" stroke-width="2" opacity="0"/>
      <circle id="n1b" class="journey-node" cx="620" cy="1020" r="4"
        fill="white" stroke="#421835" stroke-width="2" opacity="0"/>
      <circle id="n1c" class="journey-node" cx="500" cy="955" r="5"
        fill="#421835" stroke="none" filter="url(#glow-sm)" opacity="0"/>

      <!-- ─── SEGMENT 2: Orbital → LinkedIn ─── -->
      <path id="seg-2" class="journey-path"
        d="M 350 1100
           C 340 1150, 300 1180, 260 1210
           C 220 1240, 200 1270, 250 1280"
        fill="none" stroke="#1F1F1F" stroke-width="1.3" stroke-opacity="0.82"
        stroke-linecap="round" stroke-linejoin="round"
        marker-end="url(#arrow-tip)" />

      <circle id="n2a" class="journey-node" cx="350" cy="1100" r="4"
        fill="white" stroke="#421835" stroke-width="2" opacity="0"/>
      <circle id="n2b" class="journey-node" cx="250" cy="1280" r="5"
        fill="#421835" stroke="none" filter="url(#glow-sm)" opacity="0"/>

      <!-- ─── SEGMENT 3: LinkedIn → Crafting Text ─── -->
      <path id="seg-3" class="journey-path"
        d="M 420 1420
           C 460 1400, 480 1450, 490 1490
           C 500 1530, 500 1560, 510 1590"
        fill="none" stroke="#1F1F1F" stroke-width="1.3" stroke-opacity="0.82"
        stroke-linecap="round" stroke-linejoin="round"
        marker-end="url(#arrow-tip)" />

      <circle id="n3a" class="journey-node" cx="420" cy="1420" r="4"
        fill="white" stroke="#421835" stroke-width="2" opacity="0"/>
      <circle id="n3b" class="journey-node" cx="490" cy="1490" r="4"
        fill="white" stroke="#421835" stroke-width="2" opacity="0"/>
      <circle id="n3c" class="journey-node" cx="510" cy="1590" r="5"
        fill="#421835" stroke="none" filter="url(#glow-sm)" opacity="0"/>

      <!-- ─── SEGMENT 4: Crafting → Shavira ─── -->
      <path id="seg-4" class="journey-path"
        d="M 900 1600
           C 930 1590, 950 1610, 960 1640
           C 970 1670, 975 1700, 980 1730"
        fill="none" stroke="#1F1F1F" stroke-width="1.3" stroke-opacity="0.82"
        stroke-linecap="round" stroke-linejoin="round"
        marker-end="url(#arrow-tip)" />

      <circle id="n4a" class="journey-node" cx="900" cy="1600" r="4"
        fill="white" stroke="#421835" stroke-width="2" opacity="0"/>
      <circle id="n4b" class="journey-node" cx="980" cy="1730" r="6"
        fill="#421835" stroke="white" stroke-width="2" filter="url(#glow-lg)" opacity="0"/>

    </svg>'''

# Replace the entire SVG element
content = re.sub(
    r'<svg[^>]*id="timeline-svg"[^>]*>.*?</svg>',
    NEW_SVG.strip(),
    content,
    flags=re.DOTALL
)

# ══════════════════════════════════════════════════
# STEP 2: Replace the GSAP animation script block
# ══════════════════════════════════════════════════

# Find and remove old animation block(s), replace with our masterpiece
OLD_BLOCK_PATTERN = r'// ── SCROLL-DRAW ARROWS ──.*?}\);\s*};?\s*\}'

NEW_GSAP_BLOCK = '''// ══════════════════════════════════════════════════════
      // JOURNEY DRAW SYSTEM — Awwwards-level scroll animation
      // Each segment is hidden on load and revealed via scrub
      // The line "draws itself" as the user scrolls, guided by
      // a GSAP ScrollTrigger tied directly to scroll progress.
      // Reverse scroll = reverse draw (ink pulled back into pen).
      // ══════════════════════════════════════════════════════
      document.addEventListener('DOMContentLoaded', function () {
        if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') {
          console.warn('GSAP or ScrollTrigger not loaded.');
          return;
        }

        // ── Config: one entry per segment ──────────────────────
        // trigger: element that enters viewport to start drawing
        // startPct: % from top of viewport when drawing starts
        // endPct:   % from top of viewport when drawing finishes
        // nodes:    IDs of dots to pop in (first=source, rest=waypoints, last=dest)
        // card:     card element to lift when this segment completes
        const segments = [
          {
            id:    'seg-0',
            trigger: '#node-hero',
            start:   'top 55%',
            end:     'bottom 15%',
            nodes:   ['n0a', 'n0b', 'n0c'],
            card:    '#trigger-girl',
          },
          {
            id:    'seg-1',
            trigger: '#trigger-girl',
            start:   'top 55%',
            end:     'bottom 15%',
            nodes:   ['n1a', 'n1b', 'n1c'],
            card:    '#trigger-orbital',
          },
          {
            id:    'seg-2',
            trigger: '#trigger-orbital',
            start:   'top 55%',
            end:     'bottom 15%',
            nodes:   ['n2a', 'n2b'],
            card:    '#node-linkedin',
          },
          {
            id:    'seg-3',
            trigger: '#node-linkedin',
            start:   'top 55%',
            end:     'bottom 15%',
            nodes:   ['n3a', 'n3b', 'n3c'],
            card:    '#trigger-crafting',
          },
          {
            id:    'seg-4',
            trigger: '#trigger-crafting',
            start:   'top 60%',
            end:     'bottom 20%',
            nodes:   ['n4a', 'n4b'],
            card:    '#trigger-shavira',
          },
        ];

        segments.forEach(({ id, trigger, start, end, nodes, card }) => {
          const path = document.getElementById(id);
          if (!path) return;

          // Measure actual path length and hide it completely
          const totalLen = path.getTotalLength();
          path.style.strokeDasharray = totalLen + 'px';
          path.style.strokeDashoffset = totalLen + 'px';

          // Set all nodes invisible initially
          nodes.forEach(nId => {
            const el = document.getElementById(nId);
            if (el) gsap.set(el, { opacity: 0, scale: 0, transformOrigin: '50% 50%' });
          });

          // ── Build the scrub timeline ─────────────────────────
          const tl = gsap.timeline({
            scrollTrigger: {
              trigger:  trigger,
              start:    start,
              end:      end,
              scrub:    2,          // 2 = silky smooth, matches scroll closely
              // markers: true,     // uncomment to debug
            }
          });

          // 1. Source node pops in (spring scale-up)
          const srcNode = document.getElementById(nodes[0]);
          if (srcNode) {
            tl.to(srcNode, {
              opacity: 1, scale: 1.4, duration: 0.08, ease: 'back.out(3)'
            }).to(srcNode, {
              scale: 1, duration: 0.05, ease: 'power2.out'
            });
          }

          // 2. Line draws itself (the core effect)
          tl.to(path, {
            strokeDashoffset: 0,
            duration: 0.80,
            ease: 'power2.inOut',
          }, srcNode ? '+=0' : '0');

          // 3. Waypoint nodes pop in at ~40% and ~75% through the line draw
          if (nodes.length > 2) {
            const midNode = document.getElementById(nodes[1]);
            if (midNode) {
              // Append at 40% of line draw progress
              tl.to(midNode, {
                opacity: 1, scale: 1.3, duration: 0.06, ease: 'back.out(3)'
              }, '-=0.55').to(midNode, {
                scale: 1, duration: 0.04, ease: 'power2.out'
              });
            }
          }

          // 4. Destination node pops in with glow pulse
          const destNode = document.getElementById(nodes[nodes.length - 1]);
          if (destNode) {
            tl.to(destNode, {
              opacity: 1, scale: 1.5, duration: 0.07, ease: 'back.out(3)'
            }).to(destNode, {
              scale: 1, duration: 0.06, ease: 'elastic.out(1, 0.5)'
            });
          }

          // 5. When segment completes → target card lifts in elegantly
          if (card) {
            const cardEl = document.querySelector(card);
            if (cardEl) {
              // Set initial hidden state
              gsap.set(cardEl, { y: 18, opacity: 0 });

              ScrollTrigger.create({
                trigger: trigger,
                start:   start,
                end:     end,
                scrub:   2,
                onUpdate(self) {
                  // Sync card reveal to last 30% of draw progress
                  const progress = Math.max(0, (self.progress - 0.7) / 0.3);
                  gsap.set(cardEl, {
                    y:       18 * (1 - progress),
                    opacity: progress,
                  });
                }
              });
            }
          }
        });

        // ── Subtle ambient drift on nodes (breathing feel) ──────
        document.querySelectorAll('.journey-node').forEach((node, i) => {
          gsap.to(node, {
            x: 'random(-1.5, 1.5)',
            y: 'random(-1.5, 1.5)',
            duration: 'random(8, 16)',
            ease:  'sine.inOut',
            repeat: -1,
            yoyo:   true,
            delay:   i * 0.3,
          });
        });

        // ── Node hover: ripple on mouse-over ────────────────────
        document.querySelectorAll('.journey-node').forEach(node => {
          node.style.pointerEvents = 'auto';
          node.style.cursor = 'pointer';
          node.addEventListener('mouseenter', () => {
            gsap.to(node, { scale: 1.6, duration: 0.25, ease: 'back.out(3)', overwrite: true });
          });
          node.addEventListener('mouseleave', () => {
            gsap.to(node, { scale: 1,   duration: 0.35, ease: 'elastic.out(1,0.5)', overwrite: true });
          });
        });

      }); // end DOMContentLoaded'''

# Replace old GSAP block
content = re.sub(OLD_BLOCK_PATTERN, NEW_GSAP_BLOCK.strip(), content, flags=re.DOTALL)

# Also remove the old "Premium Editorial Connection System" block which targets .anim-path
OLD_ANIM_BLOCK = r'document\.addEventListener\("DOMContentLoaded",.*?}\);\s*// NEW SVG DRAW ANIMATION: Sequential Flow with Dots'
content = re.sub(OLD_ANIM_BLOCK, '// SCROLL-DRAW ARROWS: See DOMContentLoaded block below\n      ', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done. SVG redrawn and GSAP rewritten.")
