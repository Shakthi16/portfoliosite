import os, re

def search_in_file(filepath, pattern):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            if pattern.lower() in content.lower():
                print(f"=== Found in {filepath} ===")
                matches = re.findall(rf'.{{0,100}}{pattern}.{{0,100}}', content, re.IGNORECASE)
                for m in matches[:5]:
                    print("  ...", m.strip().replace('\n', ' '), "...")
    except Exception as e:
        pass

for fname in os.listdir('.'):
    if fname.endswith('.py') or fname.endswith('.html') or fname.endswith('.txt'):
        search_in_file(fname, 'achievements')
        search_in_file(fname, 'ach-carousel')
