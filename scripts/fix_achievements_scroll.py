import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update ach-carousel inline style to give generous right padding (14vw) so the 4th card scrolls fully into view
OLD_CAROUSEL_DIV = '<div class="ach-carousel relative z-10" id="ach-carousel" style="display: flex; gap: 50px; padding: 0 4vw; min-width: max-content; align-items: center; height: 100%; position: relative;">'
NEW_CAROUSEL_DIV = '<div class="ach-carousel relative z-10" id="ach-carousel" style="display: flex; gap: 40px; padding-left: 6vw; padding-right: 14vw; min-width: max-content; align-items: center; height: 100%; position: relative;">'

content = content.replace(OLD_CAROUSEL_DIV, NEW_CAROUSEL_DIV)

# 2. Add fixed width, height, flex-shrink-0, and rounded corners to each ach-card so they maintain clean dimensions
CARD_OLD_STYLE = 'style="background: linear-gradient(135deg,'
def fix_card_style(match):
    return 'style="width: 380px; max-width: 85vw; height: 350px; flex-shrink: 0; border-radius: 2rem; background: linear-gradient(135deg,'

content = re.sub(
    r'class="ach-card relative flex flex-col justify-center items-center p-8 shadow-2xl" data-index="(\d+)" style="background: linear-gradient\(135deg,',
    r'class="ach-card relative flex flex-col justify-center items-center p-8 shadow-2xl flex-shrink-0" data-index="\1" style="width: 380px; max-width: 85vw; height: 350px; flex-shrink: 0; border-radius: 2rem; background: linear-gradient(135deg,',
    content
)

# 3. Update JS ScrollTrigger for achievements pinning to ensure complete horizontal scroll to the right
OLD_ACH_JS = """          // ─── Achievements Horizontal scroll panel pinning ───
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
          }"""

NEW_ACH_JS = """          // ─── Achievements Horizontal scroll panel pinning ───
          const achSection = document.getElementById('achievements');
          const achCarousel = document.getElementById('ach-carousel');
          if (achSection && achCarousel) {
            const getAchScrollAmount = () => {
              // Add +80px buffer so the last card scrolls completely into view with margin
              return Math.max(0, (achCarousel.scrollWidth - window.innerWidth) + 80);
            };
            
            pinAchTimeline = gsap.timeline({
              scrollTrigger: {
                trigger: achSection,
                start: "top top",
                end: () => "+=" + (getAchScrollAmount() * 2.2),
                pin: true,
                scrub: 1,
                invalidateOnRefresh: true
              }
            });

            pinAchTimeline.to(achCarousel, {
              x: () => -getAchScrollAmount(),
              ease: "none"
            }, 0);
          }"""

content = content.replace(OLD_ACH_JS, NEW_ACH_JS)

# Also ensure window 'load' triggers a ScrollTrigger refresh so images loading late don't break horizontal scroll distance calculation
LOAD_REFRESH_JS = """          if (typeof ScrollTrigger !== 'undefined') {
            ScrollTrigger.refresh();
          }
          window.addEventListener('load', () => {
            if (typeof ScrollTrigger !== 'undefined') ScrollTrigger.refresh();
          });"""

content = content.replace(
    "if (typeof ScrollTrigger !== 'undefined') {\n            ScrollTrigger.refresh();\n          }",
    LOAD_REFRESH_JS
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated Achievements horizontal scroll logic and layout.")
