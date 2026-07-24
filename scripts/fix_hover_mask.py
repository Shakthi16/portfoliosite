import re
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add background mask CSS to SHAKTHI SRI T S
shakthi_target = r'<h2 class="contact-bg-text select-none text-center tracking-tighter w-full">\s*SHAKTHI SRI T S\s*</h2>'
new_h2 = r'''<h2 id="flowing-text" class="contact-bg-text select-none text-center tracking-tighter w-full" style="background-image: url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2000&auto=format&fit=crop'); background-size: 150%; background-position: 50% 50%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; transition: background-position 0.2s ease-out;">
            SHAKTHI SRI T S
          </h2>'''
html = re.sub(shakthi_target, new_h2, html)

# 2. Update the JS event listener
old_js = r'''const textMaskSection = document.getElementById\('text-mask-section'\);'''
new_js = r'''const textMaskSection = document.getElementById('contact');'''
html = re.sub(old_js, new_js, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Restored hover mask JS")
