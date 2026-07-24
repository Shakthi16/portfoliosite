import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove desk-loader and loader-terminal CSS
content = re.sub(r'/\* Sequential Loader overlay \*/.*?(?=</style>)', '', content, flags=re.DOTALL)
# It might not match till </style> if there are other rules. Let's just remove specific blocks
content = re.sub(r'#desk-loader\s*\{[^}]*\}', '', content)
content = re.sub(r'#loader-terminal\s*\{[^}]*\}', '', content)
content = re.sub(r'\.desk-item\s*\{\s*opacity:\s*0;\s*visibility:\s*hidden;\s*\}', '', content)

# Remove preloader styles
content = re.sub(r'/\* Clean Preloader Styles \*/.*?(?=\/\* ========================)', '', content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Loaders removed!")
