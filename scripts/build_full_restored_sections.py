import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# -------------------------------------------------------------
# 1. THE EDITORIAL CANVAS (#about)
# -------------------------------------------------------------
EDITORIAL_ABOUT_HTML = """<!-- ABOUT: CINEMATIC EDITORIAL CANVAS -->
<section class="editorial-canvas font-sans relative z-20 overflow-hidden text-[#1F1F1F]" id="about" style="min-height: 2700px; background: linear-gradient(to bottom, rgba(219,234,254,0.8) 0%, rgba(240,249,255,0.9) 40%, rgba(250,248,245,0.95) 100%), url('sky_clouds_bg.png') center/cover no-repeat;">
  <!-- Grain overlay -->
  <div class="absolute inset-0 pointer-events-none z-0 mix-blend-multiply opacity-[0.04]" style="background-image: url('data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22n%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%220.85%22 numOctaves=%223%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23n)%22/%3E%3C/svg%3E');"></div>

  <style>
    .journey-path {
      stroke: #64748b !important;
      stroke-width: 2.5px !important;
      stroke-dasharray: 8 8 !important;
      stroke-opacity: 1 !important;
      stroke-linecap: round !important;
      fill: none !important;
    }
    .hover-card { transition: all 0.3s ease; }
  </style>

  <!-- Desktop Canvas -->
  <div class="relative w-full max-w-[1400px] mx-auto px-6 lg:px-12 z-10 hidden md:block" id="timeline-container" style="height: 2700px;">

    <!-- SVG ARROW SYSTEM -->
    <svg class="absolute inset-0 w-full h-full pointer-events-none" id="timeline-svg" viewBox="0 0 1400 2700" preserveAspectRatio="xMidYMid meet" style="z-index: 50; overflow: visible;">
      <defs>
        <marker id="arrow-tip" viewBox="0 0 12 12" refX="9" refY="6" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 2 2 L 9 6 L 2 10" fill="none" stroke="#64748b" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
        </marker>
        <filter id="glow-sm" x="-100%" y="-100%" width="300%" height="300%">
          <feGaussianBlur stdDeviation="3" result="blur"/>
          <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
      </defs>
      <path id="seg-0" class="journey-path" d="" marker-end="url(#arrow-tip)"/>
      <circle id="n0-end" cx="0" cy="0" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)"/>
      <path id="seg-1" class="journey-path" d="" marker-end="url(#arrow-tip)"/>
      <circle id="n1-end" cx="0" cy="0" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)"/>
      <path id="seg-2" class="journey-path" d="" marker-end="url(#arrow-tip)"/>
      <circle id="n2-end" cx="0" cy="0" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)"/>
      <path id="seg-3" class="journey-path" d="" marker-end="url(#arrow-tip)"/>
      <circle id="n3-end" cx="0" cy="0" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)"/>
      <path id="seg-4" class="journey-path" d="" marker-end="url(#arrow-tip)"/>
      <circle id="n4-end" cx="0" cy="0" r="5" fill="#421835" stroke="white" stroke-width="1.5" filter="url(#glow-sm)"/>
    </svg>

    <!-- 1. HERO CARD (Top Left) -->
    <div class="absolute top-[80px] left-[80px] w-[420px] z-20 hover-card rotate-[-1.5deg] hover:rotate-0 transition-transform duration-500" id="node-hero" style="overflow:visible;">
      <!-- Lime washi tape clip -->
      <div class="absolute left-1/2 z-40 pointer-events-none" style="top:-20px; width:56px; height:28px; background:rgba(132,204,22,0.9); transform:translateX(-50%) rotate(-3deg); box-shadow:0 2px 8px rgba(0,0,0,0.18); border-left:2px dashed rgba(255,255,255,0.55); border-right:2px dashed rgba(255,255,255,0.55);"></div>
      <div class="w-full relative rounded-[32px] overflow-hidden bg-white/65 backdrop-blur-2xl p-3 border border-white/60 shadow-[0_30px_60px_-15px_rgba(0,0,0,0.07)] transition-all duration-500 hover:shadow-[0_40px_80px_-15px_rgba(66,24,53,0.1)] hover:-translate-y-2">
        <img alt="Editorial Side" class="w-full h-auto rounded-[24px]" src="bg1.png"/>
      </div>
    </div>

    <!-- 2. HEADLINE — Top Right -->
    <div class="absolute top-[120px] right-[80px] w-[480px] z-20 text-center" id="text-hero">
      <span class="inline-block px-3.5 py-1 bg-[#1e293b] text-white font-mono text-xs font-bold rounded-full mb-3 shadow-sm tracking-wider">{01}</span>
      <h1 class="font-bold text-[42px] leading-[1.1] text-[#1F1F1F] tracking-tighter mb-4">I design intelligent<br/>systems.</h1>
      <p class="font-sans text-[15px] text-gray-600 leading-[1.7] font-medium">
        Class of 2026 Graduate learning scale.<br/>
        Software engineer &amp; cybersecurity researcher<br/>
        learning speed.<br/>
        Published researcher at <span class="text-[#421835] font-bold">ICTACA'26.</span>
      </p>
    </div>

    <!-- 3. GIRL ILLUSTRATION — Mid Right -->
    <div class="absolute top-[540px] right-[80px] w-[360px] z-20 hover-card rotate-[1.5deg] hover:rotate-0 transition-transform duration-500" id="trigger-girl" style="overflow:visible;">
      <!-- Hot-pink washi tape clip -->
      <div class="absolute left-1/2 z-40 pointer-events-none" style="top:-20px; width:56px; height:28px; background:rgba(236,72,153,0.9); transform:translateX(-50%) rotate(4deg); box-shadow:0 2px 8px rgba(0,0,0,0.18); border-left:2px dashed rgba(255,255,255,0.55); border-right:2px dashed rgba(255,255,255,0.55);"></div>
      <div class="w-full relative rounded-[32px] overflow-hidden bg-white/65 backdrop-blur-2xl p-2 border border-white/60 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.05)] transition-all duration-500 hover:shadow-[0_40px_80px_-15px_rgba(66,24,53,0.1)] hover:-translate-y-2">
        <img alt="Shakthi Sri" class="w-full h-auto rounded-[28px] bg-gray-50/50 mix-blend-multiply" src="me.png"/>
      </div>
    </div>

    <!-- 4. ORBITAL OBJECT — Mid Left -->
    <div class="absolute top-[980px] left-[80px] w-[260px] h-[260px] z-10 flex items-center justify-center" id="trigger-orbital">
      <div class="absolute inset-0 rounded-full border border-gray-300/60 animate-[spin_60s_linear_infinite]"></div>
      <div class="absolute inset-[25px] rounded-full border border-dashed border-gray-300/80 animate-[spin_40s_linear_infinite_reverse]"></div>
      <div class="absolute z-20 text-center flex flex-col items-center justify-center">
        <div class="text-[#8b2252] text-xl mb-1">✦</div>
        <div class="font-serif italic text-lg text-[#1F1F1F] leading-tight max-w-[140px]">Designing<br/>Systems<br/>That Think.</div>
      </div>
      <div class="absolute inset-0 animate-[spin_50s_linear_infinite]">
        <div style="position:absolute;top:-12px;left:50%;transform:translateX(-50%);font-size:8px;font-weight:700;color:#94a3b8;letter-spacing:0.15em;">INTENTION</div>
        <div style="position:absolute;top:30%;right:-15px;transform:rotate(72deg);font-size:8px;font-weight:700;color:#94a3b8;letter-spacing:0.15em;">BUILD</div>
        <div style="position:absolute;bottom:5%;right:15%;transform:rotate(144deg);font-size:8px;font-weight:700;color:#94a3b8;letter-spacing:0.15em;">ITERATE</div>
        <div style="position:absolute;bottom:5%;left:15%;transform:rotate(216deg);font-size:8px;font-weight:700;color:#94a3b8;letter-spacing:0.15em;">SYSTEMS</div>
        <div style="position:absolute;top:30%;left:-15px;transform:rotate(288deg);font-size:8px;font-weight:700;color:#94a3b8;letter-spacing:0.15em;">RESEARCH</div>
      </div>
    </div>

    <!-- 5. HEADLINE 2 — Center -->
    <div class="absolute top-[940px] left-[400px] w-[440px] z-20 text-left" id="text-premium">
      <span class="inline-block px-3.5 py-1 bg-[#1e293b] text-white font-mono text-xs font-bold rounded-full mb-3 shadow-sm tracking-wider">{02}</span>
      <h2 class="text-[34px] font-bold text-[#1F1F1F] mb-4 tracking-tight leading-[1.1]">I build premium<br/>interfaces.</h2>
      <p class="text-gray-600 font-medium text-[13px] leading-relaxed">
        Focusing on micro-animations, glassmorphic styling,<br/>
        and clean responsive layouts.<br/>
        Striving for visual excellence that feels<br/>
        responsive and alive.
      </p>
    </div>

    <!-- 6. LINKEDIN CARD — Bottom Left -->
    <div class="absolute top-[1400px] left-[80px] w-[340px] z-30 hover-card rotate-[-1.2deg] hover:rotate-0 transition-transform duration-500" id="node-linkedin" style="overflow:visible;">
      <!-- Cyan washi tape clip -->
      <div class="absolute left-1/2 z-40 pointer-events-none" style="top:-20px; width:56px; height:28px; background:rgba(6,182,212,0.9); transform:translateX(-50%) rotate(-3deg); box-shadow:0 2px 8px rgba(0,0,0,0.18); border-left:2px dashed rgba(255,255,255,0.55); border-right:2px dashed rgba(255,255,255,0.55);"></div>
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

    <!-- LinkedIn Text — Right of LinkedIn Card -->
    <div class="absolute top-[1420px] left-[480px] w-[460px] z-20 text-left" id="text-linkedin">
      <span class="inline-block px-3.5 py-1 bg-[#1e293b] text-white font-mono text-xs font-bold rounded-full mb-3 shadow-sm tracking-wider">{03}</span>
      <h2 class="text-[34px] font-bold text-[#1F1F1F] mb-4 tracking-tight leading-[1.1]">Connecting with industry leaders.</h2>
      <p class="text-gray-600 font-medium text-[13px] leading-relaxed">
        Building a strong professional network of engineers,<br/>designers, and researchers on LinkedIn.<br/>
        Open to contract work, summer internships, and<br/>security research collaborations.
      </p>
    </div>

    <!-- 7. GITHUB CARD — Mid Right -->
    <div class="absolute top-[1840px] right-[80px] w-[340px] z-30 hover-card rotate-[1.5deg] hover:rotate-0 transition-transform duration-500" id="node-github" style="overflow:visible;">
      <!-- Amber washi tape clip -->
      <div class="absolute left-1/2 z-40 pointer-events-none" style="top:-20px; width:56px; height:28px; background:rgba(245,158,11,0.9); transform:translateX(-50%) rotate(3deg); box-shadow:0 2px 8px rgba(0,0,0,0.18); border-left:2px dashed rgba(255,255,255,0.55); border-right:2px dashed rgba(255,255,255,0.55);"></div>
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
          <p class="text-[12px] text-gray-400 font-medium tracking-wide">Code &amp; Repositories</p>
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

    <!-- GitHub Text — Left of GitHub Card -->
    <div class="absolute top-[1860px] right-[480px] w-[460px] z-20 text-left" id="text-github">
      <span class="inline-block px-3.5 py-1 bg-[#1e293b] text-white font-mono text-xs font-bold rounded-full mb-3 shadow-sm tracking-wider">{04}</span>
      <h2 class="text-[34px] font-bold text-[#1F1F1F] mb-4 tracking-tight leading-[1.1]">Contributing to open source.</h2>
      <p class="text-gray-600 font-medium text-[13px] leading-relaxed">
        Pushing code, templates, and layouts to GitHub<br/>for transparent collaboration.<br/>
        Explore my repos to view security tools, UI playgrounds,<br/>and boilerplate architectures.
      </p>
    </div>

    <!-- 8. SHAVIRA CARD — Bottom Left -->
    <div class="absolute top-[2280px] left-[80px] w-[340px] z-30 hover-card rotate-[-1.5deg] hover:rotate-0 transition-transform duration-500" id="trigger-shavira" style="overflow:visible;">
      <!-- Purple washi tape clip -->
      <div class="absolute left-1/2 z-40 pointer-events-none" style="top:-20px; width:56px; height:28px; background:rgba(168,85,247,0.9); transform:translateX(-50%) rotate(-4deg); box-shadow:0 2px 8px rgba(0,0,0,0.18); border-left:2px dashed rgba(255,255,255,0.55); border-right:2px dashed rgba(255,255,255,0.55);"></div>
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
          <p class="text-[12px] text-gray-500 leading-relaxed">Designing premium web interfaces, visual brand systems, and secure applications. Available for contract collaborations.</p>
        </div>
        <div class="pt-5 border-t border-gray-100/80 flex justify-between items-center mt-4">
          <span class="font-bold text-sm text-[#1F1F1F]">@shavira.studio</span>
          <span class="bg-[#1F1F1F] text-white text-[11px] font-bold tracking-wide px-5 py-2.5 rounded-xl hover:bg-[#421835] transition-colors inline-block">Follow</span>
        </div>
      </div>
    </div>

    <!-- 9. CRAFTING TEXT — Bottom Right -->
    <div class="absolute top-[2300px] left-[480px] w-[460px] z-20 text-left" id="trigger-crafting">
      <span class="inline-block px-3.5 py-1 bg-[#1e293b] text-white font-mono text-xs font-bold rounded-full mb-3 shadow-sm tracking-wider">{05}</span>
      <h2 class="text-[30px] font-bold text-[#1F1F1F] mb-4 tracking-tight leading-[1.1]">Crafting bespoke digital<br/>products.</h2>
      <p class="text-gray-600 font-medium text-[12px] leading-relaxed">
        Delivering design and code collaborations under<br/>
        the studio banner SHAVIRA.<br/>
        Creating high-performance full-stack web<br/>
        applications with robust security.
      </p>
    </div>

  </div><!-- /timeline-container -->

  <!-- Mobile Fallback -->
  <div class="relative w-full max-w-[700px] mx-auto px-6 py-16 flex flex-col gap-16 md:hidden z-10">
    <div class="text-center">
      <h1 class="font-bold text-[36px] leading-tight text-[#1F1F1F] tracking-tighter mb-3">I design intelligent systems.</h1>
    </div>
    <div class="rounded-[28px] overflow-hidden shadow-xl bg-white p-2 border border-gray-100">
      <img alt="Editorial Side" class="w-full h-auto rounded-[22px]" src="bg1.png"/>
    </div>
    <div class="text-center">
      <h2 class="text-[30px] font-bold text-[#1F1F1F] mb-3 tracking-tight">I build premium interfaces.</h2>
    </div>
    <div class="rounded-[28px] overflow-hidden shadow-xl bg-white p-2 border border-gray-100">
      <img alt="Shakthi Sri" class="w-full h-auto rounded-[22px]" src="me.png"/>
    </div>
    <div class="text-center">
      <h2 class="text-[30px] font-bold text-[#1F1F1F] mb-3 tracking-tight">Crafting bespoke digital products.</h2>
    </div>
  </div>
</section>
"""

