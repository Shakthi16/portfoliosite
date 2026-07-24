with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_pin = text.find('id="timeline-pin-section"')
if pos_pin != -1:
    pos_sec_start = text.rfind('<section', 0, pos_pin)
    pos_sec_end = text.find('</section>', pos_pin) + len('</section>')
    print(text[pos_sec_start:pos_sec_end])
