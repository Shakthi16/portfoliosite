import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '<section class="relative bg-[#FAFAFA] text-[#1F1F1F] overflow-hidden py-24 border-t border-b border-gray-200/60" id="timeline-pin-section">'
end_marker = '</section>'

start_pos = text.find(start_marker)
if start_pos == -1:
    print("Could not find start marker!")
    exit(1)

end_pos = text.find(end_marker, start_pos) + len(end_marker)

new_section_html = '''<section class="relative bg-gradient-to-b from-[#F4F8FF] via-[#EEF5FF] to-[#F8FAFC] text-[#1F1F1F] overflow-hidden py-16 border-t border-b border-blue-100" id="timeline-pin-section" style="min-height: 100vh;">

  <!-- Subtle Circuit Grid Background Pattern -->
  <div class="absolute inset-0 pointer-events-none opacity-[0.03] z-0" style="background-image: radial-gradient(#0066FF 1.5px, transparent 1.5px); background-size: 32px 32px;"></div>
  
  <!-- Header Title (Diego Sevilla Awwwards Style) -->
  <div class="max-w-7xl mx-auto px-6 mb-8 relative z-20 flex flex-col md:flex-row justify-between items-start md:items-end">
    <div>
      <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-blue-50/90 border border-blue-200/80 text-[#0066FF] font-mono text-[11px] font-bold tracking-widest uppercase mb-3 shadow-sm">
        <span class="w-2 h-2 rounded-full bg-[#0066FF] animate-pulse"></span>
        WORK EXPERIENCES
      </div>
      <h2 class="text-4xl md:text-6xl font-extrabold font-sans tracking-tight text-[#0F172A] flex items-center gap-3">
        Work Experiences
      </h2>
    </div>
    <div class="mt-4 md:mt-0 flex items-center gap-3 text-xs md:text-sm text-slate-500 font-medium bg-white/70 backdrop-blur-md px-4 py-2 rounded-full border border-blue-100 shadow-sm">
      <span>Scroll vertically to explore timeline</span>
      <svg class="w-4 h-4 text-[#0066FF] animate-bounce" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
    </div>
  </div>

  <!-- Horizontal Scroll Pin Wrapper -->
  <div class="relative w-full overflow-hidden" id="timeline-scroll-wrapper" style="min-height: 580px;">

    <!-- Background Digits Watermark -->
    <div class="absolute inset-0 pointer-events-none flex items-center justify-between opacity-[0.04] select-none z-0 px-12" style="font-family: 'Outfit', sans-serif; font-size: 260px; font-weight: 900; color: #0066FF; letter-spacing: -0.05em;">
      <span>2025</span>
      <span>2026</span>
    </div>

    <!-- Connected Circuit SVG Path Line (Diego Sevilla Signature Style) -->
    <svg class="absolute top-1/2 left-0 w-[2600px] h-[300px] -translate-y-1/2 pointer-events-none z-10 overflow-visible" viewBox="0 0 2600 300" fill="none">
      <defs>
        <linearGradient id="circuit-blue-grad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#0066FF" />
          <stop offset="50%" stop-color="#3B82F6" />
          <stop offset="100%" stop-color="#0066FF" />
        </linearGradient>
        <filter id="circuit-glow" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="4" result="blur" />
          <feMerge>
            <feMergeNode in="blur" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
      </defs>
      <!-- Continuous Wave Circuit Line connecting all nodes -->
      <path id="timeline-circuit-path" d="M 0 150 L 300 150 C 450 150, 480 80, 650 80 C 820 80, 950 220, 1150 220 C 1350 220, 1480 90, 1680 90 C 1880 90, 2000 150, 2600 150" stroke="url(#circuit-blue-grad)" stroke-width="4" stroke-linecap="round" filter="url(#circuit-glow)" />

      <!-- Nodes / Junction Points along Path -->
      <g transform="translate(650, 80)">
        <circle r="8" fill="#0066FF" stroke="#FFFFFF" stroke-width="3" />
        <circle r="16" fill="none" stroke="#0066FF" stroke-width="1.5" stroke-dasharray="3 3" class="animate-[spin_10s_linear_infinite]" />
      </g>

      <g transform="translate(1150, 220)">
        <circle r="8" fill="#F59E0B" stroke="#FFFFFF" stroke-width="3" />
        <circle r="16" fill="none" stroke="#F59E0B" stroke-width="1.5" stroke-dasharray="3 3" class="animate-[spin_10s_linear_infinite]" />
      </g>

      <g transform="translate(1680, 90)">
        <circle r="8" fill="#8B5CF6" stroke="#FFFFFF" stroke-width="3" />
        <circle r="16" fill="none" stroke="#8B5CF6" stroke-width="1.5" stroke-dasharray="3 3" class="animate-[spin_10s_linear_infinite]" />
      </g>
    </svg>

    <!-- Horizontal Items Container -->
    <div class="flex items-center gap-16 px-8 md:px-24 py-8 w-max relative z-20 transition-transform duration-300" id="timeline-scroll-content">

      <!-- ITEM 1: IIT Madras -- CYSTAR Lab -->
      <div class="timeline-node-card group relative flex flex-col justify-between bg-white/90 backdrop-blur-xl rounded-[32px] p-8 border border-blue-100 shadow-[0_20px_50px_-15px_rgba(0,102,255,0.08)] hover:shadow-[0_30px_70px_-15px_rgba(0,102,255,0.18)] w-[90vw] md:w-[620px] shrink-0 transition-all duration-500 hover:-translate-y-2">
        <!-- Visual Top Graphic -->
        <div class="flex items-start justify-between mb-6">
          <div class="flex items-center gap-4">
            <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center text-white shadow-lg shadow-blue-500/30">
              <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
            </div>
            <div>
              <span class="text-[11px] font-mono font-bold uppercase tracking-[0.2em] text-[#0066FF]">CYBERSECURITY RESEARCH INTERN</span>
              <h3 class="text-2xl md:text-3xl font-extrabold text-[#0F172A] leading-tight">IIT Madras — CYSTAR Lab</h3>
            </div>
          </div>
          <span class="px-3.5 py-1.5 rounded-full bg-slate-100 text-slate-600 font-mono text-[11px] font-bold shrink-0">
            Jul 2025 – May 2026
          </span>
        </div>

        <!-- Visual Media Preview Card -->
        <div class="relative w-full h-[180px] rounded-2xl overflow-hidden mb-6 group-hover:shadow-md transition-shadow">
          <img src="bg1.png" alt="IIT Madras CYSTAR Lab" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"/>
          <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-slate-950/20 to-transparent flex items-end p-4">
            <span class="text-white font-mono text-xs font-semibold flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-emerald-400"></span> EDR/AV Evasion & Exposure Analysis
            </span>
          </div>
        </div>

        <!-- Summary Paragraph -->
        <p class="text-xs md:text-sm text-slate-600 leading-relaxed font-medium mb-6">
          Conducted cybersecurity research focused on exposure analysis, EDR/AV behaviour evaluation, and secure system design under supervised research initiatives.
        </p>

        <!-- Key Duties Button (Diego Sevilla Style) -->
        <div class="flex items-center justify-between pt-4 border-t border-slate-100">
          <button onclick="openDutyModal('modal-cystar')" class="px-6 py-2.5 rounded-full bg-[#0066FF] hover:bg-blue-700 text-white font-sans text-xs font-bold tracking-wide shadow-md shadow-blue-500/20 transition-all transform hover:scale-105 flex items-center gap-2">
            <span>Key Duties</span>
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
          </button>
          <span class="text-[11px] font-mono text-slate-400">IIT Madras</span>
        </div>
      </div>


      <!-- ITEM 2: OpsIntellix -->
      <div class="timeline-node-card group relative flex flex-col justify-between bg-white/90 backdrop-blur-xl rounded-[32px] p-8 border border-amber-100 shadow-[0_20px_50px_-15px_rgba(245,158,11,0.08)] hover:shadow-[0_30px_70px_-15px_rgba(245,158,11,0.18)] w-[90vw] md:w-[620px] shrink-0 transition-all duration-500 hover:-translate-y-2 mt-8 md:mt-12">
        <!-- Visual Top Graphic -->
        <div class="flex items-start justify-between mb-6">
          <div class="flex items-center gap-4">
            <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-amber-500 to-orange-600 flex items-center justify-center text-white shadow-lg shadow-amber-500/30">
              <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
            </div>
            <div>
              <span class="text-[11px] font-mono font-bold uppercase tracking-[0.2em] text-[#D97706]">OPERATIONS INTERN — AP AUTOMATION</span>
              <h3 class="text-2xl md:text-3xl font-extrabold text-[#0F172A] leading-tight">OpsIntellix</h3>
            </div>
          </div>
          <span class="px-3.5 py-1.5 rounded-full bg-slate-100 text-slate-600 font-mono text-[11px] font-bold shrink-0">
            Nov 2025 – Feb 2026
          </span>
        </div>

        <!-- Visual Media Preview Card -->
        <div class="relative w-full h-[180px] rounded-2xl overflow-hidden mb-6 group-hover:shadow-md transition-shadow">
          <img src="opsintellix.png" alt="OpsIntellix Automation" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"/>
          <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-slate-950/20 to-transparent flex items-end p-4">
            <span class="text-white font-mono text-xs font-semibold flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-amber-400"></span> Python AP & Mortgage Automation (+30% Efficiency)
            </span>
          </div>
        </div>

        <!-- Summary Paragraph -->
        <p class="text-xs md:text-sm text-slate-600 leading-relaxed font-medium mb-6">
          Automated mortgage and banking workflows using Python, including document classification, data extraction, validation, and reporting.
        </p>

        <!-- Key Duties Button (Diego Sevilla Style) -->
        <div class="flex items-center justify-between pt-4 border-t border-slate-100">
          <button onclick="openDutyModal('modal-opsintellix')" class="px-6 py-2.5 rounded-full bg-[#F59E0B] hover:bg-amber-600 text-white font-sans text-xs font-bold tracking-wide shadow-md shadow-amber-500/20 transition-all transform hover:scale-105 flex items-center gap-2">
            <span>Key Duties</span>
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
          </button>
          <span class="text-[11px] font-mono text-slate-400">OpsIntellix</span>
        </div>
      </div>


      <!-- ITEM 3: Focuslogic IT Services -->
      <div class="timeline-node-card group relative flex flex-col justify-between bg-white/90 backdrop-blur-xl rounded-[32px] p-8 border border-purple-100 shadow-[0_20px_50px_-15px_rgba(139,92,246,0.08)] hover:shadow-[0_30px_70px_-15px_rgba(139,92,246,0.18)] w-[90vw] md:w-[620px] shrink-0 transition-all duration-500 hover:-translate-y-2">
        <!-- Visual Top Graphic -->
        <div class="flex items-start justify-between mb-6">
          <div class="flex items-center gap-4">
            <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-purple-500 to-pink-600 flex items-center justify-center text-white shadow-lg shadow-purple-500/30">
              <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path></svg>
            </div>
            <div>
              <span class="text-[11px] font-mono font-bold uppercase tracking-[0.2em] text-[#7C3AED]">WEB DEVELOPMENT INTERN</span>
              <h3 class="text-2xl md:text-3xl font-extrabold text-[#0F172A] leading-tight">Focuslogic IT Services</h3>
            </div>
          </div>
          <span class="px-3.5 py-1.5 rounded-full bg-slate-100 text-slate-600 font-mono text-[11px] font-bold shrink-0">
            Mar 2025 – May 2025
          </span>
        </div>

        <!-- Visual Media Preview Card -->
        <div class="relative w-full h-[180px] rounded-2xl overflow-hidden mb-6 group-hover:shadow-md transition-shadow">
          <img src="write.png" alt="Focuslogic IT Services" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"/>
          <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-slate-950/20 to-transparent flex items-end p-4">
            <span class="text-white font-mono text-xs font-semibold flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-purple-400"></span> React.js & REST API Frontend Optimization (-25% Load Time)
            </span>
          </div>
        </div>

        <!-- Summary Paragraph -->
        <p class="text-xs md:text-sm text-slate-600 leading-relaxed font-medium mb-6">
          Developed responsive and accessible web applications using React.js, HTML, CSS, and Tailwind CSS based on Figma design specifications.
        </p>

        <!-- Key Duties Button (Diego Sevilla Style) -->
        <div class="flex items-center justify-between pt-4 border-t border-slate-100">
          <button onclick="openDutyModal('modal-focuslogic')" class="px-6 py-2.5 rounded-full bg-[#8B5CF6] hover:bg-purple-600 text-white font-sans text-xs font-bold tracking-wide shadow-md shadow-purple-500/20 transition-all transform hover:scale-105 flex items-center gap-2">
            <span>Key Duties</span>
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
          </button>
          <span class="text-[11px] font-mono text-slate-400">Focuslogic</span>
        </div>
      </div>

    </div>
  </div>


  <!-- MODAL 1: IIT Madras CYSTAR Lab -->
  <div id="modal-cystar" class="duty-modal fixed inset-0 z-[999] flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-md opacity-0 pointer-events-none transition-all duration-300">
    <div class="relative bg-white rounded-3xl p-6 md:p-8 max-w-xl w-full border border-blue-100 shadow-2xl transform scale-95 transition-all duration-300">
      <button onclick="closeDutyModal('modal-cystar')" class="absolute top-5 right-5 w-9 h-9 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center font-bold text-lg transition-colors">✕</button>
      <div class="flex items-center gap-3 mb-4">
        <span class="w-3 h-3 rounded-full bg-[#0066FF]"></span>
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-[#0066FF]">Jul 2025 – May 2026</span>
      </div>
      <h3 class="text-2xl font-extrabold text-[#0F172A] mb-1">IIT Madras — CYSTAR Lab</h3>
      <p class="text-xs font-mono font-semibold text-slate-500 uppercase tracking-wider mb-6">Cybersecurity Research Intern</p>
      
      <div class="space-y-4 text-sm text-slate-600 leading-relaxed font-medium">
        <div class="flex items-start gap-3 bg-blue-50/50 p-3.5 rounded-xl border border-blue-100/80">
          <span class="text-[#0066FF] text-base mt-0.5">✦</span>
          <p>Conducted cybersecurity research focused on exposure analysis, EDR/AV behaviour evaluation, and secure system design under supervised research initiatives.</p>
        </div>
        <div class="flex items-start gap-3 bg-blue-50/50 p-3.5 rounded-xl border border-blue-100/80">
          <span class="text-[#0066FF] text-base mt-0.5">✦</span>
          <p>Contributed to the development of explainable security workflows, technical research documentation, and security tool evaluation for cybersecurity research projects.</p>
        </div>
        <div class="flex items-start gap-3 bg-blue-50/50 p-3.5 rounded-xl border border-blue-100/80">
          <span class="text-[#0066FF] text-base mt-0.5">✦</span>
          <p>Collaborated with research teams on threat modelling, security analysis, and confidential research activities within enterprise security environments.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL 2: OpsIntellix -->
  <div id="modal-opsintellix" class="duty-modal fixed inset-0 z-[999] flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-md opacity-0 pointer-events-none transition-all duration-300">
    <div class="relative bg-white rounded-3xl p-6 md:p-8 max-w-xl w-full border border-amber-100 shadow-2xl transform scale-95 transition-all duration-300">
      <button onclick="closeDutyModal('modal-opsintellix')" class="absolute top-5 right-5 w-9 h-9 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center font-bold text-lg transition-colors">✕</button>
      <div class="flex items-center gap-3 mb-4">
        <span class="w-3 h-3 rounded-full bg-[#F59E0B]"></span>
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-[#D97706]">Nov 2025 – Feb 2026</span>
      </div>
      <h3 class="text-2xl font-extrabold text-[#0F172A] mb-1">OpsIntellix</h3>
      <p class="text-xs font-mono font-semibold text-slate-500 uppercase tracking-wider mb-6">Operations Intern — AP Automation</p>
      
      <div class="space-y-4 text-sm text-slate-600 leading-relaxed font-medium">
        <div class="flex items-start gap-3 bg-amber-50/50 p-3.5 rounded-xl border border-amber-100/80">
          <span class="text-[#F59E0B] text-base mt-0.5">✦</span>
          <p>Automated mortgage and banking workflows using Python, including document classification, data extraction, validation, and reporting processes.</p>
        </div>
        <div class="flex items-start gap-3 bg-amber-50/50 p-3.5 rounded-xl border border-amber-100/80">
          <span class="text-[#F59E0B] text-base mt-0.5">✦</span>
          <p>Optimized business process automation pipelines, improving operational efficiency by 30% while supporting compliance-driven workflows.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL 3: Focuslogic IT Services -->
  <div id="modal-focuslogic" class="duty-modal fixed inset-0 z-[999] flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-md opacity-0 pointer-events-none transition-all duration-300">
    <div class="relative bg-white rounded-3xl p-6 md:p-8 max-w-xl w-full border border-purple-100 shadow-2xl transform scale-95 transition-all duration-300">
      <button onclick="closeDutyModal('modal-focuslogic')" class="absolute top-5 right-5 w-9 h-9 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center font-bold text-lg transition-colors">✕</button>
      <div class="flex items-center gap-3 mb-4">
        <span class="w-3 h-3 rounded-full bg-[#8B5CF6]"></span>
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-[#7C3AED]">Mar 2025 – May 2025</span>
      </div>
      <h3 class="text-2xl font-extrabold text-[#0F172A] mb-1">Focuslogic IT Services</h3>
      <p class="text-xs font-mono font-semibold text-slate-500 uppercase tracking-wider mb-6">Web Development Intern</p>
      
      <div class="space-y-4 text-sm text-slate-600 leading-relaxed font-medium">
        <div class="flex items-start gap-3 bg-purple-50/50 p-3.5 rounded-xl border border-purple-100/80">
          <span class="text-[#8B5CF6] text-base mt-0.5">✦</span>
          <p>Developed responsive and accessible web applications using React.js, HTML, CSS, and Tailwind CSS based on Figma design specifications.</p>
        </div>
        <div class="flex items-start gap-3 bg-purple-50/50 p-3.5 rounded-xl border border-purple-100/80">
          <span class="text-[#8B5CF6] text-base mt-0.5">✦</span>
          <p>Integrated RESTful APIs and optimized frontend performance, reducing page load time by 25% while improving overall user experience.</p>
        </div>
      </div>
    </div>
  </div>


  <!-- Dedicated Section Script for Pinning & Modals -->
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

    // Close on backdrop click & ESC key
    document.addEventListener('DOMContentLoaded', () => {
      document.querySelectorAll('.duty-modal').forEach(modal => {
        modal.addEventListener('click', (e) => {
          if (e.target === modal) {
            closeDutyModal(modal.id);
          }
        });
      });
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
          document.querySelectorAll('.duty-modal').forEach(modal => {
            closeDutyModal(modal.id);
          });
        }
      });

      // Initialize GSAP Horizontal Pinning for Work Experiences Section
      const initTimelinePin = () => {
        if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') {
          setTimeout(initTimelinePin, 200);
          return;
        }

        const section = document.getElementById('timeline-pin-section');
        const track = document.getElementById('timeline-scroll-content');
        if (!section || !track) return;

        let getScrollAmount = () => {
          let trackWidth = track.scrollWidth;
          return -(trackWidth - window.innerWidth + 120);
        };

        const timelineTween = gsap.to(track, {
          x: getScrollAmount,
          ease: "none",
          scrollTrigger: {
            trigger: section,
            start: "top top",
            end: () => "+=" + (track.scrollWidth - window.innerWidth + 400),
            pin: true,
            scrub: 1,
            invalidateOnRefresh: true
          }
        });

        // Dynamic Circuit Path line animation as scroll occurs
        const path = document.getElementById('timeline-circuit-path');
        if (path) {
          const pathLength = path.getTotalLength();
          path.style.strokeDasharray = pathLength;
          path.style.strokeDashoffset = pathLength;

          gsap.to(path, {
            strokeDashoffset: 0,
            ease: "none",
            scrollTrigger: {
              trigger: section,
              start: "top top",
              end: () => "+=" + (track.scrollWidth - window.innerWidth + 400),
              scrub: 1
            }
          });
        }
      };

      initTimelinePin();
    });
  </script>
</section>'''

updated_text = text[:start_pos] + new_section_html + text[end_pos:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(updated_text)

print("Successfully replaced section timeline-pin-section in index.html!")
