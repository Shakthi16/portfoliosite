import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# -------------------------------------------------------------
# 1. REMOVE SHAPING TOMORROW SECTION (#text-mask-section)
# -------------------------------------------------------------
pos_mask = content.find('id="text-mask-section"')
if pos_mask != -1:
    sec_start = content.rfind('<section', 0, pos_mask)
    sec_end = content.find('</section>', pos_mask) + len('</section>')
    content = content[:sec_start] + content[sec_end:]
    print("Successfully removed #text-mask-section (Shaping Tomorrow)!")

# -------------------------------------------------------------
# 2. APPLY GRADIENT TRANSITION TO SHAKTHI SRI T S IN CONTACT SECTION
# -------------------------------------------------------------
# Update CSS for .contact-bg-text
old_css_pattern = r'\.contact-bg-text\s*\{[^}]*\}'
new_css = """.contact-bg-text {
      font-size: clamp(2.5rem, 11vw, 8.5rem);
      font-weight: 900;
      background: linear-gradient(135deg, #f9a8d4 0%, #c084fc 35%, #818cf8 70%, #f472b6 100%);
      background-size: 200% 200%;
      animation: gradient-shift 6s ease infinite alternate;
      -webkit-background-clip: text !important;
      -webkit-text-fill-color: transparent !important;
      background-clip: text !important;
      color: transparent !important;
      -webkit-text-stroke: 0px transparent !important;
      text-transform: uppercase;
      letter-spacing: -0.04em;
      line-height: 0.85;
      font-family: 'Outfit', sans-serif;
    }

    @keyframes gradient-shift {
      0% { background-position: 0% 50%; }
      100% { background-position: 100% 50%; }
    }"""

content = re.sub(old_css_pattern, new_css, content, count=1)
print("Successfully applied gradient transition style to SHAKTHI SRI T S contact text!")

# Also remove stroke override in light-mode CSS if present
content = content.replace(
    'body.light-mode .contact-bg-text {\n      color: transparent;\n      -webkit-text-stroke: 1.5px rgba(0, 0, 0, 0.14);\n    }',
    'body.light-mode .contact-bg-text {\n      background: linear-gradient(135deg, #ec4899 0%, #a855f7 40%, #6366f1 80%, #f43f5e 100%) !important;\n      background-size: 200% 200% !important;\n      -webkit-background-clip: text !important;\n      -webkit-text-fill-color: transparent !important;\n      -webkit-text-stroke: 0px transparent !important;\n    }'
)

# -------------------------------------------------------------
# 3. DYNAMICALLY CONNECTING ARROWS & ANIMATION BETWEEN CARDS IN #about
# -------------------------------------------------------------
CONNECTING_ARROWS_SCRIPT = """
<!-- DYNAMIC DOWNHILL CONNECTING PATHS BETWEEN EDITORIAL CARDS -->
<script>
  document.addEventListener('DOMContentLoaded', function () {
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

    // Card nodes sequence
    const cards = [
      { id: 'node-hero', dotStart: 'seg-0', dotEnd: 'n0-end' },
      { id: 'trigger-girl', dotStart: 'seg-1', dotEnd: 'n1-end' },
      { id: 'trigger-orbital', dotStart: 'seg-2', dotEnd: 'n2-end' },
      { id: 'node-linkedin', dotStart: 'seg-3', dotEnd: 'n3-end' },
      { id: 'trigger-crafting', dotStart: 'seg-4', dotEnd: 'n4-end' },
      { id: 'trigger-shavira', dotStart: null, dotEnd: null }
    ];

    function updateCardConnections() {
      const container = document.getElementById('timeline-container');
      const svg = document.getElementById('timeline-svg');
      if (!container || !svg) return;

      const cRect = container.getBoundingClientRect();
      const svgW = 1400;
      const svgH = 2200;

      for (let i = 0; i < cards.length - 1; i++) {
        const sourceEl = document.getElementById(cards[i].id);
        const targetEl = document.getElementById(cards[i + 1].id);
        const pathEl = document.getElementById(`seg-${i}`);
        const endDot = document.getElementById(`n${i}-end`);

        if (sourceEl && targetEl && pathEl) {
          const sRect = sourceEl.getBoundingClientRect();
          const tRect = targetEl.getBoundingClientRect();

          // Convert client coordinates to SVG viewBox space (1400 x 2200)
          const x1 = ((sRect.left + sRect.width / 2 - cRect.left) / cRect.width) * svgW;
          const y1 = ((sRect.bottom - cRect.top) / cRect.height) * svgH;

          const x2 = ((tRect.left + tRect.width / 2 - cRect.left) / cRect.width) * svgW;
          const y2 = ((tRect.top - cRect.top) / cRect.height) * svgH;

          // Smooth curved bezier S-path connecting card 1 bottom to card 2 top
          const midY = (y1 + y2) / 2;
          const d = `M ${x1.toFixed(1)} ${y1.toFixed(1)} C ${x1.toFixed(1)} ${midY.toFixed(1)}, ${x2.toFixed(1)} ${midY.toFixed(1)}, ${x2.toFixed(1)} ${y2.toFixed(1)}`;
          pathEl.setAttribute('d', d);

          if (endDot) {
            endDot.setAttribute('cx', x2.toFixed(1));
            endDot.setAttribute('cy', y2.toFixed(1));
          }

          // Set dasharray & initial offset for GSAP scroll trigger
          const pathLen = pathEl.getTotalLength();
          gsap.set(pathEl, { strokeDasharray: '8 6', strokeDashoffset: pathLen });
        }
      }
    }

    // Initial positioning & update on resize
    updateCardConnections();
    window.addEventListener('resize', updateCardConnections);

    // Animate paths as user scrolls down between cards
    for (let i = 0; i < cards.length - 1; i++) {
      const pathEl = document.getElementById(`seg-${i}`);
      const sourceEl = document.getElementById(cards[i].id);

      if (pathEl && sourceEl) {
        gsap.to(pathEl, {
          strokeDashoffset: 0,
          ease: 'none',
          scrollTrigger: {
            trigger: sourceEl,
            start: 'top 70%',
            end: 'bottom 20%',
            scrub: 1.2,
            onUpdate: function () {
              // Ensure paths recalculate if layout shifts during scroll
              updateCardConnections();
            }
          }
        });
      }
    }
  });
</script>
"""

if '</body' in content:
    content = content.replace('</body>', CONNECTING_ARROWS_SCRIPT + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("All requested updates applied successfully!")
