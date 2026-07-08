import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Fix 1: Move Music Player and Vinyl higher up
# Find vinyl
content = content.replace(
    'style="bottom: -10%; right: -5%; z-index: 5; --rot: 15deg; scale: 0.9;"',
    'style="bottom: -2%; right: -2%; z-index: 5; --rot: 15deg; scale: 0.8;"'
)
# Find Music Player
content = content.replace(
    'style="bottom: 5%; right: 2%; z-index: 15; --rot: -4deg; transform-origin: bottom right; scale: 0.85;"',
    'style="bottom: 12%; right: 5%; z-index: 25; --rot: -4deg; transform-origin: bottom right; scale: 0.9;"'
)

# Fix 2: Replace broken Unsplash image links with working ones
content = content.replace(
    'https://images.unsplash.com/photo-1543788304-c5cb3673f4e2?q=80&w=400',
    'https://images.unsplash.com/photo-1490750967868-88cb44cb271b?q=80&w=400'
)
content = content.replace(
    'https://images.unsplash.com/photo-1603503362142-a82f3c3065d0?q=80&w=400',
    'https://images.unsplash.com/photo-1542841791-1925b02a2bf5?q=80&w=400'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Music card moved up and broken image links fixed.")
