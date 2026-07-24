import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ─────────────────────────────────────────────
# 1. FIX viewbox → viewBox on the SVG element
# ─────────────────────────────────────────────
content = content.replace(
    'id="timeline-svg" viewbox="0 0 1400 2200"',
    'id="timeline-svg" viewBox="0 0 1400 2200"'
)

# ─────────────────────────────────────────────
# 2. REPLACE the entire SVG inner content with
#    correct paths that match actual card positions.
#
#  Card layout (top px, rough center coords in 1400-wide viewBox):
#   Hero card      : top=100,  left=100,  w=450  → center ≈ (325, 380) bottom ≈ (325, 550)
#   Girl card      : top=650,  right=100, w=380  → left edge ≈ (920, 760), bottom ≈ (1110, 1000)
#   Orbital        : top=800,  left=200,  w=300  → center ≈ (350, 950), right ≈ (500, 950)
#   LinkedIn card  : top=1250, left=80,   w=340  → center ≈ (250, 1410)
#   Crafting text  : top=1500, center,    w=400  → center ≈ (700, 1570)
#   Shavira card   : top=1600, right=80,  w=340  → left ≈ (980, 1760)
# ─────────────────────────────────────────────

new_svg_content = '''<defs>
        <marker id="arrow-head" viewBox="0 0 10 10" refX="8" refY="5"
                markerWidth="5" markerHeight="5" orient="auto">
          <path d="M 1 2 L 8 5 L 1 8" fill="none" stroke="#421835"
                stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </marker>
        <filter id="node-glow" x="-80%" y="-80%" width="260%" height="260%">
          <feGaussianBlur stdDeviation="4" result="blur"/>
          <feComposite in="SourceGraphic" in2="blur" operator="over"/>
        </filter>
      </defs>

      <!-- All paths hidden initially via stroke-dasharray set by JS -->
      <g fill="none" stroke="#421835" stroke-width="1.4" stroke-opacity="0.9">

        <!-- PATH 0: Hero card bottom → Girl card top-left -->
        <!-- Hero bottom ~(325,550) → arc across → Girl top ~(920,660) -->
        <path id="path-0" class="draw-path"
          d="M 325 550 C 325 700, 600 620, 920 660"
          marker-end="url(#arrow-head)" />
        <circle id="dot-0-start" class="anim-dot" cx="325" cy="550" r="5"
          fill="white" stroke="#421835" stroke-width="2" opacity="0"/>
        <circle id="dot-0-end"   class="anim-dot" cx="920" cy="660" r="5"
          fill="#421835" filter="url(#node-glow)" opacity="0"/>

        <!-- PATH 1: Girl card left → Orbital right edge -->
        <!-- Girl left ~(920,960) → S-curve → Orbital right ~(500,950) -->
        <path id="path-1" class="draw-path"
          d="M 920 960 C 820 1060, 680 1020, 500 950"
          marker-end="url(#arrow-head)" />
        <circle id="dot-1-start" class="anim-dot" cx="920" cy="960" r="5"
          fill="white" stroke="#421835" stroke-width="2" opacity="0"/>
        <circle id="dot-1-end"   class="anim-dot" cx="500" cy="950" r="5"
          fill="#421835" filter="url(#node-glow)" opacity="0"/>

        <!-- PATH 2: Orbital bottom → LinkedIn top -->
        <!-- Orbital bottom ~(350,1100) → down → LinkedIn top ~(250,1250) -->
        <path id="path-2" class="draw-path"
          d="M 350 1100 C 380 1170, 300 1190, 250 1250"
          marker-end="url(#arrow-head)" />
        <circle id="dot-2-start" class="anim-dot" cx="350" cy="1100" r="5"
          fill="white" stroke="#421835" stroke-width="2" opacity="0"/>
        <circle id="dot-2-end"   class="anim-dot" cx="250" cy="1250" r="5"
          fill="#421835" filter="url(#node-glow)" opacity="0"/>

        <!-- PATH 3: LinkedIn right → Crafting text center -->
        <!-- LinkedIn right ~(420,1410) → arc right → Crafting ~(540,1520) -->
        <path id="path-3" class="draw-path"
          d="M 420 1410 C 460 1380, 500 1480, 540 1520"
          marker-end="url(#arrow-head)" />
        <circle id="dot-3-start" class="anim-dot" cx="420" cy="1410" r="5"
          fill="white" stroke="#421835" stroke-width="2" opacity="0"/>
        <circle id="dot-3-end"   class="anim-dot" cx="540" cy="1520" r="5"
          fill="#421835" filter="url(#node-glow)" opacity="0"/>

        <!-- PATH 4: Crafting text right → Shavira card left -->
        <!-- Crafting right ~(860,1570) → curve → Shavira left ~(980,1760) -->
        <path id="path-4" class="draw-path"
          d="M 860 1570 C 920 1570, 940 1680, 980 1760"
          marker-end="url(#arrow-head)" />
        <circle id="dot-4-start" class="anim-dot" cx="860" cy="1570" r="5"
          fill="white" stroke="#421835" stroke-width="2" opacity="0"/>
        <circle id="dot-4-end"   class="anim-dot" cx="980" cy="1760" r="5"
          fill="#421835" filter="url(#node-glow)" opacity="0"/>

      </g>'''

