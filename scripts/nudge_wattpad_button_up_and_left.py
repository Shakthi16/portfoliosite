import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_pos = html.find('<div id="smriti-spread-3"')
end_pos = html.find('</div>\n\n        </div>', start_pos)

if start_pos != -1:
    old_spread3 = html[start_pos:end_pos + len('</div>')]

    # Smaller button size, moved up to sit directly on the dotted line, and moved left away from the inkwell
    new_button = '''<!-- WATTPAD INTERACTIVE LINK BUTTON EMBEDDED PERFECTLY ON DOTTED PLACEHOLDER LINE -->
            <a href="https://www.wattpad.com/story/411657344-the-threadweaver's-knot" target="_blank" rel="noopener noreferrer" 
               class="absolute bottom-[22px] md:bottom-[30px] right-[95px] md:right-[140px] z-40 bg-[#4A1224] hover:bg-[#6B2137] text-white font-bold text-[9.5px] sm:text-[10.5px] px-2.5 sm:px-3.5 py-0.5 sm:py-1 rounded-full shadow-md transition-all hover:scale-105 flex items-center gap-1 border border-amber-200/40 group">
              <span class="text-[#FF6122] font-black text-[10px] sm:text-xs">W</span>
              <span class="font-bold tracking-wide" style="font-family: 'Outfit', sans-serif !important;">Read on Wattpad ↗</span>
            </a>'''

    updated_spread3 = re.sub(r'<!-- WATTPAD INTERACTIVE LINK BUTTON EMBEDDED PERFECTLY IN PLACEHOLDER -->[\s\S]*?</a>', new_button, old_spread3)

    new_html = html[:start_pos] + updated_spread3 + html[end_pos + len('</div>'):]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY NUDGED WATTPAD BUTTON UP, LEFT, AND REDUCED SIZE TO SIT PERFECTLY ON THE DOTTED LINE!")
else:
    print("Failed to find spread 3!")
