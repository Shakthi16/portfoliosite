import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_tag = '<section class="relative bg-[#FAF8F5] text-[#1F1F1F] py-6 md:py-10 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">'
end_tag = '</section>'

start_pos = html.find(start_tag)
end_pos = html.find(end_tag, start_pos)

if start_pos != -1 and end_pos != -1:
    journal_html = html[start_pos:end_pos + len(end_tag)]

    new_spread1 = '''          <!-- INNER PAGES SPREAD 1 (EXACT HIGH-RES JOURNAL1.PNG IMAGE MATCH) -->
          <div id="smriti-spread-1" class="w-full bg-[#FAF6EE] rounded-[18px] p-1.5 md:p-2 relative overflow-hidden text-left min-h-[520px] md:min-h-[550px] h-[520px] md:h-[550px] flex items-center justify-center">
            
            <!-- HIGH-RES FULL SPREAD IMAGE JOURNAL1.PNG -->
            <img src="journal1.png" alt="Shakthi Sri Journal Page 1 &amp; 2" class="w-full h-full object-cover rounded-[16px] shadow-sm block"/>

            <!-- TOP-RIGHT CLOSE BUTTON '✕' -->
            <button onclick="closeSmritiBook()" class="absolute top-3 right-4 text-gray-600 hover:text-[#6B2137] text-lg font-bold z-40 p-1.5 bg-white/70 hover:bg-white rounded-full shadow-xs transition-colors" title="Close Journal">
              ✕
            </button>

            <!-- Center Spine Stitch Line Overlay -->
            <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[1.5px] bg-amber-900/15 hidden md:block"></div>
          </div>'''

    spread1_pattern = r'<!-- INNER PAGES SPREAD 1 [\s\S]*?(?=<!-- INNER PAGES SPREAD 2)'
    journal_html = re.sub(spread1_pattern, new_spread1 + '\n\n          ', journal_html)

    new_html = html[:start_pos] + journal_html + html[end_pos + len(end_tag):]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY INTEGRATED JOURNAL1.PNG IMAGE FOR SPREAD 1 PERFECTLY ALIGNED!")
else:
    print("Failed to find start or end tag for about-journal!")
