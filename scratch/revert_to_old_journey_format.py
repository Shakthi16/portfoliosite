with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

with open('restored_journey_section.html', 'r', encoding='utf-8') as f:
    old_journey_html = f.read().strip()

start_marker = 'id="timeline-pin-section"'
start_pos = text.find(start_marker)

if start_pos == -1:
    print("Error: timeline-pin-section not found in index.html")
    exit(1)

sec_start = text.rfind('<section', 0, start_pos)
sec_end = text.find('</section>', start_pos) + len('</section>')

print(f"Replacing current timeline section (chars {sec_start} to {sec_end}) with original restored_journey_section.html...")

updated_text = text[:sec_start] + old_journey_html + text[sec_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(updated_text)

print("Successfully reverted Professional Journey section back to the old format!")
