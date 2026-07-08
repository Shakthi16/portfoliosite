import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace flowers image
content = content.replace(
    '<img src="https://images.unsplash.com/photo-1490750967868-88cb44cb271b?q=80&w=400" alt="Flowers"',
    '<img src="flowers.jpe" alt="Flowers"'
)

# Replace candle desk image
content = content.replace(
    '<img src="https://images.unsplash.com/photo-1542841791-1925b02a2bf5?q=80&w=400" alt="Candle Desk"',
    '<img src="candle%20desk.jpe" alt="Candle Desk"'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Image URLs replaced with local JPE files.")
