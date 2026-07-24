import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Adjust LinkedIn and Shavira positions to avoid overlap
content = content.replace('left-[150px] w-[360px] z-30 hover-card" id="node-linkedin"', 'left-[80px] w-[340px] z-30 hover-card" id="node-linkedin"')
content = content.replace('right-[100px] w-[360px] z-30 hover-card"', 'right-[80px] w-[340px] z-30 hover-card" id="trigger-shavira"')

# 2. Redraw the SVG arrows and dots
# We'll completely replace the SVG contents
new_svg_content = """<defs>
        <filter id="node-glow" x="-50%" y="-50%" width="200%" height="200%">
          <feGaussianBlur stdDeviation="3" result="blur" />
          <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
      </defs>
      <g stroke="#421835" stroke-width="1.2" fill="none" stroke-opacity="0.85" class="floating-arrows">
        <!-- Arrow 1: Hero to Girl -->
        <!-- Hero center bottom: (325, 450). Girl top left: (920, 650) -->
        <path id="path-0" class="draw-path" d="M 325 450 C 325 650, 700 600, 920 650" />
        <circle id="dot-0-start" cx="325" cy="450" r="4" fill="white" stroke="#421835" stroke-width="2" class="anim-dot" opacity="0" />
        <circle id="dot-0-end" cx="920" cy="650" r="4" fill="white" stroke="#421835" stroke-width="2" filter="url(#node-glow)" class="anim-dot" opacity="0" />

        <!-- Arrow 2: Girl to Orbital -->
        <!-- Girl left edge: (920, 900). Orbital right edge: (550, 950) -->
        <path id="path-1" class="draw-path" d="M 920 900 C 800 1100, 650 1100, 500 950" />
        <circle id="dot-1-start" cx="920" cy="900" r="4" fill="white" stroke="#421835" stroke-width="2" class="anim-dot" opacity="0" />
        <circle id="dot-1-end" cx="500" cy="950" r="4" fill="white" stroke="#421835" stroke-width="2" filter="url(#node-glow)" class="anim-dot" opacity="0" />

        <!-- Arrow 3: Orbital to LinkedIn -->
        <!-- Orbital bottom: (350, 1100). LinkedIn top right: (400, 1250) -->
        <path id="path-2" class="draw-path" d="M 350 1100 C 350 1200, 420 1150, 420 1250" />
        <circle id="dot-2-start" cx="350" cy="1100" r="4" fill="white" stroke="#421835" stroke-width="2" class="anim-dot" opacity="0" />
        <circle id="dot-2-end" cx="420" cy="1250" r="4" fill="white" stroke="#421835" stroke-width="2" filter="url(#node-glow)" class="anim-dot" opacity="0" />

        <!-- Arrow 4: LinkedIn to Crafting Text -->
        <!-- LinkedIn right edge: (420, 1400). Text left edge: (500, 1550) -->
        <path id="path-3" class="draw-path" d="M 420 1400 C 460 1400, 460 1550, 500 1550" />
        <circle id="dot-3-start" cx="420" cy="1400" r="4" fill="white" stroke="#421835" stroke-width="2" class="anim-dot" opacity="0" />
        <circle id="dot-3-end" cx="500" cy="1550" r="4" fill="white" stroke="#421835" stroke-width="2" filter="url(#node-glow)" class="anim-dot" opacity="0" />

        <!-- Arrow 5: Crafting Text to Shavira -->
        <!-- Text right edge: (900, 1550). Shavira top left: (980, 1600) -->
        <path id="path-4" class="draw-path" d="M 900 1550 C 940 1550, 940 1600, 980 1600" />
        <circle id="dot-4-start" cx="900" cy="1550" r="4" fill="white" stroke="#421835" stroke-width="2" class="anim-dot" opacity="0" />
        <circle id="dot-4-end" cx="980" cy="1600" r="4" fill="white" stroke="#421835" stroke-width="2" filter="url(#node-glow)" class="anim-dot" opacity="0" />
      </g>"""

svg_pattern = r'<defs>.*?</g>'
content = re.sub(svg_pattern, new_svg_content.strip(), content, flags=re.DOTALL)

# 3. Fix the GSAP animation logic
new_gsap = """// NEW SVG DRAW ANIMATION: Sequential Flow with Dots
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
      }"""

gsap_pattern = r'// NEW SVG DRAW ANIMATION.*?\}\s*\}'
content = re.sub(gsap_pattern, new_gsap.strip(), content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Arrows and GSAP fixed.")
