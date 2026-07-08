import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Add Caveat font if not present
if "family=Caveat" not in content:
    content = content.replace(
        '<style>',
        '<style>\n    @import url(\'https://fonts.googleapis.com/css2?family=Caveat:wght@600&display=swap\');'
    )

# Adjust the wrapper padding to push text away from the wax seal
content = content.replace(
    'padding: 60px 40px 40px 60px;',
    'padding: 65px 20px 40px 85px;'
)

# Change the font size, font family, and line height of the list items
content = content.replace(
    'font-size: 10px; font-weight: 600; color: #2d1023; font-family: \'Manrope\', sans-serif !important; line-height: 1.8; text-align: left; width: 100%; max-width: 160px;">',
    'font-size: 15px; font-weight: 600; color: #2d1023; font-family: \'Caveat\', cursive !important; line-height: 1.4; text-align: left; width: 100%; max-width: 170px;">'
)

# Also update the title font to Caveat to match and make it slightly bigger
content = content.replace(
    'font-size: 9px; font-weight: 800; color: #2d1023; letter-spacing: 0.1em; line-height: 1.4; margin-bottom: 15px; text-align: left; width: 100%; max-width: 160px;">LESSONS I\'M STILL<br>LEARNING</div>',
    'font-size: 12px; font-weight: 800; color: #2d1023; letter-spacing: 0.1em; line-height: 1.2; margin-bottom: 15px; text-align: left; width: 100%; max-width: 170px; font-family: \'Manrope\', sans-serif !important;">LESSONS I\'M STILL<br>LEARNING</div>'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Font and padding adjusted for the Lessons note.")
