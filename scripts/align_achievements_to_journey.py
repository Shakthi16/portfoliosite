import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the HTML for #achievements section to match Professional Journey track spacing
OLD_ACH_SECTION = re.search(r'<!-- ACHIEVEMENTS -->.*?</section>', content, re.DOTALL).group(0)

NEW_ACH_SECTION = """<!-- ACHIEVEMENTS -->
<section id="achievements" class="relative w-full bg-[#FAF8F5]" style="height: 100vh; display: flex; flex-direction: column; justify-content: flex-start; z-index: 20; padding: 40px 0 0 0; border-top: 1px solid rgba(66,24,53,0.1);">
  <div class="max-w-7xl mx-auto px-6 w-full flex-shrink-0" style="margin-bottom: 20px;">
    <div class="flex flex-col md:flex-row justify-between items-start md:items-end mb-6 md:mb-12 gs-reveal gap-3 md:gap-4">
      <div>
        <p class="text-xs uppercase tracking-[0.2em] text-purple-400 font-bold mb-2 font-sans">My Milestones</p>
        <h2 class="text-5xl md:text-7xl font-bold brand text-[#1f1f1f]">Achievements</h2>
      </div>
      <p class="text-sm text-[#555] max-w-sm">
        A showcase of academic honors, research papers, patents, and hackathon victories. Click any card to view details.
      </p>
    </div>
  </div>

  <!-- Horizontal Scroll Wrapper (matching Professional Journey feel) -->
  <div id="horizontal-ach-scroll" class="w-full flex-grow flex items-center" style="position: relative; overflow: hidden;">
    <div class="ach-carousel relative z-10" id="ach-carousel" style="display: flex; gap: 220px; padding-left: 6vw; padding-right: 15vw; min-width: max-content; align-items: center; height: 100%; position: relative;">
      
      <!-- Card 1: Research -->
      <div class="ach-card relative flex flex-col justify-between p-10 shadow-2xl flex-shrink-0" data-index="0" style="width: 560px; max-width: 80vw; height: 370px; flex-shrink: 0; border-radius: 2.5rem; background: linear-gradient(135deg, #1e1b4b 0%, #1e293b 100%); border: 1px solid rgba(255,255,255,0.1); position: relative; overflow: visible;">
        <!-- Character PNG pop-out -->
        <div class="absolute inset-x-0 top-0 bottom-0 flex justify-center items-start pointer-events-none -top-20 z-20">
          <img alt="Research Character" class="object-contain" onerror="this.style.display='none'" src="research.png" style="height:clamp(160px,32vh,320px)"/>
        </div>
        <!-- Card content base background gradient container -->
        <div class="absolute inset-x-0 bottom-0 h-[60%] rounded-[2.5rem] bg-gradient-to-t from-black/90 via-black/50 to-transparent z-0 pointer-events-none"></div>
        <div class="relative z-10 text-center pointer-events-none flex flex-col items-center justify-end h-full w-full pb-2">
          <p class="text-xs font-sans uppercase tracking-[0.2em] text-pink-400 font-bold mb-2">Research</p>
          <h3 class="text-3xl md:text-4xl font-bold text-white mb-2 leading-tight">Published Researcher</h3>
          <p class="text-sm text-white/70 font-medium">ICTACA'26 Conference Paper</p>
        </div>
      </div>

      <!-- Card 2: Patent -->
      <div class="ach-card relative flex flex-col justify-between p-10 shadow-2xl flex-shrink-0" data-index="1" style="width: 560px; max-width: 80vw; height: 370px; flex-shrink: 0; border-radius: 2.5rem; background: linear-gradient(135deg, #3b0764 0%, #1e1b4b 100%); border: 1px solid rgba(255,255,255,0.1); position: relative; overflow: visible;">
        <!-- Character PNG pop-out -->
        <div class="absolute inset-x-0 top-0 bottom-0 flex justify-center items-start pointer-events-none -top-20 z-20">
          <img alt="Patent Character" class="object-contain" onerror="this.style.display='none'" src="patent.png" style="height:clamp(160px,32vh,320px)"/>
        </div>
        <!-- Card content base background gradient container -->
        <div class="absolute inset-x-0 bottom-0 h-[60%] rounded-[2.5rem] bg-gradient-to-t from-black/90 via-black/50 to-transparent z-0 pointer-events-none"></div>
        <div class="relative z-10 text-center pointer-events-none flex flex-col items-center justify-end h-full w-full pb-2">
          <p class="text-xs font-sans uppercase tracking-[0.2em] text-pink-400 font-bold mb-2">Intellectual Property</p>
          <h3 class="text-3xl md:text-4xl font-bold text-white mb-2 leading-tight">Patent Filed</h3>
          <p class="text-sm text-white/70 font-medium">Nanosafe Cloak System</p>
        </div>
      </div>

      <!-- Card 3: Hackathon -->
      <div class="ach-card relative flex flex-col justify-between p-10 shadow-2xl flex-shrink-0" data-index="2" style="width: 560px; max-width: 80vw; height: 370px; flex-shrink: 0; border-radius: 2.5rem; background: linear-gradient(135deg, #064e3b 0%, #0c4a6e 100%); border: 1px solid rgba(255,255,255,0.1); position: relative; overflow: visible;">
        <!-- Character PNG pop-out -->
        <div class="absolute inset-x-0 top-0 bottom-0 flex justify-center items-start pointer-events-none -top-20 z-20">
          <img alt="Hackathon Character" class="object-contain" onerror="this.style.display='none'" src="hackathon.png" style="height:clamp(160px,32vh,320px)"/>
        </div>
        <!-- Card content base background gradient container -->
        <div class="absolute inset-x-0 bottom-0 h-[60%] rounded-[2.5rem] bg-gradient-to-t from-black/90 via-black/50 to-transparent z-0 pointer-events-none"></div>
        <div class="relative z-10 text-center pointer-events-none flex flex-col items-center justify-end h-full w-full pb-2">
          <p class="text-xs font-sans uppercase tracking-[0.2em] text-pink-400 font-bold mb-2">Competition</p>
          <h3 class="text-3xl md:text-4xl font-bold text-white mb-2 leading-tight">Hackathon Winner</h3>
          <p class="text-sm text-white/70 font-medium">3rd Place Vibeaithon</p>
        </div>
      </div>

      <!-- Card 4: Outgoing Student -->
      <div class="ach-card relative flex flex-col justify-between p-10 shadow-2xl flex-shrink-0" data-index="3" style="width: 560px; max-width: 80vw; height: 370px; flex-shrink: 0; border-radius: 2.5rem; background: linear-gradient(135deg, #7c2d12 0%, #451a03 100%); border: 1px solid rgba(255,255,255,0.1); position: relative; overflow: visible;">
        <!-- Character PNG pop-out -->
        <div class="absolute inset-x-0 top-0 bottom-0 flex justify-center items-start pointer-events-none -top-20 z-20">
          <img alt="Outgoing Student Character" class="object-contain" onerror="this.style.display='none'" src="beststudent.png" style="height:clamp(160px,32vh,320px)"/>
        </div>
        <!-- Card content base background gradient container -->
        <div class="absolute inset-x-0 bottom-0 h-[60%] rounded-[2.5rem] bg-gradient-to-t from-black/90 via-black/50 to-transparent z-0 pointer-events-none"></div>
        <div class="relative z-10 text-center pointer-events-none flex flex-col items-center justify-end h-full w-full pb-2">
          <p class="text-xs font-sans uppercase tracking-[0.2em] text-pink-400 font-bold mb-2">Academic Excellence</p>
          <h3 class="text-3xl md:text-4xl font-bold text-white mb-2 leading-tight">Best Outgoing Student</h3>
          <p class="text-sm text-white/70 font-medium">Kingston Engineering College</p>
        </div>
      </div>

    </div>
  </div>
</section>"""

