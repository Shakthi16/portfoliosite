import subprocess
import re

try:
    result = subprocess.run(["C:\\Program Files\\Git\\cmd\\git.exe", "show", "HEAD~1:index.html"], capture_output=True, check=True)
    old_html = result.stdout.decode('utf-8', errors='ignore')
    
    # Extract paint palette
    paint_match = re.search(r'<!-- FAR RIGHT: Functional Retro MacPaint Palette.*?</div>\s*</div>\s*</div>', old_html, flags=re.DOTALL)
    if paint_match:
        with open("paint.txt", "w", encoding="utf-8") as f:
            f.write(paint_match.group(0))
            print("FOUND PAINT PALETTE!")
            
    # Extract interactive folder
    folder_match = re.search(r'<!-- 9\. 3D INTERACTIVE MASTER FOLDER.*?</div>\s*</div>\s*</div>', old_html, flags=re.DOTALL)
    if folder_match:
        with open("folder.txt", "w", encoding="utf-8") as f:
            f.write(folder_match.group(0))
            print("FOUND INTERACTIVE FOLDER!")
            
    # Also extract the canvas scripts
    script_match = re.search(r'<script>\s*\(function\(\) \{\s*// 3\. Canvas Logic.*?</script>', old_html, flags=re.DOTALL)
    if script_match:
        with open("canvas_script.txt", "w", encoding="utf-8") as f:
            f.write(script_match.group(0))
            print("FOUND CANVAS SCRIPT!")
            
except Exception as e:
    print(f"Error: {e}")