# -------------------------------------------------------------
# 2. HORIZONTAL SCROLL PROFESSIONAL JOURNEY (#timeline-pin-section)
# -------------------------------------------------------------
HORIZONTAL_JOURNEY_HTML = """<!-- HORIZONTAL PINNED PROFESSIONAL JOURNEY -->
<section class="relative bg-[#FAFAFA] text-[#1F1F1F] overflow-hidden py-24 border-t border-b border-gray-200/60" id="timeline-pin-section">
  
  <div class="max-w-7xl mx-auto px-6 mb-12 flex flex-col md:flex-row justify-between items-start md:items-end">
    <div>
      <span class="text-xs uppercase tracking-[0.2em] text-[#8b2252] font-mono font-bold block mb-2">EXPERIENCE &amp; RESEARCH</span>
      <h2 class="text-4xl md:text-6xl font-bold font-sans tracking-tight text-[#1F1F1F]">Professional Journey</h2>
    </div>
    <p class="text-sm text-gray-500 font-medium max-w-md mt-4 md:mt-0">
      Offensive security research, full-stack development, and workflow automation. Scroll horizontally to view milestones.
    </p>
  </div>

  <!-- Horizontal Scroll Track -->
  <div class="relative w-full overflow-hidden" id="timeline-scroll-wrapper" style="min-height: 480px;">
    
    <!-- Year Digits Watermark Background -->
    <div class="absolute inset-0 pointer-events-none flex items-center justify-between opacity-[0.06] select-none z-0 px-12" style="font-family: 'Outfit', sans-serif; font-size: 240px; font-weight: 900; color: #1F1F1F; letter-spacing: -0.05em;">
      <span class="year-digit-1">2025</span>
      <span class="year-digit-2">2026</span>
    </div>

    <!-- Cards Container -->
    <div class="flex gap-12 px-6 md:px-20 py-6 w-max relative z-10 transition-transform duration-300" id="timeline-scroll-content">
      
      <!-- CARD 1: IIT Madras CYSTAR Lab -->
      <div class="timeline-scroll-item flex flex-col md:flex-row items-center gap-8 bg-white/90 backdrop-blur-xl rounded-[36px] p-6 md:p-8 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.08)] border border-gray-200/80 w-[90vw] md:w-[720px] shrink-0">
        <div class="relative w-full md:w-[300px] h-[220px] rounded-[28px] overflow-hidden shrink-0 shadow-md">
          <img src="bg1.png" alt="IIT Madras CYSTAR Lab" class="w-full h-full object-cover"/>
          <div class="absolute bottom-4 left-4 bg-black/80 backdrop-blur-md text-white font-mono text-[10px] font-bold uppercase tracking-wider px-3.5 py-1.5 rounded-full border border-white/20">
            AUG 2025 - PRESENT
          </div>
        </div>
        <div class="flex flex-col justify-center text-left">
          <span class="text-[11px] font-mono uppercase tracking-[0.2em] text-[#8b2252] font-bold mb-2">CYBERSECURITY RESEARCH INTERN</span>
          <h3 class="text-2xl md:text-3xl font-bold text-[#1F1F1F] mb-3 leading-tight">IIT Madras — CYSTAR Lab</h3>
          <p class="text-xs md:text-sm text-gray-600 leading-relaxed font-medium">
            Conducting offensive security research workflows including vulnerability exposure analysis, studying AV/EDR evasion techniques, implementing explainable security models, and producing thorough technical documentation.
          </p>
        </div>
      </div>

      <!-- CARD 2: OpsIntellix -->
      <div class="timeline-scroll-item flex flex-col md:flex-row items-center gap-8 bg-white/90 backdrop-blur-xl rounded-[36px] p-6 md:p-8 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.08)] border border-gray-200/80 w-[90vw] md:w-[720px] shrink-0">
        <div class="relative w-full md:w-[300px] h-[220px] rounded-[28px] overflow-hidden shrink-0 shadow-md">
          <img src="opsintellix.png" alt="OpsIntellix" class="w-full h-full object-cover"/>
          <div class="absolute bottom-4 left-4 bg-black/80 backdrop-blur-md text-white font-mono text-[10px] font-bold uppercase tracking-wider px-3.5 py-1.5 rounded-full border border-white/20">
            NOV 2025 - FEB 2026
          </div>
        </div>
        <div class="flex flex-col justify-center text-left">
          <span class="text-[11px] font-mono uppercase tracking-[0.2em] text-[#8b2252] font-bold mb-2">OPERATIONS INTERN — AP AUTOMATION</span>
          <h3 class="text-2xl md:text-3xl font-bold text-[#1F1F1F] mb-3 leading-tight">OpsIntellix</h3>
          <p class="text-xs md:text-sm text-gray-600 leading-relaxed font-medium">
            Automated banking workflows, invoice processing pipelines, document classification, and validation using Python, driving processing efficiency up by 30%.
          </p>
        </div>
      </div>

      <!-- CARD 3: Focuslogic IT Services -->
      <div class="timeline-scroll-item flex flex-col md:flex-row items-center gap-8 bg-white/90 backdrop-blur-xl rounded-[36px] p-6 md:p-8 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.08)] border border-gray-200/80 w-[90vw] md:w-[720px] shrink-0">
        <div class="relative w-full md:w-[300px] h-[220px] rounded-[28px] overflow-hidden shrink-0 shadow-md">
          <img src="write.png" alt="Focuslogic IT Services" class="w-full h-full object-cover"/>
          <div class="absolute bottom-4 left-4 bg-black/80 backdrop-blur-md text-white font-mono text-[10px] font-bold uppercase tracking-wider px-3.5 py-1.5 rounded-full border border-white/20">
            MAR 2025 - MAY 2025
          </div>
        </div>
        <div class="flex flex-col justify-center text-left">
          <span class="text-[11px] font-mono uppercase tracking-[0.2em] text-[#8b2252] font-bold mb-2">WEB DEVELOPMENT INTERN</span>
          <h3 class="text-2xl md:text-3xl font-bold text-[#1F1F1F] mb-3 leading-tight">Focuslogic IT Services</h3>
          <p class="text-xs md:text-sm text-gray-600 leading-relaxed font-medium">
            Built responsive React.js frontends from Figma designs, integrated REST APIs, conducted manual UI testing, and reduced load latency by 25%.
          </p>
        </div>
      </div>

    </div>
  </div>
</section>
"""

