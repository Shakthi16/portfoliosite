with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_hero = text.find('id="node-hero"')
if pos_hero != -1:
    print("node-hero snippet:")
    print(text[pos_hero-150:pos_hero+400])

pos_texthero = text.find('id="text-hero"')
if pos_texthero != -1:
    print("\ntext-hero snippet:")
    print(text[pos_texthero-150:pos_texthero+400])
