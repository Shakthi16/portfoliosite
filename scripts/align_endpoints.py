with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the static center dot inside the orbital object
content = content.replace(
    '<div class="w-4 h-4 rounded-full bg-[#421835] mb-3 shadow-[0_0_15px_rgba(66,24,53,0.4)]"></div>',
    ''
)

# 2. Convert Shavira card tag from <a> to <div> to remove the link
content = content.replace(
    '<!-- 8. SHAVIRA CARD (Bottom Right) -->\n<div class="absolute top-[2050px] left-[80px] w-[340px] z-30 hover-card" id="trigger-shavira">\n<a class="bg-white/80 backdrop-blur-xl rounded-[32px] p-8 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.04)] flex flex-col justify-between h-[320px] w-full text-black transform transition-all duration-500 hover:-translate-y-3 cursor-pointer border border-white/60 hover:shadow-[0_40px_80px_-15px_rgba(66,24,53,0.1)] block" href="https://www.instagram.com/shaviraworks" target="_blank">',
    '<!-- 8. SHAVIRA CARD (Bottom Right) -->\n<div class="absolute top-[2050px] left-[80px] w-[340px] z-30 hover-card" id="trigger-shavira">\n<div class="bg-white/80 backdrop-blur-xl rounded-[32px] p-8 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.04)] flex flex-col justify-between h-[320px] w-full text-black transform transition-all duration-500 hover:-translate-y-3 border border-white/60 hover:shadow-[0_40px_80px_-15px_rgba(66,24,53,0.1)] block">'
)

content = content.replace(
    '</a>\n</div>\n</div>\n<!-- Mobile Fallback (Hidden on Desktop) -->',
    '</div>\n</div>\n</div>\n<!-- Mobile Fallback (Hidden on Desktop) -->'
)

# 3. Update buildJourneyPaths variables
content = content.replace(
    """          const H_bot  = vb('#node-hero',        0.35, 1.02); // hero card bottom, 35% from left
          const G_top  = vb('#trigger-girl',     0.12, 0.0);  // girl card top-left corner
          const G_bot  = vb('#trigger-girl',     0.12, 1.0);  // girl card bottom-left
          const O_r    = vb('#trigger-orbital',  1.05, 0.5);  // orbital right edge
          const O_bot  = vb('#trigger-orbital',  0.35, 1.02); // orbital bottom""",
    """          const H_bot  = vb('#node-hero',        0.35, 1.02); // hero card bottom, 35% from left
          const G_left = vb('#trigger-girl',     -0.02, 0.5); // girl card middle-left
          const O_r    = vb('#trigger-orbital',  1.05, 0.5);  // orbital right edge"""
)

# Update guard checks
content = content.replace(
    "if (!H_bot || !G_top || !G_bot || !O_r || !O_bot ||",
    "if (!H_bot || !G_left || !O_r ||"
)

# Update seg-0 builder
content = content.replace(
    """          // ─── SEG 0: Hero → Girl ─────────────────────────────
          // Drop from hero bottom, large elegant clockwise sweep
          {
            const drop = { x: H_bot.x, y: H_bot.y + 35 };
            // Horizontal span
            const span = G_top.x - drop.x;
            // Control points: first goes down then swings right
            const cp1  = { x: drop.x - span * 0.05, y: drop.y + Math.abs(G_top.y - drop.y) * 0.55 };
            const cp2  = { x: G_top.x - span * 0.20, y: G_top.y - 30 };
            setPath('seg-0',
              `M ${H_bot.x} ${H_bot.y} L ${drop.x} ${drop.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${G_top.x} ${G_top.y}`
            );
            mv('n0-end', G_top.x, G_top.y);
          }""",
    """          // ─── SEG 0: Hero → Girl ─────────────────────────────
          // Drop from hero bottom, large elegant clockwise sweep
          {
            const drop = { x: H_bot.x, y: H_bot.y + 35 };
            // Horizontal span
            const span = G_left.x - drop.x;
            // Control points: first goes down then swings right
            const cp1  = { x: drop.x - span * 0.05, y: drop.y + Math.abs(G_left.y - drop.y) * 0.55 };
            const cp2  = { x: G_left.x - span * 0.20, y: G_left.y - 30 };
            setPath('seg-0',
              `M ${H_bot.x} ${H_bot.y} L ${drop.x} ${drop.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${G_left.x} ${G_left.y}`
            );
            mv('n0-end', G_left.x, G_left.y);
          }"""
)

# Update seg-1 builder
content = content.replace(
    """          // ─── SEG 1: Girl → Orbital ────────────────────────
          // From girl's bottom-left, S-curve under "I build" heading, arrive at orbital right
          {
            const span = O_r.x - G_bot.x;   // negative (left-moving)
            const dy   = O_r.y - G_bot.y;
            const cp1  = { x: G_bot.x + span * 0.35, y: G_bot.y + 220 };
            const cp2  = { x: O_r.x + 180,           y: O_r.y + 240   };
            setPath('seg-1',
              `M ${G_bot.x} ${G_bot.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${O_r.x} ${O_r.y}`
            );
            mv('n1-end', O_r.x, O_r.y);
          }""",
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
          }"""
)

# Update seg-2 builder to start from O_r (orbital right) instead of O_bot
content = content.replace(
    """          // ─── SEG 2: Orbital → LinkedIn ────────────────────
          // Short graceful arc dropping left and down
          {
            const dy  = LI_top.y - O_bot.y;
            const cp1 = { x: O_bot.x - 25, y: O_bot.y + dy * 0.45 };
            const cp2 = { x: LI_top.x + 30, y: LI_top.y - 25 };
            setPath('seg-2',
              `M ${O_bot.x} ${O_bot.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${LI_top.x} ${LI_top.y}`
            );
            mv('n2-end', LI_top.x, LI_top.y);
          }""",
    """          // ─── SEG 2: Orbital → LinkedIn ────────────────────
          // Short graceful arc dropping left and down from orbital right edge
          {
            const dy  = LI_top.y - O_r.y;
            const cp1 = { x: O_r.x - 25, y: O_r.y + dy * 0.45 };
            const cp2 = { x: LI_top.x + 30, y: LI_top.y - 25 };
            setPath('seg-2',
              `M ${O_r.x} ${O_r.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${LI_top.x} ${LI_top.y}`
            );
            mv('n2-end', LI_top.x, LI_top.y);
          }"""
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done updating endpoints and removing link.")
