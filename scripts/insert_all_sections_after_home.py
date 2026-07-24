import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# All Sections HTML to be placed right after line 3861 (the closing </section> of #home)
ALL_PORTFOLIO_SECTIONS = """
<!-- ==================== 1. ABOUT ME: INTERACTIVE 3-PAGE JOURNAL BOOK ==================== -->
<section class="relative bg-[#f4efe6] text-[#1F1F1F] py-24 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">
  <div class="max-w-6xl mx-auto px-4 md:px-8">
    
    <!-- Header & Page Controls -->
    <div class="flex flex-col md:flex-row justify-between items-center mb-10 gap-4">
      <div class="text-center md:text-left">
        <span class="text-xs uppercase tracking-[0.25em] text-[#8b2252] font-mono font-bold block mb-1">ABOUT ME</span>
        <h2 class="text-3xl md:text-5xl font-bold font-serif italic text-[#1F1F1F]">The Personal Journal</h2>
      </div>

      <!-- Page Flip Controls -->
      <div class="flex items-center gap-3 bg-white/80 backdrop-blur-md px-4 py-2 rounded-full border border-amber-900/10 shadow-sm">
        <button onclick="switchJournalTab('cover')" id="tab-cover" class="px-4 py-1.5 text-xs font-bold font-mono rounded-full transition-all bg-[#421835] text-white">Cover</button>
        <button onclick="switchJournalTab('spread1')" id="tab-spread1" class="px-4 py-1.5 text-xs font-bold font-mono rounded-full transition-all text-gray-600 hover:text-black">Page 1-2</button>
        <button onclick="switchJournalTab('spread2')" id="tab-spread2" class="px-4 py-1.5 text-xs font-bold font-mono rounded-full transition-all text-gray-600 hover:text-black">Page 3</button>
      </div>
    </div>

    <!-- BOOK STAGE CONTAINER -->
    <div class="relative w-full max-w-[960px] mx-auto min-h-[580px] flex items-center justify-center">

      <!-- VIEW 1: CLOSED JOURNAL COVER -->
      <div id="jview-cover" class="jview transition-all duration-700 ease-out transform opacity-100 scale-100 flex flex-col items-center">
        <div class="relative group cursor-pointer" onclick="switchJournalTab('spread1')">
          <div class="w-[320px] md:w-[390px] h-[520px] rounded-[26px] shadow-[0_30px_70px_-15px_rgba(0,0,0,0.25)] overflow-hidden relative bg-[#1b4d3e] border border-emerald-900/40 transition-transform duration-500 hover:scale-[1.02]">
            <img src="cover.png" alt="Shakthi Sri Journal Cover" class="w-full h-full object-cover"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/40 via-transparent to-transparent pointer-events-none"></div>
            
            <div class="absolute inset-0 bg-black/20 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
              <span class="bg-white/90 backdrop-blur-md text-black font-mono text-xs font-bold px-6 py-3 rounded-full shadow-xl border border-white/60 tracking-wider uppercase">Click to Open Journal →</span>
            </div>
          </div>
          <div class="absolute -bottom-6 left-12 w-6 h-12 bg-[#55826b] rounded-b-md shadow-md pointer-events-none"></div>
        </div>
      </div>

      <!-- VIEW 2: OPENED SPREAD (PAGES 1 & 2) -->
      <div id="jview-spread1" class="jview hidden transition-all duration-700 ease-out transform opacity-0 scale-95 w-full">
        
        <div class="w-full bg-[#faf7f2] rounded-[32px] shadow-[0_30px_80px_-20px_rgba(0,0,0,0.18)] border border-amber-900/15 p-6 md:p-10 relative overflow-hidden" style="background-image: radial-gradient(#d6cebe 1px, transparent 1px); background-size: 20px 20px;">
          
          <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[2px] bg-amber-900/15 hidden md:block"></div>
          <div class="absolute bottom-0 left-1/2 -translate-x-1/2 w-6 h-8 bg-[#55826b] rounded-t-sm shadow-md hidden md:block"></div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-10 md:gap-14 relative z-10">
            
            <!-- LEFT PAGE: BIO & EXPERIENCE TIMELINE -->
            <div class="flex flex-col justify-between text-left pr-0 md:pr-4">
              <div>
                <h3 class="text-3xl md:text-4xl font-bold font-serif text-[#1F1F1F] mb-3 tracking-tight">Shakthi Sri T S</h3>
                
                <div class="flex flex-wrap gap-2 mb-6">
                  <span class="px-3.5 py-1 bg-sky-100 text-sky-800 text-[11px] font-mono font-bold rounded-full border border-sky-200">Software Engineer</span>
                  <span class="px-3.5 py-1 bg-purple-100 text-purple-800 text-[11px] font-mono font-bold rounded-full border border-purple-200">Cybersecurity Researcher</span>
                </div>

                <div class="space-y-3 font-sans text-xs md:text-sm text-gray-700 font-medium mb-6">
                  <div class="flex justify-between items-center border-b border-amber-900/10 pb-2">
                    <span class="flex items-center gap-2 font-bold text-[#421835]"><span class="text-xs">●</span> IIT Madras CYSTAR Lab</span>
                    <span class="font-mono text-xs text-gray-500">2025 — Present</span>
                  </div>
                  <div class="flex justify-between items-center border-b border-amber-900/10 pb-2">
                    <span class="flex items-center gap-2 font-bold text-[#421835]"><span class="text-xs">●</span> OpsIntellix</span>
                    <span class="font-mono text-xs text-gray-500">2025 — 2026</span>
                  </div>
                  <div class="flex justify-between items-center border-b border-amber-900/10 pb-2">
                    <span class="flex items-center gap-2 font-bold text-[#421835]"><span class="text-xs">●</span> Focuslogic IT Services</span>
                    <span class="font-mono text-xs text-gray-500">2025 — 2025</span>
                  </div>
                  <div class="flex justify-between items-center border-b border-amber-900/10 pb-2">
                    <span class="flex items-center gap-2 font-bold text-[#421835]"><span class="text-xs">●</span> Kingston Eng. College</span>
                    <span class="font-mono text-xs text-gray-500">2022 — 2026</span>
                  </div>
                </div>

                <div class="bg-white/80 rounded-2xl p-4 border border-amber-900/10 shadow-sm mb-6">
                  <div class="flex items-center gap-1.5 mb-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-rose-400"></span>
                    <span class="w-2.5 h-2.5 rounded-full bg-amber-400"></span>
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                    <span class="text-[10px] font-mono text-gray-400 ml-2">Today</span>
                  </div>
                  <p class="text-xs text-gray-600 leading-relaxed font-medium">
                    Building intelligent systems that perform at scale and keep user data secure. <span class="italic text-gray-800">"Usability and security must coexist seamlessly."</span>
                  </p>
                </div>
              </div>

              <div class="pt-4 border-t border-dashed border-amber-900/20 flex flex-col sm:flex-row justify-between items-start sm:items-end gap-3">
                <div class="bg-amber-100/60 p-3 rounded-xl text-[11px] font-mono text-gray-700 border border-amber-900/10">
                  <p class="font-bold">shakthisri1929@gmail.com</p>
                  <p class="text-gray-500">Vellore | Tamil Nadu, India</p>
                </div>
                <p class="font-serif italic text-xs text-[#8b2252] font-semibold">"Write, build, iterate — make an impact!"</p>
              </div>

            </div>

            <!-- RIGHT PAGE: PHOTO & FLOATING STICKERS -->
            <div class="flex flex-col items-center justify-center relative min-h-[380px]">
              
              <div class="relative z-20 group">
                <div class="w-[200px] md:w-[240px] h-[240px] md:h-[280px] rounded-[24px] overflow-hidden shadow-xl border-4 border-white transform rotate-[-2deg] transition-transform duration-500 group-hover:rotate-0">
                  <img src="me.png" alt="Shakthi Sri" class="w-full h-full object-cover"/>
                </div>
                <div class="absolute -top-3 right-2 bg-black/80 text-white font-mono text-[10px] font-bold px-3 py-1 rounded-full shadow-md z-30">
                  @Shakthi16
                </div>
              </div>

              <div class="absolute top-2 left-2 z-10 pointer-events-none transform -rotate-12">
                <span class="text-2xl">🌸</span>
                <span class="block text-[9px] font-mono text-gray-400">flower.png</span>
              </div>

              <div class="absolute top-2 right-4 z-10 pointer-events-none text-center">
                <div class="w-10 h-10 bg-sky-400/20 rounded-xl flex items-center justify-center text-sky-600 text-lg mx-auto">📁</div>
                <span class="block text-[9px] font-mono text-gray-500 mt-1">Cursor</span>
              </div>

              <div class="absolute top-1/2 right-0 -translate-y-1/2 z-10 pointer-events-none text-center hidden sm:block">
                <span class="text-2xl">🏋️‍♀️</span>
                <span class="block text-[9px] font-mono text-gray-400">lifestyle</span>
              </div>

              <div class="absolute bottom-4 left-4 z-10 pointer-events-none text-center">
                <div class="w-9 h-9 bg-purple-500/20 rounded-xl flex items-center justify-center text-purple-700 text-base mx-auto">💻</div>
                <span class="block text-[9px] font-mono text-gray-500 mt-1">Experiments.md</span>
              </div>

              <div class="absolute bottom-4 right-4 z-10 pointer-events-none text-center">
                <span class="text-2xl">🥤</span>
                <span class="block text-[9px] font-mono text-gray-400">CoffeeLover.png</span>
              </div>

            </div>

          </div>

        </div>
      </div>

      <!-- VIEW 3: PAGE 3 (NOTES & REFLECTIONS) -->
      <div id="jview-spread2" class="jview hidden transition-all duration-700 ease-out transform opacity-0 scale-95 w-full">
        
        <div class="w-full bg-[#faf7f2] rounded-[32px] shadow-[0_30px_80px_-20px_rgba(0,0,0,0.18)] border border-amber-900/15 p-6 md:p-10 relative overflow-hidden" style="background-image: radial-gradient(#d6cebe 1px, transparent 1px); background-size: 20px 20px;">
          
          <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[2px] bg-amber-900/15 hidden md:block"></div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-10 md:gap-14 relative z-10 text-left">
            
            <div class="space-y-4">
              <span class="text-xs font-mono uppercase tracking-[0.2em] text-[#8b2252] font-bold block">PAGE 3 — NOTES</span>
              <h3 class="text-2xl font-bold font-serif text-[#1F1F1F]">Research &amp; Security Findings</h3>
              
              <div class="p-4 rounded-2xl bg-white/80 border border-amber-900/10 space-y-2">
                <h4 class="font-bold text-xs text-[#421835]">● EDR &amp; AV Evasion Study</h4>
                <p class="text-xs text-gray-600 leading-relaxed font-medium">Investigating behavioral endpoint telemetry, bypass mechanisms, and memory inspection techniques in modern security controls.</p>
              </div>

              <div class="p-4 rounded-2xl bg-white/80 border border-amber-900/10 space-y-2">
                <h4 class="font-bold text-xs text-[#421835]">● ICTACA'26 Publication</h4>
                <p class="text-xs text-gray-600 leading-relaxed font-medium">Authored research paper on explainable cybersecurity models and exposure risk prioritization for enterprise networks.</p>
              </div>
            </div>

            <div class="space-y-4">
              <span class="text-xs font-mono uppercase tracking-[0.2em] text-[#8b2252] font-bold block">REFLECTIONS &amp; IDEAS</span>
              <h3 class="text-2xl font-bold font-serif text-[#1F1F1F]">Full-Stack &amp; Automation</h3>
              
              <div class="p-4 rounded-2xl bg-white/80 border border-amber-900/10 space-y-2">
                <h4 class="font-bold text-xs text-[#421835]">● Banking AP Automation</h4>
                <p class="text-xs text-gray-600 leading-relaxed font-medium">Built automated document validation and invoice extraction pipelines with Python, achieving 30% speedup.</p>
              </div>

              <div class="p-4 rounded-2xl bg-white/80 border border-amber-900/10 space-y-2">
                <h4 class="font-bold text-xs text-[#421835]">● SHAVIRA Studio Mission</h4>
                <p class="text-xs text-gray-600 leading-relaxed font-medium">Combining high-level aesthetic craftsmanship with bulletproof backend architecture for bespoke client products.</p>
              </div>
            </div>

          </div>

        </div>
      </div>

    </div>

  </div>
</section>

<!-- Journal Switcher Script -->
<script>
  function switchJournalTab(targetId) {
    const vCover = document.getElementById('jview-cover');
    const vSpread1 = document.getElementById('jview-spread1');
    const vSpread2 = document.getElementById('jview-spread2');

    const tabCover = document.getElementById('tab-cover');
    const tabSpread1 = document.getElementById('tab-spread1');
    const tabSpread2 = document.getElementById('tab-spread2');

    const views = [vCover, vSpread1, vSpread2];
    const tabs = [tabCover, tabSpread1, tabSpread2];

    views.forEach(v => {
      if (v) {
        v.classList.add('hidden');
        v.classList.remove('opacity-100', 'scale-100');
        v.classList.add('opacity-0', 'scale-95');
      }
    });

    tabs.forEach(t => {
      if (t) {
        t.classList.remove('bg-[#421835]', 'text-white');
        t.classList.add('text-gray-600');
      }
    });

    let selView, selTab;
    if (targetId === 'cover') { selView = vCover; selTab = tabCover; }
    else if (targetId === 'spread1') { selView = vSpread1; selTab = tabSpread1; }
    else if (targetId === 'spread2') { selView = vSpread2; selTab = tabSpread2; }

    if (selView && selTab) {
      selView.classList.remove('hidden');
      setTimeout(() => {
        selView.classList.remove('opacity-0', 'scale-95');
        selView.classList.add('opacity-100', 'scale-100');
      }, 40);

      selTab.classList.remove('text-gray-600');
      selTab.classList.add('bg-[#421835]', 'text-white');
    }
  }
</script>

<!-- ==================== 2. EDITORIAL CANVAS (#about) ==================== -->
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

  </div>

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

# Replace everything from the end of #home (line 3861) up to <script src="https://cdnjs.cloudflare.com/...
target_start = content.find('</section>', content.find('id="home"')) + len('</section>')
target_end = content.find('<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap')

if target_start != -1 and target_end != -1:
    content = content[:target_start] + '\n\n' + ALL_PORTFOLIO_SECTIONS + '\n\n' + content[target_end:]
    print("Successfully inserted Journal Book & Editorial Canvas directly after #home!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
