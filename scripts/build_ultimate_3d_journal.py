import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# -------------------------------------------------------------
# ULTIMATE PHYSICAL 3D BOOK ENGINE MATCHING EXACT IMAGES 1, 2, & 3
# -------------------------------------------------------------
ULTIMATE_3D_JOURNAL_HTML = """<!-- ABOUT ME: ULTIMATE PHYSICAL 3D BOOK (MATCHING MOCKUPS 1, 2 & 3) -->
<section class="relative bg-[#f4efe6] text-[#1F1F1F] py-24 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">
  <div class="max-w-7xl mx-auto px-4 md:px-8 text-center">
    
    <!-- Title Header -->
    <div class="mb-10">
      <span class="text-[11px] uppercase tracking-[0.3em] text-[#8b2252] font-mono font-bold block mb-1">ABOUT ME</span>
      <h2 class="text-4xl md:text-5xl font-bold font-serif italic text-[#1F1F1F]">The Personal Journal</h2>
    </div>

    <style>
      .book-viewport {
        perspective: 2000px;
      }
      .book-wrapper {
        position: relative;
        transform-style: preserve-3d;
        transition: transform 0.8s cubic-bezier(0.4, 0.2, 0.2, 1);
      }
      /* Cover Flip Leaf */
      .cover-leaf {
        position: absolute;
        inset: 0;
        transform-origin: left center;
        transform-style: preserve-3d;
        transition: transform 0.9s cubic-bezier(0.645, 0.045, 0.355, 1);
        z-index: 50;
      }
      .cover-leaf.open {
        transform: rotateY(-180deg);
      }
      /* Page Leaf Flip */
      .page-turn-leaf {
        position: absolute;
        top: 0; right: 0; bottom: 0; width: 50%;
        transform-origin: left center;
        transform-style: preserve-3d;
        transition: transform 0.8s cubic-bezier(0.645, 0.045, 0.355, 1);
        z-index: 40;
      }
      .page-turn-leaf.flipped {
        transform: rotateY(-180deg);
      }
      .backface-hidden {
        backface-visibility: hidden;
        -webkit-backface-visibility: hidden;
      }
    </style>

    <!-- PHYSICAL 3D BOOK CONTAINER -->
    <div class="book-viewport relative w-full max-w-[1020px] mx-auto min-h-[640px] flex items-center justify-center">

      <!-- ==================== CLOSED BOOK COVER STATE ==================== -->
      <div id="physical-book-cover" class="cursor-pointer transition-all duration-500 z-50 group" onclick="openBook3D()">
        <div class="relative">
          <!-- Hardcover Book (Stable, Zero Shaking) -->
          <div class="w-[330px] md:w-[430px] h-[550px] rounded-[30px] shadow-[0_30px_70px_-15px_rgba(0,0,0,0.35)] overflow-hidden relative bg-[#36132b] border border-amber-900/30">
            <img src="cover.png" alt="Shakthi Sri Journal Cover" class="w-full h-full object-cover block"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/30 via-transparent to-transparent pointer-events-none"></div>
          </div>
          <!-- Spine Ribbon Bookmark -->
          <div class="w-6 h-12 bg-[#8b2252] rounded-b-md shadow-md absolute -bottom-5 left-10 pointer-events-none"></div>
        </div>
      </div>

      <!-- ==================== OPENED PHYSICAL 3D BOOK ==================== -->
      <div id="physical-book-opened" class="hidden w-full transition-opacity duration-500 opacity-0 z-40">
        
        <!-- SPREAD 1: PAGES 01 & 02 (MATCHING IMAGE 1 EXACTLY) -->
        <div id="spread-pages-1-2" class="w-full bg-[#faf6ee] rounded-[32px] shadow-[0_30px_80px_-20px_rgba(0,0,0,0.22)] border-4 border-[#36132b] p-6 md:p-10 relative overflow-hidden text-left" style="background-image: radial-gradient(#d6cebe 1px, transparent 1px); background-size: 20px 20px;">
          
          <!-- TOP-RIGHT CLOSE BUTTON '✕' (MATCHING IMAGE 1) -->
          <button onclick="closeBook3D()" class="absolute top-5 right-6 text-gray-500 hover:text-[#8b2252] text-xl font-bold z-50 p-1 transition-colors" title="Close Journal">
            ✕
          </button>

          <!-- SIDE TAB INDEX (RIGHT MARGIN - MATCHING IMAGE 3) -->
          <div class="absolute top-16 -right-1 flex flex-col gap-2 z-50 hidden md:flex">
            <button onclick="switchSpread('spread1')" class="px-2.5 py-3 bg-[#421835] text-white text-[10px] font-mono font-bold rounded-l-lg shadow-md border-l border-t border-b border-amber-900/30 writing-mode-vertical uppercase">
              P. 01-02
            </button>
            <button onclick="switchSpread('spread2')" class="px-2.5 py-3 bg-[#ebdcc4] hover:bg-[#421835] text-gray-800 hover:text-white text-[10px] font-mono font-bold rounded-l-lg shadow-md border-l border-t border-b border-amber-900/30 writing-mode-vertical uppercase transition-colors">
              P. 03-04
            </button>
          </div>

          <!-- Center Spine Shadow -->
          <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[2px] bg-amber-900/15 hidden md:block"></div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 relative z-10 pt-1">
            
            <!-- PAGE 01: LEFT SIDE (MATCHING IMAGE 1 EXACTLY) -->
            <div class="flex flex-col justify-between text-left pr-0 md:pr-4">
              <div>
                <h3 class="text-4xl md:text-5xl font-bold font-serif text-[#1F1F1F] mb-3 tracking-tight">Shakthi Sri</h3>
                
                <!-- Pill Badges -->
                <div class="flex flex-wrap items-center gap-3 mb-6">
                  <span class="px-3.5 py-1 bg-[#f0e3db] text-[#8b2252] text-[11px] font-mono font-bold rounded-full border border-[#d8c2b5] tracking-wider uppercase">DEVELOPER &amp; RESEARCHER</span>
                  <span class="font-serif italic text-sm text-gray-600 underline decoration-amber-900/30">class of 2026</span>
                </div>

                <!-- Achievements List with Official SVG Logos -->
                <div class="space-y-3 font-mono text-xs text-gray-700 font-medium mb-6">
                  <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-2">
                    <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                      <svg class="w-4 h-4 text-[#8b2252]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/></svg>
                      B.Tech Information Technology
                    </span>
                    <span class="text-gray-500">2022 - 2026</span>
                  </div>

                  <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-2">
                    <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                      <svg class="w-4 h-4 text-[#8b2252]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5m0 0h4m-4 0v-4m0 0h4m-4 0V9m4 4v4"/></svg>
                      Kingston Engineering College
                    </span>
                    <span class="text-[#8b2252] font-bold">CGPA: 8.6</span>
                  </div>

                  <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-2">
                    <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                      <svg class="w-4 h-4 text-[#8b2252]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L5.6 15.12a2 2 0 00-1.182.17l-1.04.52a2 2 0 00-.778 2.766l1.54 2.31a2 2 0 002.324.793l2.45-.817a6 6 0 013.79 0l2.45.817a2 2 0 002.324-.793l1.54-2.31a2 2 0 00-.592-2.738z"/></svg>
                      IIT Madras — CYSTAR
                    </span>
                    <span class="text-gray-500">Research Intern</span>
                  </div>

                  <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-2">
                    <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                      <svg class="w-4 h-4 text-[#8b2252]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/></svg>
                      Full-Stack Developer
                    </span>
                    <span class="text-gray-500">MERN Stack</span>
                  </div>

                  <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-2">
                    <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                      <svg class="w-4 h-4 text-[#8b2252]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                      Cybersecurity Enthusiast
                    </span>
                    <span class="text-gray-500">Always Learning</span>
                  </div>
                </div>

                <!-- Taped Cards Row -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6">
                  <div class="bg-[#f7f0e6] p-4 rounded-2xl border border-amber-900/15 shadow-sm relative">
                    <div class="absolute -top-3 left-1/2 -translate-x-1/2 w-10 h-4 bg-amber-200/80 rotate-[-2deg] border-l border-r border-white/60"></div>
                    <span class="font-serif italic text-xs text-[#8b2252] font-bold block mb-2">about me</span>
                    <ul class="text-[11px] text-gray-700 leading-relaxed font-sans space-y-1.5">
                      <li>• I love turning ideas into impactful digital solutions.</li>
                      <li>• Curious mind with a strong drive to build, secure &amp; innovate.</li>
                      <li>• Believer in discipline, consistency &amp; growth.</li>
                    </ul>
                  </div>

                  <div class="bg-[#f7f0e6] p-4 rounded-2xl border border-amber-900/15 shadow-sm relative">
                    <div class="flex items-center gap-1 mb-2">
                      <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                      <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                      <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                      <span class="text-[9px] font-mono text-gray-400 ml-1 uppercase">TODAY</span>
                    </div>
                    <p class="text-[11px] text-gray-700 font-sans leading-relaxed">
                      Building skills.<br/>Solving problems.<br/>Creating solutions.<br/>Preparing for impact.<br/>One step at a time.
                    </p>
                  </div>
                </div>
              </div>

              <!-- Contact Memo & Quote -->
              <div class="pt-4 border-t border-dashed border-amber-900/20 flex flex-col sm:flex-row justify-between items-start sm:items-end gap-3">
                <div class="bg-[#f0e8dc] p-3 rounded-xl text-[11px] font-mono text-gray-800 border border-amber-900/15">
                  <p class="font-bold">srishakthi799@gmail.com</p>
                  <p class="text-gray-600">+91 7895032098</p>
                  <p class="text-gray-500">Chennai | Vellore</p>
                </div>
                <div class="text-right">
                  <span class="text-2xl text-[#8b2252] font-serif leading-none block">“</span>
                  <p class="font-serif italic text-xs text-[#421835] font-semibold">code with purpose,<br/>create with impact.</p>
                </div>
              </div>

            </div>

            <!-- PAGE 02: RIGHT SIDE (MATCHING IMAGE 1 EXACTLY) -->
            <div class="flex flex-col justify-between relative text-left pl-0 md:pl-2">
              
              <!-- Top Row -->
              <div class="flex justify-between items-start mb-4">
                <div class="text-center">
                  <svg class="w-6 h-6 text-[#8b2252] mx-auto" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2a10 10 0 100 20 10 10 0 000-20zm0 18a8 8 0 110-16 8 8 0 010 16z"/></svg>
                  <span class="block text-[9px] font-mono text-gray-500 mt-1">breathe</span>
                </div>
                <div class="flex items-center gap-6">
                  <div class="text-center">
                    <div class="w-8 h-8 bg-[#8b2252]/10 rounded-lg flex items-center justify-center text-[#8b2252] text-sm font-bold mx-auto">
                      <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M2 6a2 2 0 012-2h5l2 2h5a2 2 0 012 2v6a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"/></svg>
                    </div>
                    <span class="block text-[9px] font-mono text-gray-500 mt-1">Goals</span>
                  </div>
                  <div class="text-center">
                    <div class="w-8 h-8 bg-amber-900/10 rounded-lg flex items-center justify-center text-amber-900 text-sm font-bold mx-auto">
                      <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M3 4a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-1 1H4a1 1 0 01-1-1V4zm0 6a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-1 1H4a1 1 0 01-1-1v-2zm0 6a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-1 1H4a1 1 0 01-1-1v-2z" clip-rule="evenodd"/></svg>
                    </div>
                    <span class="block text-[9px] font-mono text-gray-500 mt-1">Reminders</span>
                  </div>
                </div>
              </div>

              <!-- Photo & Currently Box -->
              <div class="grid grid-cols-1 sm:grid-cols-12 gap-6 items-center mb-6">
                <!-- Currently Box -->
                <div class="sm:col-span-6 border border-dashed border-amber-900/30 rounded-2xl p-4 bg-[#fbf7f0]">
                  <span class="font-serif italic text-xs text-[#8b2252] font-bold block mb-2">currently</span>
                  <ul class="text-[11px] text-gray-700 leading-relaxed font-sans space-y-1.5">
                    <li>• Exploring AI &amp; LLMs</li>
                    <li>• Building secure systems</li>
                    <li>• Deepening full-stack</li>
                    <li>• Learning. Shipping.</li>
                    <li>• Growing. Always.</li>
                  </ul>
                </div>

                <!-- Centered Photo -->
                <div class="sm:col-span-6 flex justify-center relative">
                  <div class="relative">
                    <div class="w-[170px] h-[210px] rounded-[22px] overflow-hidden shadow-xl border-4 border-white">
                      <img src="me.png" alt="Shakthi Sri" class="w-full h-full object-cover"/>
                    </div>
                    <div class="absolute -top-3 right-0 bg-black/80 text-white font-mono text-[9px] font-bold px-3 py-1 rounded-full shadow-md z-30">
                      @Shakthi.16
                    </div>
                  </div>
                </div>
              </div>

              <!-- Tech I Work With Box (BRAND LOGOS ONLY) -->
              <div class="border border-dashed border-amber-900/30 rounded-2xl p-4 bg-[#fbf7f0] mb-6">
                <span class="font-serif italic text-xs text-[#8b2252] font-bold block mb-3">tech i work with</span>
                <div class="flex flex-wrap items-center justify-between gap-3 text-center">
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-800 font-bold">
                    <svg class="w-4 h-4 text-[#61dafb]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 9a3 3 0 100 6 3 3 0 000-6zm0-7c-5.52 0-10 1.79-10 4s4.48 4 10 4 10-1.79 10-4-4.48-4-10-4zm0 6c-4.41 0-8-1.34-8-2s3.59-2 8-2 8 1.34 8 2-3.59 2-8 2z"/></svg>
                    React.js
                  </div>
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-800 font-bold">
                    <svg class="w-4 h-4 text-[#339933]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2L2 7.5v9L12 22l10-5.5v-9L12 2zm0 2.3l7.5 4.1-7.5 4.1-7.5-4.1L12 4.3z"/></svg>
                    Node.js
                  </div>
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-800 font-bold">
                    <svg class="w-4 h-4 text-gray-700" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0L1 6v12l11 6 11-6V6L12 0zm9 17.2l-9 4.9-9-4.9V6.8l9-4.9 9 4.9v10.4z"/></svg>
                    Express.js
                  </div>
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-800 font-bold">
                    <svg class="w-4 h-4 text-[#47A248]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 1.5C11.5 3 7 7.5 7 13c0 3 2 5.5 5 6.5 3-1 5-3.5 5-6.5 0-5.5-4.5-10-5-11.5z"/></svg>
                    MongoDB
                  </div>
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-800 font-bold">
                    <svg class="w-4 h-4 text-[#F24E1E]" fill="currentColor" viewBox="0 0 24 24"><path d="M8 2h4v4H8V2zm0 6h4v4H8V8zm0 6h4v4a4 4 0 11-4-4zm8-12h4v4h-4V2zm0 6h4v4h-4V8z"/></svg>
                    Figma
                  </div>
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-800 font-bold">
                    <svg class="w-4 h-4 text-[#007ACC]" fill="currentColor" viewBox="0 0 24 24"><path d="M23.15 2.587L18.21.21a1.494 1.494 0 00-1.705.291L7.548 8.69 3.4 5.564a.747.747 0 00-.986.079L.24 7.728a.747.747 0 00-.03.996l3.96 4.67-3.96 4.67a.747.747 0 00.03.996l2.174 2.085a.747.747 0 00.986.079l4.148-3.126 8.957 8.189c.498.455 1.25.412 1.705-.098l4.94-4.757a1.494 1.494 0 00.44-1.077V3.664c0-.406-.164-.796-.44-1.077z"/></svg>
                    VS Code
                  </div>
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-800 font-bold">
                    <svg class="w-4 h-4 text-black" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C9.5 2 7.5 4 7.5 6.5v4c0 1.5-1 3-2.5 4 0 3 3 5.5 7 5.5s7-2.5 7-5.5c-1.5-1-2.5-2.5-2.5-4v-4C16.5 4 14.5 2 12 2z"/></svg>
                    Linux
                  </div>
                </div>
              </div>

              <!-- What I Build Box -->
              <div class="border border-dashed border-amber-900/30 rounded-2xl p-4 bg-[#fbf7f0]">
                <span class="font-serif italic text-xs text-[#8b2252] font-bold block mb-2 text-center">what i build</span>
                <div class="grid grid-cols-3 gap-2 text-center text-[10px] font-mono text-gray-700 font-bold">
                  <div class="p-2 bg-white/80 rounded-xl border border-amber-900/10 flex items-center justify-center gap-1">🌐 Full-Stack Web Apps</div>
                  <div class="p-2 bg-white/80 rounded-xl border border-amber-900/10 flex items-center justify-center gap-1">🔒 Cybersecurity Tools</div>
                  <div class="p-2 bg-white/80 rounded-xl border border-amber-900/10 flex items-center justify-center gap-1">🧠 AI Solutions</div>
                </div>
              </div>

            </div>

          </div>

          <!-- Bottom Nav -->
          <div class="mt-6 pt-3 border-t border-amber-900/10 flex justify-between items-center text-xs font-mono text-gray-500">
            <button onclick="closeBook3D()" class="hover:text-[#8b2252] font-bold cursor-pointer">← Cover</button>
            <span class="font-bold text-gray-400">Page 01-02 of 04</span>
            <button onclick="switchSpread('spread2')" class="hover:text-[#8b2252] font-bold cursor-pointer">Page 03-04 ➔</button>
          </div>

        </div>

        <!-- SPREAD 2: PAGES 03 & 04 (MATCHING IMAGE 3 EXACTLY) -->
        <div id="spread-pages-3-4" class="hidden w-full bg-[#faf6ee] rounded-[32px] shadow-[0_30px_80px_-20px_rgba(0,0,0,0.22)] border-4 border-[#36132b] p-6 md:p-10 relative overflow-hidden text-left" style="background-image: radial-gradient(#d6cebe 1px, transparent 1px); background-size: 20px 20px;">
          
          <!-- TOP-RIGHT CLOSE BUTTON '✕' (MATCHING IMAGE 3) -->
          <button onclick="closeBook3D()" class="absolute top-5 right-6 text-gray-500 hover:text-[#8b2252] text-xl font-bold z-50 p-1 transition-colors" title="Close Journal">
            ✕
          </button>

          <!-- SIDE TAB INDEX (RIGHT MARGIN - MATCHING IMAGE 3 EXACTLY) -->
          <div class="absolute top-16 -right-1 flex flex-col gap-2 z-50 hidden md:flex">
            <button onclick="switchSpread('spread1')" class="px-2.5 py-3 bg-[#ebdcc4] hover:bg-[#421835] text-gray-800 hover:text-white text-[10px] font-mono font-bold rounded-l-lg shadow-md border-l border-t border-b border-amber-900/30 writing-mode-vertical uppercase transition-colors">
              P. 01-02
            </button>
            <button onclick="switchSpread('spread2')" class="px-2.5 py-3 bg-[#421835] text-white text-[10px] font-mono font-bold rounded-l-lg shadow-md border-l border-t border-b border-amber-900/30 writing-mode-vertical uppercase">
              Engineering Notes
            </button>
          </div>

          <!-- Center Spine -->
          <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[2px] bg-amber-900/15 hidden md:block"></div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 relative z-10 pt-1">
            
            <!-- PAGE 03: FIELD NOTES (MATCHING IMAGE 3 UI EXACTLY) -->
            <div class="space-y-4 text-left">
              <div class="flex items-center justify-between">
                <div>
                  <div class="flex items-center gap-2">
                    <span class="px-2 py-0.5 bg-[#f0e3db] text-[#8b2252] font-mono font-bold text-[10px] rounded border border-amber-900/20">03</span>
                    <h3 class="text-2xl font-bold font-serif text-[#1F1F1F]">FIELD NOTES</h3>
                  </div>
                  <p class="text-xs text-gray-500 font-medium italic mt-0.5">observations. learnings. growth. ♡</p>
                </div>
                <!-- Taped Quote Card (Top Right) -->
                <div class="hidden sm:block max-w-[170px] bg-[#f7f0e6] p-2.5 rounded-xl border border-amber-900/15 text-[9px] font-serif italic text-gray-700 relative">
                  <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-8 h-3 bg-amber-200/80 rotate-[-1deg]"></div>
                  "The best code is the code that is easy to change, understand and trust." ♡
                </div>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-12 gap-4">
                
                <!-- Left Column: 4 Entry Cards -->
                <div class="sm:col-span-7 space-y-2.5">
                  
                  <div class="p-3 rounded-xl bg-white/90 border border-amber-900/10 space-y-1">
                    <h4 class="font-bold text-xs text-[#421835]">01 Understand First</h4>
                    <p class="text-[10px] text-gray-600 leading-relaxed">Before writing code, I invest time in truly understanding the problem, the users, the context and constraints. Clarity before coding saves time, energy and confusion.</p>
                  </div>

                  <div class="p-3 rounded-xl bg-white/90 border border-amber-900/10 space-y-1">
                    <h4 class="font-bold text-xs text-[#421835]">02 Simplicity is Engineered</h4>
                    <p class="text-[10px] text-gray-600 leading-relaxed">Simplicity doesn't happen by chance. It is the result of removing the unnecessary and keeping only what truly matters. Simple solutions create the most powerful impact.</p>
                  </div>

                  <div class="p-3 rounded-xl bg-white/90 border border-amber-900/10 space-y-1">
                    <h4 class="font-bold text-xs text-[#421835]">03 Secure by Design</h4>
                    <p class="text-[10px] text-gray-600 leading-relaxed">Security is not a checklist at the end. It is an architecture decision made every step of the way. Trust is built in the design, not added later.</p>
                  </div>

                  <div class="p-3 rounded-xl bg-white/90 border border-amber-900/10 space-y-1">
                    <h4 class="font-bold text-xs text-[#421835]">04 Iterate Relentlessly</h4>
                    <p class="text-[10px] text-gray-600 leading-relaxed">Nothing is perfect in the first version. Iteration, feedback and improvement transform ideas into solutions that last and scale.</p>
                  </div>

                </div>

                <!-- Right Column: Engineering Flow Chart (Matching Image 3) -->
                <div class="sm:col-span-5 flex flex-col justify-between space-y-3">
                  <div class="bg-[#f7f0e6] p-3 rounded-2xl border border-amber-900/15 text-center">
                    <span class="text-[9px] font-mono font-bold uppercase tracking-wider text-[#8b2252] block mb-2">ENGINEERING FLOW</span>
                    <div class="space-y-1 text-[10px] font-mono font-bold text-gray-700">
                      <div class="p-1 bg-white rounded-lg border border-amber-900/10">👁️ Observe</div>
                      <div class="text-[9px] text-gray-400">↓</div>
                      <div class="p-1 bg-white rounded-lg border border-amber-900/10">❓ Question</div>
                      <div class="text-[9px] text-gray-400">↓</div>
                      <div class="p-1 bg-white rounded-lg border border-amber-900/10">💡 Understand</div>
                      <div class="text-[9px] text-gray-400">↓</div>
                      <div class="p-1 bg-white rounded-lg border border-amber-900/10">✏️ Design</div>
                      <div class="text-[9px] text-gray-400">↓</div>
                      <div class="p-1 bg-white rounded-lg border border-amber-900/10">&lt;/&gt; Build</div>
                      <div class="text-[9px] text-gray-400">↓</div>
                      <div class="p-1 bg-white rounded-lg border border-amber-900/10">✔️ Test</div>
                      <div class="text-[9px] text-gray-400">↓</div>
                      <div class="p-1 bg-white rounded-lg border border-amber-900/10">🚀 Improve</div>
                    </div>
                  </div>

                  <div class="bg-amber-100/60 p-2.5 rounded-xl text-[9px] font-mono text-gray-700 italic border border-amber-900/15 text-center">
                    "Simplicity is the ultimate sophistication."
                  </div>
                </div>

              </div>

              <!-- Taped Bottom Quote Card -->
              <div class="p-3 bg-[#f7f0e6] rounded-xl border border-amber-900/15 text-[10px] font-serif italic text-gray-700 text-center">
                “Every project teaches something. Every mistake documents something. Every revision improves something.” ♡
              </div>

            </div>

            <!-- PAGE 04: ENGINEERING PRINCIPLES (MATCHING IMAGE 3 UI EXACTLY) -->
            <div class="space-y-4 text-left">
              <div class="flex items-center justify-between">
                <div>
                  <div class="flex items-center gap-2">
                    <span class="px-2 py-0.5 bg-[#f0e3db] text-[#8b2252] font-mono font-bold text-[10px] rounded border border-amber-900/20">04</span>
                    <h3 class="text-2xl font-bold font-serif text-[#1F1F1F]">ENGINEERING PRINCIPLES</h3>
                  </div>
                  <p class="text-xs text-gray-500 font-medium italic mt-0.5">Ideas that guide every decision I make. ♡</p>
                </div>
                <!-- Profile Tag -->
                <div class="flex items-center gap-2">
                  <div class="w-8 h-8 rounded-full overflow-hidden border-2 border-white shadow">
                    <img src="me.png" alt="Shakthi Sri" class="w-full h-full object-cover"/>
                  </div>
                  <span class="text-[9px] font-mono font-bold text-gray-600">@Shakthi.16</span>
                </div>
              </div>

              <!-- 6 Principle Cards Grid -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-[10px] text-gray-700">
                
                <div class="p-2.5 rounded-xl bg-white/90 border border-amber-900/10 space-y-1">
                  <h4 class="font-bold text-[#421835]">01 Purpose Over Features</h4>
                  <p class="text-gray-600 leading-relaxed">Build features that solve meaningful problems. A product with purpose creates value that lasts.</p>
                </div>

                <div class="p-2.5 rounded-xl bg-white/90 border border-amber-900/10 space-y-1">
                  <h4 class="font-bold text-[#421835]">02 Continuous Learning</h4>
                  <p class="text-gray-600 leading-relaxed">Technology evolves every day. A curious mind that keeps learning will always stay relevant.</p>
                </div>

                <div class="p-2.5 rounded-xl bg-white/90 border border-amber-900/10 space-y-1">
                  <h4 class="font-bold text-[#421835]">03 Humans First</h4>
                  <p class="text-gray-600 leading-relaxed">Behind every interface is a person with emotions, goals and challenges. Design with empathy.</p>
                </div>

                <div class="p-2.5 rounded-xl bg-white/90 border border-amber-900/10 space-y-1">
                  <h4 class="font-bold text-[#421835]">04 Document to Empower</h4>
                  <p class="text-gray-600 leading-relaxed">Good documentation empowers collaboration, preserves knowledge and future-proofs the product.</p>
                </div>

                <div class="p-2.5 rounded-xl bg-white/90 border border-amber-900/10 space-y-1">
                  <h4 class="font-bold text-[#421835]">05 Quality Over Speed</h4>
                  <p class="text-gray-600 leading-relaxed">Speed impresses in the short term. Quality builds trust in the long run. I choose quality, always.</p>
                </div>

                <div class="p-2.5 rounded-xl bg-white/90 border border-amber-900/10 space-y-1">
                  <h4 class="font-bold text-[#421835]">06 Ethics &amp; Responsibility</h4>
                  <p class="text-gray-600 leading-relaxed">As engineers, our code can impact lives. I choose to build responsibly, respect privacy and do right.</p>
                </div>

              </div>

              <!-- Note to Self Box (Matching Image 3) -->
              <div class="p-3 bg-[#f7f0e6] rounded-2xl border border-amber-900/15">
                <span class="text-[9px] font-mono font-bold uppercase text-[#8b2252] block mb-1.5 text-center">NOTE TO SELF</span>
                <div class="grid grid-cols-2 gap-2 text-[10px] font-mono text-gray-700">
                  <div>• Stay curious.<br/>• Stay consistent.<br/>• Stay humble.</div>
                  <div>• Build meaningful things.<br/>• Help others grow.<br/>• Never stop improving.</div>
                </div>
              </div>

              <div class="pt-2 border-t border-dashed border-amber-900/20 flex justify-between items-center text-[10px] font-serif italic text-gray-600">
                <span>Code with purpose, create with impact. ☆</span>
                <span class="font-bold text-[#8b2252]">Principles endure.</span>
              </div>

            </div>

          </div>

          <!-- Bottom Nav -->
          <div class="mt-6 pt-3 border-t border-amber-900/10 flex justify-between items-center text-xs font-mono text-gray-500">
            <button onclick="switchSpread('spread1')" class="hover:text-[#8b2252] font-bold cursor-pointer">← Page 01-02</button>
            <span class="font-bold text-gray-400">Page 03-04 of 04</span>
            <button onclick="closeBook3D()" class="hover:text-[#8b2252] font-bold cursor-pointer">Close Book ➔</button>
          </div>

        </div>

      </div>

    </div>

  </div>
</section>

<!-- Smooth Physical 3D Book Flip Engine Script -->
<script>
  function openBook3D() {
    const coverView = document.getElementById('physical-book-cover');
    const openedView = document.getElementById('physical-book-opened');
    const spread1 = document.getElementById('spread-pages-1-2');
    const spread2 = document.getElementById('spread-pages-3-4');

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

  function closeBook3D() {
    const coverView = document.getElementById('physical-book-cover');
    const openedView = document.getElementById('physical-book-opened');

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

  function switchSpread(targetId) {
    const spread1 = document.getElementById('spread-pages-1-2');
    const spread2 = document.getElementById('spread-pages-3-4');

    let curSpread, nextSpread;
    if (targetId === 'spread2') {
      curSpread = spread1;
      nextSpread = spread2;
    } else {
      curSpread = spread2;
      nextSpread = spread1;
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

end_pos = content.find('<!-- ==================== 2. EDITORIAL CANVAS (#about) ==================== -->')
if end_pos == -1:
    end_pos = content.find('id="about"')
    end_pos = content.rfind('<section', 0, end_pos)

if start_pos != -1 and end_pos != -1:
    content = content[:start_pos] + ULTIMATE_3D_JOURNAL_HTML + '\n\n' + content[end_pos:]
    print("Successfully replaced with Ultimate 3D Physical Book matching mockups 1, 2, and 3!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
