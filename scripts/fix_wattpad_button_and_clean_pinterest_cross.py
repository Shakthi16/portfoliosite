import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_pos = html.find('<section class="relative bg-[#FAF8F5] text-[#1F1F1F] py-6 md:py-10 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">')
end_pos = html.find('</section>', start_pos)

if start_pos != -1:
    journal_html = html[start_pos:end_pos + len('</section>')]

    # 1. Update Wattpad button: move a little right
    new_button = '''<!-- WATTPAD INTERACTIVE LINK BUTTON EMBEDDED PERFECTLY ON DOTTED PLACEHOLDER LINE -->
            <a href="https://www.wattpad.com/story/411657344-the-threadweaver's-knot" target="_blank" rel="noopener noreferrer" 
               class="absolute bottom-[26px] md:bottom-[32px] right-[105px] md:right-[148px] z-40 bg-[#4A1224] hover:bg-[#6B2137] text-white font-bold text-[9.5px] sm:text-[10.5px] px-2.5 sm:px-3.5 py-0.5 sm:py-1 rounded-full shadow-md transition-all hover:scale-105 flex items-center gap-1 border border-amber-200/40 group">
              <span class="text-[#FF6122] font-black text-[10px] sm:text-xs">W</span>
              <span class="font-bold tracking-wide" style="font-family: 'Outfit', sans-serif !important;">Read on Wattpad ↗</span>
            </a>'''

    journal_html = re.sub(r'<!-- WATTPAD INTERACTIVE LINK BUTTON EMBEDDED PERFECTLY ON DOTTED PLACEHOLDER LINE -->[\s\S]*?</a>', new_button, journal_html)

    # 2. Replace all close buttons across spreads with clean Pinterest-style cross icon (no white circle background)
    clean_cross_btn = '''<button onclick="closeSmritiBook()" class="absolute top-3 right-4 text-[#541C2E] hover:text-[#6B2137] text-xl font-bold z-40 p-1 transition-all hover:scale-110 opacity-75 hover:opacity-100" title="Close Journal">
              ✕
            </button>'''

    journal_html = re.sub(r'<button onclick="closeSmritiBook\(\)" class="absolute top-3 right-4 [^>]*>[\s\S]*?✕[\s\S]*?</button>', clean_cross_btn, journal_html)

    new_html = html[:start_pos] + journal_html + html[end_pos + len('</section>'):]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY NUDGED WATTPAD BUTTON LITTLE RIGHT AND MADE CLOSE BUTTON A CLEAN PINTEREST CROSS (NO CIRCLE)!")
else:
    print("Failed to find about-journal section!")
