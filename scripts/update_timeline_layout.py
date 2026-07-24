import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the #about section block
start_marker = r'<!-- ABOUT: CINEMATIC EDITORIAL CANVAS -->'
end_marker = r'<!-- PROJECTS \(GRID VIEW\) -->'

# We will replace everything between these markers.
new_about_section = """<!-- ABOUT: CINEMATIC EDITORIAL CANVAS -->
    <section class="editorial-canvas font-sans relative z-20 bg-[#fdfcfb] text-gray-900 overflow-hidden" id="about">
      
      <!-- Background elements for depth -->
      <div class="absolute inset-0 z-0 pointer-events-none opacity-50 overflow-hidden">
        <div class="absolute top-[-10%] right-[-10%] w-[500px] h-[500px] bg-red-100 rounded-full blur-[100px]"></div>
        <div class="absolute top-[40%] left-[-10%] w-[400px] h-[400px] bg-purple-100 rounded-full blur-[100px]"></div>
      </div>

      <!-- SVG Arrow Overlay -->
      <svg id="timeline-svg" class="absolute inset-0 w-full h-full pointer-events-none z-10 hidden md:block" style="min-height: 2500px;">
        <path id="timeline-path" fill="none" stroke="#555" stroke-width="1.5" stroke-dasharray="8 8" />
        <!-- We will generate dynamic circles at JS level for nodes -->
      </svg>

      <div class="relative w-full max-w-[1400px] mx-auto px-6 lg:px-12 z-20 py-24 pb-48 flex flex-col items-center" id="timeline-container">
        
        <!-- Element 1: Top Row (Collage + Text) -->
        <div class="w-full flex flex-col lg:flex-row items-center justify-between gap-12 mt-12 timeline-node" id="node-1">
          <!-- Left: Collage -->
          <div class="w-full lg:w-[45%] flex justify-center lg:justify-start">
            <div class="w-full max-w-[450px] bg-white rounded-3xl p-2 shadow-2xl transform hover:scale-[1.02] transition-transform">
              <img src="bg1.png" alt="Collage" class="w-full h-auto rounded-2xl" />
            </div>
          </div>
          <!-- Right: Text -->
          <div class="w-full lg:w-[50%] flex flex-col justify-center items-center lg:items-start text-center lg:text-left">
            <h1 class="brand font-bold text-[clamp(32px,4vw,56px)] leading-[1.1] tracking-tighter mb-6 text-gray-900">
              I design intelligent<br/>systems.
            </h1>
            <p class="font-sans text-[clamp(16px,1.5vw,20px)] text-gray-600 leading-[1.5] font-medium max-w-lg">
              Class of 2026 Graduate learning scale.<br />
              Software engineer &amp; cybersecurity researcher learning speed.<br />
              Published researcher at <span class="text-purple-600 font-bold">ICTACA'26.</span>
            </p>
          </div>
        </div>

        <!-- Element 2: Spinning Circular Badge -->
        <div class="w-full flex justify-center mt-32 timeline-node relative z-20" id="node-2">
          <div class="relative w-[250px] h-[250px] rounded-full border border-gray-200 bg-white/50 backdrop-blur-sm shadow-xl flex items-center justify-center">
            <!-- Center Star -->
            <div class="absolute z-10 w-8 h-8 flex items-center justify-center">
              <svg viewBox="0 0 24 24" fill="#9d4edd" class="w-8 h-8"><path d="M12 2l2.4 7.6h8l-6.4 4.8 2.4 7.6-6.4-4.8-6.4 4.8 2.4-7.6-6.4-4.8h8z"/></svg>
            </div>
            <!-- Spinning Text SVG -->
            <svg class="w-[240px] h-[240px] animate-spin-slow" viewBox="0 0 200 200">
              <path id="circlePath" d="M 100, 100 m -80, 0 a 80,80 0 1,1 160,0 a 80,80 0 1,1 -160,0" fill="none" />
              <text fill="#444" font-weight="bold" font-size="14" letter-spacing="3">
                <textPath href="#circlePath" startOffset="0%">
                   INTENTION • INNOVATION • IMPACT • DESIGNING IMPACT WITH CODE &amp; CREATIVITY •
                </textPath>
              </text>
            </svg>
          </div>
        </div>

        <!-- Element 3: Text Block 2 (Middle Left) -->
        <div class="w-full flex flex-col md:flex-row justify-between items-center mt-32 px-4 md:px-24 timeline-node" id="node-3">
          <div class="max-w-sm text-center md:text-left mb-12 md:mb-0">
             <h2 class="text-3xl font-bold text-gray-900 mb-4 tracking-tight">I build premium<br/>interfaces.</h2>
             <p class="text-gray-500 font-medium text-sm leading-relaxed">
               Focusing on micro-animations, glassmorphic styling, and clean responsive layouts. Striving for visual excellence that feels responsive and alive.
             </p>
          </div>
          <!-- Element 4: Girl Photo (Middle Right) -->
          <div class="w-full max-w-[320px] bg-white rounded-3xl p-3 shadow-xl transform hover:-translate-y-2 transition-transform timeline-node" id="node-4">
             <img src="me.png" alt="Profile" class="w-full h-auto rounded-2xl bg-gray-50" />
             <div class="flex justify-end mt-4 px-2 pb-2">
                <div class="w-6 h-[2px] bg-gray-400"></div>
                <div class="w-6 h-[2px] bg-gray-400 ml-1"></div>
             </div>
          </div>
        </div>

        <!-- Element 5: LinkedIn Card (Bottom Left) -->
        <div class="w-full flex justify-start mt-32 px-4 md:px-12 timeline-node" id="node-5">
           <a href="https://linkedin.com/in/shakthisri" target="_blank" class="w-full max-w-[350px] bg-white rounded-[2rem] p-6 shadow-xl flex flex-col justify-between h-[300px] text-black transform transition-transform hover:-translate-y-2 border border-gray-100 block">
                <div class="flex justify-between items-start w-full">
                  <div class="w-12 h-12 rounded-full bg-[#0a66c2] flex items-center justify-center shadow-inner">
                    <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"></path>
                    </svg>
                  </div>
                  <div class="flex items-center gap-1 border border-gray-200 rounded-md px-3 py-1 bg-gray-50">
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wide">Verified</span>
                  </div>
                </div>
                <div class="mt-4 mb-auto">
                  <h3 class="font-bold text-xl text-gray-900 mb-1">LinkedIn</h3>
                  <p class="text-xs text-gray-400 font-medium">Professional Network</p>
                  <div class="flex flex-wrap gap-2 mt-4">
                    <span class="text-[10px] bg-gray-100 text-gray-600 px-3 py-1 rounded-full font-bold">Researcher</span>
                    <span class="text-[10px] bg-gray-100 text-gray-600 px-3 py-1 rounded-full font-bold">Tech Enthusiast</span>
                  </div>
                </div>
                <div class="pt-4 border-t border-gray-100 flex justify-between items-center mt-4">
                  <span class="font-bold text-md text-gray-900 truncate max-w-[120px]">@Shakthi16</span>
                  <span class="bg-gray-900 text-white text-[11px] font-bold px-4 py-2 rounded-lg hover:bg-gray-800 transition-colors inline-block">View Profile</span>
                </div>
            </a>
        </div>

        <!-- Element 6: Shavira Studio Card (Bottom Right) -->
        <div class="w-full flex flex-col md:flex-row justify-between items-center mt-32 px-4 md:px-12 timeline-node" id="node-6">
           <div class="max-w-md text-center md:text-left mb-12 md:mb-0">
             <h2 class="text-3xl font-bold text-gray-900 mb-4 tracking-tight">Crafting bespoke digital products.</h2>
             <p class="text-gray-500 font-medium text-sm leading-relaxed mb-2">Delivering design and code collaborations under the studio banner SHAVIRA.</p>
             <p class="text-gray-500 font-medium text-sm leading-relaxed">Creating high-performance full-stack web applications with robust security.</p>
           </div>
           
           <a href="https://www.instagram.com/shaviraworks" target="_blank" class="w-full max-w-[350px] bg-white rounded-[2rem] p-6 shadow-xl flex flex-col justify-between h-[300px] text-black transform transition-transform hover:-translate-y-2 border border-gray-100 block">
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
                  <p class="text-xs text-gray-400 font-medium mb-3">Creative Freelance &amp; Design</p>
                  <p class="text-[11px] text-gray-500 leading-snug">Designing premium web interfaces, visual brand systems, and secure applications.<br/>Available for contract collaborations.</p>
                </div>
                <div class="pt-4 border-t border-gray-100 flex justify-between items-center mt-4">
                  <span class="font-bold text-md text-gray-900 truncate max-w-[120px]">@shavira.studio</span>
                  <span class="bg-gray-900 text-white text-[11px] font-bold px-4 py-2 rounded-lg hover:bg-gray-800 transition-colors inline-block">Follow</span>
                </div>
           </a>
        </div>

      </div>
    </section>
"""

# Replace in html
pattern = re.compile(start_marker + r'.*?' + end_marker, re.DOTALL)
html = pattern.sub(new_about_section + '\n    ' + end_marker, html)

# Add custom css for the spin animation if it doesn't exist
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
print("Updated HTML structure for Timeline!")
