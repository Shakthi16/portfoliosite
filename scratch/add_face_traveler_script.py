import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Ensure #path-traveler-avatar is placed inside #timeline-container right after </svg>
AVATAR_ELEMENT = """    <!-- TRAVELING FACE EMOJI STICKER ALONG ARROW PATHS -->
    <div id="path-traveler-avatar" class="absolute z-[80] pointer-events-none transition-transform duration-75" style="width: 52px; height: 52px; top: 0; left: 0; transform: translate(-50%, -50%); display: none;">
      <div class="relative w-full h-full flex items-center justify-center">
        <!-- Speed Dash Motion Trail -->
        <div class="absolute -left-3 top-1/2 -translate-y-1/2 flex flex-col gap-1 opacity-60 pointer-events-none">
          <div class="w-2.5 h-0.5 bg-gray-500 rounded-full"></div>
          <div class="w-1.5 h-0.5 bg-gray-500 rounded-full ml-1"></div>
          <div class="w-2.5 h-0.5 bg-gray-500 rounded-full"></div>
        </div>
        <!-- Face Emoji Sticker with crisp 0.5px white border & shadow -->
        <img src="face.png" alt="Traveling Avatar" class="w-full h-full object-contain rounded-full" style="filter: drop-shadow(0 0 2px #ffffff) drop-shadow(0 0 1px #ffffff) drop-shadow(0 4px 10px rgba(0,0,0,0.18)); border: 0.5px solid rgba(255,255,255,0.95);"/>
      </div>
    </div>"""

# Remove old avatar element if present
content = re.sub(r'<!-- TRAVELING FACE EMOJI STICKER ALONG ARROW PATHS -->.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
content = re.sub(r'<div id="path-traveler-avatar"[^>]*>.*?</div>\s*</div>', '', content, flags=re.DOTALL)

# Insert avatar right after timeline-svg </svg>
svg_end_pos = content.find('</svg>', content.find('id="timeline-svg"'))
if svg_end_pos != -1:
    insert_idx = svg_end_pos + len('</svg>')
    content = content[:insert_idx] + '\n\n' + AVATAR_ELEMENT + content[insert_idx:]
    print("Successfully inserted #path-traveler-avatar HTML element!")

# 2. Add complete updatePathAvatarScroll script before </body>
PATH_RUNNER_SCRIPT = """
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

      // Display avatar when timeline section is active in viewport
      if (cRect.bottom < 0 || cRect.top > windowH) {
        avatar.style.display = 'none';
        return;
      }

      const totalDist = cRect.height - windowH;
      let p = (-cRect.top) / (totalDist || 1);
      p = Math.max(0, Math.min(1, p));

      avatar.style.display = 'block';

      // Calculate total cumulative length of arrow paths
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
      const scaleY = (cRect.height || 2950) / 2950;
      const cssX = pt.x * scaleX;
      const cssY = pt.y * scaleY;

      avatar.style.transform = `translate3d(${cssX}px, ${cssY}px, 0px) translate(-50%, -50%) rotate(${angle * 0.15}deg)`;
    } catch (e) {
      console.error("updatePathAvatarScroll error:", e);
    }
  }

  window.addEventListener('scroll', updatePathAvatarScroll, { passive: true });
  window.addEventListener('resize', updatePathAvatarScroll, { passive: true });
  document.addEventListener('DOMContentLoaded', () => {
    setTimeout(updatePathAvatarScroll, 200);
    setTimeout(updatePathAvatarScroll, 800);
  });
  if (document.readyState !== 'loading') {
    setTimeout(updatePathAvatarScroll, 200);
  }
</script>
"""

# Remove old script if present
if 'updatePathAvatarScroll' in content:
    content = re.sub(r'<!-- TRAVELING FACE EMOJI SCROLL ANIMATION -->.*?<\/script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script>\s*// Traveling Face Emoji Scroll Animation.*?<\/script>', '', content, flags=re.DOTALL)

# Re-insert script right before </body>
content = content.replace('</body>', PATH_RUNNER_SCRIPT + '\n</body>')
print("Successfully inserted updatePathAvatarScroll script before </body>!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done updating face traveler emoji script!")
