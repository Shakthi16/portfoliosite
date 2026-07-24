import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_tag = '<section class="relative bg-[#FAF7F2] text-[#1F1F1F] py-6 md:py-10 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">'
end_tag = '</section>'

start_pos = html.find(start_tag)
end_pos = html.find(end_tag, start_pos)

if start_pos != -1 and end_pos != -1:
    journal_html = html[start_pos:end_pos + len(end_tag)]

    # Replace 'Great Vibes' and other handwriting fonts with 'Patrick Hand' for all handwriting text
    updated_journal = re.sub(
        r"font-family:\s*['\"][^'\"]*(?:Great Vibes|Caveat|Handlee|Pinyon Script|Brittany Signature)[^'\"]*['\"][^;]*;",
        "font-family: 'Patrick Hand', cursive !important;",
        journal_html
    )

    # Ensure main page section titles ("Shakthi Sri", "On Building.", "Story Writing.") use Outfit font
    updated_journal = updated_journal.replace(
        "font-family: 'Patrick Hand', cursive !important;\">On Building.",
        "font-family: 'Outfit', sans-serif !important;\ font-weight: 800;\">On Building."
    )
    updated_journal = updated_journal.replace(
        "font-family: 'Patrick Hand', cursive !important;\">Things I've Learned.",
        "font-family: 'Outfit', sans-serif !important;\ font-weight: 800;\">Things I've Learned."
    )
    updated_journal = updated_journal.replace(
        "font-family: 'Patrick Hand', cursive !important;\">\n                    Story",
        "font-family: 'Outfit', sans-serif !important;\ font-weight: 800;\">\n                    Story"
    )

    # Restore clean font sizing for Patrick Hand
    updated_journal = updated_journal.replace("text-sm text-[#2C2C2C] font-semibold", "text-[13px] md:text-[14px] text-[#2C2C2C] font-medium")
    updated_journal = updated_journal.replace("text-xs text-[#2C2C2C] font-semibold", "text-[12px] md:text-[13px] text-[#2C2C2C] font-medium")

    new_html = html[:start_pos] + updated_journal + html[end_pos + len(end_tag):]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY APPLIED PATRICK HAND TO JOURNAL TEXT!")
else:
    print("Failed to find start or end tag for about-journal!")
