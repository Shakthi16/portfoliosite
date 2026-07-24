import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update SVG preserveAspectRatio="none"
content = re.sub(
    r'<svg[^>]*id="timeline-svg"[^>]*>',
    '<svg class="absolute inset-0 w-full h-full pointer-events-none" id="timeline-svg" viewBox="0 0 1400 2700" preserveAspectRatio="none" style="z-index: 50; overflow: visible;">',
    content
)

# 2. Update .journey-path CSS for high contrast visibility
OLD_CSS = r'\.journey-path\s*\{[^}]*\}'
NEW_CSS = """.journey-path {
      stroke: #334155 !important;
      stroke-width: 3.5px !important;
      stroke-dasharray: 10 10 !important;
      stroke-opacity: 0.9 !important;
      stroke-linecap: round !important;
      fill: none !important;
    }"""

content = re.sub(OLD_CSS, NEW_CSS, content)

# 3. Pre-calculated fallback d attributes for all 5 SVG paths in viewBox 0 0 1400 2700
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

# 4. Instant-on updatePathAvatarScroll Script
AVATAR_RUNNER_SCRIPT = """
<!-- TRAVELING FACE EMOJI SCROLL ANIMATION -->
<script>
  function updatePathAvatarScroll() {
    try {
      const avatar = document.getElementById('path-traveler-avatar');
      const container = document.getElementById('timeline-container');
      if (!avatar || !container) return;

      const segIds = ['seg-0', 'seg-1', 'seg-2', 'seg-3', 'seg-4'];
      const segs = segIds
        .map(id => document.getElementById(id))
        .filter(path => path && path.getAttribute('d') && path.getAttribute('d').trim() !== '');

      if (segs.length === 0) {
        avatar.style.display = 'none';
        return;
      }

      const cRect = container.getBoundingClientRect();
      const windowH = window.innerHeight;

      // Show avatar whenever section is active or near viewport
      if (cRect.bottom < -200 || cRect.top > windowH + 200) {
        avatar.style.display = 'none';
        return;
      }

      const totalDist = cRect.height - windowH;
      let p = (-cRect.top) / (totalDist || 1);
      p = Math.max(0, Math.min(1, p));

      avatar.style.display = 'block';

      // Calculate total cumulative length across all segments
      let totalLen = 0;
      const segLens = segs.map(s => {
        try {
          const l = s.getTotalLength();
          totalLen += l;
          return l;
        } catch(e) { return 0; }
      });

      if (totalLen === 0) return;

      let targetLen = p * totalLen;
      let accumulated = 0;
      let targetSeg = segs[0];
      let distInSeg = 0;

      for (let i = 0; i < segs.length; i++) {
        if (accumulated + segLens[i] >= targetLen || i === segs.length - 1) {
          targetSeg = segs[i];
          distInSeg = targetLen - accumulated;
          distInSeg = Math.max(0, Math.min(segLens[i], distInSeg));
          break;
        }
        accumulated += segLens[i];
      }

      const pt = targetSeg.getPointAtLength(distInSeg);
      const segLen = segLens[segs.indexOf(targetSeg)];
      const ptNext = targetSeg.getPointAtLength(Math.min(segLen, distInSeg + 3));

      const dx = ptNext.x - pt.x;
      const dy = ptNext.y - pt.y;
      const angle = Math.atan2(dy, dx) * (180 / Math.PI);

      const cW = container.clientWidth || 1400;
      const scaleX = cW / 1400;
      const scaleY = (cRect.height || 2700) / 2700;
      const cssX = pt.x * scaleX;
      const cssY = pt.y * scaleY;

      avatar.style.transform = `translate3d(${cssX}px, ${cssY}px, 0px) translate(-50%, -50%) rotate(${angle * 0.12}deg)`;
    } catch (e) {
      console.error("updatePathAvatarScroll error:", e);
    }
  }

  window.addEventListener('scroll', updatePathAvatarScroll, { passive: true });
  window.addEventListener('resize', updatePathAvatarScroll, { passive: true });
  
  // Instant execution on load
  updatePathAvatarScroll();
  setTimeout(updatePathAvatarScroll, 100);
  setTimeout(updatePathAvatarScroll, 500);
  document.addEventListener('DOMContentLoaded', updatePathAvatarScroll);
</script>
"""

# Replace script in content
if 'updatePathAvatarScroll' in content:
    content = re.sub(r'<!-- TRAVELING FACE EMOJI SCROLL ANIMATION -->.*?<\/script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script>\s*// Traveling Face Emoji Scroll Animation.*?<\/script>', '', content, flags=re.DOTALL)

content = content.replace('</body>', AVATAR_RUNNER_SCRIPT + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully fixed SVG preserveAspectRatio='none', journey-path CSS visibility, and instant avatar initialization!")
