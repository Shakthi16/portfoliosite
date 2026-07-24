import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Make the title darker and bolder
content = content.replace(
    'font-weight: 600; color: #7a3a5e; letter-spacing: 0.1em; line-height: 1.4; margin-bottom: 15px; text-align: left; width: 100%; max-width: 160px;">LESSONS I\'M STILL<br>LEARNING</div>',
    'font-weight: 800; color: #2d1023; letter-spacing: 0.1em; line-height: 1.4; margin-bottom: 15px; text-align: left; width: 100%; max-width: 160px;">LESSONS I\'M STILL<br>LEARNING</div>'
)

# Make the list items darker and bolder
content = content.replace(
    'ul style="list-style: none; padding: 0; margin: 0; font-size: 10px; color: #582a4b; font-family: \'Manrope\', sans-serif !important; line-height: 1.8; text-align: left; width: 100%; max-width: 160px;">',
    'ul style="list-style: none; padding: 0; margin: 0; font-size: 10px; font-weight: 600; color: #2d1023; font-family: \'Manrope\', sans-serif !important; line-height: 1.8; text-align: left; width: 100%; max-width: 160px;">'
)

# Ensure bullets are also very dark
content = content.replace(
    '<span style="position: absolute; left: 0; top: 0; color: #421835;">•</span>',
    '<span style="position: absolute; left: 0; top: 0; color: #11040d;">•</span>'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Text contrast fixed.")
