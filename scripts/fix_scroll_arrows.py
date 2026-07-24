import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove marker-end attributes to prevent floating arrowheads
content = re.sub(r'marker-end="url\(#minimal-arrow\)"', '', content)

# Add IDs to the trigger elements for precise scroll tracking
content = content.replace('<!-- 5. FLOATING GIRL ILLUSTRATION (Mid Right) -->\n    <div class="absolute', '<!-- 5. FLOATING GIRL ILLUSTRATION (Mid Right) -->\n    <div id="trigger-girl" class="absolute')
content = content.replace('<!-- 3. CENTRAL ORBITAL OBJECT (Mid Left) -->\n    <div class="absolute', '<!-- 3. CENTRAL ORBITAL OBJECT (Mid Left) -->\n    <div id="trigger-orbital" class="absolute')
content = content.replace('<!-- 7. THIRD HEADING (Bottom Center) -->\n    <div class="absolute', '<!-- 7. THIRD HEADING (Bottom Center) -->\n    <div id="trigger-crafting" class="absolute')

# Replace the GSAP animation block
old_gsap_pattern = r'// NEW SVG DRAW ANIMATION\s*if\s*\(typeof gsap.*?\s*\}\s*\}'
new_gsap = """// NEW SVG DRAW ANIMATION: Sequential Flow
      if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        const drawPaths = document.querySelectorAll('.draw-path');
        const triggers = ['#node-hero', '#trigger-girl', '#trigger-orbital', '#node-linkedin', '#trigger-crafting'];
        
        drawPaths.forEach((path, index) => {
            let length = path.getTotalLength();
            // Hide path initially
            gsap.set(path, { strokeDasharray: length, strokeDashoffset: length });
            
            // Create a specific scroll trigger for this path based on its corresponding card
            if (triggers[index]) {
                gsap.to(path, {
                    strokeDashoffset: 0,
                    ease: 'none',
                    scrollTrigger: {
                        trigger: triggers[index],
                        start: 'top 60%',
                        end: 'bottom 20%', // Draw as the user scrolls past the card
                        scrub: 1,
                    }
                });
            }
        });
      }"""

# Using DOTALL is tricky with the closing brackets, let's just use string replace for the whole <script> block if possible.
# Actually, I'll use regex to match the block between "// NEW SVG DRAW ANIMATION" and the end.
content = re.sub(r'// NEW SVG DRAW ANIMATION.*?\}\s*\}', new_gsap, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated scroll animations and removed marker-ends.")
