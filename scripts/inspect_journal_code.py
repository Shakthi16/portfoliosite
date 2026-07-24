import os

for fname in os.listdir('.'):
    if fname.endswith('.py') or fname.endswith('.html'):
        try:
            with open(fname, encoding='utf-8', errors='ignore') as f:
                content = f.read()
            if 'smriti-book-cover' in content or 'openSmritiBook' in content or 'cover.png' in content:
                print(f"Found in {fname}: size {len(content)}")
        except:
            pass
