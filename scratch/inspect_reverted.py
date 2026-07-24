with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_pos = text.find('id="timeline-pin-section"')
sec_start = text.rfind('<section', 0, start_pos)
sec_end = text.find('</section>', start_pos) + len('</section>')

print(text[sec_start:sec_end])
