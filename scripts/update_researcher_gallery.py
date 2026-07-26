with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

target = 'gallery: ["bg1.png", "cystar.webp"]'
replacement = 'gallery: ["conference.png"]'

if target in html:
    html = html.replace(target, replacement)
    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("SUCCESSFULLY REPLACED RESEARCHER GALLERY MOCKUP WITH conference.png!")
else:
    print("Target string not found in index.html")
