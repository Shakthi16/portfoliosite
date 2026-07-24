import re

html_file = 'index.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new About section
new_about_section = """<!-- ABOUT: CINEMATIC EDITORIAL CANVAS -->
<section class="editorial-canvas font-sans relative z-20 overflow-hidden bg-[#FAFAFA] text-[#1F1F1F]" id="about" style="min-height: 2200px;">
  
  <!-- Subtle Grain & Grid Overlay -->
  <div class="absolute inset-0 pointer-events-none z-0 mix-blend-multiply opacity-[0.05]" style="background-image: url('data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noiseFilter%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%220.85%22 numOctaves=%223%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noiseFilter)%22/%3E%3C/svg%3E');"></div>
  <div class="absolute inset-0 pointer-events-none z-0 opacity-[0.03]" style="background-size: 100px 100px; background-image: linear-gradient(to right, #1F1F1F 1px, transparent 1px), linear-gradient(to bottom, #1F1F1F 1px, transparent 1px);"></div>

  <div class="relative w-full max-w-[1400px] mx-auto px-6 lg:px-12 z-10 hidden md:block" id="timeline-container" style="height: 2200px;">
    
    <style>
      .floating-arrows { animation: driftArrows 15s ease-in-out infinite alternate; }
      @keyframes driftArrows { 0% { transform: translate(0px, 0px); } 100% { transform: translate(0.5px, 0.5px); } }
      .interactive-node { transition: all 0.3s ease; }
      .interactive-node:hover { stroke-width: 4; cursor: pointer; fill: rgba(255,255,255,0.8); }
      .hover-card:hover ~ svg .interactive-node { transform: scale(1.1); transform-origin: center; }
    </style>

    <!-- THE ARROW SYSTEM SVG -->
    <svg id="timeline-svg" class="absolute inset-0 w-full h-full pointer-events-none z-[100] drawing-arrows" viewBox="0 0 1400 2200">
      <defs>
        <marker id="minimal-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse">
          <path d="M 2 2 L 8 5 L 2 8" fill="none" stroke="#1F1F1F" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
        </marker>
        <filter id="node-glow" x="-50%" y="-50%" width="200%" height="200%">
          <feGaussianBlur stdDeviation="3" result="blur" />
          <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <linearGradient id="fade-out" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#1F1F1F" stop-opacity="0.85" />
          <stop offset="100%" stop-color="#1F1F1F" stop-opacity="0" />
        </linearGradient>
      </defs>

      <!-- All paths have 1.2px, #1F1F1F, 85% opacity -->
      <g stroke="#1F1F1F" stroke-width="1.2" fill="none" stroke-opacity="0.85" class="floating-arrows">
        
        <!-- Arrow 1: Hero Card (Top Left) -> Center Overshoot -> Girl Illustration (Mid Right) -->
        <path class="draw-path" d="M 300 550 L 300 590 C 300 900, 1000 500, 1050 820" marker-end="url(#minimal-arrow)" />
        <circle cx="700" cy="710" r="4" fill="white" stroke="#B14665" stroke-width="2" filter="url(#node-glow)" class="interactive-node" style="pointer-events: auto;" />
        <circle cx="1050" cy="820" r="4" fill="white" stroke="#B14665" stroke-width="2" class="interactive-node" style="pointer-events: auto;" />

        <!-- Arrow 2: Girl (Mid Right) -> S-Curve under "I build..." -> Center loop -> Down -->
        <path class="draw-path" d="M 1030 980 C 800 1150, 400 1000, 500 1150 C 600 1300, 800 1150, 700 1300" marker-end="url(#minimal-arrow)" />
        <circle cx="530" cy="1110" r="4" fill="white" stroke="#B14665" stroke-width="2" class="interactive-node" style="pointer-events: auto;" />
        <circle cx="700" cy="1300" r="4" fill="white" stroke="#B14665" stroke-width="2" class="interactive-node" style="pointer-events: auto;" />

        <!-- Arrow 3: Under Heading -> U-Turn -> wrap LinkedIn (Bottom Left) -> Up -->
        <path class="draw-path" d="M 680 1350 C 680 1450, 150 1450, 150 1700 C 150 1800, 300 1850, 350 1750" marker-end="url(#minimal-arrow)" />
        <circle cx="160" cy="1550" r="4" fill="white" stroke="#B14665" stroke-width="2" filter="url(#node-glow)" class="interactive-node" style="pointer-events: auto;" />
        <circle cx="350" cy="1750" r="4" fill="white" stroke="#B14665" stroke-width="2" class="interactive-node" style="pointer-events: auto;" />

        <!-- Arrow 4: Near LinkedIn -> Diagonal -> Behind Center -> Shavira -->
        <path class="draw-path" d="M 380 1620 C 600 1500, 900 1500, 1100 1720" marker-end="url(#minimal-arrow)" />
        <circle cx="750" cy="1530" r="4" fill="white" stroke="#B14665" stroke-width="2" class="interactive-node" style="pointer-events: auto;" />
        <circle cx="1100" cy="1720" r="4" fill="white" stroke="#B14665" stroke-width="2" class="interactive-node" style="pointer-events: auto;" />

        <!-- Arrow 5: Leaves Shavira -> tiny loop -> Footer -> Fade -->
        <path class="draw-path fade-stroke" d="M 1120 1850 C 1200 1850, 1200 1950, 1120 1950 C 1000 1950, 1000 2150, 1000 2200" stroke="url(#fade-out)" />
        <circle cx="1165" cy="1900" r="4" fill="white" stroke="#B14665" stroke-width="2" filter="url(#node-glow)" class="interactive-node" style="pointer-events: auto;" />
      </g>
    </svg>

    <!-- UI ELEMENTS (The Cards & Text) -->
    
    <!-- 1. HERO CARD (Top Left) -->
    <div class="absolute top-[100px] left-[100px] w-[450px] z-20 hover-card" id="node-hero">
      <div class="w-full relative rounded-[32px] overflow-hidden bg-white/50 backdrop-blur-2xl p-3 border border-white/40 shadow-[0_30px_60px_-15px_rgba(0,0,0,0.05)] transition-all duration-500 hover:shadow-[0_40px_80px_-15px_rgba(177,70,101,0.1)] hover:-translate-y-2">
        <img alt="Editorial Side" class="w-full h-auto rounded-[24px]" src="bg1.png"/>
      </div>
    </div>
    
    <!-- 2. HEADLINE (Top Right) -->
    <div class="absolute top-[250px] right-[100px] w-[500px] text-right z-20">
      <h1 class="font-bold text-[64px] leading-[1.0] text-[#1F1F1F] tracking-tighter mb-6">
        I design intelligent<br/>systems.
      </h1>
      <p class="font-sans text-[18px] text-gray-500 leading-[1.6] font-medium">
        Class of 2026 Graduate learning scale.<br/>
        Software engineer &amp; cybersecurity researcher.<br/>
        Published researcher at <span class="text-[#B14665] font-bold">ICTACA'26.</span>
      </p>
    </div>

    <!-- 3. CENTRAL ORBITAL OBJECT (The Creative Engine) -->
    <div class="absolute top-[1000px] left-[50%] transform -translate-x-[50%] -translate-y-1/2 w-[400px] h-[400px] z-10 flex items-center justify-center">
      <!-- Outer rotating ring -->
      <div class="absolute inset-0 rounded-full border-[1px] border-gray-300/60 animate-[spin_60s_linear_infinite]"></div>
      <!-- Middle dashed orbit -->
      <div class="absolute inset-[30px] rounded-full border-[1.5px] border-dashed border-gray-300/80 animate-[spin_40s_linear_infinite_reverse]"></div>
      
      <!-- Center Text -->
      <div class="absolute z-20 text-center flex flex-col items-center">
        <div class="w-4 h-4 rounded-full bg-[#B14665] mb-3 shadow-[0_0_15px_rgba(177,70,101,0.4)]"></div>
        <div class="font-bold text-[#1F1F1F] tracking-widest text-[11px] uppercase leading-relaxed">
          Designing<br/>Systems<br/>That Think
        </div>
      </div>

      <!-- Orbital Labels -->
      <div class="absolute inset-0 animate-[spin_60s_linear_infinite]">
        <div class="absolute top-[-10px] left-[50%] transform -translate-x-[50%] text-[9px] font-bold text-gray-400 tracking-[0.2em]">INTENTION</div>
        <div class="absolute bottom-[-10px] left-[50%] transform -translate-x-[50%] rotate-180 text-[9px] font-bold text-gray-400 tracking-[0.2em]">SYSTEMS</div>
        <div class="absolute left-[-20px] top-[50%] transform -translate-y-[50%] -rotate-90 text-[9px] font-bold text-gray-400 tracking-[0.2em]">RESEARCH</div>
        <div class="absolute right-[-15px] top-[50%] transform -translate-y-[50%] rotate-90 text-[9px] font-bold text-gray-400 tracking-[0.2em]">BUILD</div>
        <div class="absolute right-[40px] top-[40px] transform rotate-[45deg] text-[9px] font-bold text-gray-400 tracking-[0.2em]">ITERATE</div>
      </div>
    </div>

    <!-- 4. SECOND HEADING (Mid Left) -->
    <div class="absolute top-[1100px] left-[150px] w-[350px] z-20">
      <h2 class="text-[48px] font-bold text-[#1F1F1F] mb-4 tracking-tight leading-[1.05]">I build premium<br/>interfaces.</h2>
      <p class="text-gray-500 font-medium text-[15px] leading-relaxed">
        Focusing on micro-animations, fluid structures,<br/>
        and clean responsive layouts. Striving for visual<br/>
        excellence that feels responsive and alive.
      </p>
    </div>

    <!-- 5. FLOATING GIRL ILLUSTRATION (Mid Right) -->
    <div class="absolute top-[800px] right-[150px] w-[380px] z-20 hover-card">
      <div class="w-full relative rounded-[32px] overflow-hidden bg-white/50 backdrop-blur-2xl p-2 border border-white/40 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.05)] transition-all duration-500 hover:shadow-[0_40px_80px_-15px_rgba(177,70,101,0.1)] hover:-translate-y-2">
        <img alt="Shakthi Sri" class="w-full h-auto rounded-[28px] bg-gray-50/50 mix-blend-multiply" src="me.png"/>
      </div>
    </div>

    <!-- 6. LINKEDIN CARD (Bottom Left) -->
    <div class="absolute top-[1500px] left-[150px] w-[360px] z-30 hover-card" id="node-linkedin">
      <a class="bg-white/80 backdrop-blur-xl rounded-[32px] p-8 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.04)] flex flex-col justify-between h-[320px] w-full text-black transform transition-all duration-500 hover:-translate-y-3 cursor-pointer border border-white/60 hover:shadow-[0_40px_80px_-15px_rgba(177,70,101,0.1)] block" href="https://linkedin.com/in/shakthisri" target="_blank">
        <div class="flex justify-between items-start w-full">
          <div class="w-14 h-14 rounded-full bg-[#0a66c2] flex items-center justify-center shadow-[0_8px_15px_-5px_rgba(10,102,194,0.3)]">
            <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"></path></svg>
          </div>
          <div class="flex items-center gap-1 border border-gray-200/50 rounded-md px-3 py-1 bg-gray-50/50">
            <span class="text-[10px] font-bold text-gray-500 uppercase tracking-widest">VERIFIED</span>
          </div>
        </div>
        <div class="mt-4 mb-auto">
          <h3 class="font-bold text-2xl text-[#1F1F1F] mb-1">LinkedIn</h3>
          <p class="text-[12px] text-gray-400 font-medium tracking-wide">Professional Network</p>
          <div class="flex flex-wrap gap-2 mt-5">
            <span class="text-[10px] bg-gray-100/80 text-gray-600 px-4 py-1.5 rounded-full font-bold tracking-wide">Researcher</span>
            <span class="text-[10px] bg-gray-100/80 text-gray-600 px-4 py-1.5 rounded-full font-bold tracking-wide">Tech Enthusiast</span>
          </div>
        </div>
        <div class="pt-5 border-t border-gray-100/80 flex justify-between items-center mt-4">
          <span class="font-bold text-sm text-[#1F1F1F]">@Shakthi16</span>
          <span class="bg-[#1F1F1F] text-white text-[11px] font-bold tracking-wide px-5 py-2.5 rounded-xl hover:bg-[#B14665] transition-colors inline-block">View Profile</span>
        </div>
      </a>
    </div>

    <!-- 7. SHAVIRA CARD (Bottom Right) -->
    <div class="absolute top-[1700px] right-[150px] w-[360px] z-30 hover-card">
      <a class="bg-white/80 backdrop-blur-xl rounded-[32px] p-8 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.04)] flex flex-col justify-between h-[320px] w-full text-black transform transition-all duration-500 hover:-translate-y-3 cursor-pointer border border-white/60 hover:shadow-[0_40px_80px_-15px_rgba(177,70,101,0.1)] block" href="https://www.instagram.com/shaviraworks" target="_blank">
        <div class="flex justify-between items-start w-full">
          <div class="w-14 h-14 rounded-full bg-[#B14665] flex items-center justify-center shadow-[0_8px_15px_-5px_rgba(177,70,101,0.3)]">
            <span class="text-white font-bold font-sans text-2xl">S</span>
          </div>
          <div class="flex items-center gap-1 border border-gray-200/50 rounded-md px-3 py-1 bg-gray-50/50">
            <span class="text-[10px] font-bold text-gray-500 uppercase tracking-widest">STUDIO</span>
          </div>
        </div>
        <div class="mt-4 mb-auto">
          <h3 class="font-bold text-2xl text-[#1F1F1F] mb-1">SHAVIRA</h3>
          <p class="text-[12px] text-gray-400 font-medium tracking-wide mb-3">Creative Freelance &amp; Design</p>
          <p class="text-[12px] text-gray-500 leading-relaxed line-clamp-3">Designing premium web interfaces, visual brand systems, and secure applications. Available for contract collaborations.</p>
        </div>
        <div class="pt-5 border-t border-gray-100/80 flex justify-between items-center mt-4">
          <span class="font-bold text-sm text-[#1F1F1F]">@shavira.studio</span>
          <span class="bg-[#1F1F1F] text-white text-[11px] font-bold tracking-wide px-5 py-2.5 rounded-xl hover:bg-[#B14665] transition-colors inline-block">Follow</span>
        </div>
      </a>
    </div>

  </div>
  
  <!-- Mobile Fallback (Hidden on Desktop) -->
  <div class="relative w-full max-w-[1200px] mx-auto px-6 py-[10vh] flex flex-col gap-24 md:hidden z-10">
      <div class="w-full text-center">
        <h1 class="brand font-bold text-[40px] leading-[1.0] text-[#1F1F1F] tracking-tighter mb-4">I design intelligent<br/>systems.</h1>
      </div>
      <div class="w-full relative rounded-[32px] overflow-hidden shadow-2xl bg-white p-2 border border-gray-100">
        <img alt="Editorial Side" class="w-full h-auto rounded-[24px]" src="bg1.png"/>
      </div>
      <div class="w-full text-center">
        <h2 class="text-[32px] font-bold text-[#1F1F1F] mb-4 tracking-tight leading-[1.1]">I build premium<br/>interfaces.</h2>
      </div>
      <div class="w-full relative rounded-[32px] overflow-hidden shadow-2xl bg-white p-2 border border-gray-100">
        <img alt="Shakthi Sri" class="w-full h-auto rounded-[24px]" src="me.png"/>
      </div>
  </div>
</section>
"""

# Extract the old about section
pattern = r'(<!-- ABOUT: CINEMATIC EDITORIAL CANVAS -->\s*<section.*id="about".*?>.*?</section>)'
match = re.search(pattern, content, re.DOTALL)

if match:
    content = content.replace(match.group(1), new_about_section)
else:
    print("Could not find the about section.")

# Add GSAP draw logic to the main script block
gsap_logic = """
      // NEW SVG DRAW ANIMATION
      if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        const drawPaths = document.querySelectorAll('.draw-path');
        if(drawPaths.length > 0) {
            let drawTimeline = gsap.timeline({
                scrollTrigger: {
                    trigger: '#about',
                    start: 'top 50%',
                    end: 'bottom 50%',
                    scrub: 1,
                }
            });
            drawPaths.forEach((path, i) => {
                let length = path.getTotalLength();
                gsap.set(path, { strokeDasharray: length, strokeDashoffset: length });
                drawTimeline.to(path, { strokeDashoffset: 0, duration: 1, ease: 'power2.inOut' });
            });
        }
      }
"""

# Inject before the final closing script tag
script_inject_pattern = r'(</script>\s*</body>\s*</html>)'
content = re.sub(script_inject_pattern, gsap_logic + r'\n\1', content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html")
