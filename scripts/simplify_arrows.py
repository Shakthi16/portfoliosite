import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ─────────────────────────────────────────────────────────
# STEP 1: Remove all middle waypoint nodes from SVG.
# Keep only the END nodes (one dot per segment arrival).
# No start dots — just one dot appears where the line lands.
# ─────────────────────────────────────────────────────────

# Replace old SVG node block (everything between defs close and </svg>)
# with a clean set of only 6 destination dots — one per segment end.
OLD_NODES_BLOCK = '''      <!-- ─── SEGMENT 0: Hero → Girl ─── -->
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

      <!-- ─── SEGMENT 5: LinkedIn → GitHub ─── -->
      <path id="seg-5" class="journey-path"
        d="M 420 1420 C 600 1350, 800 1280, 980 1410"
        fill="none" stroke="#1F1F1F" stroke-width="1.3" stroke-opacity="0.82"
        stroke-linecap="round" stroke-linejoin="round"
        marker-end="url(#arrow-tip)" />
      <circle id="n5a" class="journey-node" cx="420" cy="1420" r="4"
        fill="white" stroke="#421835" stroke-width="2" opacity="0"/>
      <circle id="n5b" class="journey-node" cx="980" cy="1410" r="5"
        fill="#421835" stroke="none" filter="url(#glow-sm)" opacity="0"/>

    '''

NEW_NODES_BLOCK = '''      <!-- One clean path per card connection. No intermediate dots. -->
      <!-- Paths use placeholder d="" — JS will compute real coords. -->

      <!-- SEG 0: Hero card → Girl illustration -->
      <path id="seg-0" class="journey-path" d=""
        fill="none" stroke="#1F1F1F" stroke-width="1.3" stroke-opacity="0.82"
        stroke-linecap="round" stroke-linejoin="round"
        marker-end="url(#arrow-tip)" />
      <circle id="n0-end" class="journey-node" cx="0" cy="0" r="5"
        fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="0"/>

      <!-- SEG 1: Girl illustration → Orbital -->
      <path id="seg-1" class="journey-path" d=""
        fill="none" stroke="#1F1F1F" stroke-width="1.3" stroke-opacity="0.82"
        stroke-linecap="round" stroke-linejoin="round"
        marker-end="url(#arrow-tip)" />
      <circle id="n1-end" class="journey-node" cx="0" cy="0" r="5"
        fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="0"/>

      <!-- SEG 2: Orbital → LinkedIn card -->
      <path id="seg-2" class="journey-path" d=""
        fill="none" stroke="#1F1F1F" stroke-width="1.3" stroke-opacity="0.82"
        stroke-linecap="round" stroke-linejoin="round"
        marker-end="url(#arrow-tip)" />
      <circle id="n2-end" class="journey-node" cx="0" cy="0" r="5"
        fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="0"/>

      <!-- SEG 3: LinkedIn card → GitHub card -->
      <path id="seg-3" class="journey-path" d=""
        fill="none" stroke="#1F1F1F" stroke-width="1.3" stroke-opacity="0.82"
        stroke-linecap="round" stroke-linejoin="round"
        marker-end="url(#arrow-tip)" />
      <circle id="n3-end" class="journey-node" cx="0" cy="0" r="5"
        fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="0"/>

      <!-- SEG 4: GitHub card → Crafting text -->
      <path id="seg-4" class="journey-path" d=""
        fill="none" stroke="#1F1F1F" stroke-width="1.3" stroke-opacity="0.82"
        stroke-linecap="round" stroke-linejoin="round"
        marker-end="url(#arrow-tip)" />
      <circle id="n4-end" class="journey-node" cx="0" cy="0" r="5"
        fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="0"/>

      <!-- SEG 5: Crafting text → Shavira card -->
      <path id="seg-5" class="journey-path" d=""
        fill="none" stroke="#1F1F1F" stroke-width="1.3" stroke-opacity="0.82"
        stroke-linecap="round" stroke-linejoin="round"
        marker-end="url(#arrow-tip)" />
      <circle id="n5-end" class="journey-node" cx="0" cy="0" r="6"
        fill="#421835" stroke="white" stroke-width="2" filter="url(#glow-lg)" opacity="0"/>

    '''

