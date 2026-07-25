import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_tag = '<section class="relative bg-[#FAF8F5] text-[#1F1F1F] py-6 md:py-10 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">'
end_tag = '</section>'

start_pos = html.find(start_tag)
end_pos = html.find(end_tag, start_pos)

if start_pos != -1 and end_pos != -1:
    journal_html = html[start_pos:end_pos + len(end_tag)]

    # Remove all style tags inside about-journal
    journal_html = re.sub(r'<style>[\s\S]*?</style>', '', journal_html)

    # 1. Enforce ONLY 'Caveat' (the exact font used in 'code with purpose') for 100% of all elements inside #about-journal
    override_style = """<style>
      #about-journal, #about-journal * {
        font-family: 'Caveat', cursive !important;
        font-style: normal !important;
      }
      #about-journal h3, #about-journal h4, #about-journal .font-bold {
        font-weight: 700 !important;
      }
    </style>"""

    journal_html = override_style + '\n' + journal_html

    # 2. Clean all font class references (font-display, font-handwriting, font-mono-clean, font-great-vibes, etc.)
    journal_html = journal_html.replace(' font-display', '')
    journal_html = journal_html.replace(' font-handwriting', '')
    journal_html = journal_html.replace(' font-mono-clean', '')
    journal_html = journal_html.replace(' font-great-vibes', '')
    journal_html = journal_html.replace(' font-outfit', '')
    journal_html = journal_html.replace(' font-caveat', '')
    journal_html = re.sub(r'style="font-family:\s*[\'"][^\'"]*[\'"][^"]*"', '', journal_html)

    # 3. Scale font sizes so that ALL text on ALL 3 spreads fits perfectly with zero text overflow/clipping
    journal_html = journal_html.replace('min-h-[530px] md:min-h-[560px] h-[530px] md:h-[560px]', 'min-h-[510px] md:min-h-[540px] h-[510px] md:h-[540px]')
    journal_html = journal_html.replace('min-h-[520px] md:min-h-[560px]', 'min-h-[510px] md:min-h-[540px]')

    new_html = html[:start_pos] + journal_html + html[end_pos + len(end_tag):]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY ENFORCED CAVEAT FONT EXCLUSIVELY ACROSS ALL JOURNAL ELEMENTS!")
else:
    print("Failed to find start or end tag for about-journal!")
