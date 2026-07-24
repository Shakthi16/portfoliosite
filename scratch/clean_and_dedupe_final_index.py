with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Helper function to extract a section by id
def extract_section_by_id(full_html, sec_id):
    pos = full_html.find(f'id="{sec_id}"')
    if pos == -1:
        pos = full_html.find(f"id='{sec_id}'")
    if pos == -1:
        return ""
    sec_start = full_html.rfind('<section', 0, pos)
    sec_end = full_html.find('</section>', pos) + len('</section>')
    return full_html[sec_start:sec_end]

# Extract head & opening body
head_end = text.find('</head>') + len('</head>')
head_part = text[:head_end]

# Extract body up to first section
body_start = text.find('<body', head_end)
first_sec = text.find('<section', body_start)
body_top = text[head_end:first_sec]

# Extract closing scripts & body end
last_sec_end = text.rfind('</section>') + len('</section>')
scripts_bottom = text[last_sec_end:]

# Extract unique sections
sec_home = extract_section_by_id(text, 'home')
sec_journal = extract_section_by_id(text, 'about-journal')
sec_about = extract_section_by_id(text, 'about')
sec_timeline = extract_section_by_id(text, 'timeline-pin-section')
sec_academic = extract_section_by_id(text, 'academic-background')
sec_learning = extract_section_by_id(text, 'learning-in-motion')
sec_skills = extract_section_by_id(text, 'skills')
sec_achievements = extract_section_by_id(text, 'achievements')
sec_textmask = extract_section_by_id(text, 'text-mask-section')
sec_projects = extract_section_by_id(text, 'projects')
sec_contact = extract_section_by_id(text, 'contact')

ordered_sections = [
    sec_home,
    sec_journal,
    sec_about,
    sec_timeline,
    sec_academic,
    sec_learning,
    sec_skills,
    sec_achievements,
    sec_textmask,
    sec_projects,
    sec_contact
]

clean_sections = [s.strip() for s in ordered_sections if s.strip()]

new_full_html = head_part + body_top + '\n\n' + '\n\n'.join(clean_sections) + '\n\n' + scripts_bottom.strip() + '\n'

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_full_html)

print("Successfully deduped and cleaned index.html!")
