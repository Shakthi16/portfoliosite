with open('git_version.html', 'r', encoding='utf-8') as f:
    git_lines = f.readlines()

# Extract lines 4508 to 6500 (0-indexed: 4507 to end before script)
remaining_html = ''.join(git_lines[4507:5900])

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Attach right after #learning-in-motion section
if '</section>' in content and 'id="learning-in-motion"' in content:
    target = content.find('</section>', content.find('id="learning-in-motion"'))
    if target != -1:
        end_idx = target + len('</section>')
        content = content[:end_idx] + '\n\n' + remaining_html + content[end_idx:]
        print("Successfully attached skills, achievements, projects, and contact sections!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
