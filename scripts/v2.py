import sys
sys.stdout.reconfigure(encoding='utf-8')
c = open('index.html','r',encoding='utf-8').read()
checks = [
    ('n0-end exists',    'id="n0-end"' in c),
    ('n5-end exists',    'id="n5-end"' in c),
    ('no n0a stale',     'id="n0a"' not in c),
    ('no n0b stale',     'id="n0b"' not in c),
    ('no n1b stale',     'id="n1b"' not in c),
    ('endNode in segs',  'endNode:' in c),
    ('dot pop-in',       'dot, { opacity: 1' in c),
    ('6 seg-X paths',    c.count('id="seg-') == 6),
    ('6 n-end dots',     c.count('-end" class="journey-node"') == 6),
]
for name, ok in checks:
    print(f'  [{"OK  " if ok else "FAIL"}]  {name}')
