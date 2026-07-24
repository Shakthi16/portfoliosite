import re
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Contact Footer text color (replace background image with gradient)
shakthi_target = r'<h2 id="flowing-text".*?SHAKTHI SRI T S\s*</h2>'
new_h2 = r'''<h2 id="flowing-text" class="contact-bg-text select-none text-center tracking-tighter w-full" style="background-image: linear-gradient(90deg, #421835 0%, #a4768f 25%, #421835 50%, #a4768f 75%, #421835 100%); background-size: 200%; background-position: 0% 50%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; transition: background-position 0.3s ease-out;">
            SHAKTHI SRI T S
          </h2>'''
html = re.sub(shakthi_target, new_h2, html, flags=re.DOTALL)

# 2. Rebuild #about section with masonry/absolute layout for Desktop
start_marker = r'<!-- ABOUT: CINEMATIC EDITORIAL CANVAS -->'
end_marker = r'<!-- 3\. PROFESSIONAL JOURNEY -->'

new_about_section = """<!-- ABOUT: CINEMATIC EDITORIAL CANVAS -->
<section class="editorial-canvas font-sans relative z-20 overflow-hidden bg-[#FAFAFA] text-gray-900" id="about">
  
  <!-- Canvas for SVG drawing -->
  <svg id="timeline-svg" class="absolute inset-0 w-full h-full pointer-events-none z-[100] hidden md:block"></svg>

  <div class="relative w-full max-w-[1200px] mx-auto px-6 lg:px-12 z-10 hidden md:block" id="timeline-container" style="height: 1700px;">
    
    <!-- Row 1: Collage (Left) & Text (Right) -->
    <div class="absolute top-[100px] left-[0px] w-[350px] timeline-node" id="node-1">
      <div class="w-full relative rounded-[2rem] overflow-hidden shadow-2xl bg-white p-2 border border-gray-100">
        <img alt="Editorial Side" class="w-full h-auto rounded-[1.5rem]" src="bg1.png"/>
      </div>
    </div>
    
    <div class="absolute top-[120px] left-[420px] w-[500px]">
      <h1 class="brand font-bold text-[56px] leading-[1.0] text-gray-900 tracking-tighter mb-4">
        I design intelligent<br/>systems.
      </h1>
      <p class="font-sans text-[16px] text-gray-600 leading-[1.6] font-medium">
        Class of 2026 Graduate learning scale.<br/>
        Software engineer &amp; cybersecurity researcher learning speed.<br/>
        Published researcher at <span class="text-[#421835] font-bold">ICTACA'26.</span>
      </p>
    </div>

    <!-- Row 2: Circular Badge (Left), Text (Center), Girl (Right) -->
    <div class="absolute top-[600px] left-[150px] timeline-node" id="node-2">
      <div class="relative w-[280px] h-[280px] rounded-full flex items-center justify-center bg-white/80 backdrop-blur-md shadow-[0_20px_60px_-15px_rgba(0,0,0,0.1)] border border-gray-100">
        <div class="absolute z-10 w-8 h-8 flex items-center justify-center">
          <svg viewBox="0 0 24 24" fill="#a4768f" class="w-8 h-8"><path d="M12 2l2.4 7.6h8l-6.4 4.8 2.4 7.6-6.4-4.8-6.4 4.8 2.4-7.6-6.4-4.8h8z"/></svg>
        </div>
        <svg class="w-[260px] h-[260px] animate-spin-slow" viewBox="0 0 200 200">
          <path id="circlePath" d="M 100, 100 m -80, 0 a 80,80 0 1,1 160,0 a 80,80 0 1,1 -160,0" fill="none" />
          <text fill="#111" font-weight="900" font-size="14" letter-spacing="4" font-family="sans-serif">
            <textPath href="#circlePath" startOffset="0%">
               INTENTION • INNOVATION • IMPACT • DESIGNING IMPACT WITH CODE &amp; CREATIVITY •
            </textPath>
          </text>
        </svg>
      </div>
    </div>

    <div class="absolute top-[650px] left-[480px] w-[300px]">
      <h2 class="text-[32px] font-bold text-gray-900 mb-4 tracking-tight leading-[1.1]">I build premium<br/>interfaces.</h2>
      <p class="text-gray-500 font-medium text-[13px] leading-relaxed">
        Focusing on micro-animations, glassmorphic styling, and clean responsive layouts.<br/>
        Striving for visual excellence that feels responsive and alive.
      </p>
    </div>

    <div class="absolute top-[450px] right-[0px] w-[350px] timeline-node" id="node-3">
      <div class="w-full relative rounded-[2rem] overflow-hidden shadow-2xl bg-white p-2 border border-gray-100">
        <img alt="Shakthi Sri" class="w-full h-auto rounded-[1.5rem] bg-gray-50" src="me.png"/>
      </div>
    </div>

    <!-- Row 3: LinkedIn (Left), Text (Center), Shavira (Right) -->
    <div class="absolute top-[1050px] left-[50px] w-[350px] timeline-node" id="node-4">
      <a class="bg-white rounded-[2rem] p-6 shadow-xl flex flex-col justify-between h-[300px] w-full text-black transform transition-transform hover:-translate-y-2 cursor-pointer border border-gray-100 block" href="https://linkedin.com/in/shakthisri" target="_blank">
        <div class="flex justify-between items-start w-full">
          <div class="w-12 h-12 rounded-full bg-[#0a66c2] flex items-center justify-center shadow-inner">
            <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"></path></svg>
          </div>
          <div class="flex items-center gap-1 border border-gray-200 rounded-md px-3 py-1 bg-gray-50">
            <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wide">VERIFIED</span>
          </div>
        </div>
        <div class="mt-4 mb-auto">
          <h3 class="font-bold text-xl text-gray-900 mb-1">LinkedIn</h3>
          <p class="text-[11px] text-gray-400 font-medium">Professional Network</p>
          <div class="flex flex-wrap gap-2 mt-4">
            <span class="text-[10px] bg-gray-100 text-gray-600 px-3 py-1 rounded-full font-bold">Researcher</span>
            <span class="text-[10px] bg-gray-100 text-gray-600 px-3 py-1 rounded-full font-bold">Tech Enthusiast</span>
          </div>
        </div>
        <div class="pt-4 border-t border-gray-100 flex justify-between items-center mt-4">
          <span class="font-bold text-sm text-gray-900">@Shakthi16</span>
          <span class="bg-[#111] text-white text-[11px] font-bold px-4 py-2 rounded-lg hover:bg-gray-800 transition-colors inline-block">View Profile</span>
        </div>
      </a>
    </div>

    <div class="absolute top-[1250px] left-[450px] w-[300px] text-center">
      <h2 class="text-[32px] font-bold text-gray-900 mb-4 tracking-tight leading-[1.1]">Crafting bespoke digital<br/>products.</h2>
      <p class="text-gray-500 font-medium text-[11px] leading-relaxed mb-4">
        Delivering design and code collaborations under the studio banner SHAVIRA.
      </p>
      <p class="text-gray-500 font-medium text-[11px] leading-relaxed">
        Creating high-performance full-stack web applications with robust security.
      </p>
    </div>

    <div class="absolute top-[1200px] right-[50px] w-[350px] timeline-node" id="node-5">
      <a class="bg-white rounded-[2rem] p-6 shadow-xl flex flex-col justify-between h-[300px] w-full text-black transform transition-transform hover:-translate-y-2 cursor-pointer border border-gray-100 block" href="https://www.instagram.com/shaviraworks" target="_blank">
        <div class="flex justify-between items-start w-full">
          <div class="w-12 h-12 rounded-full bg-[#421835] flex items-center justify-center shadow-inner">
            <span class="text-white font-bold font-sans text-xl">S</span>
          </div>
          <div class="flex items-center gap-1 border border-gray-200 rounded-md px-3 py-1 bg-gray-50">
            <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wide">STUDIO</span>
          </div>
        </div>
        <div class="mt-4 mb-auto">
          <h3 class="font-bold text-xl text-gray-900 mb-1">SHAVIRA</h3>
          <p class="text-[11px] text-gray-400 font-medium mb-2">Creative Freelance &amp; Design</p>
          <p class="text-[11px] text-gray-500 leading-relaxed line-clamp-3">Designing premium web interfaces, visual brand systems, and secure applications. Available for contract collaborations.</p>
        </div>
        <div class="pt-4 border-t border-gray-100 flex justify-between items-center mt-4">
          <span class="font-bold text-sm text-gray-900">@shavira.studio</span>
          <span class="bg-[#111] text-white text-[11px] font-bold px-4 py-2 rounded-lg hover:bg-gray-800 transition-colors inline-block">Follow</span>
        </div>
      </a>
    </div>

  </div>

  <!-- Mobile Fallback -->
  <div class="relative w-full max-w-[1200px] mx-auto px-6 py-[10vh] flex flex-col gap-24 md:hidden">
      <!-- Same elements in column flow -->
      <div class="w-full text-center">
        <h1 class="brand font-bold text-[40px] leading-[1.0] text-gray-900 tracking-tighter mb-4">I design intelligent<br/>systems.</h1>
      </div>
      <div class="w-full relative rounded-[2rem] overflow-hidden shadow-2xl bg-white p-2 border border-gray-100">
        <img alt="Editorial Side" class="w-full h-auto rounded-[1.5rem]" src="bg1.png"/>
      </div>
      <div class="w-full flex justify-center">
        <div class="relative w-[280px] h-[280px] rounded-full flex items-center justify-center bg-white/80 shadow-2xl border border-gray-100">
          <div class="absolute z-10 w-8 h-8 flex items-center justify-center">
            <svg viewBox="0 0 24 24" fill="#a4768f" class="w-8 h-8"><path d="M12 2l2.4 7.6h8l-6.4 4.8 2.4 7.6-6.4-4.8-6.4 4.8 2.4-7.6-6.4-4.8h8z"/></svg>
          </div>
          <svg class="w-[260px] h-[260px] animate-spin-slow" viewBox="0 0 200 200">
            <path id="circlePathMobile" d="M 100, 100 m -80, 0 a 80,80 0 1,1 160,0 a 80,80 0 1,1 -160,0" fill="none" />
            <text fill="#111" font-weight="900" font-size="14" letter-spacing="4" font-family="sans-serif"><textPath href="#circlePathMobile" startOffset="0%">INTENTION • INNOVATION • IMPACT • DESIGNING IMPACT WITH CODE &amp; CREATIVITY •</textPath></text>
          </svg>
        </div>
      </div>
      <div class="w-full relative rounded-[2rem] overflow-hidden shadow-2xl bg-white p-2 border border-gray-100">
        <img alt="Shakthi Sri" class="w-full h-auto rounded-[1.5rem] bg-gray-50" src="me.png"/>
      </div>
  </div>
</section>
"""