# -------------------------------------------------------------
# 3. ACADEMIC BACKGROUND SECTION
# -------------------------------------------------------------
ACADEMIC_SECTION_HTML = """<!-- ACADEMIC BACKGROUND -->
<section class="py-20 bg-[#F5F5F7] text-[#1F1F1F] border-b border-gray-200/60" id="academic-background">
  <div class="max-w-7xl mx-auto px-6 lg:px-12">
    <div class="text-center mb-12">
      <span class="text-xs uppercase tracking-[0.2em] text-[#8b2252] font-mono font-bold block mb-2">EDUCATION</span>
      <h2 class="text-4xl md:text-6xl font-bold font-sans tracking-tight text-[#1F1F1F]">Academic Background</h2>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      
      <!-- B.Tech Card -->
      <div class="bg-white/90 backdrop-blur-xl rounded-[32px] p-8 border border-gray-200/80 shadow-[0_15px_40px_-15px_rgba(0,0,0,0.05)] hover:shadow-[0_25px_60px_-15px_rgba(66,24,53,0.1)] transition-all duration-500 hover:-translate-y-2 flex flex-col justify-between h-[240px]">
        <div>
          <span class="text-xs font-mono font-bold text-gray-400 uppercase tracking-widest block mb-2">2022 — 2026</span>
          <h3 class="text-2xl font-bold text-[#1F1F1F] mb-1">B.Tech in IT</h3>
          <p class="text-xs text-gray-500 font-medium">Kingston Eng. College</p>
        </div>
        <div class="pt-4 border-t border-gray-100 flex justify-between items-end">
          <span class="text-xs text-gray-400 font-bold uppercase tracking-wider">CGPA</span>
          <span class="text-4xl font-extrabold text-[#421835] tracking-tight">9.03</span>
        </div>
      </div>

      <!-- HSC Card -->
      <div class="bg-white/90 backdrop-blur-xl rounded-[32px] p-8 border border-gray-200/80 shadow-[0_15px_40px_-15px_rgba(0,0,0,0.05)] hover:shadow-[0_25px_60px_-15px_rgba(66,24,53,0.1)] transition-all duration-500 hover:-translate-y-2 flex flex-col justify-between h-[240px]">
        <div>
          <span class="text-xs font-mono font-bold text-gray-400 uppercase tracking-widest block mb-2">2021 — 2022</span>
          <h3 class="text-2xl font-bold text-[#1F1F1F] mb-1">HSC</h3>
          <p class="text-xs text-gray-500 font-medium">Sai Guruji School</p>
        </div>
        <div class="pt-4 border-t border-gray-100 flex justify-between items-end">
          <span class="text-xs text-gray-400 font-bold uppercase tracking-wider">SCORE</span>
          <span class="text-4xl font-extrabold text-[#421835] tracking-tight">89.2%</span>
        </div>
      </div>

      <!-- SSLC Card -->
      <div class="bg-white/90 backdrop-blur-xl rounded-[32px] p-8 border border-gray-200/80 shadow-[0_15px_40px_-15px_rgba(0,0,0,0.05)] hover:shadow-[0_25px_60px_-15px_rgba(66,24,53,0.1)] transition-all duration-500 hover:-translate-y-2 flex flex-col justify-between h-[240px]">
        <div>
          <span class="text-xs font-mono font-bold text-gray-400 uppercase tracking-widest block mb-2">2019 — 2020</span>
          <h3 class="text-2xl font-bold text-[#1F1F1F] mb-1">SSLC</h3>
          <p class="text-xs text-gray-500 font-medium">Sai Guruji School</p>
        </div>
        <div class="pt-4 border-t border-gray-100 flex justify-between items-end">
          <span class="text-xs text-gray-400 font-bold uppercase tracking-wider">SCORE</span>
          <span class="text-4xl font-extrabold text-[#421835] tracking-tight">92%</span>
        </div>
      </div>

    </div>
  </div>
</section>
"""

