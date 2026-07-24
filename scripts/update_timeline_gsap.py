import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = r'// 3\. Editorial Scroll Canvas'
end_marker = r'// 4\. Reveal Animations'

new_gsap = """// 3. Editorial Scroll Canvas (Custom Curve Design)
      if (document.querySelector('#timeline-container')) {
        const svg = document.querySelector('#timeline-svg');
        const path = document.querySelector('#timeline-path');
        const container = document.querySelector('#timeline-container');
        
        // Define the nodes that the line should connect in order
        const targetNodes = [
           document.querySelector('#node-1 img'), // Collage
           document.querySelector('#node-2'), // Badge
           document.querySelector('#node-4'), // Girl photo
           document.querySelector('#node-5 a'), // LinkedIn
           document.querySelector('#node-6 a') // Shavira
        ];

        let dots = [];

        function drawPath() {
           if (!svg || !path || !targetNodes[0]) return;
           
           svg.setAttribute('viewBox', `0 0 ${container.offsetWidth} ${container.offsetHeight}`);
           
           // Clear old dots
           dots.forEach(dot => dot.remove());
           dots = [];

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

           // Generate smooth bezier curve through points
           let pathString = `M ${points[0].x} ${points[0].y} `;
           
           for (let i = 0; i < points.length - 1; i++) {
               const current = points[i];
               const next = points[i + 1];
               
               // Control points for a swooping 'S' curve feel
               const cp1x = current.x + (next.x - current.x) * 0.1;
               const cp1y = current.y + (next.y - current.y) * 0.8;
               const cp2x = next.x - (next.x - current.x) * 0.1;
               const cp2y = next.y - (next.y - current.y) * 0.2;
               
               pathString += `C ${cp1x} ${cp1y}, ${cp2x} ${cp2y}, ${next.x} ${next.y} `;
           }
           
           path.setAttribute('d', pathString);

           // Create node dots on the SVG
           points.forEach(pt => {
               const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
               circle.setAttribute("cx", pt.x);
               circle.setAttribute("cy", pt.y);
               circle.setAttribute("r", "5");
               circle.setAttribute("fill", "#fafafc");
               circle.setAttribute("stroke", "#c97ce5");
               circle.setAttribute("stroke-width", "3");
               svg.appendChild(circle);
               dots.push(circle);
           });
           
           return path;
        }

        const drawnPath = drawPath();

        if (drawnPath) {
           const length = drawnPath.getTotalLength();
           gsap.set(drawnPath, { strokeDasharray: length, strokeDashoffset: length });

           gsap.to(drawnPath, {
               strokeDashoffset: 0,
               ease: "none",
               scrollTrigger: {
                   trigger: "#timeline-container",
                   start: "top 30%",
                   end: "bottom 80%",
                   scrub: 1
               }
           });
        }

        window.addEventListener('resize', () => {
            drawPath();
            ScrollTrigger.refresh();
        });
      }

      """

pattern = re.compile(start_marker + r'.*?' + end_marker, re.DOTALL)
html = pattern.sub(new_gsap + end_marker, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated GSAP timeline logic!")
