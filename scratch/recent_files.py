import os, time

files = [f for f in os.listdir('.') if f.endswith('.py') or f.endswith('.html')]
files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

print("Files modified recently:")
for f in files[:20]:
    mtime = time.ctime(os.path.getmtime(f))
    size = os.path.getsize(f)
    print(f" - {f:<45} {size:>8} bytes   {mtime}")
