import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = 'id="timeline-pin-section"'
start_pos = text.find(start_marker)
if start_pos == -1:
    print("Could not find start marker!")
    exit(1)

sec_start = text.rfind('<section', 0, start_pos)
sec_end = text.find('</section>', start_pos) + len('</section>')

diego_sevilla_section = '''<section class="relative bg-[#F8FBFF] text-[#222222] overflow-hidden py-16 border-t border-b border-[#0162e6]/10" id="timeline-pin-section" style="min-height: 100vh;">

  <!-- Faint Dot Grid & Ambient Light Glow -->
  <div class="absolute inset-0 pointer-events-none opacity-[0.035] z-0" style="background-image: radial-gradient(#0157cb 1.5px, transparent 1.5px); background-size: 28px 28px;"></div>
  <div class="absolute top-1/4 left-1/4 w-[500px] h-[500px] bg-[#0162e6]/5 rounded-full blur-[120px] pointer-events-none z-0"></div>
  <div class="absolute bottom-1/4 right-1/4 w-[600px] h-[600px] bg-[#388eff]/5 rounded-full blur-[140px] pointer-events-none z-0"></div>

  <!-- Outer Track Canvas for GSAP Horizontal Pinning -->
  <div class="relative w-full overflow-hidden" id="timeline-scroll-wrapper" style="min-height: 680px;">

    <!-- Massive Year Digits Watermark (Diego Sevilla Signature Parallax) -->
    <div id="timeline-year-watermark" class="absolute inset-0 pointer-events-none flex items-center justify-between opacity-[0.05] select-none z-0 px-20 transition-transform duration-300" style="font-family: 'Outfit', sans-serif; font-size: 280px; font-weight: 900; color: #0157cb; letter-spacing: -0.06em; min-width: 3200px;">
      <span class="translate-x-12">2025</span>
      <span class="translate-x-64">2026</span>
    </div>

    <!-- MAIN SVG CIRCUIT PATH & CONNECTING STEMS -->
    <svg class="absolute top-0 left-0 w-[3600px] h-full pointer-events-none z-10 overflow-visible" id="timeline-circuit-svg" viewBox="0 0 3600 680" fill="none">
      <defs>
        <linearGradient id="ds-blue-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#0157cb" />
          <stop offset="40%" stop-color="#0162e6" />
          <stop offset="70%" stop-color="#388eff" />
          <stop offset="100%" stop-color="#0157cb" />
        </linearGradient>
        <filter id="ds-glow" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="5" result="blur" />
          <feMerge>
            <feMergeNode in="blur" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
      </defs>

      <!-- Main Weaving Circuit Line across all 3 experiences -->
      <path id="ds-circuit-main-path" d="M 50 180 L 400 180 C 550 180, 600 220, 750 220 L 1050 220 C 1200 220, 1250 460, 1400 460 L 1750 460 C 1900 460, 1950 200, 2100 200 L 2450 200 C 2600 200, 2650 360, 2800 360 L 3200 360" stroke="url(#ds-blue-gradient)" stroke-width="4" stroke-linecap="round" filter="url(#ds-glow)" />

      <!-- Dashed Circuit Stems & Dots -->
      <!-- Stem 1: Header to Intro -->
      <path d="M 280 180 L 280 240" stroke="#0162e6" stroke-width="2" stroke-dasharray="4 4" />
      <circle cx="280" cy="180" r="5" fill="#0162e6" />
      <circle cx="280" cy="240" r="4" fill="#0162e6" />

      <!-- Stem 2: IIT Madras Node -->
      <path d="M 880 220 L 880 140" stroke="#0162e6" stroke-width="2" stroke-dasharray="4 4" />
      <circle cx="880" cy="220" r="7" fill="#0157cb" stroke="#FFFFFF" stroke-width="2" />

      <!-- Stem 3: OpsIntellix Node -->
      <path d="M 1580 460 L 1580 540" stroke="#f29111" stroke-width="2" stroke-dasharray="4 4" />
      <circle cx="1580" cy="460" r="7" fill="#f29111" stroke="#FFFFFF" stroke-width="2" />

      <!-- Stem 4: Focuslogic Node -->
      <path d="M 2280 200 L 2280 120" stroke="#8b5cf6" stroke-width="2" stroke-dasharray="4 4" />
      <circle cx="2280" cy="200" r="7" fill="#8b5cf6" stroke="#FFFFFF" stroke-width="2" />

      <!-- Stem 5: Coming Soon Node -->
      <circle cx="2800" cy="360" r="9" fill="#0157cb" stroke="#FFFFFF" stroke-width="3" />
      <circle cx="2800" cy="360" r="18" fill="none" stroke="#0162e6" stroke-width="1.5" stroke-dasharray="4 4" class="animate-[spin_12s_linear_infinite]" />

      <!-- Animated Traveling Traveler Dot (Diego Sevilla Feature) -->
      <circle id="ds-traveler-dot" cx="50" cy="180" r="8" fill="#0162e6" stroke="#FFFFFF" stroke-width="3" filter="url(#ds-glow)" />
    </svg>


    <!-- HORIZONTAL SCROLL CONTENT TRACK -->
    <div class="flex items-center gap-16 px-12 md:px-24 py-8 w-max relative z-20 transition-transform duration-300" id="timeline-scroll-content">

      <!-- STAGE 0: TITLE & INTRO HEADER (Diego Sevilla Web Style) -->
      <div class="w-[380px] shrink-0 flex flex-col justify-center pr-4">
        <!-- Floating Cloud & Gear Tech Graphic (Diego Sevilla Header Icon) -->
        <div class="w-20 h-20 mb-6 relative flex items-center justify-center">
          <div class="absolute inset-0 bg-[#0162e6]/10 rounded-3xl rotate-6"></div>
          <div class="relative w-16 h-16 rounded-2xl bg-white shadow-lg border border-[#0162e6]/20 flex items-center justify-center text-[#0157cb]">
            <!-- Cloud + Gear Vector SVG -->
            <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 00-9.78 2.096A4.001 4.001 0 003 15z"></path>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 12m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0"></path>
            </svg>
          </div>
        </div>

        <h2 class="text-4xl md:text-5xl font-black tracking-tight text-[#012c66] leading-tight mb-3" style="font-family: 'Outfit', sans-serif;">
          Work<br/>
          <span class="text-[#0157cb]">Experiences</span>
        </h2>
        <p class="text-xs md:text-sm text-slate-500 font-medium leading-relaxed mb-6 max-w-xs">
          A interactive timeline of my cybersecurity research, software engineering, and process automation roles.
        </p>

        <div class="inline-flex items-center gap-2 text-xs font-bold text-[#0157cb] bg-[#0162e6]/10 px-4 py-2 rounded-full w-max">
          <span>Scroll to explore</span>
          <svg class="w-4 h-4 animate-bounce-x" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
        </div>
      </div>


      <!-- STAGE 1: IIT MADRAS — CYSTAR LAB (Upper Tier Card + Floating Graphic Badges) -->
      <div class="timeline-stage-item relative flex flex-col justify-start w-[88vw] md:w-[720px] shrink-0 -mt-16">
        
        <!-- EXPERIENCE CARD -->
        <div class="bg-white/95 backdrop-blur-xl rounded-[32px] p-8 border border-blue-100/90 shadow-[0_25px_60px_-15px_rgba(1,87,203,0.12)] relative z-20 transition-transform duration-500 hover:-translate-y-2">
          
          <!-- Card Header Row -->
          <div class="flex items-start justify-between mb-4">
            <div>
              <h3 class="text-2xl md:text-3xl font-extrabold text-[#012c66] tracking-tight mb-1" style="font-family: 'Outfit', sans-serif;">
                IIT Madras — CYSTAR Lab
              </h3>
              <p class="text-xs md:text-sm font-bold text-[#0162e6] tracking-wide uppercase font-mono">
                Cybersecurity Research Intern
              </p>
            </div>
            <div class="flex flex-col items-end">
              <span class="px-4 py-1.5 rounded-full bg-[#0162e6]/10 text-[#0157cb] font-mono text-[11px] font-bold">
                Jul 2025 – May 2026
              </span>
              <span class="text-[10px] text-slate-400 font-semibold mt-1">Chennai, India</span>
            </div>
          </div>

          <!-- Description Paragraph -->
          <p class="text-xs md:text-sm text-slate-600 leading-relaxed font-medium mb-6">
            Conducted cybersecurity research focused on exposure analysis, EDR/AV behaviour evaluation, and secure system design under supervised research initiatives.
          </p>

          <!-- Key Duties Button (Exact Diego Sevilla Pill Style) -->
          <div class="flex items-center justify-between pt-4 border-t border-slate-100">
            <button onclick="openDutyModal('ds-modal-cystar')" class="px-6 py-2.5 rounded-full bg-[#0157cb] hover:bg-[#014198] text-white font-bold text-xs shadow-lg shadow-[#0157cb]/25 transition-all transform hover:scale-105 flex items-center gap-2">
              <span>Key Duties</span>
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
            </button>
            <span class="text-[11px] font-mono text-slate-400 font-semibold">CYSTAR Lab</span>
          </div>
        </div>

        <!-- FLOATING GRAPHIC MEDIA BADGES (Diego Sevilla Grid Gallery Style below Card) -->
        <div class="grid grid-cols-2 gap-4 mt-6 relative z-10 px-2">
          <div class="relative h-[120px] rounded-2xl overflow-hidden shadow-md group border border-slate-200/60">
            <img src="bg1.png" alt="Research Lab" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"/>
            <div class="absolute inset-0 bg-slate-900/40 flex items-end p-3">
              <span class="text-white text-[11px] font-bold font-mono">✦ Exposure Analysis</span>
            </div>
          </div>
          <div class="relative h-[120px] rounded-2xl overflow-hidden shadow-md group border border-slate-200/60">
            <img src="research.png" alt="Cyber Security" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"/>
            <div class="absolute inset-0 bg-slate-900/40 flex items-end p-3">
              <span class="text-white text-[11px] font-bold font-mono">✦ EDR / AV Behavior</span>
            </div>
          </div>
        </div>

      </div>


      <!-- STAGE 2: OPSINTELLIX (Lower Tier Card + Floating Graphic Badges) -->
      <div class="timeline-stage-item relative flex flex-col justify-end w-[88vw] md:w-[720px] shrink-0 mt-20">

        <!-- FLOATING GRAPHIC MEDIA BADGES (Upper Gallery for OpsIntellix) -->
        <div class="grid grid-cols-2 gap-4 mb-6 relative z-10 px-2">
          <div class="relative h-[120px] rounded-2xl overflow-hidden shadow-md group border border-amber-200/60">
            <img src="opsintellix.png" alt="OpsIntellix" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"/>
            <div class="absolute inset-0 bg-slate-900/40 flex items-end p-3">
              <span class="text-white text-[11px] font-bold font-mono">✦ Banking & Mortgage</span>
            </div>
          </div>
          <div class="relative h-[120px] rounded-2xl overflow-hidden shadow-md group border border-amber-200/60">
            <img src="bento-tech.png" alt="Python Automation" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"/>
            <div class="absolute inset-0 bg-slate-900/40 flex items-end p-3">
              <span class="text-amber-300 text-[11px] font-bold font-mono">✦ +30% Efficiency</span>
            </div>
          </div>
        </div>
        
        <!-- EXPERIENCE CARD -->
        <div class="bg-white/95 backdrop-blur-xl rounded-[32px] p-8 border border-amber-200/80 shadow-[0_25px_60px_-15px_rgba(242,145,17,0.12)] relative z-20 transition-transform duration-500 hover:-translate-y-2">
          
          <!-- Card Header Row -->
          <div class="flex items-start justify-between mb-4">
            <div>
              <h3 class="text-2xl md:text-3xl font-extrabold text-[#012c66] tracking-tight mb-1" style="font-family: 'Outfit', sans-serif;">
                OpsIntellix
              </h3>
              <p class="text-xs md:text-sm font-bold text-[#f29111] tracking-wide uppercase font-mono">
                Operations Intern — AP Automation
              </p>
            </div>
            <div class="flex flex-col items-end">
              <span class="px-4 py-1.5 rounded-full bg-amber-100/80 text-[#d88328] font-mono text-[11px] font-bold">
                Nov 2025 – Feb 2026
              </span>
            </div>
          </div>

          <!-- Description Paragraph -->
          <p class="text-xs md:text-sm text-slate-600 leading-relaxed font-medium mb-6">
            Automated mortgage and banking workflows using Python, including document classification, data extraction, validation, and reporting processes.
          </p>

          <!-- Key Duties Button (Exact Diego Sevilla Pill Style) -->
          <div class="flex items-center justify-between pt-4 border-t border-slate-100">
            <button onclick="openDutyModal('ds-modal-opsintellix')" class="px-6 py-2.5 rounded-full bg-[#f29111] hover:bg-[#e58a25] text-white font-bold text-xs shadow-lg shadow-[#f29111]/25 transition-all transform hover:scale-105 flex items-center gap-2">
              <span>Key Duties</span>
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
            </button>
            <span class="text-[11px] font-mono text-slate-400 font-semibold">OpsIntellix</span>
          </div>
        </div>

      </div>


      <!-- STAGE 3: FOCUSLOGIC IT SERVICES (Upper Tier Card + Floating Graphic Badges) -->
      <div class="timeline-stage-item relative flex flex-col justify-start w-[88vw] md:w-[720px] shrink-0 -mt-16">
        
        <!-- EXPERIENCE CARD -->
        <div class="bg-white/95 backdrop-blur-xl rounded-[32px] p-8 border border-purple-100/90 shadow-[0_25px_60px_-15px_rgba(139,92,246,0.12)] relative z-20 transition-transform duration-500 hover:-translate-y-2">
          
          <!-- Card Header Row -->
          <div class="flex items-start justify-between mb-4">
            <div>
              <h3 class="text-2xl md:text-3xl font-extrabold text-[#012c66] tracking-tight mb-1" style="font-family: 'Outfit', sans-serif;">
                Focuslogic IT Services
              </h3>
              <p class="text-xs md:text-sm font-bold text-[#8b5cf6] tracking-wide uppercase font-mono">
                Web Development Intern
              </p>
            </div>
            <div class="flex flex-col items-end">
              <span class="px-4 py-1.5 rounded-full bg-purple-100/80 text-[#7c3aed] font-mono text-[11px] font-bold">
                Mar 2025 – May 2025
              </span>
            </div>
          </div>

          <!-- Description Paragraph -->
          <p class="text-xs md:text-sm text-slate-600 leading-relaxed font-medium mb-6">
            Developed responsive and accessible web applications using React.js, HTML, CSS, and Tailwind CSS based on Figma design specifications.
          </p>

          <!-- Key Duties Button (Exact Diego Sevilla Pill Style) -->
          <div class="flex items-center justify-between pt-4 border-t border-slate-100">
            <button onclick="openDutyModal('ds-modal-focuslogic')" class="px-6 py-2.5 rounded-full bg-[#8b5cf6] hover:bg-[#7c3aed] text-white font-bold text-xs shadow-lg shadow-[#8b5cf6]/25 transition-all transform hover:scale-105 flex items-center gap-2">
              <span>Key Duties</span>
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
            </button>
            <span class="text-[11px] font-mono text-slate-400 font-semibold">Focuslogic</span>
          </div>
        </div>

        <!-- FLOATING GRAPHIC MEDIA BADGES (Lower Gallery for Focuslogic) -->
        <div class="grid grid-cols-2 gap-4 mt-6 relative z-10 px-2">
          <div class="relative h-[120px] rounded-2xl overflow-hidden shadow-md group border border-slate-200/60">
            <img src="write.png" alt="React Web Apps" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"/>
            <div class="absolute inset-0 bg-slate-900/40 flex items-end p-3">
              <span class="text-white text-[11px] font-bold font-mono">✦ React.js & Tailwind</span>
            </div>
          </div>
          <div class="relative h-[120px] rounded-2xl overflow-hidden shadow-md group border border-slate-200/60">
            <img src="card.png" alt="Figma Integration" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"/>
            <div class="absolute inset-0 bg-slate-900/40 flex items-end p-3">
              <span class="text-purple-300 text-[11px] font-bold font-mono">✦ -25% Load Time</span>
            </div>
          </div>
        </div>

      </div>


      <!-- STAGE 4: COMING SOON / FUTURE MILESTONES (Diego Sevilla End Card) -->
      <div class="w-[320px] shrink-0 flex flex-col items-center justify-center text-center pr-12">
        <div class="w-16 h-16 rounded-full bg-[#0157cb]/10 border border-[#0162e6]/20 flex items-center justify-center text-[#0157cb] mb-4 shadow-sm animate-pulse">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path></svg>
        </div>
        <h4 class="text-2xl font-black text-[#012c66] tracking-tight mb-2" style="font-family: 'Outfit', sans-serif;">
          Next Chapters
        </h4>
        <p class="text-xs text-slate-400 font-medium max-w-[200px]">
          Always building, researching, and scaling intelligent systems.
        </p>
      </div>

    </div>
  </div>


  <!-- DETAIL MODALS FOR KEY DUTIES -->

  <!-- MODAL 1: IIT Madras CYSTAR Lab -->
  <div id="ds-modal-cystar" class="duty-modal fixed inset-0 z-[999] flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-md opacity-0 pointer-events-none transition-all duration-300">
    <div class="relative bg-white rounded-[32px] p-8 max-w-xl w-full border border-blue-100 shadow-2xl transform scale-95 transition-all duration-300">
      <button onclick="closeDutyModal('ds-modal-cystar')" class="absolute top-6 right-6 w-9 h-9 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center font-bold text-base transition-colors">✕</button>
      
      <div class="flex items-center gap-3 mb-3">
        <span class="w-3 h-3 rounded-full bg-[#0157cb]"></span>
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-[#0157cb]">Jul 2025 – May 2026</span>
      </div>
      <h3 class="text-2xl font-extrabold text-[#012c66] mb-1" style="font-family: 'Outfit', sans-serif;">IIT Madras — CYSTAR Lab</h3>
      <p class="text-xs font-mono font-bold text-slate-400 uppercase tracking-wider mb-6">Cybersecurity Research Intern</p>
      
      <div class="space-y-4 text-xs md:text-sm text-slate-600 leading-relaxed font-medium">
        <div class="flex items-start gap-3 bg-[#0162e6]/5 p-4 rounded-2xl border border-[#0162e6]/10">
          <span class="text-[#0157cb] font-bold text-base mt-0.5">✦</span>
          <p>Conducted cybersecurity research focused on exposure analysis, EDR/AV behaviour evaluation, and secure system design under supervised research initiatives.</p>
        </div>
        <div class="flex items-start gap-3 bg-[#0162e6]/5 p-4 rounded-2xl border border-[#0162e6]/10">
          <span class="text-[#0157cb] font-bold text-base mt-0.5">✦</span>
          <p>Contributed to the development of explainable security workflows, technical research documentation, and security tool evaluation for cybersecurity research projects.</p>
        </div>
        <div class="flex items-start gap-3 bg-[#0162e6]/5 p-4 rounded-2xl border border-[#0162e6]/10">
          <span class="text-[#0157cb] font-bold text-base mt-0.5">✦</span>
          <p>Collaborated with research teams on threat modelling, security analysis, and confidential research activities within enterprise security environments.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL 2: OpsIntellix -->
  <div id="ds-modal-opsintellix" class="duty-modal fixed inset-0 z-[999] flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-md opacity-0 pointer-events-none transition-all duration-300">
    <div class="relative bg-white rounded-[32px] p-8 max-w-xl w-full border border-amber-100 shadow-2xl transform scale-95 transition-all duration-300">
      <button onclick="closeDutyModal('ds-modal-opsintellix')" class="absolute top-6 right-6 w-9 h-9 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center font-bold text-base transition-colors">✕</button>
      
      <div class="flex items-center gap-3 mb-3">
        <span class="w-3 h-3 rounded-full bg-[#f29111]"></span>
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-[#d88328]">Nov 2025 – Feb 2026</span>
      </div>
      <h3 class="text-2xl font-extrabold text-[#012c66] mb-1" style="font-family: 'Outfit', sans-serif;">OpsIntellix</h3>
      <p class="text-xs font-mono font-bold text-slate-400 uppercase tracking-wider mb-6">Operations Intern — AP Automation</p>
      
      <div class="space-y-4 text-xs md:text-sm text-slate-600 leading-relaxed font-medium">
        <div class="flex items-start gap-3 bg-amber-500/5 p-4 rounded-2xl border border-amber-500/10">
          <span class="text-[#f29111] font-bold text-base mt-0.5">✦</span>
          <p>Automated mortgage and banking workflows using Python, including document classification, data extraction, validation, and reporting processes.</p>
        </div>
        <div class="flex items-start gap-3 bg-amber-500/5 p-4 rounded-2xl border border-amber-500/10">
          <span class="text-[#f29111] font-bold text-base mt-0.5">✦</span>
          <p>Optimized business process automation pipelines, improving operational efficiency by 30% while supporting compliance-driven workflows.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL 3: Focuslogic IT Services -->
  <div id="ds-modal-focuslogic" class="duty-modal fixed inset-0 z-[999] flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-md opacity-0 pointer-events-none transition-all duration-300">
    <div class="relative bg-white rounded-[32px] p-8 max-w-xl w-full border border-purple-100 shadow-2xl transform scale-95 transition-all duration-300">
      <button onclick="closeDutyModal('ds-modal-focuslogic')" class="absolute top-6 right-6 w-9 h-9 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center font-bold text-base transition-colors">✕</button>
      
      <div class="flex items-center gap-3 mb-3">
        <span class="w-3 h-3 rounded-full bg-[#8b5cf6]"></span>
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-[#7c3aed]">Mar 2025 – May 2025</span>
      </div>
      <h3 class="text-2xl font-extrabold text-[#012c66] mb-1" style="font-family: 'Outfit', sans-serif;">Focuslogic IT Services</h3>
      <p class="text-xs font-mono font-bold text-slate-400 uppercase tracking-wider mb-6">Web Development Intern</p>
      
      <div class="space-y-4 text-xs md:text-sm text-slate-600 leading-relaxed font-medium">
        <div class="flex items-start gap-3 bg-purple-500/5 p-4 rounded-2xl border border-purple-500/10">
          <span class="text-[#8b5cf6] font-bold text-base mt-0.5">✦</span>
          <p>Developed responsive and accessible web applications using React.js, HTML, CSS, and Tailwind CSS based on Figma design specifications.</p>
        </div>
        <div class="flex items-start gap-3 bg-purple-500/5 p-4 rounded-2xl border border-purple-500/10">
          <span class="text-[#8b5cf6] font-bold text-base mt-0.5">✦</span>
          <p>Integrated RESTful APIs and optimized frontend performance, reducing page load time by 25% while improving overall user experience.</p>
        </div>
      </div>
    </div>
  </div>


  <!-- Dedicated Script for Diego Sevilla Timeline Horizontal Pin & Traveler Dot -->
  <script>
    function openDutyModal(modalId) {
      const modal = document.getElementById(modalId);
      if (modal) {
        modal.classList.remove('opacity-0', 'pointer-events-none');
        modal.classList.add('opacity-100', 'pointer-events-auto');
        const card = modal.querySelector('div');
        if (card) {
          card.classList.remove('scale-95');
          card.classList.add('scale-100');
        }
      }
    }

    function closeDutyModal(modalId) {
      const modal = document.getElementById(modalId);
      if (modal) {
        modal.classList.remove('opacity-100', 'pointer-events-auto');
        modal.classList.add('opacity-0', 'pointer-events-none');
        const card = modal.querySelector('div');
        if (card) {
          card.classList.remove('scale-100');
          card.classList.add('scale-95');
        }
      }
    }

    document.addEventListener('DOMContentLoaded', () => {
      document.querySelectorAll('.duty-modal').forEach(modal => {
        modal.addEventListener('click', (e) => {
          if (e.target === modal) closeDutyModal(modal.id);
        });
      });
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
          document.querySelectorAll('.duty-modal').forEach(modal => closeDutyModal(modal.id));
        }
      });

      // GSAP ScrollTrigger Setup
      const setupDiegoTimeline = () => {
        if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') {
          setTimeout(setupDiegoTimeline, 150);
          return;
        }

        const section = document.getElementById('timeline-pin-section');
        const track = document.getElementById('timeline-scroll-content');
        const watermark = document.getElementById('timeline-year-watermark');
        const circuitPath = document.getElementById('ds-circuit-main-path');
        const travelerDot = document.getElementById('ds-traveler-dot');

        if (!section || !track) return;

        let getScrollAmount = () => -(track.scrollWidth - window.innerWidth + 160);

        // Pin Timeline Section during scroll
        const pinTimeline = gsap.to(track, {
          x: getScrollAmount,
          ease: "none",
          scrollTrigger: {
            trigger: section,
            start: "top top",
            end: () => "+=" + (track.scrollWidth - window.innerWidth + 600),
            pin: true,
            scrub: 1,
            invalidateOnRefresh: true,
            onUpdate: (self) => {
              // Move watermark slower for parallax effect
              if (watermark) {
                gsap.set(watermark, { x: -self.progress * 350 });
              }

              // Animate traveler dot along SVG path
              if (circuitPath && travelerDot) {
                const totalLen = circuitPath.getTotalLength();
                const point = circuitPath.getPointAtLength(self.progress * totalLen);
                travelerDot.setAttribute('cx', point.x);
                travelerDot.setAttribute('cy', point.y);
              }
            }
          }
        });

        // Path Drawing Progress
        if (circuitPath) {
          const pathLength = circuitPath.getTotalLength();
          circuitPath.style.strokeDasharray = pathLength;
          circuitPath.style.strokeDashoffset = pathLength;

          gsap.to(circuitPath, {
            strokeDashoffset: 0,
            ease: "none",
            scrollTrigger: {
              trigger: section,
              start: "top top",
              end: () => "+=" + (track.scrollWidth - window.innerWidth + 600),
              scrub: 1
            }
          });
        }
      };

      setupDiegoTimeline();
    });
  </script>
</section>'''

updated_text = text[:sec_start] + diego_sevilla_section + text[sec_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(updated_text)

print("Successfully replaced timeline section with exact Diego Sevilla design!")
