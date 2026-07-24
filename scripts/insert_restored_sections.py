import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('restored_learning_in_motion.html', 'r', encoding='utf-8') as f:
    lm_html = f.read()

with open('restored_skills_section.html', 'r', encoding='utf-8') as f:
    sk_html = f.read()

# 1. Remove old academic-background section if present
if 'id="academic-background"' in html:
    start_ab = html.find('<section', html.find('id="academic-background"') - 100)
    # Find matching </section>
    depth = 0
    pos = start_ab
    end_ab = -1
    while pos < len(html):
        op = html.find('<section', pos)
        cl = html.find('</section>', pos)
        if op == -1 and cl == -1:
            break
        if op != -1 and (cl == -1 or op < cl):
            depth += 1
            pos = op + 1
        else:
            depth -= 1
            if depth == 0:
                end_ab = cl + len('</section>')
                break
            pos = cl + 1
    if end_ab != -1:
        html = html[:start_ab] + html[end_ab:]
        print("Successfully removed old academic-background section!")

# 2. Check if learning-in-motion is already present, if not insert after timeline-pin-section (Professional Journey)
if 'id="learning-in-motion"' not in html:
    pos_timeline = html.find('id="timeline-pin-section"')
    if pos_timeline != -1:
        # Find end of timeline-pin-section
        start_tp = html.rfind('<section', 0, pos_timeline)
        depth = 0
        pos = start_tp
        end_tp = -1
        while pos < len(html):
            op = html.find('<section', pos)
            cl = html.find('</section>', pos)
            if op == -1 and cl == -1:
                break
            if op != -1 and (cl == -1 or op < cl):
                depth += 1
                pos = op + 1
            else:
                depth -= 1
                if depth == 0:
                    end_tp = cl + len('</section>')
                    break
                pos = cl + 1
        if end_tp != -1:
            html = html[:end_tp] + '\n\n' + lm_html + '\n\n' + html[end_tp:]
            print("Successfully inserted Learning in Motion section after Professional Journey!")

# 3. Check if id="skills" is present, if not insert after learning-in-motion
if 'id="skills"' not in html:
    pos_lm = html.find('id="learning-in-motion"')
    if pos_lm != -1:
        start_lm = html.rfind('<section', 0, pos_lm)
        depth = 0
        pos = start_lm
        end_lm = -1
        while pos < len(html):
            op = html.find('<section', pos)
            cl = html.find('</section>', pos)
            if op == -1 and cl == -1:
                break
            if op != -1 and (cl == -1 or op < cl):
                depth += 1
                pos = op + 1
            else:
                depth -= 1
                if depth == 0:
                    end_lm = cl + len('</section>')
                    break
                pos = cl + 1
        if end_lm != -1:
            html = html[:end_lm] + '\n\n' + sk_html + '\n\n' + html[end_lm:]
            print("Successfully inserted My Arsenal (skills) section after Learning in Motion!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Restoration complete!")
