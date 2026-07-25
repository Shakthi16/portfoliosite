import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_tag = '<section class="relative bg-[#FAF8F5] text-[#1F1F1F] py-6 md:py-10 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">'
end_tag = '</section>'

start_pos = html.find(start_tag)
end_pos = html.find(end_tag, start_pos)

if start_pos != -1 and end_pos != -1:
    journal_html = html[start_pos:end_pos + len(end_tag)]

    new_spread2_and_3 = '''          <!-- INNER PAGES SPREAD 2 (EXACT HIGH-RES JOURNAL2.PNG IMAGE MATCH) -->
          <div id="smriti-spread-2" class="hidden w-full bg-[#FAF6EE] rounded-[18px] p-1.5 md:p-2 relative overflow-hidden text-left min-h-[520px] md:min-h-[550px] h-[520px] md:h-[550px] flex items-center justify-center">
            
            <!-- HIGH-RES FULL SPREAD IMAGE JOURNAL2.PNG -->
            <img src="journal2.png" alt="Things I Learnt - Journal Page 3 &amp; 4" class="w-full h-full object-cover rounded-[16px] shadow-sm block"/>

            <!-- TOP-RIGHT CLOSE BUTTON '✕' -->
            <button onclick="closeSmritiBook()" class="absolute top-3 right-4 text-gray-600 hover:text-[#6B2137] text-lg font-bold z-40 p-1.5 bg-white/70 hover:bg-white rounded-full shadow-xs transition-colors" title="Close Journal">
              ✕
            </button>

            <!-- Center Spine Stitch Line Overlay -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[1.5px] bg-amber-900/15 hidden md:block"></div>
          </div>

          <!-- INNER PAGES SPREAD 3 (EXACT HIGH-RES JOURNAL3.PNG IMAGE MATCH WITH WATTPAD LINK) -->
          <div id="smriti-spread-3" class="hidden w-full bg-[#FAF6EE] rounded-[18px] p-1.5 md:p-2 relative overflow-hidden text-left min-h-[520px] md:min-h-[550px] h-[520px] md:h-[550px] flex items-center justify-center">
            
            <!-- HIGH-RES FULL SPREAD IMAGE JOURNAL3.PNG -->
            <img src="journal3.png" alt="Story Writing - Journal Page 5 &amp; 6" class="w-full h-full object-cover rounded-[16px] shadow-sm block"/>

            <!-- TOP-RIGHT CLOSE BUTTON '✕' -->
            <button onclick="closeSmritiBook()" class="absolute top-3 right-4 text-gray-600 hover:text-[#6B2137] text-lg font-bold z-40 p-1.5 bg-white/70 hover:bg-white rounded-full shadow-xs transition-colors" title="Close Journal">
              ✕
            </button>

            <!-- Center Spine Stitch Line Overlay -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[1.5px] bg-amber-900/15 hidden md:block"></div>

            <!-- WATTPAD INTERACTIVE LINK BUTTON EMBEDDED IN PLACEHOLDER -->
            <a href="https://www.wattpad.com/story/411657344-the-threadweaver's-knot" target="_blank" rel="noopener noreferrer" 
               class="absolute bottom-[36px] md:bottom-[42px] right-[50px] md:right-[75px] z-40 bg-[#4A1224] hover:bg-[#6B2137] text-white font-bold text-xs sm:text-sm px-3.5 sm:px-5 py-1.5 sm:py-2 rounded-full shadow-lg transition-all hover:scale-105 flex items-center gap-2 border border-amber-200/30 group">
              <span class="text-[#FF6122] font-black text-sm sm:text-base">W</span>
              <span class="font-bold tracking-wide" style="font-family: 'Outfit', sans-serif !important;">Read on Wattpad ↗</span>
            </a>
          </div>'''

    spread2_3_pattern = r'<!-- INNER PAGES SPREAD 2 [\s\S]*?(?=</div>\s*</div>\s*</div>\s*</section>)'
    journal_html = re.sub(spread2_3_pattern, new_spread2_and_3 + '\n\n        ', journal_html)

    new_html = html[:start_pos] + journal_html + html[end_pos + len(end_tag):]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY INTEGRATED JOURNAL2.PNG AND JOURNAL3.PNG WITH INTERACTIVE WATTPAD LINK!")
else:
    print("Failed to find start or end tag for about-journal!")
