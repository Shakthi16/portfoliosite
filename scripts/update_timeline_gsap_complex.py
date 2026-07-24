import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = r'// 3\. Editorial Scroll Canvas'
end_marker = r'// 4\. Reveal Animations'

new_gsap = """// 3. Editorial Scroll Canvas (Complex Procedural SVG Paths)
      if (document.querySelector('#timeline-container')) {
        const svg = document.querySelector('#timeline-svg');
        const container = document.querySelector('#timeline-container');
        
        // The core nodes in the timeline
        const targetNodes = [
           document.querySelector('#node-1 img'),
           document.querySelector('#node-2'),
           document.querySelector('#node-4'),
           document.querySelector('#node-5 a'),
           document.querySelector('#node-6 a')
        ];

        let drawnElements = [];
        let pathsToAnimate = [];

        function drawPaths() {
           if (!svg || !targetNodes[0]) return;
           
           svg.setAttribute('viewBox', `0 0 ${container.offsetWidth} ${container.offsetHeight}`);
           
           // Clear old paths and decorations
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

           if (points.length < 2) return;

           const ns = "http://www.w3.org/2000/svg";

           // Helper to create paths
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

           // Helper to create decorations
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
               t.setAttribute("fill", "#888");
               t.setAttribute("font-size", "10");
               t.setAttribute("font-weight", "bold");
               t.setAttribute("letter-spacing", "2");
               t.textContent = textStr;
               svg.appendChild(t);
               drawnElements.push(t);
           }

           // MAIN PATH (The Flowing Journey)
           let pathString = `M ${points[0].x} ${points[0].y} `;
           
           for (let i = 0; i < points.length - 1; i++) {
               const curr = points[i];
               const next = points[i + 1];
               
               // Generate highly intricate overlapping curves
               // If going left to right vs right to left
               const dx = next.x - curr.x;
               const dy = next.y - curr.y;
               
               let cp1x, cp1y, cp2x, cp2y;
               
               if (i === 1) {
                   // Loop down and around into the center badge
                   cp1x = curr.x + dx * 1.5;
                   cp1y = curr.y + dy * 0.2;
                   cp2x = next.x - dx * 0.5;
                   cp2y = next.y - dy * 0.8;
               } else if (i === 2) {
                   // Swoop right to the girl photo
                   cp1x = curr.x;
                   cp1y = curr.y + dy * 0.8;
                   cp2x = next.x - dx * 0.5;
                   cp2y = next.y - dy * 0.2;
               } else if (i === 3) {
                   // Cross over figure-8 back to the left (LinkedIn)
                   cp1x = curr.x - container.offsetWidth * 0.2;
                   cp1y = curr.y + dy * 0.5;
                   cp2x = next.x + container.offsetWidth * 0.2;
                   cp2y = next.y - dy * 0.5;
               } else {
                   // Default graceful S-curve
                   cp1x = curr.x;
                   cp1y = curr.y + dy * 0.5;
                   cp2x = next.x;
                   cp2y = next.y - dy * 0.5;
               }
               
               pathString += `C ${cp1x} ${cp1y}, ${cp2x} ${cp2y}, ${next.x} ${next.y} `;
           }
           
           const mainPath = createPath(pathString, "#111", "1");
           pathsToAnimate.push(mainPath);

           // SECONDARY PATH (The Center Convergence)
           // Draw a sweeping line that starts from the left edge, loops through the center (brain), and goes right
           if (points[1]) {
               const bx = points[1].x;
               const by = points[1].y;
               const secPathString = `M 0 ${by - 200} C ${bx - 300} ${by - 100}, ${bx - 100} ${by + 200}, ${bx} ${by} C ${bx + 150} ${by - 150}, ${bx + 300} ${by + 100}, ${container.offsetWidth} ${by + 300}`;
               const secPath = createPath(secPathString, "#ccc", "1", "4 4");
               pathsToAnimate.push(secPath);
           }

           // DECORATIONS (Nodes, Accents, Labels)
           points.forEach((pt, index) => {
               // Pink accent dots
               createCircle(pt.x, pt.y, 4, "#E85D8A");
               
               // Hollow ring wrappers around main nodes
               if (index !== 1) { // Skip center badge
                   createCircle(pt.x, pt.y, 16, "none", "#ddd", "1");
               }

               // Micro labels
               const labels = ["START", "FOCUS", "BUILD", "CONNECT", "SHIP"];
               if (labels[index]) {
                   // Position label slightly off the dot
                   createLabel(pt.x + 24, pt.y - 12, labels[index]);
               }
           });
           
           // Extra mid-way decorations
           if (points.length >= 4) {
               const midPt = {
                   x: points[2].x + (points[3].x - points[2].x) * 0.5,
                   y: points[2].y + (points[3].y - points[2].y) * 0.5
               };
               createCircle(midPt.x, midPt.y, 3, "#E85D8A");
               createCircle(midPt.x, midPt.y, 12, "none", "#ddd", "1");
               createLabel(midPt.x + 16, midPt.y + 4, "CROSSOVER");
           }
        }

        drawPaths();

        // Animate all generated paths
        pathsToAnimate.forEach(p => {
           const length = p.getTotalLength();
           gsap.set(p, { strokeDasharray: length, strokeDashoffset: length });

           gsap.to(p, {
               strokeDashoffset: 0,
               ease: "none",
               scrollTrigger: {
                   trigger: "#timeline-container",
                   start: "top 40%",
                   end: "bottom 80%",
                   scrub: 1
               }
           });
        });

        window.addEventListener('resize', () => {
            drawPaths();
            // Re-apply animations after redraw
            pathsToAnimate.forEach(p => {
               const length = p.getTotalLength();
               gsap.set(p, { strokeDasharray: length, strokeDashoffset: 0 }); // Just show them on resize to prevent buggy scrollTrigger refresh resets
            });
            ScrollTrigger.refresh();
        });
      }

      """

pattern = re.compile(start_marker + r'.*?' + end_marker, re.DOTALL)
html = pattern.sub(new_gsap + end_marker, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated GSAP timeline logic for complex paths!")
