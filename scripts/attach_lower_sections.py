with open('git_version.html', 'r', encoding='utf-8') as f:
    git_lines = f.readlines()

# All lower sections HTML
LOWER_SECTIONS_HTML = """
<!-- ==================== 3. HORIZONTAL SCROLL PROFESSIONAL JOURNEY ==================== -->
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

<!-- ==================== 4. ACADEMIC BACKGROUND ==================== -->
<section class="py-20 bg-[#F5F5F7] text-[#1F1F1F] border-b border-gray-200/60" id="academic-background">
  <div class="max-w-7xl mx-auto px-6 lg:px-12">
    <div class="text-center mb-12">
      <span class="text-xs uppercase tracking-[0.2em] text-[#8b2252] font-mono font-bold block mb-2">EDUCATION</span>
      <h2 class="text-4xl md:text-6xl font-bold font-sans tracking-tight text-[#1F1F1F]">Academic Background</h2>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      
      <!-- B.Tech Card -->
      <div class="bg-white/90 backdrop-blur-xl rounded-[32px] p-8 border border-gray-200/80 shadow-[0_15px_40px_-15px_rgba(0,0,0,0.05)] hover:shadow-[0_25px_60px_-15px_rgba(66,24,53,0.1)] transition-all duration-500 hover:-translate-y-2 flex flex-col justify-between h-[240px]">
        <div>
          <span class="text-xs font-mono font-bold text-gray-400 uppercase tracking-widest block mb-2">2022 — 2026</span>
          <h3 class="text-2xl font-bold text-[#1F1F1F] mb-1">B.Tech in IT</h3>
          <p class="text-xs text-gray-500 font-medium">Kingston Eng. College</p>
        </div>
        <div class="pt-4 border-t border-gray-100 flex justify-between items-end">
          <span class="text-xs text-gray-400 font-bold uppercase tracking-wider">CGPA</span>
          <span class="text-4xl font-extrabold text-[#421835] tracking-tight">9.03</span>
        </div>
      </div>

      <!-- HSC Card -->
      <div class="bg-white/90 backdrop-blur-xl rounded-[32px] p-8 border border-gray-200/80 shadow-[0_15px_40px_-15px_rgba(0,0,0,0.05)] hover:shadow-[0_25px_60px_-15px_rgba(66,24,53,0.1)] transition-all duration-500 hover:-translate-y-2 flex flex-col justify-between h-[240px]">
        <div>
          <span class="text-xs font-mono font-bold text-gray-400 uppercase tracking-widest block mb-2">2021 — 2022</span>
          <h3 class="text-2xl font-bold text-[#1F1F1F] mb-1">HSC</h3>
          <p class="text-xs text-gray-500 font-medium">Sai Guruji School</p>
        </div>
        <div class="pt-4 border-t border-gray-100 flex justify-between items-end">
          <span class="text-xs text-gray-400 font-bold uppercase tracking-wider">SCORE</span>
          <span class="text-4xl font-extrabold text-[#421835] tracking-tight">89.2%</span>
        </div>
      </div>

      <!-- SSLC Card -->
      <div class="bg-white/90 backdrop-blur-xl rounded-[32px] p-8 border border-gray-200/80 shadow-[0_15px_40px_-15px_rgba(0,0,0,0.05)] hover:shadow-[0_25px_60px_-15px_rgba(66,24,53,0.1)] transition-all duration-500 hover:-translate-y-2 flex flex-col justify-between h-[240px]">
        <div>
          <span class="text-xs font-mono font-bold text-gray-400 uppercase tracking-widest block mb-2">2019 — 2020</span>
          <h3 class="text-2xl font-bold text-[#1F1F1F] mb-1">SSLC</h3>
          <p class="text-xs text-gray-500 font-medium">Sai Guruji School</p>
        </div>
        <div class="pt-4 border-t border-gray-100 flex justify-between items-end">
          <span class="text-xs text-gray-400 font-bold uppercase tracking-wider">SCORE</span>
          <span class="text-4xl font-extrabold text-[#421835] tracking-tight">92%</span>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- ==================== 5. LEARNING IN MOTION ==================== -->
<section class="py-28 bg-[#FAFAFA] text-[#1F1F1F] overflow-hidden relative border-b border-gray-200/60" id="learning-in-motion">
  
  <div class="max-w-4xl mx-auto text-center px-6 mb-16">
    <h2 class="text-5xl md:text-7xl font-extrabold font-sans tracking-tight text-[#1F1F1F] mb-4">Learning in Motion</h2>
    <div class="w-2.5 h-2.5 rounded-full bg-[#ec4899] mx-auto mb-6 shadow-sm"></div>
    <p class="text-sm md:text-base text-gray-600 font-medium leading-relaxed max-w-lg mx-auto">
      A mindset of curiosity. A habit of growth.<br/>Constantly exploring, building, and leveling up.
    </p>
  </div>

  <div class="relative w-[130vw] -ml-[15vw] space-y-6">
    
    <div class="bg-[#3d1830] text-white py-5 shadow-xl rotate-[-2deg] overflow-hidden flex items-center border-y border-white/10">
      <div class="marquee-track flex items-center gap-12 whitespace-nowrap animate-[marquee_25s_linear_infinite]">
        
        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">IN</span>
          <div class="text-left"><span class="font-bold text-sm block">Infosys</span><span class="text-[11px] text-pink-200/80">UI/UX, React, AI, Python</span></div>
        </div>

        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">UD</span>
          <div class="text-left"><span class="font-bold text-sm block">Udemy</span><span class="text-[11px] text-pink-200/80">Cybersecurity</span></div>
        </div>

        <div class="flex items-center gap-2 text-pink-300 font-mono text-xs font-bold px-4">
          <span class="text-lg">✦</span> 150+ Hours of Learning
        </div>

        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">GO</span>
          <div class="text-left"><span class="font-bold text-sm block">Google</span><span class="text-[11px] text-pink-200/80">Data Analytics &amp; Cloud</span></div>
        </div>

        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">NT</span>
          <div class="text-left"><span class="font-bold text-sm block">NoviTech</span><span class="text-[11px] text-pink-200/80">Full Stack Web Dev</span></div>
        </div>

        <span class="text-xl text-pink-300 px-2">→</span>

        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">IN</span>
          <div class="text-left"><span class="font-bold text-sm block">Infosys</span><span class="text-[11px] text-pink-200/80">UI/UX, React, AI, Python</span></div>
        </div>

        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">UD</span>
          <div class="text-left"><span class="font-bold text-sm block">Udemy</span><span class="text-[11px] text-pink-200/80">Cybersecurity</span></div>
        </div>

      </div>
    </div>

    <div class="bg-[#3d1830] text-white py-5 shadow-xl rotate-[-2deg] overflow-hidden flex items-center border-y border-white/10">
      <div class="marquee-track flex items-center gap-12 whitespace-nowrap animate-[marquee-reverse_30s_linear_infinite]">
        
        <span class="text-xl text-pink-300 px-2">→</span>

        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">GO</span>
          <div class="text-left"><span class="font-bold text-sm block">Google</span><span class="text-[11px] text-pink-200/80">Data Analytics &amp; Cloud</span></div>
        </div>

        <span class="text-lg text-pink-300">✦</span>

        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">IN</span>
          <div class="text-left"><span class="font-bold text-sm block">Infosys</span><span class="text-[11px] text-pink-200/80">UI/UX, React, AI, Python</span></div>
        </div>

        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">UD</span>
          <div class="text-left"><span class="font-bold text-sm block">Udemy</span><span class="text-[11px] text-pink-200/80">Cybersecurity</span></div>
        </div>

        <div class="text-pink-300 font-mono text-xs font-bold px-4">
          Always Exploring Always Evolving
        </div>

        <div class="flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center font-bold text-xs">GO</span>
          <div class="text-left"><span class="font-bold text-sm block">Google</span><span class="text-[11px] text-pink-200/80">Data Analytics &amp; Cloud</span></div>
        </div>

        <span class="text-xl text-pink-300 px-2">→</span>

      </div>
    </div>

  </div>
</section>
"""

# Extract skills, achievements, projects, contact from git_version
remaining_sections_html = ''.join(git_lines[4507:5900])

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert right after section id="about" closing tag
target_pos = content.find('</section>', content.find('id="about"'))
if target_pos != -1:
    end_idx = target_pos + len('</section>')
    content = content[:end_idx] + '\n\n' + LOWER_SECTIONS_HTML + '\n\n' + remaining_sections_html + content[end_idx:]
    print("Successfully attached all lower sections!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