# -------------------------------------------------------------
# 4. LEARNING IN MOTION SECTION (MATCHING IMAGE 2 EXACTLY)
# -------------------------------------------------------------
LEARNING_IN_MOTION_HTML = """<!-- LEARNING IN MOTION SECTION -->
<section class="py-28 bg-[#FAFAFA] text-[#1F1F1F] overflow-hidden relative border-b border-gray-200/60" id="learning-in-motion">
  
  <div class="max-w-4xl mx-auto text-center px-6 mb-16">
    <h2 class="text-5xl md:text-7xl font-extrabold font-sans tracking-tight text-[#1F1F1F] mb-4">Learning in Motion</h2>
    <div class="w-2.5 h-2.5 rounded-full bg-[#ec4899] mx-auto mb-6 shadow-sm"></div>
    <p class="text-sm md:text-base text-gray-600 font-medium leading-relaxed max-w-lg mx-auto">
      A mindset of curiosity. A habit of growth.<br/>Constantly exploring, building, and leveling up.
    </p>
  </div>

  <!-- Angled Marquee Ribbons (Plum Background #3d1830) -->
  <div class="relative w-[130vw] -ml-[15vw] space-y-6">
    
    <!-- RIBBON 1 (Angled -2deg) -->
    <div class="bg-[#3d1830] text-white py-5 shadow-xl rotate-[-2deg] overflow-hidden flex items-center border-y border-white/10">
      <div class="marquee-track flex items-center gap-12 whitespace-nowrap animate-[marquee_25s_linear_infinite]">
        
        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">IN</span>
          <div class="text-left"><span class="font-bold text-sm block">Infosys</span><span class="text-[11px] text-pink-200/80">UI/UX, React, AI, Python</span></div>
        </div>

        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">UD</span>
          <div class="text-left"><span class="font-bold text-sm block">Udemy</span><span class="text-[11px] text-pink-200/80">Cybersecurity</span></div>
        </div>

        <div class="flex items-center gap-2 text-pink-300 font-mono text-xs font-bold px-4">
          <span class="text-lg">✦</span> 150+ Hours of Learning
        </div>

        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">GO</span>
          <div class="text-left"><span class="font-bold text-sm block">Google</span><span class="text-[11px] text-pink-200/80">Data Analytics &amp; Cloud</span></div>
        </div>

        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">NT</span>
          <div class="text-left"><span class="font-bold text-sm block">NoviTech</span><span class="text-[11px] text-pink-200/80">Full Stack Web Dev</span></div>
        </div>

        <span class="text-xl text-pink-300 px-2">→</span>

        <!-- Duplicated items for seamless loop -->
        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">IN</span>
          <div class="text-left"><span class="font-bold text-sm block">Infosys</span><span class="text-[11px] text-pink-200/80">UI/UX, React, AI, Python</span></div>
        </div>

        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">UD</span>
          <div class="text-left"><span class="font-bold text-sm block">Udemy</span><span class="text-[11px] text-pink-200/80">Cybersecurity</span></div>
        </div>

      </div>
    </div>

    <!-- RIBBON 2 (Angled -2deg Reverse) -->
    <div class="bg-[#3d1830] text-white py-5 shadow-xl rotate-[-2deg] overflow-hidden flex items-center border-y border-white/10">
      <div class="marquee-track flex items-center gap-12 whitespace-nowrap animate-[marquee-reverse_30s_linear_infinite]">
        
        <span class="text-xl text-pink-300 px-2">→</span>

        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">GO</span>
          <div class="text-left"><span class="font-bold text-sm block">Google</span><span class="text-[11px] text-pink-200/80">Data Analytics &amp; Cloud</span></div>
        </div>

        <span class="text-lg text-pink-300">✦</span>

        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">IN</span>
          <div class="text-left"><span class="font-bold text-sm block">Infosys</span><span class="text-[11px] text-pink-200/80">UI/UX, React, AI, Python</span></div>
        </div>

        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">UD</span>
          <div class="text-left"><span class="font-bold text-sm block">Udemy</span><span class="text-[11px] text-pink-200/80">Cybersecurity</span></div>
        </div>

        <div class="text-pink-300 font-mono text-xs font-bold px-4">
          Always Exploring Always Evolving
        </div>

        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">GO</span>
          <div class="text-left"><span class="font-bold text-sm block">Google</span><span class="text-[11px] text-pink-200/80">Data Analytics &amp; Cloud</span></div>
        </div>

        <span class="text-xl text-pink-300 px-2">→</span>

      </div>
    </div>

  </div>
</section>
"""

