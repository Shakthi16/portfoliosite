import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_tag = '<section class="relative bg-[#FAF8F5] text-[#1F1F1F] py-6 md:py-10 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">'
end_tag = '</section>'

start_pos = html.find(start_tag)
end_pos = html.find(end_tag, start_pos)

if start_pos != -1 and end_pos != -1:
    journal_html = html[start_pos:end_pos + len(end_tag)]

    # Clean existing style block inside about-journal
    journal_html = re.sub(r'<style>[\s\S]*?</style>', '', journal_html)

    # High contrast, BOLD Caveat font styling across ALL journal elements
    bold_style = """<style>
      #about-journal, #about-journal * {
        font-family: 'Caveat', cursive !important;
        font-style: normal !important;
        font-weight: 700 !important;
        color: #1C1917;
      }
      #about-journal h3, #about-journal h4 {
        color: #4A1224 !important;
        font-weight: 800 !important;
      }
      #about-journal .text-gray-500, #about-journal .text-gray-600 {
        color: #374151 !important;
      }
    </style>"""

    journal_html = bold_style + '\n' + journal_html

    # Adjust inner spread height to 520px / 550px and increase font size to 16px - 18px for crisp readability
    journal_html = journal_html.replace('text-[14px]', 'text-[16px]')
    journal_html = journal_html.replace('text-[13px]', 'text-[15px]')
    journal_html = journal_html.replace('text-xs text-[#2C2C2C]', 'text-[16px] text-[#1C1917]')
    journal_html = journal_html.replace('min-h-[510px] md:min-h-[540px] h-[510px] md:h-[540px]', 'min-h-[520px] md:min-h-[550px] h-[520px] md:h-[550px]')
    journal_html = journal_html.replace('min-h-[510px] md:min-h-[540px]', 'min-h-[520px] md:min-h-[550px]')

    new_html = html[:start_pos] + journal_html + html[end_pos + len(end_tag):]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY MADE ALL JOURNAL TEXT BOLD, CRISP, HIGH-CONTRAST & PERFECTLY ALIGNED!")
else:
    print("Failed to find start or end tag for about-journal!")
