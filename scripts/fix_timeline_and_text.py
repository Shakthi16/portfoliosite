import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the text mask hover effect
# Find the SHAKTHI SRI T S h2 and ensure it has id="flowing-text"
target_h2 = r'<h2 class="contact-bg-text select-none text-center tracking-tighter w-full" style="background-image: url\(\'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe\?q=80&w=2000&auto=format&fit=crop\'\); background-size: 150%; background-position: 50% 50%; -webkit-background-clip: text; -webkit-text-fill-color: transparent;">\s*SHAKTHI SRI T S\s*</h2>'
new_h2 = r'''<h2 id="flowing-text" class="contact-bg-text select-none text-center tracking-tighter w-full" style="background-image: url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2000&auto=format&fit=crop'); background-size: 150%; background-position: 50% 50%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; transition: background-position 0.2s ease-out;">
            SHAKTHI SRI T S
          </h2>'''

html = re.sub(target_h2, new_h2, html)

# Update the JS for flowing-text to use 'contact' section
old_js = r'''const textMaskSection = document.getElementById\('text-mask-section'\);'''
new_js = r'''const textMaskSection = document.getElementById('contact');'''
html = re.sub(old_js, new_js, html)

# 2. Fix the Timeline SVG
# Set z-index to 100 so arrows appear IN the cards
html = html.replace('id="timeline-svg" class="absolute inset-0 w-full h-full pointer-events-none z-10 hidden md:block"', 
                    'id="timeline-svg" class="absolute inset-0 w-full h-full pointer-events-none z-[100] hidden md:block"')

# Ensure the circular badge renders properly by making text darker and fixing viewBox
html = html.replace('fill="#444" font-weight="bold" font-size="14"', 'fill="#111" font-weight="900" font-size="16"')
# The badge might be hidden because the background was white/50, let's make it a more visible glass effect
html = html.replace('bg-white/50 backdrop-blur-sm', 'bg-white/80 backdrop-blur-md shadow-2xl')

# 3. Completely rewrite the GSAP JS for drawing the paths.
# We will replace the entire // 3. Editorial Scroll Canvas block
gsap_start = r'// 3\. Editorial Scroll Canvas \(Complex Procedural SVG Paths\)'
gsap_end = r'// 4\. Reveal Animations'

