import os, sys

scripts = [
    'build_perfect_creative_journal.py',
    'build_full_restored_sections.py',
    'refine_face_emoji_appearance.py',
    'undo_last_changes.py'
]

for s in scripts:
    if os.path.exists(s):
        print(f"Executing {s}...")
        try:
            with open(s, 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, {'__name__': '__main__'})
            print(f"Successfully executed {s}")
        except Exception as e:
            print(f"Error in {s}: {e}")
    else:
        print(f"Script {s} not found!")

print("\nRestoration complete!")
