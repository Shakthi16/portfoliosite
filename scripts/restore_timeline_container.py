import os, re

def find_timeline_container():
    for fname in os.listdir('.'):
        if (fname.endswith('.py') or fname.endswith('.html')) and fname != 'index.html':
            try:
                with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
                    c = f.read()
                    if 'id="timeline-container"' in c:
                        print(f"Found timeline-container in {fname}")
                        m = re.search(r'<div class="relative w-full max-w-\[1400px\].*?id="timeline-container".*?<!-- Mobile Fallback', c, re.DOTALL)
                        if m:
                            print(f"Match length in {fname}: {len(m.group(0))}")
                            with open('timeline_backup.html', 'w', encoding='utf-8') as out:
                                out.write(m.group(0))
                            return
            except Exception as e:
                pass

find_timeline_container()
