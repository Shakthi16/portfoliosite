with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_line = -1
end_line = -1
for i, line in enumerate(lines):
    if 'id="timeline-pin-section"' in line:
        start_line = i + 1
        # find closing tag
        for j in range(i, len(lines)):
            if '</section>' in lines[j]:
                end_line = j + 1
                break
        break

print(f"timeline-pin-section starts at line {start_line} and ends at line {end_line}")
