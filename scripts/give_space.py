import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Editorial section height to 2700px
content = content.replace('id="about" style="min-height: 2350px;"', 'id="about" style="min-height: 2700px;"')
content = content.replace('id="about" style="min-height: 2450px;"', 'id="about" style="min-height: 2700px;"')
content = content.replace('id="timeline-container" style="height: 2350px;"', 'id="timeline-container" style="height: 2700px;"')
content = content.replace('id="timeline-container" style="height: 2450px;"', 'id="timeline-container" style="height: 2700px;"')
content = content.replace('id="timeline-svg" viewBox="0 0 1400 2350"', 'id="timeline-svg" viewBox="0 0 1400 2700"')
content = content.replace('id="timeline-svg" viewBox="0 0 1400 2450"', 'id="timeline-svg" viewBox="0 0 1400 2700"')

# 2. Re-position UI elements with generous vertical and horizontal spacing

# Hero Card (Row 1 Left): top 80px, left 80px, w 420px
content = re.sub(
    r'<div class="[^"]*hover-card" id="node-hero">',
    '<div class="absolute top-[80px] left-[80px] w-[420px] z-20 hover-card" id="node-hero">',
    content
)

# Hero Text (Row 1 Right): top 120px, right 80px, w 480px
content = re.sub(
    r'<div class="[^"]*" id="text-hero">',
    '<div class="absolute top-[120px] right-[80px] w-[480px] z-20 bg-white/40 backdrop-blur-md rounded-[32px] p-8 border border-white/60 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.03)] hover:shadow-[0_30px_60px_-15px_rgba(66,24,53,0.06)] transition-all duration-500 hover:-translate-y-1 text-center" id="text-hero">',
    content
)

# Girl Card (Row 2 Right): top 540px, right 80px, w 360px
content = re.sub(
    r'<div class="[^"]*hover-card" id="trigger-girl">',
    '<div class="absolute top-[540px] right-[80px] w-[360px] z-20 hover-card" id="trigger-girl">',
    content
)

# Central Orbital Object (Row 3 Left): top 980px, left 80px, w 260px
content = re.sub(
    r'<div class="[^"]*" id="trigger-orbital">',
    '<div class="absolute top-[980px] left-[80px] w-[260px] h-[260px] z-10 flex items-center justify-center" id="trigger-orbital">',
    content
)

# Headline 2 "I build premium interfaces." (Row 3 Left-Center): top 970px, left 380px, w 440px
content = re.sub(
    r'<div class="[^"]*" id="text-premium">',
    '<div class="absolute top-[970px] left-[380px] w-[440px] z-20 bg-white/40 backdrop-blur-md rounded-[32px] p-8 border border-white/60 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.03)] hover:shadow-[0_30px_60px_-15px_rgba(66,24,53,0.06)] transition-all duration-500 hover:-translate-y-1 text-left" id="text-premium">',
    content
)

# LinkedIn Card (Row 4 Left): top 1400px, left 80px, w 340px
content = re.sub(
    r'<div class="[^"]*hover-card" id="node-linkedin">',
    '<div class="absolute top-[1400px] left-[80px] w-[340px] z-30 hover-card" id="node-linkedin">',
    content
)

# LinkedIn Text (Row 4 Right): top 1400px, left 460px, w 480px
content = re.sub(
    r'<div class="[^"]*" id="text-linkedin">',
    '<div class="absolute top-[1400px] left-[460px] w-[480px] z-20 bg-white/40 backdrop-blur-md rounded-[32px] p-8 border border-white/60 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.03)] hover:shadow-[0_30px_60px_-15px_rgba(66,24,53,0.06)] transition-all duration-500 hover:-translate-y-1 text-left" id="text-linkedin">',
    content
)

# GitHub Card (Row 5 Right): top 1840px, right 80px, w 340px
content = re.sub(
    r'<div class="[^"]*hover-card" id="node-github">',
    '<div class="absolute top-[1840px] right-[80px] w-[340px] z-30 hover-card" id="node-github">',
    content
)

# GitHub Text (Row 5 Left): top 1840px, right 460px, w 480px
content = re.sub(
    r'<div class="[^"]*" id="text-github">',
    '<div class="absolute top-[1840px] right-[460px] w-[480px] z-20 bg-white/40 backdrop-blur-md rounded-[32px] p-8 border border-white/60 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.03)] hover:shadow-[0_30px_60px_-15px_rgba(66,24,53,0.06)] transition-all duration-500 hover:-translate-y-1 text-left" id="text-github">',
    content
)

# Shavira Card (Row 6 Left): top 2280px, left 80px, w 340px
content = re.sub(
    r'<div class="[^"]*hover-card" id="trigger-shavira">',
    '<div class="absolute top-[2280px] left-[80px] w-[340px] z-30 hover-card" id="trigger-shavira">',
    content
)

