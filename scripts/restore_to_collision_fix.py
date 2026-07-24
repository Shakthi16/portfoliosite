with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update text block position back to left-[480px]
content = content.replace(
    'class="absolute top-[850px] left-[600px] w-[350px] z-20 text-left"',
    'class="absolute top-[850px] left-[480px] w-[350px] z-20 text-left"'
)

# 2. Set G_left back to middle-left (-0.02, 0.5)
content = content.replace(
    "const G_left = vb('#trigger-girl',     0.0, 0.0); // girl card top-left corner",
    "const G_left = vb('#trigger-girl',     -0.02, 0.5); // girl card middle-left"
)

# 3. Restore seg-0 control points to stay high
content = content.replace(
    """            // Control points: first goes down then swings right
            const cp1  = { x: drop.x - span * 0.05, y: drop.y + Math.abs(G_left.y - drop.y) * 0.55 };
            const cp2  = { x: G_left.x - span * 0.20, y: G_left.y - 30 };""",
    """            // Control points: first goes down then swings right (stay high above the text block)
            const cp1  = { x: drop.x + 200, y: drop.y + 40 };
            const cp2  = { x: G_left.x - 200, y: G_left.y - 250 };"""
)

# 4. Restore seg-1 control points to the previous standard dip
content = content.replace(
    """          // ─── SEG 1: Girl → Orbital ────────────────────────
          // From girl's top-left corner, dip deep along the card edge and sweep under the text block
          {
            const span = O_r.x - G_left.x;   // negative (left-moving)
            const cp1  = { x: G_left.x + span * 0.15, y: G_left.y + 400 };
            const cp2  = { x: O_r.x + 180,           y: O_r.y + 200   };
            setPath('seg-1',
              `M ${G_left.x} ${G_left.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${O_r.x} ${O_r.y}`
            );
            mv('n1-end', O_r.x, O_r.y);
          }""",
    """          // ─── SEG 1: Girl → Orbital ────────────────────────
          // From girl's middle-left, S-curve under "I build" heading, arrive at orbital right
          {
            const span = O_r.x - G_left.x;   // negative (left-moving)
            const cp1  = { x: G_left.x + span * 0.35, y: G_left.y + 160 };
            const cp2  = { x: O_r.x + 160,           y: O_r.y + 180   };
            setPath('seg-1',
              `M ${G_left.x} ${G_left.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${O_r.x} ${O_r.y}`
            );
            mv('n1-end', O_r.x, O_r.y);
          }"""
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Restored to the collision-free horizontal-shift state.")
