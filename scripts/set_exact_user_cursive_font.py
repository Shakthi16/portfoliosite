import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_tag = '<section class="relative bg-[#FAF8F5] text-[#1F1F1F] py-6 md:py-10 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">'
end_tag = '</section>'

start_pos = html.find(start_tag)
end_pos = html.find(end_tag, start_pos)

if start_pos != -1 and end_pos != -1:
    journal_html = html[start_pos:end_pos + len(end_tag)]

    # 1. Global CSS Rule enforcing Caveat (slanted cursive handwriting font) on ALL elements inside #about-journal
    override_style = """<style>
      #about-journal, #about-journal * {
        font-family: 'Caveat', cursive !important;
        font-style: italic !important;
      }
      #about-journal h3, #about-journal h4, #about-journal .font-bold {
        font-weight: 700 !important;
      }
    </style>"""

    # Remove existing style block if present
    journal_html = re.sub(r'<style>[\s\S]*?#about-journal[\s\S]*?</style>', '', journal_html)
    journal_html = override_style + '\n' + journal_html

    # Replace inline font declarations
    journal_html = re.sub(r'font-family:\s*[\'"][^\'"]*[\'"]\s*(!important)?', "font-family: 'Caveat', cursive !important", journal_html)

    # 2. Ensure container height fits pages without clipping
    journal_html = journal_html.replace('min-h-[530px] md:min-h-[560px] h-[530px] md:h-[560px]', 'min-h-[510px] md:min-h-[540px] h-[510px] md:h-[540px]')
    journal_html = journal_html.replace('min-h-[520px] md:min-h-[560px]', 'min-h-[510px] md:min-h-[540px]')

    new_html = html[:start_pos] + journal_html + html[end_pos + len(end_tag):]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY APPLIED EXACT USER CURSIVE FONT (CAVEAT ITALIC) TO ALL JOURNAL ELEMENTS!")
else:
    print("Failed to find start or end tag for about-journal!")
