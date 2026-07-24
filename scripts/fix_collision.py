with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update anchor points CR_l and CR_r to be 60px outside the Crafting text container (using -0.15 and 1.15)
content = content.replace(
    "const CR_l   = vb('#trigger-crafting', 0.05, 0.4);  // crafting text left",
    "const CR_l   = vb('#trigger-crafting', -0.15, 0.4);  // crafting text left"
)
content = content.replace(
    "const CR_r   = vb('#trigger-crafting', 0.95, 0.4);  // crafting text right",
    "const CR_r   = vb('#trigger-crafting', 1.15, 0.4);  // crafting text right"
)

# 2. Update SEG 1 control points to dip lower and stay completely clear of the paragraph text
content = content.replace(
    "const cp1  = { x: G_bot.x + span * 0.35, y: G_bot.y + 160 };\n            const cp2  = { x: O_r.x + 160,           y: O_r.y + 180   };",
    "const cp1  = { x: G_bot.x + span * 0.35, y: G_bot.y + 220 };\n            const cp2  = { x: O_r.x + 180,           y: O_r.y + 240   };"
)

# 3. Update SEG 4 control points to stay completely to the left and route cleanly above Crafting text
content = content.replace(
    "const cp1 = { x: GH_bot.x - 150, y: GH_bot.y + 10 };\n            const cp2 = { x: CR_l.x,         y: GH_bot.y + 10 };",
    "const cp1 = { x: GH_bot.x - 150, y: GH_bot.y + 5 };\n            const cp2 = { x: CR_l.x - 40,    y: GH_bot.y + 5 };"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done adjusting collision parameters.")
