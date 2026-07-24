import bs4

# Read both files
with open('old_index.html', 'r', encoding='utf-16le') as f:
    old_soup = bs4.BeautifulSoup(f.read(), 'html.parser')

with open('index.html', 'r', encoding='utf-8') as f:
    new_soup = bs4.BeautifulSoup(f.read(), 'html.parser')

# Map old cards by title
old_cards = old_soup.find_all(lambda t: t.has_attr('class') and 'project-card' in t['class'])
old_card_map = {}
for c in old_cards:
    title_tag = c.find('h3')
    if title_tag:
        title = title_tag.text.strip()
        # Find the github and external links
        links = []
        for a in c.find_all('a'):
            href = a.get('href', '')
            if 'github.com' in href or a.find('i', class_=lambda c: c and 'fa-github' in c):
                links.append({'type': 'github', 'href': href})
            elif 'fa-external-link-alt' in str(a) or 'figma.com' in href or a.find('i', class_=lambda c: c and 'fa-figma' in c):
                # Using external link or figma
                icon_type = 'figma' if 'figma.com' in href else 'external'
                links.append({'type': icon_type, 'href': href})
        old_card_map[title] = links

# Update new cards
new_cards = new_soup.find_all(lambda t: t.has_attr('class') and 'project-card' in t['class'])
for c in new_cards:
    title_tag = c.find('h3')
    if title_tag:
        title = title_tag.text.strip()
        if title in old_card_map and old_card_map[title]:
            links = old_card_map[title]
            
            # Find the flex container that holds the badges
            # It's the div inside the flex items-center justify-between
            bottom_div = title_tag.find_next_sibling('div')
            if bottom_div:
                # Append the links to the badges container
                for link in links:
                    a_tag = new_soup.new_tag('a', href=link['href'], target="_blank")
                    a_tag['class'] = "text-gray-500 hover:text-[#B14665] transition-colors flex items-center justify-center p-1"
                    if link['type'] == 'github':
                        a_tag.append(bs4.BeautifulSoup('<i class="fab fa-github text-lg"></i>', 'html.parser'))
                    elif link['type'] == 'figma':
                        a_tag.append(bs4.BeautifulSoup('<i class="fab fa-figma text-lg"></i>', 'html.parser'))
                    else:
                        a_tag.append(bs4.BeautifulSoup('<i class="fas fa-external-link-alt text-lg"></i>', 'html.parser'))
                    bottom_div.append(a_tag)

# 2. Extract Profiles and Experience from old_about.txt and inject them back
with open('old_about.txt', 'r', encoding='utf-8') as f:
    old_about_soup = bs4.BeautifulSoup(f.read(), 'html.parser')

