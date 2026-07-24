"""
Rewrites journal spreads 1, 2, 3 and sidebar tabs to match the reference mockup images exactly.
Key design rules:
- Great Vibes ONLY for cursive labels (about me ヾ, currently ヾ, class of 2026, etc.)
- Patrick Hand / Courier Prime monospace for body text (timeline rows, bullet text)  
- Outfit for headings (Shakthi Sri, On Building., Things I've Learned.)
- Sidebar tabs: thin, narrow, muted, no thick burgundy slabs
- Icons: uniform thin SVG stroke-based icons, all same color (#6B2137), no emojis
- Tech logos: all desaturated / muted #6B2137 color, no colorful icons
- Cards: slightly rounded (rounded-lg) not over-rounded, notebook-style
- Clear hierarchy: big title > section header (Great Vibes italic) > body (Patrick Hand small)
- Spacing: consistent 8px / 12px / 16px rhythm
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────────
# 1. SIDEBAR TABS – thin, muted, narrow
# ─────────────────────────────────────────────────────────────────
OLD_TABS = '''          <div class="absolute top-6 -right-8 md:-right-10 flex flex-col gap-2 z-50">
            
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

          </div>'''

NEW_TABS = '''          <!-- OUTSIDE RIGHT VERTICAL INDEX TABS – thin, muted, notebook-style -->
          <div class="absolute top-4 -right-[26px] md:-right-[30px] flex flex-col gap-1.5 z-50">
            
            <!-- Home Tab -->
            <button onclick="closeSmritiBook()" class="w-6 md:w-7 h-8 bg-[#EDE4D9] hover:bg-[#6B2137] text-[#6B2137] hover:text-white rounded-r-lg shadow-sm border border-l-0 border-amber-900/25 flex items-center justify-center transition-all duration-200" title="Close to Cover">
              <svg class="w-3 h-3" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 9.75L12 3l9 6.75V21H15v-6H9v6H3V9.75z"/></svg>
            </button>

            <!-- Tab 1: About Me -->
            <button id="tab-btn-spread1" onclick="switchSmritiSpread('spread1')" class="w-6 md:w-7 py-5 bg-[#C9A8B2] text-white rounded-r-lg shadow-sm border border-l-0 border-[#B08898] flex items-center justify-center transition-all duration-200 hover:bg-[#6B2137]" style="writing-mode: vertical-rl; text-orientation: mixed; font-family: 'Outfit', sans-serif; font-size: 8px; letter-spacing: 0.5px; font-weight: 600;">
              About Me
            </button>

            <!-- Tab 2: Things I Learnt -->
            <button id="tab-btn-spread2" onclick="switchSmritiSpread('spread2')" class="w-6 md:w-7 py-5 bg-[#B8929E] hover:bg-[#6B2137] text-white rounded-r-lg shadow-sm border border-l-0 border-[#A07888] flex items-center justify-center transition-all duration-200" style="writing-mode: vertical-rl; text-orientation: mixed; font-family: 'Outfit', sans-serif; font-size: 8px; letter-spacing: 0.5px; font-weight: 600;">
              Things I Learnt
            </button>

            <!-- Tab 3: Story Writing -->
            <button id="tab-btn-spread3" onclick="switchSmritiSpread('spread3')" class="w-6 md:w-7 py-5 bg-[#A67D88] hover:bg-[#6B2137] text-white rounded-r-lg shadow-sm border border-l-0 border-[#8A6070] hidden sm:flex items-center justify-center transition-all duration-200" style="writing-mode: vertical-rl; text-orientation: mixed; font-family: 'Outfit', sans-serif; font-size: 8px; letter-spacing: 0.5px; font-weight: 600;">
              Story Writing
            </button>

          </div>'''

html = html.replace(OLD_TABS, NEW_TABS)

# ─────────────────────────────────────────────────────────────────
# 2. SPREAD 1 – About Me (Pages 01 & 02)
# ─────────────────────────────────────────────────────────────────
# Find spread 1 boundaries
s1_start = html.find('<!-- INNER PAGES SPREAD 1 (PAGES 01 & 02 - EXACT MOCKUP MATCH) -->')
s1_end   = html.find('<!-- INNER PAGES SPREAD 2 -->', s1_start)
assert s1_start != -1 and s1_end != -1, "Spread 1 markers not found"

SPREAD1_HTML = '''<!-- INNER PAGES SPREAD 1 (PAGES 01 & 02 - EXACT MOCKUP MATCH) -->
          <div id="smriti-spread-1" class="w-full bg-[#FAF6EE] rounded-[14px] relative overflow-hidden text-left" style="height:520px; background-image: radial-gradient(#D8CFC3 1px, transparent 1px); background-size: 18px 18px;">

            <!-- Center Spine -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-px bg-amber-900/12 hidden md:block pointer-events-none"></div>

            <!-- X Close -->
            <button onclick="closeSmritiBook()" class="absolute top-2.5 right-3 text-gray-400 hover:text-[#6B2137] text-base z-40 transition-colors leading-none" title="Close Journal">✕</button>

            <div class="grid grid-cols-2 h-full">

              <!-- ══ PAGE 01 – LEFT ══ -->
              <div class="flex flex-col p-5 pr-4 overflow-hidden">

                <!-- Name -->
                <h3 class="text-[34px] font-bold text-[#1C1917] leading-none mb-1.5" style="font-family:'Outfit',sans-serif; letter-spacing:-0.5px;">Shakthi Sri</h3>

                <!-- Pill + cursive -->
                <div class="flex items-center gap-3 mb-3">
                  <span class="border border-[#6B2137]/40 text-[#6B2137] text-[8.5px] font-semibold px-2 py-0.5 rounded-sm tracking-widest uppercase" style="font-family:'Outfit',sans-serif; background:#fdf6ee;">DEVELOPER &amp; RESEARCHER</span>
                  <span class="text-lg text-[#2C2C2C]" style="font-family:'Great Vibes',cursive;">class of 2026</span>
                </div>

                <!-- Timeline rows – uniform thin SVG icons, monospace body -->
                <div class="space-y-[7px] mb-3">
                  <!-- Row helper: icon left, label bold, value right muted -->
                  <div class="flex items-center justify-between border-b border-dashed border-amber-900/15 pb-[5px]">
                    <span class="flex items-center gap-1.5 text-[11px] font-semibold text-[#1C1917]" style="font-family:'Courier Prime','Courier New',monospace;">
                      <!-- laptop icon -->
                      <svg class="w-3 h-3 text-[#6B2137] shrink-0" fill="none" stroke="currentColor" stroke-width="1.6" viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="13" rx="1.5"/><path d="M0 19h24"/></svg>
                      B.Tech Information Technology
                    </span>
                    <span class="text-[10px] text-gray-500 shrink-0 ml-2" style="font-family:'Courier Prime','Courier New',monospace;">2022 – 2026</span>
                  </div>
                  <div class="flex items-center justify-between border-b border-dashed border-amber-900/15 pb-[5px]">
                    <span class="flex items-center gap-1.5 text-[11px] font-semibold text-[#1C1917]" style="font-family:'Courier Prime','Courier New',monospace;">
                      <svg class="w-3 h-3 text-[#6B2137] shrink-0" fill="none" stroke="currentColor" stroke-width="1.6" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 14l9-5-9-5-9 5 9 5zm0 0v6m-4-3.5l4 2 4-2"/></svg>
                      Kingston Engineering College
                    </span>
                    <span class="text-[10px] font-bold text-[#6B2137] shrink-0 ml-2" style="font-family:'Courier Prime','Courier New',monospace;">CGPA: 8.6</span>
                  </div>
                  <div class="flex items-center justify-between border-b border-dashed border-amber-900/15 pb-[5px]">
                    <span class="flex items-center gap-1.5 text-[11px] font-semibold text-[#1C1917]" style="font-family:'Courier Prime','Courier New',monospace;">
                      <svg class="w-3 h-3 text-[#6B2137] shrink-0" fill="none" stroke="currentColor" stroke-width="1.6" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 3H6a2 2 0 00-2 2v14a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2h-3m-4 0V1m0 2h4m-4 0H9m0 0V1"/></svg>
                      IIT Madras — CYSTAR
                    </span>
                    <span class="text-[10px] text-gray-500 shrink-0 ml-2" style="font-family:'Courier Prime','Courier New',monospace;">Research Intern</span>
                  </div>
                  <div class="flex items-center justify-between border-b border-dashed border-amber-900/15 pb-[5px]">
                    <span class="flex items-center gap-1.5 text-[11px] font-semibold text-[#1C1917]" style="font-family:'Courier Prime','Courier New',monospace;">
                      <svg class="w-3 h-3 text-[#6B2137] shrink-0" fill="none" stroke="currentColor" stroke-width="1.6" viewBox="0 0 24 24"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
                      Full-Stack Developer
                    </span>
                    <span class="text-[10px] text-gray-500 shrink-0 ml-2" style="font-family:'Courier Prime','Courier New',monospace;">MERN Stack</span>
                  </div>
                  <div class="flex items-center justify-between pb-[5px]">
                    <span class="flex items-center gap-1.5 text-[11px] font-semibold text-[#1C1917]" style="font-family:'Courier Prime','Courier New',monospace;">
                      <svg class="w-3 h-3 text-[#6B2137] shrink-0" fill="none" stroke="currentColor" stroke-width="1.6" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                      Cybersecurity Enthusiast
                    </span>
                    <span class="text-[10px] text-gray-500 shrink-0 ml-2" style="font-family:'Courier Prime','Courier New',monospace;">Always Learning</span>
                  </div>
                </div>

                <!-- Two small cards: about me + TODAY -->
                <div class="grid grid-cols-2 gap-2 mb-auto">
                  <!-- about me note -->
                  <div class="bg-[#F5EDE1] border border-amber-900/15 rounded-lg p-2.5 relative">
                    <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-6 h-2 bg-[#DDD0BC]/80 rotate-[-1.5deg]"></div>
                    <span class="block text-sm text-[#6B2137] mb-1" style="font-family:'Great Vibes',cursive;">about me ✦</span>
                    <ul class="text-[9.5px] text-[#2C2C2C] leading-relaxed space-y-0.5" style="font-family:'Patrick Hand',cursive;">
                      <li>♥ I love turning ideas into impactful digital solutions.</li>
                      <li>♥ Curious mind with a strong drive to build, secure and innovate.</li>
                      <li>♥ Believer in discipline, consistency &amp; growth.</li>
                    </ul>
                    <span class="absolute bottom-1.5 right-2 text-[10px] text-[#6B2137]/50">♡</span>
                  </div>
                  <!-- TODAY widget -->
                  <div class="bg-[#F5EDE1] border border-amber-900/15 rounded-lg p-2.5 relative">
                    <div class="flex items-center gap-1 mb-1">
                      <span class="w-1.5 h-1.5 rounded-full bg-rose-300"></span>
                      <span class="w-1.5 h-1.5 rounded-full bg-amber-300"></span>
                      <span class="w-1.5 h-1.5 rounded-full bg-green-300"></span>
                      <span class="ml-auto text-amber-700/40 text-xs">☆</span>
                    </div>
                    <span class="block text-[8px] font-bold tracking-widest text-gray-400 uppercase mb-1" style="font-family:'Outfit',sans-serif;">TODAY</span>
                    <p class="text-[9.5px] text-[#2C2C2C] leading-relaxed" style="font-family:'Patrick Hand',cursive;">
                      Building skills. Solving problems.<br/>Creating solutions.<br/>Preparing for impact.<br/>One step at a time.
                    </p>
                  </div>
                </div>

                <!-- Contact + Quote bottom strip -->
                <div class="border-t border-dashed border-amber-900/15 mt-2 pt-2 flex items-end justify-between gap-2">
                  <div class="bg-[#EDE3D4] rounded-md px-2.5 py-1.5 text-[9.5px] text-[#2C2C2C]" style="font-family:'Patrick Hand',cursive;">
                    <p class="font-semibold text-[#1C1917]">srishakthi799@gmail.com</p>
                    <p>+91 7895032098</p>
                    <p class="text-gray-500">Chennai | Vellore</p>
                  </div>
                  <div class="text-right">
                    <p class="text-sm text-[#541C2E] leading-snug" style="font-family:'Great Vibes',cursive;">code with purpose,<br/>create with impact.</p>
                    <span class="text-xs text-[#6B2137]/60">♡</span>
                  </div>
                </div>
              </div>

              <!-- ══ PAGE 02 – RIGHT ══ -->
              <div class="flex flex-col p-5 pl-4 overflow-hidden">

                <!-- Top row: breathe + Goals + Reminders -->
                <div class="flex items-start justify-between mb-3">
                  <!-- breathe botanical -->
                  <div class="flex flex-col items-center gap-0.5">
                    <svg class="w-5 h-7 text-[#6B2137]/60" fill="none" stroke="currentColor" stroke-width="1.2" viewBox="0 0 24 32">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M12 30V14M12 14C9 11 5 12 5 12s1 4 5 4M12 14c3-3 7-2 7-2s-1 4-5 4M12 14c-2-3-1-8-1-8s4 1 4 6"/>
                    </svg>
                    <span class="text-[8px] text-gray-500" style="font-family:'Patrick Hand',cursive;">breathe.png</span>
                  </div>
                  <!-- Goals & Reminders -->
                  <div class="flex items-center gap-4">
                    <div class="flex flex-col items-center gap-0.5">
                      <!-- folder icon -->
                      <div class="w-8 h-7 bg-[#7A3045] rounded-md rounded-tl-none relative flex items-center justify-center">
                        <div class="absolute -top-1.5 left-0 w-3 h-1.5 bg-[#7A3045] rounded-t-sm"></div>
                      </div>
                      <span class="text-[8px] text-gray-600" style="font-family:'Patrick Hand',cursive;">Goals</span>
                    </div>
                    <div class="flex flex-col items-center gap-0.5">
                      <!-- floppy disk icon -->
                      <div class="w-7 h-7 bg-[#D5C9BB] border border-amber-900/20 rounded-sm relative">
                        <div class="absolute top-1 left-1 right-1 h-2.5 bg-[#B5A898] rounded-sm"></div>
                        <div class="absolute bottom-0.5 left-1 right-1 h-2.5 bg-[#C5B9AB] rounded-sm flex items-center justify-center">
                          <div class="w-1 h-1.5 bg-[#E5DDD5] rounded-sm"></div>
                        </div>
                      </div>
                      <span class="text-[8px] text-gray-600" style="font-family:'Patrick Hand',cursive;">Reminders</span>
                    </div>
                  </div>
                </div>

                <!-- @Shakthi.16 tag + girl illustration -->
                <div class="flex gap-2.5 mb-2.5">
                  <!-- currently card -->
                  <div class="flex-1 border border-dashed border-amber-900/25 rounded-lg p-2.5 bg-[#F8F2E8]">
                    <span class="block text-sm text-[#6B2137] mb-1.5" style="font-family:'Great Vibes',cursive;">currently ✦</span>
                    <ul class="text-[9.5px] text-[#2C2C2C] leading-relaxed space-y-0.5" style="font-family:'Patrick Hand',cursive;">
                      <li>♥ Exploring AI &amp; LLMs</li>
                      <li>♥ Building secure systems</li>
                      <li>♥ Deepening full-stack</li>
                      <li>♥ Learning. Shipping.</li>
                      <li>♥ Growing. Always. ♡</li>
                    </ul>
                  </div>
                  <!-- illustration -->
                  <div class="relative shrink-0">
                    <div class="absolute -top-2 left-1/2 -translate-x-1/2 bg-[#1A1A1A] text-white text-[7.5px] font-semibold px-2 py-0.5 rounded-full z-10 whitespace-nowrap" style="font-family:'Outfit',sans-serif;">@Shakthi.16</div>
                    <div class="w-[110px] h-[155px] rounded-xl overflow-hidden border-2 border-white shadow-md bg-[#F0E8DC]">
                      <img src="girl.png" alt="Shakthi Sri" class="w-full h-full object-cover"/>
                    </div>
                  </div>
                </div>

                <!-- tech i work with -->
                <div class="border border-dashed border-amber-900/20 rounded-lg p-2 bg-[#F8F2E8] mb-2">
                  <span class="block text-[11px] text-[#6B2137] mb-1.5" style="font-family:'Great Vibes',cursive;">tech i work with ✦</span>
                  <div class="flex items-center justify-between">
                    <!-- React -->
                    <div class="flex flex-col items-center gap-0.5">
                      <svg class="w-4 h-4 text-[#6B2137]/70" fill="none" stroke="currentColor" stroke-width="1.2" viewBox="0 0 24 24">
                        <ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(0)"/><ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(60)"/><ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(120)"/><circle cx="12" cy="12" r="1.5" fill="currentColor"/>
                      </svg>
                      <span class="text-[7.5px] text-gray-600" style="font-family:'Patrick Hand',cursive;">React.js</span>
                    </div>
                    <!-- Node -->
                    <div class="flex flex-col items-center gap-0.5">
                      <div class="w-4 h-4 border border-[#6B2137]/50 rounded-sm flex items-center justify-center">
                        <span class="text-[6px] font-bold text-[#6B2137]" style="font-family:'Outfit',sans-serif;">ncb</span>
                      </div>
                      <span class="text-[7.5px] text-gray-600" style="font-family:'Patrick Hand',cursive;">Node.js</span>
                    </div>
                    <!-- Express -->
                    <div class="flex flex-col items-center gap-0.5">
                      <span class="text-[11px] font-bold text-[#6B2137]/70 leading-none" style="font-family:'Courier Prime','Courier New',monospace;">ex</span>
                      <span class="text-[7.5px] text-gray-600" style="font-family:'Patrick Hand',cursive;">Express.js</span>
                    </div>
                    <!-- MongoDB -->
                    <div class="flex flex-col items-center gap-0.5">
                      <svg class="w-4 h-4 text-[#6B2137]/70" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C10 5 8 9 8 13c0 2.5 1.5 4.5 4 5.5 2.5-1 4-3 4-5.5 0-4-2-8-4-11z"/></svg>
                      <span class="text-[7.5px] text-gray-600" style="font-family:'Patrick Hand',cursive;">MongoDB</span>
                    </div>
                    <!-- separator -->
                    <div class="w-px h-8 bg-amber-900/15"></div>
                    <!-- Figma -->
                    <div class="flex flex-col items-center gap-0.5">
                      <svg class="w-4 h-4 text-[#6B2137]/70" fill="none" stroke="currentColor" stroke-width="1.4" viewBox="0 0 24 24">
                        <rect x="8" y="2" width="8" height="5" rx="2"/><rect x="8" y="9" width="8" height="5" rx="2.5"/><rect x="8" y="16" width="5" height="5" rx="2.5"/><circle cx="16" cy="11.5" r="2.5"/>
                      </svg>
                      <span class="text-[7.5px] text-gray-600" style="font-family:'Patrick Hand',cursive;">Figma</span>
                    </div>
                    <!-- VS Code -->
                    <div class="flex flex-col items-center gap-0.5">
                      <svg class="w-4 h-4 text-[#6B2137]/70" fill="none" stroke="currentColor" stroke-width="1.4" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M16 3L4 13l5 4L3 21l18-9L16 3z"/>
                      </svg>
                      <span class="text-[7.5px] text-gray-600" style="font-family:'Patrick Hand',cursive;">VS Code</span>
                    </div>
                    <!-- Linux -->
                    <div class="flex flex-col items-center gap-0.5">
                      <svg class="w-4 h-4 text-[#6B2137]/70" fill="none" stroke="currentColor" stroke-width="1.4" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 3C9 3 7 6 7 9v4c0 1.5-1 3-2 4 0 3 3 4 7 4s7-1 7-4c-1-1-2-2.5-2-4V9c0-3-2-6-5-6z"/>
                        <path stroke-linecap="round" d="M9 17.5c1 1 5 1 6 0"/>
                      </svg>
                      <span class="text-[7.5px] text-gray-600" style="font-family:'Patrick Hand',cursive;">Linux</span>
                    </div>
                  </div>
                </div>

                <!-- what i build + taped botanical -->
                <div class="flex items-stretch gap-2">
                  <div class="flex-1 border border-dashed border-amber-900/20 rounded-lg p-2 bg-[#F8F2E8]">
                    <span class="block text-[11px] text-[#6B2137] mb-1.5 text-center" style="font-family:'Great Vibes',cursive;">what i build ♡</span>
                    <div class="grid grid-cols-3 gap-1 text-center">
                      <div class="bg-white/70 rounded-md p-1 border border-amber-900/10">
                        <svg class="w-3.5 h-3.5 text-[#6B2137]/60 mx-auto mb-0.5" fill="none" stroke="currentColor" stroke-width="1.4" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 010 20M12 2a15 15 0 000 20"/></svg>
                        <span class="text-[7.5px] text-[#2C2C2C] leading-tight block" style="font-family:'Patrick Hand',cursive;">Full-Stack Web Applications</span>
                      </div>
                      <div class="bg-white/70 rounded-md p-1 border border-amber-900/10">
                        <svg class="w-3.5 h-3.5 text-[#6B2137]/60 mx-auto mb-0.5" fill="none" stroke="currentColor" stroke-width="1.4" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                        <span class="text-[7.5px] text-[#2C2C2C] leading-tight block" style="font-family:'Patrick Hand',cursive;">Cybersecurity Tools &amp; Research</span>
                      </div>
                      <div class="bg-white/70 rounded-md p-1 border border-amber-900/10">
                        <svg class="w-3.5 h-3.5 text-[#6B2137]/60 mx-auto mb-0.5" fill="none" stroke="currentColor" stroke-width="1.4" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707M12 21a9 9 0 110-18 9 9 0 010 18z"/></svg>
                        <span class="text-[7.5px] text-[#2C2C2C] leading-tight block" style="font-family:'Patrick Hand',cursive;">AI-Enhanced Solutions</span>
                      </div>
                    </div>
                  </div>
                  <!-- botanical taped card -->
                  <div class="w-10 bg-[#EDE3D4] rounded-lg border border-amber-900/15 flex items-center justify-center relative shrink-0">
                    <div class="absolute -top-1.5 left-1/2 -translate-x-1/2 w-5 h-2 bg-[#D5C0A8]/70 rotate-[1.5deg]"></div>
                    <svg class="w-5 h-8 text-[#6B2137]/50" fill="none" stroke="currentColor" stroke-width="1.2" viewBox="0 0 24 32">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M12 30V14M12 14C9 11 5 12 5 12s1 4 5 4M12 14c3-3 7-2 7-2s-1 4-5 4"/>
                    </svg>
                  </div>
                </div>

              </div>
            </div>
          </div>
'''

html = html[:s1_start] + SPREAD1_HTML + '\n' + html[s1_end:]

# ─────────────────────────────────────────────────────────────────
# 3. SPREAD 2 – On Building (Pages 03 & 04)
# ─────────────────────────────────────────────────────────────────
s2_start = html.find('<!-- INNER PAGES SPREAD 2 -->')
# find spread 3 comment (old or new) after s2
s2_end_marker = html.find('<!-- INNER PAGES SPREAD 3', s2_start)
assert s2_start != -1 and s2_end_marker != -1, "Spread 2 markers not found"

SPREAD2_HTML = '''<!-- INNER PAGES SPREAD 2 -->
          <div id="smriti-spread-2" class="hidden w-full bg-[#FAF6EE] rounded-[14px] relative overflow-hidden text-left" style="height:520px; background-image: radial-gradient(#D8CFC3 1px, transparent 1px); background-size: 18px 18px;">

            <!-- Center Spine -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-px bg-amber-900/12 hidden md:block pointer-events-none"></div>

            <!-- X Close -->
            <button onclick="closeSmritiBook()" class="absolute top-2.5 right-3 text-gray-400 hover:text-[#6B2137] text-base z-40 transition-colors leading-none" title="Close Journal">✕</button>

            <div class="grid grid-cols-2 h-full">

              <!-- ══ PAGE 03 – On Building (LEFT) ══ -->
              <div class="flex flex-col p-5 pr-4 overflow-hidden">

                <!-- Page number + title -->
                <div class="mb-1">
                  <span class="text-[9px] font-bold text-[#6B2137]/50 tracking-widest" style="font-family:'Outfit',sans-serif;">03</span>
                  <h3 class="text-[28px] font-bold text-[#1C1917] leading-none mt-0.5" style="font-family:'Outfit',sans-serif; letter-spacing:-0.3px;">On Building. <span class="text-[#6B2137]/40" style="font-family:'Great Vibes',cursive; font-size:22px;">✦</span></h3>
                  <p class="text-[9px] text-gray-400 mt-0.5" style="font-family:'Outfit',sans-serif;">Journal Entry — 03</p>
                </div>

                <!-- Two-col layout: taped quote left, bridge sketch right -->
                <div class="grid grid-cols-2 gap-2 mb-2.5">
                  <!-- big quote card -->
                  <div class="bg-[#F5EDE1] border border-amber-900/15 rounded-lg p-2.5 relative">
                    <div class="absolute -top-1.5 left-4 w-6 h-2 bg-[#D5C0A8]/70 rotate-[-2deg]"></div>
                    <span class="text-base text-[#6B2137]/30 leading-none block">"</span>
                    <p class="text-[9.5px] text-[#2C2C2C] leading-relaxed" style="font-family:'Patrick Hand',cursive;">
                      If a system becomes difficult to explain, it is usually becoming difficult to maintain.
                    </p>
                    <span class="text-base text-[#6B2137]/30 leading-none block text-right">"</span>
                  </div>
                  <!-- bridge SVG + entry text -->
                  <div class="flex flex-col justify-between">
                    <p class="text-[9.5px] text-[#2C2C2C] leading-relaxed" style="font-family:'Patrick Hand',cursive;">
                      When I first started writing software, I believed engineering was about finding answers.
                    </p>
                    <!-- bridge sketch SVG -->
                    <svg class="w-full h-14 text-[#6B2137]/30 mt-1" viewBox="0 0 130 50" fill="none" stroke="currentColor" stroke-width="0.9">
                      <path stroke-linecap="round" d="M5 45h120M30 10v35M100 10v35M5 32c20-16 40-16 50 0c10-16 30-16 50 0"/>
                      <path stroke-linecap="round" stroke-dasharray="1.5 2" d="M30 10L5 32M30 10l25 22M100 10l-25 22M100 10l25 22"/>
                      <!-- sun -->
                      <circle cx="100" cy="12" r="5" stroke-width="0.7"/>
                      <!-- birds -->
                      <path d="M55 8c2-2 4-2 6 0M65 5c1-1.5 3-1.5 4 0"/>
                    </svg>
                  </div>
                </div>

                <!-- I realised... -->
                <div class="mb-2">
                  <span class="text-[10px] font-semibold text-[#6B2137] block mb-0.5" style="font-family:'Great Vibes',cursive; font-size:13px;">I realised...</span>
                  <p class="text-[9.5px] text-[#2C2C2C]" style="font-family:'Patrick Hand',cursive;">Good engineering begins with understanding. ♡</p>
                </div>

                <!-- Observe · Understand · Build row -->
                <div class="flex items-center gap-3 mb-2.5">
                  <div class="flex flex-col items-center gap-0.5">
                    <svg class="w-4 h-4 text-[#6B2137]/60" fill="none" stroke="currentColor" stroke-width="1.4" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
                    <span class="text-[8px] text-gray-500" style="font-family:'Patrick Hand',cursive;">Observe.</span>
                  </div>
                  <div class="flex flex-col items-center gap-0.5">
                    <svg class="w-4 h-4 text-[#6B2137]/60" fill="none" stroke="currentColor" stroke-width="1.4" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707M12 21a9 9 0 110-18 9 9 0 010 18z"/></svg>
                    <span class="text-[8px] text-gray-500" style="font-family:'Patrick Hand',cursive;">Understand.</span>
                  </div>
                  <div class="flex flex-col items-center gap-0.5">
                    <svg class="w-4 h-4 text-[#6B2137]/60" fill="none" stroke="currentColor" stroke-width="1.4" viewBox="0 0 24 24"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
                    <span class="text-[8px] text-gray-500" style="font-family:'Patrick Hand',cursive;">Build.</span>
                  </div>
                </div>

                <!-- Two bottom cards: What matters Most + Reflection -->
                <div class="grid grid-cols-2 gap-2 mt-auto">
                  <!-- What matters Most -->
                  <div class="bg-[#F5EDE1] border border-amber-900/15 rounded-lg p-2.5 relative">
                    <div class="absolute -top-1.5 left-4 w-5 h-2 bg-[#D5C0A8]/70 rotate-[1deg]"></div>
                    <span class="text-[9px] font-semibold text-[#1C1917] block mb-1" style="font-family:'Patrick Hand',cursive;">What matters Most</span>
                    <ul class="text-[9px] text-[#2C2C2C] space-y-0.5" style="font-family:'Patrick Hand',cursive;">
                      <li>♥ The right problem</li>
                      <li>♥ The right assumptions</li>
                      <li>♥ The right people</li>
                    </ul>
                    <span class="absolute bottom-1.5 right-2 text-[9px] text-[#6B2137]/40">♡</span>
                  </div>
                  <!-- Reflection -->
                  <div class="flex flex-col gap-1">
                    <div class="bg-[#F8F2E8] border border-dashed border-amber-900/15 rounded-lg p-2">
                      <span class="text-[10px] font-semibold text-[#6B2137] underline underline-offset-2 block mb-0.5" style="font-family:'Patrick Hand',cursive;">Reflection ☆</span>
                      <p class="text-[8.5px] text-[#2C2C2C] leading-relaxed" style="font-family:'Patrick Hand',cursive;">
                        I measure progress by how much <span class="underline underline-offset-1 decoration-[#6B2137]/50 font-semibold">clarity</span> my thinking brings to each project.
                      </p>
                    </div>
                    <!-- small coffee + books sketch -->
                    <svg class="w-full h-10 text-[#6B2137]/25" viewBox="0 0 100 36" fill="none" stroke="currentColor" stroke-width="0.9">
                      <!-- coffee cup -->
                      <path stroke-linecap="round" d="M15 10h14l-2 14H17L15 10zm14 4h4a3 3 0 010 6h-4"/>
                      <!-- steam -->
                      <path stroke-linecap="round" d="M20 7c0-2 2-2 2-4M24 7c0-2 2-2 2-4"/>
                      <!-- books stack -->
                      <rect x="55" y="16" width="18" height="4" rx="0.5"/>
                      <rect x="57" y="12" width="14" height="4" rx="0.5"/>
                      <rect x="53" y="20" width="22" height="4" rx="0.5"/>
                      <!-- flower/twig -->
                      <path stroke-linecap="round" d="M82 30V18M82 18c-2-2-4-1-4-1s0 2 2 3M82 18c2-2 4-1 4-1s0 2-2 3M82 22c-1-1-3-1-3-1s0 2 2 2"/>
                    </svg>
                  </div>
                </div>

              </div>

              <!-- ══ PAGE 04 – Things I've Learned (RIGHT) ══ -->
              <div class="flex flex-col p-5 pl-4 overflow-hidden">

                <!-- Title + page num -->
                <div class="flex items-start justify-between mb-2.5">
                  <div>
                    <h3 class="text-[26px] font-bold text-[#1C1917] leading-none" style="font-family:'Outfit',sans-serif;">Things I've <span class="underline decoration-[#6B2137]/40 underline-offset-3">Learned.</span> <span class="text-[#6B2137]" style="font-size:18px;">♡</span></h3>
                    <div class="w-16 h-0.5 bg-[#6B2137]/30 mt-1 rounded-full"></div>
                  </div>
                  <span class="text-[9px] font-bold text-[#6B2137]/50 tracking-widest shrink-0 mt-0.5" style="font-family:'Outfit',sans-serif;">04</span>
                </div>

                <!-- 2x2 lesson cards -->
                <div class="grid grid-cols-2 gap-2 mb-2">
                  <!-- card: Code isn't everything -->
                  <div class="bg-[#F8F2E8] border border-amber-900/15 rounded-lg p-2.5 flex gap-2">
                    <div class="shrink-0 w-7 h-7 rounded-full bg-[#EDE3D4] border border-amber-900/15 flex items-center justify-center text-[#6B2137]">
                      <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
                    </div>
                    <div>
                      <p class="text-[9.5px] font-bold text-[#1C1917]" style="font-family:'Patrick Hand',cursive;">Code isn't everything.</p>
                      <p class="text-[8.5px] text-gray-500 leading-tight mt-0.5" style="font-family:'Patrick Hand',cursive;">Good code solves problems. Great code solves the right ones.</p>
                    </div>
                  </div>
                  <!-- card: Team over ego -->
                  <div class="bg-[#F8F2E8] border border-amber-900/15 rounded-lg p-2.5 flex gap-2">
                    <div class="shrink-0 w-7 h-7 rounded-full bg-[#EDE3D4] border border-amber-900/15 flex items-center justify-center text-[#6B2137]">
                      <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
                    </div>
                    <div>
                      <p class="text-[9.5px] font-bold text-[#1C1917]" style="font-family:'Patrick Hand',cursive;">Team over ego.</p>
                      <p class="text-[8.5px] text-gray-500 leading-tight mt-0.5" style="font-family:'Patrick Hand',cursive;">Not every contribution is visible in commits.</p>
                      <span class="text-[9px] text-[#6B2137]/40">♡</span>
                    </div>
                  </div>
                  <!-- card: Speed is temporary -->
                  <div class="bg-[#F8F2E8] border border-amber-900/15 rounded-lg p-2.5 flex gap-2">
                    <div class="shrink-0 w-7 h-7 rounded-full bg-[#EDE3D4] border border-amber-900/15 flex items-center justify-center text-[#6B2137]">
                      <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>
                    </div>
                    <div>
                      <p class="text-[9.5px] font-bold text-[#1C1917]" style="font-family:'Patrick Hand',cursive;">Speed is temporary.</p>
                      <p class="text-[8.5px] text-gray-500 leading-tight mt-0.5" style="font-family:'Patrick Hand',cursive;">Maintainability is permanent.</p>
                    </div>
                  </div>
                  <!-- card: Docs matter -->
                  <div class="bg-[#F8F2E8] border border-amber-900/15 rounded-lg p-2.5 flex gap-2">
                    <div class="shrink-0 w-7 h-7 rounded-full bg-[#EDE3D4] border border-amber-900/15 flex items-center justify-center text-[#6B2137]">
                      <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                    </div>
                    <div>
                      <p class="text-[9.5px] font-bold text-[#1C1917]" style="font-family:'Patrick Hand',cursive;">Docs matter.</p>
                      <p class="text-[8.5px] text-gray-500 leading-tight mt-0.5" style="font-family:'Patrick Hand',cursive;">Future you will thank you.</p>
                    </div>
                  </div>
                </div>

                <!-- Learning never ends card -->
                <div class="bg-[#F8F2E8] border border-amber-900/15 rounded-lg p-2.5 flex gap-2 mb-2">
                  <div class="shrink-0 w-7 h-7 rounded-full bg-[#EDE3D4] border border-amber-900/15 flex items-center justify-center text-[#6B2137]">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                  </div>
                  <div>
                    <p class="text-[9.5px] font-bold text-[#1C1917]" style="font-family:'Patrick Hand',cursive;">Learning never ends.</p>
                    <p class="text-[8.5px] text-gray-500 leading-tight mt-0.5" style="font-family:'Patrick Hand',cursive;">Stay curious. Stay adaptable.</p>
                  </div>
                </div>

                <!-- Working With Others + mountain polaroid -->
                <div class="grid grid-cols-2 gap-2 mt-auto">
                  <!-- Working With Others card -->
                  <div class="bg-[#F5EDE1] border border-amber-900/15 rounded-lg p-2.5 relative">
                    <div class="absolute -top-1.5 left-4 w-5 h-1.5 bg-[#D5C0A8]/60 rotate-[1deg]"></div>
                    <span class="text-[9px] font-semibold text-[#1C1917] block mb-1" style="font-family:'Patrick Hand',cursive;">Working With Others</span>
                    <ul class="text-[8.5px] text-[#2C2C2C] space-y-0.5" style="font-family:'Patrick Hand',cursive;">
                      <li>♥ Communicate clearly.</li>
                      <li>♥ Simplify decisions.</li>
                      <li>♥ Prevent mistakes early.</li>
                      <li>♥ Respect time.</li>
                    </ul>
                    <span class="absolute bottom-1.5 right-2 text-[9px] text-[#6B2137]/40">♡</span>
                  </div>
                  <!-- Impact Reminder + polaroid photo -->
                  <div class="flex flex-col gap-1.5">
                    <div class="bg-[#F5EDE1] border border-amber-900/15 rounded-lg p-2 relative">
                      <div class="absolute -top-1.5 left-3 w-1.5 h-4 bg-[#D5C0A8]/70 rounded-sm rotate-[-5deg]"></div>
                      <span class="text-[8px] font-semibold text-[#6B2137] block mb-0.5 text-center" style="font-family:'Patrick Hand',cursive;">Impact Reminder</span>
                      <p class="text-[8px] text-[#2C2C2C] leading-tight text-center" style="font-family:'Patrick Hand',cursive; font-style:italic;">Every project leaves behind more than software. It leaves behind trust.</p>
                    </div>
                    <!-- mountain polaroid -->
                    <div class="bg-white border border-gray-200 rounded-md p-1 shadow-sm rotate-[1.5deg]">
                      <div class="w-full h-14 rounded overflow-hidden bg-gray-100">
                        <img src="tobe.png" alt="Mountain" class="w-full h-full object-cover" onerror="this.style.display='none'; this.parentElement.style.background='#E5DDD4'"/>
                      </div>
                    </div>
                  </div>
                </div>

              </div>
            </div>
          </div>
'''

html = html[:s2_start] + SPREAD2_HTML + '\n          ' + html[s2_end_marker:]

# ─────────────────────────────────────────────────────────────────
# 4. SPREAD 3 – Story Writing (Pages 05 & 06)
# ─────────────────────────────────────────────────────────────────
s3_start = html.find('<!-- INNER PAGES SPREAD 3')
# find closing wrapper after spread 3
s3_end_marker = html.find('</div>\n        </div>\n      </div>', s3_start)
assert s3_start != -1 and s3_end_marker != -1, f"Spread 3 end not found, s3_start={s3_start}"

SPREAD3_HTML = '''<!-- INNER PAGES SPREAD 3 (PAGES 05 & 06 - STORY WRITING) -->
          <div id="smriti-spread-3" class="hidden w-full bg-[#FAF6EE] rounded-[14px] relative overflow-hidden text-left" style="height:520px; background-image: radial-gradient(#D8CFC3 1px, transparent 1px); background-size: 18px 18px;">

            <!-- Center Spine -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-px bg-amber-900/12 hidden md:block pointer-events-none"></div>

            <!-- X Close -->
            <button onclick="closeSmritiBook()" class="absolute top-2.5 right-3 text-gray-400 hover:text-[#6B2137] text-base z-40 transition-colors leading-none" title="Close Journal">✕</button>

            <div class="grid grid-cols-2 h-full">

              <!-- ══ PAGE 05 – Story Writing (LEFT) ══ -->
              <div class="flex flex-col p-5 pr-4 overflow-hidden">

                <!-- Page badge + title -->
                <div class="mb-2">
                  <span class="text-[9px] font-bold text-[#6B2137]/50 tracking-widest" style="font-family:'Outfit',sans-serif;">05</span>
                  <h3 class="text-[28px] font-bold text-[#1C1917] leading-none mt-0.5" style="font-family:'Outfit',sans-serif; letter-spacing:-0.2px;">Story Writing. <span class="text-[#6B2137]/30" style="font-family:'Great Vibes',cursive; font-size:20px;">✦</span></h3>
                  <div class="w-14 h-0.5 bg-[#6B2137]/30 mt-1 rounded-full"></div>
                </div>

                <!-- Tagline -->
                <p class="text-[10px] text-gray-500 mb-3 leading-relaxed" style="font-family:'Patrick Hand',cursive;">
                  weave words. leave worlds behind. <span class="text-[#6B2137]">♡</span>
                </p>

                <!-- Main wattpad.png illustration -->
                <div class="relative flex-1 rounded-lg overflow-hidden border border-amber-900/10 shadow-sm mb-3 group" style="min-height:180px; max-height:220px;">
                  <img src="wattpad.png" alt="Story Writing" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-[1.03]"/>
                  <div class="absolute inset-0 bg-gradient-to-t from-black/20 via-transparent to-transparent"></div>
                  <!-- pinned note overlay -->
                  <div class="absolute top-2.5 right-2.5 max-w-[100px] bg-[#FAF6EE]/92 p-2 rounded-md border border-amber-900/10 text-[8.5px] text-[#2C2C2C] shadow-sm" style="font-family:'Patrick Hand',cursive;">
                    the most beautiful stories come from the quiet places. 🌿
                  </div>
                </div>

                <!-- Wire-bound notebook note at bottom -->
                <div class="bg-[#F5EDE1] border border-amber-900/15 rounded-lg p-2.5 relative pl-7 shrink-0">
                  <!-- wire rings -->
                  <div class="absolute left-2 top-1.5 bottom-1.5 flex flex-col justify-evenly">
                    <div class="w-2 h-2 rounded-full border border-gray-300 bg-[#FAF6EE]"></div>
                    <div class="w-2 h-2 rounded-full border border-gray-300 bg-[#FAF6EE]"></div>
                    <div class="w-2 h-2 rounded-full border border-gray-300 bg-[#FAF6EE]"></div>
                  </div>
                  <p class="text-[9.5px] text-[#2C2C2C] leading-relaxed" style="font-family:'Patrick Hand',cursive;">
                    one page today, a whole universe tomorrow. <span class="text-[#6B2137]">♡</span>
                  </p>
                </div>
              </div>

              <!-- ══ PAGE 06 – My Story in Progress (RIGHT) ══ -->
              <div class="flex flex-col p-5 pl-4 overflow-hidden">

                <!-- Page badge -->
                <div class="flex justify-end mb-1.5">
                  <span class="text-[9px] font-bold text-[#6B2137]/50 tracking-widest" style="font-family:'Outfit',sans-serif;">06</span>
                </div>

                <!-- Heading -->
                <div class="mb-2.5">
                  <h4 class="text-[15px] text-[#6B2137]" style="font-family:'Great Vibes',cursive;">my story in progress ♡</h4>
                  <div class="w-28 h-0.5 bg-[#6B2137]/25 rounded-full mt-0.5"></div>
                </div>

                <!-- Taped title banner -->
                <div class="bg-[#F5EDE1] border border-amber-900/15 rounded-lg p-2.5 text-center relative mb-3">
                  <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-8 h-2.5 bg-[#D5C0A8]/70 rotate-[-1deg]"></div>
                  <h5 class="text-[11px] font-bold text-[#541C2E]" style="font-family:'Outfit',sans-serif;">The Threadweaver's Knot</h5>
                  <!-- small botanical right -->
                  <svg class="absolute right-2 top-1 w-4 h-6 text-[#6B2137]/30" fill="none" stroke="currentColor" stroke-width="1" viewBox="0 0 16 24">
                    <path stroke-linecap="round" d="M8 22V10M8 10c-2-2-4-1-4-1s0 2 2 3M8 10c2-2 4-1 4-1s0 2-2 3"/>
                  </svg>
                </div>

                <!-- Polaroids collage -->
                <div class="flex gap-2 mb-3 flex-1" style="min-height:0;">
                  <!-- big left polaroid -->
                  <div class="relative shrink-0" style="flex:1.5;">
                    <div class="absolute -top-1.5 left-1/2 -translate-x-1/2 w-7 h-2 bg-[#D5C0A8]/70 rotate-[-2deg] z-10"></div>
                    <div class="bg-white p-1.5 rounded-md shadow-md border border-gray-100 rotate-[-2deg] h-full">
                      <div class="w-full h-full min-h-[120px] rounded overflow-hidden bg-gray-100">
                        <img src="candle desk.jpe" alt="Cozy Writing" class="w-full h-full object-cover"/>
                      </div>
                    </div>
                  </div>
                  <!-- right stacked polaroids -->
                  <div class="flex flex-col gap-2 flex-1">
                    <div class="relative">
                      <div class="bg-white p-1 rounded-md shadow-sm border border-gray-100 rotate-[2.5deg]">
                        <div class="w-full h-[65px] rounded overflow-hidden bg-gray-100">
                          <img src="flowers.jpe" alt="Flowers" class="w-full h-full object-cover"/>
                        </div>
                      </div>
                    </div>
                    <div class="bg-white p-1 rounded-md shadow-sm border border-gray-100 rotate-[-1.5deg]">
                      <div class="w-full h-[65px] rounded overflow-hidden bg-gray-100">
                        <img src="write.png" alt="Manuscript" class="w-full h-full object-cover"/>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Wattpad link card -->
                <div class="bg-[#F5EDE1] border border-amber-900/15 rounded-lg p-2.5 relative shrink-0">
                  <!-- paperclip icon SVG (not emoji) -->
                  <div class="absolute -top-3 left-2.5">
                    <svg class="w-3.5 h-6 text-gray-400 -rotate-12" fill="none" stroke="currentColor" stroke-width="1.4" viewBox="0 0 14 28">
                      <path stroke-linecap="round" d="M7 26V8a4 4 0 00-8 0v14a7 7 0 0014 0V6"/>
                    </svg>
                  </div>
                  <div class="flex items-center justify-between mb-1.5">
                    <span class="text-[11px] text-[#6B2137]" style="font-family:'Great Vibes',cursive;">read my story on wattpad</span>
                    <span class="text-[10px] text-[#6B2137]/50">♡</span>
                  </div>
                  <a href="https://www.wattpad.com/story/411657344-the-threadweavers-knot" target="_blank" rel="noopener noreferrer"
                     class="flex items-center gap-2 bg-white/80 border border-amber-900/10 rounded-md px-2 py-1.5 hover:border-[#6B2137]/30 hover:shadow-sm transition-all group">
                    <!-- globe SVG -->
                    <svg class="w-3 h-3 text-gray-400 shrink-0 group-hover:text-[#6B2137]" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 010 20M12 2a15 15 0 000 20"/></svg>
                    <span class="text-[8px] text-gray-500 truncate group-hover:text-[#6B2137] underline" style="font-family:'Courier Prime','Courier New',monospace;">
                      wattpad.com/story/411657344-the-threadweavers-knot
                    </span>
                    <!-- quill SVG -->
                    <svg class="w-3.5 h-3.5 text-[#6B2137]/50 shrink-0 ml-auto" fill="none" stroke="currentColor" stroke-width="1.4" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"/>
                    </svg>
                  </a>
                </div>

              </div>
            </div>
          </div>
'''

html = html[:s3_start] + SPREAD3_HTML + '\n        </div>\n      </div>'  + html[s3_end_marker + len('</div>\n        </div>\n      </div>'):]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done! All three journal spreads + sidebar tabs rewritten to match reference images exactly!")
print("   - Spread 1 (About Me): consistent monospace body, Great Vibes cursive labels, muted SVG tech icons")
print("   - Spread 2 (On Building + Things I've Learned): journal card grid, sketch icons, hierarchy")
print("   - Spread 3 (Story Writing): wattpad.png, polaroid collage, quill SVG wattpad link")
print("   - Sidebar tabs: thin, narrow, muted rosewood tones")
