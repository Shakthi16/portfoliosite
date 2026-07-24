import os

# Search the git_version.html for the skills/arsenal section which has the full original HTML
with open('git_version.html', encoding='utf-8') as f:
    raw = f.read()

terms = ['MY ARSENAL', 'id="skills"', 'PROGRAMMING', 'skillsDial', 'LLM Integration']
for t in terms:
    pos = raw.find(t)
    if pos != -1:
        print(f'Found "{t}" at pos {pos}')
        sec_start = raw.rfind('<section', 0, pos)
        print('Section start:', sec_start)
        print('Preview:', raw[sec_start:sec_start+250])
        print()
