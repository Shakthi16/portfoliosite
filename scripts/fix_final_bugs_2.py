import re
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Contact Page Hover Effect (Restore old Shaping Tomorrow style)
old_contact_h2 = r'<h2 id="flowing-text".*?SHAKTHI SRI T S\s*</h2>'
new_contact_h2 = r'''<h2 id="flowing-text" class="contact-bg-text select-none text-center tracking-tighter w-full" style="background-image: url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2000&auto=format&fit=crop'); background-size: 150%; background-position: 50% 50%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; transition: background-position 0.2s ease-out;">
            SHAKTHI SRI T S
          </h2>'''
html = re.sub(old_contact_h2, new_contact_h2, html, flags=re.DOTALL)

# 2. Fix the arrows missing issue (Wait for images to load + delay)
# Find the event listener block for DOMContentLoaded and add load events
old_js_start = r'document.addEventListener("DOMContentLoaded", \(\) => \{'
new_js_start = r'''document.addEventListener("DOMContentLoaded", () => {
    window.addEventListener("load", () => { if(typeof drawPaths === 'function') drawPaths(); });
    setTimeout(() => { if(typeof drawPaths === 'function') drawPaths(); }, 500);
    setTimeout(() => { if(typeof drawPaths === 'function') drawPaths(); }, 2000);'''
html = html.replace(old_js_start, new_js_start)

# 3. Modify the drawPaths function to handle 0 height elements better, just in case
# Also, remove the gsap strokeDashoffset hiding initially, so if ScrollTrigger fails, they are still visible.
# Find the gsap.set and gsap.to block
old_gsap_block = r'''               gsap.set\(p, \{ strokeDasharray: length, strokeDashoffset: length \}\);

               gsap.to\(p, \{
                   strokeDashoffset: 0,'''

new_gsap_block = r'''               gsap.set(p, { strokeDasharray: length, strokeDashoffset: length });

               gsap.to(p, {
                   strokeDashoffset: 0,'''

# Let's just fix the bounding client rect issue directly.
# Replace points calculation
old_points = r'''                   points.push\(\{
                       x: rect.left - containerRect.left \+ rect.width / 2,
                       y: rect.top - containerRect.top \+ rect.height / 2,
                       w: rect.width,
                       h: rect.height,
                       top: rect.top - containerRect.top,
                       left: rect.left - containerRect.left,
                       right: rect.right - containerRect.left,
                       bottom: rect.bottom - containerRect.top
                   \}\);'''
                   
new_points = r'''                   // Fallback for image loading dimensions
                   let h = rect.height || 300;
                   points.push({
                       x: rect.left - containerRect.left + rect.width / 2,
                       y: rect.top - containerRect.top + h / 2,
                       w: rect.width,
                       h: h,
                       top: rect.top - containerRect.top,
                       left: rect.left - containerRect.left,
                       right: rect.right - containerRect.left,
                       bottom: rect.top - containerRect.top + h
                   });'''
html = re.sub(old_points, new_points, html)

# Just to be absolutely safe, let's remove the initial strokeDashoffset hiding if scrollTrigger isn't working
# Actually, I'll just change the start trigger to "top 85%" so it activates earlier when scrolling
html = html.replace('start: "top 60%"', 'start: "top 85%"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Applied final fixes to arrows and text mask!")
