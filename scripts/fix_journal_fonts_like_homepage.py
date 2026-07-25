import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_tag = '<section class="relative bg-[#FAF8F5] text-[#1F1F1F] py-6 md:py-10 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">'
end_tag = '</section>'

start_pos = html.find(start_tag)
end_pos = html.find(end_tag, start_pos)

if start_pos != -1 and end_pos != -1:
    journal_html = html[start_pos:end_pos + len(end_tag)]

    # Remove over-slanted forced italic style block
    journal_html = re.sub(r'<style>[\s\S]*?#about-journal[\s\S]*?</style>', '', journal_html)

    # Clean style rules inside about-journal
    new_style = """<style>
      #about-journal .font-great-vibes {
        font-family: 'Great Vibes', cursive !important;
        font-style: normal !important;
      }
      #about-journal .font-caveat {
        font-family: 'Caveat', cursive !important;
        font-style: normal !important;
        font-weight: 600 !important;
      }
      #about-journal .font-outfit {
        font-family: 'Outfit', sans-serif !important;
        font-style: normal !important;
      }
    </style>"""

    journal_html = new_style + '\n' + journal_html

    # Apply font-great-vibes to major cursive title headers:
    journal_html = journal_html.replace('Shakthi Sri</h3>', '<span class="font-great-vibes text-4xl md:text-5xl text-[#6B2137]">Shakthi Sri</span></h3>')
    journal_html = journal_html.replace('On Building.</h3>', '<span class="font-great-vibes text-3xl md:text-4xl text-[#6B2137]">On Building.</span></h3>')
    journal_html = journal_html.replace("Things I've Learned. ♡</h3>", "<span class=\"font-great-vibes text-3xl md:text-4xl text-[#6B2137]\">Things I've Learned. ♡</span></h3>")

    # Apply font-caveat to body text, list items, quotes, mementos (normal weight, no heavy forced italic slant)
    journal_html = re.sub(r'style="font-family:\s*\'Patrick Hand\'[^\"]*"', 'class="font-caveat"', journal_html)
    journal_html = re.sub(r'style="font-family:\s*\'Caveat\'[^\"]*"', 'class="font-caveat"', journal_html)

    new_html = html[:start_pos] + journal_html + html[end_pos + len(end_tag):]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY FIXED JOURNAL FONTS MATCHING HOMEPAGE HIERARCHY!")
else:
    print("Failed to find start or end tag for about-journal!")
