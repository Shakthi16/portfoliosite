with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Revert text block position back to left-[600px]
content = content.replace(
    'class="absolute top-[850px] left-[480px] w-[350px] z-20 text-left"',
    'class="absolute top-[850px] left-[600px] w-[350px] z-20 text-left"'
)

# 2. Revert seg-0 control points back to what they were before the last change
content = content.replace(
    """            // Control points: first goes down then swings right (stay high above the text block)
            const cp1  = { x: drop.x + 200, y: drop.y + 40 };
            const cp2  = { x: G_left.x - 200, y: G_left.y - 250 };""",
    """            // Control points: first goes down then swings right
            const cp1  = { x: drop.x - span * 0.05, y: drop.y + Math.abs(G_left.y - drop.y) * 0.55 };
            const cp2  = { x: G_left.x - span * 0.20, y: G_left.y - 30 };"""
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Reverted the last change successfully.")