# -------------------------------------------------------------
# 5. THE JOURNAL SECTION WITH COVER.PNG
# -------------------------------------------------------------
JOURNAL_SECTION_HTML = """<!-- THE JOURNAL SECTION WITH COVER.PNG -->
<section class="py-24 bg-[#FAF8F5] text-[#1F1F1F] overflow-hidden relative border-b border-gray-200/60" id="about-journal">
  <div class="max-w-6xl mx-auto px-6">
    
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
      
      <!-- Left Column: The Interactive Book / Journal (using cover.png) -->
      <div class="lg:col-span-6 flex justify-center">
        <div class="relative group cursor-pointer perspective-1000">
          <div class="w-[320px] md:w-[380px] h-[480px] rounded-[24px] shadow-[0_30px_70px_-15px_rgba(0,0,0,0.2)] overflow-hidden transition-transform duration-700 group-hover:rotate-y-12 group-hover:scale-105 border border-white/60 relative bg-white">
            <!-- Journal Cover Image -->
            <img src="cover.png" alt="Shakthi Sri Journal Cover" class="w-full h-full object-cover"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent pointer-events-none"></div>
            <div class="absolute bottom-8 left-8 text-white">
              <span class="font-mono text-[10px] tracking-[0.2em] uppercase bg-white/20 backdrop-blur-md px-3 py-1 rounded-full border border-white/30">INTERACTIVE JOURNAL</span>
              <h3 class="text-2xl font-bold font-serif italic mt-2">Notes &amp; Reflections</h3>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Column: Description & Highlights -->
      <div class="lg:col-span-6 text-left">
        <span class="text-xs uppercase tracking-[0.2em] text-[#8b2252] font-mono font-bold block mb-2">PERSONAL NOTES</span>
        <h2 class="text-4xl md:text-5xl font-bold text-[#1F1F1F] mb-6 tracking-tight">The Engineer's Journal</h2>
        <p class="text-sm md:text-base text-gray-600 leading-relaxed font-medium mb-8">
          A personal collection of architectural blueprints, malware analysis findings, design experiments, and security research notes documented during my journey.
        </p>

        <div class="space-y-4">
          <div class="p-5 rounded-2xl bg-white border border-gray-200/80 shadow-sm flex items-start gap-4">
            <span class="text-xl text-[#8b2252]">✦</span>
            <div>
              <h4 class="font-bold text-sm text-[#1F1F1F]">Cybersecurity Research</h4>
              <p class="text-xs text-gray-500 mt-1">EDR evasion analysis, explainable security models, and offensive vulnerability testing.</p>
            </div>
          </div>
          <div class="p-5 rounded-2xl bg-white border border-gray-200/80 shadow-sm flex items-start gap-4">
            <span class="text-xl text-[#8b2252]">✦</span>
            <div>
              <h4 class="font-bold text-sm text-[#1F1F1F]">System Design &amp; Automation</h4>
              <p class="text-xs text-gray-500 mt-1">Python automation scripts, REST API architecture, and micro-frontend performance tuning.</p>
            </div>
          </div>
        </div>

      </div>

    </div>

  </div>
</section>
"""

# Replace all old about/journey/skills blocks in index.html cleanly
content = re.sub(r'<!-- ABOUT: CINEMATIC EDITORIAL CANVAS -->.*?(?=<!-- SKILLS -->)', 
                 EDITORIAL_ABOUT_HTML + '\n\n' + HORIZONTAL_JOURNEY_HTML + '\n\n' + ACADEMIC_SECTION_HTML + '\n\n' + LEARNING_IN_MOTION_HTML + '\n\n' + JOURNAL_SECTION_HTML + '\n\n', 
                 content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully injected all restored sections into index.html!")
