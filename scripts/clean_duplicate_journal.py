import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find first occurrence of #about-journal
first_pos = content.find('id="about-journal"')
if first_pos != -1:
    second_pos = content.find('id="about-journal"', first_pos + 20)
    if second_pos != -1:
        # Keep everything up to second_pos start comment and remove it
        start_cut = content.rfind('<!-- ABOUT ME: INTERACTIVE 3-PAGE JOURNAL BOOK', 0, second_pos)
        end_cut = content.find('</script>', second_pos) + len('</script>')
        if start_cut != -1 and end_cut != -1:
            content = content[:start_cut] + content[end_cut:]
            print("Successfully removed second duplicate #about-journal section!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
