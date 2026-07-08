import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# --- 1. Terminal Typing Runtime ---
# We replace the terminal body content with an empty div and add a script to type it out.
terminal_original = r'''          <div
            style="padding: 15px; font-family: 'IBM Plex Mono', monospace !important; font-size: 9px; line-height: 1.8; color: #421835;">
            <div style="color: #a4768f; margin-bottom: 2px;">~\$ whoami</div>
            <div style="font-weight: 600; margin-bottom: 12px;">designer\. builder\. problem-solver\.</div>
            <div style="color: #a4768f; margin-bottom: 2px;">~\$ focus</div>
            <div style="font-weight: 600; margin-bottom: 12px;">secure systems\. seamless experiences\.</div>
            <div style="color: #a4768f; margin-bottom: 2px;">~\$ status</div>
            <div style="font-weight: 600;"><span style="color: #421835; font-size: 10px;">●</span> building \| learning \|
              growing</div>
          </div>'''

terminal_new = '''          <div id="terminal-body"
            style="padding: 15px; font-family: 'IBM Plex Mono', monospace !important; font-size: 9px; line-height: 1.8; color: #421835; min-height: 140px;">
          </div>'''

content = re.sub(terminal_original, terminal_new, content, count=1)

# Add the script for typing effect right before </body>
typing_script = '''
  <style>
    @keyframes blinkCursor { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
    .cursor-blink { animation: blinkCursor 1s step-end infinite; color: #a4768f; }
  </style>
  <script>
    document.addEventListener("DOMContentLoaded", () => {
      const term = document.getElementById("terminal-body");
      if(term) {
        const lines = [
          { t: "~$ whoami", c: "cmd" },
          { t: "designer. builder. problem-solver.", c: "out" },
          { t: "~$ focus", c: "cmd" },
          { t: "secure systems. seamless experiences.", c: "out" },
          { t: "~$ status", c: "cmd" },
          { t: "● building | learning | growing", c: "out" }
        ];
        let lineIdx = 0;
        function typeLine() {
          if (lineIdx >= lines.length) {
            const cur = document.createElement("span");
            cur.className = "cursor-blink";
            cur.innerHTML = "█";
            term.appendChild(cur);
            return;
          }
          const l = lines[lineIdx];
          const div = document.createElement("div");
          if (l.c === "cmd") {
            div.style.color = "#a4768f"; div.style.marginBottom = "2px";
          } else {
            div.style.fontWeight = "600"; div.style.marginBottom = "12px";
          }
          term.appendChild(div);
          
          let charIdx = 0;
          function typeChar() {
            if(charIdx < l.t.length) {
              if (l.t.charAt(charIdx) === '●') {
                div.innerHTML += '<span style="color: #421835; font-size: 10px;">●</span>';
              } else {
                div.innerHTML += l.t.charAt(charIdx);
              }
              charIdx++;
              setTimeout(typeChar, 30 + Math.random() * 40);
            } else {
              lineIdx++;
              setTimeout(typeLine, 400);
            }
          }
          typeChar();
        }
        setTimeout(typeLine, 800);
      }
    });
  </script>
'''
content = content.replace('</body>', typing_script + '\n</body>')

# --- 2. Other Folders: Colors and 3D shadow ---
# Folder 1: #884d77 & #753c63 -> #60a5fa & #3b82f6
content = re.sub(r'fill="#884d77"', 'fill="#60a5fa"', content)
content = re.sub(r'fill="#753c63"', 'fill="#3b82f6"', content)

# Folder 2: #9e5684 & #a4768f -> #93c5fd & #60a5fa
content = re.sub(r'fill="#9e5684"', 'fill="#93c5fd"', content)
content = re.sub(r'fill="#a4768f"', 'fill="#60a5fa"', content)

# Folder 3: #602548 & #4f2940 -> #3b82f6 & #2563eb
content = re.sub(r'fill="#602548"', 'fill="#3b82f6"', content)
content = re.sub(r'fill="#4f2940"', 'fill="#2563eb"', content)

# Add 3D drop shadow to the folder SVGs
content = re.sub(
    r'(<svg width="34" height="28" viewBox="0 0 62 52" fill="none" xmlns="http://www.w3.org/2000/svg")',
    r'\g<1> style="filter: drop-shadow(3px 5px 6px rgba(37,99,235,0.5)) drop-shadow(-1px -1px 3px rgba(255,255,255,0.7));"',
    content
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updates applied: Terminal typing script added, sub-folders colored blue with 3D shadow.")
