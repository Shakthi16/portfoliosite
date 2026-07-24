with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("path-traveler-avatar in index.html:", 'path-traveler-avatar' in text)
print("face.png in index.html:", 'face.png' in text)
print("smriti-book-cover in index.html:", 'smriti-book-cover' in text)
print("text-mask-section in index.html:", 'text-mask-section' in text)
print("Shaping in index.html:", 'Shaping' in text)
