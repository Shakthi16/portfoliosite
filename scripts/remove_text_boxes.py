import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. text-hero
content = re.sub(
    r'<div class="[^"]*" id="text-hero">',
    '<div class="absolute top-[120px] right-[80px] w-[480px] z-20 text-center" id="text-hero">',
    content
)

# 2. text-premium
content = re.sub(
    r'<div class="[^"]*" id="text-premium">',
    '<div class="absolute top-[970px] left-[380px] w-[440px] z-20 text-left" id="text-premium">',
    content
)

# 3. text-linkedin
content = re.sub(
    r'<div class="[^"]*" id="text-linkedin">',
    '<div class="absolute top-[1400px] left-[460px] w-[480px] z-20 text-left" id="text-linkedin">',
    content
)

# 4. text-github
content = re.sub(
    r'<div class="[^"]*" id="text-github">',
    '<div class="absolute top-[1840px] right-[460px] w-[480px] z-20 text-left" id="text-github">',
    content
)

# 5. trigger-crafting
content = re.sub(
    r'<div class="[^"]*" id="trigger-crafting">',
    '<div class="absolute top-[2280px] left-[460px] w-[480px] z-20 text-left" id="trigger-crafting">',
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully removed white frosted boxes around side text headings.")