content = content.replace(OLD_NODES_BLOCK, NEW_NODES_BLOCK)

# ─────────────────────────────────────────────────────────
# STEP 2: Replace GSAP segments config and path builder
#         so there's just ONE dot per segment (destination),
#         and ONE clean Bézier per pair of cards.
# ─────────────────────────────────────────────────────────

OLD_SEGMENTS = """        const segments = [
          { id: 'seg-0', trigger: '#node-hero',        start: 'top 60%', end: 'bottom 10%', nodes: ['n0a','n0b','n0c'], card: '#trigger-girl'    },
          { id: 'seg-1', trigger: '#trigger-girl',     start: 'top 60%', end: 'bottom 10%', nodes: ['n1a','n1b','n1c'], card: '#trigger-orbital' },
          { id: 'seg-2', trigger: '#trigger-orbital',  start: 'top 60%', end: 'bottom 10%', nodes: ['n2a','n2b'],       card: '#node-linkedin'   },
          { id: 'seg-3', trigger: '#node-linkedin',    start: 'top 60%', end: 'bottom 10%', nodes: ['n3a','n3b','n3c'], card: '#node-github'     },
          { id: 'seg-4', trigger: '#node-github',      start: 'top 60%', end: 'bottom 10%', nodes: ['n4a','n4b'],       card: '#trigger-crafting'},
          { id: 'seg-5', trigger: '#trigger-crafting', start: 'top 65%', end: 'bottom 15%', nodes: ['n5a','n5b'],       card: '#trigger-shavira' },
        ];"""

NEW_SEGMENTS = """        // ONE destination dot per segment. Clean and minimal.
        const segments = [
          { id: 'seg-0', trigger: '#node-hero',        start: 'top 60%', end: 'bottom 10%', endNode: 'n0-end' },
          { id: 'seg-1', trigger: '#trigger-girl',     start: 'top 60%', end: 'bottom 10%', endNode: 'n1-end' },
          { id: 'seg-2', trigger: '#trigger-orbital',  start: 'top 60%', end: 'bottom 10%', endNode: 'n2-end' },
          { id: 'seg-3', trigger: '#node-linkedin',    start: 'top 60%', end: 'bottom 10%', endNode: 'n3-end' },
          { id: 'seg-4', trigger: '#node-github',      start: 'top 60%', end: 'bottom 10%', endNode: 'n4-end' },
          { id: 'seg-5', trigger: '#trigger-crafting', start: 'top 65%', end: 'bottom 15%', endNode: 'n5-end' },
        ];"""

content = content.replace(OLD_SEGMENTS, NEW_SEGMENTS)

# Replace the forEach that animates segments
OLD_FOREACH = """          segments.forEach(({ id, trigger, start, end, nodes, card }) => {
            const path = document.getElementById(id);
            if (!path) return;

            // Measure & fully hide path
            const len = path.getTotalLength();
            if (!len) return; // path not built yet
            path.style.strokeDasharray  = len + 'px';
            path.style.strokeDashoffset = len + 'px';

            // Hide all nodes initially
            nodes.forEach(nId => {
              const el = document.getElementById(nId);
              if (el) gsap.set(el, { opacity: 0, scale: 0, transformOrigin: '50% 50%' });
            });

            // Build scrub timeline
            const tl = gsap.timeline({
              scrollTrigger: { trigger, start, end, scrub: 2 }
            });

            const srcEl  = document.getElementById(nodes[0]);
            if (srcEl) {
              tl.to(srcEl, { opacity: 1, scale: 1.4, duration: 0.07, ease: 'back.out(4)' })
                .to(srcEl, { scale: 1, duration: 0.05, ease: 'power2.out' });
            }

            tl.to(path, { strokeDashoffset: 0, duration: 0.80, ease: 'power2.inOut' });

            if (nodes.length > 2) {
              const midEl = document.getElementById(nodes[1]);
              if (midEl) {
                tl.to(midEl, { opacity: 1, scale: 1.3, duration: 0.06, ease: 'back.out(3)' }, '-=0.5')
                  .to(midEl, { scale: 1, duration: 0.04, ease: 'power2.out' });
              }
            }

            const destEl = document.getElementById(nodes[nodes.length - 1]);
            if (destEl) {
              tl.to(destEl, { opacity: 1, scale: 1.6, duration: 0.07, ease: 'back.out(4)' })
                .to(destEl, { scale: 1, duration: 0.08, ease: 'elastic.out(1, 0.5)' });
            }
          });"""

