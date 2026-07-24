with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_vas = text.find('updatePathAvatarScroll')
if pos_vas != -1:
    print(text[pos_vas:pos_vas+1200])
