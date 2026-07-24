with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="timeline-pin-section"')
if start != -1:
    sec_start = text.rfind('<section', 0, start)
    sec_end = text.find('</section>', start) + len('</section>')
    print("Found section timeline-pin-section:")
    print(text[sec_start:sec_end])
else:
    print("Not found")
