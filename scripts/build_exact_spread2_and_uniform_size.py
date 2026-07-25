import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_tag = '<section class="relative bg-[#FAF8F5] text-[#1F1F1F] py-6 md:py-10 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">'
end_tag = '</section>'

start_pos = html.find(start_tag)
end_pos = html.find(end_tag, start_pos)

if start_pos != -1 and end_pos != -1:
    journal_html = html[start_pos:end_pos + len(end_tag)]

    # 1. Enforce exact uniform height across all 3 spread containers
    # (smriti-spread-1, smriti-spread-2, smriti-spread-3)
    uniform_class = 'class="w-full bg-[#FAF6EE] rounded-[18px] p-4 md:p-5 relative overflow-hidden text-left min-h-[530px] md:min-h-[560px] h-[530px] md:h-[560px] flex flex-col justify-between"'

    journal_html = re.sub(
        r'id="smriti-spread-1" class="[^"]*"',
        'id="smriti-spread-1" ' + uniform_class,
        journal_html
    )
    journal_html = re.sub(
        r'id="smriti-spread-2" class="[^"]*"',
        'id="smriti-spread-2" ' + uniform_class,
        journal_html
    )
    journal_html = re.sub(
        r'id="smriti-spread-3" class="[^"]*"',
        'id="smriti-spread-3" ' + uniform_class,
        journal_html
    )

    # 2. Build exact Spread 2 HTML matching reference mockup 100%
    new_spread_2_html = '''          <!-- INNER PAGES SPREAD 2 (EXACT IMAGE REFERENCE MATCH) -->
          <div id="smriti-spread-2" class="hidden w-full bg-[#FAF6EE] rounded-[18px] p-4 md:p-5 relative overflow-hidden text-left min-h-[530px] md:min-h-[560px] h-[530px] md:h-[560px] flex flex-col justify-between" style="background-image: radial-gradient(#D8CFC3 1.2px, transparent 1.2px); background-size: 20px 20px;">
            
            <!-- TOP-RIGHT CLOSE BUTTON '✕' -->
            <button onclick="closeSmritiBook()" class="absolute top-3 right-4 text-gray-500 hover:text-[#6B2137] text-lg font-bold z-40 p-1 transition-colors" title="Close Journal">
              ✕
            </button>

            <!-- Center Spine Stitch Line -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[1.5px] bg-amber-900/15 hidden md:block"></div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6 relative z-10 h-full overflow-y-auto md:overflow-hidden">
              
              <!-- PAGE 03: ON BUILDING. -->
              <div class="flex flex-col justify-between text-left pr-0 md:pr-2 h-full">
                <!-- Top Row: Page number 03 badge -->
                <div class="flex items-center justify-between mb-1">
                  <div>
                    <h3 class="text-2xl md:text-3xl font-bold text-[#1F1F1F]" style="font-family: 'Outfit', sans-serif;">On Building.</h3>
                    <p class="text-xs text-gray-500" style="font-family: 'Patrick Hand', cursive !important;">Journal Entry — 03</p>
                  </div>
                  <span class="px-2 py-0.5 bg-[#E8D5CE] text-[#6B2137] font-bold text-[10px] rounded border border-[#D9BEB4]">03</span>
                </div>

                <!-- Grid of Taped Note & Quote -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 items-center my-1">
                  <!-- Taped Quote Note with Botanical Sprig -->
                  <div class="bg-[#F6EFE6] p-2.5 rounded-xl border border-amber-900/15 shadow-2xs text-[11.5px] text-[#2C2C2C] relative" style="font-family: 'Patrick Hand', cursive !important;">
                    <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-7 h-2.5 bg-[#E6D7C3]/90 rotate-[-1deg]"></div>
                    <div class="absolute -top-3 -right-1 text-xs">🌿</div>
                    <span class="text-base text-[#6B2137] font-bold">“</span>
                    <p class="leading-tight inline">If a system becomes difficult to explain, it is usually becoming difficult to maintain.</p>
                    <span class="text-base text-[#6B2137] font-bold">”</span>
                  </div>

                  <!-- Top Right Text -->
                  <div class="text-[11.5px] text-[#2C2C2C] leading-snug" style="font-family: 'Patrick Hand', cursive !important;">
                    When I first started writing software, I believed engineering was about <span class="font-bold underline decoration-amber-900/40">finding answers.</span>
                  </div>
                </div>

                <!-- Bridge Sketch Illustration -->
                <div class="text-center my-1">
                  <svg class="w-full h-14 text-[#6B2137]/80 mx-auto" viewBox="0 0 160 45" fill="none" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.2" d="M10 38h140M35 10v28M125 10v28M10 28c25-15 50-15 70 0c20-15 45-15 70 0M35 10L10 28M35 10l35 18M125 10l-35 18M125 10l25 18"/>
                    <circle cx="110" cy="18" r="9" fill="#D98A8A" opacity="0.35" stroke="none"/>
                  </svg>
                </div>

                <!-- Middle Row: "I realised..." + "What matters Most" taped grid note -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 items-start my-1">
                  <div>
                    <span class="px-2 py-0.5 bg-[#E8D5CE] text-[#6B2137] text-[9.5px] font-bold rounded-full border border-[#D9BEB4]" style="font-family: 'Outfit', sans-serif;">I realised...</span>
                    <p class="text-[11.5px] text-[#2C2C2C] mt-1 mb-2 leading-tight" style="font-family: 'Patrick Hand', cursive !important;">Good engineering begins with understanding.</p>
                    <div class="flex items-center gap-2.5 text-[10px] text-gray-700 font-bold" style="font-family: 'Patrick Hand', cursive !important;">
                      <div class="text-center">👁️<br/>Observe.</div>
                      <div class="text-center">💡<br/>Understand.</div>
                      <div class="text-center">&lt;/&gt;<br/>Build.</div>
                    </div>
                  </div>

                  <!-- What matters Most Note -->
                  <div class="bg-[#F8F3EA] p-2.5 rounded-xl border border-amber-900/15 relative text-[11.5px] text-[#2C2C2C] shadow-2xs" style="font-family: 'Patrick Hand', cursive !important;">
                    <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-6 h-2.5 bg-[#E6D7C3]/90"></div>
                    <span class="font-bold text-[#1F1F1F] block mb-0.5 text-xs">What matters Most</span>
                    <ul class="space-y-0.5 text-[10.5px]">
                      <li>♥ The right problem</li>
                      <li>♥ The right assumptions</li>
                      <li>♥ The right people</li>
                    </ul>
                    <span class="absolute bottom-1 right-2 text-[10px] text-[#6B2137]">♡</span>
                  </div>
                </div>

                <!-- Bottom Reflection Box -->
                <div class="pt-1 border-t border-dashed border-amber-900/20 flex items-center justify-between gap-2">
                  <div>
                    <span class="px-2 py-0.5 bg-[#EFE5D8] text-[#6B2137] text-[9.5px] font-bold rounded-full" style="font-family: 'Outfit', sans-serif;">Reflection ✦</span>
                    <p class="text-[11.5px] text-[#2C2C2C] mt-0.5 leading-tight" style="font-family: 'Patrick Hand', cursive !important;">
                      I measure progress by how much <span class="bg-[#F6EFE6] px-1 rounded font-bold">clarity</span> my thinking brings to each project.
                    </p>
                  </div>
                  <!-- Coffee cup & books sketch -->
                  <div class="shrink-0 text-center text-base">☕📚</div>
                </div>
              </div>

              <!-- PAGE 04: THINGS I'VE LEARNED. ♡ -->
              <div class="flex flex-col justify-between text-left pl-0 md:pl-2 h-full">
                <!-- Header -->
                <div class="flex items-center justify-between mb-1">
                  <div>
                    <h3 class="text-2xl md:text-3xl font-bold text-[#1F1F1F]" style="font-family: 'Outfit', sans-serif;">Things I've Learned. ♡</h3>
                    <div class="w-20 h-0.5 bg-[#6B2137]/40 rounded-full"></div>
                  </div>
                  <span class="px-2 py-0.5 bg-[#E8D5CE] text-[#6B2137] font-bold text-[10px] rounded border border-[#D9BEB4]">04</span>
                </div>

                <!-- 6 Grid Cards Container (2 cols x 3 rows) -->
                <div class="grid grid-cols-2 gap-2 text-xs text-[#2C2C2C]" style="font-family: 'Patrick Hand', cursive !important;">
                  
                  <!-- Card 1: Code isn't everything -->
                  <div class="p-2 bg-white/80 rounded-xl border border-amber-900/15 shadow-2xs flex flex-col justify-between min-h-[75px]">
                    <div class="flex items-center justify-between mb-0.5">
                      <div class="w-5 h-5 rounded-full bg-[#E8D5CE] text-[#6B2137] text-[9px] font-bold flex items-center justify-center font-mono">&lt;/&gt;</div>
                    </div>
                    <div>
                      <h4 class="font-bold text-[11px] text-[#1F1F1F]">Code isn't everything.</h4>
                      <p class="text-[9.5px] text-gray-600 leading-tight">Good code solves problems. Great code solves the right ones.</p>
                    </div>
                    <div class="text-right text-xs opacity-70">🌸</div>
                  </div>

                  <!-- Card 2: Team over ego -->
                  <div class="p-2 bg-white/80 rounded-xl border border-amber-900/15 shadow-2xs flex flex-col justify-between min-h-[75px]">
                    <div class="flex items-center justify-between mb-0.5">
                      <div class="w-5 h-5 rounded-full bg-[#E8D5CE] text-[#6B2137] text-[9px] font-bold flex items-center justify-center">👥</div>
                      <span class="text-[9px] text-[#6B2137]">♡</span>
                    </div>
                    <div>
                      <h4 class="font-bold text-[11px] text-[#1F1F1F]">Team over ego.</h4>
                      <p class="text-[9.5px] text-gray-600 leading-tight">Not every contribution is visible in commits.</p>
                    </div>
                    <div class="text-right text-xs opacity-70">🤝</div>
                  </div>

                  <!-- Card 3: Speed is temporary -->
                  <div class="p-2 bg-white/80 rounded-xl border border-amber-900/15 shadow-2xs flex flex-col justify-between min-h-[75px]">
                    <div class="flex items-center justify-between mb-0.5">
                      <div class="w-5 h-5 rounded-full bg-[#E8D5CE] text-[#6B2137] text-[9px] font-bold flex items-center justify-center">🕒</div>
                    </div>
                    <div>
                      <h4 class="font-bold text-[11px] text-[#1F1F1F]">Speed is temporary.</h4>
                      <p class="text-[9.5px] text-gray-600 leading-tight">Maintainability is permanent.</p>
                    </div>
                    <div class="text-right text-xs opacity-70">⏱️</div>
                  </div>

                  <!-- Card 4: Docs matter -->
                  <div class="p-2 bg-white/80 rounded-xl border border-amber-900/15 shadow-2xs flex flex-col justify-between min-h-[75px]">
                    <div class="flex items-center justify-between mb-0.5">
                      <div class="w-5 h-5 rounded-full bg-[#E8D5CE] text-[#6B2137] text-[9px] font-bold flex items-center justify-center">📄</div>
                    </div>
                    <div>
                      <h4 class="font-bold text-[11px] text-[#1F1F1F]">Docs matter.</h4>
                      <p class="text-[9.5px] text-gray-600 leading-tight">Future you will thank you.</p>
                    </div>
                    <div class="text-right text-xs opacity-70">📖</div>
                  </div>

                  <!-- Card 5: Learning never ends -->
                  <div class="p-2 bg-white/80 rounded-xl border border-amber-900/15 shadow-2xs flex flex-col justify-between min-h-[75px]">
                    <div class="flex items-center justify-between mb-0.5">
                      <div class="w-5 h-5 rounded-full bg-[#E8D5CE] text-[#6B2137] text-[9px] font-bold flex items-center justify-center">🌱</div>
                    </div>
                    <div>
                      <h4 class="font-bold text-[11px] text-[#1F1F1F]">Learning never ends.</h4>
                      <p class="text-[9.5px] text-gray-600 leading-tight">Stay curious. Stay adaptable.</p>
                    </div>
                    <div class="text-right text-xs opacity-70">🌿</div>
                  </div>

                  <!-- Card 6: Working With Others Taped Note -->
                  <div class="p-2 bg-[#F6EFE6] rounded-xl border border-amber-900/15 shadow-2xs relative flex flex-col justify-between min-h-[75px]">
                    <div class="absolute -top-1.5 left-1/2 -translate-x-1/2 w-5 h-2 bg-[#E6D7C3]/90"></div>
                    <span class="font-bold text-[10.5px] text-[#6B2137] block mb-0.5">Working With Others</span>
                    <ul class="text-[9px] text-gray-700 space-y-0.5 leading-tight">
                      <li>♥ Communicate clearly.</li>
                      <li>♥ Simplify decisions.</li>
                      <li>♥ Prevent mistakes early.</li>
                      <li>♥ Respect time.</li>
                    </ul>
                    <span class="absolute bottom-1 right-1 text-[8px] text-[#6B2137]">♡</span>
                  </div>
                </div>

                <!-- Full Width Bottom Banner: Impact Reminder -->
                <div class="grid grid-cols-12 gap-2 items-center pt-1 border-t border-dashed border-amber-900/20">
                  <div class="col-span-8 bg-[#F6EFE6] p-2 rounded-xl border border-amber-900/15 text-xs text-[#2C2C2C] relative shadow-2xs" style="font-family: 'Patrick Hand', cursive !important;">
                    <div class="flex items-center gap-1 mb-0.5">
                      <span class="text-xs">📌</span>
                      <h4 class="font-bold text-[10.5px] text-[#6B2137] italic">Impact Reminder</h4>
                    </div>
                    <p class="text-[10px] text-gray-700 leading-tight">
                      Every project leaves behind more than software. It leaves behind trust.
                    </p>
                  </div>

                  <!-- Polaroid Photo (Mountain/Road Landscape View) -->
                  <div class="col-span-4 bg-white p-1 rounded-lg shadow-md border border-gray-200 rotate-[2deg] overflow-hidden relative">
                    <div class="absolute -top-1 left-1/2 -translate-x-1/2 w-5 h-1.5 bg-[#E6D7C3]/90 rotate-[-2deg] z-10"></div>
                    <img src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=250" alt="Mountain Landscape" class="w-full h-11 object-cover rounded-sm"/>
                  </div>
                </div>
              </div>

            </div>

          </div>'''

    spread2_pattern = r'<!-- INNER PAGES SPREAD 2 \(EXACT IMAGE 2 FONT & CREATIVE ARRANGEMENT\) -->[\s\S]*?(?=<!-- INNER PAGES SPREAD 3)'
    
    if re.search(spread2_pattern, journal_html):
        journal_html = re.sub(spread2_pattern, new_spread_2_html + '\n\n          ', journal_html)
    else:
        # Fallback search by id
        spread2_pattern2 = r'<div id="smriti-spread-2"[\s\S]*?(?=<div id="smriti-spread-3")'
        journal_html = re.sub(spread2_pattern2, new_spread_2_html + '\n\n          ', journal_html)

    new_html = html[:start_pos] + journal_html + html[end_pos + len(end_tag):]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY REBUILT SPREAD 2 & ENFORCED UNIFORM SIZE FOR ALL SPREADS!")
else:
    print("Failed to find start or end tag for about-journal!")
