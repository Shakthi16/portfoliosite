import os

files = [f for f in os.listdir('.') if f.endswith('.html')]
print("All HTML files in repository:")
for f in files:
    size = os.path.getsize(f)
    print(f" - {f:<35} {size:>8} bytes")
