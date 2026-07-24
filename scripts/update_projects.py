from bs4 import BeautifulSoup
import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')

cards = soup.find_all(class_="project-card")

for card in cards:
    # Extract data
    img = card.find('img')
    src = img['src'] if img and img.has_attr('src') else ''
    alt = img['alt'] if img and img.has_attr('alt') else 'Project'

    overlay = card.find(class_="project-overlay")
    if not overlay:
        # Check if it was already modified or has a different structure
        continue
    
    h3 = overlay.find('h3')
    title = h3.get_text(strip=True) if h3 else 'Project Title'
    
    p = overlay.find('p')
    category = p.get_text(strip=True) if p else 'Category'

    # Clear current contents
    card.clear()

    # Determine classes to keep
    classes = card.get('class', [])
    new_classes = [c for c in classes if c not in ['hoverable', 'project-overlay']]
    # Add new styling classes
    style_classes = "group bg-[#fafafc] rounded-[1.5rem] p-4 flex flex-col gap-4 border border-black/5 hover:shadow-xl transition-all duration-300 cursor-pointer".split()
    for sc in style_classes:
        if sc not in new_classes:
            new_classes.append(sc)
    
    card['class'] = new_classes

    # Build new inner HTML
    inner_html = f"""
    <!-- Image Container -->
    <div class="w-full aspect-video rounded-xl overflow-hidden relative bg-gray-100">
      <img src="{src}" alt="{alt}" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" />
    </div>
    <!-- Meta Container -->
    <div class="flex items-center justify-between px-2 pb-2">
      <h3 class="text-lg md:text-xl font-bold text-gray-900 tracking-tight">{title}</h3>
      <div class="flex items-center gap-2">
        <span class="px-3 py-1 rounded-full border border-gray-200 text-xs md:text-sm text-gray-700 bg-white shadow-sm font-medium whitespace-nowrap">2024</span>
        <span class="px-3 py-1 rounded-full border border-gray-200 text-xs md:text-sm text-gray-700 bg-white shadow-sm font-medium whitespace-nowrap hidden sm:inline-block">{category}</span>
      </div>
    </div>
    """
    
    # Parse the inner html and append to card
    inner_soup = BeautifulSoup(inner_html, 'html.parser')
    for elem in inner_soup:
        card.append(elem)

# Also update the main section container to be light if needed (user wants a light background for cards, so maybe the section too)
# The user asked "in portfolio the projects sectin display make it look like this design". 
# The design has an off-white bg. We should make the portfolio section background light.
projects_section = soup.find(id="work")
if projects_section:
    sec_classes = projects_section.get('class', [])
    # replace bg-black/bg-[#111] with bg-[#F8F9FA] or similar
    new_sec_classes = [c for c in sec_classes if not c.startswith('bg-')]
    new_sec_classes.append('bg-[#F3F4F6]')
    projects_section['class'] = new_sec_classes
    
    # Also fix text colors in the section header (e.g. "Selected Works")
    headers = projects_section.find_all(['h2', 'p', 'h3'])
    for h in headers:
        hc = h.get('class', [])
        hc = [c for c in hc if not c.startswith('text-white')]
        if 'brand' in hc or h.name == 'h2':
            hc.append('text-gray-900')
        else:
            hc.append('text-gray-600')
        h['class'] = hc
        
    # Update category filters
    filters = projects_section.find_all('button', class_='filter-btn')
    for f in filters:
        fc = f.get('class', [])
        # replace dark mode button styles with light mode styles
        fc = [c for c in fc if c not in ['text-white/50', 'hover:text-white', 'text-white', 'border-white', 'border-transparent']]
        if 'active' in fc:
            fc.extend(['text-gray-900', 'border-gray-900'])
        else:
            fc.extend(['text-gray-500', 'hover:text-gray-900', 'border-transparent'])
        f['class'] = fc

with open("index.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Successfully updated project cards.")
