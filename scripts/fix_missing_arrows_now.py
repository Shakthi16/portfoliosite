import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update SVG element with preserveAspectRatio="none"
content = re.sub(
    r'<svg[^>]*id="timeline-svg"[^>]*>',
    '<svg class="absolute inset-0 w-full h-full pointer-events-none" id="timeline-svg" viewBox="0 0 1400 2950" preserveAspectRatio="none" style="z-index: 50; overflow: visible;">',
    content
)

# 2. Update .journey-path CSS styling for high visibility
OLD_CSS = r'\.journey-path\s*\{[^}]*\}'
NEW_CSS = """.journey-path {
      stroke: #475569 !important;
      stroke-width: 3px !important;
      stroke-dasharray: 8 8 !important;
      stroke-opacity: 0.85 !important;
      stroke-linecap: round !important;
      fill: none !important;
    }"""

content = re.sub(OLD_CSS, NEW_CSS, content)

# 3. Add default fallback 'd' attributes for instant static rendering of all 5 arrow segments
SEG_0_D = "M 290 360 C 290 500, 1020 390, 1020 530"
SEG_1_D = "M 1140 890 C 1140 1150, 410 920, 210 980"
SEG_2_D = "M 80 1110 C 20 1270, 140 1470, 140 1550"
SEG_3_D = "M 250 1880 C 250 2020, 1260 1910, 1260 2030"
SEG_4_D = "M 1150 2360 C 1150 2500, 140 2390, 140 2510"

content = re.sub(r'<path id="seg-0" class="journey-path" d="[^"]*"', f'<path id="seg-0" class="journey-path" d="{SEG_0_D}"', content)
content = re.sub(r'<path id="seg-1" class="journey-path" d="[^"]*"', f'<path id="seg-1" class="journey-path" d="{SEG_1_D}"', content)
content = re.sub(r'<path id="seg-2" class="journey-path" d="[^"]*"', f'<path id="seg-2" class="journey-path" d="{SEG_2_D}"', content)
content = re.sub(r'<path id="seg-3" class="journey-path" d="[^"]*"', f'<path id="seg-3" class="journey-path" d="{SEG_3_D}"', content)
content = re.sub(r'<path id="seg-4" class="journey-path" d="[^"]*"', f'<path id="seg-4" class="journey-path" d="{SEG_4_D}"', content)

# 4. Improve safeJourneyPaths script to use getBoundingClientRect inside container
JS_REPLACEMENT = """
  // Robust Arrow Path Calculation Script
  function safeJourneyPaths() {
    try {
      const container = document.getElementById('timeline-container');
      const svg = document.getElementById('timeline-svg');
      if (!container || !svg) return;

      const cRect = container.getBoundingClientRect();
      const cW = container.clientWidth || 1400;
      const scaleX = 1400 / cW;

      function getVB(sel, ax, ay) {
        const el = document.querySelector(sel);
        if (!el) return null;
        const r = el.getBoundingClientRect();
        if (!r || r.width === 0) return null;
        const x = (r.left - cRect.left + r.width * ax) * scaleX;
        const y = (r.top - cRect.top + r.height * ay) * (2950 / (cRect.height || 2950));
        if (isNaN(x) || isNaN(y)) return null;
        return { x: parseFloat(x.toFixed(1)), y: parseFloat(y.toFixed(1)) };
      }

      function updateSeg(id, pathStr, nodeEndId, endPoint) {
        const path = document.getElementById(id);
        if (path && pathStr && !pathStr.includes('NaN')) {
          path.setAttribute('d', pathStr);
        }
        if (nodeEndId && endPoint) {
          const n = document.getElementById(nodeEndId);
          if (n) {
            n.setAttribute('cx', endPoint.x);
            n.setAttribute('cy', endPoint.y);
            n.style.opacity = '1';
          }
        }
      }

      const H_bot = getVB('#node-hero', 0.5, 1.02);
      const G_top = getVB('#trigger-girl', 0.18, -0.02);
      const G_bot = getVB('#trigger-girl', 0.5, 1.02);
      const O_bot = getVB('#trigger-orbital', 0.5, 1.02);
      const O_left = getVB('#trigger-orbital', -0.05, 0.5);
      const LI_top = getVB('#node-linkedin', 0.18, -0.02);
      const LI_bot = getVB('#node-linkedin', 0.5, 1.02);
      const GH_top = getVB('#node-github', 0.82, -0.02);
      const GH_bot = getVB('#node-github', 0.5, 1.02);
      const SH_top = getVB('#trigger-shavira', 0.18, -0.02);

      if (H_bot && G_top) {
        updateSeg('seg-0', `M ${H_bot.x} ${H_bot.y} C ${H_bot.x} ${H_bot.y + 140}, ${G_top.x} ${G_top.y - 140}, ${G_top.x} ${G_top.y}`, 'n0-end', G_top);
      }
      if (G_bot && O_bot) {
        updateSeg('seg-1', `M ${G_bot.x} ${G_bot.y} C ${G_bot.x} ${G_bot.y + 260}, ${O_bot.x + 200} ${O_bot.y + 40}, ${O_bot.x} ${O_bot.y}`, 'n1-end', O_bot);
      }
      if (O_left && LI_top) {
        updateSeg('seg-2', `M ${O_left.x} ${O_left.y} C ${O_left.x - 120} ${O_left.y + 160}, ${LI_top.x} ${LI_top.y - 80}, ${LI_top.x} ${LI_top.y}`, 'n2-end', LI_top);
      }
      if (LI_bot && GH_top) {
        updateSeg('seg-3', `M ${LI_bot.x} ${LI_bot.y} C ${LI_bot.x} ${LI_bot.y + 140}, ${GH_top.x} ${GH_top.y - 120}, ${GH_top.x} ${GH_top.y}`, 'n3-end', GH_top);
      }
      if (GH_bot && SH_top) {
        updateSeg('seg-4', `M ${GH_bot.x} ${GH_bot.y} C ${GH_bot.x} ${GH_bot.y + 140}, ${SH_top.x} ${SH_top.y - 120}, ${SH_top.x} ${SH_top.y}`, 'n4-end', SH_top);
      }
    } catch (e) {
      console.error('safeJourneyPaths error:', e);
    }
    if (typeof updatePathAvatarScroll === 'function') {
      updatePathAvatarScroll();
    }
  }
"""

pos_sjp = content.find('function safeJourneyPaths()')
if pos_sjp != -1:
    pos_sjp_end = content.find('if (document.readyState ===', pos_sjp)
    content = content[:pos_sjp] + JS_REPLACEMENT + '\n\n  ' + content[pos_sjp_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully fixed missing arrows with instant pre-calculated fallback paths and accurate dynamic recalculation!")
