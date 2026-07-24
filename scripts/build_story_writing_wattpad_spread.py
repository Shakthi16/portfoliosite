import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# -------------------------------------------------------------
# SPREAD 3 (PAGES 05 & 06 - STORY WRITING WITH WATTPAD.PNG & LINK)
# -------------------------------------------------------------
STORY_WRITING_SPREAD_HTML = """<!-- INNER PAGES SPREAD 3 (PAGES 05 & 06 - STORY WRITING WITH WATTPAD) -->
          <div id="smriti-spread-3" class="hidden w-full bg-[#FAF6EE] rounded-[18px] p-5 md:p-6 relative overflow-hidden text-left h-[495px] md:h-[525px] flex flex-col justify-between" style="background-image: radial-gradient(#D8CFC3 1.2px, transparent 1.2px); background-size: 20px 20px;">
            
            <!-- TOP-RIGHT CLOSE BUTTON '✕' -->
            <button onclick="closeSmritiBook()" class="absolute top-3 right-4 text-gray-500 hover:text-[#6B2137] text-lg font-bold z-40 p-1 transition-colors" title="Close Journal">
              ✕
            </button>

            <!-- Center Spine Line -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[1.5px] bg-amber-900/15 hidden md:block"></div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-5 md:gap-8 relative z-10 h-full overflow-y-auto md:overflow-hidden">
              
              <!-- PAGE 05: STORY WRITING (LEFT SIDE) -->
              <div class="flex flex-col justify-between text-left pr-0 md:pr-2 relative">
                <div>
                  <!-- Page Number Badge 05 & Header -->
                  <div class="flex items-center justify-between mb-1">
                    <span class="px-1.5 py-0.5 bg-[#E8D5CE] text-[#6B2137] font-bold text-[10px] rounded border border-[#D9BEB4]">05</span>
                  </div>

                  <div class="mb-2">
                    <h3 class="text-2xl md:text-3xl font-bold text-[#1F1F1F]" style="font-family: 'Patrick Hand', 'Great Vibes', cursive;">Story Writing. ヾ</h3>
                    <div class="w-16 h-0.5 bg-[#6B2137]/40 rounded-full mt-0.5"></div>
                  </div>

                  <p class="text-xs text-gray-600 mb-3" style="font-family: 'Patrick Hand', 'Great Vibes', cursive;">
                    weave words.<br/>leave worlds behind. <span class="text-[#6B2137]">♡</span>
                  </p>

                  <!-- Main Cozy Desk Illustration (wattpad.png) -->
                  <div class="relative w-full h-[220px] md:h-[240px] rounded-2xl overflow-hidden shadow-md border-2 border-white bg-amber-100/30 mb-2 group">
                    <img src="wattpad.png" alt="Story Writing Cozy Desk Illustration" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"/>
                    <div class="absolute inset-0 bg-gradient-to-t from-black/30 via-transparent to-transparent"></div>
                    
                    <!-- Wall Pinned Note -->
                    <div class="absolute top-3 right-3 max-w-[110px] bg-[#FAF6EE]/90 backdrop-blur-sm p-2 rounded-lg border border-amber-900/15 text-[9px] text-gray-800 shadow-sm" style="font-family: 'Patrick Hand', 'Great Vibes', cursive;">
                      the most beautiful stories come from the quiet places. 🌿
                    </div>
                  </div>
                </div>

                <!-- Bottom Spiral Wire Note -->
                <div class="bg-[#F6EFE6] p-2.5 rounded-xl border border-amber-900/15 shadow-sm relative pl-7" style="font-family: 'Patrick Hand', 'Great Vibes', cursive;">
                  <!-- Wire Coils on Left -->
                  <div class="absolute left-1.5 top-1.5 bottom-1.5 flex flex-col justify-between">
                    <div class="w-2 h-2 rounded-full border border-gray-400"></div>
                    <div class="w-2 h-2 rounded-full border border-gray-400"></div>
                    <div class="w-2 h-2 rounded-full border border-gray-400"></div>
                  </div>
                  <p class="text-xs text-[#2C2C2C] leading-tight">
                    one page today, a whole universe tomorrow. <span class="text-[#6B2137]">♡</span>
                  </p>
                </div>

              </div>

              <!-- PAGE 06: MY STORY IN PROGRESS & WATTPAD LINK (RIGHT SIDE) -->
              <div class="flex flex-col justify-between text-left pl-0 md:pl-2 relative">
                <div>
                  <!-- Page Badge 06 -->
                  <div class="flex justify-end mb-1">
                    <span class="px-1.5 py-0.5 bg-[#E8D5CE] text-[#6B2137] font-bold text-[10px] rounded border border-[#D9BEB4]">06</span>
                  </div>

                  <!-- Subtitle -->
                  <div class="text-center mb-3">
                    <h4 class="text-base text-[#6B2137] font-bold" style="font-family: 'Patrick Hand', 'Great Vibes', cursive;">my story in progress ♡</h4>
                    <div class="w-24 h-0.5 bg-[#6B2137]/30 mx-auto mt-0.5 rounded-full"></div>
                  </div>

                  <!-- Taped Story Banner -->
                  <div class="bg-[#F6EFE6] p-2.5 rounded-xl border border-amber-900/15 text-center relative shadow-sm mb-4">
                    <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-8 h-3 bg-[#E6D7C3]/90 rotate-[-1deg] border-l border-r border-white/60"></div>
                    <h5 class="text-sm font-bold text-[#541C2E]" style="font-family: 'Outfit', sans-serif;">The Threadweaver's Knot</h5>
                  </div>

                  <!-- Polaroids Grid -->
                  <div class="grid grid-cols-12 gap-2.5 items-center mb-3">
                    <!-- Main Left Polaroid -->
                    <div class="col-span-7 bg-white p-2 rounded-xl shadow-md border border-gray-200 rotate-[-2deg] relative">
                      <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-8 h-3 bg-[#E6D7C3]/80 rotate-[2deg] z-10"></div>
                      <div class="w-full h-[140px] rounded-lg overflow-hidden bg-gray-100">
                        <img src="candle desk.jpe" alt="Cozy Writing Polaroid" class="w-full h-full object-cover"/>
                      </div>
                    </div>

                    <!-- Right Stacked Polaroids -->
                    <div class="col-span-5 space-y-2">
                      <div class="bg-white p-1.5 rounded-lg shadow-sm border border-gray-200 rotate-[3deg]">
                        <div class="w-full h-[62px] rounded overflow-hidden bg-gray-100">
                          <img src="flowers.jpe" alt="Letters Polaroid" class="w-full h-full object-cover"/>
                        </div>
                      </div>
                      <div class="bg-white p-1.5 rounded-lg shadow-sm border border-gray-200 rotate-[-1deg]">
                        <div class="w-full h-[62px] rounded overflow-hidden bg-gray-100">
                          <img src="write.png" alt="Manuscript Polaroid" class="w-full h-full object-cover"/>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Wattpad Clickable Link Card (Bottom) -->
                <div class="bg-[#F8F3EA] p-3 rounded-2xl border border-amber-900/15 relative shadow-sm">
                  <!-- Paperclip Accent -->
                  <div class="absolute -top-3 left-3 text-gray-500 text-base transform -rotate-12">📎</div>

                  <div class="flex items-center justify-between mb-1">
                    <span class="text-xs text-[#6B2137] font-bold" style="font-family: 'Patrick Hand', 'Great Vibes', cursive;">read my story on wattpad</span>
                    <span class="text-xs text-[#6B2137]">♡</span>
                  </div>

                  <a href="https://www.wattpad.com/story/411657344-the-threadweaver's-knot" target="_blank" rel="noopener noreferrer" class="flex items-center gap-2 p-2 bg-white/90 rounded-xl border border-amber-900/10 hover:border-[#6B2137]/40 hover:shadow-md transition-all group">
                    <!-- Globe Icon -->
                    <span class="text-base text-gray-600 group-hover:text-[#6B2137]">🌐</span>
                    <span class="text-[10px] md:text-[11px] font-mono text-gray-700 underline truncate group-hover:text-[#6B2137]" style="font-family: 'Patrick Hand', cursive;">
                      https://www.wattpad.com/story/411657344-the-threadweaver's-knot
                    </span>
                    <!-- Quill Pen SVG -->
                    <svg class="w-4 h-4 text-[#6B2137] ml-auto shrink-0" fill="currentColor" viewBox="0 0 24 24"><path d="M2.5 19.5L6.5 19L18.5 7L17 5.5L5 17.5L2.5 19.5ZM19.2 6.3L17.7 4.8C17.3 4.4 16.7 4.4 16.3 4.8L15.3 5.8L18.2 8.7L19.2 7.7C19.6 7.3 19.6 6.7 19.2 6.3Z"/></svg>
                  </a>
                </div>

              </div>

            </div>

          </div>"""

# Replace smriti-spread-3 in index.html
content = re.sub(
    r'<div[^>]*id="smriti-spread-3"[^>]*>.*?</div>\s*</div>\s*</div>',
    STORY_WRITING_SPREAD_HTML + '\n        </div>\n      </div>',
    content,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully implemented Story Writing spread with wattpad.png, polaroids collage, and clickable Wattpad link!")
