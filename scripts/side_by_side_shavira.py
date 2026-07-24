with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Heights to 2550px (since Shavira and Crafting are side-by-side at 2050px)
content = content.replace('min-height: 2850px;', 'min-height: 2550px;')
content = content.replace('height: 2850px;', 'height: 2550px;')
content = content.replace('viewBox="0 0 1400 2850"', 'viewBox="0 0 1400 2550"')
content = content.replace('2850 vb units', '2550 vb units')

# 2. Update Shavira Card top position (move to top-[2050px] left-[80px] to be side-by-side with Crafting text)
content = content.replace(
    'class="absolute top-[2200px] left-[80px] w-[340px] z-30 hover-card" id="trigger-shavira"',
    'class="absolute top-[2050px] left-[80px] w-[340px] z-30 hover-card" id="trigger-shavira"'
)

# 3. Update Crafting Text to right-[80px], w-[500px], text-left, top-[2050px]
content = content.replace(
    'class="absolute top-[2050px] left-[50%] transform -translate-x-[50%] w-[400px] z-20 text-center" id="trigger-crafting"',
    'class="absolute top-[2050px] right-[80px] w-[500px] z-20 text-left" id="trigger-crafting"'
)

# 4. Update segments config in JS ScrollTrigger loop
content = content.replace(
    """          { id: 'seg-4', trigger: '#node-github',      start: 'top 60%', end: 'bottom 10%', endNode: 'n4-end' },
          { id: 'seg-5', trigger: '#trigger-crafting', start: 'top 65%', end: 'bottom 15%', endNode: 'n5-end' },""",
    """          { id: 'seg-4', trigger: '#node-github',      start: 'top 60%', end: 'bottom 10%', endNode: 'n4-end' },
          { id: 'seg-5', trigger: '#trigger-shavira',  start: 'top 65%', end: 'bottom 15%', endNode: 'n5-end' },"""
)

# 5. Update buildJourneyPaths() JS code
# Update anchor points block
content = content.replace(
    """          const GH_top = vb('#node-github',      0.5,  0.0);  // github top-center
          const GH_bot = vb('#node-github',      0.5,  1.02); // github bottom-center
          const CR_l   = vb('#trigger-crafting', -0.15, 0.4);  // crafting text left
          const CR_r   = vb('#trigger-crafting', 1.15, 0.4);  // crafting text right
          const SH_tl  = vb('#trigger-shavira',  0.5, 0.0);  // shavira top-center""",
    """          const GH_top = vb('#node-github',      0.5,  0.0);  // github top-center
          const GH_bot = vb('#node-github',      0.5,  1.02); // github bottom-center
          const SH_top = vb('#trigger-shavira',  0.5,  0.0);  // shavira top-center
          const SH_r   = vb('#trigger-shavira',  1.02, 0.5);  // shavira right-center
          const CR_l   = vb('#trigger-crafting', -0.10, 0.5);  // crafting text left"""
)

# Update the seg-4 and seg-5 path generators
content = content.replace(
    """          // ─── SEG 4: GitHub → Crafting Text ────────────────
          // Drop from github bottom toward crafting text left (route above the text)
          {
            const cp1 = { x: GH_bot.x - 150, y: GH_bot.y + 5 };
            const cp2 = { x: CR_l.x - 40,    y: GH_bot.y + 5 };
            setPath('seg-4',
              `M ${GH_bot.x} ${GH_bot.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${CR_l.x} ${CR_l.y}`
            );
            mv('n4-end', CR_l.x, CR_l.y);
          }

          // ─── SEG 5: Crafting Text → Shavira ───────────────
          // Clean S-curve from crafting text right to shavira top-center
          {
            const cp1 = { x: CR_r.x + 120, y: CR_r.y + 40 };
            const cp2 = { x: SH_tl.x + 120, y: SH_tl.y - 80 };
            setPath('seg-5',
              `M ${CR_r.x} ${CR_r.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${SH_tl.x} ${SH_tl.y}`
            );
            mv('n5-end', SH_tl.x, SH_tl.y);
          }""",
    """          // ─── SEG 4: GitHub → Shavira ──────────────────────
          // Diagonal sweep from github bottom to shavira top-center
          {
            const cp1 = { x: GH_bot.x - 300, y: GH_bot.y + 30 };
            const cp2 = { x: SH_top.x + 300, y: SH_top.y - 50 };
            setPath('seg-4',
              `M ${GH_bot.x} ${GH_bot.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${SH_top.x} ${SH_top.y}`
            );
            mv('n4-end', SH_top.x, SH_top.y);
          }

          // ─── SEG 5: Shavira → Crafting Text ───────────────
          // Clean horizontal arc from shavira right-center to crafting left
          {
            const cp1 = { x: SH_r.x + 100, y: SH_r.y + 20 };
            const cp2 = { x: CR_l.x - 100, y: CR_l.y + 20 };
            setPath('seg-5',
              `M ${SH_r.x} ${SH_r.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${CR_l.x} ${CR_l.y}`
            );
            mv('n5-end', CR_l.x, CR_l.y);
          }"""
)

# Fix verify checks inside buildJourneyPaths
content = content.replace(
    "!LI_top || !LI_r || !GH_top || !CR_l || !CR_r || !SH_tl",
    "!LI_top || !LI_r || !GH_top || !CR_l || !SH_top || !SH_r"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done setting Shavira side-by-side with Crafting text.")
