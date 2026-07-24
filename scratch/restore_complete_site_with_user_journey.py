with open('git_version.html', 'r', encoding='utf-8') as f:
    git_text = f.read()

# Original Professional Journey section content
JOURNEY_HTML = """<!-- ==================== PROFESSIONAL JOURNEY ==================== -->
<section class="relative bg-[#FAFAFA] text-[#1F1F1F] overflow-hidden py-24 border-t border-b border-gray-200/60" id="timeline-pin-section">
  
  <div class="max-w-7xl mx-auto px-6 mb-12 flex flex-col md:flex-row justify-between items-start md:items-end">
    <div>
      <span class="text-xs uppercase tracking-[0.2em] text-[#8b2252] font-mono font-bold block mb-2">EXPERIENCE &amp; RESEARCH</span>
      <h2 class="text-4xl md:text-6xl font-bold font-sans tracking-tight text-[#1F1F1F]">Professional Journey</h2>
    </div>
    <p class="text-sm text-gray-500 font-medium max-w-md mt-4 md:mt-0">
      Offensive security research, full-stack development, and workflow automation. Scroll horizontally to view milestones.
    </p>
  </div>

  <!-- Horizontal Scroll Track -->
  <div class="relative w-full overflow-hidden" id="timeline-scroll-wrapper" style="min-height: 480px;">
    
    <!-- Year Digits Watermark Background -->
    <div class="absolute inset-0 pointer-events-none flex items-center justify-between opacity-[0.06] select-none z-0 px-12" style="font-family: 'Outfit', sans-serif; font-size: 240px; font-weight: 900; color: #1F1F1F; letter-spacing: -0.05em;">
      <span class="year-digit-1">2025</span>
      <span class="year-digit-2">2026</span>
    </div>

    <!-- Cards Container -->
    <div class="flex gap-12 px-6 md:px-20 py-6 w-max relative z-10 transition-transform duration-300" id="timeline-scroll-content">
      
      <!-- CARD 1: IIT Madras CYSTAR Lab -->
      <div class="timeline-scroll-item flex flex-col md:flex-row items-center gap-8 bg-white/90 backdrop-blur-xl rounded-[36px] p-6 md:p-8 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.08)] border border-gray-200/80 w-[90vw] md:w-[720px] shrink-0">
        <div class="relative w-full md:w-[300px] h-[220px] rounded-[28px] overflow-hidden shrink-0 shadow-md">
          <img src="bg1.png" alt="IIT Madras CYSTAR Lab" class="w-full h-full object-cover"/>
          <div class="absolute bottom-4 left-4 bg-black/80 backdrop-blur-md text-white font-mono text-[10px] font-bold uppercase tracking-wider px-3.5 py-1.5 rounded-full border border-white/20">
            AUG 2025 - PRESENT
          </div>
        </div>
        <div class="flex flex-col justify-center text-left">
          <span class="text-[11px] font-mono uppercase tracking-[0.2em] text-[#8b2252] font-bold mb-2">CYBERSECURITY RESEARCH INTERN</span>
          <h3 class="text-2xl md:text-3xl font-bold text-[#1F1F1F] mb-3 leading-tight">IIT Madras — CYSTAR Lab</h3>
          <p class="text-xs md:text-sm text-gray-600 leading-relaxed font-medium">
            Conducting offensive security research workflows including vulnerability exposure analysis, studying AV/EDR evasion techniques, implementing explainable security models, and producing thorough technical documentation.
          </p>
        </div>
      </div>

      <!-- CARD 2: OpsIntellix -->
      <div class="timeline-scroll-item flex flex-col md:flex-row items-center gap-8 bg-white/90 backdrop-blur-xl rounded-[36px] p-6 md:p-8 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.08)] border border-gray-200/80 w-[90vw] md:w-[720px] shrink-0">
        <div class="relative w-full md:w-[300px] h-[220px] rounded-[28px] overflow-hidden shrink-0 shadow-md">
          <img src="opsintellix.png" alt="OpsIntellix" class="w-full h-full object-cover"/>
          <div class="absolute bottom-4 left-4 bg-black/80 backdrop-blur-md text-white font-mono text-[10px] font-bold uppercase tracking-wider px-3.5 py-1.5 rounded-full border border-white/20">
            NOV 2025 - FEB 2026
          </div>
        </div>
        <div class="flex flex-col justify-center text-left">
          <span class="text-[11px] font-mono uppercase tracking-[0.2em] text-[#8b2252] font-bold mb-2">OPERATIONS INTERN — AP AUTOMATION</span>
          <h3 class="text-2xl md:text-3xl font-bold text-[#1F1F1F] mb-3 leading-tight">OpsIntellix</h3>
          <p class="text-xs md:text-sm text-gray-600 leading-relaxed font-medium">
            Automated banking workflows, invoice processing pipelines, document classification, and validation using Python, driving processing efficiency up by 30%.
          </p>
        </div>
      </div>

      <!-- CARD 3: Focuslogic IT Services -->
      <div class="timeline-scroll-item flex flex-col md:flex-row items-center gap-8 bg-white/90 backdrop-blur-xl rounded-[36px] p-6 md:p-8 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.08)] border border-gray-200/80 w-[90vw] md:w-[720px] shrink-0">
        <div class="relative w-full md:w-[300px] h-[220px] rounded-[28px] overflow-hidden shrink-0 shadow-md">
          <img src="write.png" alt="Focuslogic IT Services" class="w-full h-full object-cover"/>
          <div class="absolute bottom-4 left-4 bg-black/80 backdrop-blur-md text-white font-mono text-[10px] font-bold uppercase tracking-wider px-3.5 py-1.5 rounded-full border border-white/20">
            MAR 2025 - MAY 2025
          </div>
        </div>
        <div class="flex flex-col justify-center text-left">
          <span class="text-[11px] font-mono uppercase tracking-[0.2em] text-[#8b2252] font-bold mb-2">WEB DEVELOPMENT INTERN</span>
          <h3 class="text-2xl md:text-3xl font-bold text-[#1F1F1F] mb-3 leading-tight">Focuslogic IT Services</h3>
          <p class="text-xs md:text-sm text-gray-600 leading-relaxed font-medium">
            Built responsive React.js frontends from Figma designs, integrated REST APIs, conducted manual UI testing, and reduced load latency by 25%.
          </p>
        </div>
      </div>

    </div>
  </div>
</section>
"""

# Insert JOURNEY_HTML right after section id="about"
about_pos = git_text.find('id="about"')
about_end = git_text.find('</section>', about_pos) + len('</section>')

final_html = git_text[:about_end] + '\n\n' + JOURNEY_HTML + '\n\n' + git_text[about_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Successfully restored complete index.html with user's original Professional Journey format and all intact sections!")
