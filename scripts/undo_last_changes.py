import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# -------------------------------------------------------------
# 1. REMOVE THE DYNAMIC CONNECTING ARROWS SCRIPT AT BOTTOM OF index.html
# -------------------------------------------------------------
script_marker = "<!-- DYNAMIC DOWNHILL CONNECTING PATHS BETWEEN EDITORIAL CARDS -->"
if script_marker in content:
    pos_script = content.find(script_marker)
    pos_end_script = content.find('</script>', pos_script) + len('</script>')
    content = content[:pos_script] + content[pos_end_script:]
    print("Successfully removed dynamic connecting arrows script!")

# -------------------------------------------------------------
# 2. RESTORE ORIGINAL .contact-bg-text CSS
# -------------------------------------------------------------
css_pattern = r'\.contact-bg-text\s*\{[^}]*\}(?:\s*@keyframes gradient-shift\s*\{[^}]*\}\s*\}?)?'
original_css = """.contact-bg-text {
      font-size: clamp(2.5rem, 11vw, 8.5rem);
      font-weight: 900;
      color: transparent;
      -webkit-text-stroke: 1.5px rgba(255, 255, 255, 0.18);
      text-transform: uppercase;
      letter-spacing: -0.04em;
      line-height: 0.85;
      font-family: 'Outfit', sans-serif;
      transition: color 0.5s ease, -webkit-text-stroke 0.5s ease;
    }"""

content = re.sub(css_pattern, original_css, content, count=1)

# Restore light-mode .contact-bg-text
light_mode_pattern = r'body\.light-mode \.contact-bg-text\s*\{[^}]*\}'
original_light_css = """body.light-mode .contact-bg-text {
      color: transparent;
      -webkit-text-stroke: 1.5px rgba(0, 0, 0, 0.14);
    }"""

content = re.sub(light_mode_pattern, original_light_css, content, count=1)
print("Successfully restored original .contact-bg-text CSS!")

# -------------------------------------------------------------
# 3. RE-INSERT #text-mask-section (Shaping Tomorrow)
# -------------------------------------------------------------
if 'id="text-mask-section"' not in content:
    TEXT_MASK_HTML = """
    <!-- Text Masking Section (Awwwards Style) -->
    <section class="py-24 px-6 gs-reveal relative" id="text-mask-section">
      <div class="max-w-7xl mx-auto text-center hoverable flex justify-center items-center min-h-[40vh]">
        <h2 class="text-[12vw] font-black brand leading-none uppercase tracking-tighter w-full" id="flowing-text"
          style="background-image: url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&amp;w=2000&amp;auto=format&amp;fit=crop'); background-size: 150%; background-position: 50% 50%; -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
          Shaping<br />Tomorrow
        </h2>
      </div>
    </section>
"""
    pos_projects = content.find('id="projects"')
    if pos_projects != -1:
        sec_start = content.rfind('<section', 0, pos_projects)
        content = content[:sec_start] + TEXT_MASK_HTML + '\n' + content[sec_start:]
        print("Successfully re-inserted #text-mask-section (Shaping Tomorrow)!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Last turn changes completely undone from index.html without touching git history.")
