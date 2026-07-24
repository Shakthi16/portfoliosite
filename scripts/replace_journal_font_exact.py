import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_tag = '<section class="relative bg-[#FAF7F2] text-[#1F1F1F] py-6 md:py-10 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">'
end_tag = '</section>'

start_pos = html.find(start_tag)
end_pos = html.find(end_tag, start_pos)

if start_pos != -1 and end_pos != -1:
    journal_html = html[start_pos:end_pos + len(end_tag)]
    
    # Replace all font-family definitions that use Patrick Hand, Handlee, Caveat, etc. inside about-journal with Great Vibes
    updated_journal = re.sub(
        r"font-family:\s*['\"][^'\"]*Patrick Hand[^'\"]*['\"][^;]*;",
        "font-family: 'Great Vibes', cursive !important;",
        journal_html
    )
    updated_journal = re.sub(
        r"font-family:\s*['\"][^'\"]*Caveat[^'\"]*['\"][^;]*;",
        "font-family: 'Great Vibes', cursive !important;",
        updated_journal
    )
    updated_journal = re.sub(
        r"font-family:\s*['\"][^'\"]*Handlee[^'\"]*['\"][^;]*;",
        "font-family: 'Great Vibes', cursive !important;",
        updated_journal
    )

    # Scale font size slightly for Great Vibes elegance where text-[11px] or text-xs is used with handwriting
    updated_journal = updated_journal.replace("text-[11px] text-[#2C2C2C]", "text-sm text-[#2C2C2C] font-semibold")
    updated_journal = updated_journal.replace("text-[10px] text-[#2C2C2C]", "text-xs text-[#2C2C2C] font-semibold")

    new_html = html[:start_pos] + updated_journal + html[end_pos + len(end_tag):]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY APPLIED GREAT VIBES TO ALL JOURNAL TEXT!")
else:
    print("Failed to find start or end tag for about-journal!")
