import re
import sys

def process_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the section background
    content = content.replace('bg-[#050505]" id="about"', 'bg-[#FAF8F5]" id="about"')

    # 2. Update background meshes
    content = content.replace('bg-[#b55cd5] rounded-full mix-blend-screen filter blur-[150px] opacity-40', 'bg-[#eadaf2] rounded-full mix-blend-multiply filter blur-[150px] opacity-70')
    content = content.replace('bg-[#421835] rounded-full mix-blend-screen filter blur-[150px] opacity-50', 'bg-[#f5e6eb] rounded-full mix-blend-multiply filter blur-[150px] opacity-70')
    content = content.replace('bg-[#c97ce5] rounded-full mix-blend-screen filter blur-[150px] opacity-40', 'bg-[#e6ebf5] rounded-full mix-blend-multiply filter blur-[150px] opacity-70')
    content = content.replace('bg-black/40 backdrop-blur-[2px]', 'bg-white/40 backdrop-blur-[4px]')
    
    # 3. Replace the timeline line with SVG
    old_line = '''<!-- The Center Timeline Guide -->
      <div class="absolute left-1/2 top-0 bottom-0 w-[2px] bg-white/10 -translate-x-1/2 z-10 hidden md:block" id="ed-timeline-line">
        <div id="timeline-progress" class="w-full bg-gradient-to-b from-[#b55cd5] to-[#c97ce5] h-0 relative">
          <div class="absolute bottom-0 left-1/2 -translate-x-1/2 w-8 h-8 bg-[#050505] border-2 border-[#c97ce5] rounded-full shadow-[0_0_25px_#c97ce5] flex items-center justify-center transform translate-y-1/2">
            <svg class="w-4 h-4 text-[#c97ce5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path></svg>
          </div>
        </div>
      </div>'''
      
    new_svg = '''<!-- The Cursive Timeline Arrow -->
      <svg id="cursive-arrow-svg" class="absolute top-0 left-0 w-full h-full pointer-events-none z-[25] hidden md:block" preserveAspectRatio="none">
        <path id="cursive-arrow-path" fill="none" stroke="url(#arrow-gradient)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0px 4px 6px rgba(201,124,229,0.4));" />
        <defs>
          <linearGradient id="arrow-gradient" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#b55cd5" />
            <stop offset="50%" stop-color="#c97ce5" />
            <stop offset="100%" stop-color="#421835" />
          </linearGradient>
        </defs>
        <polygon id="arrow-head" points="0,-8 12,0 0,8" fill="#421835" />
      </svg>'''
    
    content = content.replace(old_line, new_svg)

    # 4. Update Text blocks and Dots in .timeline-row
    # We'll use regex to replace text-white with text-gray-900 in headers, and text-white/70 with text-gray-700 in p tags within ed-text-block
    # And row-dot styles
    content = re.sub(r'(class="font-bold text-\[clamp\(.*?\)\] leading-\[1\.1\] )text-white(.*?) filter drop-shadow-\[.*?\]', r'\1text-gray-900\2', content)
    content = re.sub(r'(class="font-sans text-\[clamp\(.*?\)\] )text-white/70(.*?)', r'\1text-gray-700\2', content)
    content = content.replace('border-white/20 bg-[#111]', 'border-[#c97ce5]/30 bg-white')

    # 5. GSAP Logic Replacement
    old_gsap_start = "// 3. Editorial Scroll Canvas (Redesigned with Timeline Arrow)"
    old_gsap_end = "// 4. Reveal Animations (Blur -> Sharp)"
    
    gsap_pattern = re.compile(re.escape(old_gsap_start) + r'.*?' + re.escape(old_gsap_end), re.DOTALL)
    
    new_gsap = '''// 3. Editorial Scroll Canvas (Redesigned with Cursive Arrow)
      if (document.querySelector('#ed-scroll-tracks')) {
        const rows = document.querySelectorAll('.timeline-row');
        const svg = document.querySelector('#cursive-arrow-svg');
        const path = document.querySelector('#cursive-arrow-path');
        const arrowHead = document.querySelector('#arrow-head');

        // Dynamically build the SVG path based on row positions
        function updatePath() {
            if (!svg || !path) return;
            
            // Adjust SVG height to container
            const container = document.querySelector('#ed-scroll-tracks');
            svg.setAttribute('viewBox', `0 0 ${container.offsetWidth} ${container.offsetHeight}`);
            
            let pathString = "";
            let points = [];
            
            // Start point (top center)
            points.push({ x: container.offsetWidth / 2, y: 0 });
            
            rows.forEach((row, i) => {
                const dot = row.querySelector('.row-dot');
                if (dot) {
                    const rect = dot.getBoundingClientRect();
                    const containerRect = container.getBoundingClientRect();
                    points.push({
                        x: rect.left - containerRect.left + rect.width / 2,
                        y: rect.top - containerRect.top + rect.height / 2
                    });
                }
            });
            
            // End point (bottom center)
            points.push({ x: container.offsetWidth / 2, y: container.offsetHeight });

            // Generate bezier curve through points
            if (points.length > 0) {
                pathString += `M ${points[0].x} ${points[0].y} `;
                for (let i = 1; i < points.length; i++) {
                    const prev = points[i - 1];
                    const curr = points[i];
                    // Create a cursive swooping effect
                    const cp1x = prev.x;
                    const cp1y = prev.y + (curr.y - prev.y) / 2;
                    const cp2x = curr.x;
                    const cp2y = curr.y - (curr.y - prev.y) / 2;
                    pathString += `C ${cp1x} ${cp1y}, ${cp2x} ${cp2y}, ${curr.x} ${curr.y} `;
                }
                path.setAttribute('d', pathString);
            }
            
            return path;
        }

        // Initialize path and ScrollTrigger
        const generatedPath = updatePath();
        
        if (generatedPath) {
            const length = generatedPath.getTotalLength();
            gsap.set(generatedPath, { strokeDasharray: length, strokeDashoffset: length });
            gsap.set(arrowHead, { opacity: 0 });

            // Animate arrow drawing
            const arrowAnim = gsap.to(generatedPath, {
                strokeDashoffset: 0,
                ease: "none",
                scrollTrigger: {
                    trigger: "#ed-scroll-tracks",
                    start: "top 30%",
                    end: "bottom 80%",
                    scrub: 1,
                    onUpdate: (self) => {
                        // Calculate arrow head position and rotation
                        const progress = self.progress;
                        if (progress > 0 && progress < 1) {
                            gsap.set(arrowHead, { opacity: 1 });
                            const pt = generatedPath.getPointAtLength(length * progress);
                            const ptNext = generatedPath.getPointAtLength(length * progress + 1);
                            const angle = Math.atan2(ptNext.y - pt.y, ptNext.x - pt.x) * 180 / Math.PI;
                            gsap.set(arrowHead, {
                                x: pt.x,
                                y: pt.y,
                                rotation: angle,
                                transformOrigin: "center center"
                            });
                        } else {
                            gsap.set(arrowHead, { opacity: 0 });
                        }
                    }
                }
            });
        }

        // Handle Window Resize
        window.addEventListener('resize', () => {
            updatePath();
            ScrollTrigger.refresh();
        });

        // Fade in text blocks and cards according to card
        rows.forEach((row, i) => {
          const card = row.querySelector('.ed-parallax-item, .bg-white.rounded-\\\\[2rem\\\\]') || row.querySelector('a, div');
          const textBlock = row.querySelector('.ed-text-block');
          const dot = row.querySelector('.row-dot');

          // Parallax for cards
          if (card) {
            gsap.to(card, {
              yPercent: -10,
              ease: "none",
              scrollTrigger: {
                trigger: row,
                start: "top bottom",
                end: "bottom top",
                scrub: true
              }
            });
          }

          // Ensure text only appears when card is active (Cursive connection)
          if (textBlock) {
            gsap.fromTo(textBlock, 
              { opacity: 0, y: 30, filter: "blur(8px)" },
              { 
                opacity: 1, y: 0, filter: "blur(0px)", duration: 0.6, ease: "power3.out",
                scrollTrigger: {
                  trigger: row,
                  start: "top 60%",
                  end: "bottom 40%",
                  toggleActions: "play reverse play reverse"
                }
              }
            );
          }

          // Light up timeline dot
          if (dot) {
            ScrollTrigger.create({
              trigger: row,
              start: "top 60%",
              end: "bottom 40%",
              onEnter: () => gsap.to(dot, { backgroundColor: "#c97ce5", borderColor: "#c97ce5", scale: 1.6, boxShadow: "0 0 20px rgba(201,124,229,0.6)", duration: 0.4 }),
              onLeave: () => gsap.to(dot, { backgroundColor: "#fff", borderColor: "rgba(201,124,229,0.3)", scale: 1, boxShadow: "none", duration: 0.4 }),
              onEnterBack: () => gsap.to(dot, { backgroundColor: "#c97ce5", borderColor: "#c97ce5", scale: 1.6, boxShadow: "0 0 20px rgba(201,124,229,0.6)", duration: 0.4 }),
              onLeaveBack: () => gsap.to(dot, { backgroundColor: "#fff", borderColor: "rgba(201,124,229,0.3)", scale: 1, boxShadow: "none", duration: 0.4 })
            });
          }
        });
      }

      // 4. Reveal Animations (Blur -> Sharp)'''
      
    content = gsap_pattern.sub(new_gsap, content)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done")

process_html()
