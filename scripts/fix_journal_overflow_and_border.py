import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_tag = '<section class="relative bg-[#FAF8F5] text-[#1F1F1F] py-6 md:py-10 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">'
end_tag = '</section>'

start_pos = html.find(start_tag)
end_pos = html.find(end_tag, start_pos)

if start_pos != -1 and end_pos != -1:
    journal_html = html[start_pos:end_pos + len(end_tag)]

    # 1. Reduce outer hardcover border frame size from p-2.5 md:p-3 to p-1 md:p-1.5
    journal_html = journal_html.replace(
        'class="relative w-full max-w-[860px] mx-auto rounded-[24px] p-2.5 md:p-3 shadow-[0_25px_70px_rgba(0,0,0,0.3)] border-2 border-[#3D1426] bg-[#3D1426]"',
        'class="relative w-full max-w-[890px] mx-auto rounded-[20px] p-1 md:p-1.5 shadow-[0_15px_40px_rgba(0,0,0,0.25)] border border-[#3D1426] bg-[#3D1426]"'
    )

    # 2. Increase spread container height so content never clips, and allow overflow-y-auto if needed
    journal_html = journal_html.replace(
        'h-[495px] md:h-[525px]',
        'min-h-[520px] md:min-h-[580px] h-auto'
    )

    # 3. Compact text font sizes so all handwriting fits inside the journal pages beautifully
    journal_html = journal_html.replace(
        'text-[13px] md:text-[14px]',
        'text-[11.5px] md:text-[12.5px]'
    )
    journal_html = journal_html.replace(
        'text-sm text-[#2C2C2C] font-medium mb-3',
        'text-xs text-[#2C2C2C] font-medium mb-1.5'
    )
    journal_html = journal_html.replace(
        'space-y-1.5 text-sm',
        'space-y-1 text-xs'
    )

    # 4. Make character illustration slightly more compact (h-[160px] md:h-[180px] -> h-[130px] md:h-[145px])
    journal_html = journal_html.replace(
        'h-[160px] md:h-[180px]',
        'h-[125px] md:h-[140px]'
    )
    journal_html = journal_html.replace(
        'w-[130px] md:w-[150px]',
        'w-[110px] md:w-[125px]'
    )

    # Replace in full HTML
    new_html = html[:start_pos] + journal_html + html[end_pos + len(end_tag):]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY FIXED JOURNAL OVERFLOW AND REDUCED BORDER SIZE!")
else:
    print("Failed to find start or end tag for about-journal!")
