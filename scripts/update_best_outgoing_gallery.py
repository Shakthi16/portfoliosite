with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

target = 'gallery: ["beststudent.png"]'
replacement = 'gallery: ["best_outgoing_award.jpg"]'

if target in html:
    html = html.replace(target, replacement)
    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("SUCCESSFULLY REPLACED GALLERY MOCKUP FOR BEST OUTGOING STUDENT!")
else:
    print("Target string not found in index.html")
