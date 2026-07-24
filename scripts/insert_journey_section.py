with open('git_version.html', 'r', encoding='utf-8') as f:
    git_lines = f.readlines()

# Extract journey + academic + certs (lines 4271-4506, 0-indexed)
journey_html = ''.join(git_lines[4271:4507])

# Fix ID conflict: rename inner timeline-container to journey-timeline-container
journey_html = journey_html.replace('id="timeline-container"', 'id="journey-timeline-container"')
journey_html = journey_html.replace("'timeline-fill'", "'journey-timeline-fill'")
journey_html = journey_html.replace('id="timeline-fill"', 'id="journey-timeline-fill"')

# Wrap in a dark section wrapper
WRAPPED = f"""    <!-- 3. PROFESSIONAL JOURNEY, ACADEMIC BACKGROUND & CERTIFICATIONS -->
    <section class="relative bg-[var(--charcoal-bg)] text-white" id="journey-section" style="overflow:hidden;">
      <div class="max-w-7xl mx-auto px-6 lg:px-12">
{journey_html}
      </div>
    </section>

"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert right before <!-- SKILLS -->
ANCHOR = '    <!-- SKILLS -->'
if ANCHOR in content:
    content = content.replace(ANCHOR, WRAPPED + ANCHOR, 1)
    print("Successfully inserted Professional Journey section before SKILLS.")
else:
    print("ERROR: Could not find anchor '    <!-- SKILLS -->'")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
