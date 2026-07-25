import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_tag = '<div id="smriti-spread-3"'
end_tag = '</div>'

start_pos = html.find(start_tag)
end_pos = html.find('</div>\n\n        </div>', start_pos)

if start_pos != -1:
    old_spread3 = html[start_pos:end_pos + len('</div>')]

    # Replace wattpad button positioning to align perfectly inside the dotted placeholder line
    new_button = '''<!-- WATTPAD INTERACTIVE LINK BUTTON EMBEDDED PERFECTLY IN PLACEHOLDER -->
            <a href="https://www.wattpad.com/story/411657344-the-threadweaver's-knot" target="_blank" rel="noopener noreferrer" 
               class="absolute bottom-[16px] md:bottom-[22px] right-[65px] md:right-[105px] z-40 bg-[#4A1224] hover:bg-[#6B2137] text-white font-bold text-[11px] sm:text-xs px-3 sm:px-4 py-1 sm:py-1.5 rounded-full shadow-md transition-all hover:scale-105 flex items-center gap-1.5 border border-amber-200/40 group">
              <span class="text-[#FF6122] font-black text-xs sm:text-sm">W</span>
              <span class="font-bold tracking-wide" style="font-family: 'Outfit', sans-serif !important;">Read on Wattpad ↗</span>
            </a>'''

    # Replace old button tag inside spread 3
    updated_spread3 = re.sub(r'<!-- WATTPAD INTERACTIVE LINK BUTTON EMBEDDED IN PLACEHOLDER -->[\s\S]*?</a>', new_button, old_spread3)

    new_html = html[:start_pos] + updated_spread3 + html[end_pos + len('</div>'):]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY RE-POSITIONED WATTPAD BUTTON PERFECTLY INSIDE DOTTED PLACEHOLDER LINE!")
else:
    print("Failed to find spread 3!")
