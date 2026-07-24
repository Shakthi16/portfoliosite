import os

scripts = [
    'fix_missing_section_REAL.py',
    'fix_missing_section_final.py',
    'build_full_restored_sections.py',
    'build_perfect_creative_journal.py',
    'add_face_path_runner.py',
    'refine_face_emoji_appearance.py'
]

for s in scripts:
    if os.path.exists(s):
        print(f"=== {s} ({os.path.getsize(s)} bytes) ===")
        with open(s, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            print("First 15 lines:")
            for l in lines[:15]:
                print(" ", l.rstrip())
        print("\n" + "="*40 + "\n")
