import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add CSS for CD spin and cute stars
style_block = """  <style>
    @keyframes spin {
      100% { transform: rotate(360deg); }
    }
    .spin-cd {
      animation: spin 10s linear infinite;
    }
  </style>

  <!-- Cute Star Cluster SVG Template -->
  <svg style="display:none;">
    <defs>
      <g id="icon-star-cluster">
        <!-- Main Star -->
        <path d="M12 2L14.4 9.6H22.4L16 14.4L18.4 22L12 17.2L5.6 22L8 14.4L1.6 9.6H9.6L12 2Z" fill="url(#star-grad)" />
        <!-- Top Small Star -->
        <path d="M6 1L6.6 3.2H9L7 4.6L7.8 7L6 5.6L4.2 7L5 4.6L3 3.2H5.4L6 1Z" fill="url(#star-grad)" transform="translate(6, -6) scale(0.6)" />
        <!-- Bottom Small Star -->
        <path d="M6 1L6.6 3.2H9L7 4.6L7.8 7L6 5.6L4.2 7L5 4.6L3 3.2H5.4L6 1Z" fill="url(#star-grad)" transform="translate(-10, 6) scale(0.8)" />
      </g>
      <linearGradient id="star-grad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#fcd34d" />
        <stop offset="100%" stop-color="#f59e0b" />
      </linearGradient>
    </defs>
  </svg>
"""

# Insert style block right after <section id="home"...>
content = re.sub(
    r'(<section id="home"[^>]*>)',
    r'\1\n' + style_block,
    content,
    count=1
)

# 2. Replace the text emojis with the SVG star cluster
content = re.sub(
    r'<div style="position: absolute;[^"]*font-size: \d+px; color: #a4768f;[^>]*>✨</div>',
    lambda m: m.group(0).replace('✨', '<svg style="width:32px; height:32px; filter: drop-shadow(0 2px 4px rgba(245,158,11,0.4));"><use href="#icon-star-cluster"/></svg>'),
    content
)

# Replace the text emoji heart with SVG heart (if any)
# I'll just leave the moon and heart text emojis as is, or replace them if they are stars.
# Let's replace the heart in "today's focus" with a nice SVG? No, user just said "instead of stars icon make sure to add the star".

# 3. Animate the CD
content = content.replace(
    '<img src="https://images.unsplash.com/photo-1603048588665-791ca8aea617?q=80&w=450" alt="Vinyl" style="width: 100%; height: 100%; object-fit: cover; filter: brightness(1.2);" />',
    '<img src="https://images.unsplash.com/photo-1603048588665-791ca8aea617?q=80&w=450" alt="Vinyl" style="width: 100%; height: 100%; object-fit: cover; filter: brightness(1.2);" class="spin-cd" />'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("CD spin animation and custom star SVG added successfully.")
