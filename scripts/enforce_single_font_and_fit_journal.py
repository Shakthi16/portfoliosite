import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_tag = '<section class="relative bg-[#FAF8F5] text-[#1F1F1F] py-6 md:py-10 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">'
end_tag = '</section>'

start_pos = html.find(start_tag)
end_pos = html.find(end_tag, start_pos)

if start_pos != -1 and end_pos != -1:
    journal_html = html[start_pos:end_pos + len(end_tag)]

    # 1. Add global override style for about-journal to enforce Caveat font on EVERY element
    override_style = """<style>
      #about-journal, #about-journal * {
        font-family: 'Caveat', cursive !important;
      }
      #about-journal .font-mono {
        font-family: 'Caveat', cursive !important;
        font-weight: 700 !important;
      }
    </style>"""

    if '#about-journal, #about-journal *' not in journal_html:
        journal_html = override_style + '\n' + journal_html

    # 2. Replace any inline Outfit / Inter font-family references inside about-journal
    journal_html = re.sub(r'font-family:\s*[\'"][^\'"]*[\'"]\s*(!important)?', "font-family: 'Caveat', cursive !important", journal_html)

    # 3. Fine-tune Spreads to fit inside container without overflow or clipping
    # Spread 1 Page 01 spacing adjustments:
    journal_html = journal_html.replace('text-[13.5px]', 'text-[15px]')
    journal_html = journal_html.replace('text-[13px]', 'text-[14px]')
    journal_html = journal_html.replace('min-h-[530px] md:min-h-[560px] h-[530px] md:h-[560px]', 'min-h-[510px] md:min-h-[540px] h-[510px] md:h-[540px]')
    journal_html = journal_html.replace('min-h-[520px] md:min-h-[560px]', 'min-h-[510px] md:min-h-[540px]')

    new_html = html[:start_pos] + journal_html + html[end_pos + len(end_tag):]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY ENFORCED SINGLE CAVEAT FONT AND FITTED ALL JOURNAL PAGES!")
else:
    print("Failed to find start or end tag for about-journal!")
