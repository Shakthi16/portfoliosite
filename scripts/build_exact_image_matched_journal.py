import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Preload required Google Fonts: Great Vibes, Patrick Hand, Kalam, Caveat, Outfit
FONT_TAG = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Architects+Daughter&family=Caveat:wght@400;600;700&family=Great+Vibes&family=Kalam:wght@300;400;700&family=Outfit:wght@400;600;700;800&family=Patrick+Hand&display=swap" rel="stylesheet">"""

if 'Great+Vibes' not in content:
    content = content.replace('</head>', FONT_TAG + '\n</head>')

# -------------------------------------------------------------
# EXACT IMAGE 1 & IMAGE 2 MATCHING JOURNAL HTML
# -------------------------------------------------------------
EXACT_JOURNAL_HTML = """<!-- REALISTIC DECKLE-EDGE TORN PAPER SEPARATION DIVIDER (TOP) -->
<div class="w-full relative z-20 pointer-events-none -mb-1 bg-[#FAF8F5]">
  <svg class="w-full h-7 md:h-11 text-[#FAF7F2] fill-current block" viewBox="0 0 1200 80" preserveAspectRatio="none">
    <path d="M0,0 L0,35 L15,38 L30,32 L45,41 L60,34 L75,39 L90,31 L105,37 L120,33 L135,42 L150,36 L165,40 L180,31 L195,38 L210,33 L225,41 L240,35 L255,39 L270,32 L285,38 L300,34 L315,40 L330,31 L345,39 L360,33 L375,41 L390,35 L405,38 L420,32 L435,40 L450,34 L465,39 L480,31 L495,38 L510,33 L525,42 L540,36 L555,40 L570,32 L585,39 L600,33 L615,41 L630,35 L645,38 L660,32 L675,40 L690,34 L705,39 L720,31 L735,38 L750,33 L765,42 L780,36 L795,40 L810,32 L825,39 L840,33 L855,41 L870,35 L885,38 L900,32 L915,40 L930,34 L945,39 L960,31 L975,38 L990,33 L1005,42 L1020,36 L1035,40 L1050,32 L1065,39 L1080,33 L1095,41 L1110,35 L1125,38 L1140,32 L1155,40 L1170,34 L1185,39 L1200,31 L1200,80 L0,80 Z"></path>
  </svg>
</div>

<!-- ABOUT ME: PHYSICAL JOURNAL BOOK (EXACT IMAGE MATCH) -->
<section class="relative bg-[#FAF7F2] text-[#1F1F1F] py-8 md:py-12 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">
  <div class="max-w-7xl mx-auto px-4 md:px-8 text-center">
    
    <!-- BOOK STAGE CONTAINER -->
    <div class="relative w-full max-w-[1040px] mx-auto min-h-[580px] md:min-h-[620px] flex items-center justify-center">

      <!-- ==================== CLOSED BOOK COVER STATE ==================== -->
      <div id="smriti-book-cover" class="cursor-pointer transition-all duration-500 z-40 group" onclick="openSmritiBook()">
        <div class="relative">
          <!-- Cover Book Image -->
          <div class="w-[330px] md:w-[430px] h-[540px] md:h-[580px] rounded-[28px] shadow-[0_30px_70px_-15px_rgba(0,0,0,0.35)] overflow-hidden relative bg-[#3D1426] border-2 border-[#3D1426]/50">
            <img src="cover.png" alt="Shakthi Sri Journal Cover" class="w-full h-full object-cover block"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/25 via-transparent to-transparent pointer-events-none"></div>
          </div>
          <!-- Spine Bookmark Ribbon -->
          <div class="w-7 h-14 bg-[#55826b] rounded-b-md shadow-md absolute -bottom-6 left-12 pointer-events-none"></div>
        </div>
      </div>

      <!-- ==================== OPENED PHYSICAL HARDCOVER BOOK ==================== -->
      <div id="smriti-book-opened" class="hidden w-full transition-opacity duration-500 opacity-0 z-30">
        
        <!-- HARDCOVER CONTAINER (BURGUNDY FRAME #3D1426 FULLY ENCLOSING PAGES) -->
        <div class="relative w-full rounded-[26px] md:rounded-[30px] p-2.5 md:p-3.5 shadow-[0_30px_80px_rgba(0,0,0,0.28)] border-2 border-[#3D1426] bg-[#3D1426]">
          
          <!-- OUTSIDE RIGHT VERTICAL INDEX TABS (STICKING OUT BEYOND THE BOOK COVER) -->
          <div class="absolute top-8 -right-9 md:-right-11 flex flex-col gap-2 z-50">
            
            <!-- Home / Cover Tab -->
            <button onclick="closeSmritiBook()" class="w-9 md:w-11 h-10 bg-[#EFE3D5] hover:bg-[#6B2137] text-gray-800 hover:text-white rounded-r-xl shadow-md border-t border-r border-b border-amber-900/20 flex items-center justify-center transition-all hover:translate-x-1" title="Close to Cover">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001-1.414-1.414l-7-7z"/></svg>
            </button>

            <!-- Tab 1: About Me (P. 01-02) -->
            <button id="tab-btn-spread1" onclick="switchSmritiSpread('spread1')" class="px-2 md:px-2.5 py-4 bg-[#541C2E] text-white text-[11px] font-bold rounded-r-xl shadow-md border-t border-r border-b border-amber-900/30 flex items-center justify-center transition-all hover:translate-x-1" style="writing-mode: vertical-rl; text-orientation: mixed; font-family: 'Outfit', sans-serif;">
              About Me
            </button>

            <!-- Tab 2: Things I Learnt (P. 03-04) -->
            <button id="tab-btn-spread2" onclick="switchSmritiSpread('spread2')" class="px-2 md:px-2.5 py-4 bg-[#7A364B] hover:bg-[#541C2E] text-white text-[11px] font-bold rounded-r-xl shadow-md border-t border-r border-b border-amber-900/30 flex items-center justify-center transition-all hover:translate-x-1" style="writing-mode: vertical-rl; text-orientation: mixed; font-family: 'Outfit', sans-serif;">
              Things I Learnt
            </button>

            <!-- Tab 3: Story Writing -->
            <button id="tab-btn-spread3" onclick="switchSmritiSpread('spread3')" class="px-2 md:px-2.5 py-4 bg-[#A36D7D] hover:bg-[#541C2E] text-white text-[11px] font-bold rounded-r-xl shadow-md border-t border-r border-b border-amber-900/30 flex items-center justify-center transition-all hover:translate-x-1 hidden sm:flex" style="writing-mode: vertical-rl; text-orientation: mixed; font-family: 'Outfit', sans-serif;">
              Story Writing
            </button>

          </div>

          <!-- INNER PAGES SPREAD 1 (EXACT MATCH TO IMAGE 1) -->
          <div id="smriti-spread-1" class="w-full bg-[#FAF6EE] rounded-[22px] p-6 md:p-8 relative overflow-hidden text-left min-h-[540px] md:min-h-[580px] flex flex-col justify-between" style="background-image: radial-gradient(#D8CFC3 1.2px, transparent 1.2px); background-size: 22px 22px;">
            
            <!-- TOP-RIGHT CLOSE BUTTON '✕' -->
            <button onclick="closeSmritiBook()" class="absolute top-4 right-5 text-gray-500 hover:text-[#6B2137] text-xl font-bold z-40 p-1 transition-colors" title="Close Journal">
              ✕
            </button>

            <!-- Center Spine Line -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[1.5px] bg-amber-900/15 hidden md:block"></div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 relative z-10 h-full">
              
              <!-- PAGE 01: LEFT SIDE (MATCHING IMAGE 1) -->
              <div class="flex flex-col justify-between text-left pr-0 md:pr-3">
                <div>
                  <!-- Main Header -->
                  <h3 class="text-4xl md:text-5xl font-bold text-[#1F1F1F] mb-1 tracking-tight" style="font-family: 'Outfit', sans-serif;">Shakthi Sri</h3>
                  
                  <!-- Sub-header Row with Pill & Cursive Handwriting -->
                  <div class="flex flex-wrap items-center gap-3 mb-5">
                    <span class="px-3.5 py-0.5 bg-[#E8D5CE] text-[#6B2137] text-[10px] font-bold rounded-full border border-[#D9BEB4] tracking-wider uppercase" style="font-family: 'Outfit', sans-serif;">DEVELOPER &amp; RESEARCHER</span>
                    <span class="text-xl text-[#2C2C2C] underline underline-offset-4 decoration-amber-900/40" style="font-family: 'Great Vibes', cursive;">class of 2026</span>
                  </div>

                  <!-- Timeline List with Icons -->
                  <div class="space-y-3 text-sm text-[#2C2C2C] font-medium mb-6" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/20 pb-1.5">
                      <span class="flex items-center gap-2.5 font-bold text-[#1F1F1F]">
                        <svg class="w-4 h-4 text-[#6B2137]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                        B.Tech Information Technology
                      </span>
                      <span class="text-gray-600">2022 - 2026</span>
                    </div>

                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/20 pb-1.5">
                      <span class="flex items-center gap-2.5 font-bold text-[#1F1F1F]">
                        <svg class="w-4 h-4 text-[#6B2137]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/></svg>
                        Kingston Engineering College
                      </span>
                      <span class="text-[#6B2137] font-bold">CGPA: 8.6</span>
                    </div>

                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/20 pb-1.5">
                      <span class="flex items-center gap-2.5 font-bold text-[#1F1F1F]">
                        <svg class="w-4 h-4 text-[#6B2137]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L5.6 15.12a2 2 0 00-1.182.17l-1.04.52a2 2 0 00-.778 2.766l1.54 2.31a2 2 0 002.324.793l2.45-.817a6 6 0 013.79 0l2.45.817a2 2 0 002.324-.793l1.54-2.31a2 2 0 00-.592-2.738z"/></svg>
                        IIT Madras — CYSTAR
                      </span>
                      <span class="text-gray-600">Research Intern</span>
                    </div>

                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/20 pb-1.5">
                      <span class="flex items-center gap-2.5 font-bold text-[#1F1F1F]">
                        <svg class="w-4 h-4 text-[#6B2137]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/></svg>
                        Full-Stack Developer
                      </span>
                      <span class="text-gray-600">MERN Stack</span>
                    </div>

                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/20 pb-1.5">
                      <span class="flex items-center gap-2.5 font-bold text-[#1F1F1F]">
                        <svg class="w-4 h-4 text-[#6B2137]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                        Cybersecurity Enthusiast
                      </span>
                      <span class="text-gray-600">Always Learning</span>
                    </div>
                  </div>

                  <!-- Taped Cards Row -->
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-4">
                    
                    <!-- Taped Note: about me ヾ -->
                    <div class="bg-[#F6EFE6] p-3.5 rounded-2xl border border-amber-900/15 shadow-sm relative">
                      <div class="absolute -top-2.5 left-1/2 -translate-x-1/2 w-8 h-3.5 bg-[#E6D7C3]/90 rotate-[-2deg] border-l border-r border-white/60"></div>
                      <span class="text-lg text-[#6B2137] font-bold block mb-1" style="font-family: 'Patrick Hand', 'Kalam', cursive;">about me ヾ</span>
                      <ul class="text-xs text-[#2C2C2C] leading-snug space-y-1" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                        <li>♥ I love turning ideas into impactful digital solutions.</li>
                        <li>♥ Curious mind with a strong drive to build, secure and innovate.</li>
                        <li>♥ Believer in discipline, consistency &amp; growth.</li>
                      </ul>
                      <span class="absolute bottom-1.5 right-2.5 text-xs text-[#6B2137]">♡</span>
                    </div>

                    <!-- TODAY Box with 3 colored dots & star -->
                    <div class="bg-[#F6EFE6] p-3.5 rounded-2xl border border-amber-900/15 shadow-sm relative">
                      <div class="flex items-center justify-between mb-1">
                        <div class="flex items-center gap-1">
                          <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                          <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                          <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                        </div>
                        <span class="text-xs text-amber-900 font-bold">☆</span>
                      </div>
                      <span class="text-[10px] font-mono font-bold text-gray-500 uppercase block mb-1">TODAY</span>
                      <p class="text-xs text-[#2C2C2C] leading-relaxed" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                        Building skills.<br/>Solving problems.<br/>Creating solutions.<br/>Preparing for impact.<br/>One step at a time.
                      </p>
                    </div>

                  </div>
                </div>

                <!-- Contact Memo & Quote -->
                <div class="pt-3 border-t border-dashed border-amber-900/20 flex justify-between items-center gap-3">
                  <div class="bg-[#EFE5D8] px-3 py-2 rounded-xl text-xs text-[#2C2C2C] border border-amber-900/15" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                    <p class="font-bold">srishakthi799@gmail.com</p>
                    <p class="text-gray-600">+91 7895032098</p>
                    <p class="text-gray-500">Chennai | Vellore</p>
                  </div>
                  <div class="text-right">
                    <span class="text-2xl text-[#6B2137] font-serif leading-none block">“</span>
                    <p class="text-lg text-[#541C2E] font-bold leading-tight" style="font-family: 'Great Vibes', cursive;">code with purpose,<br/>create with impact.</p>
                    <div class="w-16 h-0.5 bg-[#541C2E]/40 ml-auto mt-0.5"></div>
                    <span class="text-xs text-[#6B2137] block mt-0.5">♡</span>
                  </div>
                </div>

              </div>

              <!-- PAGE 02: RIGHT SIDE (MATCHING IMAGE 1) -->
              <div class="flex flex-col justify-between relative text-left pl-0 md:pl-3">
                
                <!-- Top Row: Flower, Goals, Reminders -->
                <div class="flex justify-between items-start mb-3">
                  <div class="text-center">
                    <!-- Flower Illustration SVG -->
                    <svg class="w-6 h-8 text-[#6B2137] mx-auto" viewBox="0 0 24 32" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 28V12M12 12C9 9 5 10 5 10s1 4 4 5M12 12c3-3 7-2 7-2s-1 4-4 5M12 12c-2-3-1-7-1-7s4 1 4 5"/></svg>
                    <span class="block text-xs text-gray-700 mt-0.5" style="font-family: 'Patrick Hand', 'Kalam', cursive;">breathe.png</span>
                  </div>
                  <div class="flex items-center gap-6" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                    <div class="text-center">
                      <div class="w-8 h-8 bg-[#6B2137]/10 rounded-lg flex items-center justify-center text-[#6B2137] text-sm font-bold mx-auto">
                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M2 6a2 2 0 012-2h5l2 2h5a2 2 0 012 2v6a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"/></svg>
                      </div>
                      <span class="block text-xs text-gray-600 mt-0.5">Goals</span>
                    </div>
                    <div class="text-center">
                      <div class="w-8 h-8 bg-amber-900/10 rounded-lg flex items-center justify-center text-amber-900 text-sm font-bold mx-auto">
                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M4 3a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2H4zm12 12H4l4-8 3 6 2-4 3 6z"/></svg>
                      </div>
                      <span class="block text-xs text-gray-600 mt-0.5">Reminders</span>
                    </div>
                  </div>
                </div>

                <!-- Currently Box & Illustration Container -->
                <div class="grid grid-cols-1 sm:grid-cols-12 gap-4 items-center mb-4">
                  
                  <!-- currently ヾ -->
                  <div class="sm:col-span-6 border border-dashed border-amber-900/30 rounded-2xl p-3.5 bg-[#F8F3EA]">
                    <span class="text-lg text-[#6B2137] font-bold block mb-1.5" style="font-family: 'Patrick Hand', 'Kalam', cursive;">currently ヾ</span>
                    <ul class="text-xs text-[#2C2C2C] leading-snug space-y-1" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                      <li>♥ Exploring AI &amp; LLMs</li>
                      <li>♥ Building secure systems</li>
                      <li>♥ Deepening full-stack</li>
                      <li>♥ Learning. Shipping.</li>
                      <li>♥ Growing. Always.</li>
                    </ul>
                    <span class="block text-right text-xs text-[#6B2137] mt-1">♡</span>
                  </div>

                  <!-- Character Illustration / Photo with @Shakthi.16 Tag -->
                  <div class="sm:col-span-6 flex justify-center relative">
                    <div class="relative">
                      <div class="w-[150px] md:w-[170px] h-[190px] md:h-[210px] rounded-[22px] overflow-hidden shadow-md border-4 border-white bg-white">
                        <img src="girl.png" alt="Shakthi Sri Illustration" class="w-full h-full object-cover"/>
                      </div>
                      <div class="absolute -top-3 right-2 bg-[#1A1A1A] text-white font-mono text-[9px] font-bold px-3 py-1 rounded-full shadow-md z-30">
                        @Shakthi.16
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Tech I Work With (Official Brand Colored Logos) -->
                <div class="border border-dashed border-amber-900/30 rounded-2xl p-3 bg-[#F8F3EA] mb-3">
                  <span class="text-base text-[#6B2137] font-bold block mb-2" style="font-family: 'Patrick Hand', 'Kalam', cursive;">tech i work with ヾ</span>
                  
                  <div class="grid grid-cols-7 gap-2 items-center text-center text-[10px] font-medium text-gray-700">
                    <!-- React -->
                    <div class="flex flex-col items-center">
                      <svg class="w-5 h-5 text-[#61DAFB]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 9a3 3 0 100 6 3 3 0 000-6zm0-7c-5.52 0-10 1.79-10 4s4.48 4 10 4 10-1.79 10-4-4.48-4-10-4zm0 6c-4.41 0-8-1.34-8-2s3.59-2 8-2 8 1.34 8 2-3.59 2-8 2z"/></svg>
                      <span class="mt-0.5">React.js</span>
                    </div>
                    <!-- Node -->
                    <div class="flex flex-col items-center">
                      <div class="w-5 h-5 rounded-md bg-[#339933] text-white text-[9px] font-bold flex items-center justify-center">ncb</div>
                      <span class="mt-0.5">Node.js</span>
                    </div>
                    <!-- Express -->
                    <div class="flex flex-col items-center">
                      <span class="font-mono font-bold text-xs text-gray-800">ex</span>
                      <span class="mt-0.5">Express.js</span>
                    </div>
                    <!-- MongoDB -->
                    <div class="flex flex-col items-center">
                      <svg class="w-5 h-5 text-[#47A248]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 1.5C11.5 3 7 7.5 7 13c0 3 2 5.5 5 6.5 3-1 5-3.5 5-6.5 0-5.5-4.5-10-5-11.5z"/></svg>
                      <span class="mt-0.5">MongoDB</span>
                    </div>
                    <!-- Figma -->
                    <div class="flex flex-col items-center border-l border-dashed border-amber-900/20 pl-2">
                      <svg class="w-5 h-5 text-[#F24E1E]" fill="currentColor" viewBox="0 0 24 24"><path d="M8 2h4v4H8V2zm0 6h4v4H8V8zm0 6h4v4a4 4 0 11-4-4zm8-12h4v4h-4V2zm0 6h4v4h-4V8z"/></svg>
                      <span class="mt-0.5">Figma</span>
                    </div>
                    <!-- VS Code -->
                    <div class="flex flex-col items-center">
                      <svg class="w-5 h-5 text-[#007ACC]" fill="currentColor" viewBox="0 0 24 24"><path d="M23.15 2.587L18.21.21a1.494 1.494 0 00-1.705.291L7.548 8.69 3.4 5.564a.747.747 0 00-.986.079L.24 7.728a.747.747 0 00-.03.996l3.96 4.67-3.96 4.67a.747.747 0 00.03.996l2.174 2.085a.747.747 0 00.986.079l4.148-3.126 8.957 8.189c.498.455 1.25.412 1.705-.098l4.94-4.757a1.494 1.494 0 00.44-1.077V3.664c0-.406-.164-.796-.44-1.077z"/></svg>
                      <span class="mt-0.5">VS Code</span>
                    </div>
                    <!-- Linux -->
                    <div class="flex flex-col items-center">
                      <svg class="w-5 h-5 text-black" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C9.5 2 7.5 4 7.5 6.5v4c0 1.5-1 3-2.5 4 0 3 3 5.5 7 5.5s7-2.5 7-5.5c-1.5-1-2.5-2.5-2.5-4v-4C16.5 4 14.5 2 12 2z"/></svg>
                      <span class="mt-0.5">Linux</span>
                    </div>
                  </div>
                </div>

                <!-- What I Build Box & Dried Flower Taped Card -->
                <div class="grid grid-cols-12 gap-3 items-center">
                  <div class="col-span-9 border border-dashed border-amber-900/30 rounded-2xl p-2.5 bg-[#F8F3EA]">
                    <span class="text-base text-[#6B2137] font-bold block mb-1 text-center" style="font-family: 'Patrick Hand', 'Kalam', cursive;">what i build ♡</span>
                    <div class="grid grid-cols-3 gap-2 text-center text-xs font-bold text-gray-800" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                      <div class="p-1.5 bg-white/80 rounded-xl border border-amber-900/10 flex items-center justify-center gap-1">🌐 Full-Stack Web Applications</div>
                      <div class="p-1.5 bg-white/80 rounded-xl border border-amber-900/10 flex items-center justify-center gap-1">🔒 Cybersecurity Tools &amp; Research</div>
                      <div class="p-1.5 bg-white/80 rounded-xl border border-amber-900/10 flex items-center justify-center gap-1">🧠 AI-Enhanced Solutions</div>
                    </div>
                  </div>

                  <!-- Taped Botanical Card -->
                  <div class="col-span-3 bg-[#EFE5D8] p-2 rounded-xl border border-amber-900/15 text-center relative shadow-sm">
                    <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-6 h-2.5 bg-[#E6D7C3]/90 rotate-[-2deg]"></div>
                    <svg class="w-5 h-7 text-[#6B2137] mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 22V8M12 8C9 5 5 6 5 6s1 4 4 5M12 8c3-3 7-2 7-2s-1 4-4 5"/></svg>
                  </div>
                </div>

              </div>

            </div>

          </div>

          <!-- INNER PAGES SPREAD 2 (EXACT MATCH TO IMAGE 2) -->
          <div id="smriti-spread-2" class="hidden w-full bg-[#FAF6EE] rounded-[22px] p-6 md:p-8 relative overflow-hidden text-left min-h-[540px] md:min-h-[580px] flex flex-col justify-between" style="background-image: radial-gradient(#D8CFC3 1.2px, transparent 1.2px); background-size: 22px 22px;">
            
            <!-- TOP-RIGHT CLOSE BUTTON '✕' -->
            <button onclick="closeSmritiBook()" class="absolute top-4 right-5 text-gray-500 hover:text-[#6B2137] text-xl font-bold z-40 p-1 transition-colors" title="Close Journal">
              ✕
            </button>

            <!-- Center Spine Line -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[1.5px] bg-amber-900/15 hidden md:block"></div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 relative z-10 h-full">
              
              <!-- PAGE 03: ON BUILDING. JOURNAL ENTRY — 03 (MATCHING IMAGE 2) -->
              <div class="flex flex-col justify-between text-left pr-0 md:pr-3">
                
                <!-- Header with 03 Pill Badge -->
                <div>
                  <div class="flex items-center gap-2.5 mb-1">
                    <span class="px-2 py-0.5 bg-[#E8D5CE] text-[#6B2137] font-bold text-xs rounded-md border border-[#D9BEB4]">03</span>
                    <h3 class="text-3xl md:text-4xl font-bold text-[#1F1F1F]" style="font-family: 'Patrick Hand', 'Kalam', cursive;">On Building. ヾ</h3>
                  </div>
                  <p class="text-xs text-gray-500 mb-3" style="font-family: 'Patrick Hand', 'Kalam', cursive;">Journal Entry — 03</p>

                  <p class="text-xs text-[#2C2C2C] leading-relaxed mb-2" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                    When I first started writing software, I believed engineering was about finding answers.<br/>
                    Over time, I realised it is far more often about <span class="underline underline-offset-2 decoration-amber-900/50 font-bold">asking better questions.</span>
                  </p>

                  <ul class="text-xs text-[#2C2C2C] space-y-1 mb-3" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                    <li>♥ What problem actually needs solving?</li>
                    <li>♥ Who will depend on this system tomorrow?</li>
                    <li>♥ What assumptions am I making today that could become failures later?</li>
                  </ul>

                  <p class="text-xs text-[#2C2C2C] leading-relaxed mb-2" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                    The quality of a solution is usually determined long before the first line of code is written.<br/>
                    <span class="underline underline-offset-2 decoration-amber-900/50 font-bold text-[#6B2137]">Good engineering begins with understanding.</span><br/>
                    Everything else follows.
                  </p>
                </div>

                <!-- Taped Quote Note & Bridge Sketch Illustration -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center my-2">
                  
                  <!-- Taped Quote Card -->
                  <div class="bg-[#F6EFE6] p-3 rounded-2xl border border-amber-900/15 shadow-sm text-xs text-[#2C2C2C] relative" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                    <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-7 h-3 bg-[#E6D7C3]/90 rotate-[-1deg]"></div>
                    <span class="text-base text-[#6B2137] block mb-0.5">“</span>
                    If a system becomes difficult to explain, it is usually becoming difficult to maintain.
                    <span class="text-base text-[#6B2137] block text-right">”</span>
                  </div>

                  <!-- Bridge Sketch Illustration -->
                  <div class="text-center p-2 bg-white/60 rounded-2xl border border-amber-900/10 shadow-sm">
                    <!-- Drawn suspension bridge SVG -->
                    <svg class="w-full h-16 text-[#6B2137]/80" viewBox="0 0 120 40" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M10 35h100M30 10v25M90 10v25M10 25c20-10 40-10 50 0c10-10 30-10 50 0M30 10L10 25M30 10l30 15M90 10l-30 15M90 10l20 15"/><path stroke-linecap="round" stroke-width="0.5" stroke-dasharray="1 1" d="M30 18h60M30 24h60"/></svg>
                  </div>
                </div>

                <!-- Bottom Wire Spiral Note & Reflection Card -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2 border-t border-dashed border-amber-900/20">
                  
                  <!-- Spiral Coil Note Card -->
                  <div class="bg-[#F8F3EA] p-3 rounded-2xl border border-amber-900/15 relative pl-7" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                    <!-- Wire Coils on left -->
                    <div class="absolute left-2 top-2 bottom-2 flex flex-col justify-between">
                      <div class="w-2.5 h-2.5 rounded-full border-2 border-gray-400"></div>
                      <div class="w-2.5 h-2.5 rounded-full border-2 border-gray-400"></div>
                      <div class="w-2.5 h-2.5 rounded-full border-2 border-gray-400"></div>
                      <div class="w-2.5 h-2.5 rounded-full border-2 border-gray-400"></div>
                    </div>

                    <p class="font-bold text-xs text-[#6B2137] mb-1">A small note I often return to</p>
                    <ul class="text-[11px] text-[#2C2C2C] space-y-0.5">
                      <li>👁️ Observe.</li>
                      <li>💡 Understand.</li>
                      <li>⊖ Reduce.</li>
                      <li>&lt;/&gt; Build.</li>
                      <li>📈 Improve.</li>
                      <li>↺ Repeat. ♡</li>
                    </ul>
                  </div>

                  <!-- Reflection Card -->
                  <div class="text-left text-xs text-[#2C2C2C] flex flex-col justify-between" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                    <div>
                      <span class="font-bold text-sm text-[#6B2137] block mb-1 underline underline-offset-2">Reflection</span>
                      <p class="leading-relaxed">
                        I no longer measure progress by the number of features I complete. I measure it by <span class="bg-[#EFE5D8] px-1 rounded font-bold">how much clearer my thinking becomes</span> after each project. ☆
                      </p>
                    </div>
                  </div>

                </div>

              </div>

              <!-- PAGE 04: THINGS I'VE LEARNED. ♡ (MATCHING IMAGE 2) -->
              <div class="flex flex-col justify-between text-left pl-0 md:pl-3">
                
                <div>
                  <!-- Page Number Badge 04 & Header -->
                  <div class="flex items-center justify-between mb-2">
                    <div>
                      <h3 class="text-3xl md:text-4xl font-bold text-[#1F1F1F] mb-1" style="font-family: 'Patrick Hand', 'Kalam', cursive;">Things I've Learned. ♡</h3>
                      <div class="w-24 h-1 bg-[#6B2137]/40 rounded-full"></div>
                    </div>
                    <span class="px-2 py-0.5 bg-[#E8D5CE] text-[#6B2137] font-bold text-xs rounded-md border border-[#D9BEB4]">04</span>
                  </div>

                  <!-- 4 Circle Icon Items Grid -->
                  <div class="space-y-3 text-xs text-[#2C2C2C] mb-4" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                    
                    <!-- Item 1: </> -->
                    <div class="flex items-start gap-3">
                      <div class="w-7 h-7 rounded-full bg-[#EFE5D8] border border-amber-900/20 flex items-center justify-center text-xs font-bold text-[#6B2137] shrink-0 mt-0.5">&lt;/&gt;</div>
                      <div>
                        <h4 class="font-bold text-sm text-[#1F1F1F]">The best code usually disappears.</h4>
                        <p class="text-gray-600 leading-tight">Users remember experiences. Developers remember implementations. Good engineering satisfies both. ♡</p>
                      </div>
                    </div>

                    <!-- Item 2: Clock -->
                    <div class="flex items-start gap-3">
                      <div class="w-7 h-7 rounded-full bg-[#EFE5D8] border border-amber-900/20 flex items-center justify-center text-xs font-bold text-[#6B2137] shrink-0 mt-0.5">🕒</div>
                      <div>
                        <h4 class="font-bold text-sm text-[#1F1F1F]">Speed is temporary.</h4>
                        <p class="text-gray-600 leading-tight">Maintainability is permanent. Every shortcut eventually introduces interest that someone must repay.</p>
                      </div>
                    </div>

                    <!-- Item 3: Document -->
                    <div class="flex items-start gap-3">
                      <div class="w-7 h-7 rounded-full bg-[#EFE5D8] border border-amber-900/20 flex items-center justify-center text-xs font-bold text-[#6B2137] shrink-0 mt-0.5">📄</div>
                      <div>
                        <h4 class="font-bold text-sm text-[#1F1F1F]">Documentation is an act of respect.</h4>
                        <p class="text-gray-600 leading-tight">For teammates. For future contributors. For the version of yourself who returns six months later. ☆</p>
                      </div>
                    </div>

                    <!-- Item 4: Plant -->
                    <div class="flex items-start gap-3">
                      <div class="w-7 h-7 rounded-full bg-[#EFE5D8] border border-amber-900/20 flex items-center justify-center text-xs font-bold text-[#6B2137] shrink-0 mt-0.5">🌱</div>
                      <div>
                        <h4 class="font-bold text-sm text-[#1F1F1F]">Learning is never finished.</h4>
                        <p class="text-gray-600 leading-tight">Technology changes. Tools change. Expectations change. Curiosity should not. ♡</p>
                      </div>
                    </div>

                  </div>

                  <!-- Taped Bottom Wisdom Card -->
                  <div class="p-3 bg-[#F6EFE6] rounded-2xl border border-amber-900/15 text-xs text-[#2C2C2C] text-center mb-3 relative shadow-sm" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                    <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-8 h-3 bg-[#E6D7C3]/90 rotate-[1deg]"></div>
                    Every completed project leaves behind more than software. It leaves behind a better engineer than the one who started it. 🌸
                  </div>
                </div>

                <!-- Right Column: Working With Others 👥 -->
                <div class="pt-2 border-t border-dashed border-amber-900/20">
                  <div class="flex items-center justify-between mb-1">
                    <h4 class="font-bold text-base text-[#1F1F1F]" style="font-family: 'Patrick Hand', 'Kalam', cursive;">Working With Others. 👥</h4>
                  </div>

                  <p class="text-xs text-gray-600 leading-tight mb-2" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                    Not every contribution is visible in a commit history.<br/>
                    Some improve communication. Some simplify decisions. Some prevent mistakes before they happen.
                  </p>

                  <!-- Taped Note: Most valuable work -->
                  <div class="bg-[#F6EFE6] p-2.5 rounded-xl border border-amber-900/15 text-xs text-[#2C2C2C] text-center mb-2" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                    "The most valuable work is often the work no one notices because everything simply functions as expected. ♡"
                  </div>

                  <p class="text-xs font-bold text-[#6B2137] mb-1" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                    I believe professionalism is demonstrated through reliability rather than recognition.
                  </p>

                  <ul class="text-xs text-[#2C2C2C] space-y-0.5" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                    <li>♥ Showing up prepared.</li>
                    <li>♥ Writing clearly.</li>
                    <li>♥ Listening carefully.</li>
                    <li>♥ Accepting feedback without defending ego.</li>
                    <li>♥ Leaving projects easier to continue than they were found.</li>
                  </ul>
                </div>

              </div>

            </div>

          </div>

          <!-- INNER PAGES SPREAD 3 (STORY WRITING) -->
          <div id="smriti-spread-3" class="hidden w-full bg-[#FAF6EE] rounded-[22px] p-6 md:p-8 relative overflow-hidden text-left min-h-[540px] md:min-h-[580px] flex flex-col justify-between" style="background-image: radial-gradient(#D8CFC3 1.2px, transparent 1.2px); background-size: 22px 22px;">
            
            <!-- TOP-RIGHT CLOSE BUTTON '✕' -->
            <button onclick="closeSmritiBook()" class="absolute top-4 right-5 text-gray-500 hover:text-[#6B2137] text-xl font-bold z-40 p-1 transition-colors" title="Close Journal">
              ✕
            </button>

            <!-- Center Spine Line -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[1.5px] bg-amber-900/15 hidden md:block"></div>

            <div class="flex flex-col items-center justify-center h-full text-center p-8">
              <span class="text-5xl mb-4">✍️</span>
              <h3 class="text-4xl font-bold text-[#1F1F1F] mb-3" style="font-family: 'Great Vibes', cursive;">Story Writing</h3>
              <p class="text-lg text-gray-700 max-w-md" style="font-family: 'Patrick Hand', 'Kalam', cursive;">
                "Story writing section ready! Provide your stories or text whenever you'd like to populate these pages." ♡
              </p>
            </div>

          </div>

        </div>

      </div>

    </div>

  </div>
</section>

<!-- REALISTIC DECKLE-EDGE TORN PAPER BOTTOM SEPARATION DIVIDER -->
<div class="w-full relative z-20 pointer-events-none -mt-1 bg-[#FAF7F2]">
  <svg class="w-full h-7 md:h-11 text-white fill-current block" viewBox="0 0 1200 80" preserveAspectRatio="none">
    <path d="M0,0 L15,9 L30,3 L45,12 L60,5 L75,10 L90,2 L105,8 L120,4 L135,13 L150,7 L165,11 L180,2 L195,9 L210,4 L225,12 L240,6 L255,10 L270,3 L285,9 L300,5 L315,11 L330,2 L345,10 L360,4 L375,12 L390,6 L405,9 L420,3 L435,11 L450,5 L465,10 L480,2 L495,9 L510,4 L525,13 L540,7 L555,11 L570,3 L585,10 L600,4 L615,12 L630,6 L645,9 L660,3 L675,11 L690,5 L705,10 L720,2 L735,9 L750,4 L765,13 L780,7 L795,11 L810,3 L825,10 L840,4 L855,12 L870,6 L885,9 L900,3 L915,11 L930,5 L945,10 L960,2 L975,9 L990,4 L1005,13 L1020,7 L1035,11 L1050,3 L1065,10 L1080,4 L1095,12 L1110,6 L1125,9 L1140,3 L1155,11 L1170,5 L1185,10 L1200,2 L1200,80 L0,80 Z"></path>
  </svg>
</div>

<!-- Smooth Physical Journal Open/Close & Spread Switch Script -->
<script>
  function openSmritiBook() {
    const coverView = document.getElementById('smriti-book-cover');
    const openedView = document.getElementById('smriti-book-opened');
    const spread1 = document.getElementById('smriti-spread-1');
    const spread2 = document.getElementById('smriti-spread-2');
    const spread3 = document.getElementById('smriti-spread-3');

    if (coverView && openedView) {
      coverView.style.transition = 'transform 0.8s cubic-bezier(0.645, 0.045, 0.355, 1), opacity 0.5s ease';
      coverView.style.transform = 'rotateY(-90deg) scale(0.95)';
      coverView.style.opacity = '0';

      setTimeout(() => {
        coverView.classList.add('hidden');
        openedView.classList.remove('hidden');
        if (spread1) spread1.classList.remove('hidden');
        if (spread2) spread2.classList.add('hidden');
        if (spread3) spread3.classList.add('hidden');

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
    const spread3 = document.getElementById('smriti-spread-3');
    const btn1 = document.getElementById('tab-btn-spread1');
    const btn2 = document.getElementById('tab-btn-spread2');
    const btn3 = document.getElementById('tab-btn-spread3');

    const spreads = { 'spread1': spread1, 'spread2': spread2, 'spread3': spread3 };
    const btns = { 'spread1': btn1, 'spread2': btn2, 'spread3': btn3 };

    Object.keys(spreads).forEach(key => {
      if (spreads[key]) {
        if (key === targetId) {
          spreads[key].classList.remove('hidden');
          spreads[key].style.opacity = '1';
        } else {
          spreads[key].classList.add('hidden');
        }
      }
      if (btns[key]) {
        if (key === targetId) {
          btns[key].classList.remove('bg-[#7A364B]', 'bg-[#A36D7D]');
          btns[key].classList.add('bg-[#541C2E]');
        } else {
          btns[key].classList.remove('bg-[#541C2E]');
          btns[key].classList.add(key === 'spread2' ? 'bg-[#7A364B]' : 'bg-[#A36D7D]');
        }
      }
    });
  }
</script>
"""

# Replace section in index.html
start_pos = content.find('<!-- REALISTIC DECKLE-EDGE TORN PAPER SEPARATION DIVIDER (TOP)')
if start_pos == -1:
    start_pos = content.find('<!-- REALISTIC DECKLE-EDGE TORN PAPER SEPARATION DIVIDER')
    if start_pos == -1:
        start_pos = content.find('id="about-journal"')
        start_pos = content.rfind('<section', 0, start_pos)

end_pos = content.find('<!-- ==================== 2. EDITORIAL CANVAS (#about) ==================== -->')
if end_pos == -1:
    end_pos = content.find('id="about"')
    end_pos = content.rfind('<section', 0, end_pos)

if start_pos != -1 and end_pos != -1:
    content = content[:start_pos] + EXACT_JOURNAL_HTML + '\n\n' + content[end_pos:]
    print("Successfully built exact Image 1 & Image 2 matching journal layout, logos, fonts and Great Vibes handwriting!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
