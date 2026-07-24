with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Heights to 2850px
content = content.replace('min-height: 2650px;', 'min-height: 2850px;')
content = content.replace('height: 2650px;', 'height: 2850px;')
content = content.replace('viewBox="0 0 1400 2650"', 'viewBox="0 0 1400 2850"')
content = content.replace('2650 vb units', '2850 vb units')

# 2. Lower/reposition the cards to alternate vertically
# LinkedIn remains at: top-[1350px] left-[80px]
# GitHub Card: Move from top-[1350px] right-[80px] to top-[1650px] right-[80px]
content = content.replace(
    'class="absolute top-[1350px] right-[80px] w-[340px] z-30 hover-card" id="node-github"',
    'class="absolute top-[1650px] right-[80px] w-[340px] z-30 hover-card" id="node-github"'
)

# Crafting Text: Move from top-[1850px] left-[50%] to top-[2050px] left-[50%]
content = content.replace(
    'class="absolute top-[1850px] left-[50%] transform -translate-x-[50%] w-[400px] z-20 text-center" id="trigger-crafting"',
    'class="absolute top-[2050px] left-[50%] transform -translate-x-[50%] w-[400px] z-20 text-center" id="trigger-crafting"'
)

# Shavira Card: Move from right-[80px] to left-[80px] and top-[2050px] to top-[2200px]
content = content.replace(
    'class="absolute top-[2050px] right-[80px] w-[340px] z-30 hover-card" id="trigger-shavira"',
    'class="absolute top-[2200px] left-[80px] w-[340px] z-30 hover-card" id="trigger-shavira"'
)

# 3. Update the dynamic JS path coordinates and control points in buildJourneyPaths()
# Update SH_tl anchor definition
content = content.replace(
    "const SH_tl  = vb('#trigger-shavira',  0.12, 0.0);  // shavira top-left",
    "const SH_tl  = vb('#trigger-shavira',  0.5, 0.0);  // shavira top-center"
)

# Update seg-3 control points
content = content.replace(
    """          // ─── SEG 3: LinkedIn → GitHub ─────────────────────
          // Diagonal right-crossing arc from linkedin right to github top
          {
            const midX = (LI_r.x + GH_top.x) / 2;
            const midY = Math.min(LI_r.y, GH_top.y) - 50; // arc over the gap
            const cp1  = { x: midX - 60, y: LI_r.y   - 20 };
            const cp2  = { x: midX + 60, y: GH_top.y - 20 };
            setPath('seg-3',
              `M ${LI_r.x} ${LI_r.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${GH_top.x} ${GH_top.y}`
            );
            mv('n3-end', GH_top.x, GH_top.y);
          }""",
    """          // ─── SEG 3: LinkedIn → GitHub ─────────────────────
          // Diagonal right-crossing arc from linkedin right to github top
          {
            const cp1  = { x: LI_r.x + 200, y: LI_r.y + 40 };
            const cp2  = { x: GH_top.x - 200, y: GH_top.y - 60 };
            setPath('seg-3',
              `M ${LI_r.x} ${LI_r.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${GH_top.x} ${GH_top.y}`
            );
            mv('n3-end', GH_top.x, GH_top.y);
          }"""
)

# Update seg-5 control points to curve beautifully to the left-aligned Shavira Card
content = content.replace(
    """          // ─── SEG 5: Crafting Text → Shavira ───────────────
          // Short arc from crafting text right to shavira top-left
          {
            const dy  = SH_tl.y - CR_r.y;
            const cp1 = { x: CR_r.x  + 35, y: CR_r.y  + dy * 0.30 };
            const cp2 = { x: SH_tl.x + 15, y: SH_tl.y - 25 };
            setPath('seg-5',
              `M ${CR_r.x} ${CR_r.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${SH_tl.x} ${SH_tl.y}`
            );
            mv('n5-end', SH_tl.x, SH_tl.y);
          }""",
    """          // ─── SEG 5: Crafting Text → Shavira ───────────────
          // Clean S-curve from crafting text right to shavira top-center
          {
            const cp1 = { x: CR_r.x + 120, y: CR_r.y + 40 };
            const cp2 = { x: SH_tl.x + 120, y: SH_tl.y - 80 };
            setPath('seg-5',
              `M ${CR_r.x} ${CR_r.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${SH_tl.x} ${SH_tl.y}`
            );
            mv('n5-end', SH_tl.x, SH_tl.y);
          }"""
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done adjusting layout to criss-cross vertical columns.")
