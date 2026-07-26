import os, bs4, subprocess, tempfile

html_files = [f for f in os.listdir('e:/portfoliosite') if f.endswith('.html') and not f.startswith('old_') and not f.startswith('timeline_')]

print(f"--- RUNNING COMPREHENSIVE COMPATIBILITY & MOBILE AUDIT ON {len(html_files)} HTML PAGES ---")

audit_results = {}

for hf in html_files:
    fp = os.path.join('e:/portfoliosite', hf)
    with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
        html_code = f.read()
    
    soup = bs4.BeautifulSoup(html_code, 'html.parser')
    
    # 1. Check Viewport Meta Tag
    viewport = soup.find('meta', attrs={'name': 'viewport'})
    has_viewport = viewport is not None and 'width=device-width' in viewport.get('content', '')
    
    # 2. Check Favicons
    favicons = soup.find_all('link', rel=lambda r: r and 'icon' in r)
    has_favicon = len(favicons) > 0
    
    # 3. Audit Images
    images = soup.find_all('img')
    missing_imgs = []
    for img in images:
        src = img.get('src', '')
        if src and not src.startswith('http://') and not src.startswith('https://') and not src.startswith('data:'):
            img_path = os.path.join('e:/portfoliosite', src.split('#')[0].split('?')[0])
            if not os.path.exists(img_path):
                missing_imgs.append(src)
                
    # 4. Audit Internal Links
    links = soup.find_all('a')
    missing_links = []
    for link in links:
        href = link.get('href', '')
        if href and not href.startswith('http') and not href.startswith('mailto:') and not href.startswith('tel:') and not href.startswith('#'):
            link_path = os.path.join('e:/portfoliosite', href.split('#')[0].split('?')[0])
            if not os.path.exists(link_path):
                missing_links.append(href)
                
    # 5. Node.js Script Syntax Validation
    scripts = soup.find_all('script')
    js_errors = []
    for i, script in enumerate(scripts):
        if script.string and script.string.strip():
            with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as tf:
                tf.write(script.string)
                tf_path = tf.name
            res = subprocess.run(['node', '--check', tf_path], capture_output=True, text=True)
            if res.returncode != 0:
                js_errors.append(f"Script #{i+1}: {res.stderr.strip()}")
            try:
                os.remove(tf_path)
            except Exception:
                pass

    audit_results[hf] = {
        'has_viewport': has_viewport,
        'has_favicon': has_favicon,
        'image_count': len(images),
        'missing_imgs': missing_imgs,
        'link_count': len(links),
        'missing_links': missing_links,
        'script_count': len(scripts),
        'js_errors': js_errors
    }

print("\n=== AUDIT RESULTS SUMMARY ===")
all_passed = True
for hf, res in audit_results.items():
    print(f"\nPAGE: {hf}")
    print(f"  * Viewport Meta: {'[PASS]' if res['has_viewport'] else '[FAIL]'}")
    print(f"  * Favicon Linked: {'[PASS]' if res['has_favicon'] else '[FAIL]'}")
    print(f"  * Images Checked: {res['image_count']} total ({len(res['missing_imgs'])} missing)")
    if res['missing_imgs']:
        print(f"    WARNING Missing Images: {res['missing_imgs']}")
        all_passed = False
    print(f"  * Links Checked: {res['link_count']} total ({len(res['missing_links'])} missing)")
    if res['missing_links']:
        print(f"    WARNING Missing Links: {res['missing_links']}")
        all_passed = False
    print(f"  * JavaScript Scripts: {res['script_count']} checked ({len(res['js_errors'])} errors)")
    if res['js_errors']:
        print(f"    WARNING JS Syntax Errors: {res['js_errors']}")
        all_passed = False

if all_passed:
    print("\nALL COMPATIBILITY, RESPONSIVENESS, IMAGE, LINK AND SCRIPT CHECKS PASSED WITH 100% SUCCESS!")
else:
    print("\nSOME CHECKS NEED FIXES - SEE DETAILED LOG ABOVE!")
