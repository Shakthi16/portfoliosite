import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Load Google Fonts: Great Vibes, Patrick Hand, Handlee, Caveat, Outfit
FONT_TAG = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@400;600;700&family=Great+Vibes&family=Handlee&family=Outfit:wght@400;600;700;800&family=Patrick+Hand&display=swap" rel="stylesheet">"""

if 'Patrick+Hand' not in content or 'Handlee' not in content:
    content = content.replace('</head>', FONT_TAG + '\n</head>')

# -------------------------------------------------------------
# PERFECT CREATIVE JOURNAL ARRANGEMENT & FONT MATCHING
# -------------------------------------------------------------
CREATIVE_JOURNAL_HTML = """<!-- REALISTIC DECKLE-EDGE TORN PAPER SEPARATION DIVIDER (TOP) -->
<div class="w-full relative z-20 pointer-events-none -mb-1 bg-[#FAF8F5]">
  <svg class="w-full h-7 md:h-10 text-[#FAF7F2] fill-current block" viewBox="0 0 1200 80" preserveAspectRatio="none">
    <path d="M0,0 L0,35 L15,38 L30,32 L45,41 L60,34 L75,39 L90,31 L105,37 L120,33 L135,42 L150,36 L165,40 L180,31 L195,38 L210,33 L225,41 L240,35 L255,39 L270,32 L285,38 L300,34 L315,40 L330,31 L345,39 L360,33 L375,41 L390,35 L405,38 L420,32 L435,40 L450,34 L465,39 L480,31 L495,38 L510,33 L525,42 L540,36 L555,40 L570,32 L585,39 L600,33 L615,41 L630,35 L645,38 L660,32 L675,40 L690,34 L705,39 L720,31 L735,38 L750,33 L765,42 L780,36 L795,40 L810,32 L825,39 L840,33 L855,41 L870,35 L885,38 L900,32 L915,40 L930,34 L945,39 L960,31 L975,38 L990,33 L1005,42 L1020,36 L1035,40 L1050,32 L1065,39 L1080,33 L1095,41 L1110,35 L1125,38 L1140,32 L1155,40 L1170,34 L1185,39 L1200,31 L1200,80 L0,80 Z"></path>
  </svg>
</div>

<!-- ABOUT ME: PHYSICAL JOURNAL BOOK (EXACT CREATIVE LAYOUT & FONTS MATCH) -->
<section class="relative bg-[#FAF7F2] text-[#1F1F1F] py-6 md:py-10 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">
  <div class="max-w-6xl mx-auto px-3 md:px-6 text-center">
    
    <!-- BOOK STAGE CONTAINER -->
    <div class="relative w-full max-w-[890px] mx-auto min-h-[520px] md:min-h-[560px] flex items-center justify-center">

      <!-- ==================== CLOSED BOOK COVER STATE ==================== -->
      <div id="smriti-book-cover" class="cursor-pointer transition-all duration-500 z-40 group" onclick="openSmritiBook()">
        <div class="relative">
          <!-- Cover Book Image (Proportional 380px x 530px) -->
          <div class="w-[290px] md:w-[380px] h-[480px] md:h-[530px] rounded-[26px] shadow-[0_25px_65px_-15px_rgba(0,0,0,0.38)] overflow-hidden relative bg-[#3D1426] border-2 border-[#3D1426]/50">
            <img src="cover.png" alt="Shakthi Sri Journal Cover" class="w-full h-full object-cover block"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/25 via-transparent to-transparent pointer-events-none"></div>
          </div>
          <!-- Spine Bookmark Ribbon -->
          <div class="w-6 h-12 bg-[#55826b] rounded-b-md shadow-md absolute -bottom-5 left-10 pointer-events-none"></div>
        </div>
      </div>

      <!-- ==================== OPENED PHYSICAL HARDCOVER BOOK ==================== -->
      <div id="smriti-book-opened" class="hidden w-full transition-opacity duration-500 opacity-0 z-30">
        
        <!-- HARDCOVER FRAME: BURGUNDY #3D1426 MARGIN ENCLOSING PAGES -->
        <div class="relative w-full max-w-[860px] mx-auto rounded-[24px] p-2.5 md:p-3 shadow-[0_25px_70px_rgba(0,0,0,0.3)] border-2 border-[#3D1426] bg-[#3D1426]">
          
          <!-- OUTSIDE RIGHT VERTICAL INDEX TABS -->
          <div class="absolute top-6 -right-8 md:-right-10 flex flex-col gap-2 z-50">
            
            <!-- Home / Cover Tab -->
            <button onclick="closeSmritiBook()" class="w-8 md:w-10 h-9 bg-[#EFE3D5] hover:bg-[#6B2137] text-gray-800 hover:text-white rounded-r-xl shadow-md border-t border-r border-b border-amber-900/20 flex items-center justify-center transition-all hover:translate-x-1" title="Close to Cover">
              <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001-1.414-1.414l-7-7z"/></svg>
            </button>

            <!-- Tab 1: About Me (P. 01-02) -->
            <button id="tab-btn-spread1" onclick="switchSmritiSpread('spread1')" class="px-1.5 md:px-2 py-4 bg-[#541C2E] text-white text-[10px] font-bold rounded-r-xl shadow-md border-t border-r border-b border-amber-900/30 flex items-center justify-center transition-all hover:translate-x-1" style="writing-mode: vertical-rl; text-orientation: mixed; font-family: 'Outfit', sans-serif;">
              About Me
            </button>

            <!-- Tab 2: Things I Learnt (P. 03-04) -->
            <button id="tab-btn-spread2" onclick="switchSmritiSpread('spread2')" class="px-1.5 md:px-2 py-4 bg-[#7A364B] hover:bg-[#541C2E] text-white text-[10px] font-bold rounded-r-xl shadow-md border-t border-r border-b border-amber-900/30 flex items-center justify-center transition-all hover:translate-x-1" style="writing-mode: vertical-rl; text-orientation: mixed; font-family: 'Outfit', sans-serif;">
              Things I Learnt
            </button>

            <!-- Tab 3: Story Writing -->
            <button id="tab-btn-spread3" onclick="switchSmritiSpread('spread3')" class="px-1.5 md:px-2 py-4 bg-[#A36D7D] hover:bg-[#541C2E] text-white text-[10px] font-bold rounded-r-xl shadow-md border-t border-r border-b border-amber-900/30 flex items-center justify-center transition-all hover:translate-x-1 hidden sm:flex" style="writing-mode: vertical-rl; text-orientation: mixed; font-family: 'Outfit', sans-serif;">
              Story Writing
            </button>

          </div>

          <!-- INNER PAGES SPREAD 1 (PAGES 01 & 02 - EXACT FONT & LAYOUT MATCH) -->
          <div id="smriti-spread-1" class="w-full bg-[#FAF6EE] rounded-[18px] p-5 md:p-6 relative overflow-hidden text-left h-[495px] md:h-[525px] flex flex-col justify-between" style="background-image: radial-gradient(#D8CFC3 1.2px, transparent 1.2px); background-size: 20px 20px;">
            
            <!-- TOP-RIGHT CLOSE BUTTON '✕' -->
            <button onclick="closeSmritiBook()" class="absolute top-3 right-4 text-gray-500 hover:text-[#6B2137] text-lg font-bold z-40 p-1 transition-colors" title="Close Journal">
              ✕
            </button>

            <!-- Center Spine Stitch Line -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[1.5px] bg-amber-900/15 hidden md:block"></div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-5 md:gap-8 relative z-10 h-full overflow-y-auto md:overflow-hidden">
              
              <!-- PAGE 01: LEFT SIDE -->
              <div class="flex flex-col justify-between text-left pr-0 md:pr-2">
                <div>
                  <!-- Header -->
                  <h3 class="text-3xl md:text-[40px] font-bold text-[#1C1917] mb-0.5 tracking-tight leading-none" style="font-family: 'Outfit', sans-serif;">Shakthi Sri</h3>
                  
                  <!-- Sub-header Pill & Cursive Handwriting -->
                  <div class="flex flex-wrap items-center gap-2.5 mb-3">
                    <span class="px-2.5 py-0.5 bg-[#E8D5CE] text-[#6B2137] text-[9px] font-bold rounded-full border border-[#D9BEB4] tracking-wider uppercase" style="font-family: 'Outfit', sans-serif;">DEVELOPER &amp; RESEARCHER</span>
                    <span class="text-base text-[#2C2C2C] underline underline-offset-2 decoration-amber-900/40" style="font-family: 'Patrick Hand', 'Handlee', cursive;">class of 2026</span>
                  </div>

                  <!-- Timeline List with Icons -->
                  <div class="space-y-1.5 text-xs text-[#2C2C2C] font-medium mb-3" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/20 pb-1">
                      <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                        <svg class="w-3.5 h-3.5 text-[#6B2137]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                        B.Tech Information Technology
                      </span>
                      <span class="text-gray-600">2022 - 2026</span>
                    </div>

                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/20 pb-1">
                      <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                        <svg class="w-3.5 h-3.5 text-[#6B2137]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/></svg>
                        Kingston Engineering College
                      </span>
                      <span class="text-[#6B2137] font-bold">CGPA: 8.6</span>
                    </div>

                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/20 pb-1">
                      <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                        <svg class="w-3.5 h-3.5 text-[#6B2137]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L5.6 15.12a2 2 0 00-1.182.17l-1.04.52a2 2 0 00-.778 2.766l1.54 2.31a2 2 0 002.324.793l2.45-.817a6 6 0 013.79 0l2.45.817a2 2 0 002.324-.793l1.54-2.31a2 2 0 00-.592-2.738z"/></svg>
                        IIT Madras — CYSTAR
                      </span>
                      <span class="text-gray-600">Research Intern</span>
                    </div>

                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/20 pb-1">
                      <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                        <svg class="w-3.5 h-3.5 text-[#6B2137]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/></svg>
                        Full-Stack Developer
                      </span>
                      <span class="text-gray-600">MERN Stack</span>
                    </div>

                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/20 pb-1">
                      <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                        <svg class="w-3.5 h-3.5 text-[#6B2137]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                        Cybersecurity Enthusiast
                      </span>
                      <span class="text-gray-600">Always Learning</span>
                    </div>
                  </div>

                  <!-- Taped Cards Row -->
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 mb-2">
                    
                    <!-- Taped Note: about me ヾ -->
                    <div class="bg-[#F6EFE6] p-3 rounded-xl border border-amber-900/15 shadow-sm relative">
                      <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-7 h-2.5 bg-[#E6D7C3]/90 rotate-[-2deg] border-l border-r border-white/60"></div>
                      <span class="text-base text-[#6B2137] font-bold block mb-0.5" style="font-family: 'Patrick Hand', 'Handlee', cursive;">about me ヾ</span>
                      <ul class="text-[11px] text-[#2C2C2C] leading-tight space-y-0.5" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
                        <li>♥ I love turning ideas into impactful digital solutions.</li>
                        <li>♥ Curious mind driving build &amp; security.</li>
                        <li>♥ Believer in discipline &amp; growth.</li>
                      </ul>
                      <span class="absolute bottom-1 right-2 text-[10px] text-[#6B2137]">♡</span>
                    </div>

                    <!-- TODAY Box -->
                    <div class="bg-[#F6EFE6] p-3 rounded-xl border border-amber-900/15 shadow-sm relative">
                      <div class="flex items-center justify-between mb-0.5">
                        <div class="flex items-center gap-1">
                          <span class="w-1.5 h-1.5 rounded-full bg-rose-400"></span>
                          <span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>
                          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                        </div>
                        <span class="text-[10px] text-amber-900 font-bold">☆</span>
                      </div>
                      <span class="text-[9px] font-mono font-bold text-gray-500 uppercase block mb-0.5">TODAY</span>
                      <p class="text-[11px] text-[#2C2C2C] leading-tight" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
                        Building skills. Solving problems.<br/>Creating solutions.<br/>Preparing for impact.<br/>One step at a time.
                      </p>
                    </div>

                  </div>
                </div>

                <!-- Contact Memo & Quote -->
                <div class="pt-2 border-t border-dashed border-amber-900/20 flex justify-between items-center gap-2">
                  <div class="bg-[#EFE5D8] px-2.5 py-1.5 rounded-lg text-[11px] text-[#2C2C2C] border border-amber-900/15" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
                    <p class="font-bold">srishakthi799@gmail.com</p>
                    <p class="text-gray-600">+91 7895032098</p>
                    <p class="text-gray-500">Chennai | Vellore</p>
                  </div>
                  <div class="text-right">
                    <p class="text-base text-[#541C2E] font-bold leading-tight" style="font-family: 'Great Vibes', cursive;">code with purpose,<br/>create with impact. ♡</p>
                  </div>
                </div>

              </div>

              <!-- PAGE 02: RIGHT SIDE -->
              <div class="flex flex-col justify-between relative text-left pl-0 md:pl-2">
                
                <!-- Top Row -->
                <div class="flex justify-between items-start mb-2">
                  <div class="text-center">
                    <svg class="w-5 h-6 text-[#6B2137] mx-auto" viewBox="0 0 24 32" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 28V12M12 12C9 9 5 10 5 10s1 4 4 5M12 12c3-3 7-2 7-2s-1 4-4 5M12 12c-2-3-1-7-1-7s4 1 4 5"/></svg>
                    <span class="block text-[10px] text-gray-700 mt-0.5" style="font-family: 'Patrick Hand', 'Handlee', cursive;">breathe.png</span>
                  </div>
                  <div class="flex items-center gap-5" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
                    <div class="text-center">
                      <div class="w-7 h-7 bg-[#6B2137]/10 rounded-lg flex items-center justify-center text-[#6B2137] text-xs font-bold mx-auto">
                        <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path d="M2 6a2 2 0 012-2h5l2 2h5a2 2 0 012 2v6a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"/></svg>
                      </div>
                      <span class="block text-[10px] text-gray-600 mt-0.5">Goals</span>
                    </div>
                    <div class="text-center">
                      <div class="w-7 h-7 bg-amber-900/10 rounded-lg flex items-center justify-center text-amber-900 text-xs font-bold mx-auto">
                        <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path d="M4 3a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2H4zm12 12H4l4-8 3 6 2-4 3 6z"/></svg>
                      </div>
                      <span class="block text-[10px] text-gray-600 mt-0.5">Reminders</span>
                    </div>
                  </div>
                </div>

                <!-- Currently Box & Illustration Container -->
                <div class="grid grid-cols-1 sm:grid-cols-12 gap-3 items-center mb-2">
                  
                  <!-- currently ヾ -->
                  <div class="sm:col-span-6 border border-dashed border-amber-900/30 rounded-xl p-3 bg-[#F8F3EA]">
                    <span class="text-base text-[#6B2137] font-bold block mb-1" style="font-family: 'Patrick Hand', 'Handlee', cursive;">currently ヾ</span>
                    <ul class="text-[11px] text-[#2C2C2C] leading-tight space-y-0.5" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
                      <li>♥ Exploring AI &amp; LLMs</li>
                      <li>♥ Building secure systems</li>
                      <li>♥ Deepening full-stack</li>
                      <li>♥ Learning. Shipping.</li>
                      <li>♥ Growing. Always. ♡</li>
                    </ul>
                  </div>

                  <!-- Character Illustration / Photo with @Shakthi.16 Tag -->
                  <div class="sm:col-span-6 flex justify-center relative">
                    <div class="relative">
                      <div class="w-[130px] md:w-[150px] h-[160px] md:h-[180px] rounded-[18px] overflow-hidden shadow-md border-3 border-white bg-white">
                        <img src="girl.png" alt="Shakthi Sri Illustration" class="w-full h-full object-cover"/>
                      </div>
                      <div class="absolute -top-2.5 right-1 bg-[#1A1A1A] text-white font-mono text-[8px] font-bold px-2.5 py-0.5 rounded-full shadow-md z-30">
                        @Shakthi.16
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Tech I Work With -->
                <div class="border border-dashed border-amber-900/30 rounded-xl p-2 bg-[#F8F3EA] mb-2">
                  <span class="text-xs text-[#6B2137] font-bold block mb-1" style="font-family: 'Patrick Hand', 'Handlee', cursive;">tech i work with ヾ</span>
                  
                  <div class="grid grid-cols-7 gap-1.5 items-center text-center text-[9px] font-medium text-gray-700">
                    <div class="flex flex-col items-center">
                      <svg class="w-4 h-4 text-[#61DAFB]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 9a3 3 0 100 6 3 3 0 000-6zm0-7c-5.52 0-10 1.79-10 4s4.48 4 10 4 10-1.79 10-4-4.48-4-10-4zm0 6c-4.41 0-8-1.34-8-2s3.59-2 8-2 8 1.34 8 2-3.59 2-8 2z"/></svg>
                      <span>React.js</span>
                    </div>
                    <div class="flex flex-col items-center">
                      <div class="w-4 h-4 rounded bg-[#339933] text-white text-[8px] font-bold flex items-center justify-center">ncb</div>
                      <span>Node.js</span>
                    </div>
                    <div class="flex flex-col items-center">
                      <span class="font-mono font-bold text-[10px] text-gray-800">ex</span>
                      <span>Express.js</span>
                    </div>
                    <div class="flex flex-col items-center">
                      <svg class="w-4 h-4 text-[#47A248]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 1.5C11.5 3 7 7.5 7 13c0 3 2 5.5 5 6.5 3-1 5-3.5 5-6.5 0-5.5-4.5-10-5-11.5z"/></svg>
                      <span>MongoDB</span>
                    </div>
                    <div class="flex flex-col items-center border-l border-dashed border-amber-900/20 pl-1">
                      <svg class="w-4 h-4 text-[#F24E1E]" fill="currentColor" viewBox="0 0 24 24"><path d="M8 2h4v4H8V2zm0 6h4v4H8V8zm0 6h4v4a4 4 0 11-4-4zm8-12h4v4h-4V2zm0 6h4v4h-4V8z"/></svg>
                      <span>Figma</span>
                    </div>
                    <div class="flex flex-col items-center">
                      <svg class="w-4 h-4 text-[#007ACC]" fill="currentColor" viewBox="0 0 24 24"><path d="M23.15 2.587L18.21.21a1.494 1.494 0 00-1.705.291L7.548 8.69 3.4 5.564a.747.747 0 00-.986.079L.24 7.728a.747.747 0 00-.03.996l3.96 4.67-3.96 4.67a.747.747 0 00.03.996l2.174 2.085a.747.747 0 00.986.079l4.148-3.126 8.957 8.189c.498.455 1.25.412 1.705-.098l4.94-4.757a1.494 1.494 0 00.44-1.077V3.664c0-.406-.164-.796-.44-1.077z"/></svg>
                      <span>VS Code</span>
                    </div>
                    <div class="flex flex-col items-center">
                      <svg class="w-4 h-4 text-black" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C9.5 2 7.5 4 7.5 6.5v4c0 1.5-1 3-2.5 4 0 3 3 5.5 7 5.5s7-2.5 7-5.5c-1.5-1-2.5-2.5-2.5-4v-4C16.5 4 14.5 2 12 2z"/></svg>
                      <span>Linux</span>
                    </div>
                  </div>
                </div>

                <!-- What I Build Box -->
                <div class="grid grid-cols-12 gap-2 items-center">
                  <div class="col-span-9 border border-dashed border-amber-900/30 rounded-xl p-2 bg-[#F8F3EA]">
                    <span class="text-xs text-[#6B2137] font-bold block mb-1 text-center" style="font-family: 'Patrick Hand', 'Handlee', cursive;">what i build ♡</span>
                    <div class="grid grid-cols-3 gap-1.5 text-center text-[10px] font-bold text-gray-800" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
                      <div class="p-1 bg-white/80 rounded-lg border border-amber-900/10 flex items-center justify-center gap-0.5">🌐 Full-Stack Apps</div>
                      <div class="p-1 bg-white/80 rounded-lg border border-amber-900/10 flex items-center justify-center gap-0.5">🔒 Security Tools</div>
                      <div class="p-1 bg-white/80 rounded-lg border border-amber-900/10 flex items-center justify-center gap-0.5">🧠 AI Solutions</div>
                    </div>
                  </div>

                  <!-- Taped Botanical Card -->
                  <div class="col-span-3 bg-[#EFE5D8] p-1.5 rounded-lg border border-amber-900/15 text-center relative shadow-sm">
                    <div class="absolute -top-1.5 left-1/2 -translate-x-1/2 w-5 h-2 bg-[#E6D7C3]/90 rotate-[-2deg]"></div>
                    <svg class="w-4 h-5 text-[#6B2137] mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 22V8M12 8C9 5 5 6 5 6s1 4 4 5M12 8c3-3 7-2 7-2s-1 4-4 5"/></svg>
                  </div>
                </div>

              </div>

            </div>

          </div>

          <!-- INNER PAGES SPREAD 2 (EXACT IMAGE 2 FONT & CREATIVE ARRANGEMENT) -->
          <div id="smriti-spread-2" class="hidden w-full bg-[#FAF6EE] rounded-[18px] p-5 md:p-6 relative overflow-hidden text-left h-[495px] md:h-[525px] flex flex-col justify-between" style="background-image: radial-gradient(#D8CFC3 1.2px, transparent 1.2px); background-size: 20px 20px;">
            
            <!-- TOP-RIGHT CLOSE BUTTON '✕' -->
            <button onclick="closeSmritiBook()" class="absolute top-3 right-4 text-gray-500 hover:text-[#6B2137] text-lg font-bold z-40 p-1 transition-colors" title="Close Journal">
              ✕
            </button>

            <!-- Center Spine Stitch Line -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[1.5px] bg-amber-900/15 hidden md:block"></div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-5 md:gap-8 relative z-10 h-full overflow-y-auto md:overflow-hidden">
              
              <!-- PAGE 03: ON BUILDING. -->
              <div class="flex flex-col justify-between text-left pr-0 md:pr-2">
                <div>
                  <div class="flex items-center gap-2 mb-0.5">
                    <span class="px-1.5 py-0.5 bg-[#E8D5CE] text-[#6B2137] font-bold text-[10px] rounded border border-[#D9BEB4]">03</span>
                    <h3 class="text-2xl md:text-3xl font-bold text-[#1F1F1F]" style="font-family: 'Patrick Hand', 'Handlee', cursive;">On Building. ヾ</h3>
                  </div>
                  <p class="text-[11px] text-gray-500 mb-2" style="font-family: 'Patrick Hand', 'Handlee', cursive;">Journal Entry — 03</p>

                  <p class="text-xs text-[#2C2C2C] leading-tight mb-1.5" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
                    When I first started writing software, I believed engineering was about finding answers.<br/>
                    Over time, I realised it is far more often about <span class="underline underline-offset-2 decoration-amber-900/50 font-bold">asking better questions.</span>
                  </p>

                  <ul class="text-[11px] text-[#2C2C2C] space-y-0.5 mb-2" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
                    <li>♥ What problem actually needs solving?</li>
                    <li>♥ Who will depend on this system tomorrow?</li>
                    <li>♥ What assumptions am I making today that could become failures later?</li>
                  </ul>

                  <p class="text-[11px] text-[#2C2C2C] leading-tight" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
                    The quality of a solution is usually determined long before the first line of code is written.<br/>
                    <span class="underline underline-offset-2 decoration-amber-900/50 font-bold text-[#6B2137]">Good engineering begins with understanding.</span> Everything else follows.
                  </p>
                </div>

                <!-- Taped Quote Note & Bridge Sketch -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 items-center my-1.5">
                  <div class="bg-[#F6EFE6] p-2.5 rounded-xl border border-amber-900/15 shadow-sm text-[11px] text-[#2C2C2C] relative" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
                    <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-6 h-2.5 bg-[#E6D7C3]/90 rotate-[-1deg]"></div>
                    “ If a system becomes difficult to explain, it is usually becoming difficult to maintain. ”
                  </div>

                  <div class="text-center p-1.5 bg-white/60 rounded-xl border border-amber-900/10 shadow-sm">
                    <svg class="w-full h-12 text-[#6B2137]/80" viewBox="0 0 120 40" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M10 35h100M30 10v25M90 10v25M10 25c20-10 40-10 50 0c10-10 30-10 50 0M30 10L10 25M30 10l30 15M90 10l-30 15M90 10l20 15"/><path stroke-linecap="round" stroke-width="0.5" stroke-dasharray="1 1" d="M30 18h60M30 24h60"/></svg>
                  </div>
                </div>

                <!-- Bottom Wire Spiral Note & Reflection -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1.5 border-t border-dashed border-amber-900/20">
                  <div class="bg-[#F8F3EA] p-2.5 rounded-xl border border-amber-900/15 relative pl-6" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
                    <div class="absolute left-1.5 top-1.5 bottom-1.5 flex flex-col justify-between">
                      <div class="w-2 h-2 rounded-full border border-gray-400"></div>
                      <div class="w-2 h-2 rounded-full border border-gray-400"></div>
                      <div class="w-2 h-2 rounded-full border border-gray-400"></div>
                    </div>

                    <p class="font-bold text-[11px] text-[#6B2137] mb-0.5">A small note I often return to</p>
                    <ul class="text-[10px] text-[#2C2C2C] space-y-0.5">
                      <li>👁️ Observe. 💡 Understand.</li>
                      <li>⊖ Reduce. &lt;/&gt; Build.</li>
                      <li>📈 Improve. ↺ Repeat. ♡</li>
                    </ul>
                  </div>

                  <div class="text-left text-[11px] text-[#2C2C2C] flex flex-col justify-between" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
                    <div>
                      <span class="font-bold text-xs text-[#6B2137] block mb-0.5 underline">Reflection</span>
                      <p class="leading-tight">
                        I no longer measure progress by features. I measure it by <span class="bg-[#EFE5D8] px-1 rounded font-bold">how much clearer my thinking becomes</span>. ☆
                      </p>
                    </div>
                  </div>
                </div>

              </div>

              <!-- PAGE 04: THINGS I'VE LEARNED. ♡ -->
              <div class="flex flex-col justify-between text-left pl-0 md:pl-2">
                <div>
                  <div class="flex items-center justify-between mb-1.5">
                    <div>
                      <h3 class="text-2xl md:text-3xl font-bold text-[#1F1F1F]" style="font-family: 'Patrick Hand', 'Handlee', cursive;">Things I've Learned. ♡</h3>
                      <div class="w-20 h-0.5 bg-[#6B2137]/40 rounded-full"></div>
                    </div>
                    <span class="px-1.5 py-0.5 bg-[#E8D5CE] text-[#6B2137] font-bold text-[10px] rounded border border-[#D9BEB4]">04</span>
                  </div>

                  <div class="space-y-2 text-[11px] text-[#2C2C2C] mb-2" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
                    <div class="flex items-start gap-2">
                      <div class="w-6 h-6 rounded-full bg-[#EFE5D8] border border-amber-900/20 flex items-center justify-center text-[10px] font-bold text-[#6B2137] shrink-0 mt-0.5">&lt;/&gt;</div>
                      <div>
                        <h4 class="font-bold text-xs text-[#1F1F1F]">The best code usually disappears.</h4>
                        <p class="text-gray-600 leading-tight">Users remember experiences. Developers remember implementations. Good engineering satisfies both. ♡</p>
                      </div>
                    </div>

                    <div class="flex items-start gap-2">
                      <div class="w-6 h-6 rounded-full bg-[#EFE5D8] border border-amber-900/20 flex items-center justify-center text-[10px] font-bold text-[#6B2137] shrink-0 mt-0.5">🕒</div>
                      <div>
                        <h4 class="font-bold text-xs text-[#1F1F1F]">Speed is temporary.</h4>
                        <p class="text-gray-600 leading-tight">Maintainability is permanent. Every shortcut introduces interest that someone must repay.</p>
                      </div>
                    </div>

                    <div class="flex items-start gap-2">
                      <div class="w-6 h-6 rounded-full bg-[#EFE5D8] border border-amber-900/20 flex items-center justify-center text-[10px] font-bold text-[#6B2137] shrink-0 mt-0.5">📄</div>
                      <div>
                        <h4 class="font-bold text-xs text-[#1F1F1F]">Documentation is respect.</h4>
                        <p class="text-gray-600 leading-tight">For teammates, future contributors, and yourself 6 months later. ☆</p>
                      </div>
                    </div>

                    <div class="flex items-start gap-2">
                      <div class="w-6 h-6 rounded-full bg-[#EFE5D8] border border-amber-900/20 flex items-center justify-center text-[10px] font-bold text-[#6B2137] shrink-0 mt-0.5">🌱</div>
                      <div>
                        <h4 class="font-bold text-xs text-[#1F1F1F]">Learning is never finished.</h4>
                        <p class="text-gray-600 leading-tight">Tools change. Curiosity should not. ♡</p>
                      </div>
                    </div>
                  </div>

                  <div class="p-2.5 bg-[#F6EFE6] rounded-xl border border-amber-900/15 text-[11px] text-[#2C2C2C] text-center mb-2 relative shadow-sm" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
                    <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-7 h-2.5 bg-[#E6D7C3]/90 rotate-[1deg]"></div>
                    Every completed project leaves behind a better engineer than the one who started it. 🌸
                  </div>
                </div>

                <div class="pt-1.5 border-t border-dashed border-amber-900/20">
                  <h4 class="font-bold text-sm text-[#1F1F1F] mb-0.5" style="font-family: 'Patrick Hand', 'Handlee', cursive;">Working With Others. 👥</h4>
                  <p class="text-[10.5px] text-gray-600 leading-tight mb-1" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
                    Some contributions improve communication, simplify decisions, and prevent mistakes.
                  </p>

                  <div class="bg-[#F6EFE6] p-2 rounded-lg border border-amber-900/15 text-[10.5px] text-[#2C2C2C] text-center mb-1" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
                    "The most valuable work is often the work no one notices because everything functions as expected. ♡"
                  </div>

                  <ul class="text-[10.5px] text-[#2C2C2C] space-y-0.5" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
                    <li>♥ Showing up prepared.</li>
                    <li>♥ Writing clearly.</li>
                    <li>♥ Listening carefully.</li>
                    <li>♥ Accepting feedback without defending ego.</li>
                  </ul>
                </div>

              </div>

            </div>

          </div>

          <!-- INNER PAGES SPREAD 3 -->
          <div id="smriti-spread-3" class="hidden w-full bg-[#FAF6EE] rounded-[18px] p-5 md:p-6 relative overflow-hidden text-left h-[495px] md:h-[525px] flex flex-col justify-between" style="background-image: radial-gradient(#D8CFC3 1.2px, transparent 1.2px); background-size: 20px 20px;">
            <button onclick="closeSmritiBook()" class="absolute top-3 right-4 text-gray-500 hover:text-[#6B2137] text-lg font-bold z-40 p-1 transition-colors" title="Close Journal">
              ✕
            </button>
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[1.5px] bg-amber-900/15 hidden md:block"></div>
            <div class="flex flex-col items-center justify-center h-full text-center p-6">
              <span class="text-4xl mb-3">✍️</span>
              <h3 class="text-3xl font-bold text-[#1F1F1F] mb-2" style="font-family: 'Great Vibes', cursive;">Story Writing</h3>
              <p class="text-base text-gray-700 max-w-md" style="font-family: 'Patrick Hand', 'Handlee', cursive;">
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
  <svg class="w-full h-7 md:h-10 text-white fill-current block" viewBox="0 0 1200 80" preserveAspectRatio="none">
    <path d="M0,0 L15,9 L30,3 L45,12 L60,5 L75,10 L90,2 L105,8 L120,4 L135,13 L150,7 L165,11 L180,2 L195,9 L210,4 L225,12 L240,6 L255,10 L270,3 L285,9 L300,5 L315,11 L330,2 L345,10 L360,4 L375,12 L390,6 L405,9 L420,3 L435,11 L450,5 L465,10 L480,2 L495,9 L510,4 L525,13 L540,7 L555,11 L570,3 L585,10 L600,4 L615,12 L630,6 L645,9 L660,3 L675,11 L690,5 L705,10 L720,2 L735,9 L750,4 L765,13 L780,7 L795,11 L810,3 L825,10 L840,4 L855,12 L870,6 L885,9 L900,3 L915,11 L930,5 L945,10 L960,2 L1005,13 L1020,7 L1035,11 L1050,3 L1065,10 L1080,4 L1095,12 L1110,6 L1125,9 L1140,3 L1155,11 L1170,5 L1185,10 L1200,2 L1200,80 L0,80 Z"></path>
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
    content = content[:start_pos] + CREATIVE_JOURNAL_HTML + '\n\n' + content[end_pos:]
    print("Successfully built exact creative arrangement with Patrick Hand/Handlee font and Great Vibes accents!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
