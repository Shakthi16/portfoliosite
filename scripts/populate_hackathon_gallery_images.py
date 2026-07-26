import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# 1. Update Gallery Mockups HTML section to give id="detail-gallery-grid"
old_gallery_html = '''<div class="grid grid-cols-3 gap-3 md:gap-4">
                <div
                  class="h-12 md:h-16 bg-zinc-900 border border-white/5 rounded-xl flex items-center justify-center opacity-40 hover:opacity-100 transition-opacity">
                  <i class="fas fa-image text-purple-500/50 text-sm md:text-base"></i>
                </div>
                <div
                  class="h-12 md:h-16 bg-zinc-900 border border-white/5 rounded-xl flex items-center justify-center opacity-40 hover:opacity-100 transition-opacity">
                  <i class="fas fa-file-code text-purple-500/50 text-sm md:text-base"></i>
                </div>
                <div
                  class="h-12 md:h-16 bg-zinc-900 border border-white/5 rounded-xl flex items-center justify-center opacity-40 hover:opacity-100 transition-opacity">
                  <i class="fas fa-shield-alt text-purple-500/50 text-sm md:text-base"></i>
                </div>
              </div>'''

new_gallery_html = '''<div class="grid grid-cols-3 gap-3 md:gap-4" id="detail-gallery-grid">
                <!-- Dynamically populated with real photos -->
              </div>'''

html = html.replace(old_gallery_html, new_gallery_html)

# 2. Add gallery image arrays to achData items
start_ach = html.find('const achData = [')
end_ach = html.find('];', start_ach)

if start_ach != -1 and end_ach != -1:
    ach_code = html[start_ach:end_ach + 2]

    # Add gallery array to Competition / Hackathon Winner (index 2)
    ach_code = ach_code.replace(
        'charImg: "hackathon.png",',
        'charImg: "hackathon.png",\n          gallery: ["vibe_hackathon_img_2.jpg", "vibe_hackathon_img_3.jpg", "vibe_hackathon_img_4.jpg"],'
    )
    # Add default gallery array to Research (index 0)
    ach_code = ach_code.replace(
        'charImg: "research.png",',
        'charImg: "research.png",\n          gallery: ["bg1.png", "cystar.webp"],'
    )
    # Add default gallery array to Patent (index 1)
    ach_code = ach_code.replace(
        'charImg: "patent.png",',
        'charImg: "patent.png",\n          gallery: ["patent.png"],'
    )
    # Add default gallery array to Best Outgoing Student (index 3)
    ach_code = ach_code.replace(
        'charImg: "beststudent.png",',
        'charImg: "beststudent.png",\n          gallery: ["beststudent.png"],'
    )

    html = html[:start_ach] + ach_code + html[end_ach + 2:]

# 3. Populate detail-gallery-grid dynamically in JS click handler
js_target = "metaList.appendChild(li);\n          });"
js_replacement = """metaList.appendChild(li);
          });

          // Populate gallery mockups dynamically with real photos
          const galleryGrid = document.getElementById('detail-gallery-grid');
          if (galleryGrid) {
            galleryGrid.innerHTML = '';
            if (data.gallery && data.gallery.length > 0) {
              data.gallery.forEach(imgSrc => {
                const thumb = document.createElement('div');
                thumb.className = 'h-16 md:h-20 bg-zinc-900 border border-white/20 rounded-xl overflow-hidden shadow-md cursor-pointer hover:border-purple-400 hover:scale-105 transition-all relative group';
                thumb.onclick = (e) => {
                  e.stopPropagation();
                  window.open(imgSrc, '_blank');
                };
                thumb.innerHTML = `<img src="${imgSrc}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-300" alt="Gallery Photo"/>
                                  <div class="absolute inset-0 bg-black/20 group-hover:bg-transparent transition-colors"></div>`;
                galleryGrid.appendChild(thumb);
              });
            } else {
              galleryGrid.innerHTML = '<p class="text-xs text-gray-500 italic">No additional gallery photos available</p>';
            }
          }"""

html = html.replace(js_target, js_replacement)

with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESSFULLY INTEGRATED LINKEDIN HACKATHON WINNER PHOTOS INTO GALLERY MOCKUPS!")
