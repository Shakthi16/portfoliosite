import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ══════════════════════════════════════════════════
# STEP 1: Add GitHub card after LinkedIn card,
#         and add seg-5/n5a/n5b to SVG
# ══════════════════════════════════════════════════

# Insert GitHub card before the Crafting heading (#7)
GITHUB_CARD = '''<!-- 6b. GITHUB CARD (Mid Right) -->
<div class="absolute top-[1250px] right-[80px] w-[340px] z-30 hover-card" id="node-github">
  <a class="bg-white/80 backdrop-blur-xl rounded-[32px] p-8 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.04)] flex flex-col justify-between h-[320px] w-full text-black transform transition-all duration-500 hover:-translate-y-3 cursor-pointer border border-white/60 hover:shadow-[0_40px_80px_-15px_rgba(66,24,53,0.1)] block" href="https://github.com/Shakthi16" target="_blank">
    <div class="flex justify-between items-start w-full">
      <div class="w-14 h-14 rounded-full bg-[#1a1a1a] flex items-center justify-center shadow-[0_8px_15px_-5px_rgba(0,0,0,0.3)]">
        <svg class="w-7 h-7 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0 1 12 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/></svg>
      </div>
      <div class="flex items-center gap-1 border border-gray-200/50 rounded-md px-3 py-1 bg-gray-50/50">
        <span class="text-[10px] font-bold text-gray-500 uppercase tracking-widest">OPEN SOURCE</span>
      </div>
    </div>
    <div class="mt-4 mb-auto">
      <h3 class="font-bold text-2xl text-[#1F1F1F] mb-1">GitHub</h3>
      <p class="text-[12px] text-gray-400 font-medium tracking-wide">Code & Repositories</p>
      <div class="flex flex-wrap gap-2 mt-5">
        <span class="text-[10px] bg-gray-100/80 text-gray-600 px-4 py-1.5 rounded-full font-bold tracking-wide">Web Dev</span>
        <span class="text-[10px] bg-gray-100/80 text-gray-600 px-4 py-1.5 rounded-full font-bold tracking-wide">Security</span>
        <span class="text-[10px] bg-gray-100/80 text-gray-600 px-4 py-1.5 rounded-full font-bold tracking-wide">AI</span>
      </div>
    </div>
    <div class="pt-5 border-t border-gray-100/80 flex justify-between items-center mt-4">
      <span class="font-bold text-sm text-[#1F1F1F]">@Shakthi16</span>
      <span class="bg-[#1F1F1F] text-white text-[11px] font-bold tracking-wide px-5 py-2.5 rounded-xl hover:bg-[#421835] transition-colors inline-block">View Repos</span>
    </div>
  </a>
</div>

'''

content = content.replace(
    '<!-- 7. THIRD HEADING (Bottom Center) -->',
    GITHUB_CARD + '<!-- 7. THIRD HEADING (Bottom Center) -->'
)

