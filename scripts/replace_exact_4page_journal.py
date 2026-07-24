with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

EXACT_JOURNAL_HTML = """<!-- ABOUT ME: EXACT SPECIFICATION 4-PAGE JOURNAL BOOK -->
<section class="relative bg-[#f4efe6] text-[#1F1F1F] py-24 overflow-hidden border-b border-amber-900/10 z-20" id="about-journal">
  <div class="max-w-6xl mx-auto px-4 md:px-8 text-center">
    
    <!-- Title Header -->
    <div class="mb-8">
      <span class="text-[11px] uppercase tracking-[0.3em] text-[#8b2252] font-mono font-bold block mb-1">ABOUT ME</span>
      <h2 class="text-4xl md:text-5xl font-bold font-serif italic text-[#1F1F1F]">The Personal Journal</h2>
    </div>

    <!-- BOOK STAGE CONTAINER (3D Perspective) -->
    <div class="relative w-full max-w-[980px] mx-auto min-h-[620px] flex items-center justify-center perspective-1000">

      <!-- ==================== VIEW 1: CLOSED COVER (COVER.PNG) ==================== -->
      <div id="jbook-cover" class="cursor-pointer transition-all duration-700 ease-out transform scale-100 opacity-100 flex flex-col items-center z-30" onclick="flipJournalBook('spread1')">
        <div class="relative group">
          <!-- Journal Cover Book Image -->
          <div class="w-[320px] md:w-[420px] h-[540px] rounded-[28px] shadow-[0_30px_70px_-15px_rgba(0,0,0,0.3)] overflow-hidden relative bg-[#36132b] border border-amber-900/30 transition-transform duration-500 hover:scale-[1.02] hover:-rotate-1">
            <img src="cover.png" alt="Shakthi Sri Journal Cover" class="w-full h-full object-cover"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/40 via-transparent to-transparent pointer-events-none"></div>
          </div>

          <!-- Hanging Ribbon Bookmark -->
          <div class="absolute -bottom-6 left-12 w-6 h-12 bg-[#8b2252] rounded-b-md shadow-md pointer-events-none"></div>
        </div>
      </div>

      <!-- ==================== VIEW 2: OPENED SPREAD 1 (PAGES 1 & 2 - MATCHING IMAGE 1 EXACTLY) ==================== -->
      <div id="jbook-spread1" class="hidden transition-all duration-700 ease-out transform opacity-0 scale-95 w-full z-30">
        
        <div class="w-full bg-[#faf6ee] rounded-[32px] shadow-[0_30px_80px_-20px_rgba(0,0,0,0.22)] border border-amber-900/15 p-6 md:p-10 relative overflow-hidden text-left" style="background-image: radial-gradient(#d6cebe 1px, transparent 1px); background-size: 20px 20px;">
          
          <!-- CORNER PAGE FLIP TAB (TOP-RIGHT DOG-EAR TO PAGE 3-4) -->
          <div onclick="flipJournalBook('spread2')" class="absolute top-0 right-0 w-16 h-16 cursor-pointer group z-40" title="Next: Page 3-4">
            <div class="w-full h-full bg-[#ebdcc4] border-b border-l border-amber-900/20 rounded-bl-2xl shadow-md transition-transform duration-300 group-hover:scale-110 flex items-center justify-center">
              <span class="text-xs font-mono font-bold text-[#8b2252] pl-2 pb-2">p.3-4 →</span>
            </div>
          </div>

          <!-- CLOSE BOOK RIBBON (TOP-LEFT) -->
          <div onclick="flipJournalBook('cover')" class="absolute top-0 left-6 cursor-pointer group z-40" title="Close Journal">
            <div class="bg-[#421835] text-white text-[10px] font-mono font-bold px-3 py-2.5 rounded-b-lg shadow-md transition-transform group-hover:translate-y-1">
              ✕ Close
            </div>
          </div>

          <!-- Center Book Spine -->
          <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[2px] bg-amber-900/15 hidden md:block"></div>
          <div class="absolute bottom-0 left-1/2 -translate-x-1/2 w-6 h-8 bg-[#8b2252] rounded-t-sm shadow-md hidden md:block"></div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 relative z-10 pt-2">
            
            <!-- PAGE 1: LEFT SIDE (MATCHING IMAGE 1 EXACTLY) -->
            <div class="flex flex-col justify-between text-left pr-0 md:pr-4">
              <div>
                <h3 class="text-4xl md:text-5xl font-bold font-serif text-[#1F1F1F] mb-3 tracking-tight">Shakthi Sri</h3>
                
                <!-- Pill Badges -->
                <div class="flex flex-wrap items-center gap-3 mb-6">
                  <span class="px-3.5 py-1 bg-[#f0e3db] text-[#8b2252] text-[11px] font-mono font-bold rounded-full border border-[#d8c2b5] tracking-wider uppercase">DEVELOPER &amp; RESEARCHER</span>
                  <span class="font-serif italic text-sm text-gray-600 underline decoration-amber-900/30">class of 2026</span>
                </div>

                <!-- Achievements List -->
                <div class="space-y-3 font-mono text-xs text-gray-700 font-medium mb-6">
                  <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-2">
                    <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">💻 B.Tech Information Technology</span>
                    <span class="text-gray-500">2022 - 2026</span>
                  </div>
                  <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-2">
                    <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">🎓 Kingston Engineering College</span>
                    <span class="text-[#8b2252] font-bold">CGPA: 8.6</span>
                  </div>
                  <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-2">
                    <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">🧪 IIT Madras — CYSTAR</span>
                    <span class="text-gray-500">Research Intern</span>
                  </div>
                  <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-2">
                    <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">&lt;/&gt; Full-Stack Developer</span>
                    <span class="text-gray-500">MERN Stack</span>
                  </div>
                  <div class="flex justify-between items-center border-b border-dashed border-amber-900/15 pb-2">
                    <span class="flex items-center gap-2 font-bold text-[#1F1F1F]">🛡️ Cybersecurity Enthusiast</span>
                    <span class="text-gray-500">Always Learning</span>
                  </div>
                </div>

                <!-- Taped Cards Row -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6">
                  <!-- Taped About Me Note -->
                  <div class="bg-[#f7f0e6] p-4 rounded-2xl border border-amber-900/15 shadow-sm relative">
                    <div class="absolute -top-3 left-1/2 -translate-x-1/2 w-10 h-4 bg-amber-200/80 rotate-[-2deg] border-l border-r border-white/60"></div>
                    <span class="font-serif italic text-xs text-[#8b2252] font-bold block mb-2">about me ✏️</span>
                    <ul class="text-[11px] text-gray-700 leading-relaxed font-sans space-y-1.5">
                      <li>♥ I love turning ideas into impactful digital solutions.</li>
                      <li>♥ Curious mind with a strong drive to build, secure &amp; innovate.</li>
                      <li>♥ Believer in discipline, consistency &amp; growth.</li>
                    </ul>
                  </div>

                  <!-- Today Widget Note -->
                  <div class="bg-[#f7f0e6] p-4 rounded-2xl border border-amber-900/15 shadow-sm relative">
                    <div class="flex items-center gap-1 mb-2">
                      <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                      <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                      <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                      <span class="text-[9px] font-mono text-gray-400 ml-1 uppercase">TODAY</span>
                      <span class="ml-auto text-xs text-amber-800">★</span>
                    </div>
                    <p class="text-[11px] text-gray-700 font-sans leading-relaxed">
                      Building skills.<br/>Solving problems.<br/>Creating solutions.<br/>Preparing for impact.<br/>One step at a time.
                    </p>
                  </div>
                </div>
              </div>

              <!-- Contact Memo & Quote -->
              <div class="pt-4 border-t border-dashed border-amber-900/20 flex flex-col sm:flex-row justify-between items-start sm:items-end gap-3">
                <div class="bg-[#f0e8dc] p-3 rounded-xl text-[11px] font-mono text-gray-800 border border-amber-900/15">
                  <p class="font-bold">srishakthi799@gmail.com</p>
                  <p class="text-gray-600">+91 7895032098</p>
                  <p class="text-gray-500">Chennai | Vellore</p>
                </div>
                <div class="text-right">
                  <span class="text-2xl text-[#8b2252] font-serif leading-none block">“</span>
                  <p class="font-serif italic text-xs text-[#421835] font-semibold">code with purpose,<br/>create with impact.</p>
                </div>
              </div>

            </div>

            <!-- PAGE 2: RIGHT SIDE (MATCHING IMAGE 1 EXACTLY) -->
            <div class="flex flex-col justify-between relative text-left pl-0 md:pl-2">
              
              <!-- Top Icons Row -->
              <div class="flex justify-between items-start mb-4">
                <div class="text-center">
                  <span class="text-2xl">🌸</span>
                  <span class="block text-[9px] font-mono text-gray-400 mt-1">breathe.png</span>
                </div>
                <div class="flex items-center gap-6">
                  <div class="text-center">
                    <div class="w-8 h-8 bg-[#8b2252]/10 rounded-lg flex items-center justify-center text-[#8b2252] text-sm font-bold mx-auto">📁</div>
                    <span class="block text-[9px] font-mono text-gray-500 mt-1">Goals</span>
                  </div>
                  <div class="text-center">
                    <div class="w-8 h-8 bg-amber-900/10 rounded-lg flex items-center justify-center text-amber-900 text-sm font-bold mx-auto">💾</div>
                    <span class="block text-[9px] font-mono text-gray-500 mt-1">Reminders</span>
                  </div>
                </div>
              </div>

              <!-- Main Photo & Currently Card Row -->
              <div class="grid grid-cols-1 sm:grid-cols-12 gap-6 items-center mb-6">
                <!-- Currently Box -->
                <div class="sm:col-span-6 border border-dashed border-amber-900/30 rounded-2xl p-4 bg-[#fbf7f0]">
                  <span class="font-serif italic text-xs text-[#8b2252] font-bold block mb-2">currently ✏️</span>
                  <ul class="text-[11px] text-gray-700 leading-relaxed font-sans space-y-1.5">
                    <li>♥ Exploring AI &amp; LLMs</li>
                    <li>♥ Building secure systems</li>
                    <li>♥ Deepening full-stack</li>
                    <li>♥ Learning. Shipping.</li>
                    <li>♥ Growing. Always.</li>
                  </ul>
                </div>

                <!-- Centered Photo -->
                <div class="sm:col-span-6 flex justify-center relative">
                  <div class="relative group">
                    <div class="w-[170px] h-[210px] rounded-[22px] overflow-hidden shadow-xl border-4 border-white transform rotate-[1.5deg] transition-transform duration-500 group-hover:rotate-0">
                      <img src="me.png" alt="Shakthi Sri" class="w-full h-full object-cover"/>
                    </div>
                    <div class="absolute -top-3 right-0 bg-black/80 text-white font-mono text-[9px] font-bold px-3 py-1 rounded-full shadow-md z-30">
                      @Shakthi.16
                    </div>
                  </div>
                </div>
              </div>

              <!-- Tech I Work With Box -->
              <div class="border border-dashed border-amber-900/30 rounded-2xl p-4 bg-[#fbf7f0] mb-6">
                <span class="font-serif italic text-xs text-[#8b2252] font-bold block mb-3">tech i work with ✏️</span>
                <div class="flex flex-wrap items-center justify-between gap-3 text-center">
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-700 font-bold">⚛️ React.js</div>
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-700 font-bold">🟩 Node.js</div>
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-700 font-bold">⚙️ Express.js</div>
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-700 font-bold">🍃 MongoDB</div>
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-700 font-bold">🎨 Figma</div>
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-700 font-bold">💻 VS Code</div>
                  <div class="flex items-center gap-1.5 text-[11px] font-mono text-gray-700 font-bold">🐧 Linux</div>
                </div>
              </div>

              <!-- What I Build Box -->
              <div class="border border-dashed border-amber-900/30 rounded-2xl p-4 bg-[#fbf7f0]">
                <span class="font-serif italic text-xs text-[#8b2252] font-bold block mb-2 text-center">what i build ♡</span>
                <div class="grid grid-cols-3 gap-2 text-center text-[10px] font-mono text-gray-700 font-bold">
                  <div class="p-2 bg-white/70 rounded-xl border border-amber-900/10">🌐 Full-Stack Web Applications</div>
                  <div class="p-2 bg-white/70 rounded-xl border border-amber-900/10">🔒 Cybersecurity Tools &amp; Research</div>
                  <div class="p-2 bg-white/70 rounded-xl border border-amber-900/10">🧠 AI-Enhanced Solutions</div>
                </div>
              </div>

            </div>

          </div>

          <!-- Bottom Footer Nav -->
          <div class="mt-6 pt-3 border-t border-amber-900/10 flex justify-between items-center text-xs font-mono text-gray-500">
            <button onclick="flipJournalBook('cover')" class="hover:text-[#8b2252] font-bold cursor-pointer">← Cover</button>
            <span class="font-bold text-gray-400">Page 1-2 of 4</span>
            <button onclick="flipJournalBook('spread2')" class="hover:text-[#8b2252] font-bold cursor-pointer">Page 3-4 →</button>
          </div>

        </div>
      </div>

      <!-- ==================== VIEW 3: OPENED SPREAD 2 (PAGES 3 & 4 - EXACT CONTENT) ==================== -->
      <div id="jbook-spread2" class="hidden transition-all duration-700 ease-out transform opacity-0 scale-95 w-full z-30">
        
        <div class="w-full bg-[#faf6ee] rounded-[32px] shadow-[0_30px_80px_-20px_rgba(0,0,0,0.22)] border border-amber-900/15 p-6 md:p-10 relative overflow-hidden text-left" style="background-image: radial-gradient(#d6cebe 1px, transparent 1px); background-size: 20px 20px;">
          
          <!-- CORNER FLIP BACK TAB (TOP-RIGHT DOG-EAR TO PAGE 1-2) -->
          <div onclick="flipJournalBook('spread1')" class="absolute top-0 right-0 w-16 h-16 cursor-pointer group z-40" title="Back to Page 1-2">
            <div class="w-full h-full bg-[#ebdcc4] border-b border-l border-amber-900/20 rounded-bl-2xl shadow-md transition-transform duration-300 group-hover:scale-110 flex items-center justify-center">
              <span class="text-xs font-mono font-bold text-[#8b2252] pl-2 pb-2">← p.1-2</span>
            </div>
          </div>

          <!-- CLOSE BOOK RIBBON (TOP-LEFT) -->
          <div onclick="flipJournalBook('cover')" class="absolute top-0 left-6 cursor-pointer group z-40" title="Close Journal">
            <div class="bg-[#421835] text-white text-[10px] font-mono font-bold px-3 py-2.5 rounded-b-lg shadow-md transition-transform group-hover:translate-y-1">
              ✕ Close
            </div>
          </div>

          <!-- Center Book Spine -->
          <div class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 w-[2px] bg-amber-900/15 hidden md:block"></div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-10 md:gap-14 relative z-10 pt-2">
            
            <!-- PAGE 3: FIELD NOTES (EXACT TEXT FROM PROMPT) -->
            <div class="space-y-4 text-left">
              <div>
                <span class="text-[10px] font-mono uppercase tracking-[0.2em] text-[#8b2252] font-bold block mb-1">PAGE 3</span>
                <h3 class="text-2xl font-bold font-serif text-[#1F1F1F]">FIELD NOTES</h3>
                <p class="text-xs text-gray-500 font-medium italic">Observations collected while learning, building, and improving.</p>
              </div>

              <!-- ENTRY 01 -->
              <div class="p-3.5 rounded-2xl bg-white/80 border border-amber-900/10 space-y-1.5">
                <h4 class="font-bold text-xs text-[#421835] flex items-center gap-1.5">📍 ENTRY 01 — Engineering Begins With Understanding</h4>
                <p class="text-[11px] text-gray-600 leading-relaxed">
                  Every project introduces uncertainty. Before selecting technologies or writing the first line of code, I spend time understanding the problem from multiple perspectives. Good engineering rarely starts with implementation—it begins with observation.
                </p>
                <p class="text-[10px] font-serif italic text-amber-900 font-semibold pt-1">I believe the strongest solutions emerge when curiosity is allowed to lead before assumptions.</p>
              </div>

              <!-- ENTRY 02 -->
              <div class="p-3.5 rounded-2xl bg-white/80 border border-amber-900/10 space-y-1.5">
                <h4 class="font-bold text-xs text-[#421835] flex items-center gap-1.5">📍 ENTRY 02 — Simplicity Requires Discipline</h4>
                <p class="text-[11px] text-gray-600 leading-relaxed">
                  People often associate complexity with intelligence. In practice, simplicity demands significantly more thought. Removing unnecessary steps, reducing cognitive load, and making systems intuitive requires continuous refinement.
                </p>
                <div class="bg-amber-100/60 p-2 rounded-xl text-[10px] font-mono text-gray-700 italic border border-amber-900/10">
                  Notebook Margin: "Complexity is added naturally. Simplicity is engineered intentionally."
                </div>
              </div>

              <!-- ENTRY 03 & FLOW -->
              <div class="p-3.5 rounded-2xl bg-white/80 border border-amber-900/10 space-y-1.5">
                <h4 class="font-bold text-xs text-[#421835] flex items-center gap-1.5">📍 ENTRY 03 — Security Is an Architectural Decision</h4>
                <p class="text-[11px] text-gray-600 leading-relaxed">
                  Security cannot be postponed until deployment. Authentication, authorization, validation, monitoring, and privacy should exist from the first sketch—not the final sprint.
                </p>
                <div class="text-[10px] font-mono text-gray-600 font-bold text-center py-1 bg-amber-50 rounded-lg">
                  Observe ➔ Question ➔ Understand ➔ Design ➔ Build ➔ Improve
                </div>
              </div>

              <!-- Research Note & Footer -->
              <div class="pt-2 border-t border-dashed border-amber-900/20 text-[10px] font-mono text-gray-500">
                <p class="text-amber-900 font-bold mb-1">📌 Research Note:</p>
                <p class="italic text-gray-600">"Engineering is not about writing more code. It is about reducing unnecessary complexity while increasing reliability."</p>
                <p class="text-right font-serif italic text-[#8b2252] mt-1">"Every finished project becomes the starting point for a better question."</p>
              </div>

            </div>

            <!-- PAGE 4: ENGINEERING PRINCIPLES (EXACT TEXT FROM PROMPT) -->
            <div class="space-y-4 text-left">
              <div>
                <span class="text-[10px] font-mono uppercase tracking-[0.2em] text-[#8b2252] font-bold block mb-1">PAGE 4</span>
                <h3 class="text-2xl font-bold font-serif text-[#1F1F1F]">ENGINEERING PRINCIPLES</h3>
                <p class="text-xs text-gray-500 font-medium italic">Ideas that influence every project I choose to build.</p>
              </div>

              <div class="space-y-2 text-[11px] text-gray-700">
                
                <div class="p-2.5 rounded-xl bg-white/80 border border-amber-900/10">
                  <h4 class="font-bold text-xs text-[#421835]">Principle 01 — Build With Purpose</h4>
                  <p class="text-gray-600 leading-relaxed">Technology should create measurable value. Features should solve meaningful problems—not because they are technically impressive.</p>
                </div>

                <div class="p-2.5 rounded-xl bg-white/80 border border-amber-900/10">
                  <h4 class="font-bold text-xs text-[#421835]">Principle 02 — Learn Continuously</h4>
                  <p class="text-gray-600 leading-relaxed">Technology evolves faster than any curriculum. Remaining effective requires continuous learning, experimentation, and adaptation.</p>
                </div>

                <div class="p-2.5 rounded-xl bg-white/80 border border-amber-900/10">
                  <h4 class="font-bold text-xs text-[#421835]">Principle 03 — Design For Humans</h4>
                  <p class="text-gray-600 leading-relaxed">Behind every interface is a person trying to accomplish something. Thoughtful design reduces confusion, respects attention, and allows technology to become almost invisible.</p>
                </div>

                <div class="p-2.5 rounded-xl bg-white/80 border border-amber-900/10">
                  <h4 class="font-bold text-xs text-[#421835]">Principle 04 — Document Everything That Matters</h4>
                  <p class="text-gray-600 leading-relaxed">Knowledge becomes valuable only when it can be transferred. Clear documentation preserves context and supports collaboration.</p>
                </div>

                <div class="p-2.5 rounded-xl bg-white/80 border border-amber-900/10">
                  <h4 class="font-bold text-xs text-[#421835]">Principle 05 — Progress Through Iteration</h4>
                  <p class="text-gray-600 leading-relaxed">Perfection is rarely achieved in the first version. Meaningful improvement comes through observation, feedback, refinement, and repetition.</p>
                </div>

              </div>

              <!-- Notebook Reflection Box & Closing -->
              <div class="p-3 bg-[#f0e8dc] rounded-2xl border border-amber-900/15 text-[10px] font-mono text-gray-800 text-center font-bold">
                Knowledge + Curiosity + Discipline + Consistency = Professional Growth
              </div>

              <div class="pt-2 border-t border-dashed border-amber-900/20 flex justify-between items-center text-[10px] font-serif italic text-gray-600">
                <span>"Every system teaches. Every mistake documents."</span>
                <span class="font-bold text-[#8b2252]">"Technology changes rapidly. Principles endure."</span>
              </div>

            </div>

          </div>

          <!-- Bottom Footer Nav -->
          <div class="mt-6 pt-3 border-t border-amber-900/10 flex justify-between items-center text-xs font-mono text-gray-500">
            <button onclick="flipJournalBook('spread1')" class="hover:text-[#8b2252] font-bold cursor-pointer">← Page 1-2</button>
            <span class="font-bold text-gray-400">Page 3-4 of 4</span>
            <button onclick="flipJournalBook('cover')" class="hover:text-[#8b2252] font-bold cursor-pointer">Close Journal ➔</button>
          </div>

        </div>
      </div>

    </div>

  </div>
</section>

<!-- Smooth Page Flip Script -->
<script>
  function flipJournalBook(targetState) {
    const cover = document.getElementById('jbook-cover');
    const spread1 = document.getElementById('jbook-spread1');
    const spread2 = document.getElementById('jbook-spread2');

    const views = [cover, spread1, spread2];

    views.forEach(v => {
      if (v) {
        v.classList.add('hidden');
        v.classList.remove('opacity-100', 'scale-100');
        v.classList.add('opacity-0', 'scale-95');
      }
    });

    let targetView;
    if (targetState === 'cover') targetView = cover;
    else if (targetState === 'spread1') targetView = spread1;
    else if (targetState === 'spread2') targetView = spread2;

    if (targetView) {
      targetView.classList.remove('hidden');
      setTimeout(() => {
        targetView.classList.remove('opacity-0', 'scale-95');
        targetView.classList.add('opacity-100', 'scale-100');
      }, 40);
    }
  }
</script>"""

start_pos = content.find('<section class="relative bg-[#f4efe6]', content.find('id="about-journal"'))
if start_pos == -1:
    start_pos = content.find('id="about-journal"')
    start_pos = content.rfind('<section', 0, start_pos)

end_pos = content.find('<!-- ==================== 2. EDITORIAL CANVAS (#about) ==================== -->')
if end_pos == -1:
    end_pos = content.find('id="about"')
    end_pos = content.rfind('<section', 0, end_pos)

if start_pos != -1 and end_pos != -1:
    content = content[:start_pos] + EXACT_JOURNAL_HTML + '\n\n' + content[end_pos:]
    print("Successfully replaced journal section with exact 4-page specification!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
