import re
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the entire #about section
start_marker = r'<!-- ABOUT: CINEMATIC EDITORIAL CANVAS -->'
end_marker = r'<!-- 3\. PROFESSIONAL JOURNEY -->'

new_about_section = """<!-- ABOUT: CINEMATIC EDITORIAL CANVAS -->
<section class="editorial-canvas font-sans relative z-20 overflow-hidden bg-[#FAFAFA] text-gray-900" id="about">
  
  <!-- Massive invisible canvas for SVG drawing -->
  <svg id="timeline-svg" class="absolute inset-0 w-full h-full pointer-events-none z-[100] hidden md:block"></svg>

  <div class="relative w-full max-w-[1200px] mx-auto px-6 lg:px-12 z-10 flex flex-col pt-[15vh] pb-[25vh]" id="timeline-container">
    
    <!-- Row 1: Collage + Text -->
    <div class="w-full flex justify-between items-start mt-12 timeline-node">
      <div class="w-[45%] max-w-[400px]" id="node-1">
        <div class="w-full relative rounded-3xl overflow-hidden shadow-2xl bg-white p-2">
          <img alt="Editorial Side" class="w-full h-auto rounded-2xl" src="bg1.png"/>
        </div>
      </div>
      <div class="w-[50%] flex flex-col justify-center pt-12">
        <h1 class="brand font-bold text-[clamp(32px,4vw,56px)] leading-[1.1] text-gray-900 tracking-tighter mb-6">
          I design intelligent<br/>systems.
        </h1>
        <p class="font-sans text-[clamp(14px,1.5vw,18px)] text-gray-600 leading-[1.5] font-bold">
          Class of 2026 Graduate learning scale.<br/>
          Software engineer &amp; cybersecurity researcher learning speed.<br/>
          Published researcher at <span class="text-purple-600">ICTACA'26.</span>
        </p>
      </div>
    </div>

    <!-- Row 2: Circular Badge -->
    <div class="w-full flex justify-center mt-32 timeline-node">
      <div class="relative w-[280px] h-[280px] rounded-full flex items-center justify-center bg-white/80 backdrop-blur-md shadow-[0_20px_60px_-15px_rgba(0,0,0,0.1)] border border-gray-100" id="node-2">
        <div class="absolute z-10 w-8 h-8 flex items-center justify-center">
          <svg viewBox="0 0 24 24" fill="#9d4edd" class="w-8 h-8"><path d="M12 2l2.4 7.6h8l-6.4 4.8 2.4 7.6-6.4-4.8-6.4 4.8 2.4-7.6-6.4-4.8h8z"/></svg>
        </div>
        <svg class="w-[260px] h-[260px] animate-spin-slow" viewBox="0 0 200 200">
          <path id="circlePath" d="M 100, 100 m -80, 0 a 80,80 0 1,1 160,0 a 80,80 0 1,1 -160,0" fill="none" />
          <text fill="#111" font-weight="900" font-size="16" letter-spacing="3" font-family="sans-serif">
            <textPath href="#circlePath" startOffset="0%">
               INTENTION • INNOVATION • IMPACT • DESIGNING IMPACT WITH CODE &amp; CREATIVITY •
            </textPath>
          </text>
        </svg>
      </div>
    </div>

    <!-- Row 3: Text + Girl Photo -->
    <div class="w-full flex justify-between items-center mt-32 timeline-node">
      <div class="w-[45%] flex flex-col justify-center">
        <h2 class="text-4xl font-bold text-gray-900 mb-6 tracking-tight">I build premium<br/>interfaces.</h2>
        <p class="text-gray-500 font-medium text-sm leading-relaxed max-w-sm">
          Focusing on micro-animations, glassmorphic styling, and clean responsive layouts. 
          Striving for visual excellence that feels responsive and alive.
        </p>
      </div>
      <div class="w-[45%] max-w-[350px]" id="node-3">
        <div class="w-full relative rounded-3xl overflow-hidden shadow-2xl bg-white p-3">
          <img alt="Shakthi Sri" class="w-full h-auto rounded-2xl bg-gray-50" src="me.png"/>
        </div>
      </div>
    </div>

    <!-- Row 4: LinkedIn -->
    <div class="w-full flex justify-start mt-32 timeline-node">
      <div class="w-full max-w-[400px]" id="node-4">
        <a class="bg-white rounded-[2rem] p-6 shadow-xl flex flex-col justify-between h-[300px] w-full text-black transform transition-transform hover:-translate-y-2 cursor-pointer border border-gray-100 block" href="https://linkedin.com/in/shakthisri" target="_blank">
          <div class="flex justify-between items-start w-full">
            <div class="w-12 h-12 rounded-full bg-[#0a66c2] flex items-center justify-center shadow-inner">
              <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"></path></svg>
            </div>
            <div class="flex items-center gap-1 border border-gray-200 rounded-md px-3 py-1 bg-gray-50">
              <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wide">Visit</span>
            </div>
          </div>
          <div class="mt-4 mb-auto">
            <h3 class="font-bold text-xl text-gray-900 mb-1">LinkedIn</h3>
            <p class="text-xs text-gray-400 font-medium">Professional Network</p>
            <div class="flex flex-wrap gap-2 mt-4">
              <span class="text-[10px] bg-gray-100 text-gray-600 px-3 py-1 rounded-full font-bold">Connect</span>
              <span class="text-[10px] bg-gray-100 text-gray-600 px-3 py-1 rounded-full font-bold">Hire Me</span>
            </div>
          </div>
          <div class="pt-4 border-t border-gray-100 flex justify-between items-center mt-4">
            <span class="font-bold text-md text-gray-900 truncate max-w-[120px]">@Shakthi16</span>
            <span class="bg-gray-900 text-white text-[11px] font-bold px-4 py-2 rounded-lg hover:bg-gray-800 transition-colors inline-block">View Profile</span>
          </div>
        </a>
      </div>
    </div>

    <!-- Row 5: Shavira Studio -->
    <div class="w-full flex justify-between items-center mt-32 timeline-node">
      <div class="w-[45%] flex flex-col justify-center">
        <h2 class="text-4xl font-bold text-gray-900 mb-6 tracking-tight">Crafting bespoke digital products.</h2>
        <p class="text-gray-500 font-medium text-sm leading-relaxed max-w-sm mb-4">
          Delivering design and code collaborations under the studio banner SHAVIRA.
        </p>
        <p class="text-gray-500 font-medium text-sm leading-relaxed max-w-sm">
          Creating high-performance full-stack web applications with robust security.
        </p>
      </div>
      <div class="w-full max-w-[400px]" id="node-5">
        <a class="bg-white rounded-[2rem] p-6 shadow-xl flex flex-col justify-between h-[300px] w-full text-black transform transition-transform hover:-translate-y-2 cursor-pointer border border-gray-100 block" href="https://www.instagram.com/shaviraworks" target="_blank">
          <div class="flex justify-between items-start w-full">
            <div class="w-12 h-12 rounded-full bg-[#421835] flex items-center justify-center shadow-inner">
              <span class="text-white font-bold font-sans text-xl">S</span>
            </div>
            <div class="flex items-center gap-1 border border-gray-200 rounded-md px-3 py-1 bg-gray-50">
              <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wide">Studio</span>
            </div>
          </div>
          <div class="mt-4 mb-auto">
            <h3 class="font-bold text-xl text-gray-900 mb-1">SHAVIRA</h3>
            <p class="text-xs text-gray-400 font-medium mb-2">Creative Freelance &amp; Design</p>
            <p class="text-[11px] text-gray-500 leading-relaxed line-clamp-3">Designing premium web interfaces, robust backend systems, and secure applications.</p>
          </div>
          <div class="pt-4 border-t border-gray-100 flex justify-between items-center mt-4">
            <span class="font-bold text-md text-gray-900 truncate max-w-[120px]">@shavira.studio</span>
            <span class="bg-gray-900 text-white text-[11px] font-bold px-4 py-2 rounded-lg hover:bg-gray-800 transition-colors inline-block">Follow</span>
          </div>
        </a>
      </div>
    </div>

  </div>
</section>
"""

