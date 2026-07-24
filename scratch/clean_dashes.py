with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

text = text.replace('IIT Madras  CYSTAR Lab', 'IIT Madras — CYSTAR Lab')
text = text.replace('OPERATIONS INTERN  AP AUTOMATION', 'OPERATIONS INTERN — AP AUTOMATION')
text = text.replace('', '—')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Cleaned up dashes in index.html!")