content = content.replace(OLD_ACH_SECTION, NEW_ACH_SECTION)

# Replace the GSAP achievements script
OLD_ACH_JS_PATTERN = r'const achSection = document\.getElementById\(\'achievements\'\);.*?pinAchTimeline\.to\(achCarousel, \{\n\s+x: \(\) => -getAchScrollAmount\(\),\n\s+ease: "none"\n\s+\}, 0\);\n\s+\}'

NEW_ACH_JS = """const achSection = document.getElementById('achievements');
          const achCarousel = document.getElementById('ach-carousel');
          if (achSection && achCarousel) {
            const getAchScrollAmount = () => {
              return achCarousel.scrollWidth - window.innerWidth;
            };
            
            pinAchTimeline = gsap.timeline({
              scrollTrigger: {
                trigger: achSection,
                start: "top top",
                end: () => "+=" + (getAchScrollAmount() * 1.6),
                pin: true,
                scrub: 1,
                invalidateOnRefresh: true
              }
            });

            pinAchTimeline.to(achCarousel, {
              x: () => -getAchScrollAmount(),
              ease: "none"
            }, 0);

            // Container-animated scaling per card like Professional Journey items
            const cards = achSection.querySelectorAll('.ach-card');
            cards.forEach((card) => {
              gsap.fromTo(card, 
                { scale: 0.88, opacity: 0.6 },
                { 
                  scale: 1, 
                  opacity: 1, 
                  ease: "none", 
                  scrollTrigger: { 
                    trigger: card, 
                    containerAnimation: pinAchTimeline.scrollTrigger, 
                    start: "left 85%", 
                    end: "center center", 
                    scrub: true 
                  }
                }
              );
            });
          }"""

content = re.sub(OLD_ACH_JS_PATTERN, NEW_ACH_JS, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated Achievements layout and GSAP containerAnimation.")
