import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# -------------------------------------------------------------
# INTERACTIVE 3-PAGE JOURNAL BOOK COMPONENT
# -------------------------------------------------------------
JOURNAL_BOOK_HTML = """<!-- THE JOURNAL BOOK (3-PAGE INTERACTIVE BOOK DIRECTLY BELOW HOME) -->
<section class="relative bg-[#f4efe6] text-[#1F1F1F] py-20 overflow-hidden border-b border-amber-900/10" id="about-journal">
  <div class="max-w-6xl mx-auto px-4 md:px-8">
    
    <!-- Header & Controls -->
    <div class="flex flex-col md:flex-row justify-between items-center mb-10 gap-4">
      <div class="text-center md:text-left">
        <span class="text-xs uppercase tracking-[0.25em] text-[#8b2252] font-mono font-bold block mb-1">INTERACTIVE NOTEBOOK</span>
        <h2 class="text-3xl md:text-4xl font-bold font-serif italic text-[#1F1F1F]">The Personal Journal</h2>
      </div>

      <!-- Page Flip Controls -->
      <div class="flex items-center gap-3 bg-white/80 backdrop-blur-md px-4 py-2 rounded-full border border-amber-900/10 shadow-sm">
        <button onclick="setJournalPage('cover')" id="btn-page-cover" class="px-3 py-1 text-xs font-bold font-mono rounded-full transition-all bg-[#421835] text-white">Cover</button>
        <button onclick="setJournalPage('spread1')" id="btn-page-spread1" class="px-3 py-1 text-xs font-bold font-mono rounded-full transition-all text-gray-600 hover:text-black">Page 1-2</button>
        <button onclick="setJournalPage('spread2')" id="btn-page-spread2" class="px-3 py-1 text-xs font-bold font-mono rounded-full transition-all text-gray-600 hover:text-black">Page 3</button>
      </div>
    </div>

    <!-- BOOK STAGE CONTAINER -->
    <div class="relative w-full max-w-[960px] mx-auto min-h-[580px] flex items-center justify-center">

      <!-- ==================== PAGE 0: COVER ==================== -->
      <div id="journal-view-cover" class="journal-view transition-all duration-700 ease-out transform opacity-100 scale-100 flex flex-col items-center">
        <div class="relative group cursor-pointer" onclick="setJournalPage('spread1')">
          <!-- Green Journal Cover Book -->
          <div class="w-[320px] md:w-[390px] h-[520px] rounded-[24px] shadow-[0_30px_70px_-15px_rgba(0,0,0,0.25)] overflow-hidden relative bg-[#1b4d3e] border border-emerald-900/40 transition-transform duration-500 hover:scale-[1.02]">
            <img src="cover.png" alt="Shakthi Sri Journal Cover" class="w-full h-full object-cover"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/40 via-transparent to-transparent pointer-events-none"></div>
            
            <!-- Click hint overlay -->
            <div class="absolute inset-0 bg-black/20 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
              <span class="bg-white/90 backdrop-blur-md text-black font-mono text-xs font-bold px-5 py-2.5 rounded-full shadow-lg border border-white/60 tracking-wider uppercase">Click to Open Journal →</span>
            </div>
          </div>
          <!-- Ribbon Bookmark hanging down -->
          <div class="absolute -bottom-6 left-12 w-6 h-12 bg-[#55826b] rounded-b-md shadow-md pointer-events-none"></div>
        </div>
      </div>

      <!-- ==================== SPREAD 1: PAGES 1 & 2 (OPENED SPREAD) ==================== -->
      <div id="journal-view-spread1" class="journal-view hidden transition-all duration-700 ease-out transform opacity-0 scale-95 w-full">
        
        <div class="w-full bg-[#faf7f2] rounded-[32px] shadow-[0_30px_80px_-20px_rgba(0,0,0,0.18)] border border-amber-900/15 p-6 md:p-10 relative overflow-hidden" style="background-image: radial-gradient(#d6cebe 1px, transparent 1px); background-size: 20px 20px;">
          
          <!-- Center Book Spine -->
          <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[2px] bg-amber-900/15 hidden md:block"></div>
          <div class="absolute bottom-0 left-1/2 -translate-x-1/2 w-6 h-8 bg-[#55826b] rounded-t-sm shadow-md hidden md:block"></div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-10 md:gap-14 relative z-10">
            
            <!-- LEFT PAGE: BIO & TIMELINE -->
            <div class="flex flex-col justify-between text-left pr-0 md:pr-4">
              <div>
                <h3 class="text-3xl md:text-4xl font-bold font-serif text-[#1F1F1F] mb-3 tracking-tight">Shakthi Sri T S</h3>
                
                <!-- Pill Badges -->
                <div class="flex flex-wrap gap-2 mb-6">
                  <span class="px-3 py-1 bg-sky-100 text-sky-800 text-[11px] font-mono font-bold rounded-full border border-sky-200">Software Engineer</span>
                  <span class="px-3 py-1 bg-purple-100 text-purple-800 text-[11px] font-mono font-bold rounded-full border border-purple-200">Cybersecurity Researcher</span>
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

            <!-- RIGHT PAGE: PHOTO & FLOATING STICKERS -->
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

        </div>
      </div>

      <!-- ==================== SPREAD 2: PAGE 3 (NOTES & REFLECTIONS) ==================== -->
      <div id="journal-view-spread2" class="journal-view hidden transition-all duration-700 ease-out transform opacity-0 scale-95 w-full">
        
        <div class="w-full bg-[#faf7f2] rounded-[32px] shadow-[0_30px_80px_-20px_rgba(0,0,0,0.18)] border border-amber-900/15 p-6 md:p-10 relative overflow-hidden" style="background-image: radial-gradient(#d6cebe 1px, transparent 1px); background-size: 20px 20px;">
          
          <!-- Center Book Spine -->
          <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[2px] bg-amber-900/15 hidden md:block"></div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-10 md:gap-14 relative z-10 text-left">
            
            <!-- PAGE 3 LEFT: RESEARCH REFLECTIONS -->
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

            <!-- PAGE 3 RIGHT: SYSTEM ARCHITECTURE & GOALS -->
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
  function setJournalPage(pageId) {
    const cover = document.getElementById('journal-view-cover');
    const spread1 = document.getElementById('journal-view-spread1');
    const spread2 = document.getElementById('journal-view-spread2');

    const btnCover = document.getElementById('btn-page-cover');
    const btnSpread1 = document.getElementById('btn-page-spread1');
    const btnSpread2 = document.getElementById('btn-page-spread2');

    const views = [cover, spread1, spread2];
    const btns = [btnCover, btnSpread1, btnSpread2];

    views.forEach(v => {
      if (v) {
        v.classList.add('hidden');
        v.classList.remove('opacity-100', 'scale-100');
        v.classList.add('opacity-0', 'scale-95');
      }
    });

    btns.forEach(b => {
      if (b) {
        b.classList.remove('bg-[#421835]', 'text-white');
        b.classList.add('text-gray-600');
      }
    });

    let targetView, targetBtn;
    if (pageId === 'cover') {
      targetView = cover;
      targetBtn = btnCover;
    } else if (pageId === 'spread1') {
      targetView = spread1;
      targetBtn = btnSpread1;
    } else if (pageId === 'spread2') {
      targetView = spread2;
      targetBtn = btnSpread2;
    }

    if (targetView && targetBtn) {
      targetView.classList.remove('hidden');
      setTimeout(() => {
        targetView.classList.remove('opacity-0', 'scale-95');
        targetView.classList.add('opacity-100', 'scale-100');
      }, 50);

      targetBtn.classList.remove('text-gray-600');
      targetBtn.classList.add('bg-[#421835]', 'text-white');
    }
  }
</script>
"""

# Insert directly before <section class="editorial-canvas ... id="about">
if 'id="about-journal"' in content:
    content = re.sub(r'<!-- THE JOURNAL SECTION WITH COVER.PNG -->.*?</script>', JOURNAL_BOOK_HTML, content, flags=re.DOTALL)
elif 'id="about"' in content:
    content = re.sub(r'<!-- ABOUT: CINEMATIC EDITORIAL CANVAS -->', JOURNAL_BOOK_HTML + '\n\n<!-- ABOUT: CINEMATIC EDITORIAL CANVAS -->', content, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully injected 3-page Journal Book directly below home section!")