# We'll create a new section for Experience and Profiles
# to be placed right before #projects (or right after #about)
experience_html = """
<section class="py-24 px-6 bg-[#FAFAFA] text-[#1F1F1F] border-t border-gray-200" id="experience">
  <div class="max-w-7xl mx-auto">
    <div class="flex flex-col md:flex-row gap-12">
      <!-- Experience Column -->
      <div class="flex-1">
        <h2 class="text-4xl font-bold mb-8 text-[#1F1F1F] tracking-tight">Experience</h2>
        <div class="space-y-8 relative before:absolute before:inset-0 before:ml-5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-gray-300 before:to-transparent">
          
          <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
            <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white bg-[#B14665] text-white shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10">
              <i class="fas fa-shield-alt text-xs"></i>
            </div>
            <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-white p-6 rounded-2xl shadow-[0_10px_30px_-15px_rgba(0,0,0,0.05)] border border-gray-100 transition-all duration-300 hover:shadow-[0_20px_50px_-15px_rgba(177,70,101,0.1)] hover:-translate-y-1">
              <div class="flex items-center justify-between mb-2">
                <h4 class="font-bold text-gray-900 text-lg">IIT Madras - CYSTAR Lab</h4>
                <span class="text-xs font-bold text-[#B14665] bg-[#B14665]/10 px-3 py-1 rounded-full">Aug '25</span>
              </div>
              <p class="text-sm font-medium text-gray-500 mb-3">Cybersecurity Research Intern</p>
              <p class="text-gray-600 text-sm leading-relaxed">Offensive security research workflows including exposure analysis, EDR/AV study, explainable security, and technical documentation.</p>
            </div>
          </div>

          <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group">
            <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white bg-gray-200 text-gray-500 shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10">
              <i class="fas fa-cogs text-xs"></i>
            </div>
            <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-white p-6 rounded-2xl shadow-[0_10px_30px_-15px_rgba(0,0,0,0.05)] border border-gray-100 transition-all duration-300 hover:shadow-[0_20px_50px_-15px_rgba(177,70,101,0.1)] hover:-translate-y-1">
              <div class="flex items-center justify-between mb-2">
                <h4 class="font-bold text-gray-900 text-lg">OpsIntellix</h4>
                <span class="text-xs font-bold text-gray-500 bg-gray-100 px-3 py-1 rounded-full">Nov '25 - Feb '26</span>
              </div>
              <p class="text-sm font-medium text-gray-500 mb-3">Operations Intern - AP Automation</p>
              <p class="text-gray-600 text-sm leading-relaxed">Automated banking workflows, document classification, and validation using Python, boosting pipeline efficiency by 30%.</p>
            </div>
          </div>

          <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group">
            <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white bg-gray-200 text-gray-500 shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10">
              <i class="fas fa-code text-xs"></i>
            </div>
            <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-white p-6 rounded-2xl shadow-[0_10px_30px_-15px_rgba(0,0,0,0.05)] border border-gray-100 transition-all duration-300 hover:shadow-[0_20px_50px_-15px_rgba(177,70,101,0.1)] hover:-translate-y-1">
              <div class="flex items-center justify-between mb-2">
                <h4 class="font-bold text-gray-900 text-lg">Focuslogic IT Services</h4>
                <span class="text-xs font-bold text-gray-500 bg-gray-100 px-3 py-1 rounded-full">Mar - May '25</span>
              </div>
              <p class="text-sm font-medium text-gray-500 mb-3">Web Development Intern</p>
              <p class="text-gray-600 text-sm leading-relaxed">Built responsive React.js frontends from Figma, integrated REST APIs, conducted manual UI testing, and reduced load latency by 25%.</p>
            </div>
          </div>

        </div>
      </div>
      
      <!-- Right Column: Profiles & Certifications -->
      <div class="w-full md:w-[350px] flex flex-col gap-6">
        <h2 class="text-4xl font-bold mb-2 text-[#1F1F1F] tracking-tight">Profiles</h2>
        <div class="bg-white p-6 rounded-3xl shadow-[0_10px_30px_-15px_rgba(0,0,0,0.05)] border border-gray-100 flex flex-col gap-4">
          <a href="https://linkedin.com/in/shakthisri" target="_blank" class="flex items-center justify-between p-3 rounded-xl hover:bg-gray-50 transition-colors group">
            <div class="flex items-center gap-3"><i class="fab fa-linkedin text-2xl text-[#0a66c2]"></i><span class="font-bold text-gray-700 group-hover:text-black">LinkedIn</span></div>
            <i class="fas fa-arrow-right text-gray-300 group-hover:text-[#B14665] transition-colors -rotate-45"></i>
          </a>
          <a href="https://github.com/Shakthi16" target="_blank" class="flex items-center justify-between p-3 rounded-xl hover:bg-gray-50 transition-colors group">
            <div class="flex items-center gap-3"><i class="fab fa-github text-2xl text-gray-900"></i><span class="font-bold text-gray-700 group-hover:text-black">GitHub</span></div>
            <i class="fas fa-arrow-right text-gray-300 group-hover:text-[#B14665] transition-colors -rotate-45"></i>
          </a>
          <a href="https://leetcode.com/u/srishakthi799/" target="_blank" class="flex items-center justify-between p-3 rounded-xl hover:bg-gray-50 transition-colors group">
            <div class="flex items-center gap-3"><i class="fas fa-code text-2xl text-yellow-500"></i><span class="font-bold text-gray-700 group-hover:text-black">LeetCode</span></div>
            <i class="fas fa-arrow-right text-gray-300 group-hover:text-[#B14665] transition-colors -rotate-45"></i>
          </a>
          <a href="https://tryhackme.com/p/shakthisri1929" target="_blank" class="flex items-center justify-between p-3 rounded-xl hover:bg-gray-50 transition-colors group">
            <div class="flex items-center gap-3"><i class="fas fa-shield-alt text-2xl text-red-500"></i><span class="font-bold text-gray-700 group-hover:text-black">TryHackMe</span></div>
            <i class="fas fa-arrow-right text-gray-300 group-hover:text-[#B14665] transition-colors -rotate-45"></i>
          </a>
        </div>

        <h2 class="text-4xl font-bold mt-4 mb-2 text-[#1F1F1F] tracking-tight">Certs</h2>
        <div class="bg-white p-6 rounded-3xl shadow-[0_10px_30px_-15px_rgba(0,0,0,0.05)] border border-gray-100 flex flex-col gap-4">
          <div class="flex items-start gap-3">
            <i class="fas fa-certificate text-[#B14665] mt-1"></i>
            <p class="text-sm text-gray-600 font-medium">UI/UX, React, AI, Python <br/><span class="text-xs text-gray-400">Infosys Springboard</span></p>
          </div>
          <div class="flex items-start gap-3">
            <i class="fas fa-certificate text-[#B14665] mt-1"></i>
            <p class="text-sm text-gray-600 font-medium">Cybersecurity Mastery <br/><span class="text-xs text-gray-400">Udemy</span></p>
          </div>
          <div class="flex items-start gap-3">
            <i class="fas fa-certificate text-[#B14665] mt-1"></i>
            <p class="text-sm text-gray-600 font-medium">Full Stack Web Dev <br/><span class="text-xs text-gray-400">NoviTech</span></p>
          </div>
          <div class="flex items-start gap-3">
            <i class="fas fa-certificate text-[#B14665] mt-1"></i>
            <a href="https://rb.gy/l6f8ss" target="_blank" class="text-sm text-gray-600 font-medium hover:text-[#B14665]">Data Analytics & Cloud <br/><span class="text-xs text-gray-400">Google</span></a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

# Insert the experience section right before the projects section
projects_section = new_soup.find('section', id='projects')
if projects_section:
    projects_section.insert_before(bs4.BeautifulSoup(experience_html, 'html.parser'))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(new_soup))

print("Restored missing project Github links and created Experience/Profiles section.")
