import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_tag = '<section class="relative bg-[#FAF8F5] text-[#1F1F1F] py-6 md:py-10 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">'
end_tag = '</section>'

start_pos = html.find(start_tag)
end_pos = html.find(end_tag, start_pos)

if start_pos != -1 and end_pos != -1:
    journal_html = html[start_pos:end_pos + len(end_tag)]

    # Replace 'Patrick Hand' with 'Caveat' inside about-journal
    updated_journal = journal_html.replace(
        "font-family: 'Patrick Hand', cursive !important;",
        "font-family: 'Caveat', cursive !important; font-weight: 600;"
    )
    updated_journal = updated_journal.replace(
        "font-family: 'Patrick Hand', cursive;",
        "font-family: 'Caveat', cursive !important; font-weight: 600;"
    )

    # Adjust font sizes slightly for Caveat readability (Caveat looks crisp and gorgeous at 14px - 17px)
    updated_journal = updated_journal.replace("text-[10.5px]", "text-[14px]")
    updated_journal = updated_journal.replace("text-[11px]", "text-[14.5px]")
    updated_journal = updated_journal.replace("text-[11.5px]", "text-[15px]")
    updated_journal = updated_journal.replace("text-xs text-[#2C2C2C]", "text-[15px] text-[#2C2C2C]")

    new_html = html[:start_pos] + updated_journal + html[end_pos + len(end_tag):]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY APPLIED CAVEAT FONT TO JOURNAL BOOK!")
else:
    print("Failed to find start or end tag for about-journal!")
