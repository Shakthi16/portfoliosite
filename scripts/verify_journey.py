import sys
sys.stdout.reconfigure(encoding='utf-8')

content = open('index.html','r',encoding='utf-8').read()

checks = [
    ('viewBox correct',       'viewBox="0 0 1400 2200"' in content),
    ('seg-0 exists',          'id="seg-0"' in content),
    ('seg-4 exists',          'id="seg-4"' in content),
    ('journey-node class',    'journey-node' in content),
    ('journey-path class',    'journey-path' in content),
    ('JOURNEY DRAW SYSTEM',   'JOURNEY DRAW SYSTEM' in content),
    ('DOMContentLoaded once', content.count("JOURNEY DRAW SYSTEM") == 1),
    ('No old path-0 id',      'id="path-0"' not in content),
    ('No old dot-0-start',    'id="dot-0-start"' not in content),
    ('scrub: 2',              'scrub:   2' in content),
    ('strokeDashoffset: 0',   'strokeDashoffset: 0' in content),
    ('elastic.out',           'elastic.out' in content),
    ('Only 1 script close',   content[-500:].count('</script>') == 1),
]

all_ok = True
for name, result in checks:
    status = 'OK  ' if result else 'FAIL'
    if not result:
        all_ok = False
    print(f'  [{status}]  {name}')

print()
print('ALL CLEAR' if all_ok else 'SOME CHECKS FAILED')