new_gsap = """// 3. Editorial Premium Vector Flow System
      if (document.querySelector('#timeline-container')) {
        const svg = document.querySelector('#timeline-svg');
        const container = document.querySelector('#timeline-container');
        
        // Define exact anchor points inside the cards
        const targetNodes = [
           document.querySelector('#node-1 img'), // Collage
           document.querySelector('#node-2'), // Center Badge
           document.querySelector('#node-4'), // Girl Photo
           document.querySelector('#node-5 a'), // LinkedIn
           document.querySelector('#node-6 a') // Shavira
        ];

        let drawnElements = [];
        let pathsToAnimate = [];

        function drawPaths() {
           if (!svg || !targetNodes[0]) return;
           
           svg.setAttribute('viewBox', `0 0 ${container.offsetWidth} ${container.offsetHeight}`);
           
           // Clear previous drawings
           drawnElements.forEach(el => el.remove());
           drawnElements = [];
           pathsToAnimate = [];

           let points = [];
           const containerRect = container.getBoundingClientRect();

           targetNodes.forEach(node => {
               if (node) {
                   const rect = node.getBoundingClientRect();
                   points.push({
                       x: rect.left - containerRect.left + rect.width / 2,
                       y: rect.top - containerRect.top + rect.height / 2
                   });
               }
           });

           if (points.length < 5) return;

           const ns = "http://www.w3.org/2000/svg";

           function createPath(d, stroke, width, dash = "") {
               const p = document.createElementNS(ns, "path");
               p.setAttribute("d", d);
               p.setAttribute("fill", "none");
               p.setAttribute("stroke", stroke);
               p.setAttribute("stroke-width", width);
               if (dash) p.setAttribute("stroke-dasharray", dash);
               svg.appendChild(p);
               drawnElements.push(p);
               return p;
           }

           function createCircle(cx, cy, r, fill, stroke, width) {
               const c = document.createElementNS(ns, "circle");
               c.setAttribute("cx", cx);
               c.setAttribute("cy", cy);
               c.setAttribute("r", r);
               c.setAttribute("fill", fill);
               if (stroke) c.setAttribute("stroke", stroke);
               if (width) c.setAttribute("stroke-width", width);
               svg.appendChild(c);
               drawnElements.push(c);
           }

           function createLabel(x, y, textStr) {
               const t = document.createElementNS(ns, "text");
               t.setAttribute("x", x);
               t.setAttribute("y", y);
               t.setAttribute("fill", "#666"); // subtle gray
               t.setAttribute("font-size", "9");
               t.setAttribute("font-weight", "800");
               t.setAttribute("letter-spacing", "3");
               t.setAttribute("font-family", "sans-serif");
               t.textContent = textStr;
               svg.appendChild(t);
               drawnElements.push(t);
           }
           
           // Elegant Arrowhead Marker Defs
           const defs = document.createElementNS(ns, "defs");
           const marker = document.createElementNS(ns, "marker");
           marker.setAttribute("id", "editorial-arrow");
           marker.setAttribute("viewBox", "0 0 10 10");
           marker.setAttribute("refX", "5");
           marker.setAttribute("refY", "5");
           marker.setAttribute("markerWidth", "4");
           marker.setAttribute("markerHeight", "4");
           marker.setAttribute("orient", "auto-start-reverse");
           const arrowPath = document.createElementNS(ns, "path");
           arrowPath.setAttribute("d", "M 0 0 L 10 5 L 0 10 z");
           arrowPath.setAttribute("fill", "#E85D8A");
           marker.appendChild(arrowPath);
           defs.appendChild(marker);
           svg.appendChild(defs);
           drawnElements.push(defs);

           // THE HERO PATH - Masterfully crafted Bezier loops
           // Instead of a single array loop, we hand-craft the elegant paths between nodes to guarantee premium layout.

           // Path 1: Node 1 (Collage) to Node 2 (Center Badge) - Sweeping loop
           let d1 = `M ${points[0].x} ${points[0].y} C ${points[0].x + 300} ${points[0].y + 100}, ${points[1].x - 300} ${points[1].y - 200}, ${points[1].x} ${points[1].y}`;
           let p1 = createPath(d1, "#111", "1.5");
           pathsToAnimate.push(p1);

           // Path 2: Node 2 (Center Badge) to Node 3 (Girl Photo) - Figure 8 exit
           let d2 = `M ${points[1].x} ${points[1].y} C ${points[1].x + 400} ${points[1].y + 300}, ${points[2].x - 200} ${points[2].y - 300}, ${points[2].x} ${points[2].y}`;
           let p2 = createPath(d2, "#111", "1.5");
           pathsToAnimate.push(p2);

           // Path 3: Node 3 (Girl Photo) to Node 4 (LinkedIn) - Large cross-canvas swoop
           let d3 = `M ${points[2].x} ${points[2].y} C ${points[2].x + 200} ${points[2].y + 300}, ${points[3].x - 200} ${points[3].y - 100}, ${points[3].x} ${points[3].y}`;
           let p3 = createPath(d3, "#111", "1.5");
           pathsToAnimate.push(p3);

           // Path 4: Node 4 (LinkedIn) to Node 5 (Shavira) - Organic bend
           let d4 = `M ${points[3].x} ${points[3].y} C ${points[3].x + 200} ${points[3].y + 200}, ${points[4].x - 200} ${points[4].y - 100}, ${points[4].x} ${points[4].y}`;
           let p4 = createPath(d4, "#111", "1.5");
           p4.setAttribute("marker-end", "url(#editorial-arrow)");
           pathsToAnimate.push(p4);

           // Decorative Hub Paths (Secondary visual flair around Center Badge)
           const cx = points[1].x;
           const cy = points[1].y;
           const hubPathD = `M ${cx - 300} ${cy - 50} C ${cx - 100} ${cy - 100}, ${cx + 100} ${cy + 150}, ${cx + 300} ${cy + 50}`;
           let pHub = createPath(hubPathD, "#ccc", "1", "4 4");
           pathsToAnimate.push(pHub);

           // Node Decorations & Micro-Interactions
           const labels = ["START", "FOCUS", "BUILD", "CONNECT", "SHIP"];
           points.forEach((pt, i) => {
               // The pink accent dot inside the card
               createCircle(pt.x, pt.y, 4, "#E85D8A");
               
               // Hollow luxury rings
               createCircle(pt.x, pt.y, 14, "none", "#E85D8A", "1");
               
               // Editorial micro-labels
               if (labels[i]) {
                   // Offset text slightly so it doesn't overlap the dot
                   createLabel(pt.x + 22, pt.y + 4, labels[i]);
               }
           });
           
           // Extra Sparkle/Star Symbols along the paths for luxury feel
           createLabel(points[0].x + (points[1].x - points[0].x)*0.5, points[0].y + (points[1].y - points[0].y)*0.5, "✦ RESEARCH");
           createLabel(points[2].x + (points[3].x - points[2].x)*0.3, points[2].y + (points[3].y - points[2].y)*0.3 - 20, "✦ DESIGN");
        }

        drawPaths();

        // Animate paths flowing down on scroll
        pathsToAnimate.forEach((p, idx) => {
           const length = p.getTotalLength();
           gsap.set(p, { strokeDasharray: length, strokeDashoffset: length });

           gsap.to(p, {
               strokeDashoffset: 0,
               ease: "none",
               scrollTrigger: {
                   trigger: "#timeline-container",
                   start: "top 60%", // Starts animating sooner
                   end: "bottom 80%",
                   scrub: 1
               }
           });
        });

        window.addEventListener('resize', () => {
            drawPaths();
            pathsToAnimate.forEach(p => {
               const length = p.getTotalLength();
               gsap.set(p, { strokeDasharray: length, strokeDashoffset: 0 }); // Show instantly on resize to avoid glitched refresh
            });
            ScrollTrigger.refresh();
        });
      }

"""

pattern = re.compile(gsap_start + r'.*?' + gsap_end, re.DOTALL)
html = pattern.sub(new_gsap + '\n      // 4. Reveal Animations', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated text mask and GSAP logic!")
