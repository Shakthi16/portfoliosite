with open('index.html', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines, 1):
    if ('id="about"' in line or 'id="home"' in line or 
        'id="about-journal"' in line or 'node-hero' in line or
        'timeline-container' in line):
        print(f'Line {i}: {line.rstrip()}')
