with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pos_mask = content.find('id="text-mask-section"')
if pos_mask != -1:
    sec_start = content.rfind('<section', 0, pos_mask)
    sec_end = content.find('</section>', pos_mask) + len('</section>')
    print("TEXT MASK SECTION HTML:")
    print(content[sec_start:sec_end])
    print("="*60)

pos_contact = content.find('id="contact"')
if pos_contact != -1:
    sec_start = content.rfind('<section', 0, pos_contact)
    sec_end = content.find('</section>', pos_contact) + len('</section>')
    print("CONTACT SECTION HTML:")
    print(content[sec_start:sec_end])
