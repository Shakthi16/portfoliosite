with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("On Building in content?", "On Building" in content)
print("Things I've Learned in content?", "Things I've Learned" in content)
print("Story Writing in content?", "Story Writing" in content)
