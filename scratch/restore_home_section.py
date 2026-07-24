with open('git_version.html', 'r', encoding='utf-8', errors='ignore') as f:
    git_text = f.read()

pos_home_git = git_text.find('id="home"')
pos_home_git_end = git_text.find('</section>', pos_home_git) + len('</section>')
git_home_html = git_text[git_text.rfind('<section', 0, pos_home_git):pos_home_git_end]

with open('index.html', 'r', encoding='utf-8') as f:
    idx_text = f.read()

pos_home_idx = idx_text.find('id="home"')
pos_home_idx_end = idx_text.find('</section>', pos_home_idx) + len('</section>')

# Replace #home section in index.html with uncorrupted git_home_html
idx_text = idx_text[:idx_text.rfind('<section', 0, pos_home_idx)] + git_home_html + idx_text[pos_home_idx_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_text)

print("Successfully restored uncorrupted #home section from git_version.html!")
