import os

for fn in ['timeline_backup.html', 'restored_journey_section.html', 'old_index.html']:
    if os.path.exists(fn):
        print(f"=== {fn} ({os.path.getsize(fn)} bytes) ===")
        with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            print(content[:500])
            print("\n" + "="*40 + "\n")
    else:
        print(f"=== {fn} NOT FOUND ===")
