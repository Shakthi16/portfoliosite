import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Locate and remove the GSAP parallax section
start_match = re.search(r'<!-- ════════ GSAP PARALLAX INTRO SEQUENCE ════════ -->', content)
if start_match:
    end_match = re.search(r'</script>', content[start_match.start():])
    if end_match:
        start_idx = start_match.start()
        end_idx = start_idx + end_match.end()
        
        # Remove the section completely
        updated_content = content[:start_idx] + content[end_idx:]
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("GSAP Parallax Intro successfully removed!")
    else:
        print("Could not find end of script.")
else:
    print("Could not find the GSAP parallax section.")
