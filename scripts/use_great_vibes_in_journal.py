import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Locate section #about-journal
start_idx = html.find('id="about-journal"')
end_idx = html.find('</section>', start_idx)

if start_idx != -1 and end_idx != -1:
    journal_section = html[start_idx:end_idx]

    # Replace Patrick Hand, Handlee, Caveat with 'Great Vibes', cursive !important
    updated_journal = re.sub(
        r"font-family:\s*'(?:Patrick Hand|Handlee|Caveat|Pinyon Script)'(?:,\s*'(?:Handlee|Caveat|cursive)')*(?:\s*!important)?;",
        "font-family: 'Great Vibes', cursive !important;",
        journal_section
    )

    # Adjust font sizes slightly for Great Vibes readability if needed
    # (Great Vibes looks gorgeous at slightly larger sizes e.g. 14px-18px)
    updated_journal = updated_journal.replace("text-xs text-[#2C2C2C] font-medium mb-3", "text-sm text-[#2C2C2C] font-medium mb-3")

    html_updated = html[:start_idx] + updated_journal + html[end_idx:]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(html_updated)
    print("SUCCESSFULLY APPLIED GREAT VIBES FONT TO ABOUT-JOURNAL!")
else:
    print("Could not locate about-journal section!")
