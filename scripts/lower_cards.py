with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove static marker-end="url(#arrow-tip)" from all 6 paths to prevent floating arrowheads
content = content.replace('marker-end="url(#arrow-tip)"', '')

# 2. Update height to 2650px
content = content.replace('min-height: 2450px;', 'min-height: 2650px;')
content = content.replace('height: 2450px;', 'height: 2650px;')
content = content.replace('viewBox="0 0 1400 2450"', 'viewBox="0 0 1400 2650"')
content = content.replace('2450 vb units', '2650 vb units')

# 3. Lower the cards/text blocks
content = content.replace(
    'class="absolute top-[1250px] left-[80px] w-[340px] z-30 hover-card" id="node-linkedin"',
    'class="absolute top-[1350px] left-[80px] w-[340px] z-30 hover-card" id="node-linkedin"'
)
content = content.replace(
    'class="absolute top-[1250px] right-[80px] w-[340px] z-30 hover-card" id="node-github"',
    'class="absolute top-[1350px] right-[80px] w-[340px] z-30 hover-card" id="node-github"'
)
content = content.replace(
    'class="absolute top-[1700px] left-[50%] transform -translate-x-[50%] w-[400px] z-20 text-center" id="trigger-crafting"',
    'class="absolute top-[1850px] left-[50%] transform -translate-x-[50%] w-[400px] z-20 text-center" id="trigger-crafting"'
)
content = content.replace(
    'class="absolute top-[1850px] right-[80px] w-[340px] z-30 hover-card" id="trigger-shavira"',
    'class="absolute top-[2050px] right-[80px] w-[340px] z-30 hover-card" id="trigger-shavira"'
)

# 4. Update the GSAP timeline to add marker-end dynamically during scroll draw
OLD_GSAP_FOREACH = """          // Animate each segment: line draws → destination dot pops in.
          // That's it. One line, one dot. Clean.
          segments.forEach(({ id, trigger, start, end, endNode }) => {
            const path = document.getElementById(id);
            if (!path) return;

            const len = path.getTotalLength();
            if (!len) return;

            // Fully hide the line
            path.style.strokeDasharray  = len + 'px';
            path.style.strokeDashoffset = len + 'px';

            // Hide destination dot
            const dot = document.getElementById(endNode);
            if (dot) gsap.set(dot, { opacity: 0, scale: 0, transformOrigin: '50% 50%' });

            // Scrub timeline: line draws → dot pops
            const tl = gsap.timeline({
              scrollTrigger: { trigger, start, end, scrub: 2 }
            });

            // Draw the line
            tl.to(path, { strokeDashoffset: 0, duration: 0.85, ease: 'power2.inOut' });

            // Destination dot pops in with spring
            if (dot) {
              tl.to(dot, { opacity: 1, scale: 1.5, duration: 0.08, ease: 'back.out(4)' })
                .to(dot, { scale: 1, duration: 0.10, ease: 'elastic.out(1, 0.5)' });
            }
          });"""

NEW_GSAP_FOREACH = """          // Animate each segment: line draws → destination dot pops in.
          // That's it. One line, one dot. Clean.
          // marker-end is set dynamically on scroll to prevent floating arrowheads!
          segments.forEach(({ id, trigger, start, end, endNode }) => {
            const path = document.getElementById(id);
            if (!path) return;

            const len = path.getTotalLength();
            if (!len) return;

            // Fully hide the line and marker initially
            path.style.strokeDasharray  = len + 'px';
            path.style.strokeDashoffset = len + 'px';
            path.setAttribute('marker-end', 'none');

            // Hide destination dot
            const dot = document.getElementById(endNode);
            if (dot) gsap.set(dot, { opacity: 0, scale: 0, transformOrigin: '50% 50%' });

            // Scrub timeline: line draws → dot pops
            const tl = gsap.timeline({
              scrollTrigger: { trigger, start, end, scrub: 2 }
            });

            // Draw the line and animate the arrowhead visibility dynamically
            tl.to(path, { 
              strokeDashoffset: 0, 
              duration: 0.85, 
              ease: 'power2.inOut',
              onUpdate: function() {
                // Only show arrowhead when the path is nearly completed
                if (this.progress() > 0.92) {
                  path.setAttribute('marker-end', 'url(#arrow-tip)');
                } else {
                  path.setAttribute('marker-end', 'none');
                }
              }
            });

            // Destination dot pops in with spring
            if (dot) {
              tl.to(dot, { opacity: 1, scale: 1.5, duration: 0.08, ease: 'back.out(4)' })
                .to(dot, { scale: 1, duration: 0.10, ease: 'elastic.out(1, 0.5)' });
            }
          });"""

content = content.replace(OLD_GSAP_FOREACH, NEW_GSAP_FOREACH)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done lowering cards and fixing floating arrowheads.")
