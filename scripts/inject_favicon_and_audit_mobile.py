import os, re

favicon_tags = '''  <!-- Custom Branded Favicon for Browser Visibility -->
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="alternate icon" type="image/svg+xml" href="favicon.svg">
  <link rel="apple-touch-icon" href="favicon.svg">
'''

target_htmls = ['index.html', 'agni-c2.html', 'startuptn.html', 'pitch-deck.html', 'corporate-card.html', 'brand-identity.html']

for fname in target_htmls:
    fp = os.path.join('e:/portfoliosite', fname)
    if os.path.exists(fp):
        try:
            with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Remove any existing broken favicon tags if present
            content = re.sub(r'<link[^>]*rel=["\'](?:shortcut )?icon["\'][^>]*>', '', content, flags=re.IGNORECASE)
            
            # Inject new favicon tags right after <head> or before </head>
            if '<head>' in content:
                content = content.replace('<head>', '<head>\n' + favicon_tags)
            elif '</head>' in content:
                content = content.replace('</head>', favicon_tags + '\n</head>')
                
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Successfully injected custom favicon into {fname}!')
        except Exception as e:
            print(f'Error processing {fname}: {e}')

print("FAVICON INJECTION COMPLETE!")
