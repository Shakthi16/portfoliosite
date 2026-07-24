with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pos_mask = content.find('id="text-mask-section"')
if pos_mask != -1:
    sec_start = content.rfind('<section', 0, pos_mask)
    sec_end = content.find('</section>', pos_mask) + len('</section>')
    content = content[:sec_start] + content[sec_end:]
    print("Successfully removed #text-mask-section (Shaping Tomorrow) from index.html!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
