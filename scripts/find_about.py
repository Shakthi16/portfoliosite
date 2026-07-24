with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="about"' in line or 'editorial-canvas' in line or 'timeline-container' in line:
        print(f"Line {i+1}: {line.strip()[:80]}")
