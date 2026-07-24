import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make sure smriti-book-cover has both onclick and touch attributes / listeners
html = re.sub(
    r'id="smriti-book-cover"[^>]*>',
    'id="smriti-book-cover" class="cursor-pointer transition-all duration-500 z-40 group" onclick="openSmritiBook()" ontouchend="openSmritiBook()">',
    html
)

JOURNAL_SCRIPT = """
<!-- Physical Journal Open/Close & Touch Flip Script -->
<script>
  function openSmritiBook() {
    const coverView = document.getElementById('smriti-book-cover');
    const openedView = document.getElementById('smriti-book-opened');
    const spread1 = document.getElementById('smriti-spread-1');
    const spread2 = document.getElementById('smriti-spread-2');
    const spread3 = document.getElementById('smriti-spread-3');

    if (coverView && openedView) {
      coverView.style.transition = 'transform 0.8s cubic-bezier(0.645, 0.045, 0.355, 1), opacity 0.5s ease';
      coverView.style.transform = 'rotateY(-90deg) scale(0.95)';
      coverView.style.opacity = '0';

      setTimeout(() => {
        coverView.classList.add('hidden');
        openedView.classList.remove('hidden');
        if (spread1) spread1.classList.remove('hidden');
        if (spread2) spread2.classList.add('hidden');
        if (spread3) spread3.classList.add('hidden');

        openedView.style.opacity = '0';
        openedView.style.transform = 'scale(0.96)';

        setTimeout(() => {
          openedView.style.transition = 'all 0.6s ease';
          openedView.style.opacity = '1';
          openedView.style.transform = 'scale(1)';
        }, 40);
      }, 400);
    }
  }

  function closeSmritiBook() {
    const coverView = document.getElementById('smriti-book-cover');
    const openedView = document.getElementById('smriti-book-opened');

    if (coverView && openedView) {
      openedView.style.transition = 'all 0.5s ease';
      openedView.style.opacity = '0';
      openedView.style.transform = 'scale(0.96)';

      setTimeout(() => {
        openedView.classList.add('hidden');
        coverView.classList.remove('hidden');
        
        coverView.style.transform = 'rotateY(-90deg) scale(0.95)';
        coverView.style.opacity = '0';

        setTimeout(() => {
          coverView.style.transition = 'transform 0.8s cubic-bezier(0.645, 0.045, 0.355, 1), opacity 0.5s ease';
          coverView.style.transform = 'rotateY(0deg) scale(1)';
          coverView.style.opacity = '1';
        }, 40);
      }, 400);
    }
  }

  function switchSmritiSpread(targetId) {
    const spread1 = document.getElementById('smriti-spread-1');
    const spread2 = document.getElementById('smriti-spread-2');
    const spread3 = document.getElementById('smriti-spread-3');
    const btn1 = document.getElementById('tab-btn-spread1');
    const btn2 = document.getElementById('tab-btn-spread2');
    const btn3 = document.getElementById('tab-btn-spread3');

    const spreads = { 'spread1': spread1, 'spread2': spread2, 'spread3': spread3 };
    const btns = { 'spread1': btn1, 'spread2': btn2, 'spread3': btn3 };

    Object.keys(spreads).forEach(key => {
      if (spreads[key]) {
        if (key === targetId) {
          spreads[key].classList.remove('hidden');
          spreads[key].style.opacity = '1';
        } else {
          spreads[key].classList.add('hidden');
        }
      }
      if (btns[key]) {
        if (key === targetId) {
          btns[key].classList.remove('bg-[#B8929E]', 'bg-[#A67D88]', 'bg-[#7A364B]', 'bg-[#A36D7D]');
          btns[key].classList.add('bg-[#6B2137]');
        } else {
          btns[key].classList.remove('bg-[#6B2137]');
          btns[key].classList.add(key === 'spread2' ? 'bg-[#B8929E]' : 'bg-[#A67D88]');
        }
      }
    });
  }

  // Touch and click listener binding
  document.addEventListener('DOMContentLoaded', () => {
    const cover = document.getElementById('smriti-book-cover');
    if (cover) {
      cover.addEventListener('click', openSmritiBook);
      cover.addEventListener('touchend', (e) => {
        e.preventDefault();
        openSmritiBook();
      });
    }
  });
</script>
"""

# Insert before </section> of about-journal
pos_about_journal_end = html.find('</section>', html.find('id="about-journal"'))
if pos_about_journal_end != -1:
    html = html[:pos_about_journal_end] + JOURNAL_SCRIPT + '\n' + html[pos_about_journal_end:]
    print("Successfully attached journal open/close and touch flip script!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
