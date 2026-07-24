with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

duplicate_block = """        <img src="face.png" alt="Traveling Avatar" class="w-full h-full object-contain filter drop-shadow-md"/>
      </div>
    </div>"""

if duplicate_block in content:
    content = content.replace(duplicate_block, "", 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Cleaned up duplicate face element snippet!")
