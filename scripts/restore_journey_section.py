with open('index.html', encoding='utf-8') as f:
    html = f.read()

with open('restored_journey_section.html', encoding='utf-8') as f:
    journey_html = f.read()

with open('restored_learning_section.html', encoding='utf-8') as f:
    learning_html = f.read()

# Find the insertion point: after </section> of the about section, before <!-- ACHIEVEMENTS -->
# The about section ends with </section>\n\n\n    <!-- ACHIEVEMENTS -->
# Let's find the achievements section
ach_pos = html.find('<!-- ACHIEVEMENTS -->')
if ach_pos == -1:
    # try alternate
    ach_section_pos = html.find('id="achievements"')
    ach_pos = html.rfind('<section', 0, ach_section_pos)

print('Achievements pos:', ach_pos)
print('Context before achievements:')
print(repr(html[ach_pos-200:ach_pos+50]))

# Insert both sections right before achievements
insert_block = '\n\n' + journey_html.strip() + '\n\n' + learning_html.strip() + '\n\n'
new_html = html[:ach_pos] + insert_block + html[ach_pos:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print('Restored Professional Journey and Learning in Motion sections!')
print('New file size:', len(new_html))