# Add seg-5 and n5a/n5b to SVG (for LinkedIn → GitHub path)
# Add it just before the closing </svg>
SEG5_SVG = '''
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

content = content.replace(
    '\n    </svg>\n<!-- UI ELEMENTS -->',
    SEG5_SVG + '\n    </svg>\n<!-- UI ELEMENTS -->'
)

# ══════════════════════════════════════════════════
# STEP 2: Replace the entire GSAP journey script
#         with a version that dynamically computes
#         path coordinates from actual DOM positions
# ══════════════════════════════════════════════════

OLD_GSAP = content[content.find('// ══════════════════════════════════════════════════════'):
                   content.find('}); // end DOMContentLoaded') + len('}); // end DOMContentLoaded')]

NEW_GSAP = '''// ══════════════════════════════════════════════════════
      // JOURNEY DRAW SYSTEM — Dynamic coordinate calculation
      // Paths are built from actual DOM element positions at
      // runtime, so arrows always perfectly align to cards.
      // ══════════════════════════════════════════════════════
      document.addEventListener('DOMContentLoaded', function () {
        if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

        // ─── Dynamic path builder ─────────────────────────────
        // Reads actual card positions and builds perfect Bézier
        // curves matching those positions in SVG viewBox coords.
        function buildJourneyPaths() {
          const container = document.getElementById('timeline-container');
          const svg       = document.getElementById('timeline-svg');
          if (!container || !svg) return;

          const cRect  = container.getBoundingClientRect();
          const cTop   = cRect.top + window.scrollY; // container top from page top
          const svgVBW = 1400;                        // viewBox width
          // SVG is 2200px tall = 2200 vb units → 1:1 vertical scale
          // Horizontal: vb = dom_x * (1400 / containerClientWidth)
          const scaleX = svgVBW / container.clientWidth;

          // Convert a DOM element's anchor point to SVG viewBox coords
          function vb(selector, ax, ay) {
            const el = document.querySelector(selector);
            if (!el) return null;
            const r   = el.getBoundingClientRect();
            const x   = (r.left - cRect.left + r.width  * ax) * scaleX;
            const y   =  r.top  + window.scrollY - cTop + r.height * ay;
            return { x: parseFloat(x.toFixed(1)), y: parseFloat(y.toFixed(1)) };
          }

          // Update an SVG path d attribute (and reset dasharray to force GSAP re-init)
          function setPath(id, d) {
            const el = document.getElementById(id);
            if (!el) return;
            el.setAttribute('d', d);
            // Reset dash to hidden — GSAP will re-measure and re-hide on init
            el.style.strokeDasharray  = '';
            el.style.strokeDashoffset = '';
          }

          // Move a circle node
          function mv(id, x, y) {
            const el = document.getElementById(id);
            if (el) { el.setAttribute('cx', x); el.setAttribute('cy', y); }
          }

          // ─── Anchor points ─────────────────────────────────
          //   (selector, fraction_of_width, fraction_of_height)
          const H_bot  = vb('#node-hero',        0.35, 1.02); // hero card bottom, 35% from left
          const G_top  = vb('#trigger-girl',     0.12, 0.0);  // girl card top-left corner
          const G_bot  = vb('#trigger-girl',     0.12, 1.0);  // girl card bottom-left
          const O_r    = vb('#trigger-orbital',  1.05, 0.5);  // orbital right edge
          const O_bot  = vb('#trigger-orbital',  0.35, 1.02); // orbital bottom
          const LI_top = vb('#node-linkedin',    0.5,  0.0);  // linkedin top-center
          const LI_r   = vb('#node-linkedin',    1.02, 0.5);  // linkedin right-center
          const GH_top = vb('#node-github',      0.5,  0.0);  // github top-center
          const GH_bot = vb('#node-github',      0.5,  1.02); // github bottom-center
          const CR_l   = vb('#trigger-crafting', 0.05, 0.4);  // crafting text left
          const CR_r   = vb('#trigger-crafting', 0.95, 0.4);  // crafting text right
          const SH_tl  = vb('#trigger-shavira',  0.12, 0.0);  // shavira top-left

          if (!H_bot || !G_top || !G_bot || !O_r || !O_bot ||
              !LI_top || !LI_r || !GH_top || !CR_l || !CR_r || !SH_tl) {
            console.warn('Journey arrows: some anchor elements not found.');
            return;
          }

          // ─── SEG 0: Hero → Girl ─────────────────────────────
          // Drop from hero bottom, large elegant clockwise sweep
          {
            const drop = { x: H_bot.x, y: H_bot.y + 35 };
            // Horizontal span
            const span = G_top.x - drop.x;
            // Control points: first goes down then swings right
            const cp1  = { x: drop.x - span * 0.05, y: drop.y + Math.abs(G_top.y - drop.y) * 0.55 };
            const cp2  = { x: G_top.x - span * 0.20, y: G_top.y - 30 };
            const mid  = {
              x: (cp1.x + cp2.x) / 2,
              y: (cp1.y + cp2.y) / 2,
            };
            setPath('seg-0',
              `M ${H_bot.x} ${H_bot.y} L ${drop.x} ${drop.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${G_top.x} ${G_top.y}`
            );
            mv('n0a', H_bot.x, H_bot.y);
            mv('n0b', mid.x,   mid.y);
            mv('n0c', G_top.x, G_top.y);
          }

          // ─── SEG 1: Girl → Orbital ────────────────────────
          // From girl's bottom-left, S-curve under "I build" heading, arrive at orbital right
          {
            const span = O_r.x - G_bot.x;   // negative (left-moving)
            const dy   = O_r.y - G_bot.y;
            const cp1  = { x: G_bot.x + span * 0.25, y: G_bot.y + 55 };
            const cp2  = { x: O_r.x + 70,            y: O_r.y - 50   };
            const mid  = { x: (cp1.x + cp2.x) / 2,   y: (cp1.y + cp2.y) / 2 };
            setPath('seg-1',
              `M ${G_bot.x} ${G_bot.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${O_r.x} ${O_r.y}`
            );
            mv('n1a', G_bot.x, G_bot.y);
            mv('n1b', mid.x,   mid.y);
            mv('n1c', O_r.x,   O_r.y);
          }

          // ─── SEG 2: Orbital → LinkedIn ────────────────────
          // Short graceful arc dropping left and down
          {
            const dy  = LI_top.y - O_bot.y;
            const cp1 = { x: O_bot.x - 25, y: O_bot.y + dy * 0.45 };
            const cp2 = { x: LI_top.x + 30, y: LI_top.y - 25 };
            setPath('seg-2',
              `M ${O_bot.x} ${O_bot.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${LI_top.x} ${LI_top.y}`
            );
            mv('n2a', O_bot.x,  O_bot.y);
            mv('n2b', LI_top.x, LI_top.y);
          }

          // ─── SEG 3: LinkedIn → GitHub ─────────────────────
          // Diagonal right-crossing arc from linkedin right to github top
          {
            const midX = (LI_r.x + GH_top.x) / 2;
            const midY = Math.min(LI_r.y, GH_top.y) - 50; // arc over the gap
            const cp1  = { x: midX - 60, y: LI_r.y   - 20 };
            const cp2  = { x: midX + 60, y: GH_top.y - 20 };
            const mid  = { x: midX, y: midY };
            setPath('seg-3',
              `M ${LI_r.x} ${LI_r.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${GH_top.x} ${GH_top.y}`
            );
            mv('n3a', LI_r.x,   LI_r.y);
            mv('n3b', mid.x,    mid.y);
            mv('n3c', GH_top.x, GH_top.y);
          }

          // ─── SEG 4: GitHub → Crafting Text ────────────────
          // Drop from github bottom toward crafting text left
          {
            const dy  = CR_l.y - GH_bot.y;
            const cp1 = { x: GH_bot.x - 40, y: GH_bot.y + dy * 0.40 };
            const cp2 = { x: CR_l.x  + 30,  y: CR_l.y   - 25 };
            setPath('seg-4',
              `M ${GH_bot.x} ${GH_bot.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${CR_l.x} ${CR_l.y}`
            );
            mv('n4a', GH_bot.x, GH_bot.y);
            mv('n4b', CR_l.x,   CR_l.y);
          }

          // ─── SEG 5: Crafting Text → Shavira ───────────────
          // Short arc from crafting text right to shavira top-left
          {
            const dy  = SH_tl.y - CR_r.y;
            const cp1 = { x: CR_r.x  + 35, y: CR_r.y  + dy * 0.30 };
            const cp2 = { x: SH_tl.x + 15, y: SH_tl.y - 25 };
            setPath('seg-5',
              `M ${CR_r.x} ${CR_r.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${SH_tl.x} ${SH_tl.y}`
            );
            mv('n5a', CR_r.x,  CR_r.y);
            mv('n5b', SH_tl.x, SH_tl.y);
          }
        }

        // ─── Build paths now & on resize ─────────────────────
        buildJourneyPaths();
        window.addEventListener('resize', () => {
          buildJourneyPaths();
          if (typeof ScrollTrigger !== 'undefined') ScrollTrigger.refresh();
        });

        // ─── Scroll-draw config ──────────────────────────────
        const segments = [
          { id: 'seg-0', trigger: '#node-hero',        start: 'top 60%', end: 'bottom 10%', nodes: ['n0a','n0b','n0c'], card: '#trigger-girl'    },
          { id: 'seg-1', trigger: '#trigger-girl',     start: 'top 60%', end: 'bottom 10%', nodes: ['n1a','n1b','n1c'], card: '#trigger-orbital' },
          { id: 'seg-2', trigger: '#trigger-orbital',  start: 'top 60%', end: 'bottom 10%', nodes: ['n2a','n2b'],       card: '#node-linkedin'   },
          { id: 'seg-3', trigger: '#node-linkedin',    start: 'top 60%', end: 'bottom 10%', nodes: ['n3a','n3b','n3c'], card: '#node-github'     },
          { id: 'seg-4', trigger: '#node-github',      start: 'top 60%', end: 'bottom 10%', nodes: ['n4a','n4b'],       card: '#trigger-crafting'},
          { id: 'seg-5', trigger: '#trigger-crafting', start: 'top 65%', end: 'bottom 15%', nodes: ['n5a','n5b'],       card: '#trigger-shavira' },
        ];

        // Small delay so paths are built before GSAP measures them
        setTimeout(() => {
          segments.forEach(({ id, trigger, start, end, nodes, card }) => {
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
          });

          // Ambient node drift
          document.querySelectorAll('.journey-node').forEach((node, i) => {
            gsap.to(node, {
              x: 'random(-1.2, 1.2)', y: 'random(-1.2, 1.2)',
              duration: 'random(8, 18)', ease: 'sine.inOut',
              repeat: -1, yoyo: true, delay: i * 0.4,
            });
          });

          // Node hover
          document.querySelectorAll('.journey-node').forEach(node => {
            node.style.pointerEvents = 'auto';
            node.style.cursor = 'pointer';
            node.addEventListener('mouseenter', () => gsap.to(node, { scale: 1.8, duration: 0.2, ease: 'back.out(3)', overwrite: true }));
            node.addEventListener('mouseleave', () => gsap.to(node, { scale: 1,   duration: 0.4, ease: 'elastic.out(1,0.4)', overwrite: true }));
          });

        }, 150); // wait 150ms for images to load and layout to settle

      }); // end DOMContentLoaded'''

content = content.replace(OLD_GSAP, NEW_GSAP)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done. GitHub card added, dynamic coordinate system installed.")
