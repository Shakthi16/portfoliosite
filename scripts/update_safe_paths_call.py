with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure updatePathAvatarScroll is also called inside safeJourneyPaths
if 'safeJourneyPaths error:' in content and 'updatePathAvatarScroll()' not in content.split('safeJourneyPaths error:')[0]:
    content = content.replace(
        "console.error('safeJourneyPaths error:', e);",
        "console.error('safeJourneyPaths error:', e);\n    }\n    if (typeof updatePathAvatarScroll === 'function') {\n      updatePathAvatarScroll();\n    }"
    )
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully linked updatePathAvatarScroll to safeJourneyPaths execution!")
else:
    print("Already linked or pattern matched!")
