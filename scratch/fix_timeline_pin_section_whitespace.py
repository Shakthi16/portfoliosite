with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix min-height: 2700px on timeline-scroll-wrapper which caused the massive whitespace gap
content = content.replace(
    '<div class="relative w-full overflow-hidden" id="timeline-scroll-wrapper" style="min-height: 2700px;">',
    '<div class="relative w-full overflow-hidden py-4" id="timeline-scroll-wrapper">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully removed min-height: 2700px from #timeline-scroll-wrapper!")
