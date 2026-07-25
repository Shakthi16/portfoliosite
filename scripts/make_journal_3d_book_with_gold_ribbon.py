import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

start_pos = html.find('<!-- ==================== CLOSED BOOK COVER STATE ==================== -->')
end_pos = html.find('<!-- HARDCOVER FRAME: BURGUNDY #3D1426 MARGIN ENCLOSING PAGES -->', start_pos)

if start_pos != -1 and end_pos != -1:
    old_cover_html = html[start_pos:end_pos]

    # Replace closed cover & open hardcover frame with 3D stacked paper page edges, realistic shadow, and warm gold satin ribbon
    new_cover_html = '''<!-- ==================== CLOSED BOOK COVER STATE (3D REALISTIC HARDCOVER & PAPER STACK) ==================== -->
      <div id="smriti-book-cover" class="cursor-pointer transition-all duration-500 z-40 group" onclick="openSmritiBook()">
        <div class="relative">
          
          <!-- Stacked Paper Pages Edge 3 (Bottom Layer) -->
          <div class="absolute inset-0 bg-[#E8DEC8] rounded-[26px] translate-x-3 translate-y-3 shadow-md border border-amber-900/15"></div>

          <!-- Stacked Paper Pages Edge 2 (Middle Layer - Paper stack look) -->
          <div class="absolute inset-0 bg-[#FAF5EC] rounded-[26px] translate-x-1.5 translate-y-1.5 shadow-md border-r-2 border-b-2 border-amber-900/15"></div>

          <!-- Cover Hardcover Front (Top Layer with Deep 3D Shadow) -->
          <div class="w-[290px] md:w-[380px] h-[480px] md:h-[530px] rounded-[26px] shadow-[0_30px_70px_-15px_rgba(0,0,0,0.55),0_15px_30px_-5px_rgba(61,20,38,0.45)] overflow-hidden relative bg-[#3D1426] border-2 border-[#3D1426]/60 transition-transform duration-300 group-hover:-translate-y-1.5">
            <img src="cover.png" alt="Shakthi Sri Journal Cover" class="w-full h-full object-cover block"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/30 via-transparent to-transparent pointer-events-none"></div>
          </div>

          <!-- Satin Gold Bookmark Ribbon (Matching Burgundy & Gold Journal Theme) -->
          <div class="w-6 h-12 bg-gradient-to-b from-[#C49A45] via-[#D4A359] to-[#B38734] rounded-b-md shadow-lg border-b border-r border-amber-900/30 absolute -bottom-5 left-10 pointer-events-none z-50"></div>
        </div>
      </div>

      <!-- ==================== OPENED PHYSICAL HARDCOVER BOOK (REALISTIC 3D PAGE STACK & SHADOW) ==================== -->
      <div id="smriti-book-opened" class="hidden w-full transition-opacity duration-500 opacity-0 z-30">
        
        <!-- HARDCOVER FRAME: BURGUNDY #3D1426 MARGIN WITH 3D DEEP SHADOW & STACKED PAPER EDGES -->
        <div class="relative w-full max-w-[890px] mx-auto rounded-[22px] p-1.5 md:p-2 shadow-[0_35px_80px_-15px_rgba(0,0,0,0.5),0_15px_35px_-8px_rgba(61,20,38,0.4)] border-2 border-[#3D1426]/80 bg-[#3D1426]">
          
          <!-- Stacked Paper Edges (Left & Right Hardcover Borders) -->
          <div class="absolute -left-1 top-4 bottom-4 w-1 bg-[#E8DEC8] rounded-l-xs opacity-70"></div>
          <div class="absolute -right-1 top-4 bottom-4 w-1 bg-[#E8DEC8] rounded-r-xs opacity-70"></div>

'''

    new_html = html[:start_pos] + new_cover_html + html[end_pos:]

    with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESSFULLY APPLIED 3D REALISTIC PAPER STACK LOOK, SHADOW, AND SATIN GOLD RIBBON!")
else:
    print("Failed to find cover section!")
