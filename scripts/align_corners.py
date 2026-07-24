with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update G_left definition to be the top-left corner of the Girl card (0.0, 0.0) instead of middle-left
content = content.replace(
    "const G_left = vb('#trigger-girl',     -0.02, 0.5); // girl card middle-left",
    "const G_left = vb('#trigger-girl',     0.0, 0.0); // girl card top-left corner"
)

# 2. Update SEG 1 to dip deep along the left edge of the Girl card and sweep under the text block
content = content.replace(
    """          // ─── SEG 1: Girl → Orbital ────────────────────────
          // From girl's middle-left, S-curve under "I build" heading, arrive at orbital right
          {
            const span = O_r.x - G_left.x;   // negative (left-moving)
            const cp1  = { x: G_left.x + span * 0.35, y: G_left.y + 220 };
            const cp2  = { x: O_r.x + 180,           y: O_r.y + 240   };
            setPath('seg-1',
              `M ${G_left.x} ${G_left.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${O_r.x} ${O_r.y}`
            );
            mv('n1-end', O_r.x, O_r.y);
          }""",
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
          }"""
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done updating endpoints and routing for top-left corner.")
