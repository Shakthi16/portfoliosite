import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_tag = '<section class="relative bg-[#FAF8F5] text-[#1F1F1F] py-6 md:py-10 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">'
end_tag = '</section>'

start_pos = html.find(start_tag)
end_pos = html.find(end_tag, start_pos)

if start_pos != -1 and end_pos != -1:
    journal_html = html[start_pos:end_pos + len(end_tag)]

    # 1. Replace all Outfit / Inter font occurrences inside about-journal with Caveat
    journal_html = re.sub(
        r"style=\"font-family:\s*'Outfit'[^;]*;\"",
        "style=\"font-family: 'Caveat', cursive !important; font-weight: 700;\"",
        journal_html
    )

    # 2. Adjust font size and line height on Spread 1 Page 01 so NOTHING is clipped or hidden at the bottom
    # Reduce font size from 15px to 13.5px on dense sections
    journal_html = journal_html.replace('text-[15px]', 'text-[13.5px]')
    journal_html = journal_html.replace('text-[14.5px]', 'text-[13px]')
    journal_html = journal_html.replace('space-y-2.5', 'space-y-1.5')
    journal_html = journal_html.replace('space-y-1.5', 'space-y-1')
    journal_html = journal_html.replace('mb-2', 'mb-1')

    # 3. Save clean HTML
    new_html = html[:start_pos] + journal_html + html[end_pos + len(end_tag):]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY UNIFIED CAVEAT FONT AND FITTED ALL TEXT INSIDE JOURNAL PAGES!")
else:
    print("Failed to find start or end tag for about-journal!")
