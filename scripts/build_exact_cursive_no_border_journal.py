import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# -------------------------------------------------------------
# GOOGLE FONTS IMPORT (CAVEAT & PATRICK HAND FOR AUTHENTIC CURSIVE HANDWRITING)
# -------------------------------------------------------------
FONT_IMPORT = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@400..700&family=Patrick+Hand&family=Reenie+Beanie&display=swap" rel="stylesheet">"""

if 'Caveat' not in content:
    content = content.replace('</head>', FONT_IMPORT + '\n</head>')

# -------------------------------------------------------------
# EXACT 100% REPLICATION OF USER'S ATTACHED IMAGES 1 & 2:
# 1. AUTHENTIC CURSIVE & MANUSCRIPT HANDWRITING TYPOGRAPHY (Caveat / Patrick Hand font)
# 2. BORDER NO! (Sleek 0px padding, edge border only)
# 3. 100% BRAND LOGOS & CLEAN SPACING
# -------------------------------------------------------------
CURSIVE_NO_BORDER_JOURNAL_HTML = """<!-- REALISTIC DECKLE-EDGE TORN PAPER SEPARATION DIVIDER (TOP) -->
<div class="w-full relative z-20 pointer-events-none -mb-1 bg-white">
  <svg class="w-full h-7 md:h-11 text-[#f4efe6] fill-current block" viewBox="0 0 1200 80" preserveAspectRatio="none">
    <path d="M0,0 L0,35 L15,38 L30,32 L45,41 L60,34 L75,39 L90,31 L105,37 L120,33 L135,42 L150,36 L165,40 L180,31 L195,38 L210,33 L225,41 L240,35 L255,39 L270,32 L285,38 L300,34 L315,40 L330,31 L345,39 L360,33 L375,41 L390,35 L405,38 L420,32 L435,40 L450,34 L465,39 L480,31 L495,38 L510,33 L525,42 L540,36 L555,40 L570,32 L585,39 L600,33 L615,41 L630,35 L645,38 L660,32 L675,40 L690,34 L705,39 L720,31 L735,38 L750,33 L765,42 L780,36 L795,40 L810,32 L825,39 L840,33 L855,41 L870,35 L885,38 L900,32 L915,40 L930,34 L945,39 L960,31 L975,38 L990,33 L1005,42 L1020,36 L1035,40 L1050,32 L1065,39 L1080,33 L1095,41 L1110,35 L1125,38 L1140,32 L1155,40 L1170,34 L1185,39 L1200,31 L1200,80 L0,80 Z"></path>
  </svg>
</div>

<!-- ABOUT ME: PHYSICAL SMRITI RAWAT STYLE JOURNAL BOOK -->
<section class="relative bg-[#f4efe6] text-[#1F1F1F] py-8 md:py-12 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal" style="font-family: 'Caveat', 'Patrick Hand', cursive;">
  <div class="max-w-7xl mx-auto px-4 md:px-8 text-center">
    
    <!-- Title Header -->
    <div class="mb-6 font-sans">
      <span class="text-[11px] uppercase tracking-[0.3em] text-[#8b2252] font-mono font-bold block mb-1">ABOUT ME</span>
      <h2 class="text-3xl md:text-5xl font-bold font-serif italic text-[#1F1F1F]">The Personal Journal</h2>
    </div>

    <!-- BOOK STAGE CONTAINER (CONSTRAINED VIEWPORT HEIGHT) -->
    <div class="relative w-full max-w-[1000px] mx-auto min-h-[530px] md:min-h-[560px] flex items-center justify-center">

      <!-- ==================== CLOSED BOOK COVER STATE ==================== -->
      <div id="smriti-book-cover" class="cursor-pointer transition-all duration-500 z-40 group" onclick="openSmritiBook()">
        <div class="relative">
          <!-- Cover Book Image -->
          <div class="w-[310px] md:w-[410px] h-[510px] md:h-[540px] rounded-[24px] shadow-[0_25px_65px_-15px_rgba(0,0,0,0.32)] overflow-hidden relative bg-[#36132b] border border-amber-900/30">
            <img src="cover.png" alt="Shakthi Sri Journal Cover" class="w-full h-full object-cover block"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/20 via-transparent to-transparent pointer-events-none"></div>
          </div>
          <!-- Spine Bookmark Ribbon -->
          <div class="w-6 h-12 bg-[#55826b] rounded-b-md shadow-md absolute -bottom-5 left-10 pointer-events-none"></div>
        </div>
      </div>

      <!-- ==================== OPENED PHYSICAL HARDCOVER BOOK ==================== -->
      <div id="smriti-book-opened" class="hidden w-full transition-opacity duration-500 opacity-0 z-30">
        
        <!-- SLEEK BOOK CONTAINER: BORDER NO! (0px PADDING, SLEEK 1px OUTER BORDER) -->
        <div class="relative w-full rounded-[22px] shadow-[0_25px_70px_-15px_rgba(0,0,0,0.30)] border border-[#36132b]/80 bg-[#36132b] p-[1.5px]">
          
          <!-- OUTSIDE RIGHT VERTICAL INDEX TABS (EXACT MATCH TO IMAGE 1) -->
          <div class="absolute top-6 -right-9 md:-right-11 flex flex-col gap-2 z-50 font-sans">
            
            <!-- Home / Cover Tab -->
            <button onclick="closeSmritiBook()" class="w-9 md:w-11 h-10 bg-[#ebdcc4] hover:bg-[#8b2252] text-gray-800 hover:text-white rounded-r-xl shadow-lg border-t border-r border-b border-amber-900/20 flex items-center justify-center transition-all hover:translate-x-1" title="Close to Cover">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001-1.414-1.414l-7-7z"/></svg>
            </button>

            <!-- Tab 1: About Me (P. 01-02) -->
            <button id="tab-btn-spread1" onclick="switchSmritiSpread('spread1')" class="px-2 md:px-2.5 py-4 bg-[#421835] text-white text-[11px] font-mono font-bold rounded-r-xl shadow-lg border-t border-r border-b border-amber-900/30 flex items-center justify-center transition-all hover:translate-x-1" style="writing-mode: vertical-rl; text-orientation: mixed;">
              About Me
            </button>

            <!-- Tab 2: Things I Learnt (P. 03-04) -->
            <button id="tab-btn-spread2" onclick="switchSmritiSpread('spread2')" class="px-2 md:px-2.5 py-4 bg-[#9b6b78] hover:bg-[#421835] text-white text-[11px] font-mono font-bold rounded-r-xl shadow-lg border-t border-r border-b border-amber-900/30 flex items-center justify-center transition-all hover:translate-x-1" style="writing-mode: vertical-rl; text-orientation: mixed;">
              Things I Learnt
            </button>

            <!-- Tab 3: Story Writing -->
            <button id="tab-btn-spread3" onclick="switchSmritiSpread('spread3')" class="px-2 md:px-2.5 py-4 bg-[#c2a297] hover:bg-[#421835] text-white text-[11px] font-mono font-bold rounded-r-xl shadow-lg border-t border-r border-b border-amber-900/30 flex items-center justify-center transition-all hover:translate-x-1 hidden sm:flex" style="writing-mode: vertical-rl; text-orientation: mixed;">
              Story Writing
            </button>

          </div>

          <!-- INNER PAGES SPREAD 1 (PAGES 01 & 02 - EXACT REPLICA OF IMAGE 2 WITH CURSIVE FONTS) -->
          <div id="smriti-spread-1" class="w-full bg-[#faf6ee] rounded-[20px] p-6 md:p-8 relative overflow-hidden text-left h-[510px] md:h-[535px] flex flex-col justify-between" style="background-image: radial-gradient(#d6cebe 1.2px, transparent 1.2px); background-size: 20px 20px;">
            
            <!-- TOP-RIGHT CLOSE BUTTON '✕' -->
            <button onclick="closeSmritiBook()" class="absolute top-4 right-5 text-gray-500 hover:text-[#8b2252] text-xl font-bold z-40 p-1 transition-colors" title="Close Journal">
              ✕
            </button>

            <!-- Center Spine Stitch Line -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[2px] bg-amber-900/15 hidden md:block"></div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-12 relative z-10 h-full overflow-y-auto md:overflow-hidden">
              
              <!-- PAGE 01: LEFT SIDE (IMAGE 2 EXACT REPLICA) -->
              <div class="flex flex-col justify-between text-left pr-0 md:pr-2">
                <div>
                  <h3 class="text-4xl md:text-5xl font-bold text-[#1F1F1F] mb-1 tracking-tight font-sans">Shakthi Sri</h3>
                  
                  <!-- Pill Badges -->
                  <div class="flex flex-wrap items-center gap-2 mb-3 font-sans">
                    <span class="px-3 py-0.5 bg-[#f0e3db] text-[#8b2252] text-[10px] font-mono font-bold rounded-full border border-[#d8c2b5] tracking-wider uppercase">DEVELOPER &amp; RESEARCHER</span>
                    <span class="text-sm text-gray-700 underline decoration-amber-900/30" style="font-family: 'Caveat', cursive;">class of 2026</span>
                  </div>

                  <!-- Timeline List with Icons (IMAGE 2 EXACT MATCH) -->
                  <div class="space-y-2 font-mono text-[11px] text-gray-800 font-medium mb-3">
                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-1">
                      <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                        💻 B.Tech Information Technology
                      </span>
                      <span class="text-gray-600">2022 - 2026</span>
                    </div>

                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-1">
                      <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                        🎓 Kingston Engineering College
                      </span>
                      <span class="text-[#8b2252] font-bold">CGPA: 8.6</span>
                    </div>

                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-1">
                      <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                        🧪 IIT Madras — CYSTAR
                      </span>
                      <span class="text-gray-600">Research Intern</span>
                    </div>

                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-1">
                      <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                        &lt;/&gt; Full-Stack Developer
                      </span>
                      <span class="text-gray-600">MERN Stack</span>
                    </div>

                    <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-1">
                      <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">
                        🛡️ Cybersecurity Enthusiast
                      </span>
                      <span class="text-gray-600">Always Learning</span>
                    </div>
                  </div>

                  <!-- Taped Cards Row (IMAGE 2 EXACT SPEC) -->
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 mb-2">
                    
                    <!-- Taped Note: about me ヾ -->
                    <div class="bg-[#f7f0e6] p-3 rounded-2xl border border-amber-900/15 shadow-sm relative">
                      <div class="absolute -top-2.5 left-1/2 -translate-x-1/2 w-7 h-3 bg-amber-200/80 rotate-[-2deg] border-l border-r border-white/60"></div>
                      <span class="text-sm text-[#8b2252] font-bold block mb-1" style="font-family: 'Caveat', cursive;">about me ヾ</span>
                      <ul class="text-[11px] text-gray-800 leading-snug space-y-1" style="font-family: 'Patrick Hand', cursive;">
                        <li>♥ I love turning ideas into impactful digital solutions.</li>
                        <li>♥ Curious mind with a strong drive to build, secure and innovate.</li>
                        <li>♥ Believer in discipline, consistency &amp; growth. ♡</li>
                      </ul>
                    </div>

                    <!-- TODAY Box with 3 colored dots & star -->
                    <div class="bg-[#f7f0e6] p-3 rounded-2xl border border-amber-900/15 shadow-sm relative">
                      <div class="flex items-center justify-between mb-1">
                        <div class="flex items-center gap-1">
                          <span class="w-1.5 h-1.5 rounded-full bg-rose-400"></span>
                          <span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>
                          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                        </div>
                        <span class="text-xs text-amber-900 font-sans">☆</span>
                      </div>
                      <span class="text-[9px] font-mono font-bold text-gray-500 uppercase block mb-0.5">TODAY</span>
                      <p class="text-[11px] text-gray-800 leading-relaxed" style="font-family: 'Patrick Hand', cursive;">
                        Building skills.<br/>Solving problems.<br/>Creating solutions.<br/>Preparing for impact.<br/>One step at a time.
                      </p>
                    </div>

                  </div>
                </div>

                <!-- Contact Memo & Quote (IMAGE 2 EXACT SPEC) -->
                <div class="pt-2 border-t border-dashed border-amber-900/20 flex justify-between items-center gap-2">
                  <div class="bg-[#f0e8dc] px-2.5 py-1.5 rounded-xl text-[10px] font-mono text-gray-800 border border-amber-900/15">
                    <p class="font-bold">srishakthi799@gmail.com</p>
                    <p class="text-gray-600">+91 7895032098</p>
                    <p class="text-gray-500">Chennai | Vellore</p>
                  </div>
                  <div class="text-right">
                    <p class="text-sm text-[#421835] font-bold leading-tight" style="font-family: 'Caveat', cursive;">“ code with purpose,<br/>create with impact. ♡</p>
                    <div class="w-12 h-0.5 bg-[#421835]/40 ml-auto mt-0.5"></div>
                  </div>
                </div>

              </div>

              <!-- PAGE 02: RIGHT SIDE (IMAGE 2 EXACT REPLICA) -->
              <div class="flex flex-col justify-between relative text-left pl-0 md:pl-2">
                
                <!-- Top Row: Breathe doodle, Goals, Reminders -->
                <div class="flex justify-between items-start mb-2 font-sans">
                  <div class="text-center">
                    <span class="text-xl">🌸</span>
                    <span class="block text-[9px] font-serif italic text-gray-600">breathe.png</span>
                  </div>
                  <div class="flex items-center gap-4">
                    <div class="text-center">
                      <div class="w-7 h-7 bg-[#8b2252]/10 rounded-lg flex items-center justify-center text-[#8b2252] text-xs font-bold mx-auto">📁</div>
                      <span class="block text-[8px] font-mono text-gray-600 mt-0.5">Goals</span>
                    </div>
                    <div class="text-center">
                      <div class="w-7 h-7 bg-amber-900/10 rounded-lg flex items-center justify-center text-amber-900 text-xs font-bold mx-auto">💾</div>
                      <span class="block text-[8px] font-mono text-gray-600 mt-0.5">Reminders</span>
                    </div>
                  </div>
                </div>

                <!-- Currently Box & Photo Container -->
                <div class="grid grid-cols-1 sm:grid-cols-12 gap-3 items-center mb-3">
                  
                  <!-- currently ヾ -->
                  <div class="sm:col-span-6 border border-dashed border-amber-900/30 rounded-2xl p-3 bg-[#fbf7f0]">
                    <span class="text-xs text-[#8b2252] font-bold block mb-1" style="font-family: 'Caveat', cursive;">currently ヾ</span>
                    <ul class="text-[11px] text-gray-800 leading-snug space-y-0.5" style="font-family: 'Patrick Hand', cursive;">
                      <li>♥ Exploring AI &amp; LLMs</li>
                      <li>♥ Building secure systems</li>
                      <li>♥ Deepening full-stack</li>
                      <li>♥ Learning. Shipping.</li>
                      <li>♥ Growing. Always. ♡</li>
                    </ul>
                  </div>

                  <!-- Photo me.png with @Shakthi.16 Badge -->
                  <div class="sm:col-span-6 flex justify-center relative">
                    <div class="relative">
                      <div class="w-[140px] md:w-[160px] h-[170px] md:h-[190px] rounded-[18px] overflow-hidden shadow-md border-4 border-white">
                        <img src="me.png" alt="Shakthi Sri" class="w-full h-full object-cover"/>
                      </div>
                      <div class="absolute -top-2.5 right-0 bg-black/80 text-white font-mono text-[8px] font-bold px-2.5 py-0.5 rounded-full shadow-md z-30">
                        @Shakthi.16
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Tech I Work With (IMAGE 2 EXACT BRAND LOGOS) -->
                <div class="border border-dashed border-amber-900/30 rounded-2xl p-2.5 bg-[#fbf7f0] mb-2">
                  <span class="text-xs text-[#8b2252] font-bold block mb-1.5" style="font-family: 'Caveat', cursive;">tech i work with ヾ</span>
                  <div class="flex flex-wrap items-center justify-between gap-2 text-center font-sans">
                    <div class="text-center">
                      <svg class="w-4 h-4 text-[#61dafb] mx-auto mb-0.5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 9a3 3 0 100 6 3 3 0 000-6zm0-7c-5.52 0-10 1.79-10 4s4.48 4 10 4 10-1.79 10-4-4.48-4-10-4zm0 6c-4.41 0-8-1.34-8-2s3.59-2 8-2 8 1.34 8 2-3.59 2-8 2z"/></svg>
                      <span class="block text-[8px] font-mono text-gray-700">React.js</span>
                    </div>
                    <div class="text-center">
                      <svg class="w-4 h-4 text-[#339933] mx-auto mb-0.5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2L2 7.5v9L12 22l10-5.5v-9L12 2zm0 2.3l7.5 4.1-7.5 4.1-7.5-4.1L12 4.3z"/></svg>
                      <span class="block text-[8px] font-mono text-gray-700">Node.js</span>
                    </div>
                    <div class="text-center">
                      <span class="block font-bold text-xs text-gray-700">ex</span>
                      <span class="block text-[8px] font-mono text-gray-700">Express.js</span>
                    </div>
                    <div class="text-center">
                      <svg class="w-4 h-4 text-[#47A248] mx-auto mb-0.5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 1.5C11.5 3 7 7.5 7 13c0 3 2 5.5 5 6.5 3-1 5-3.5 5-6.5 0-5.5-4.5-10-5-11.5z"/></svg>
                      <span class="block text-[8px] font-mono text-gray-700">MongoDB</span>
                    </div>
                    <div class="text-center">
                      <svg class="w-4 h-4 text-[#F24E1E] mx-auto mb-0.5" fill="currentColor" viewBox="0 0 24 24"><path d="M8 2h4v4H8V2zm0 6h4v4H8V8zm0 6h4v4a4 4 0 11-4-4zm8-12h4v4h-4V2zm0 6h4v4h-4V8z"/></svg>
                      <span class="block text-[8px] font-mono text-gray-700">Figma</span>
                    </div>
                    <div class="text-center">
                      <svg class="w-4 h-4 text-[#007ACC] mx-auto mb-0.5" fill="currentColor" viewBox="0 0 24 24"><path d="M23.15 2.587L18.21.21a1.494 1.494 0 00-1.705.291L7.548 8.69 3.4 5.564a.747.747 0 00-.986.079L.24 7.728a.747.747 0 00-.03.996l3.96 4.67-3.96 4.67a.747.747 0 00.03.996l2.174 2.085a.747.747 0 00.986.079l4.148-3.126 8.957 8.189c.498.455 1.25.412 1.705-.098l4.94-4.757a1.494 1.494 0 00.44-1.077V3.664c0-.406-.164-.796-.44-1.077z"/></svg>
                      <span class="block text-[8px] font-mono text-gray-700">VS Code</span>
                    </div>
                    <div class="text-center">
                      <svg class="w-4 h-4 text-black mx-auto mb-0.5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C9.5 2 7.5 4 7.5 6.5v4c0 1.5-1 3-2.5 4 0 3 3 5.5 7 5.5s7-2.5 7-5.5c-1.5-1-2.5-2.5-2.5-4v-4C16.5 4 14.5 2 12 2z"/></svg>
                      <span class="block text-[8px] font-mono text-gray-700">Linux</span>
                    </div>
                  </div>
                </div>

                <!-- What I Build Box -->
                <div class="border border-dashed border-amber-900/30 rounded-2xl p-2 bg-[#fbf7f0] relative">
                  <span class="text-xs text-[#8b2252] font-bold block mb-1 text-center" style="font-family: 'Caveat', cursive;">what i build ♡</span>
                  <div class="grid grid-cols-3 gap-1.5 text-center text-[9px] font-mono text-gray-700 font-bold font-sans">
                    <div class="p-1 bg-white/80 rounded-lg border border-amber-900/10 flex items-center justify-center gap-1">🌐 Full-Stack Web Applications</div>
                    <div class="p-1 bg-white/80 rounded-lg border border-amber-900/10 flex items-center justify-center gap-1">🔒 Cybersecurity Tools &amp; Research</div>
                    <div class="p-1 bg-white/80 rounded-lg border border-amber-900/10 flex items-center justify-center gap-1">🧠 AI-Enhanced Solutions</div>
                  </div>
                </div>

              </div>

            </div>

          </div>

          <!-- INNER PAGES SPREAD 2 (PAGES 03 & 04 - EXACT REPLICA OF IMAGE 1 WITH CURSIVE FONTS) -->
          <div id="smriti-spread-2" class="hidden w-full bg-[#faf6ee] rounded-[20px] p-6 md:p-8 relative overflow-hidden text-left h-[510px] md:h-[535px] flex flex-col justify-between" style="background-image: radial-gradient(#d6cebe 1.2px, transparent 1.2px); background-size: 20px 20px;">
            
            <!-- TOP-RIGHT CLOSE BUTTON '✕' -->
            <button onclick="closeSmritiBook()" class="absolute top-4 right-5 text-gray-500 hover:text-[#8b2252] text-xl font-bold z-40 p-1 transition-colors" title="Close Journal">
              ✕
            </button>

            <!-- Center Spine Line -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[2px] bg-amber-900/15 hidden md:block"></div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-12 relative z-10 h-full overflow-y-auto md:overflow-hidden">
              
              <!-- PAGE 03: ON BUILDING. JOURNAL ENTRY 03 (IMAGE 1 MATCH) -->
              <div class="space-y-2 text-left pr-0 md:pr-2 flex flex-col justify-between">
                <div>
                  <div class="flex items-center gap-2 mb-1 font-sans">
                    <span class="px-1.5 py-0.5 bg-[#f0e3db] text-[#8b2252] font-mono font-bold text-[9px] rounded border border-amber-900/20">03</span>
                    <div>
                      <h3 class="text-2xl md:text-3xl font-bold text-[#1F1F1F] leading-tight" style="font-family: 'Patrick Hand', cursive;">On Building. ヾ</h3>
                      <p class="text-[10px] font-mono text-gray-600" style="font-family: 'Caveat', cursive;">Journal Entry — 03</p>
                    </div>
                  </div>

                  <p class="text-[11px] text-gray-800 leading-relaxed mb-2" style="font-family: 'Patrick Hand', cursive;">
                    When I first started writing software, I believed engineering was about finding answers.<br/>
                    Over time, I realised it is far more often about <span class="underline decoration-amber-900/40 font-bold">asking better questions.</span>
                  </p>

                  <ul class="text-[10.5px] text-gray-800 space-y-0.5 mb-2" style="font-family: 'Patrick Hand', cursive;">
                    <li>♥ What problem actually needs solving?</li>
                    <li>♥ Who will depend on this system tomorrow?</li>
                    <li>♥ What assumptions am I making today that could become failures later?</li>
                  </ul>

                  <p class="text-[11px] text-gray-800 leading-relaxed mb-2" style="font-family: 'Patrick Hand', cursive;">
                    The quality of a solution is usually determined long before the first line of code is written.<br/>
                    <span class="underline decoration-amber-900/40 font-bold text-[#8b2252]">Good engineering begins with understanding.</span> Everything else follows.
                  </p>
                </div>

                <!-- Middle Taped Quote Card & Bridge Sketch -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 items-center my-1">
                  <div class="bg-[#f7f0e6] p-2.5 rounded-xl border border-amber-900/15 text-[10px] text-gray-800 relative" style="font-family: 'Caveat', cursive;">
                    <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-6 h-2 bg-amber-200/80 rotate-[-1deg]"></div>
                    “ If a system becomes difficult to explain, it is usually becoming difficult to maintain. ”
                  </div>
                  <div class="text-center font-sans">
                    <div class="w-full h-12 bg-amber-900/5 rounded-xl border border-dashed border-amber-900/20 flex items-center justify-center text-[9px] italic text-gray-500" style="font-family: 'Caveat', cursive;">
                      🌉 Bridge Illustration Sketch
                    </div>
                  </div>
                </div>

                <!-- Bottom Spiral Note & Reflection -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1 border-t border-dashed border-amber-900/20">
                  <div class="bg-[#fbf7f0] p-2 rounded-xl border border-amber-900/15 text-[10px] text-gray-800" style="font-family: 'Patrick Hand', cursive;">
                    <p class="font-bold text-[#8b2252] mb-0.5">A small note I often return to:</p>
                    <ul class="space-y-0.5">
                      <li>👁️ Observe.</li>
                      <li>💡 Understand.</li>
                      <li>⊖ Reduce.</li>
                      <li>&lt;/&gt; Build.</li>
                      <li>📈 Improve.</li>
                      <li>↻ Repeat. ♡</li>
                    </ul>
                  </div>

                  <div class="text-left text-[10px] text-gray-800 flex flex-col justify-between" style="font-family: 'Caveat', cursive;">
                    <span class="font-bold text-[#421835] block mb-0.5 text-xs">Reflection</span>
                    <p class="text-gray-700 leading-tight">
                      I no longer measure progress by the number of features I complete. I measure it by <span class="bg-amber-100 px-1 rounded">how much clearer my thinking becomes</span> after each project. ☆
                    </p>
                  </div>
                </div>

              </div>

              <!-- PAGE 04: THINGS I'VE LEARNED. ♡ (IMAGE 1 MATCH) -->
              <div class="space-y-2 text-left pl-0 md:pl-2 flex flex-col justify-between">
                <div>
                  <div class="flex items-center justify-between mb-2">
                    <div class="flex items-center gap-2 font-sans">
                      <span class="px-1.5 py-0.5 bg-[#f0e3db] text-[#8b2252] font-mono font-bold text-[9px] rounded border border-amber-900/20">04</span>
                      <h3 class="text-2xl md:text-3xl font-bold text-[#1F1F1F]" style="font-family: 'Patrick Hand', cursive;">Things I've Learned. ♡</h3>
                    </div>
                  </div>

                  <!-- 4 Circle Icon Items (IMAGE 1 SPEC) -->
                  <div class="space-y-1.5 text-[10.5px] text-gray-800 mb-3" style="font-family: 'Patrick Hand', cursive;">
                    <div class="flex items-start gap-2">
                      <div class="w-6 h-6 rounded-full bg-amber-900/10 flex items-center justify-center text-[10px] font-mono font-bold text-[#8b2252] shrink-0 mt-0.5 font-sans">&lt;/&gt;</div>
                      <div>
                        <h4 class="font-bold text-[#421835] text-xs">The best code usually disappears.</h4>
                        <p class="text-gray-600 leading-tight">Users remember experiences. Developers remember implementations. Good engineering satisfies both. ♡</p>
                      </div>
                    </div>

                    <div class="flex items-start gap-2">
                      <div class="w-6 h-6 rounded-full bg-amber-900/10 flex items-center justify-center text-[10px] font-mono font-bold text-[#8b2252] shrink-0 mt-0.5 font-sans">🕒</div>
                      <div>
                        <h4 class="font-bold text-[#421835] text-xs">Speed is temporary.</h4>
                        <p class="text-gray-600 leading-tight">Maintainability is permanent. Every shortcut eventually introduces interest that someone must repay.</p>
                      </div>
                    </div>

                    <div class="flex items-start gap-2">
                      <div class="w-6 h-6 rounded-full bg-amber-900/10 flex items-center justify-center text-[10px] font-mono font-bold text-[#8b2252] shrink-0 mt-0.5 font-sans">📄</div>
                      <div>
                        <h4 class="font-bold text-[#421835] text-xs">Documentation is an act of respect.</h4>
                        <p class="text-gray-600 leading-tight">For teammates. For future contributors. For the version of yourself who returns six months later. ☆</p>
                      </div>
                    </div>

                    <div class="flex items-start gap-2">
                      <div class="w-6 h-6 rounded-full bg-amber-900/10 flex items-center justify-center text-[10px] font-mono font-bold text-[#8b2252] shrink-0 mt-0.5 font-sans">🌱</div>
                      <div>
                        <h4 class="font-bold text-[#421835] text-xs">Learning is never finished.</h4>
                        <p class="text-gray-600 leading-tight">Technology changes. Tools change. Expectations change. Curiosity should not. ♡</p>
                      </div>
                    </div>
                  </div>

                  <!-- Taped Bottom Note Card -->
                  <div class="p-2 bg-[#f7f0e6] rounded-xl border border-amber-900/15 text-[10px] text-gray-800 text-center mb-2 relative" style="font-family: 'Caveat', cursive;">
                    <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-6 h-2 bg-amber-200/80 rotate-[1deg]"></div>
                    Every completed project leaves behind more than software. It leaves behind a better engineer than the one who started it. 🌸
                  </div>
                </div>

                <!-- Right Column: Working With Others. 👥 -->
                <div class="pt-2 border-t border-dashed border-amber-900/20">
                  <div class="flex items-center justify-between mb-1">
                    <h4 class="font-bold text-sm text-[#421835]" style="font-family: 'Patrick Hand', cursive;">Working With Others. 👥</h4>
                  </div>

                  <p class="text-[10px] text-gray-700 leading-tight mb-1.5" style="font-family: 'Patrick Hand', cursive;">
                    Not every contribution is visible in a commit history. Some improve communication. Some simplify decisions. Some prevent mistakes before they happen.
                  </p>

                  <!-- Taped Note: Most valuable work -->
                  <div class="bg-[#f7f0e6] p-1.5 rounded-lg border border-amber-900/15 text-[9.5px] text-gray-800 text-center mb-1.5" style="font-family: 'Caveat', cursive;">
                    "The most valuable work is often the work no one notices because everything simply functions as expected. ♡"
                  </div>

                  <ul class="text-[9.5px] text-gray-800 space-y-0.5" style="font-family: 'Patrick Hand', cursive;">
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

          <!-- INNER PAGES SPREAD 3 (PAGES 05 & 06 - STORY WRITING PLACEHOLDER) -->
          <div id="smriti-spread-3" class="hidden w-full bg-[#faf6ee] rounded-[20px] p-6 md:p-8 relative overflow-hidden text-left h-[510px] md:h-[535px] flex flex-col justify-between" style="background-image: radial-gradient(#d6cebe 1.2px, transparent 1.2px); background-size: 20px 20px;">
            
            <!-- TOP-RIGHT CLOSE BUTTON '✕' -->
            <button onclick="closeSmritiBook()" class="absolute top-4 right-5 text-gray-500 hover:text-[#8b2252] text-xl font-bold z-40 p-1 transition-colors" title="Close Journal">
              ✕
            </button>

            <!-- Center Spine Line -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[2px] bg-amber-900/15 hidden md:block"></div>

            <div class="flex flex-col items-center justify-center h-full text-center p-8">
              <span class="text-4xl mb-3">✍️</span>
              <h3 class="text-3xl font-bold text-[#1F1F1F] mb-2" style="font-family: 'Patrick Hand', cursive;">Story Writing</h3>
              <p class="text-sm text-gray-700 italic max-w-md" style="font-family: 'Caveat', cursive;">
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
<div class="w-full relative z-20 pointer-events-none -mt-1 bg-[#f4efe6]">
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
          btns[key].classList.remove('bg-[#9b6b78]', 'bg-[#c2a297]');
          btns[key].classList.add('bg-[#421835]');
        } else {
          btns[key].classList.remove('bg-[#421835]');
          btns[key].classList.add('bg-[#9b6b78]');
        }
      }
    });
  }
</script>
"""

# Replace in index.html
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
    content = content[:start_pos] + CURSIVE_NO_BORDER_JOURNAL_HTML + '\n\n' + content[end_pos:]
    print("Successfully updated journal with authentic CAVEAT & PATRICK HAND cursive fonts and NO chunky border!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
