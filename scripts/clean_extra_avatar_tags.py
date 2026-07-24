with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

extra_block = """        <img src="face.png" alt="Traveling Avatar" class="w-full h-full object-contain filter drop-shadow-lg"/>
      </div>
    </div>"""

if extra_block in content:
    content = content.replace(extra_block, "", 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Cleaned up extra avatar tags!")