NEW_FOREACH = """          // Animate each segment: line draws → destination dot pops in.
          // That's it. One line, one dot. Clean.
          segments.forEach(({ id, trigger, start, end, endNode }) => {
            const path = document.getElementById(id);
            if (!path) return;

            const len = path.getTotalLength();
            if (!len) return;

            // Fully hide the line
            path.style.strokeDasharray  = len + 'px';
            path.style.strokeDashoffset = len + 'px';

            // Hide destination dot
            const dot = document.getElementById(endNode);
            if (dot) gsap.set(dot, { opacity: 0, scale: 0, transformOrigin: '50% 50%' });

            // Scrub timeline: line draws → dot pops
            const tl = gsap.timeline({
              scrollTrigger: { trigger, start, end, scrub: 2 }
            });

            // Draw the line
            tl.to(path, { strokeDashoffset: 0, duration: 0.85, ease: 'power2.inOut' });

            // Destination dot pops in with spring
            if (dot) {
              tl.to(dot, { opacity: 1, scale: 1.5, duration: 0.08, ease: 'back.out(4)' })
                .to(dot, { scale: 1, duration: 0.10, ease: 'elastic.out(1, 0.5)' });
            }
          });"""

content = content.replace(OLD_FOREACH, NEW_FOREACH)

# Replace the node drift/hover section (only operates on journey-node class — still works)
# But also simplify path builder to use the new n0-end style IDs
OLD_MV = """          // Move a circle node
          function mv(id, x, y) {
            const el = document.getElementById(id);
            if (el) { el.setAttribute('cx', x); el.setAttribute('cy', y); }
          }"""
NEW_MV = """          // Move a destination dot
          function mv(id, x, y) {
            const el = document.getElementById(id);
            if (el) { el.setAttribute('cx', x); el.setAttribute('cy', y); }
          }"""
content = content.replace(OLD_MV, NEW_MV)

# Fix setPath calls and mv calls in path builder to use new node IDs
replacements = [
    # SEG 0
    ("mv('n0a', H_bot.x, H_bot.y);\n            mv('n0b', mid.x,   mid.y);\n            mv('n0c', G_top.x, G_top.y);",
     "mv('n0-end', G_top.x, G_top.y);"),
    # SEG 1
    ("mv('n1a', G_bot.x, G_bot.y);\n            mv('n1b', mid.x,   mid.y);\n            mv('n1c', O_r.x,   O_r.y);",
     "mv('n1-end', O_r.x, O_r.y);"),
    # SEG 2
    ("mv('n2a', O_bot.x,  O_bot.y);\n          mv('n2b', LI_top.x, LI_top.y);",
     "mv('n2-end', LI_top.x, LI_top.y);"),
    # SEG 3
    ("mv('n3a', LI_r.x,   LI_r.y);\n            mv('n3b', mid.x,    mid.y);\n            mv('n3c', GH_top.x, GH_top.y);",
     "mv('n3-end', GH_top.x, GH_top.y);"),
    # SEG 4
    ("mv('n4a', GH_bot.x, GH_bot.y);\n          mv('n4b', CR_l.x,   CR_l.y);",
     "mv('n4-end', CR_l.x, CR_l.y);"),
    # SEG 5
    ("mv('n5a', CR_r.x,  CR_r.y);\n          mv('n5b', SH_tl.x, SH_tl.y);",
     "mv('n5-end', SH_tl.x, SH_tl.y);"),
]

for old, new in replacements:
    content = content.replace(old, new)

# Remove the mid variable calculations (no longer needed)
content = re.sub(r'\n            const mid\s+=\s+\{[^}]+\};\n', '\n', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done. Simplified to one clean arrow per card connection.")
