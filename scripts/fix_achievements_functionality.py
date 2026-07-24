import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix containerAnimation syntax: pass pinTimeline / pinAchTimeline (the timeline instances) directly instead of .scrollTrigger

OLD_SCRIPT_SECTION = re.search(r'// ─── Horizontal Scroll Pinning ScrollTrigger \(Timeline\) ───.*?// Recalculate ScrollTrigger positions', content, re.DOTALL).group(0)

NEW_SCRIPT_SECTION = """// ─── Horizontal Scroll Pinning ScrollTrigger (Timeline) ───
          const pinSection = document.getElementById('timeline-pin-section');
          const scrollContent = document.getElementById('timeline-scroll-content');
          
          if (pinSection && scrollContent) {
            const getScrollAmount = () => {
              return scrollContent.scrollWidth - window.innerWidth;
            };
            
            pinTimeline = gsap.timeline({
              scrollTrigger: {
                trigger: pinSection,
                start: "top top",
                end: () => "+=" + (getScrollAmount() * 1.8),
                pin: true,
                scrub: 1,
                invalidateOnRefresh: true
              }
            });

            pinTimeline.to(scrollContent, {
              x: () => -getScrollAmount(),
              ease: "none"
            }, 0);

            pinTimeline.to('.timeline-year-bg', {
              x: 120,
              ease: "none"
            }, 0);

            const items = document.querySelectorAll('.timeline-scroll-item');
            items.forEach((item) => {
              const circle = item.querySelector('.timeline-circle');
              const date   = item.querySelector('.timeline-date');
              const role   = item.querySelector('.timeline-role');
              const title  = item.querySelector('.timeline-title');
              const desc   = item.querySelector('.timeline-desc');
              const digit1 = item.querySelector('.year-digit-1');
              const digit2 = item.querySelector('.year-digit-2');
              const digit3 = item.querySelector('.year-digit-3');
              const digit4 = item.querySelector('.year-digit-4');

              if (digit1 && digit2 && digit3 && digit4) {
                gsap.fromTo(digit1, { y: -50 }, { y: 50, ease: "none", scrollTrigger: { trigger: item, containerAnimation: pinTimeline, start: "left right", end: "right left", scrub: true }});
                gsap.fromTo(digit2, { y: -20 }, { y: 20, ease: "none", scrollTrigger: { trigger: item, containerAnimation: pinTimeline, start: "left right", end: "right left", scrub: true }});
                gsap.fromTo(digit3, { y: 20 },  { y: -20, ease: "none", scrollTrigger: { trigger: item, containerAnimation: pinTimeline, start: "left right", end: "right left", scrub: true }});
                gsap.fromTo(digit4, { y: 50 },  { y: -50, ease: "none", scrollTrigger: { trigger: item, containerAnimation: pinTimeline, start: "left right", end: "right left", scrub: true }});
              }

              if (circle) gsap.fromTo(circle, { scale: 0.85, rotation: -6, opacity: 0.4 }, { scale: 1, rotation: 0, opacity: 1, scrollTrigger: { trigger: item, containerAnimation: pinTimeline, start: "left 85%", end: "center center", scrub: true }});

              gsap.fromTo([date, role, title, desc], { y: 35, opacity: 0 }, { y: 0, opacity: 1, stagger: 0.08, scrollTrigger: { trigger: item, containerAnimation: pinTimeline, start: "left 80%", end: "center center", scrub: true }});
            });
          }

          // ─── Achievements Horizontal scroll panel pinning ───
          const achSection = document.getElementById('achievements');
          const achCarousel = document.getElementById('ach-carousel');
          if (achSection && achCarousel) {
            const getAchScrollAmount = () => {
              return achCarousel.scrollWidth - window.innerWidth;
            };
            
            pinAchTimeline = gsap.timeline({
              scrollTrigger: {
                trigger: achSection,
                start: "top top",
                end: () => "+=" + (getAchScrollAmount() * 1.8),
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
                    containerAnimation: pinAchTimeline, 
                    start: "left 85%", 
                    end: "center center", 
                    scrub: true 
                  }
                }
              );
            });
          }

          // Recalculate ScrollTrigger positions"""

content = content.replace(OLD_SCRIPT_SECTION, NEW_SCRIPT_SECTION)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully fixed containerAnimation syntax error in GSAP timeline.")
