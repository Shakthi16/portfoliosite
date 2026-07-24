import os

for fn in os.listdir('.'):
    if fn.endswith('.html') or fn.endswith('.py'):
        try:
            with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                if 'id="node-hero"' in content or "id='node-hero'" in content or 'node-hero' in content:
                    print(f"Match for node-hero in: {fn} ({os.path.getsize(fn)} bytes)")
        except Exception as e:
            pass
