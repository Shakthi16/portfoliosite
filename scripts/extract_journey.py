with open('build_full_restored_sections.py', encoding='utf-8') as f:
    raw = f.read()

# Find "learning in motion"
lm_pos = raw.lower().find('learning in motion')
print('Learning in Motion at:', lm_pos)
if lm_pos > 0:
    # walk back to section
    sec_start = raw.rfind('<section', 0, lm_pos)
    print('Section start:', sec_start)
    print('Preview:', raw[sec_start:sec_start+300])
    
    # Extract full section
    chunk = raw[sec_start:]
    depth = 0
    pos = 0
    result_end = -1
    while pos < len(chunk):
        open_pos = chunk.find('<section', pos)
        close_pos = chunk.find('</section>', pos)
        if open_pos == -1 and close_pos == -1:
            break
        if open_pos != -1 and (close_pos == -1 or open_pos < close_pos):
            depth += 1
            pos = open_pos + 1
        else:
            depth -= 1
            if depth == 0:
                result_end = close_pos + len('</section>')
                break
            pos = close_pos + 1

    if result_end != -1:
        learning_html = chunk[:result_end]
        print('Extracted Learning in Motion section length:', len(learning_html))
        with open('restored_learning_section.html', 'w', encoding='utf-8') as f:
            f.write(learning_html)
        print('Saved to restored_learning_section.html')
