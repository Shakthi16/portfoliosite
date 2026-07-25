import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_tag = '<section class="relative bg-[#FAF8F5] text-[#1F1F1F] py-6 md:py-10 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">'
end_tag = '</section>'

start_pos = html.find(start_tag)
end_pos = html.find(end_tag, start_pos)

if start_pos != -1 and end_pos != -1:
    journal_html = html[start_pos:end_pos + len(end_tag)]

    # Remove all previous style blocks inside about-journal
    journal_html = re.sub(r'<style>[\s\S]*?#about-journal[\s\S]*?</style>', '', journal_html)

    # Clean global CSS rule enforcing PATRICK HAND as the ONLY font on every single element in about-journal
    override_style = """<style>
      #about-journal, #about-journal * {
        font-family: 'Patrick Hand', cursive !important;
        font-style: normal !important;
      }
      #about-journal h3, #about-journal h4, #about-journal .font-bold {
        font-weight: 700 !important;
      }
    </style>"""

    journal_html = override_style + '\n' + journal_html

    # Clean any font-great-vibes, font-caveat, font-outfit classes from HTML elements inside journal
    journal_html = journal_html.replace('font-great-vibes ', '')
    journal_html = journal_html.replace('font-caveat ', '')
    journal_html = journal_html.replace('font-outfit ', '')
    journal_html = re.sub(r'font-family:\s*[\'"][^\'"]*[\'"]\s*(!important)?', "font-family: 'Patrick Hand', cursive !important", journal_html)

    # Re-apply clean title styling without Great Vibes wrappers
    journal_html = journal_html.replace('<span class="font-great-vibes text-4xl md:text-5xl text-[#6B2137]">Shakthi Sri</span>', 'Shakthi Sri')
    journal_html = journal_html.replace('<span class="font-great-vibes text-3xl md:text-4xl text-[#6B2137]">On Building.</span>', 'On Building.')
    journal_html = journal_html.replace("<span class=\"font-great-vibes text-3xl md:text-4xl text-[#6B2137]\">Things I've Learned. ♡</span>", "Things I've Learned. ♡")

    # Fit height nicely
    journal_html = journal_html.replace('min-h-[530px] md:min-h-[560px] h-[530px] md:h-[560px]', 'min-h-[510px] md:min-h-[540px] h-[510px] md:h-[540px]')
    journal_html = journal_html.replace('min-h-[520px] md:min-h-[560px]', 'min-h-[510px] md:min-h-[540px]')

    new_html = html[:start_pos] + journal_html + html[end_pos + len(end_tag):]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY ENFORCED EXACT PATRICK HAND FONT ACROSS ALL JOURNAL ELEMENTS!")
else:
    print("Failed to find start or end tag for about-journal!")
