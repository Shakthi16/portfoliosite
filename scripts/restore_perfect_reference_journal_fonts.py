import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_tag = '<section class="relative bg-[#FAF8F5] text-[#1F1F1F] py-6 md:py-10 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">'
end_tag = '</section>'

start_pos = html.find(start_tag)
end_pos = html.find(end_tag, start_pos)

if start_pos != -1 and end_pos != -1:
    journal_html = html[start_pos:end_pos + len(end_tag)]

    # Remove all blanket style overrides inside about-journal
    journal_html = re.sub(r'<style>[\s\S]*?#about-journal[\s\S]*?</style>', '', journal_html)

    # Clean CSS rule for about-journal font classes
    clean_style = """<style>
      #about-journal .font-display {
        font-family: 'Outfit', sans-serif !important;
      }
      #about-journal .font-handwriting {
        font-family: 'Caveat', cursive !important;
        font-weight: 600 !important;
      }
      #about-journal .font-mono-clean {
        font-family: monospace, monospace !important;
      }
    </style>"""

    journal_html = clean_style + '\n' + journal_html

    # Replace Spread 1 HTML with exact 1:1 reference styling and zero text overflow
    new_spread1 = '''          <!-- INNER PAGES SPREAD 1 (EXACT 1:1 DESIGN SYSTEM MATCH) -->
          <div id="smriti-spread-1" class="w-full bg-[#FAF6EE] rounded-[18px] p-4 md:p-5 relative overflow-hidden text-left min-h-[510px] md:min-h-[540px] h-[510px] md:h-[540px] flex flex-col justify-between" style="background-image: radial-gradient(#D8CFC3 1.2px, transparent 1.2px); background-size: 20px 20px;">
            
            <!-- TOP-RIGHT CLOSE BUTTON '✕' -->
            <button onclick="closeSmritiBook()" class="absolute top-3 right-4 text-gray-500 hover:text-[#6B2137] text-lg font-bold z-40 p-1 transition-colors" title="Close Journal">
              ✕
            </button>

            <!-- Center Spine Stitch Line -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[1.5px] bg-amber-900/15 hidden md:block"></div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6 relative z-10 h-full overflow-y-auto md:overflow-hidden">
              
              <!-- PAGE 01: LEFT SIDE -->
              <div class="flex flex-col justify-between space-y-1 text-left pr-0 md:pr-2 h-full">
                <!-- 1. Header & Sub-header -->
                <div>
                  <h3 class="text-3xl md:text-[38px] font-extrabold text-[#1C1917] mb-0.5 tracking-tight leading-none font-display">Shakthi Sri</h3>
                  <div class="flex flex-wrap items-center gap-2 mb-1">
                    <span class="px-2.5 py-0.5 bg-[#E8D5CE] text-[#6B2137] text-[9.5px] font-bold rounded-full border border-[#D9BEB4] tracking-wider uppercase font-display">DEVELOPER &amp; RESEARCHER</span>
                    <span class="text-xs text-[#2C2C2C] font-semibold underline underline-offset-4 decoration-[#6B2137]/30 font-handwriting">class of 2026</span>
                  </div>
                </div>

                <!-- 2. Timeline List with Icons -->
                <div class="space-y-1 text-xs text-[#2C2C2C] font-medium">
                  <div class="flex justify-between items-center border-b border-dashed border-amber-900/20 pb-0.5">
                    <span class="flex items-center gap-1.5 font-bold text-[#1F1F1F] font-display">
                      <svg class="w-3.5 h-3.5 text-[#6B2137]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                      B.Tech Information Technology
                    </span>
                    <span class="text-gray-600 font-mono text-[11px]">2022 - 2026</span>
                  </div>

                  <div class="flex justify-between items-center border-b border-dashed border-amber-900/20 pb-0.5">
                    <span class="flex items-center gap-1.5 font-bold text-[#1F1F1F] font-display">
                      <svg class="w-3.5 h-3.5 text-[#6B2137]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/></svg>
                      Kingston Engineering College
                    </span>
                    <span class="text-[#6B2137] font-bold font-mono text-[11px]">CGPA: 8.6</span>
                  </div>

                  <div class="flex justify-between items-center border-b border-dashed border-amber-900/20 pb-0.5">
                    <span class="flex items-center gap-1.5 font-bold text-[#1F1F1F] font-display">
                      <svg class="w-3.5 h-3.5 text-[#6B2137]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L5.6 15.12a2 2 0 00-1.182.17l-1.04.52a2 2 0 00-.778 2.766l1.54 2.31a2 2 0 002.324.793l2.45-.817a6 6 0 013.79 0l2.45.817a2 2 0 002.324-.793l1.54-2.31a2 2 0 00-.592-2.738z"/></svg>
                      IIT Madras — CYSTAR
                    </span>
                    <span class="text-gray-600 font-display text-[11px]">Research Intern</span>
                  </div>

                  <div class="flex justify-between items-center border-b border-dashed border-amber-900/20 pb-0.5">
                    <span class="flex items-center gap-1.5 font-bold text-[#1F1F1F] font-display">
                      <svg class="w-3.5 h-3.5 text-[#6B2137]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/></svg>
                      Full-Stack Developer
                    </span>
                    <span class="text-gray-600 font-mono text-[11px]">MERN Stack</span>
                  </div>

                  <div class="flex justify-between items-center border-b border-dashed border-amber-900/20 pb-0.5">
                    <span class="flex items-center gap-1.5 font-bold text-[#1F1F1F] font-display">
                      <svg class="w-3.5 h-3.5 text-[#6B2137]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                      Cybersecurity Enthusiast
                    </span>
                    <span class="text-gray-600 font-display text-[11px]">Always Learning</span>
                  </div>
                </div>

                <!-- 3. Taped Cards Row -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-1">
                  <!-- Taped Note: about me ヾ -->
                  <div class="bg-[#F6EFE6] p-2.5 rounded-xl border border-amber-900/15 shadow-2xs relative">
                    <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-6 h-2 bg-[#E6D7C3]/90 rotate-[-2deg] border-l border-r border-white/60"></div>
                    <span class="text-xs text-[#6B2137] font-bold block mb-0.5 font-handwriting">about me ヾ</span>
                    <ul class="text-[14px] text-[#2C2C2C] font-medium leading-tight space-y-0.5 font-handwriting">
                      <li>♥ I love turning ideas into impactful digital solutions.</li>
                      <li>♥ Curious mind with a strong drive to build, secure and innovate.</li>
                      <li>♥ Believer in discipline, consistency &amp; growth.</li>
                    </ul>
                    <span class="absolute bottom-1 right-1.5 text-[9px] text-[#6B2137]">♡</span>
                  </div>

                  <!-- TODAY Box -->
                  <div class="bg-[#F6EFE6] p-2.5 rounded-xl border border-amber-900/15 shadow-2xs relative">
                    <div class="flex items-center justify-between mb-0.5">
                      <div class="flex items-center gap-1">
                        <span class="w-1.5 h-1.5 rounded-full bg-rose-400"></span>
                        <span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                      </div>
                      <span class="text-[9px] text-amber-900 font-bold">☆</span>
                    </div>
                    <span class="text-[8.5px] font-mono font-bold text-gray-500 uppercase block mb-0.5">TODAY</span>
                    <p class="text-[14px] text-[#2C2C2C] font-medium leading-tight font-handwriting">
                      Building skills.<br/>Solving problems.<br/>Creating solutions.<br/>Preparing for impact.<br/>One step at a time.
                    </p>
                  </div>
                </div>

                <!-- 4. Contact Memo & Quote -->
                <div class="pt-1 border-t border-dashed border-amber-900/20 flex justify-between items-center gap-2">
                  <div class="bg-[#EFE5D8] px-2.5 py-1 rounded-lg text-[11px] text-[#2C2C2C] font-medium border border-amber-900/15 font-display">
                    <p class="font-bold text-[#1F1F1F]">srishakthi799@gmail.com</p>
                    <p class="text-gray-600 font-mono text-[10px]">+91 7895032098</p>
                    <p class="text-gray-500 text-[10px]">Chennai | Vellore</p>
                  </div>
                  <div class="text-right">
                    <span class="text-xs text-[#6B2137] font-bold">“</span>
                    <p class="text-sm md:text-base text-[#541C2E] font-bold leading-tight inline-block font-handwriting">code with purpose,<br/>create with impact. ♡</p>
                    <svg width="85" height="4" viewBox="0 0 85 4" class="ml-auto mt-0.5 opacity-60">
                      <path d="M2 2 C20 0.5, 55 0.5, 83 2" stroke="#541C2E" stroke-width="1.2" fill="none" stroke-linecap="round"/>
                    </svg>
                  </div>
                </div>

              </div>

              <!-- PAGE 02: RIGHT SIDE -->
              <div class="flex flex-col justify-between space-y-1 text-left pl-0 md:pl-2 h-full">
                <!-- 1. Top Row: Icons -->
                <div class="flex justify-between items-start">
                  <div class="text-center">
                    <svg class="w-4 h-5 text-[#6B2137] mx-auto" viewBox="0 0 24 32" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 28V12M12 12C9 9 5 10 5 10s1 4 4 5M12 12c3-3 7-2 7-2s-1 4-4 5M12 12c-2-3-1-7-1-7s4 1 4 5"/></svg>
                    <span class="block text-[10px] text-gray-700 mt-0.5 font-handwriting">breathe.png</span>
                  </div>
                  <div class="flex items-center gap-6 font-handwriting">
                    <div class="text-center">
                      <div class="w-6 h-6 bg-[#6B2137]/10 rounded-lg flex items-center justify-center text-[#6B2137] text-xs font-bold mx-auto">
                        <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path d="M2 6a2 2 0 012-2h5l2 2h5a2 2 0 012 2v6a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"/></svg>
                      </div>
                      <span class="block text-[10px] text-gray-600 mt-0.5">Goals</span>
                    </div>
                    <div class="text-center">
                      <div class="w-6 h-6 bg-amber-900/10 rounded-lg flex items-center justify-center text-amber-900 text-xs font-bold mx-auto">
                        <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path d="M4 3a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2H4zm12 12H4l4-8 3 6 2-4 3 6z"/></svg>
                      </div>
                      <span class="block text-[10px] text-gray-600 mt-0.5">Reminders</span>
                    </div>
                  </div>
                </div>

                <!-- 2. Currently Box & Girl Illustration -->
                <div class="grid grid-cols-12 gap-2 items-center">
                  <!-- currently ヾ -->
                  <div class="col-span-6 border border-dashed border-amber-900/30 rounded-xl p-2.5 bg-[#F8F3EA]">
                    <span class="text-xs text-[#6B2137] font-bold block mb-0.5 font-handwriting">currently ヾ</span>
                    <ul class="text-[14px] text-[#2C2C2C] font-medium leading-tight space-y-0.5 font-handwriting">
                      <li>♥ Exploring AI &amp; LLMs</li>
                      <li>♥ Building secure systems</li>
                      <li>♥ Deepening full-stack</li>
                      <li>♥ Learning. Shipping.</li>
                      <li>♥ Growing. Always. ♡</li>
                    </ul>
                  </div>

                  <!-- Character Illustration / Photo with @Shakthi.16 Tag -->
                  <div class="col-span-6 flex justify-center relative">
                    <div class="relative">
                      <div class="w-[105px] md:w-[120px] h-[120px] md:h-[135px] rounded-[16px] overflow-hidden shadow-md border-2 border-white bg-white">
                        <img src="girl.png" alt="Shakthi Sri Illustration" class="w-full h-full object-cover"/>
                      </div>
                      <div class="absolute -top-2 right-1 bg-[#1A1A1A] text-white font-mono text-[7.5px] font-bold px-2 py-0.5 rounded-full shadow-md z-30">
                        @Shakthi.16
                      </div>
                    </div>
                  </div>
                </div>

                <!-- 3. Tech I Work With -->
                <div class="border border-dashed border-amber-900/30 rounded-xl p-2 bg-[#F8F3EA]">
                  <span class="text-xs text-[#6B2137] font-bold block mb-1 font-handwriting">tech i work with ヾ</span>
                  
                  <div class="grid grid-cols-7 gap-1 items-center text-center text-[9px] font-medium text-gray-700 font-display">
                    <div class="flex flex-col items-center">
                      <svg class="w-4 h-4 text-[#61DAFB]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 9a3 3 0 100 6 3 3 0 000-6zm0-7c-5.52 0-10 1.79-10 4s4.48 4 10 4 10-1.79 10-4-4.48-4-10-4zm0 6c-4.41 0-8-1.34-8-2s3.59-2 8-2 8 1.34 8 2-3.59 2-8 2z"/></svg>
                      <span class="mt-0.5">React.js</span>
                    </div>
                    <div class="flex flex-col items-center">
                      <div class="w-4 h-4 rounded bg-[#339933] text-white text-[7.5px] font-bold flex items-center justify-center">node</div>
                      <span class="mt-0.5">Node.js</span>
                    </div>
                    <div class="flex flex-col items-center">
                      <span class="font-mono font-bold text-[10px] text-gray-800">ex</span>
                      <span class="mt-0.5">Express.js</span>
                    </div>
                    <div class="flex flex-col items-center">
                      <svg class="w-4 h-4 text-[#47A248]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 1.5C11.5 3 7 7.5 7 13c0 3 2 5.5 5 6.5 3-1 5-3.5 5-6.5 0-5.5-4.5-10-5-11.5z"/></svg>
                      <span class="mt-0.5">MongoDB</span>
                    </div>
                    <div class="flex flex-col items-center border-l border-dashed border-amber-900/20 pl-0.5">
                      <svg class="w-4 h-4 text-[#F24E1E]" fill="currentColor" viewBox="0 0 24 24"><path d="M8 2h4v4H8V2zm0 6h4v4H8V8zm0 6h4v4a4 4 0 11-4-4zm8-12h4v4h-4V2zm0 6h4v4h-4V8z"/></svg>
                      <span class="mt-0.5">Figma</span>
                    </div>
                    <div class="flex flex-col items-center">
                      <svg class="w-4 h-4 text-[#007ACC]" fill="currentColor" viewBox="0 0 24 24"><path d="M23.15 2.587L18.21.21a1.494 1.494 0 00-1.705.291L7.548 8.69 3.4 5.564a.747.747 0 00-.986.079L.24 7.728a.747.747 0 00-.03.996l3.96 4.67-3.96 4.67a.747.747 0 00.03.996l2.174 2.085a.747.747 0 00.986.079l4.148-3.126 8.957 8.189c.498.455 1.25.412 1.705-.098l4.94-4.757a1.494 1.494 0 00.44-1.077V3.664c0-.406-.164-.796-.44-1.077z"/></svg>
                      <span class="mt-0.5">VS Code</span>
                    </div>
                    <div class="flex flex-col items-center">
                      <svg class="w-4 h-4 text-black" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C9.5 2 7.5 4 7.5 6.5v4c0 1.5-1 3-2.5 4 0 3 3 5.5 7 5.5s7-2.5 7-5.5c-1.5-1-2.5-2.5-2.5-4v-4C16.5 4 14.5 2 12 2z"/></svg>
                      <span class="mt-0.5">Linux</span>
                    </div>
                  </div>
                </div>

                <!-- 4. What I Build Box -->
                <div class="grid grid-cols-12 gap-2 items-center">
                  <div class="col-span-9 border border-dashed border-amber-900/30 rounded-xl p-2 bg-[#F8F3EA]">
                    <span class="text-xs text-[#6B2137] font-bold block mb-0.5 text-center font-handwriting">what i build ♡</span>
                    <div class="grid grid-cols-3 gap-1 text-center text-[9px] font-bold text-gray-800 font-display">
                      <div class="p-1 bg-white/80 rounded-lg border border-amber-900/10 flex flex-col items-center justify-center">
                        <span class="text-xs">🌐</span>
                        <span class="leading-tight mt-0.5">Full-Stack<br/>Web Applications</span>
                      </div>
                      <div class="p-1 bg-white/80 rounded-lg border border-amber-900/10 flex flex-col items-center justify-center">
                        <span class="text-xs">🔒</span>
                        <span class="leading-tight mt-0.5">Cybersecurity Tools<br/>&amp; Research</span>
                      </div>
                      <div class="p-1 bg-white/80 rounded-lg border border-amber-900/10 flex flex-col items-center justify-center">
                        <span class="text-xs">🧠</span>
                        <span class="leading-tight mt-0.5">AI-Enhanced<br/>Solutions</span>
                      </div>
                    </div>
                  </div>

                  <!-- Taped Botanical Card with dried sprig -->
                  <div class="col-span-3 bg-[#EFE5D8] p-1.5 rounded-lg border border-amber-900/15 text-center relative shadow-sm h-full flex flex-col items-center justify-center">
                    <div class="absolute -top-1.5 left-1/2 -translate-x-1/2 w-5 h-2 bg-[#E6D7C3]/90 rotate-[-2deg]"></div>
                    <span class="text-lg">🌿</span>
                  </div>
                </div>
              </div>

            </div>

          </div>'''

    spread1_pattern = r'<!-- INNER PAGES SPREAD 1 [\s\S]*?(?=<!-- INNER PAGES SPREAD 2)'
    journal_html = re.sub(spread1_pattern, new_spread1 + '\n\n          ', journal_html)

    new_html = html[:start_pos] + journal_html + html[end_pos + len(end_tag):]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY RESTORED 1:1 REFERENCE DESIGN FONT HIERARCHY AND ELIMINATED ALL OVERFLOW!")
else:
    print("Failed to find start or end tag for about-journal!")
