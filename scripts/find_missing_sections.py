import os

# Search all files for "Learning in Motion" scrolling ticker and "My Arsenal" skills dial
targets = {
    'Learning in Motion (ticker)': ['marquee', 'ticker', 'Infosys', 'NoviTech', '150+ Hours'],
    'My Arsenal': ['MY ARSENAL', 'my-arsenal', 'id="skills"', 'bento-tech', 'dial'],
}

for label, terms in targets.items():
    print(f'\n=== {label} ===')
    for fname in sorted(os.listdir('.')):
        if not (fname.endswith('.py') or fname.endswith('.html')):
            continue
        try:
            with open(fname, encoding='utf-8', errors='ignore') as f:
                content = f.read()
            for term in terms:
                if term in content:
                    pos = content.find(term)
                    print(f'  [{fname}] found "{term}" at pos {pos}')
                    break
        except:
            pass
