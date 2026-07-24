import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# -------------------------------------------------------------
# 1. REMOVE THE SEPARATE #academic-background SECTION
# -------------------------------------------------------------
content = re.sub(r'<!-- ==================== 4\. ACADEMIC BACKGROUND ==================== -->.*?</section>\s*', '', content, flags=re.DOTALL)
content = re.sub(r'<!-- ACADEMIC BACKGROUND -->.*?</section>\s*', '', content, flags=re.DOTALL)

# -------------------------------------------------------------
# 2. CREATIVE 3D INTERACTIVE JOURNAL BOOK (NO CLUMSY HEADERS)
# -------------------------------------------------------------
CREATIVE_JOURNAL_HTML = """<!-- ABOUT ME: CREATIVE 3D INTERACTIVE JOURNAL BOOK -->
<section class="relative bg-[#f4efe6] text-[#1F1F1F] py-20 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">
  <div class="max-w-6xl mx-auto px-4 md:px-8 text-center">
    
    <!-- Title -->
    <div class="mb-8">
      <span class="text-[11px] uppercase tracking-[0.3em] text-[#8b2252] font-mono font-bold block mb-1">ABOUT ME</span>
      <h2 class="text-4xl md:text-5xl font-bold font-serif italic text-[#1F1F1F]">The Personal Journal</h2>
    </div>

    <!-- BOOK STAGE CONTAINER -->
    <div class="relative w-full max-w-[940px] mx-auto min-h-[580px] flex items-center justify-center perspective-1000">

      <!-- ==================== VIEW 1: CLOSED COVER ==================== -->
      <div id="jbook-cover" class="cursor-pointer transition-all duration-700 ease-out transform scale-100 opacity-100 flex flex-col items-center z-30" onclick="flipJournalTo('page1')">
        <div class="relative group">
          <!-- Green Journal Cover Book -->
          <div class="w-[320px] md:w-[390px] h-[520px] rounded-[26px] shadow-[0_30px_70px_-15px_rgba(0,0,0,0.28)] overflow-hidden relative bg-[#1b4d3e] border border-emerald-900/40 transition-transform duration-500 hover:scale-[1.03] hover:-rotate-1">
            <img src="cover.png" alt="Shakthi Sri Journal Cover" class="w-full h-full object-cover"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/40 via-transparent to-transparent pointer-events-none"></div>
            
            <!-- Hover Touch Hint -->
            <div class="absolute inset-0 bg-black/25 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col items-center justify-center gap-2">
              <span class="text-3xl animate-bounce">📖</span>
              <span class="bg-white/95 backdrop-blur-md text-black font-mono text-xs font-bold px-6 py-3 rounded-full shadow-2xl border border-white/60 tracking-wider uppercase">Click / Tap to Open</span>
            </div>
          </div>

          <!-- Hanging Ribbon Bookmark -->
          <div class="absolute -bottom-6 left-12 w-6 h-12 bg-[#55826b] rounded-b-md shadow-md pointer-events-none"></div>
        </div>
      </div>

      <!-- ==================== VIEW 2: OPENED SPREAD (PAGE 1 & 2) ==================== -->
      <div id="jbook-spread1" class="hidden transition-all duration-700 ease-out transform opacity-0 scale-95 w-full z-30">
        
        <div class="w-full bg-[#faf7f2] rounded-[32px] shadow-[0_30px_80px_-20px_rgba(0,0,0,0.2)] border border-amber-900/15 p-6 md:p-10 relative overflow-hidden text-left" style="background-image: radial-gradient(#d6cebe 1px, transparent 1px); background-size: 20px 20px;">
          
          <!-- CORNER PAGE FLIP TAB (TOP-RIGHT DOG-EAR) -->
          <div onclick="flipJournalTo('page3')" class="absolute top-0 right-0 w-16 h-16 cursor-pointer group z-40" title="Next Page (Page 3)">
            <div class="w-full h-full bg-[#ebdcc4] border-b border-l border-amber-900/20 rounded-bl-2xl shadow-md transition-transform duration-300 group-hover:scale-110 flex items-center justify-center">
              <span class="text-xs font-mono font-bold text-[#8b2252] pl-2 pb-2">p.3 →</span>
            </div>
          </div>

          <!-- CLOSE BOOK RIBBON (TOP-LEFT) -->
          <div onclick="flipJournalTo('cover')" class="absolute top-0 left-6 cursor-pointer group z-40" title="Close Journal">
            <div class="bg-[#55826b] text-white text-[10px] font-mono font-bold px-3 py-2.5 rounded-b-lg shadow-md transition-transform group-hover:translate-y-1">
              ✕ Close
            </div>
          </div>

          <!-- Center Book Spine -->
          <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[2px] bg-amber-900/15 hidden md:block"></div>
          <div class="absolute bottom-0 left-1/2 -translate-x-1/2 w-6 h-8 bg-[#55826b] rounded-t-sm shadow-md hidden md:block"></div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-10 md:gap-14 relative z-10 pt-4">
            
            <!-- LEFT PAGE: BIO & EXPERIENCE TIMELINE -->
            <div class="flex flex-col justify-between text-left pr-0 md:pr-4">
              <div>
                <h3 class="text-3xl md:text-4xl font-bold font-serif text-[#1F1F1F] mb-3 tracking-tight">Shakthi Sri T S</h3>
                
                <!-- Pill Badges -->
                <div class="flex flex-wrap gap-2 mb-6">
                  <span class="px-3.5 py-1 bg-sky-100 text-sky-800 text-[11px] font-mono font-bold rounded-full border border-sky-200">Software Engineer</span>
                  <span class="px-3.5 py-1 bg-purple-100 text-purple-800 text-[11px] font-mono font-bold rounded-full border border-purple-200">Cybersecurity Researcher</span>
                </div>

                <!-- Timeline List -->
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

                <!-- Window Card Widget -->
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

              <!-- Taped Contact Slip & Quote -->
              <div class="pt-4 border-t border-dashed border-amber-900/20 flex flex-col sm:flex-row justify-between items-start sm:items-end gap-3">
                <div class="bg-amber-100/60 p-3 rounded-xl text-[11px] font-mono text-gray-700 border border-amber-900/10">
                  <p class="font-bold">shakthisri1929@gmail.com</p>
                  <p class="text-gray-500">Vellore | Tamil Nadu, India</p>
                </div>
                <p class="font-serif italic text-xs text-[#8b2252] font-semibold">"Write, build, iterate — make an impact!"</p>
              </div>

            </div>

            <!-- RIGHT PAGE: PHOTO & FLOATING STICKERS/TAGS -->
            <div class="flex flex-col items-center justify-center relative min-h-[380px]">
              
              <!-- Central Photo -->
              <div class="relative z-20 group">
                <div class="w-[200px] md:w-[240px] h-[240px] md:h-[280px] rounded-[24px] overflow-hidden shadow-xl border-4 border-white transform rotate-[-2deg] transition-transform duration-500 group-hover:rotate-0">
                  <img src="me.png" alt="Shakthi Sri" class="w-full h-full object-cover"/>
                </div>
                <!-- Profile Tag -->
                <div class="absolute -top-3 right-2 bg-black/80 text-white font-mono text-[10px] font-bold px-3 py-1 rounded-full shadow-md z-30">
                  @Shakthi16
                </div>
              </div>

              <!-- Floating Sticker: Top Left (Flowers) -->
              <div class="absolute top-2 left-2 z-10 pointer-events-none transform -rotate-12">
                <span class="text-2xl">🌸</span>
                <span class="block text-[9px] font-mono text-gray-400">flower.png</span>
              </div>

              <!-- Floating Sticker: Top Right (Cursor Folder) -->
              <div class="absolute top-2 right-4 z-10 pointer-events-none text-center">
                <div class="w-10 h-10 bg-sky-400/20 rounded-xl flex items-center justify-center text-sky-600 text-lg mx-auto">📁</div>
                <span class="block text-[9px] font-mono text-gray-500 mt-1">Cursor</span>
              </div>

              <!-- Floating Sticker: Mid Right (Lifestyle) -->
              <div class="absolute top-1/2 right-0 -translate-y-1/2 z-10 pointer-events-none text-center hidden sm:block">
                <span class="text-2xl">🏋️‍♀️</span>
                <span class="block text-[9px] font-mono text-gray-400">lifestyle</span>
              </div>

              <!-- Floating Sticker: Bottom Left (Experiments.md) -->
              <div class="absolute bottom-4 left-4 z-10 pointer-events-none text-center">
                <div class="w-9 h-9 bg-purple-500/20 rounded-xl flex items-center justify-center text-purple-700 text-base mx-auto">💻</div>
                <span class="block text-[9px] font-mono text-gray-500 mt-1">Experiments.md</span>
              </div>

              <!-- Floating Sticker: Bottom Right (Coffee) -->
              <div class="absolute bottom-4 right-4 z-10 pointer-events-none text-center">
                <span class="text-2xl">🥤</span>
                <span class="block text-[9px] font-mono text-gray-400">CoffeeLover.png</span>
              </div>

            </div>

          </div>

          <!-- Bottom Footer Navigation -->
          <div class="mt-8 pt-4 border-t border-amber-900/10 flex justify-between items-center text-xs font-mono text-gray-500">
            <button onclick="flipJournalTo('cover')" class="hover:text-[#8b2252] font-bold cursor-pointer">← Cover</button>
            <span class="font-bold text-gray-400">Page 1-2 of 3</span>
            <button onclick="flipJournalTo('page3')" class="hover:text-[#8b2252] font-bold cursor-pointer">Page 3 →</button>
          </div>

        </div>
      </div>

      <!-- ==================== VIEW 3: PAGE 3 (NOTES & REFLECTIONS) ==================== -->
      <div id="jbook-spread2" class="hidden transition-all duration-700 ease-out transform opacity-0 scale-95 w-full z-30">
        
        <div class="w-full bg-[#faf7f2] rounded-[32px] shadow-[0_30px_80px_-20px_rgba(0,0,0,0.2)] border border-amber-900/15 p-6 md:p-10 relative overflow-hidden text-left" style="background-image: radial-gradient(#d6cebe 1px, transparent 1px); background-size: 20px 20px;">
          
          <!-- CORNER PAGE FLIP TAB (TOP-RIGHT DOG-EAR -> BACK TO PAGE 1-2) -->
          <div onclick="flipJournalTo('page1')" class="absolute top-0 right-0 w-16 h-16 cursor-pointer group z-40" title="Back to Page 1-2">
            <div class="w-full h-full bg-[#ebdcc4] border-b border-l border-amber-900/20 rounded-bl-2xl shadow-md transition-transform duration-300 group-hover:scale-110 flex items-center justify-center">
              <span class="text-xs font-mono font-bold text-[#8b2252] pl-2 pb-2">← p.1-2</span>
            </div>
          </div>

          <!-- CLOSE BOOK RIBBON (TOP-LEFT) -->
          <div onclick="flipJournalTo('cover')" class="absolute top-0 left-6 cursor-pointer group z-40" title="Close Journal">
            <div class="bg-[#55826b] text-white text-[10px] font-mono font-bold px-3 py-2.5 rounded-b-lg shadow-md transition-transform group-hover:translate-y-1">
              ✕ Close
            </div>
          </div>

          <!-- Center Book Spine -->
          <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[2px] bg-amber-900/15 hidden md:block"></div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-10 md:gap-14 relative z-10 pt-4">
            
            <!-- PAGE 3 LEFT: RESEARCH & SECURITY REFLECTIONS -->
            <div class="space-y-4">
              <span class="text-xs font-mono uppercase tracking-[0.2em] text-[#8b2252] font-bold block">PAGE 3 — RESEARCH NOTES</span>
              <h3 class="text-2xl font-bold font-serif text-[#1F1F1F]">Security Findings &amp; Evasion</h3>
              
              <div class="p-4 rounded-2xl bg-white/80 border border-amber-900/10 space-y-2">
                <h4 class="font-bold text-xs text-[#421835]">● EDR &amp; AV Evasion Study</h4>
                <p class="text-xs text-gray-600 leading-relaxed font-medium">Investigating behavioral endpoint telemetry, bypass mechanisms, and memory inspection techniques in modern security controls.</p>
              </div>

              <div class="p-4 rounded-2xl bg-white/80 border border-amber-900/10 space-y-2">
                <h4 class="font-bold text-xs text-[#421835]">● ICTACA'26 Publication</h4>
                <p class="text-xs text-gray-600 leading-relaxed font-medium">Authored research paper on explainable cybersecurity models and exposure risk prioritization for enterprise networks.</p>
              </div>
            </div>

            <!-- PAGE 3 RIGHT: SYSTEM ARCHITECTURE & FREELANCE -->
            <div class="space-y-4">
              <span class="text-xs font-mono uppercase tracking-[0.2em] text-[#8b2252] font-bold block">PAGE 3 — REFLECTIONS</span>
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

          <!-- Bottom Footer Navigation -->
          <div class="mt-8 pt-4 border-t border-amber-900/10 flex justify-between items-center text-xs font-mono text-gray-500">
            <button onclick="flipJournalTo('page1')" class="hover:text-[#8b2252] font-bold cursor-pointer">← Page 1-2</button>
            <span class="font-bold text-gray-400">Page 3 of 3</span>
            <button onclick="flipJournalTo('cover')" class="hover:text-[#8b2252] font-bold cursor-pointer">Close Journal ➔</button>
          </div>

        </div>
      </div>

    </div>

  </div>
</section>

<!-- Smooth Page Flip Script -->
<script>
  function flipJournalTo(state) {
    const cover = document.getElementById('jbook-cover');
    const spread1 = document.getElementById('jbook-spread1');
    const spread2 = document.getElementById('jbook-spread2');

    const views = [cover, spread1, spread2];

    views.forEach(v => {
      if (v) {
        v.classList.add('hidden');
        v.classList.remove('opacity-100', 'scale-100');
        v.classList.add('opacity-0', 'scale-95');
      }
    });

    let target;
    if (state === 'cover') target = cover;
    else if (state === 'page1') target = spread1;
    else if (state === 'page3') target = spread2;

    if (target) {
      target.classList.remove('hidden');
      setTimeout(() => {
        target.classList.remove('opacity-0', 'scale-95');
        target.classList.add('opacity-100', 'scale-100');
      }, 40);
    }
  }
</script>
"""

# Replace old #about-journal in index.html
content = re.sub(r'<!-- ABOUT ME: INTERACTIVE JOURNAL BOOK.*?<!-- Touch Journal Open/Close Script -->', CREATIVE_JOURNAL_HTML, content, flags=re.DOTALL)
content = re.sub(r'<!-- ABOUT ME: INTERACTIVE 3-PAGE JOURNAL BOOK.*?<!-- Journal Switcher Script -->', CREATIVE_JOURNAL_HTML, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated Journal Book to creative 3D flip with corner tabs & removed academic background section!")
