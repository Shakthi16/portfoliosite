import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The "Shaping Tomorrow" section to remove:
# <section class="py-24 px-6 gs-reveal relative" id="text-mask-section">
# ...
# </section>
# It's right before <!-- PROJECTS --> or <!-- PROJECTS (GRID VIEW) -->
shaping_pattern = re.compile(r'<!-- TEXT MASKING SECTION -->.*?id="text-mask-section">.*?</section>\s*', re.DOTALL)
html = shaping_pattern.sub('', html)

# Now, find SHAKTHI SRI T S in the contact section:
# <h2 class="contact-bg-text select-none text-center tracking-tighter w-full">
#            SHAKTHI SRI T S
#          </h2>
# We want to replace it with the masked style.
# Style used in Shaping Tomorrow: style="background-image: url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2000&auto=format&fit=crop'); background-size: 150%; background-position: 50% 50%; -webkit-background-clip: text; -webkit-text-fill-color: transparent;"
# We will apply this style to the SHAKTHI text.

shakthi_target = r'<h2 class="contact-bg-text select-none text-center tracking-tighter w-full">\s*SHAKTHI SRI T S\s*</h2>'
new_shakthi = r'''<h2 class="contact-bg-text select-none text-center tracking-tighter w-full" style="background-image: url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2000&auto=format&fit=crop'); background-size: 150%; background-position: 50% 50%; -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            SHAKTHI SRI T S
          </h2>'''

html = re.sub(shakthi_target, new_shakthi, html, flags=re.IGNORECASE)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Moved text mask successfully.")
