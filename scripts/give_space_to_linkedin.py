import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Editorial canvas section height to 2950px
content = content.replace('id="about" style="min-height: 2700px;"', 'id="about" style="min-height: 2950px;"')
content = content.replace('id="timeline-container" style="height: 2700px;"', 'id="timeline-container" style="height: 2950px;"')
content = content.replace('id="timeline-svg" viewBox="0 0 1400 2700"', 'id="timeline-svg" viewBox="0 0 1400 2950"')

# 2. Adjust vertical positions of LinkedIn, GitHub, and Shavira cards + text blocks

# LinkedIn Card: top-[1400px] -> top-[1560px]
content = content.replace('top-[1400px] left-[80px]', 'top-[1560px] left-[80px]')

# LinkedIn Text: top-[1420px] left-[480px] -> top-[1580px] left-[480px]
content = content.replace('top-[1420px] left-[480px]', 'top-[1580px] left-[480px]')

# GitHub Card: top-[1840px] right-[80px] -> top-[2040px] right-[80px]
content = content.replace('top-[1840px] right-[80px]', 'top-[2040px] right-[80px]')

# GitHub Text: top-[1860px] right-[480px] -> top-[2060px] right-[480px]
content = content.replace('top-[1860px] right-[480px]', 'top-[2060px] right-[480px]')

# Shavira Card: top-[2280px] left-[80px] -> top-[2520px] left-[80px]
content = content.replace('top-[2280px] left-[80px]', 'top-[2520px] left-[80px]')

# Crafting Text: top-[2300px] left-[480px] -> top-[2540px] left-[480px]
content = content.replace('top-[2300px] left-[480px]', 'top-[2540px] left-[480px]')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully increased vertical spacing around LinkedIn card and lowered lower sections!")
