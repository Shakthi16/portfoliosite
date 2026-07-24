with open('git_version.html', encoding='utf-8') as f:
    git_html = f.read()

# Extract skills section from git_version.html
skills_start = git_html.find('id="skills"')
sec_start = git_html.rfind('<section', 0, skills_start)

# Tag counting for section end
depth = 0
pos = sec_start
sec_end = -1
while pos < len(git_html):
    op = git_html.find('<section', pos)
    cl = git_html.find('</section>', pos)
    if op == -1 and cl == -1:
        break
    if op != -1 and (cl == -1 or op < cl):
        depth += 1
        pos = op + 1
    else:
        depth -= 1
        if depth == 0:
            sec_end = cl + len('</section>')
            break
        pos = cl + 1

skills_html = git_html[sec_start:sec_end]
print(f"Extracted skills section length: {len(skills_html)}")

with open('restored_skills_section.html', 'w', encoding='utf-8') as f:
    f.write(skills_html)
