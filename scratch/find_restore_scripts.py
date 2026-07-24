import os

files = [f for f in os.listdir('.') if f.endswith('.py')]
for fn in files:
    with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        if 'restored_journey_section' in content or 'timeline-pin-section' in content:
            print(f"Match in {fn}")