# Crafting Text (Row 6 Right): top 2280px, left 460px, w 480px
content = re.sub(
    r'<div class="[^"]*" id="trigger-crafting">',
    '<div class="absolute top-[2280px] left-[460px] w-[480px] z-20 bg-white/40 backdrop-blur-md rounded-[32px] p-8 border border-white/60 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.03)] hover:shadow-[0_30px_60px_-15px_rgba(66,24,53,0.06)] transition-all duration-500 hover:-translate-y-1 text-left" id="trigger-crafting">',
    content
)

# 3. Replace JS buildJourneyPaths logic with collision-free curve routing
OLD_BUILD_PATHS = r"""          // ─── SEG 0: Hero → Girl ─────────────────────────────
.*?// ─── SEG 4: GitHub → Shavira ──────────────────────
.*?\n          }"""

NEW_BUILD_PATHS = """          // ─── SEG 0: Hero → Girl ─────────────────────────────
          // Exiting down from Hero bottom, curving through open center area into Girl top-center
          {
            const cp1 = { x: H_bot.x, y: H_bot.y + 140 };
            const cp2 = { x: G_top.x, y: G_top.y - 140 };
            setPath('seg-0',
              `M ${H_bot.x} ${H_bot.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${G_top.x} ${G_top.y}`
            );
            mv('n0-end', G_top.x, G_top.y);
          }

          // ─── SEG 1: Girl → Orbital ────────────────────────
          // Exiting down from Girl bottom, curving left above text-premium in the open horizontal gap, into Orbital top
          {
            const cp1 = { x: G_bot.x, y: G_bot.y + 70 };
            const cp2 = { x: O_top.x + 100, y: O_top.y - 70 };
            setPath('seg-1',
              `M ${G_bot.x} ${G_bot.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${O_top.x} ${O_top.y}`
            );
            mv('n1-end', O_top.x, O_top.y);
          }

          // ─── SEG 2: Orbital → LinkedIn ────────────────────
          // Exiting down from Orbital bottom into LinkedIn top-center
          {
            const cp1 = { x: O_bot.x, y: O_bot.y + 80 };
            const cp2 = { x: LI_top.x, y: LI_top.y - 80 };
            setPath('seg-2',
              `M ${O_bot.x} ${O_bot.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${LI_top.x} ${LI_top.y}`
            );
            mv('n2-end', LI_top.x, LI_top.y);
          }

          // ─── SEG 3: LinkedIn → GitHub ─────────────────────
          // Exiting right from LinkedIn card, curving down through open center space into GitHub top-center
          {
            const cp1 = { x: LI_r.x + 200, y: LI_r.y + 100 };
            const cp2 = { x: GH_top.x, y: GH_top.y - 120 };
            setPath('seg-3',
              `M ${LI_r.x} ${LI_r.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${GH_top.x} ${GH_top.y}`
            );
            mv('n3-end', GH_top.x, GH_top.y);
          }

          // ─── SEG 4: GitHub → Shavira ──────────────────────
          // Exiting left from GitHub card, curving down through open space into Shavira top-center
          {
            const cp1 = { x: GH_l.x - 200, y: GH_l.y + 100 };
            const cp2 = { x: SH_top.x, y: SH_top.y - 120 };
            setPath('seg-4',
              `M ${GH_l.x} ${GH_l.y} ` +
              `C ${cp1.x} ${cp1.y}, ${cp2.x} ${cp2.y}, ${SH_top.x} ${SH_top.y}`
            );
            mv('n4-end', SH_top.x, SH_top.y);
          }
        }"""

content = re.sub(OLD_BUILD_PATHS, NEW_BUILD_PATHS, content, flags=re.DOTALL)

# Also update anchor points in JS if needed
OLD_ANCHORS = r"""          const H_bot  = vb\('#node-hero',        0\.35, 1\.02\);.*?const CR_l   = vb\('#trigger-crafting', -0\.10, 0\.5\);"""
NEW_ANCHORS = """          const H_bot  = vb('#node-hero',        0.5,  1.02);  // hero card bottom-center
          const G_top  = vb('#trigger-girl',     0.5, -0.02);  // girl card top-center
          const G_bot  = vb('#trigger-girl',     0.5,  1.02);  // girl card bottom-center
          const O_top  = vb('#trigger-orbital',  0.5, -0.02);  // orbital top-center
          const O_bot  = vb('#trigger-orbital',  0.5,  1.02);  // orbital bottom-center
          const LI_top = vb('#node-linkedin',    0.5, -0.02);  // linkedin top-center
          const LI_r   = vb('#node-linkedin',    1.02, 0.5);   // linkedin right-center
          const GH_top = vb('#node-github',      0.5, -0.02);  // github top-center
          const GH_l   = vb('#node-github',      -0.02, 0.5);  // github left-center
          const SH_top = vb('#trigger-shavira',  0.5, -0.02);  // shavira top-center"""

content = re.sub(OLD_ANCHORS, NEW_ANCHORS, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated index.html with layout spacing and clean SVG arrow routing.")
