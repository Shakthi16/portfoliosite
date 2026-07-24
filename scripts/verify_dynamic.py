import sys
sys.stdout.reconfigure(encoding='utf-8')
content = open('index.html','r',encoding='utf-8').read()
checks = [
    ('GitHub card HTML',        'id="node-github"' in content),
    ('seg-5 SVG path',          'id="seg-5"' in content),
    ('n5-end node',            'id="n5-end"' in content),
    ('Dynamic path builder',    'buildJourneyPaths' in content),
    ('vb() function',           'function vb(' in content),
    ('setPath() function',      'function setPath(' in content),
    ('resize listener',         "addEventListener('resize'" in content),
    ('setTimeout 150ms',        'setTimeout(' in content),
    ('6 segments config',       content.count("{ id: 'seg-") == 6),
    ('seg-5 in config',         "'seg-5'" in content),
    ('No stale anim-path',      '.anim-path' not in content[content.find('buildJourneyPaths'):]),
    ('Only 1 JOURNEY block',    content.count('JOURNEY DRAW SYSTEM') == 1),
]
all_ok = all(r for _,r in checks)
for name, result in checks:
    print(f'  [{"OK  " if result else "FAIL"}]  {name}')
print()
print('ALL CLEAR' if all_ok else 'SOME CHECKS FAILED')