# Replace the SVG content between the svg tags
content = re.sub(
    r'(<svg[^>]*id="timeline-svg"[^>]*>).*?(</svg>)',
    r'\1' + new_svg_content + r'\2',
    content,
    flags=re.DOTALL
)

# ─────────────────────────────────────────────
# 3. REPLACE the GSAP animation block completely
#    with a bulletproof version that runs on
#    DOMContentLoaded and uses correct triggers.
# ─────────────────────────────────────────────

old_gsap_block = '''      // NEW SVG DRAW ANIMATION: Sequential Flow with Dots
      if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        const drawPaths = document.querySelectorAll('.draw-path');
        const triggers = ['#node-hero', '#trigger-girl', '#trigger-orbital', '#node-linkedin', '#trigger-crafting'];
        
        drawPaths.forEach((path, index) => {
            let length = path.getTotalLength();
            // Hard set initial states
            path.style.strokeDasharray = length;
            path.style.strokeDashoffset = length;
            
            let startDot = document.getElementById(`dot-${index}-start`);
            let endDot = document.getElementById(`dot-${index}-end`);
            
            if (triggers[index]) {
                let tl = gsap.timeline({
                    scrollTrigger: {
                        trigger: triggers[index],
                        start: 'top 50%',
                        end: 'bottom 20%', // The scroll distance over which it draws
                        scrub: 1,
                    }
                });
                
                // Fade in start dot, draw line, fade in end dot
                if(startDot) tl.to(startDot, { opacity: 1, duration: 0.1 });
                tl.to(path, { strokeDashoffset: 0, duration: 1, ease: 'none' });
                if(endDot) tl.to(endDot, { opacity: 1, duration: 0.1 });
            }
        });
      }'''

new_gsap_block = '''      // ── SCROLL-DRAW ARROWS ──────────────────────────────────────────
      // Runs after DOM ready so getTotalLength() works on SVG paths.
      // Each path draws in when its SOURCE card enters the viewport.
      // ────────────────────────────────────────────────────────────────
      document.addEventListener('DOMContentLoaded', function () {
        if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

        // Map each path index to the card it STARTS FROM
        const config = [
          { pathId: 'path-0', trigger: '#node-hero',        start: 'top 65%',   end: 'bottom 30%' },
          { pathId: 'path-1', trigger: '#trigger-girl',     start: 'top 65%',   end: 'bottom 30%' },
          { pathId: 'path-2', trigger: '#trigger-orbital',  start: 'top 65%',   end: 'bottom 30%' },
          { pathId: 'path-3', trigger: '#node-linkedin',    start: 'top 65%',   end: 'bottom 30%' },
          { pathId: 'path-4', trigger: '#trigger-crafting', start: 'top 70%',   end: 'bottom 30%' },
        ];

        config.forEach(({ pathId, trigger, start, end }) => {
          const path = document.getElementById(pathId);
          if (!path) return;

          const idx   = pathId.split('-')[1];
          const sDot  = document.getElementById('dot-' + idx + '-start');
          const eDot  = document.getElementById('dot-' + idx + '-end');

          // Measure the path length and hide it fully
          const len = path.getTotalLength();
          gsap.set(path, { strokeDasharray: len, strokeDashoffset: len, opacity: 1 });
          if (sDot) gsap.set(sDot, { opacity: 0, scale: 0, transformOrigin: 'center' });
          if (eDot) gsap.set(eDot, { opacity: 0, scale: 0, transformOrigin: 'center' });

          // Build a scrub timeline tied to scrolling past the source card
          const tl = gsap.timeline({
            scrollTrigger: {
              trigger: trigger,
              start:   start,
              end:     end,
              scrub:   1.5,
            }
          });

          // Pop in source dot → draw line → pop in destination dot
          if (sDot) tl.to(sDot, { opacity: 1, scale: 1, duration: 0.15, ease: 'back.out(2)' });
          tl.to(path, { strokeDashoffset: 0, duration: 1, ease: 'power2.inOut' }, sDot ? '+=0' : '0');
          if (eDot) tl.to(eDot, { opacity: 1, scale: 1, duration: 0.15, ease: 'back.out(2)' });
        });
      });'''

content = content.replace(old_gsap_block, new_gsap_block)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Fixed viewBox, redrawn paths, rewrote GSAP.")
