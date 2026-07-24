import re
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Delete the "Shaping Tomorrow" TEXT MASKING SECTION completely
text_mask_pattern = re.compile(r'<!-- TEXT MASKING SECTION -->.*?<!-- PROJECTS -->', re.DOTALL)
html = text_mask_pattern.sub('<!-- PROJECTS -->', html)

# 2. Fix the SVG alignment issue by moving it inside the timeline-container
# The issue was that the SVG was absolute to the full screen section, but coordinates were relative to the centered container.
bad_svg_html = r'''<!-- Canvas for SVG drawing -->
  <svg id="timeline-svg" class="absolute inset-0 w-full h-full pointer-events-none z-[100] hidden md:block"></svg>

  <div class="relative w-full max-w-[1200px] mx-auto px-6 lg:px-12 z-10 hidden md:block" id="timeline-container" style="height: 1700px;">'''

good_svg_html = r'''<!-- Canvas for SVG drawing (Moved INSIDE container for correct coordinates) -->
  <div class="relative w-full max-w-[1200px] mx-auto px-6 lg:px-12 z-10 hidden md:block" id="timeline-container" style="height: 1700px;">
    <svg id="timeline-svg" class="absolute inset-0 w-full h-full pointer-events-none z-[100] hidden md:block"></svg>'''

if bad_svg_html in html:
    html = html.replace(bad_svg_html, good_svg_html)
else:
    print("Could not find SVG HTML to fix alignment!")
    sys.exit(1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed SVG alignment and removed Shaping Tomorrow section!")
