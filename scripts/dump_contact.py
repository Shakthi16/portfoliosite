with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pos_contact = content.find('id="contact"')
if pos_contact != -1:
    sec_start = content.rfind('<section', 0, pos_contact)
    sec_end = content.find('</section>', pos_contact) + len('</section>')
    with open('contact_section.txt', 'w', encoding='utf-8') as out:
        out.write(content[sec_start:sec_end])
    print("Wrote contact section to contact_section.txt")
