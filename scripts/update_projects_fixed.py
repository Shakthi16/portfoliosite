import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the "Selected Works" section background
html = html.replace('id="work"', 'id="work"') # Just to find it
# We know the contact section starts after work. Let's find the projects section:
# <section class="py-24 px-6 md:px-12 bg-[#050505] text-white ... id="work">
html = re.sub(r'<section class="([^"]*)bg-\[#050505\]([^"]*)id="work">', 
              r'<section class="\1bg-[#fafafa]\2id="work">', html)

html = re.sub(r'id="work">', 'id="work">\n<style>\n#work h2, #work h3 { color: #111 !important; }\n#work p { color: #444 !important; }\n#work .filter-btn { color: #666; }\n#work .filter-btn.active { color: #111; border-color: #111; }\n#work .filter-btn:hover { color: #111; }\n</style>', html)


# 2. Extract and replace project cards
# A project card looks like: <div class="... project-card ..."> ... </div> or <a> ... </a>
def replace_card(match):
    full_match = match.group(0)
    
    # Extract original tag
    tag = 'a' if full_match.strip().startswith('<a') else 'div'
    
    # Extract attributes from opening tag
    open_tag_match = re.match(r'<[a-z]+([^>]+)>', full_match)
    if not open_tag_match: return full_match
    attrs_str = open_tag_match.group(1)
    
    # Extract classes
    class_match = re.search(r'class="([^"]+)"', attrs_str)
    classes = class_match.group(1).split() if class_match else []
    
    # Retain important classes
    keep_classes = [c for c in classes if c not in ['hoverable', 'project-overlay']]
    new_styles = "group bg-[#fafafc] rounded-[1.5rem] p-4 flex flex-col gap-4 border border-black/5 hover:shadow-xl transition-all duration-300 cursor-pointer".split()
    for s in new_styles:
        if s not in keep_classes:
            keep_classes.append(s)
            
    # Extract href and target if it's an <a>
    extra_attrs = ""
    if tag == 'a':
        href_m = re.search(r'href="([^"]+)"', attrs_str)
        target_m = re.search(r'target="([^"]+)"', attrs_str)
        if href_m: extra_attrs += f' href="{href_m.group(1)}"'
        if target_m: extra_attrs += f' target="{target_m.group(1)}"'
        
    # Extract image src and alt
    img_m = re.search(r'<img[^>]*src="([^"]+)"', full_match)
    src = img_m.group(1) if img_m else ''
    
    alt_m = re.search(r'<img[^>]*alt="([^"]+)"', full_match)
    alt = alt_m.group(1) if alt_m else 'Project'
    
    # Extract title
    title_m = re.search(r'<h3[^>]*>([^<]+)</h3>', full_match)
    title = title_m.group(1).strip() if title_m else 'Project Title'
    
    # Extract category
    cat_m = re.search(r'<p[^>]*>([^<]+)</p>', full_match)
    cat = cat_m.group(1).strip() if cat_m else 'Category'
    
    # Build new card
    new_card = f'''<{tag} class="{" ".join(keep_classes)}"{extra_attrs}>
      <div class="w-full aspect-video rounded-xl overflow-hidden relative bg-gray-100">
        <img src="{src}" alt="{alt}" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" />
      </div>
      <div class="flex items-center justify-between px-2 pb-2 mt-2">
        <h3 class="text-xl font-bold text-gray-900 tracking-tight m-0">{title}</h3>
        <div class="flex items-center gap-2">
          <span class="px-3 py-1 rounded-full border border-gray-200 text-xs text-gray-700 bg-white shadow-sm font-medium whitespace-nowrap">2024</span>
          <span class="px-3 py-1 rounded-full border border-gray-200 text-xs text-gray-700 bg-white shadow-sm font-medium whitespace-nowrap hidden sm:inline-block">{cat}</span>
        </div>
      </div>
    </{tag}>'''
    
    return new_card

# Regex to match a full div or a project card block
# Since nested divs are hard with regex, we'll split by <div class="... project-card ... "> or <a class="... project-card ...">
# A safer way is to use BeautifulSoup properly this time.

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
cards = soup.find_all(lambda tag: tag.has_attr('class') and 'project-card' in tag['class'])

for card in cards:
    src = ""
    alt = "Project"
    title = "Title"
    cat = "Category"
    
    img = card.find('img')
    if img:
        src = img.get('src', '')
        alt = img.get('alt', 'Project')
        
    h3 = card.find('h3')
    if h3:
        title = h3.get_text(strip=True)
        
    p = card.find('p')
    if p:
        cat = p.get_text(strip=True)
        
    # preserve tag name
    tag_name = card.name
    
    # Keep classes
    classes = card.get('class', [])
    new_classes = [c for c in classes if c not in ['hoverable', 'project-overlay']]
    new_styles = "group bg-[#fafafc] rounded-[1.5rem] p-4 flex flex-col gap-4 border border-black/5 hover:shadow-xl transition-all duration-300 cursor-pointer".split()
    for s in new_styles:
        if s not in new_classes:
            new_classes.append(s)
    
    # Generate new inner HTML string
    inner_html = f'''
      <div class="w-full aspect-video rounded-xl overflow-hidden relative bg-gray-100 border border-gray-100">
        <img src="{src}" alt="{alt}" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" />
      </div>
      <div class="flex items-center justify-between px-2 pb-2 mt-2">
        <h3 class="text-xl font-bold text-gray-900 tracking-tight m-0" style="color:#111 !important;">{title}</h3>
        <div class="flex items-center gap-2">
          <span class="px-3 py-1 rounded-full border border-gray-200 text-xs text-gray-700 bg-white shadow-sm font-medium whitespace-nowrap" style="color:#444 !important;">2024</span>
          <span class="px-3 py-1 rounded-full border border-gray-200 text-xs text-gray-700 bg-white shadow-sm font-medium whitespace-nowrap hidden sm:inline-block" style="color:#444 !important;">{cat}</span>
        </div>
      </div>
    '''
    
    # Safely replace contents
    card.clear()
    card['class'] = new_classes
    # Parse the inner html as soup and append children
    parsed_inner = BeautifulSoup(inner_html, 'html.parser')
    for child in list(parsed_inner.children):
        card.append(child)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Done project cards")
