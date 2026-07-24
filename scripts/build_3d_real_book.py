import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# -------------------------------------------------------------
# REALISTIC 3D PHYSICAL BOOK FLIP ENGINE WITH BRAND LOGOS
# ZERO EMOJIS, ZERO SHAKING, REALISTIC BOOK OPEN & PAGE TURN
# -------------------------------------------------------------
REALISTIC_BOOK_HTML = """<!-- ABOUT ME: REALISTIC 3D PHYSICAL BOOK (BRAND LOGOS, NO SHAKING, REAL PAGE TURN) -->
<section class="relative bg-[#f4efe6] text-[#1F1F1F] py-24 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">
  <div class="max-w-6xl mx-auto px-4 md:px-8 text-center">
    
    <!-- Title Header -->
    <div class="mb-10">
      <span class="text-[11px] uppercase tracking-[0.3em] text-[#8b2252] font-mono font-bold block mb-1">ABOUT ME</span>
      <h2 class="text-4xl md:text-5xl font-bold font-serif italic text-[#1F1F1F]">The Personal Journal</h2>
    </div>

    <style>
      /* 3D BOOK STAGE STYLES */
      .book-stage {
        perspective: 1600px;
        perspective-origin: 50% 50%;
      }
      .book-3d {
        position: relative;
        transform-style: preserve-3d;
        transition: transform 0.8s cubic-bezier(0.645, 0.045, 0.355, 1);
      }
      .page-flip-leaf {
        position: absolute;
        top: 0; right: 0; bottom: 0; width: 50%;
        transform-origin: left center;
        transform-style: preserve-3d;
        transition: transform 0.8s cubic-bezier(0.645, 0.045, 0.355, 1);
        z-index: 30;
      }
      .page-flip-leaf.flipped {
        transform: rotateY(-180deg);
      }
      .page-face {
        position: absolute;
        inset: 0;
        backface-visibility: hidden;
        -webkit-backface-visibility: hidden;
      }
      .page-face.back {
        transform: rotateY(180deg);
      }
    </style>

    <!-- BOOK STAGE CONTAINER -->
    <div class="book-stage relative w-full max-w-[980px] mx-auto min-h-[620px] flex items-center justify-center">

      <!-- ==================== CLOSED BOOK COVER STATE ==================== -->
      <div id="book-closed-view" class="cursor-pointer transition-opacity duration-500 opacity-100 flex flex-col items-center z-40" onclick="openPhysicalBook()">
        <!-- Book Cover Container (STABLE, NO SHAKING) -->
        <div class="w-[320px] md:w-[410px] h-[530px] rounded-[28px] shadow-[0_25px_60px_-10px_rgba(0,0,0,0.25)] overflow-hidden relative bg-[#36132b] border border-amber-900/30">
          <img src="cover.png" alt="Shakthi Sri Journal Cover" class="w-full h-full object-cover block"/>
          <div class="absolute inset-0 bg-gradient-to-t from-black/30 via-transparent to-transparent pointer-events-none"></div>
        </div>
        <!-- Bookmark Ribbon -->
        <div class="w-6 h-10 bg-[#8b2252] rounded-b-md shadow-md -mt-1 pointer-events-none"></div>
      </div>

      <!-- ==================== OPENED 3D BOOK (SPREADS) ==================== -->
      <div id="book-opened-view" class="hidden w-full transition-opacity duration-500 opacity-0 z-30">
        
        <!-- SPREAD 1 (PAGES 1 & 2) -->
        <div id="spread-1" class="w-full bg-[#faf6ee] rounded-[32px] shadow-[0_30px_80px_-20px_rgba(0,0,0,0.22)] border border-amber-900/15 p-6 md:p-10 relative overflow-hidden text-left" style="background-image: radial-gradient(#d6cebe 1px, transparent 1px); background-size: 20px 20px;">
          
          <!-- CORNER PAGE FLIP TAB (TOP-RIGHT TO PAGE 3-4) -->
          <div onclick="turnToPage('spread2')" class="absolute top-0 right-0 w-16 h-16 cursor-pointer group z-50" title="Turn Page to 3-4">
            <div class="w-full h-full bg-[#ebdcc4] border-b border-l border-amber-900/20 rounded-bl-2xl shadow-md transition-transform duration-300 group-hover:scale-105 flex items-center justify-center">
              <span class="text-xs font-mono font-bold text-[#8b2252] pl-2 pb-2">p.3-4 ➔</span>
            </div>
          </div>

          <!-- CLOSE BOOK RIBBON (TOP-LEFT) -->
          <div onclick="closePhysicalBook()" class="absolute top-0 left-6 cursor-pointer group z-50" title="Close Book">
            <div class="bg-[#421835] text-white text-[10px] font-mono font-bold px-3.5 py-2.5 rounded-b-lg shadow-md transition-transform group-hover:translate-y-0.5">
              ✕ Close
            </div>
          </div>

          <!-- Center Spine -->
          <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[2px] bg-amber-900/15 hidden md:block"></div>
          <div class="absolute bottom-0 left-1/2 -translate-x-1/2 w-6 h-8 bg-[#8b2252] rounded-t-sm shadow-md hidden md:block"></div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 relative z-10 pt-2">
            
            <!-- PAGE 1: LEFT SIDE -->
            <div class="flex flex-col justify-between text-left pr-0 md:pr-4">
              <div>
                <h3 class="text-4xl md:text-5xl font-bold font-serif text-[#1F1F1F] mb-3 tracking-tight">Shakthi Sri</h3>
                
                <!-- Pill Badges -->
                <div class="flex flex-wrap items-center gap-3 mb-6">
                  <span class="px-3.5 py-1 bg-[#f0e3db] text-[#8b2252] text-[11px] font-mono font-bold rounded-full border border-[#d8c2b5] tracking-wider uppercase">DEVELOPER &amp; RESEARCHER</span>
                  <span class="font-serif italic text-sm text-gray-600 underline decoration-amber-900/30">class of 2026</span>
                </div>

                <!-- Achievements List with Official SVG/FontAwesome Brand Icons -->
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
                    <span class="text-[#8b2252] font-bold">CGPA: 9.03</span>
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

            <!-- PAGE 2: RIGHT SIDE (OFFICIAL BRAND LOGOS) -->
            <div class="flex flex-col justify-between relative text-left pl-0 md:pl-2">
              
              <!-- Top Row: Official App & Folder Logos -->
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
                  <!-- React.js Brand Logo -->
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-800 font-bold">
                    <svg class="w-4 h-4 text-[#61dafb]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 9a3 3 0 100 6 3 3 0 000-6zm0-7c-5.52 0-10 1.79-10 4s4.48 4 10 4 10-1.79 10-4-4.48-4-10-4zm0 6c-4.41 0-8-1.34-8-2s3.59-2 8-2 8 1.34 8 2-3.59 2-8 2z"/></svg>
                    React.js
                  </div>
                  <!-- Node.js Brand Logo -->
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-800 font-bold">
                    <svg class="w-4 h-4 text-[#339933]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2L2 7.5v9L12 22l10-5.5v-9L12 2zm0 2.3l7.5 4.1-7.5 4.1-7.5-4.1L12 4.3z"/></svg>
                    Node.js
                  </div>
                  <!-- Express.js Brand Logo -->
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-800 font-bold">
                    <svg class="w-4 h-4 text-gray-700" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0L1 6v12l11 6 11-6V6L12 0zm9 17.2l-9 4.9-9-4.9V6.8l9-4.9 9 4.9v10.4z"/></svg>
                    Express.js
                  </div>
                  <!-- MongoDB Brand Logo -->
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-800 font-bold">
                    <svg class="w-4 h-4 text-[#47A248]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 1.5C11.5 3 7 7.5 7 13c0 3 2 5.5 5 6.5 3-1 5-3.5 5-6.5 0-5.5-4.5-10-5-11.5z"/></svg>
                    MongoDB
                  </div>
                  <!-- Figma Brand Logo -->
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-800 font-bold">
                    <svg class="w-4 h-4 text-[#F24E1E]" fill="currentColor" viewBox="0 0 24 24"><path d="M8 2h4v4H8V2zm0 6h4v4H8V8zm0 6h4v4a4 4 0 11-4-4zm8-12h4v4h-4V2zm0 6h4v4h-4V8z"/></svg>
                    Figma
                  </div>
                  <!-- VS Code Brand Logo -->
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-800 font-bold">
                    <svg class="w-4 h-4 text-[#007ACC]" fill="currentColor" viewBox="0 0 24 24"><path d="M23.15 2.587L18.21.21a1.494 1.494 0 00-1.705.291L7.548 8.69 3.4 5.564a.747.747 0 00-.986.079L.24 7.728a.747.747 0 00-.03.996l3.96 4.67-3.96 4.67a.747.747 0 00.03.996l2.174 2.085a.747.747 0 00.986.079l4.148-3.126 8.957 8.189c.498.455 1.25.412 1.705-.098l4.94-4.757a1.494 1.494 0 00.44-1.077V3.664c0-.406-.164-.796-.44-1.077z"/></svg>
                    VS Code
                  </div>
                  <!-- Linux Brand Logo -->
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-800 font-bold">
                    <svg class="w-4 h-4 text-black" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C9.5 2 7.5 4 7.5 6.5v4c0 1.5-1 3-2.5 4 0 3 3 5.5 7 5.5s7-2.5 7-5.5c-1.5-1-2.5-2.5-2.5-4v-4C16.5 4 14.5 2 12 2z"/></svg>
                    Linux
                  </div>
                </div>
              </div>

              <!-- What I Build Box (BRAND ICONS) -->
              <div class="border border-dashed border-amber-900/30 rounded-2xl p-4 bg-[#fbf7f0]">
                <span class="font-serif italic text-xs text-[#8b2252] font-bold block mb-2 text-center">what i build</span>
                <div class="grid grid-cols-3 gap-2 text-center text-[10px] font-mono text-gray-700 font-bold">
                  <div class="p-2 bg-white/80 rounded-xl border border-amber-900/10 flex items-center justify-center gap-1">
                    <svg class="w-3.5 h-3.5 text-[#8b2252]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m6 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"/></svg>
                    Full-Stack Web Apps
                  </div>
                  <div class="p-2 bg-white/80 rounded-xl border border-amber-900/10 flex items-center justify-center gap-1">
                    <svg class="w-3.5 h-3.5 text-[#8b2252]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
                    Cybersecurity Tools
                  </div>
                  <div class="p-2 bg-white/80 rounded-xl border border-amber-900/10 flex items-center justify-center gap-1">
                    <svg class="w-3.5 h-3.5 text-[#8b2252]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/></svg>
                    AI Solutions
                  </div>
                </div>
              </div>

            </div>

          </div>

          <!-- Bottom Footer Nav -->
          <div class="mt-6 pt-3 border-t border-amber-900/10 flex justify-between items-center text-xs font-mono text-gray-500">
            <button onclick="closePhysicalBook()" class="hover:text-[#8b2252] font-bold cursor-pointer">← Cover</button>
            <span class="font-bold text-gray-400">Page 1-2 of 4</span>
            <button onclick="turnToPage('spread2')" class="hover:text-[#8b2252] font-bold cursor-pointer">Page 3-4 ➔</button>
          </div>

        </div>
      </div>

      <!-- ==================== SPREAD 2 (PAGES 3 & 4) ==================== -->
      <div id="spread-2" class="hidden w-full z-30">
        
        <div class="w-full bg-[#faf6ee] rounded-[32px] shadow-[0_30px_80px_-20px_rgba(0,0,0,0.22)] border border-amber-900/15 p-6 md:p-10 relative overflow-hidden text-left" style="background-image: radial-gradient(#d6cebe 1px, transparent 1px); background-size: 20px 20px;">
          
          <!-- CORNER FLIP BACK TAB (TOP-RIGHT TO PAGE 1-2) -->
          <div onclick="turnToPage('spread1')" class="absolute top-0 right-0 w-16 h-16 cursor-pointer group z-50" title="Back to Page 1-2">
            <div class="w-full h-full bg-[#ebdcc4] border-b border-l border-amber-900/20 rounded-bl-2xl shadow-md transition-transform duration-300 group-hover:scale-105 flex items-center justify-center">
              <span class="text-xs font-mono font-bold text-[#8b2252] pl-2 pb-2">← p.1-2</span>
            </div>
          </div>

          <!-- CLOSE BOOK RIBBON (TOP-LEFT) -->
          <div onclick="closePhysicalBook()" class="absolute top-0 left-6 cursor-pointer group z-50" title="Close Book">
            <div class="bg-[#421835] text-white text-[10px] font-mono font-bold px-3 py-2.5 rounded-b-lg shadow-md transition-transform group-hover:translate-y-0.5">
              ✕ Close
            </div>
          </div>

          <!-- Center Spine -->
          <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[2px] bg-amber-900/15 hidden md:block"></div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-10 md:gap-14 relative z-10 pt-2">
            
            <!-- PAGE 3: FIELD NOTES -->
            <div class="space-y-4 text-left">
              <div>
                <span class="text-[10px] font-mono uppercase tracking-[0.2em] text-[#8b2252] font-bold block mb-1">PAGE 3</span>
                <h3 class="text-2xl font-bold font-serif text-[#1F1F1F]">FIELD NOTES</h3>
                <p class="text-xs text-gray-500 font-medium italic">Observations collected while learning, building, and improving.</p>
              </div>

              <!-- ENTRY 01 -->
              <div class="p-3.5 rounded-2xl bg-white/80 border border-amber-900/10 space-y-1.5">
                <h4 class="font-bold text-xs text-[#421835] flex items-center gap-1.5">ENTRY 01 — Engineering Begins With Understanding</h4>
                <p class="text-[11px] text-gray-600 leading-relaxed">
                  Every project introduces uncertainty. Before selecting technologies or writing the first line of code, I spend time understanding the problem from multiple perspectives. Good engineering rarely starts with implementation—it begins with observation.
                </p>
                <p class="text-[10px] font-serif italic text-amber-900 font-semibold pt-1">I believe the strongest solutions emerge when curiosity is allowed to lead before assumptions.</p>
              </div>

              <!-- ENTRY 02 -->
              <div class="p-3.5 rounded-2xl bg-white/80 border border-amber-900/10 space-y-1.5">
                <h4 class="font-bold text-xs text-[#421835] flex items-center gap-1.5">ENTRY 02 — Simplicity Requires Discipline</h4>
                <p class="text-[11px] text-gray-600 leading-relaxed">
                  People often associate complexity with intelligence. In practice, simplicity demands significantly more thought. Removing unnecessary steps, reducing cognitive load, and making systems intuitive requires continuous refinement.
                </p>
                <div class="bg-amber-100/60 p-2 rounded-xl text-[10px] font-mono text-gray-700 italic border border-amber-900/10">
                  Notebook Margin: "Complexity is added naturally. Simplicity is engineered intentionally."
                </div>
              </div>

              <!-- ENTRY 03 & FLOW -->
              <div class="p-3.5 rounded-2xl bg-white/80 border border-amber-900/10 space-y-1.5">
                <h4 class="font-bold text-xs text-[#421835] flex items-center gap-1.5">ENTRY 03 — Security Is an Architectural Decision</h4>
                <p class="text-[11px] text-gray-600 leading-relaxed">
                  Security cannot be postponed until deployment. Authentication, authorization, validation, monitoring, and privacy should exist from the first sketch—not the final sprint.
                </p>
                <div class="text-[10px] font-mono text-gray-600 font-bold text-center py-1 bg-amber-50 rounded-lg">
                  Observe ➔ Question ➔ Understand ➔ Design ➔ Build ➔ Improve
                </div>
              </div>

              <!-- Research Note & Footer -->
              <div class="pt-2 border-t border-dashed border-amber-900/20 text-[10px] font-mono text-gray-500">
                <p class="text-amber-900 font-bold mb-1">Research Note:</p>
                <p class="italic text-gray-600">"Engineering is not about writing more code. It is about reducing unnecessary complexity while increasing reliability."</p>
                <p class="text-right font-serif italic text-[#8b2252] mt-1">"Every finished project becomes the starting point for a better question."</p>
              </div>

            </div>

            <!-- PAGE 4: ENGINEERING PRINCIPLES -->
            <div class="space-y-4 text-left">
              <div>
                <span class="text-[10px] font-mono uppercase tracking-[0.2em] text-[#8b2252] font-bold block mb-1">PAGE 4</span>
                <h3 class="text-2xl font-bold font-serif text-[#1F1F1F]">ENGINEERING PRINCIPLES</h3>
                <p class="text-xs text-gray-500 font-medium italic">Ideas that influence every project I choose to build.</p>
              </div>

              <div class="space-y-2 text-[11px] text-gray-700">
                
                <div class="p-2.5 rounded-xl bg-white/80 border border-amber-900/10">
                  <h4 class="font-bold text-xs text-[#421835]">Principle 01 — Build With Purpose</h4>
                  <p class="text-gray-600 leading-relaxed">Technology should create measurable value. Features should solve meaningful problems—not because they are technically impressive.</p>
                </div>

                <div class="p-2.5 rounded-xl bg-white/80 border border-amber-900/10">
                  <h4 class="font-bold text-xs text-[#421835]">Principle 02 — Learn Continuously</h4>
                  <p class="text-gray-600 leading-relaxed">Technology evolves faster than any curriculum. Remaining effective requires continuous learning, experimentation, and adaptation.</p>
                </div>

                <div class="p-2.5 rounded-xl bg-white/80 border border-amber-900/10">
                  <h4 class="font-bold text-xs text-[#421835]">Principle 03 — Design For Humans</h4>
                  <p class="text-gray-600 leading-relaxed">Behind every interface is a person trying to accomplish something. Thoughtful design reduces confusion, respects attention, and allows technology to become almost invisible.</p>
                </div>

                <div class="p-2.5 rounded-xl bg-white/80 border border-amber-900/10">
                  <h4 class="font-bold text-xs text-[#421835]">Principle 04 — Document Everything That Matters</h4>
                  <p class="text-gray-600 leading-relaxed">Knowledge becomes valuable only when it can be transferred. Clear documentation preserves context and supports collaboration.</p>
                </div>

                <div class="p-2.5 rounded-xl bg-white/80 border border-amber-900/10">
                  <h4 class="font-bold text-xs text-[#421835]">Principle 05 — Progress Through Iteration</h4>
                  <p class="text-gray-600 leading-relaxed">Perfection is rarely achieved in the first version. Meaningful improvement comes through observation, feedback, refinement, and repetition.</p>
                </div>

              </div>

              <!-- Notebook Reflection Box & Closing -->
              <div class="p-3 bg-[#f0e8dc] rounded-2xl border border-amber-900/15 text-[10px] font-mono text-gray-800 text-center font-bold">
                Knowledge + Curiosity + Discipline + Consistency = Professional Growth
              </div>

              <div class="pt-2 border-t border-dashed border-amber-900/20 flex justify-between items-center text-[10px] font-serif italic text-gray-600">
                <span>"Every system teaches. Every mistake documents."</span>
                <span class="font-bold text-[#8b2252]">"Technology changes rapidly. Principles endure."</span>
              </div>

            </div>

          </div>

          <!-- Bottom Footer Nav -->
          <div class="mt-6 pt-3 border-t border-amber-900/10 flex justify-between items-center text-xs font-mono text-gray-500">
            <button onclick="turnToPage('spread1')" class="hover:text-[#8b2252] font-bold cursor-pointer">← Page 1-2</button>
            <span class="font-bold text-gray-400">Page 3-4 of 4</span>
            <button onclick="closePhysicalBook()" class="hover:text-[#8b2252] font-bold cursor-pointer">Close Book ➔</button>
          </div>

        </div>
      </div>

    </div>

  </div>
</section>

<!-- Smooth Physical Book Open & Page Turn Script -->
<script>
  function openPhysicalBook() {
    const closedView = document.getElementById('book-closed-view');
    const openedView = document.getElementById('book-opened-view');
    const spread1 = document.getElementById('spread-1');
    const spread2 = document.getElementById('spread-2');

    if (closedView && openedView) {
      closedView.classList.remove('opacity-100');
      closedView.classList.add('opacity-0');

      setTimeout(() => {
        closedView.classList.add('hidden');
        openedView.classList.remove('hidden');
        if (spread1) spread1.classList.remove('hidden');
        if (spread2) spread2.classList.add('hidden');

        setTimeout(() => {
          openedView.classList.remove('opacity-0');
          openedView.classList.add('opacity-100');
        }, 50);
      }, 400);
    }
  }

  function closePhysicalBook() {
    const closedView = document.getElementById('book-closed-view');
    const openedView = document.getElementById('book-opened-view');

    if (closedView && openedView) {
      openedView.classList.remove('opacity-100');
      openedView.classList.add('opacity-0');

      setTimeout(() => {
        openedView.classList.add('hidden');
        closedView.classList.remove('hidden');

        setTimeout(() => {
          closedView.classList.remove('opacity-0');
          closedView.classList.add('opacity-100');
        }, 50);
      }, 400);
    }
  }

  function turnToPage(targetSpreadId) {
    const spread1 = document.getElementById('spread-1');
    const spread2 = document.getElementById('spread-2');

    let activeSpread, nextSpread;
    if (targetSpreadId === 'spread2') {
      activeSpread = spread1;
      nextSpread = spread2;
    } else {
      activeSpread = spread2;
      nextSpread = spread1;
    }

    if (activeSpread && nextSpread) {
      activeSpread.style.transition = 'all 0.5s ease';
      activeSpread.style.opacity = '0';
      activeSpread.style.transform = 'scale(0.97)';

      setTimeout(() => {
        activeSpread.classList.add('hidden');
        activeSpread.style.opacity = '';
        activeSpread.style.transform = '';

        nextSpread.classList.remove('hidden');
        nextSpread.style.opacity = '0';
        nextSpread.style.transform = 'scale(0.97)';

        setTimeout(() => {
          nextSpread.style.transition = 'all 0.5s ease';
          nextSpread.style.opacity = '1';
          nextSpread.style.transform = 'scale(1)';
        }, 50);
      }, 400);
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
    content = content[:start_pos] + REALISTIC_BOOK_HTML + '\n\n' + content[end_pos:]
    print("Successfully updated 3D Physical Book Flip with Brand Logos and zero shaking!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
