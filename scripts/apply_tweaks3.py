import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace all small folder SVGs with the Mac-style folder
mac_svg = '''<svg width="42" height="36" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(2px 4px 6px rgba(58,139,237,0.3));">
              <path d="M6 14 C6 11 8 9 11 9 L24 9 C26 9 28 10 29 12 L32 16 L53 16 C56 16 58 18 58 21 L58 52 C58 55 56 58 53 58 L11 58 C8 58 6 55 6 52 Z" fill="#61b5ff" />
              <path d="M6 26 C6 23 8 21 11 21 L53 21 C56 21 58 23 58 26 L58 52 C58 55 56 58 53 58 L11 58 C8 58 6 55 6 52 Z" fill="#2b8bf5" />
            </svg>'''

# Find the SVGs inside sub-folder-item and replace them
content = re.sub(
    r'<svg width="34" height="28".*?</svg>',
    mac_svg,
    content,
    flags=re.DOTALL
)

# 2. Update .sub-folder-label styles (there are two blocks in the CSS)
# I'll just find both and replace them with a unified style.
new_label_css = '''    .sub-folder-label {
      font-family: 'IBM Plex Mono', monospace !important;
      font-size: 11px;
      font-weight: 700;
      color: #1e3a8a !important;
      margin-top: 6px;
      background: #ffffff;
      padding: 4px 8px;
      border-radius: 4px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      white-space: nowrap;
    }'''

content = re.sub(
    r'\.sub-folder-label\s*\{[^}]*\}',
    new_label_css,
    content,
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updates applied: Mac folder SVGs injected, font updated to monospace white boxes.")
