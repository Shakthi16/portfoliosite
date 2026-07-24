import re

html_file = 'index.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_svg = """
    <!-- THE ARROW SYSTEM SVG -->
    <svg id="timeline-svg" class="absolute inset-0 w-full h-full pointer-events-none z-[100] drawing-arrows" viewBox="0 0 1400 2200">
      <defs>
        <marker id="minimal-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse">
          <path d="M 2 2 L 8 5 L 2 8" fill="none" stroke="#1F1F1F" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
        </marker>
        <filter id="node-glow" x="-50%" y="-50%" width="200%" height="200%">
          <feGaussianBlur stdDeviation="3" result="blur" />
          <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        <linearGradient id="fade-out" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#1F1F1F" stop-opacity="0.85" />
          <stop offset="100%" stop-color="#1F1F1F" stop-opacity="0" />
        </linearGradient>
      </defs>

      <!-- All paths have 1.2px, #1F1F1F, 85% opacity -->
      <g stroke="#1F1F1F" stroke-width="1.2" fill="none" stroke-opacity="0.85" class="floating-arrows">
        
        <!-- Arrow 1: Hero Card (Top Left) -> Center Overshoot -> Girl Illustration (Mid Right) -->
        <path class="draw-path" d="M 325 420 L 325 460 C 325 800, 1200 400, 850 850" marker-end="url(#minimal-arrow)" />
        <circle cx="700" cy="600" r="4" fill="white" stroke="#B14665" stroke-width="2" filter="url(#node-glow)" class="interactive-node" style="pointer-events: auto;" />
        <circle cx="850" cy="850" r="4" fill="white" stroke="#B14665" stroke-width="2" class="interactive-node" style="pointer-events: auto;" />

        <!-- Arrow 2: Girl (Mid Right) -> S-Curve under "I build..." -> Center loop -> Down -->
        <path class="draw-path" d="M 850 900 C 400 900, 100 1050, 250 1250 C 400 1450, 800 1250, 700 1450" marker-end="url(#minimal-arrow)" />
        <circle cx="250" cy="1250" r="4" fill="white" stroke="#B14665" stroke-width="2" class="interactive-node" style="pointer-events: auto;" />
        <circle cx="700" cy="1450" r="4" fill="white" stroke="#B14665" stroke-width="2" class="interactive-node" style="pointer-events: auto;" />

        <!-- Arrow 3: Under Heading -> U-Turn -> wrap LinkedIn (Bottom Left) -> Up -->
        <path class="draw-path" d="M 250 1350 C -50 1350, 50 1900, 140 1850" marker-end="url(#minimal-arrow)" />
        <circle cx="80" cy="1600" r="4" fill="white" stroke="#B14665" stroke-width="2" filter="url(#node-glow)" class="interactive-node" style="pointer-events: auto;" />
        <circle cx="140" cy="1850" r="4" fill="white" stroke="#B14665" stroke-width="2" class="interactive-node" style="pointer-events: auto;" />

        <!-- Arrow 4: Near LinkedIn -> Diagonal -> Behind Center -> Shavira -->
        <path class="draw-path" d="M 400 1600 C 600 1400, 700 1400, 880 1720" marker-end="url(#minimal-arrow)" />
        <circle cx="650" cy="1520" r="4" fill="white" stroke="#B14665" stroke-width="2" class="interactive-node" style="pointer-events: auto;" />
        <circle cx="880" cy="1720" r="4" fill="white" stroke="#B14665" stroke-width="2" class="interactive-node" style="pointer-events: auto;" />

        <!-- Arrow 5: Leaves Shavira -> tiny loop -> Footer -> Fade -->
        <path class="draw-path fade-stroke" d="M 1070 2020 C 1200 2020, 1200 2150, 1070 2150 C 900 2150, 900 2200, 900 2200" stroke="url(#fade-out)" />
        <circle cx="1150" cy="2085" r="4" fill="white" stroke="#B14665" stroke-width="2" filter="url(#node-glow)" class="interactive-node" style="pointer-events: auto;" />
      </g>
    </svg>
"""

pattern = r'<!-- THE ARROW SYSTEM SVG -->\s*<svg id="timeline-svg".*?</svg>'
content = re.sub(pattern, new_svg.strip(), content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated SVG paths in index.html")
