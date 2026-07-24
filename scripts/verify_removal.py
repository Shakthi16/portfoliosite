with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Is text-mask-section in content?", "text-mask-section" in content)