pattern = re.compile(start_marker + r'.*?' + end_marker, re.DOTALL)
if not pattern.search(html):
    print("Could not find about section to replace!")
    sys.exit(1)

html = pattern.sub(new_about_section + '\n<!-- 3. PROFESSIONAL JOURNEY -->', html)


# 2. Add the GSAP vector drawing logic right before </body>
gsap_logic = """
<script>
document.addEventListener("DOMContentLoaded", () => {
    // Premium Editorial Connection System
    const svg = document.querySelector('#timeline-svg');
    const container = document.querySelector('#timeline-container');
    
    if (svg && container) {
        const targetNodes = [
           document.querySelector('#node-1'), // Collage
           document.querySelector('#node-2'), // Center Badge
           document.querySelector('#node-3'), // Girl Photo
           document.querySelector('#node-4'), // LinkedIn
           document.querySelector('#node-5')  // Shavira
        ];

        let drawnElements = [];
        let pathsToAnimate = [];

        function drawPaths() {
           svg.setAttribute('viewBox', `0 0 ${container.offsetWidth} ${container.offsetHeight}`);
           
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
               t.setAttribute("fill", "#888"); 
               t.setAttribute("font-size", "9");
               t.setAttribute("font-weight", "800");
               t.setAttribute("letter-spacing", "3");
               t.setAttribute("font-family", "sans-serif");
               t.textContent = textStr;
               svg.appendChild(t);
               drawnElements.push(t);
           }
           
           // Elegant Arrowhead Marker
           const defs = document.createElementNS(ns, "defs");
           const marker = document.createElementNS(ns, "marker");
           marker.setAttribute("id", "editorial-arrow");
           marker.setAttribute("viewBox", "0 0 10 10");
           marker.setAttribute("refX", "5");
           marker.setAttribute("refY", "5");
           marker.setAttribute("markerWidth", "3");
           marker.setAttribute("markerHeight", "3");
           marker.setAttribute("orient", "auto-start-reverse");
           const arrowPath = document.createElementNS(ns, "path");
           arrowPath.setAttribute("d", "M 0 0 L 10 5 L 0 10 z");
           arrowPath.setAttribute("fill", "#111");
           marker.appendChild(arrowPath);
           defs.appendChild(marker);
           svg.appendChild(defs);
           drawnElements.push(defs);

           // THE HERO PATH - Hand-crafted Bezier loops for organic flow
           
           // Collage to Center Badge: Deep sweeping S-curve
           let d1 = `M ${points[0].x} ${points[0].y} C ${points[0].x + 300} ${points[0].y + 150}, ${points[1].x - 300} ${points[1].y - 200}, ${points[1].x} ${points[1].y}`;
           let p1 = createPath(d1, "#111", "1.5");
           pathsToAnimate.push(p1);

           // Badge to Girl Photo: Subtle loop / Figure-8
           let d2 = `M ${points[1].x} ${points[1].y} C ${points[1].x + 250} ${points[1].y + 250}, ${points[2].x - 200} ${points[2].y - 300}, ${points[2].x} ${points[2].y}`;
           let p2 = createPath(d2, "#111", "1.5");
           pathsToAnimate.push(p2);

           // Girl Photo to LinkedIn: Large crossover intersection
           let d3 = `M ${points[2].x} ${points[2].y} C ${points[2].x - 100} ${points[2].y + 250}, ${points[3].x + 200} ${points[3].y - 150}, ${points[3].x} ${points[3].y}`;
           let p3 = createPath(d3, "#111", "1.5");
           pathsToAnimate.push(p3);

           // LinkedIn to Shavira: Final swoop with arrow
           let d4 = `M ${points[3].x} ${points[3].y} C ${points[3].x + 400} ${points[3].y + 100}, ${points[4].x - 300} ${points[4].y - 50}, ${points[4].x} ${points[4].y}`;
           let p4 = createPath(d4, "#111", "1.5");
           p4.setAttribute("marker-end", "url(#editorial-arrow)");
           pathsToAnimate.push(p4);

           // Decorative Hub Paths (Secondary flow converging at center)
           const cx = points[1].x;
           const cy = points[1].y;
           const hubPathD = `M ${cx - 400} ${cy - 50} C ${cx - 150} ${cy - 200}, ${cx + 150} ${cy + 250}, ${cx + 400} ${cy + 50}`;
           let pHub = createPath(hubPathD, "#ccc", "1", "4 4");
           pathsToAnimate.push(pHub);

           // Node Decorations & Micro-Interactions
           const labels = ["START", "FOCUS", "BUILD", "CONNECT", "SHIP"];
           points.forEach((pt, i) => {
               // Pink accent dots directly over the card
               createCircle(pt.x, pt.y, 4, "#E85D8A");
               
               // Hollow luxury rings
               createCircle(pt.x, pt.y, 16, "none", "#E85D8A", "1");
               
               // Editorial micro-labels
               if (labels[i]) {
                   createLabel(pt.x + 24, pt.y + 4, labels[i]);
               }
           });
           
           // Extra Sparkles
           createLabel(points[0].x + (points[1].x - points[0].x)*0.4, points[0].y + (points[1].y - points[0].y)*0.4, "✦ RESEARCH");
           createLabel(points[2].x + (points[3].x - points[2].x)*0.3, points[2].y + (points[3].y - points[2].y)*0.3 - 20, "✦ DESIGN");
        }

        drawPaths();

        if (typeof gsap !== 'undefined') {
            pathsToAnimate.forEach((p) => {
               const length = p.getTotalLength();
               gsap.set(p, { strokeDasharray: length, strokeDashoffset: length });

               gsap.to(p, {
                   strokeDashoffset: 0,
                   ease: "none",
                   scrollTrigger: {
                       trigger: "#timeline-container",
                       start: "top 70%",
                       end: "bottom 90%",
                       scrub: 1
                   }
               });
            });
        }

        window.addEventListener('resize', () => {
            drawPaths();
            pathsToAnimate.forEach(p => {
               const length = p.getTotalLength();
               if(typeof gsap !== 'undefined') gsap.set(p, { strokeDasharray: length, strokeDashoffset: 0 });
            });
            if(typeof ScrollTrigger !== 'undefined') ScrollTrigger.refresh();
        });
    }
});
</script>
</body>
"""

# Inject GSAP logic right before </body>
html = html.replace('</body>', gsap_logic)

# Make sure CSS for spin exists
spin_css = """
<style>
  @keyframes spin-slow {
    100% { transform: rotate(360deg); }
  }
  .animate-spin-slow {
    animation: spin-slow 15s linear infinite;
  }
</style>
"""
if "animate-spin-slow" not in html:
    html = html.replace('</head>', f'{spin_css}\n</head>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Built massive hero timeline successfully!")
