with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_home = text.find('id="home"')
pos_home_end = text.find('</section>', pos_home)

home_content = text[pos_home:pos_home_end]

# Find last </div> before </section> in #home and remove the trailing duplicate </div>
pos_last_div = home_content.rfind('</div>')
if pos_last_div != -1:
    fixed_home_content = home_content[:pos_last_div] + home_content[pos_last_div+6:]
    text = text[:pos_home] + fixed_home_content + text[pos_home_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully fixed extra </div> in #home section!")
