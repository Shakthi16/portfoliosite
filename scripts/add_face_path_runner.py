import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert the face runner element right inside #timeline-container
AVATAR_HTML = """    <!-- TRAVELING FACE EMOJI STICKER ALONG ARROW PATHS -->
    <div id="path-traveler-avatar" class="absolute z-[80] pointer-events-none transition-transform duration-75" style="width: 58px; height: 58px; top: 0; left: 0; transform: translate(-50%, -50%); display: none;">
      <div class="relative w-full h-full">
        <!-- Speed Dash Motion Trail -->
        <div class="absolute -left-3.5 top-1/2 -translate-y-1/2 flex flex-col gap-1 opacity-70 pointer-events-none">
          <div class="w-3.5 h-0.5 bg-gray-500/70 rounded-full"></div>
          <div class="w-2.5 h-0.5 bg-gray-500/70 rounded-full ml-1"></div>
          <div class="w-3.5 h-0.5 bg-gray-500/70 rounded-full"></div>
        </div>
        <img src="face.png" alt="Traveling Avatar" class="w-full h-full object-contain filter drop-shadow-md"/>
      </div>
    </div>
"""

if 'id="path-traveler-avatar"' not in content:
    pos_svg = content.find('id="timeline-svg"')
    if pos_svg != -1:
        # Find closing tag of svg </svg>
        pos_svg_end = content.find('</svg>', pos_svg) + len('</svg>')
        content = content[:pos_svg_end] + '\n\n' + AVATAR_HTML + content[pos_svg_end:]
        print("Successfully added #path-traveler-avatar HTML element!")

# 2. Add the path traveling JS script right after safeJourneyPaths
PATH_RUNNER_SCRIPT = """
<script>
  // Traveling Face Emoji Scroll Animation along Arrow Paths
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
      
      // Show when timeline section is in viewport
      if (cRect.bottom < 0 || cRect.top > windowH) {
        avatar.style.display = 'none';
        return;
      }

      const totalDist = cRect.height - windowH;
      let p = (-cRect.top) / (totalDist || 1);
      p = Math.max(0, Math.min(1, p));

      avatar.style.display = 'block';

      // Calculate cumulative lengths
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

      const scale = container.clientWidth / 1400;
      const cssX = pt.x * scale;
      const cssY = pt.y;

      avatar.style.transform = `translate3d(${cssX}px, ${cssY}px, 0px) translate(-50%, -50%) rotate(${angle * 0.1}deg)`;
    } catch (e) {
      console.error("updatePathAvatarScroll error:", e);
    }
  }

  window.addEventListener('scroll', updatePathAvatarScroll, { passive: true });
  window.addEventListener('resize', updatePathAvatarScroll, { passive: true });
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      setTimeout(updatePathAvatarScroll, 500);
    });
  } else {
    setTimeout(updatePathAvatarScroll, 500);
  }
</script>
"""

if 'updatePathAvatarScroll' not in content:
    pos_safe_paths = content.find('setTimeout(safeJourneyPaths, 1000);')
    if pos_safe_paths != -1:
        pos_script_end = content.find('</script>', pos_safe_paths) + len('</script>')
        content = content[:pos_script_end] + '\n' + PATH_RUNNER_SCRIPT + content[pos_script_end:]
        print("Successfully added updatePathAvatarScroll script!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Traveling face emoji added along arrow curves!")
