import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# -------------------------------------------------------------
# 1. UPDATE .contact-bg-text STYLING TO USE UNSPLASH GRADIENT LIQUID MASK
# -------------------------------------------------------------
old_css_pattern = r'\.contact-bg-text\s*\{[^}]*\}'
new_css = """.contact-bg-text {
      font-size: clamp(2.5rem, 11vw, 8.5rem);
      font-weight: 900;
      background-image: url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2000&auto=format&fit=crop');
      background-size: 160%;
      background-position: 50% 50%;
      -webkit-background-clip: text !important;
      -webkit-text-fill-color: transparent !important;
      background-clip: text !important;
      color: transparent !important;
      -webkit-text-stroke: 0px transparent !important;
      text-transform: uppercase;
      letter-spacing: -0.04em;
      line-height: 0.85;
      font-family: 'Outfit', sans-serif;
      transition: background-position 0.1s ease-out;
    }"""

content = re.sub(old_css_pattern, new_css, content, count=1)

# Ensure light mode uses clean visible background mask too
content = content.replace(
    'body.light-mode .contact-bg-text {\n      color: transparent;\n      -webkit-text-stroke: 1.5px rgba(0, 0, 0, 0.14);\n    }',
    'body.light-mode .contact-bg-text {\n      background-image: url(\'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2000&auto=format&fit=crop\') !important;\n      background-size: 160% !important;\n      -webkit-background-clip: text !important;\n      -webkit-text-fill-color: transparent !important;\n      -webkit-text-stroke: 0px transparent !important;\n    }'
)

# -------------------------------------------------------------
# 2. ADD MOUSEMOVE HOVER EFFECT TO #contact AND .contact-bg-text
# -------------------------------------------------------------
HOVER_SCRIPT = """
<!-- MOUSEMOVE HOVER EFFECT FOR CONTACT SHAKTHI SRI T S TEXT -->
<script>
  document.addEventListener('DOMContentLoaded', function () {
    const contactSection = document.getElementById('contact');
    const contactBgText = document.querySelector('.contact-bg-text');

    if (contactSection && contactBgText) {
      contactSection.addEventListener('mousemove', (e) => {
        const rect = contactSection.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width;
        const y = (e.clientY - rect.top) / rect.height;

        const bgX = 20 + x * 60;
        const bgY = 20 + y * 60;
        contactBgText.style.backgroundPosition = `${bgX}% ${bgY}%`;
      });
      contactSection.addEventListener('mouseleave', () => {
        contactBgText.style.backgroundPosition = '50% 50%';
      });
    }
  });
</script>
"""

if 'CONTACT SHAKTHI SRI T S TEXT' not in content:
    content = content.replace('</body>', HOVER_SCRIPT + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully applied 'Shaping Tomorrow' image mask text effect and interactive mouse hover effect to SHAKTHI SRI T S in contact section!")
