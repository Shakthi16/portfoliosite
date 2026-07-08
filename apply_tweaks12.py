import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Move master folder little right
# from left: 26% to left: 32%
content = re.sub(
    r'(<!-- 16\. Interactive folder -->\s*<div class="floating-sticker"\s*style="top:\s*42%;\s*left:\s*)26(%;\s*z-index:\s*12;\s*transform:\s*rotate\(0deg\);\s*scale:\s*1\.1;">)',
    r'\g<1>34\g<2>',
    content
)

# 2. Swap the SVG folders for logos
# Item 1: cyber labs
icon1 = '''<div style="width: 50px; height: 50px; background: #ffffff; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 8px 20px rgba(0,0,0,0.15); border: 2px solid #eff6ff;">
              <i class="fas fa-terminal" style="font-size: 20px; color: #3b82f6;"></i>
            </div>'''
content = re.sub(
    r'<a href="#projects" class="sub-folder-item"[^>]*>.*?<svg[^>]*>.*?</svg>',
    r'<a href="#projects" class="sub-folder-item" style="text-decoration: none;">\n            ' + icon1,
    content,
    flags=re.DOTALL
)

# Item 2: brain dumps
icon2 = '''<div style="width: 50px; height: 50px; background: #ffffff; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 8px 20px rgba(0,0,0,0.15); border: 2px solid #f5f3ff;">
              <i class="fas fa-brain" style="font-size: 20px; color: #8b5cf6;"></i>
            </div>'''
content = re.sub(
    r'<a href="#about" class="sub-folder-item"[^>]*>.*?<svg[^>]*>.*?</svg>',
    r'<a href="#about" class="sub-folder-item" style="text-decoration: none;">\n            ' + icon2,
    content,
    flags=re.DOTALL
)

# Item 3: inspiration
icon3 = '''<div style="width: 50px; height: 50px; background: #ffffff; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 8px 20px rgba(0,0,0,0.15); border: 2px solid #fffbeb;">
              <i class="fas fa-lightbulb" style="font-size: 20px; color: #f59e0b;"></i>
            </div>'''
content = re.sub(
    r'<a href="#skills" class="sub-folder-item"[^>]*>.*?<svg[^>]*>.*?</svg>',
    r'<a href="#skills" class="sub-folder-item" style="text-decoration: none;">\n            ' + icon3,
    content,
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updates applied: Folder moved right, sub-folders converted to logos.")
