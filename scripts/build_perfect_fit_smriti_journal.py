import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# -------------------------------------------------------------
# SMRITI RAWAT JOURNAL SPECIFICATION:
# 1. PERFECT VIEWPORT FIT (COVER & OPENED SPREAD 100% MATCHING HEIGHT)
# 2. ZERO OVERFLOW ON LAPTOP SCREENS (MAX-HEIGHT 560px)
# 3. TORN PAPER LAYER SEPARATION DIVIDER (MATCHING IMAGE 3)
# 4. OUTSIDE LEATHER TABS & 100% BRAND LOGOS
# -------------------------------------------------------------
PERFECT_FIT_JOURNAL_HTML = """<!-- ABOUT ME: PHYSICAL SMRITI RAWAT STYLE JOURNAL BOOK (PERFECT VIEWPORT FIT + TORN PAPER DIVIDER) -->
<!-- TORN PAPER TOP LAYER DIVIDER (MATCHING IMAGE 3) -->
<div class="w-full bg-[#faf7f2] relative z-20 pointer-events-none -mb-1">
  <svg class="w-full h-8 md:h-12 text-[#f4efe6] fill-current" viewBox="0 0 1200 120" preserveAspectRatio="none">
    <path d="M0,0 C90,40 180,10 270,30 C360,50 450,20 540,40 C630,60 720,15 810,35 C900,55 990,20 1080,45 C1140,55 1170,25 1200,30 L1200,120 L0,120 Z"></path>
  </svg>
</div>

<section class="relative bg-[#f4efe6] text-[#1F1F1F] py-10 md:py-14 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">
  <div class="max-w-7xl mx-auto px-4 md:px-8 text-center">
    
    <!-- Section Title Header (Compact) -->
    <div class="mb-6">
      <span class="text-[11px] uppercase tracking-[0.3em] text-[#8b2252] font-mono font-bold block mb-1">ABOUT ME</span>
      <h2 class="text-3xl md:text-5xl font-bold font-serif italic text-[#1F1F1F]">The Personal Journal</h2>
    </div>

    <!-- BOOK STAGE CONTAINER (CONSTRAINED CONTAINER, ZERO SCREEN OVERFLOW) -->
    <div class="relative w-full max-w-[1000px] mx-auto min-h-[540px] md:min-h-[570px] flex items-center justify-center">

      <!-- ==================== CLOSED BOOK COVER STATE ==================== -->
      <div id="smriti-book-cover" class="cursor-pointer transition-all duration-500 z-40 group" onclick="openSmritiBook()">
        <div class="relative">
          <!-- Cover Book Image (EXACT HEIGHT MATCHING OPENED BOOK: 540px) -->
          <div class="w-[310px] md:w-[410px] h-[520px] md:h-[550px] rounded-[30px] shadow-[0_30px_70px_-15px_rgba(0,0,0,0.35)] overflow-hidden relative bg-[#36132b] border border-amber-900/30">
            <img src="cover.png" alt="Shakthi Sri Journal Cover" class="w-full h-full object-cover block"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/25 via-transparent to-transparent pointer-events-none"></div>
          </div>
          <!-- Spine Bookmark Ribbon -->
          <div class="w-6 h-12 bg-[#8b2252] rounded-b-md shadow-md absolute -bottom-5 left-10 pointer-events-none"></div>
        </div>
      </div>

      <!-- ==================== OPENED PHYSICAL HARDCOVER BOOK ==================== -->
      <div id="smriti-book-opened" class="hidden w-full transition-opacity duration-500 opacity-0 z-30">
        
        <!-- HARDCOVER FRAME (BURGUNDY #36132b FULLY ENCLOSING PAGES WITH 16px BORDER) -->
        <div class="relative w-full bg-[#36132b] rounded-[34px] p-3 md:p-4 shadow-[0_30px_75px_-15px_rgba(0,0,0,0.38)] border border-amber-900/40">
          
          <!-- OUTSIDE RIGHT VERTICAL INDEX TABS (STICKING OUT BEYOND THE HARDCOVER) -->
          <div class="absolute top-8 -right-9 md:-right-11 flex flex-col gap-2 z-50">
            
            <!-- Home / Cover Tab -->
            <button onclick="closeSmritiBook()" class="w-9 md:w-11 h-10 bg-[#ebdcc4] hover:bg-[#8b2252] text-gray-800 hover:text-white rounded-r-xl shadow-lg border-t border-r border-b border-amber-900/20 flex items-center justify-center transition-all hover:translate-x-1" title="Close to Cover">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"/></svg>
            </button>

            <!-- Tab 1: Engineering Notes (P. 01-02) -->
            <button id="tab-btn-spread1" onclick="switchSmritiSpread('spread1')" class="px-2 md:px-2.5 py-3.5 bg-[#421835] text-white text-[10px] font-mono font-bold rounded-r-xl shadow-lg border-t border-r border-b border-amber-900/30 flex items-center justify-center transition-all hover:translate-x-1" style="writing-mode: vertical-rl; text-orientation: mixed;">
              Engineering Notes
            </button>

            <!-- Tab 2: Philosophy (P. 03-04) -->
            <button id="tab-btn-spread2" onclick="switchSmritiSpread('spread2')" class="px-2 md:px-2.5 py-3.5 bg-[#9b6b78] hover:bg-[#421835] text-white text-[10px] font-mono font-bold rounded-r-xl shadow-lg border-t border-r border-b border-amber-900/30 flex items-center justify-center transition-all hover:translate-x-1" style="writing-mode: vertical-rl; text-orientation: mixed;">
              Philosophy
            </button>

            <!-- Tab 3: Lessons -->
            <button onclick="switchSmritiSpread('spread2')" class="px-2 md:px-2.5 py-3 bg-[#c2a297] text-white text-[10px] font-mono font-bold rounded-r-xl shadow-lg border-t border-r border-b border-amber-900/30 flex items-center justify-center transition-all hover:translate-x-1 hidden sm:flex" style="writing-mode: vertical-rl; text-orientation: mixed;">
              Lessons
            </button>

            <!-- Tab 4: Vision -->
            <button onclick="switchSmritiSpread('spread2')" class="px-2 md:px-2.5 py-2.5 bg-[#dfcfc7] text-gray-800 text-[10px] font-mono font-bold rounded-r-xl shadow-lg border-t border-r border-b border-amber-900/30 flex items-center justify-center transition-all hover:translate-x-1 hidden sm:flex" style="writing-mode: vertical-rl; text-orientation: mixed;">
              Vision
            </button>

            <!-- Bottom Bookmark Icon -->
            <div class="w-9 md:w-11 h-8 bg-[#55826b] text-white rounded-r-xl shadow-lg flex items-center justify-center">
              <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path d="M5 4a2 2 0 012-2h6a2 2 0 012 2v14l-5-2.5L5 18V4z"/></svg>
            </div>

          </div>

          <!-- INNER PAGES SPREAD 1 (PAGES 01 & 02 - CONSTRAINED HEIGHT TO FIT SCREEN) -->
          <div id="smriti-spread-1" class="w-full bg-[#faf6ee] rounded-[24px] p-5 md:p-7 relative overflow-hidden text-left h-[500px] md:h-[520px] flex flex-col justify-between" style="background-image: radial-gradient(#d6cebe 1px, transparent 1px); background-size: 20px 20px;">
            
            <!-- TOP-RIGHT CLOSE BUTTON '✕' -->
            <button onclick="closeSmritiBook()" class="absolute top-3 right-4 text-gray-400 hover:text-[#8b2252] text-lg font-bold z-40 p-1 transition-colors" title="Close Journal">
              ✕
            </button>

            <!-- Center Spine Line -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[2px] bg-amber-900/15 hidden md:block"></div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-10 relative z-10 h-full overflow-y-auto md:overflow-hidden">
              
              <!-- PAGE 01: LEFT SIDE (MATCHING IMAGE 2 EXACTLY) -->
              <div class="flex flex-col justify-between text-left pr-0 md:pr-2">
                <div>
                  <h3 class="text-3xl md:text-4xl font-bold font-serif text-[#1F1F1F] mb-2 tracking-tight">Shakthi Sri</h3>
                  
                  <!-- Pill Badges -->
                  <div class="flex flex-wrap items-center gap-2 mb-4">
                    <span class="px-3 py-0.5 bg-[#f0e3db] text-[#8b2252] text-[10px] font-mono font-bold rounded-full border border-[#d8c2b5] tracking-wider uppercase">DEVELOPER &amp; RESEARCHER</span>
                    <span class="font-serif italic text-xs text-gray-600 underline decoration-amber-900/30">class of 2026</span>
                  </div>

                  <!-- Achievements List with Official SVG Brand Logos -->
                  <div class="space-y-2 font-mono text-[11px] text-gray-700 font-medium mb-4">
                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-1.5">
                      <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                        <svg class="w-3.5 h-3.5 text-[#8b2252]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/></svg>
                        B.Tech Information Technology
                      </span>
                      <span class="text-gray-500">2022 - 2026</span>
                    </div>

                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-1.5">
                      <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                        <svg class="w-3.5 h-3.5 text-[#8b2252]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5m0 0h4m-4 0v-4m0 0h4m-4 0V9m4 4v4"/></svg>
                        Kingston Engineering College
                      </span>
                      <span class="text-[#8b2252] font-bold">CGPA: 8.6</span>
                    </div>

                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-1.5">
                      <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                        <svg class="w-3.5 h-3.5 text-[#8b2252]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L5.6 15.12a2 2 0 00-1.182.17l-1.04.52a2 2 0 00-.778 2.766l1.54 2.31a2 2 0 002.324.793l2.45-.817a6 6 0 013.79 0l2.45.817a2 2 0 002.324-.793l1.54-2.31a2 2 0 00-.592-2.738z"/></svg>
                        IIT Madras — CYSTAR
                      </span>
                      <span class="text-gray-500">Research Intern</span>
                    </div>

                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-1.5">
                      <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                        <svg class="w-3.5 h-3.5 text-[#8b2252]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/></svg>
                        Full-Stack Developer
                      </span>
                      <span class="text-gray-500">MERN Stack</span>
                    </div>

                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-1.5">
                      <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                        <svg class="w-3.5 h-3.5 text-[#8b2252]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                        Cybersecurity Enthusiast
                      </span>
                      <span class="text-gray-500">Always Learning</span>
                    </div>
                  </div>

                  <!-- Taped Cards Row -->
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-3">
                    <div class="bg-[#f7f0e6] p-3 rounded-2xl border border-amber-900/15 shadow-sm relative">
                      <div class="absolute -top-2.5 left-1/2 -translate-x-1/2 w-8 h-3.5 bg-amber-200/80 rotate-[-2deg] border-l border-r border-white/60"></div>
                      <span class="font-serif italic text-[11px] text-[#8b2252] font-bold block mb-1">about me</span>
                      <ul class="text-[10px] text-gray-700 leading-relaxed font-sans space-y-1">
                        <li>• I love turning ideas into digital solutions.</li>
                        <li>• Curious mind driving build &amp; security.</li>
                        <li>• Believer in discipline &amp; growth.</li>
                      </ul>
                    </div>

                    <div class="bg-[#f7f0e6] p-3 rounded-2xl border border-amber-900/15 shadow-sm relative">
                      <div class="flex items-center gap-1 mb-1">
                        <span class="w-1.5 h-1.5 rounded-full bg-rose-400"></span>
                        <span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                        <span class="text-[9px] font-mono text-gray-400 ml-1 uppercase">TODAY</span>
                      </div>
                      <p class="text-[10px] text-gray-700 font-sans leading-relaxed">
                        Building skills. Solving problems.<br/>Creating solutions. One step at a time.
                      </p>
                    </div>
                  </div>
                </div>

                <!-- Contact Memo & Quote -->
                <div class="pt-2 border-t border-dashed border-amber-900/20 flex justify-between items-center gap-2">
                  <div class="bg-[#f0e8dc] px-2.5 py-1.5 rounded-xl text-[10px] font-mono text-gray-800 border border-amber-900/15">
                    <p class="font-bold">srishakthi799@gmail.com</p>
                    <p class="text-gray-500">Chennai | Vellore</p>
                  </div>
                  <div class="text-right">
                    <p class="font-serif italic text-[11px] text-[#421835] font-semibold">code with purpose,<br/>create with impact.</p>
                  </div>
                </div>

              </div>

              <!-- PAGE 02: RIGHT SIDE -->
              <div class="flex flex-col justify-between relative text-left pl-0 md:pl-2">
                
                <!-- Top Row -->
                <div class="flex justify-between items-start mb-3">
                  <div class="text-center">
                    <svg class="w-5 h-5 text-[#8b2252] mx-auto" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2a10 10 0 100 20 10 10 0 000-20zm0 18a8 8 0 110-16 8 8 0 010 16z"/></svg>
                    <span class="block text-[8px] font-mono text-gray-500 mt-0.5">breathe</span>
                  </div>
                  <div class="flex items-center gap-4">
                    <div class="text-center">
                      <div class="w-7 h-7 bg-[#8b2252]/10 rounded-lg flex items-center justify-center text-[#8b2252] text-xs font-bold mx-auto">
                        <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path d="M2 6a2 2 0 012-2h5l2 2h5a2 2 0 012 2v6a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"/></svg>
                      </div>
                      <span class="block text-[8px] font-mono text-gray-500 mt-0.5">Goals</span>
                    </div>
                    <div class="text-center">
                      <div class="w-7 h-7 bg-amber-900/10 rounded-lg flex items-center justify-center text-amber-900 text-xs font-bold mx-auto">
                        <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M3 4a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-1 1H4a1 1 0 01-1-1V4zm0 6a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-1 1H4a1 1 0 01-1-1v-2zm0 6a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-1 1H4a1 1 0 01-1-1v-2z" clip-rule="evenodd"/></svg>
                      </div>
                      <span class="block text-[8px] font-mono text-gray-500 mt-0.5">Reminders</span>
                    </div>
                  </div>
                </div>

                <!-- Photo & Currently Box -->
                <div class="grid grid-cols-1 sm:grid-cols-12 gap-4 items-center mb-4">
                  <div class="sm:col-span-6 border border-dashed border-amber-900/30 rounded-2xl p-3 bg-[#fbf7f0]">
                    <span class="font-serif italic text-xs text-[#8b2252] font-bold block mb-1.5">currently</span>
                    <ul class="text-[10px] text-gray-700 leading-relaxed font-sans space-y-1">
                      <li>• Exploring AI &amp; LLMs</li>
                      <li>• Building secure systems</li>
                      <li>• Deepening full-stack</li>
                      <li>• Learning. Shipping. Always.</li>
                    </ul>
                  </div>

                  <div class="sm:col-span-6 flex justify-center relative">
                    <div class="relative">
                      <div class="w-[140px] md:w-[160px] h-[170px] md:h-[190px] rounded-[20px] overflow-hidden shadow-md border-4 border-white">
                        <img src="me.png" alt="Shakthi Sri" class="w-full h-full object-cover"/>
                      </div>
                      <div class="absolute -top-2.5 right-0 bg-black/80 text-white font-mono text-[8px] font-bold px-2.5 py-0.5 rounded-full shadow-md z-30">
                        @Shakthi.16
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Tech I Work With Box -->
                <div class="border border-dashed border-amber-900/30 rounded-2xl p-3 bg-[#fbf7f0] mb-4">
                  <span class="font-serif italic text-[11px] text-[#8b2252] font-bold block mb-2">tech i work with</span>
                  <div class="flex flex-wrap items-center justify-between gap-2 text-center">
                    <div class="flex items-center gap-1 text-[10px] font-mono text-gray-800 font-bold">
                      <svg class="w-3.5 h-3.5 text-[#61dafb]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 9a3 3 0 100 6 3 3 0 000-6zm0-7c-5.52 0-10 1.79-10 4s4.48 4 10 4 10-1.79 10-4-4.48-4-10-4zm0 6c-4.41 0-8-1.34-8-2s3.59-2 8-2 8 1.34 8 2-3.59 2-8 2z"/></svg>
                      React.js
                    </div>
                    <div class="flex items-center gap-1 text-[10px] font-mono text-gray-800 font-bold">
                      <svg class="w-3.5 h-3.5 text-[#339933]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2L2 7.5v9L12 22l10-5.5v-9L12 2zm0 2.3l7.5 4.1-7.5 4.1-7.5-4.1L12 4.3z"/></svg>
                      Node.js
                    </div>
                    <div class="flex items-center gap-1 text-[10px] font-mono text-gray-800 font-bold">
                      <svg class="w-3.5 h-3.5 text-gray-700" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0L1 6v12l11 6 11-6V6L12 0zm9 17.2l-9 4.9-9-4.9V6.8l9-4.9 9 4.9v10.4z"/></svg>
                      Express.js
                    </div>
                    <div class="flex items-center gap-1 text-[10px] font-mono text-gray-800 font-bold">
                      <svg class="w-3.5 h-3.5 text-[#47A248]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 1.5C11.5 3 7 7.5 7 13c0 3 2 5.5 5 6.5 3-1 5-3.5 5-6.5 0-5.5-4.5-10-5-11.5z"/></svg>
                      MongoDB
                    </div>
                    <div class="flex items-center gap-1 text-[10px] font-mono text-gray-800 font-bold">
                      <svg class="w-3.5 h-3.5 text-[#F24E1E]" fill="currentColor" viewBox="0 0 24 24"><path d="M8 2h4v4H8V2zm0 6h4v4H8V8zm0 6h4v4a4 4 0 11-4-4zm8-12h4v4h-4V2zm0 6h4v4h-4V8z"/></svg>
                      Figma
                    </div>
                    <div class="flex items-center gap-1 text-[10px] font-mono text-gray-800 font-bold">
                      <svg class="w-3.5 h-3.5 text-[#007ACC]" fill="currentColor" viewBox="0 0 24 24"><path d="M23.15 2.587L18.21.21a1.494 1.494 0 00-1.705.291L7.548 8.69 3.4 5.564a.747.747 0 00-.986.079L.24 7.728a.747.747 0 00-.03.996l3.96 4.67-3.96 4.67a.747.747 0 00.03.996l2.174 2.085a.747.747 0 00.986.079l4.148-3.126 8.957 8.189c.498.455 1.25.412 1.705-.098l4.94-4.757a1.494 1.494 0 00.44-1.077V3.664c0-.406-.164-.796-.44-1.077z"/></svg>
                      VS Code
                    </div>
                    <div class="flex items-center gap-1 text-[10px] font-mono text-gray-800 font-bold">
                      <svg class="w-3.5 h-3.5 text-black" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C9.5 2 7.5 4 7.5 6.5v4c0 1.5-1 3-2.5 4 0 3 3 5.5 7 5.5s7-2.5 7-5.5c-1.5-1-2.5-2.5-2.5-4v-4C16.5 4 14.5 2 12 2z"/></svg>
                      Linux
                    </div>
                  </div>
                </div>

                <!-- What I Build Box -->
                <div class="border border-dashed border-amber-900/30 rounded-2xl p-3 bg-[#fbf7f0]">
                  <span class="font-serif italic text-[10px] text-[#8b2252] font-bold block mb-1 text-center">what i build</span>
                  <div class="grid grid-cols-3 gap-1.5 text-center text-[9px] font-mono text-gray-700 font-bold">
                    <div class="p-1.5 bg-white/80 rounded-lg border border-amber-900/10 flex items-center justify-center gap-1">🌐 Full-Stack</div>
                    <div class="p-1.5 bg-white/80 rounded-lg border border-amber-900/10 flex items-center justify-center gap-1">🔒 Cybersecurity</div>
                    <div class="p-1.5 bg-white/80 rounded-lg border border-amber-900/10 flex items-center justify-center gap-1">🧠 AI Solutions</div>
                  </div>
                </div>

              </div>

            </div>

          </div>

          <!-- INNER PAGES SPREAD 2 (PAGES 03 & 04) -->
          <div id="smriti-spread-2" class="hidden w-full bg-[#faf6ee] rounded-[24px] p-5 md:p-7 relative overflow-hidden text-left h-[500px] md:h-[520px] flex flex-col justify-between" style="background-image: radial-gradient(#d6cebe 1px, transparent 1px); background-size: 20px 20px;">
            
            <!-- TOP-RIGHT CLOSE BUTTON '✕' -->
            <button onclick="closeSmritiBook()" class="absolute top-3 right-4 text-gray-400 hover:text-[#8b2252] text-lg font-bold z-40 p-1 transition-colors" title="Close Journal">
              ✕
            </button>

            <!-- Center Spine Line -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[2px] bg-amber-900/15 hidden md:block"></div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-10 relative z-10 h-full overflow-y-auto md:overflow-hidden">
              
              <!-- PAGE 03: FIELD NOTES -->
              <div class="space-y-3 text-left">
                <div class="flex items-center justify-between">
                  <div>
                    <div class="flex items-center gap-1.5">
                      <span class="px-1.5 py-0.5 bg-[#f0e3db] text-[#8b2252] font-mono font-bold text-[9px] rounded border border-amber-900/20">03</span>
                      <h3 class="text-xl md:text-2xl font-bold font-serif text-[#1F1F1F]">FIELD NOTES</h3>
                    </div>
                    <p class="text-[10px] text-gray-500 font-medium italic">observations. learnings. growth. ♡</p>
                  </div>
                  <!-- Taped Quote Card -->
                  <div class="hidden sm:block max-w-[150px] bg-[#f7f0e6] p-2 rounded-xl border border-amber-900/15 text-[8px] font-serif italic text-gray-700 relative">
                    <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-6 h-2.5 bg-amber-200/80 rotate-[-1deg]"></div>
                    "The best code is easy to change and trust." ♡
                  </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-12 gap-3">
                  
                  <!-- Left Column: 4 Entry Cards -->
                  <div class="sm:col-span-7 space-y-2">
                    <div class="p-2 rounded-xl bg-white/90 border border-amber-900/10 space-y-0.5">
                      <h4 class="font-bold text-[11px] text-[#421835]">01 Understand First</h4>
                      <p class="text-[9px] text-gray-600 leading-relaxed">Before coding, I invest time in understanding problem &amp; constraints. Clarity saves time.</p>
                    </div>

                    <div class="p-2 rounded-xl bg-white/90 border border-amber-900/10 space-y-0.5">
                      <h4 class="font-bold text-[11px] text-[#421835]">02 Simplicity is Engineered</h4>
                      <p class="text-[9px] text-gray-600 leading-relaxed">Simplicity comes from removing unnecessary steps. Simple solutions create impact.</p>
                    </div>

                    <div class="p-2 rounded-xl bg-white/90 border border-amber-900/10 space-y-0.5">
                      <h4 class="font-bold text-[11px] text-[#421835]">03 Secure by Design</h4>
                      <p class="text-[9px] text-gray-600 leading-relaxed">Security is an architecture decision. Trust is built in the design.</p>
                    </div>

                    <div class="p-2 rounded-xl bg-white/90 border border-amber-900/10 space-y-0.5">
                      <h4 class="font-bold text-[11px] text-[#421835]">04 Iterate Relentlessly</h4>
                      <p class="text-[9px] text-gray-600 leading-relaxed">Iteration and feedback transform ideas into reliable, scalable solutions.</p>
                    </div>
                  </div>

                  <!-- Right Column: Engineering Flow Chart -->
                  <div class="sm:col-span-5 flex flex-col justify-between space-y-2">
                    <div class="bg-[#f7f0e6] p-2 rounded-2xl border border-amber-900/15 text-center">
                      <span class="text-[8px] font-mono font-bold uppercase tracking-wider text-[#8b2252] block mb-1">ENGINEERING FLOW</span>
                      <div class="space-y-0.5 text-[9px] font-mono font-bold text-gray-700">
                        <div class="p-0.5 bg-white rounded border border-amber-900/10">👁️ Observe</div>
                        <div class="p-0.5 bg-white rounded border border-amber-900/10">❓ Question</div>
                        <div class="p-0.5 bg-white rounded border border-amber-900/10">💡 Understand</div>
                        <div class="p-0.5 bg-white rounded border border-amber-900/10">✏️ Design</div>
                        <div class="p-0.5 bg-white rounded border border-amber-900/10">&lt;/&gt; Build</div>
                        <div class="p-0.5 bg-white rounded border border-amber-900/10">✔️ Test &amp; Improve</div>
                      </div>
                    </div>

                    <div class="bg-amber-100/60 p-2 rounded-xl text-[8px] font-mono text-gray-700 italic border border-amber-900/15 text-center">
                      "Simplicity is sophistication."
                    </div>
                  </div>

                </div>

                <!-- Taped Bottom Quote Card -->
                <div class="p-2 bg-[#f7f0e6] rounded-xl border border-amber-900/15 text-[9px] font-serif italic text-gray-700 text-center">
                  “Every project teaches something. Every mistake documents something.” ♡
                </div>

              </div>

              <!-- PAGE 04: ENGINEERING PRINCIPLES -->
              <div class="space-y-3 text-left">
                <div class="flex items-center justify-between">
                  <div>
                    <div class="flex items-center gap-1.5">
                      <span class="px-1.5 py-0.5 bg-[#f0e3db] text-[#8b2252] font-mono font-bold text-[9px] rounded border border-amber-900/20">04</span>
                      <h3 class="text-xl md:text-2xl font-bold font-serif text-[#1F1F1F]">ENGINEERING PRINCIPLES</h3>
                    </div>
                    <p class="text-[10px] text-gray-500 font-medium italic">Ideas that guide every decision I make. ♡</p>
                  </div>
                  <!-- Profile Tag -->
                  <div class="flex items-center gap-1.5">
                    <div class="w-6 h-6 rounded-full overflow-hidden border border-white shadow">
                      <img src="me.png" alt="Shakthi Sri" class="w-full h-full object-cover"/>
                    </div>
                    <span class="text-[8px] font-mono font-bold text-gray-600">@Shakthi.16</span>
                  </div>
                </div>

                <!-- 6 Principle Cards Grid -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-[9px] text-gray-700">
                  <div class="p-2 rounded-xl bg-white/90 border border-amber-900/10">
                    <h4 class="font-bold text-[#421835]">01 Purpose Over Features</h4>
                    <p class="text-gray-600 leading-tight">Solve meaningful problems.</p>
                  </div>
                  <div class="p-2 rounded-xl bg-white/90 border border-amber-900/10">
                    <h4 class="font-bold text-[#421835]">02 Continuous Learning</h4>
                    <p class="text-gray-600 leading-tight">Adapt and grow daily.</p>
                  </div>
                  <div class="p-2 rounded-xl bg-white/90 border border-amber-900/10">
                    <h4 class="font-bold text-[#421835]">03 Humans First</h4>
                    <p class="text-gray-600 leading-tight">Design with empathy.</p>
                  </div>
                  <div class="p-2 rounded-xl bg-white/90 border border-amber-900/10">
                    <h4 class="font-bold text-[#421835]">04 Document to Empower</h4>
                    <p class="text-gray-600 leading-tight">Preserve knowledge.</p>
                  </div>
                  <div class="p-2 rounded-xl bg-white/90 border border-amber-900/10">
                    <h4 class="font-bold text-[#421835]">05 Quality Over Speed</h4>
                    <p class="text-gray-600 leading-tight">Quality builds long trust.</p>
                  </div>
                  <div class="p-2 rounded-xl bg-white/90 border border-amber-900/10">
                    <h4 class="font-bold text-[#421835]">06 Ethics &amp; Responsibility</h4>
                    <p class="text-gray-600 leading-tight">Build responsibly.</p>
                  </div>
                </div>

                <!-- Note to Self Box -->
                <div class="p-2.5 bg-[#f7f0e6] rounded-2xl border border-amber-900/15">
                  <span class="text-[8px] font-mono font-bold uppercase text-[#8b2252] block mb-1 text-center">NOTE TO SELF</span>
                  <div class="grid grid-cols-2 gap-2 text-[9px] font-mono text-gray-700">
                    <div>• Stay curious &amp; consistent.</div>
                    <div>• Build meaningful things.</div>
                  </div>
                </div>

                <div class="pt-1.5 border-t border-dashed border-amber-900/20 flex justify-between items-center text-[9px] font-serif italic text-gray-600">
                  <span>Code with purpose, create with impact. ☆</span>
                  <span class="font-bold text-[#8b2252]">Principles endure.</span>
                </div>

              </div>

            </div>

          </div>

        </div>

      </div>

    </div>

  </div>
</section>

<!-- TORN PAPER BOTTOM LAYER DIVIDER (MATCHING IMAGE 3) -->
<div class="w-full bg-[#f4efe6] relative z-20 pointer-events-none -mt-1 border-t border-amber-900/10">
  <svg class="w-full h-8 md:h-12 text-[#faf7f2] fill-current" viewBox="0 0 1200 120" preserveAspectRatio="none">
    <path d="M0,30 C150,10 300,50 450,20 C600,60 750,15 900,45 C1050,15 1120,40 1200,20 L1200,0 L0,0 Z"></path>
  </svg>
</div>

<!-- Smooth Physical Journal Open/Close & Spread Switch Script -->
<script>
  function openSmritiBook() {
    const coverView = document.getElementById('smriti-book-cover');
    const openedView = document.getElementById('smriti-book-opened');
    const spread1 = document.getElementById('smriti-spread-1');
    const spread2 = document.getElementById('smriti-spread-2');

    if (coverView && openedView) {
      coverView.style.transition = 'transform 0.8s cubic-bezier(0.645, 0.045, 0.355, 1), opacity 0.5s ease';
      coverView.style.transform = 'rotateY(-90deg) scale(0.95)';
      coverView.style.opacity = '0';

      setTimeout(() => {
        coverView.classList.add('hidden');
        openedView.classList.remove('hidden');
        if (spread1) spread1.classList.remove('hidden');
        if (spread2) spread2.classList.add('hidden');

        openedView.style.opacity = '0';
        openedView.style.transform = 'scale(0.96)';

        setTimeout(() => {
          openedView.style.transition = 'all 0.6s ease';
          openedView.style.opacity = '1';
          openedView.style.transform = 'scale(1)';
        }, 40);
      }, 400);
    }
  }

  function closeSmritiBook() {
    const coverView = document.getElementById('smriti-book-cover');
    const openedView = document.getElementById('smriti-book-opened');

    if (coverView && openedView) {
      openedView.style.transition = 'all 0.5s ease';
      openedView.style.opacity = '0';
      openedView.style.transform = 'scale(0.96)';

      setTimeout(() => {
        openedView.classList.add('hidden');
        coverView.classList.remove('hidden');
        
        coverView.style.transform = 'rotateY(-90deg) scale(0.95)';
        coverView.style.opacity = '0';

        setTimeout(() => {
          coverView.style.transition = 'transform 0.8s cubic-bezier(0.645, 0.045, 0.355, 1), opacity 0.5s ease';
          coverView.style.transform = 'rotateY(0deg) scale(1)';
          coverView.style.opacity = '1';
        }, 40);
      }, 400);
    }
  }

  function switchSmritiSpread(targetId) {
    const spread1 = document.getElementById('smriti-spread-1');
    const spread2 = document.getElementById('smriti-spread-2');
    const btn1 = document.getElementById('tab-btn-spread1');
    const btn2 = document.getElementById('tab-btn-spread2');

    let curSpread, nextSpread;
    if (targetId === 'spread2') {
      curSpread = spread1;
      nextSpread = spread2;
      if (btn1) { btn1.classList.remove('bg-[#421835]'); btn1.classList.add('bg-[#9b6b78]'); }
      if (btn2) { btn2.classList.remove('bg-[#9b6b78]'); btn2.classList.add('bg-[#421835]'); }
    } else {
      curSpread = spread2;
      nextSpread = spread1;
      if (btn2) { btn2.classList.remove('bg-[#421835]'); btn2.classList.add('bg-[#9b6b78]'); }
      if (btn1) { btn1.classList.remove('bg-[#421835]'); btn1.classList.add('bg-[#421835]'); }
    }

    if (curSpread && nextSpread) {
      curSpread.style.transition = 'all 0.4s ease';
      curSpread.style.opacity = '0';
      curSpread.style.transform = 'rotateY(-15deg)';

      setTimeout(() => {
        curSpread.classList.add('hidden');
        curSpread.style.opacity = '';
        curSpread.style.transform = '';

        nextSpread.classList.remove('hidden');
        nextSpread.style.opacity = '0';
        nextSpread.style.transform = 'rotateY(15deg)';

        setTimeout(() => {
          nextSpread.style.transition = 'all 0.5s ease';
          nextSpread.style.opacity = '1';
          nextSpread.style.transform = 'rotateY(0deg)';
        }, 40);
      }, 350);
    }
  }
</script>
"""

# Replace #about-journal section in index.html
start_pos = content.find('<!-- ABOUT ME:', content.find('id="about-journal"'))
if start_pos == -1:
    start_pos = content.find('id="about-journal"')
    start_pos = content.rfind('<section', 0, start_pos)
    if start_pos == -1:
        start_pos = content.find('<section class="relative bg-[#f4efe6]"')

# Check for top divider comment if previously added
top_div_idx = content.rfind('<!-- ABOUT ME: PHYSICAL SMRITI RAWAT STYLE JOURNAL BOOK', 0, start_pos)
if top_div_idx != -1 and start_pos - top_div_idx < 300:
    start_pos = top_div_idx

end_pos = content.find('<!-- ==================== 2. EDITORIAL CANVAS (#about) ==================== -->')
if end_pos == -1:
    end_pos = content.find('id="about"')
    end_pos = content.rfind('<section', 0, end_pos)

if start_pos != -1 and end_pos != -1:
    content = content[:start_pos] + PERFECT_FIT_JOURNAL_HTML + '\n\n' + content[end_pos:]
    print("Successfully updated with perfect viewport fit & deckle-edge torn paper dividers!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
