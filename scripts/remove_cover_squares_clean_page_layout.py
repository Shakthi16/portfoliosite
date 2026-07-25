import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_pos = html.find('<!-- ==================== CLOSED BOOK COVER STATE (ROCK-SOLID STATIC 3D HARDCOVER) ==================== -->')
end_pos = html.find('<!-- ==================== OPENED PHYSICAL HARDCOVER BOOK (REALISTIC 3D PAGE STACK & SHADOW) ==================== -->', start_pos)

if start_pos != -1 and end_pos != -1:
    old_cover_html = html[start_pos:end_pos]

    # Clean closed cover without any awkward extra striped squares, keeping smooth rounded cover and satin gold ribbon
    clean_cover_html = '''<!-- ==================== CLOSED BOOK COVER STATE (CLEAN ELEGANT HARDCOVER) ==================== -->
      <div id="smriti-book-cover" class="cursor-pointer transition-all duration-300 z-40" onclick="openSmritiBook()">
        <div class="relative max-w-fit mx-auto">
          
          <!-- Main Hardcover Image Container (Clean rounded corners, soft shadow, zero shaking) -->
          <div class="w-[290px] md:w-[380px] h-[480px] md:h-[530px] rounded-[26px] shadow-[0_25px_55px_-10px_rgba(0,0,0,0.45),0_10px_25px_-5px_rgba(61,20,38,0.35)] overflow-hidden relative bg-[#3D1426] border-2 border-[#3D1426]/60">
            <img src="cover.png" alt="Shakthi Sri Journal Cover" class="w-full h-full object-cover block"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/25 via-transparent to-transparent pointer-events-none"></div>
          </div>

          <!-- Satin Gold Bookmark Ribbon Hanging Neatly at Bottom-Left -->
          <div class="w-6 h-11 bg-gradient-to-b from-[#C49A45] via-[#D4A359] to-[#A87D2A] rounded-b-md shadow-md border-b border-r border-amber-900/30 absolute -bottom-4 left-10 pointer-events-none z-50"></div>
        </div>
      </div>

      '''

    new_html = html[:start_pos] + clean_cover_html + html[end_pos:]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY REMOVED EXTRA SQUARES AND RESTORED CLEAN BOOK COVER LAYOUT!")
else:
    print("Failed to find cover section!")
