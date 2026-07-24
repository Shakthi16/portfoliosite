import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

SECTION_ABOUT_FULL = """<!-- ABOUT: CINEMATIC EDITORIAL CANVAS -->
<section class="editorial-canvas font-sans relative z-20 overflow-hidden bg-[#dbeafe] text-[#1F1F1F]" id="about" style="min-height: 2700px; background-image: linear-gradient(to bottom, rgba(219, 234, 254, 0.7), rgba(240, 249, 255, 0.85), rgba(250, 248, 245, 0.95)), url('sky_clouds_bg.png'); background-size: cover; background-position: center; background-repeat: no-repeat;">
  <!-- Subtle Grain & Grid Overlay -->
  <div class="absolute inset-0 pointer-events-none z-0 mix-blend-multiply opacity-[0.05]" style="background-image: url('data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noiseFilter%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%220.85%22 numOctaves=%223%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noiseFilter)%22/%3E%3C/svg%3E');"></div>
  <div class="absolute inset-0 pointer-events-none z-0 opacity-[0.03]" style="background-size: 100px 100px; background-image: linear-gradient(to right, #1F1F1F 1px, transparent 1px), linear-gradient(to bottom, #1F1F1F 1px, transparent 1px);"></div>

  <div class="relative w-full max-w-[1400px] mx-auto px-6 lg:px-12 z-10 hidden md:block" id="timeline-container" style="height: 2700px;">
    
    <style>
      .interactive-node { transition: all 0.3s ease; }
      .interactive-node:hover { stroke-width: 4; cursor: pointer; fill: rgba(255,255,255,0.8); }
      .hover-card:hover ~ svg .interactive-node { transform: scale(1.1); transform-origin: center; }
      .journey-path {
        stroke: #475569 !important;
        stroke-width: 2.8px !important;
        stroke-dasharray: 8 8 !important;
        stroke-opacity: 0.95 !important;
        stroke-linecap: round !important;
        stroke-linejoin: round !important;
      }
    </style>

    <!-- THE ARROW SYSTEM SVG -->
    <svg class="absolute inset-0 w-full h-full pointer-events-none z-[50]" id="timeline-svg" viewBox="0 0 1400 2700" preserveAspectRatio="xMidYMid meet">
      <defs>
        <!-- Arrowhead marker -->
        <marker id="arrow-tip" viewBox="0 0 12 12" refX="9" refY="6" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 2 2 L 9 6 L 2 10" fill="none" stroke="#475569" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
        </marker>

        <!-- Glow filter for nodes -->
        <filter id="glow-sm" x="-100%" y="-100%" width="300%" height="300%">
          <feGaussianBlur stdDeviation="3" result="blur"/>
          <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
      </defs>

      <!-- SEG 0: Hero card → Girl illustration -->
      <path id="seg-0" class="journey-path" d="" fill="none" stroke="#475569" stroke-width="2.8" stroke-dasharray="8 8" stroke-opacity="0.95" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow-tip)" />
      <circle id="n0-end" class="journey-node" cx="0" cy="0" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>

      <!-- SEG 1: Girl illustration → Orbital -->
      <path id="seg-1" class="journey-path" d="" fill="none" stroke="#475569" stroke-width="2.8" stroke-dasharray="8 8" stroke-opacity="0.95" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow-tip)" />
      <circle id="n1-end" class="journey-node" cx="0" cy="0" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>

      <!-- SEG 2: Orbital → LinkedIn card -->
      <path id="seg-2" class="journey-path" d="" fill="none" stroke="#475569" stroke-width="2.8" stroke-dasharray="8 8" stroke-opacity="0.95" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow-tip)" />
      <circle id="n2-end" class="journey-node" cx="0" cy="0" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>

      <!-- SEG 3: LinkedIn card → GitHub card -->
      <path id="seg-3" class="journey-path" d="" fill="none" stroke="#475569" stroke-width="2.8" stroke-dasharray="8 8" stroke-opacity="0.95" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow-tip)" />
      <circle id="n3-end" class="journey-node" cx="0" cy="0" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>

      <!-- SEG 4: GitHub card → Shavira card -->
      <path id="seg-4" class="journey-path" d="" fill="none" stroke="#475569" stroke-width="2.8" stroke-dasharray="8 8" stroke-opacity="0.95" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow-tip)" />
      <circle id="n4-end" class="journey-node" cx="0" cy="0" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)" opacity="1"/>
    </svg>

    <!-- UI ELEMENTS -->
    <!-- 1. HERO CARD (Top Left) -->
    <div class="absolute top-[80px] left-[80px] w-[420px] z-20 hover-card rotate-[-1.5deg] hover:rotate-0 transition-transform duration-500" id="node-hero" style="overflow: visible;">
      <div class="absolute -top-5 left-1/2 -translate-x-1/2 w-14 h-8 z-40 pointer-events-none" style="background: rgba(132, 204, 22, 0.88); transform: translateX(-50%) rotate(-3deg); box-shadow: 0 2px 8px rgba(0,0,0,0.15); border-left: 2px dashed rgba(255,255,255,0.5); border-right: 2px dashed rgba(255,255,255,0.5);"></div>
      <div class="w-full relative rounded-[32px] overflow-hidden bg-white/60 backdrop-blur-2xl p-3 border border-white/60 shadow-[0_30px_60px_-15px_rgba(0,0,0,0.06)] transition-all duration-500 hover:shadow-[0_40px_80px_-15px_rgba(66,24,53,0.1)] hover:-translate-y-2">
        <img alt="Editorial Side" class="w-full h-auto rounded-[24px]" src="bg1.png"/>
      </div>
    </div>

    <!-- 2. HEADLINE (Top Right) -->
    <div class="absolute top-[120px] right-[80px] w-[480px] z-20 text-center" id="text-hero">
      <span class="inline-block px-3.5 py-1 bg-[#1e293b] text-white font-mono text-xs font-bold rounded-full mb-3 shadow-sm tracking-wider">{01}</span>
      <h1 class="font-bold text-[42px] leading-[1.1] text-[#1F1F1F] tracking-tighter mb-4">
        I design intelligent<br/>systems.
      </h1>
      <p class="font-sans text-[15px] text-gray-600 leading-[1.6] font-medium">
        Class of 2026 Graduate learning scale.<br/>
        Software engineer &amp; cybersecurity researcher<br/>
        learning speed.<br/>
        Published researcher at <span class="text-[#421835] font-bold">ICTACA'26.</span>
      </p>
    </div>

    <!-- 3. CENTRAL ORBITAL OBJECT (Mid Left) -->
    <div class="absolute top-[980px] left-[80px] w-[260px] h-[260px] z-10 flex items-center justify-center" id="trigger-orbital">
      <!-- Outer rotating ring -->
      <div class="absolute inset-0 rounded-full border-[1px] border-gray-300/60 animate-[spin_60s_linear_infinite]"></div>
      <!-- Middle dashed orbit -->
      <div class="absolute inset-[25px] rounded-full border-[1.5px] border-dashed border-gray-300/80 animate-[spin_40s_linear_infinite_reverse]"></div>
      <!-- Center Text -->
      <div class="absolute z-20 text-center flex flex-col items-center justify-center">
        <div class="text-[#8b2252] text-xl mb-1">✦</div>
        <div class="font-serif italic text-lg text-[#1F1F1F] leading-tight max-w-[140px]">
          Designing<br/>Systems<br/>That Think.
        </div>
      </div>
      <!-- Orbital Labels -->
      <div class="absolute inset-0 animate-[spin_50s_linear_infinite]">
        <div style="position: absolute; top: -12px; left: 50%; transform: translateX(-50%); font-family: 'Outfit', sans-serif; font-size: 8px; font-weight: 700; color: #94a3b8; letter-spacing: 0.15em;">INTENTION</div>
        <div style="position: absolute; top: 30%; right: -15px; transform: rotate(72deg); font-family: 'Outfit', sans-serif; font-size: 8px; font-weight: 700; color: #94a3b8; letter-spacing: 0.15em;">BUILD</div>
        <div style="position: absolute; bottom: 5%; right: 15%; transform: rotate(144deg); font-family: 'Outfit', sans-serif; font-size: 8px; font-weight: 700; color: #94a3b8; letter-spacing: 0.15em;">ITERATE</div>
        <div style="position: absolute; bottom: 5%; left: 15%; transform: rotate(216deg); font-family: 'Outfit', sans-serif; font-size: 8px; font-weight: 700; color: #94a3b8; letter-spacing: 0.15em;">SYSTEMS</div>
        <div style="position: absolute; top: 30%; left: -15px; transform: rotate(288deg); font-family: 'Outfit', sans-serif; font-size: 8px; font-weight: 700; color: #94a3b8; letter-spacing: 0.15em;">RESEARCH</div>
      </div>
    </div>

    <!-- 4. SECOND HEADING (Center) -->
    <div class="absolute top-[940px] left-[480px] w-[440px] z-20 text-left" id="text-premium">
      <span class="inline-block px-3.5 py-1 bg-[#1e293b] text-white font-mono text-xs font-bold rounded-full mb-3 shadow-sm tracking-wider">{02}</span>
      <h2 class="text-[34px] font-bold text-[#1F1F1F] mb-4 tracking-tight leading-[1.1]">I build premium<br/>interfaces.</h2>
      <p class="text-gray-600 font-medium text-[13px] leading-relaxed">
        Focusing on micro-animations, glassmorphic styling,<br/>
        and clean responsive layouts.<br/>
        Striving for visual excellence that feels<br/>
        responsive and alive.
      </p>
    </div>

    <!-- 5. FLOATING GIRL ILLUSTRATION (Mid Right) -->
    <div class="absolute top-[540px] right-[80px] w-[360px] z-20 hover-card rotate-[1.5deg] hover:rotate-0 transition-transform duration-500" id="trigger-girl" style="overflow: visible;">
      <div class="absolute -top-5 left-1/2 -translate-x-1/2 w-14 h-8 z-40 pointer-events-none" style="background: rgba(236, 72, 153, 0.88); transform: translateX(-50%) rotate(4deg); box-shadow: 0 2px 8px rgba(0,0,0,0.15); border-left: 2px dashed rgba(255,255,255,0.5); border-right: 2px dashed rgba(255,255,255,0.5);"></div>
      <div class="w-full relative rounded-[32px] overflow-hidden bg-white/60 backdrop-blur-2xl p-2 border border-white/60 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.05)] transition-all duration-500 hover:shadow-[0_40px_80px_-15px_rgba(66,24,53,0.1)] hover:-translate-y-2">
        <img alt="Shakthi Sri" class="w-full h-auto rounded-[28px] bg-gray-50/50 mix-blend-multiply" src="me.png"/>
      </div>
    </div>

    <!-- 6. LINKEDIN CARD (Bottom Left) -->
    <div class="absolute top-[1400px] left-[80px] w-[340px] z-30 hover-card rotate-[-1.2deg] hover:rotate-0 transition-transform duration-500" id="node-linkedin" style="overflow: visible;">
      <div class="absolute -top-5 left-1/2 -translate-x-1/2 w-14 h-8 z-40 pointer-events-none" style="background: rgba(6, 182, 212, 0.88); transform: translateX(-50%) rotate(-3deg); box-shadow: 0 2px 8px rgba(0,0,0,0.15); border-left: 2px dashed rgba(255,255,255,0.5); border-right: 2px dashed rgba(255,255,255,0.5);"></div>
      <a class="bg-white/85 backdrop-blur-xl rounded-[32px] p-8 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.05)] flex flex-col justify-between h-[320px] w-full text-black transform transition-all duration-500 hover:-translate-y-3 cursor-pointer border border-white/70 hover:shadow-[0_40px_80px_-15px_rgba(66,24,53,0.1)] block" href="https://linkedin.com/in/shakthisri" target="_blank">
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
          <span class="bg-[#1F1F1F] text-white text-[11px] font-bold tracking-wide px-5 py-2.5 rounded-xl hover:bg-[#421835] transition-colors inline-block">View Profile</span>
        </div>
      </a>
    </div>

    <!-- LinkedIn Side Card (Right) -->
    <div class="absolute top-[1400px] left-[480px] w-[480px] z-20 text-left" id="text-linkedin">
      <span class="inline-block px-3.5 py-1 bg-[#1e293b] text-white font-mono text-xs font-bold rounded-full mb-3 shadow-sm tracking-wider">{03}</span>
      <h2 class="text-[34px] font-bold text-[#1F1F1F] mb-4 tracking-tight leading-[1.1]">Connecting with industry leaders.</h2>
      <p class="text-gray-600 font-medium text-[13px] leading-relaxed">
        Building a strong professional network of engineers, designers, and researchers on LinkedIn.<br/>
        Open to contract work, summer internships, and security research collaborations.
      </p>
    </div>

    <!-- 6b. GITHUB CARD (Mid Right) -->
    <div class="absolute top-[1840px] right-[80px] w-[340px] z-30 hover-card rotate-[1.5deg] hover:rotate-0 transition-transform duration-500" id="node-github" style="overflow: visible;">
      <div class="absolute -top-5 left-1/2 -translate-x-1/2 w-14 h-8 z-40 pointer-events-none" style="background: rgba(245, 158, 11, 0.88); transform: translateX(-50%) rotate(3deg); box-shadow: 0 2px 8px rgba(0,0,0,0.15); border-left: 2px dashed rgba(255,255,255,0.5); border-right: 2px dashed rgba(255,255,255,0.5);"></div>
      <a class="bg-white/85 backdrop-blur-xl rounded-[32px] p-8 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.05)] flex flex-col justify-between h-[320px] w-full text-black transform transition-all duration-500 hover:-translate-y-3 cursor-pointer border border-white/70 hover:shadow-[0_40px_80px_-15px_rgba(66,24,53,0.1)] block" href="https://github.com/Shakthi16" target="_blank">
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

    <!-- GitHub Side Card (Left) -->
    <div class="absolute top-[1840px] right-[480px] w-[480px] z-20 text-left" id="text-github">
      <span class="inline-block px-3.5 py-1 bg-[#1e293b] text-white font-mono text-xs font-bold rounded-full mb-3 shadow-sm tracking-wider">{04}</span>
      <h2 class="text-[34px] font-bold text-[#1F1F1F] mb-4 tracking-tight leading-[1.1]">Contributing to open source.</h2>
      <p class="text-gray-600 font-medium text-[13px] leading-relaxed">
        Pushing code, templates, and layouts to GitHub for transparent collaboration.<br/>
        Explore my repos to view security tools, UI playgrounds, and boilerplate architectures.
      </p>
    </div>

    <!-- 7. THIRD HEADING (Bottom Center) -->
    <div class="absolute top-[2280px] left-[480px] w-[480px] z-20 text-left" id="trigger-crafting">
      <span class="inline-block px-3.5 py-1 bg-[#1e293b] text-white font-mono text-xs font-bold rounded-full mb-3 shadow-sm tracking-wider">{05}</span>
      <h2 class="text-[30px] font-bold text-[#1F1F1F] mb-4 tracking-tight leading-[1.1]">Crafting bespoke digital<br/>products.</h2>
      <p class="text-gray-600 font-medium text-[12px] leading-relaxed">
        Delivering design and code collaborations under the<br/>
        studio banner SHAVIRA.<br/>
        Creating high-performance full-stack web<br/>
        applications with robust security.
      </p>
    </div>

    <!-- 8. SHAVIRA CARD (Bottom Right) -->
    <div class="absolute top-[2280px] left-[80px] w-[340px] z-30 hover-card rotate-[-1.5deg] hover:rotate-0 transition-transform duration-500" id="trigger-shavira" style="overflow: visible;">
      <div class="absolute -top-5 left-1/2 -translate-x-1/2 w-14 h-8 z-40 pointer-events-none" style="background: rgba(168, 85, 247, 0.88); transform: translateX(-50%) rotate(-4deg); box-shadow: 0 2px 8px rgba(0,0,0,0.15); border-left: 2px dashed rgba(255,255,255,0.5); border-right: 2px dashed rgba(255,255,255,0.5);"></div>
      <div class="bg-white/85 backdrop-blur-xl rounded-[32px] p-8 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.05)] flex flex-col justify-between h-[320px] w-full text-black transform transition-all duration-500 hover:-translate-y-3 border border-white/70 hover:shadow-[0_40px_80px_-15px_rgba(66,24,53,0.1)] block">
        <div class="flex justify-between items-start w-full">
          <div class="w-14 h-14 rounded-full bg-[#421835] flex items-center justify-center shadow-[0_8px_15px_-5px_rgba(66,24,53,0.3)]">
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
          <span class="bg-[#1F1F1F] text-white text-[11px] font-bold tracking-wide px-5 py-2.5 rounded-xl hover:bg-[#421835] transition-colors inline-block">Follow</span>
        </div>
      </div>
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
    <div class="w-full text-center">
      <h2 class="text-[32px] font-bold text-[#1F1F1F] mb-4 tracking-tight leading-[1.1]">Crafting bespoke digital<br/>products.</h2>
    </div>
  </div>
</section>
"""

# Place section #about directly before <section id="timeline-pin-section"
TARGET = '<section id="timeline-pin-section"'
if TARGET in content:
    content = content.replace(TARGET, SECTION_ABOUT_FULL + "\n\n" + TARGET)
    print("Inserted #about section right before #timeline-pin-section.")
else:
    print("TARGET <section id=\"timeline-pin-section\" not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
