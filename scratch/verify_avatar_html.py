with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="path-traveler-avatar"')
if pos != -1:
    print(text[pos-100:pos+350])
