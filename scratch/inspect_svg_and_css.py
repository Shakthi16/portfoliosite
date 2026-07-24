with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_svg = text.find('id="timeline-svg"')
if pos_svg != -1:
    print(text[pos_svg-300:pos_svg+600])

pos_jp = text.find('.journey-path')
if pos_jp != -1:
    print("\n.journey-path CSS:")
    print(text[pos_jp:pos_jp+300])
