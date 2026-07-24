with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Shift the "I build premium" text block to the left (from left-[600px] to left-[480px])
content = content.replace(
    'class="absolute top-[850px] left-[600px] w-[350px] z-20 text-left"',
    'class="absolute top-[850px] left-[480px] w-[350px] z-20 text-left"'
)

# 2. Update seg-0 control points in buildJourneyPaths to stay high above the text
content = content.replace(
    """            // Control points: first goes down then swings right
            const cp1  = { x: drop.x - span * 0.05, y: drop.y + Math.abs(G_left.y - drop.y) * 0.55 };
            const cp2  = { x: G_left.x - span * 0.20, y: G_left.y - 30 };""",
    """            // Control points: first goes down then swings right (stay high above the text block)
            const cp1  = { x: drop.x + 200, y: drop.y + 40 };
            const cp2  = { x: G_left.x - 200, y: G_left.y - 250 };"""
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done shifting I build block and updating seg-0 path.")