pattern = re.compile(start_marker + r'.*?' + end_marker, re.DOTALL)
if not pattern.search(html):
    print("Could not find about section to replace!")
    sys.exit(1)

html = pattern.sub(new_about_section + '\n<!-- 3. PROFESSIONAL JOURNEY -->', html)


# 3. Replace the GSAP logic with EXACT arrow curves matching the mockup
gsap_old_pattern = re.compile(r'// Premium Editorial Connection System.*?</script>', re.DOTALL)

gsap_new_logic = """// Premium Editorial Connection System
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
                       y: rect.top - containerRect.top + rect.height / 2,
                       w: rect.width,
                       h: rect.height,
                       top: rect.top - containerRect.top,
                       left: rect.left - containerRect.left,
                       right: rect.right - containerRect.left,
                       bottom: rect.bottom - containerRect.top
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
           
           // Arrowhead Marker
           const defs = document.createElementNS(ns, "defs");
           const marker = document.createElementNS(ns, "marker");
           marker.setAttribute("id", "editorial-arrow");
           marker.setAttribute("viewBox", "0 0 10 10");
           marker.setAttribute("refX", "9");
           marker.setAttribute("refY", "5");
           marker.setAttribute("markerWidth", "5");
           marker.setAttribute("markerHeight", "5");
           marker.setAttribute("orient", "auto-start-reverse");
           const arrowPath = document.createElementNS(ns, "path");
           arrowPath.setAttribute("d", "M 0 2 L 10 5 L 0 8 z");
           arrowPath.setAttribute("fill", "none");
           arrowPath.setAttribute("stroke", "#444");
           arrowPath.setAttribute("stroke-width", "1");
           marker.appendChild(arrowPath);
           defs.appendChild(marker);
           svg.appendChild(defs);
           drawnElements.push(defs);

           // THE HERO PATHS (Exactly like mockup)
           const magenta = "#a4768f";
           const lineColor = "#666";

           // Line 1: Collage bottom-right to Girl photo left
           let n1 = points[0]; // Collage
           let n3 = points[2]; // Girl
           let n2 = points[1]; // Badge
           let n4 = points[3]; // LinkedIn
           let n5 = points[4]; // Shavira
           
           // Curve 1: From bottom center of collage to left of Girl Photo
           let pt1x = n1.x + 50; 
           let pt1y = n1.bottom;
           let pt2x = n3.left - 20;
           let pt2y = n3.y;
           
           let d1 = `M ${pt1x} ${pt1y} C ${pt1x + 100} ${pt1y + 150}, ${pt2x - 150} ${pt2y - 100}, ${pt2x} ${pt2y}`;
           let p1 = createPath(d1, lineColor, "1");
           p1.setAttribute("marker-end", "url(#editorial-arrow)");
           pathsToAnimate.push(p1);
           
           createCircle(pt1x, pt1y, 4, "white", magenta, "2"); // hollow dot
           createCircle(pt2x, pt2y, 4, magenta); // solid dot

           // Curve 2: From Girl Photo (left) loops down and points to Circular Badge (right)
           let pt3x = n3.left;
           let pt3y = n3.y + 100;
           let pt4x = n2.right + 10;
           let pt4y = n2.y;
           
           let d2 = `M ${pt3x} ${pt3y} C ${pt3x - 100} ${pt3y + 150}, ${pt4x + 150} ${pt4y + 150}, ${pt4x} ${pt4y}`;
           let p2 = createPath(d2, lineColor, "1");
           p2.setAttribute("marker-end", "url(#editorial-arrow)");
           pathsToAnimate.push(p2);
           
           createCircle(pt3x, pt3y, 4, "white", magenta, "2"); 

           // Curve 3: From Circular Badge (bottom) to LinkedIn (top right)
           let pt5x = n2.x;
           let pt5y = n2.bottom;
           let pt6x = n4.right + 20;
           let pt6y = n4.y - 50;
           
           let d3 = `M ${pt5x} ${pt5y} C ${pt5x + 50} ${pt5y + 150}, ${pt6x + 50} ${pt6y - 150}, ${pt6x} ${pt6y}`;
           let p3 = createPath(d3, lineColor, "1");
           pathsToAnimate.push(p3);
           
           createCircle(pt6x, pt6y, 4, "white", magenta, "2");

           // Curve 4: From LinkedIn to Shavira
           let pt7x = n4.right + 10;
           let pt7y = n4.y + 100;
           let pt8x = n5.left - 20;
           let pt8y = n5.y;
           
           let d4 = `M ${pt7x} ${pt7y} C ${pt7x + 100} ${pt7y + 100}, ${pt8x - 150} ${pt8y - 50}, ${pt8x} ${pt8y}`;
           let p4 = createPath(d4, lineColor, "1");
           pathsToAnimate.push(p4);
           
           createCircle(pt7x, pt7y, 4, "white", magenta, "2");
           createCircle(pt8x, pt8y, 4, magenta);

           // Curve 5: From Shavira (top center) curving right and down
           let pt9x = n5.x + 80;
           let pt9y = n5.top - 40;
           let pt10x = n5.right + 40;
           let pt10y = n5.y + 50;
           
           let d5 = `M ${pt9x} ${pt9y} C ${pt9x + 50} ${pt9y}, ${pt10x + 50} ${pt10y - 100}, ${pt10x} ${pt10y}`;
           let p5 = createPath(d5, lineColor, "1");
           p5.setAttribute("marker-end", "url(#editorial-arrow)");
           pathsToAnimate.push(p5);
           
           createCircle(pt9x, pt9y, 4, magenta);
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
                       start: "top 60%",
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
</script>"""

html = gsap_old_pattern.sub(gsap_new_logic, html)

# If the regex failed to find the gsap script (e.g. if the user's reset removed it)
if "// Premium Editorial Connection System" not in html:
    html = html.replace('</body>', '<script>\n' + gsap_new_logic + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Built editorial paths and updated hover color successfully!")
