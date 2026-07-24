import os

scripts = [
    'add_face_path_runner.py',
    'refine_face_emoji_appearance.py'
]

for s in scripts:
    if os.path.exists(s):
        print(f"Executing {s}...")
        with open(s, 'r', encoding='utf-8') as f:
            code = f.read()
        exec(code, {'__name__': '__main__'})

print("Avatar runner execution complete!")
