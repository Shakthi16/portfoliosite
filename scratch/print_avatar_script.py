with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('updatePathAvatarScroll')
if pos != -1:
    print(text[pos:pos+1500])
