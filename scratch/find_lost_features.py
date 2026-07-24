import os

for fn in os.listdir('.'):
    if fn.endswith('.html') or fn.endswith('.py'):
        try:
            with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                matches = []
                if 'path-traveler-avatar' in content or 'face.png' in content:
                    matches.append('face_emoji_traveler')
                if 'smriti-book-opened' in content or 'smriti-spread' in content:
                    matches.append('smriti_journal')
                if 'text-mask-section' in content or 'Shaping' in content:
                    matches.append('shaping_tomorrow')
                if matches:
                    print(f"File: {fn:<40} Matches: {matches}")
        except Exception as e:
            pass
