import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

new_home = """<section id="home" style="position: relative; overflow: hidden; height: 100vh; min-height: 700px; width: 100vw; background-color: #fdfaf8; background-image: linear-gradient(#f0e9e4 1px, transparent 1px), linear-gradient(90deg, #f0e9e4 1px, transparent 1px); background-size: 50px 50px;">

  <!-- Decorative Hand-drawn Elements (Static) -->
  <div style="position: absolute; top: 12%; left: 38%; font-size: 24px; color: #a4768f; transform: rotate(15deg); font-family: 'Great Vibes', cursive !important;">✨</div>
  <div style="position: absolute; bottom: 25%; right: 28%; font-size: 20px; color: #a4768f; transform: rotate(-10deg); font-family: 'Great Vibes', cursive !important;">✨</div>
  <div style="position: absolute; top: 30%; right: 30%; font-size: 28px; color: #a4768f; transform: rotate(5deg); font-family: 'Great Vibes', cursive !important;">✨</div>
  <div style="position: absolute; bottom: 15%; left: 45%; font-size: 22px; color: #a4768f; transform: rotate(45deg); font-family: 'Great Vibes', cursive !important;">✨</div>
  <div style="position: absolute; bottom: 35%; left: 28%; font-size: 20px; color: #a4768f; font-family: 'Cormorant Garamond', serif !important;">☾</div>
  <div style="position: absolute; top: 55%; right: 35%; font-size: 20px; color: #a4768f; font-family: 'Cormorant Garamond', serif !important;">♡</div>
  <div style="position: absolute; bottom: 25%; right: 18%; font-size: 28px; color: #a4768f; font-family: 'Great Vibes', cursive !important;">✨</div>

  <!-- CENTER TITLE (Static, purely in background) -->
  <div style="position: absolute; top: 48%; left: 50%; transform: translate(-50%, -50%); text-align: center; z-index: 1; width: 100%; pointer-events: none;">
    <h1 style="font-family: 'Brittany Signature', cursive !important; font-size: clamp(60px, 8.5vw, 120px); font-weight: 400; color: #421835; margin: 0; line-height: 1; text-shadow: 2px 2px 5px rgba(66, 24, 53, 0.1);">Shakthi Sri</h1>
    <div style="font-family: 'Manrope', sans-serif !important; font-size: clamp(9px, 1vw, 11px); font-weight: 700; letter-spacing: 0.5em; text-transform: uppercase; color: #582a4b; margin-top: 15px;">DESIGN &bull; SECURE &bull; EMPOWER</div>
    <div style="font-family: 'IBM Plex Mono', monospace !important; font-size: 9px; color: #7a3a5e; margin-top: 12px; letter-spacing: 0.05em; line-height: 1.6;">Crafting intuitive experiences.<br>Securing what matters.</div>
  </div>

  <!-- 1. ID CARD (Top Left Corner) -->
  <div class="floating-sticker" style="top: 1%; left: 1%; z-index: 10; transform: rotate(-5deg); scale: 0.8; transform-origin: top left;">
    <div style="position: absolute; top: -10px; left: 50%; transform: translateX(-50%) rotate(2deg); width: 80px; height: 25px; background: rgba(220, 200, 210, 0.9); box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-top: 1px solid rgba(255,255,255,0.5); z-index: 5;"></div>
    <div style="width: 210px; height: 320px; border-radius: 12px; padding: 25px 20px; display: flex; flex-direction: column; align-items: center; text-align: center; background: linear-gradient(135deg, #4b1a37, #2d1023); box-shadow: 0 15px 35px rgba(0,0,0,0.15); border: 1px solid rgba(255,255,255,0.1);">
      <div style="font-family: 'Manrope', sans-serif !important; font-weight: 600; font-size: 16px; color: #ebd5e0; margin-top: 10px;">Shakthi Sri</div>
      <div style="font-family: 'Manrope', sans-serif !important; font-weight: 500; font-size: 10px; margin-top: 6px; color: #c49eb3; line-height: 1.4;">UI/UX Designer<br/>Cybersecurity Enthusiast</div>
      <div style="width: 90px; height: 90px; border-radius: 50%; overflow: hidden; margin-top: 20px; border: 2px solid rgba(235, 213, 224, 0.4); box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
        <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&q=80" alt="Portrait" style="width: 100%; height: 100%; object-fit: cover;" />
      </div>
      <div style="font-family: 'IBM Plex Mono', monospace !important; font-size: 7px; margin-top: 30px; color: #a4768f; text-transform: uppercase; letter-spacing: 0.1em; line-height: 1.6;">
        Designing with purpose.<br/>Securing with impact.
      </div>
      <div style="color: #c49eb3; font-size: 10px; margin-top: 8px;">✦</div>
    </div>
  </div>

  <!-- 2. Desk Setup Image (Top Left, beside ID card) -->
  <div class="floating-sticker" style="top: 8%; left: 16%; z-index: 7; transform: rotate(3deg); scale: 0.85;">
    <div style="position: absolute; top: 10px; left: 10px; width: 14px; height: 14px; border-radius: 50%; background: #5B2C4A; box-shadow: inset -2px -2px 4px rgba(0,0,0,0.3); z-index: 10;"></div>
    <div class="polaroid-collage" style="width: 170px; padding: 10px 10px 24px; background: #fff; box-shadow: 0 8px 20px rgba(0,0,0,0.08);">
      <div style="width: 150px; height: 110px; overflow: hidden; background: #ddd;">
        <img src="https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?q=80&w=400" alt="Workspace" style="width: 100%; height: 100%; object-fit: cover;" />
      </div>
      <div style="position: absolute; bottom: 20%; left: 15%; width: 40px; height: 40px; background: url('https://images.unsplash.com/photo-1509042239860-f550ce710b93?q=80&w=100') center/cover; border-radius: 50%; border: 2px solid #fff; box-shadow: 0 4px 6px rgba(0,0,0,0.2);"></div>
    </div>
  </div>

  <!-- 3. "today's focus" Note (Pushed down and right to avoid ID card) -->
  <div class="floating-sticker" style="top: 36%; left: 12%; z-index: 8; transform: rotate(-2deg); scale: 0.85;">
    <div style="position: absolute; top: -5px; left: 50%; transform: translateX(-50%) rotate(-2deg); width: 60px; height: 20px; background: rgba(245, 235, 240, 0.85); box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-top: 1px solid rgba(255,255,255,0.5);"></div>
    <div class="torn-paper" style="width: 140px; padding: 25px 20px; background: #fff; box-shadow: 0 8px 15px rgba(0,0,0,0.05); border: 1px solid rgba(0,0,0,0.02); clip-path: polygon(0 0, 100% 0, 98% 100%, 0% 98%);">
      <div style="font-family: 'Brittany Signature', cursive !important; font-size: 24px; color: #421835; text-align: center; margin-bottom: 5px;">today's focus</div>
      <ul style="list-style: none; padding: 0; margin: 0; font-size: 11px; color: #582a4b; font-family: 'Manrope', sans-serif !important; line-height: 2;">
        <li>♡ design flow</li>
        <li>♡ threat hunting</li>
        <li>♡ final year project</li>
        <li>♡ user research</li>
        <li>♡ gym + reset</li>
      </ul>
    </div>
  </div>

  <!-- 4. Design Journey Ticket (Top Mid-Right) -->
  <div class="floating-sticker" style="top: 8%; right: 26%; z-index: 8; transform: rotate(2deg); scale: 0.85;">
    <div style="position: absolute; top: 10px; right: 10px; width: 14px; height: 14px; border-radius: 50%; background: #5B2C4A; box-shadow: inset -2px -2px 4px rgba(0,0,0,0.3); z-index: 10;"></div>
    <div class="ticket-pass" style="width: 270px; padding: 0; background: #fffafb; display: flex; box-shadow: 0 12px 30px rgba(0,0,0,0.06); border: 1px solid rgba(0,0,0,0.03); border-radius: 6px; overflow: hidden;">
      <div style="background: #a4768f; color: #fff; width: 35px; display: flex; align-items: center; justify-content: center; writing-mode: vertical-rl; transform: rotate(180deg); font-size: 9px; font-family: 'IBM Plex Mono', monospace !important; letter-spacing: 0.2em; padding: 15px 0;">all in progress</div>
      <div style="padding: 15px 20px; flex: 1;">
        <div style="font-size: 12px; font-weight: 700; color: #421835; font-family: 'Manrope', sans-serif !important; letter-spacing: 0.05em; margin-bottom: 6px;">DESIGN JOURNEY</div>
        <div style="font-size: 8px; font-weight: 600; color: #421835; font-family: 'IBM Plex Mono', monospace !important; letter-spacing: 0.05em;">UI/UX • PRODUCT • SECURITY</div>
        <div style="font-size: 10px; color: #7a3a5e; margin-top: 15px; font-family: 'Manrope', sans-serif !important; line-height: 1.5;">Turning complexity<br>into clarity.</div>
        <div style="margin-top: 15px; font-size: 8px; font-family: 'IBM Plex Mono', monospace !important; color: #7a3a5e; background: #f5ebf0; display: inline-block; padding: 5px 10px; border-radius: 12px; font-weight: 600;">EST. 2022 - PRESENT &nbsp; +</div>
      </div>
      <div style="border-left: 2px dashed #ebd5e0; width: 50px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: #fffafb;">
        <svg width="24" height="40" viewBox="0 0 28 60">
          <rect x="2" y="5" width="3" height="50" fill="#2d1023" />
          <rect x="7" y="5" width="2" height="50" fill="#2d1023" />
          <rect x="11" y="5" width="5" height="50" fill="#2d1023" />
          <rect x="18" y="5" width="2" height="50" fill="#2d1023" />
          <rect x="22" y="5" width="4" height="50" fill="#2d1023" />
        </svg>
        <span style="font-size: 8px; color: #7a3a5e; font-family: 'IBM Plex Mono', monospace !important; margin-top: 8px;">001</span>
      </div>
    </div>
  </div>

  <!-- 5. What Drives Me Note (Top Far Right - Perfect Padding) -->
  <div class="floating-sticker" style="top: 2%; right: 1%; z-index: 6; transform: rotate(-3deg); scale: 0.85;">
    <div style="position: absolute; top: 15px; right: 40%; transform: rotate(15deg); width: 45px; height: 16px; background: rgba(220, 200, 210, 0.9); box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-top: 1px solid rgba(255,255,255,0.5); z-index: 5;"></div>
    <div style="width: 320px; height: 320px; background: url('notes.png') center/contain no-repeat; padding: 75px 40px 30px 145px; box-sizing: border-box; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.05)); display: flex; flex-direction: column;">
      <div style="font-family: 'Brittany Signature', cursive !important; font-size: 26px; color: #421835; margin-bottom: 5px; text-align: left; text-shadow: 0 1px 2px rgba(255,255,255,0.5);">what drives me</div>
      <div style="font-size: 10px; color: #582a4b; font-family: 'Manrope', sans-serif !important; line-height: 2.2; text-align: left; padding-right: 10px; max-width: 140px;">
        I blend creativity with strategy, aesthetics with logic, and empathy with security — to build digital experiences that matter.
      </div>
    </div>
  </div>

  <!-- 6. GIRL.PNG (Placed next to 'Sri') -->
  <div class="floating-sticker" style="top: 40%; right: 22%; z-index: 10; transform: rotate(2deg);">
    <img src="girl.png" alt="Aesthetic Girl Illustration" style="width: 170px; opacity: 0.95; mix-blend-mode: multiply; pointer-events: none;" />
  </div>

  <!-- 7. "currently building" Pink Note (Bottom Mid-Left) -->
  <div class="floating-sticker" style="bottom: 30%; left: 3%; z-index: 9; transform: rotate(-5deg); scale: 0.8; transform-origin: bottom left;">
    <div style="position: absolute; top: 15px; right: 15px; font-size: 24px; color: #7a3a5e; opacity: 0.5; transform: rotate(15deg);">📎</div>
    <div style="width: 160px; padding: 25px; background: #ebd5e0; box-shadow: 0 8px 20px rgba(0,0,0,0.06); clip-path: polygon(0% 2%, 98% 0%, 100% 98%, 2% 100%);">
      <div style="font-family: 'Brittany Signature', cursive !important; font-size: 20px; color: #421835; text-align: center; margin-bottom: 5px;">currently building</div>
      <div style="font-family: 'Manrope', sans-serif !important; font-size: 11px; color: #582a4b; text-align: center; line-height: 1.8;">
        my future<br>one prototype,<br>one packet,<br>one step at a time.
      </div>
    </div>
  </div>

  <!-- 8. "LESSONS I'M STILL LEARNING" Note (Bottom Center-Left) -->
  <div class="floating-sticker" style="bottom: 15%; left: 18%; z-index: 7; transform: rotate(3deg); scale: 0.85;">
    <div style="width: 300px; height: 300px; background: url('notes1.png') center/contain no-repeat; padding: 60px 40px 40px 60px; box-sizing: border-box; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.05)); display: flex; flex-direction: column; align-items: center;">
      <div style="font-family: 'IBM Plex Mono', monospace !important; font-size: 9px; font-weight: 600; color: #7a3a5e; letter-spacing: 0.1em; line-height: 1.4; margin-bottom: 15px; text-align: left; width: 100%; max-width: 160px;">LESSONS I'M STILL<br>LEARNING</div>
      <ul style="list-style: none; padding: 0; margin: 0; font-size: 10px; color: #582a4b; font-family: 'Manrope', sans-serif !important; line-height: 1.8; text-align: left; width: 100%; max-width: 160px;">
        <li style="position: relative; padding-left: 10px; margin-bottom: 8px;"><span style="position: absolute; left: 0; top: 0; color: #421835;">•</span> not everything needs a solution</li>
        <li style="position: relative; padding-left: 10px; margin-bottom: 8px;"><span style="position: absolute; left: 0; top: 0; color: #421835;">•</span> it's okay to take breaks</li>
        <li style="position: relative; padding-left: 10px;"><span style="position: absolute; left: 0; top: 0; color: #421835;">•</span> balance is a continuous choice</li>
      </ul>
    </div>
  </div>

  <!-- 9. Terminal Window (Bottom Left) -->
  <div class="floating-sticker" style="bottom: 5%; left: 1%; z-index: 10; transform: rotate(-2deg); transform-origin: bottom left; scale: 0.85;">
    <div class="terminal-window" style="width: 240px; background: #fff; border-radius: 8px; box-shadow: 0 12px 30px rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.05); overflow: hidden;">
      <div style="padding: 10px 14px; background: #fdfaf8; border-bottom: 1px solid #f0e9e4; display: flex; align-items: center; justify-content: space-between;">
        <div style="display: flex; gap: 6px;">
          <span style="width: 8px; height: 8px; border-radius: 50%; background: #ff5f56; display: block;"></span>
          <span style="width: 8px; height: 8px; border-radius: 50%; background: #ffbd2e; display: block;"></span>
          <span style="width: 8px; height: 8px; border-radius: 50%; background: #27c93f; display: block;"></span>
        </div>
        <div style="font-family: 'IBM Plex Mono', monospace !important; font-size: 9px; color: #a4768f;">shakthi@journey:~</div>
      </div>
      <div style="padding: 15px; font-family: 'IBM Plex Mono', monospace !important; font-size: 9px; line-height: 1.8; color: #421835;">
        <div style="color: #a4768f; margin-bottom: 2px;">~$ whoami</div>
        <div style="font-weight: 600; margin-bottom: 12px;">designer. builder. problem-solver.</div>
        <div style="color: #a4768f; margin-bottom: 2px;">~$ focus</div>
        <div style="font-weight: 600; margin-bottom: 12px;">secure systems. seamless experiences.</div>
        <div style="color: #a4768f; margin-bottom: 2px;">~$ status</div>
        <div style="font-weight: 600;"><span style="color: #421835; font-size: 10px;">●</span> building | learning | growing</div>
      </div>
    </div>
  </div>

  <!-- 10. Dark Quote Note (Bottom Mid-Left) -->
  <div class="floating-sticker" style="bottom: 2%; left: 24%; z-index: 12; transform: rotate(4deg); transform-origin: bottom center; scale: 0.85;">
    <div style="position: absolute; top: -5px; left: 50%; transform: translateX(-50%); width: 45px; height: 14px; background: rgba(220, 200, 210, 0.9); box-shadow: 0 1px 3px rgba(0,0,0,0.1); z-index: 15;"></div>
    <div style="width: 140px; padding: 25px 20px; background: #4f2940; border-radius: 4px; box-shadow: 0 10px 25px rgba(0,0,0,0.15);">
      <div style="font-family: 'Manrope', sans-serif !important; font-size: 11px; font-weight: 500; line-height: 1.8; color: #fdfaf8; text-align: center;">
        "i design with empathy, i build with logic, i protect with purpose."
      </div>
      <div style="text-align: right; margin-top: 15px; font-family: 'Brittany Signature', cursive !important; font-size: 20px; color: #c49eb3;">- Shakthi Sri</div>
    </div>
  </div>

  <!-- 11. AGNI C2 Card (Bottom Center) -->
  <div class="floating-sticker" style="bottom: 2%; left: 38%; z-index: 9; transform: rotate(-1deg); transform-origin: bottom center; scale: 0.85;">
    <div style="width: 280px; padding: 25px; background: linear-gradient(135deg, #150912, #2d1023); border-radius: 12px; box-shadow: 0 20px 40px rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.05); position: relative; overflow: hidden;">
      <div style="position: absolute; top: 0; right: 0; width: 150px; height: 150px; background: radial-gradient(circle, rgba(251,113,133,0.15) 0%, transparent 70%); border-radius: 50%; filter: blur(20px);"></div>
      <div style="font-family: 'Manrope', sans-serif !important; font-size: 12px; font-weight: 700; color: #ebd5e0; letter-spacing: 0.05em; margin-bottom: 2px;">AGNI C2</div>
      <div style="font-family: 'IBM Plex Mono', monospace !important; font-size: 8px; color: #a4768f; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 15px;">COMMAND & CONTROL FRAMEWORK</div>
      <div style="display: flex; justify-content: space-between;">
        <ul style="list-style: none; padding: 0; margin: 0; font-family: 'Manrope', sans-serif !important; font-size: 9px; font-weight: 500; color: #d0b8c6; line-height: 2;">
          <li style="position: relative; padding-left: 10px;"><span style="position: absolute; left: 0; color: #fb7185;">•</span> Threat Simulation</li>
          <li style="position: relative; padding-left: 10px;"><span style="position: absolute; left: 0; color: #fb7185;">•</span> Real-time Monitoring</li>
          <li style="position: relative; padding-left: 10px;"><span style="position: absolute; left: 0; color: #fb7185;">•</span> Secure Communication</li>
          <li style="position: relative; padding-left: 10px;"><span style="position: absolute; left: 0; color: #fb7185;">•</span> Modular Architecture</li>
        </ul>
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-right: 10px;">
          <svg width="40" height="48" viewBox="0 0 24 24" fill="url(#agni-grad)" style="filter: drop-shadow(0 0 5px rgba(251,113,133,0.4));">
            <defs>
              <linearGradient id="agni-grad" x1="0%" y1="100%" x2="0%" y2="0%">
                <stop offset="0%" stop-color="#be123c" />
                <stop offset="50%" stop-color="#e11d48" />
                <stop offset="100%" stop-color="#fb7185" />
              </linearGradient>
            </defs>
            <path d="M12 23c-5.52 0-10-4.48-10-10 0-4.75 3.31-8.72 7.75-9.75-.41 1.25-.62 2.62-.62 4 0 4.14 3.36 7.5 7.5 7.5.38 0 .75-.03 1.12-.09C16.92 19.34 14.67 23 12 23zm-.5-21c0 3.31 2.69 6 6 6 .68 0 1.33-.11 1.94-.31C18.66 4.09 15.61 2 12.19 2c-.23 0-.46.01-.69.03V2z" />
          </svg>
          <div style="font-family: 'Manrope', sans-serif !important; font-size: 12px; font-weight: 700; color: #fb7185; letter-spacing: 0.1em; margin-top: 5px;">AGNI</div>
        </div>
      </div>
      <div style="margin-top: 10px; font-family: 'Manrope', sans-serif !important; font-size: 8px; font-weight: 600; color: #ebd5e0;">Final Year Project</div>
    </div>
  </div>

  <!-- 12. Tech Stack Grid (Bottom Center-Right) -->
  <div class="floating-sticker" style="bottom: 3%; right: 28%; z-index: 10; transform: rotate(1deg); transform-origin: bottom right; scale: 0.85;">
    <div style="position: absolute; top: -5px; left: 50%; transform: translateX(-50%); width: 14px; height: 14px; border-radius: 50%; background: #5B2C4A; box-shadow: inset -2px -2px 4px rgba(0,0,0,0.3); z-index: 10;"></div>
    <div style="width: 170px; padding: 25px 20px; background: #fff; border-radius: 12px; box-shadow: 0 15px 35px rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.02);">
      <div style="font-family: 'Manrope', sans-serif !important; font-size: 11px; font-weight: 800; color: #5B2C4A; text-transform: uppercase; letter-spacing: 0.1em; text-align: center; margin-bottom: 22px;">TECH STACK</div>
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px 15px; place-items: center;">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg" style="width: 22px; height: 22px; filter: drop-shadow(0px 4px 5px rgba(0,0,0,0.15));" />
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/photoshop/photoshop-original.svg" style="width: 22px; height: 22px; filter: drop-shadow(0px 4px 5px rgba(0,0,0,0.15)); border-radius: 4px;" />
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/illustrator/illustrator-plain.svg" style="width: 22px; height: 22px; filter: drop-shadow(0px 4px 5px rgba(0,0,0,0.15)); border-radius: 4px;" />
        
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" style="width: 22px; height: 22px; filter: drop-shadow(0px 4px 5px rgba(0,0,0,0.15));" />
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" style="width: 22px; height: 22px; filter: drop-shadow(0px 4px 5px rgba(0,0,0,0.15));" />
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" style="width: 22px; height: 22px; filter: drop-shadow(0px 4px 5px rgba(0,0,0,0.15)); border-radius: 4px;" />
        
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" style="width: 22px; height: 22px; filter: drop-shadow(0px 4px 5px rgba(0,0,0,0.15));" />
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg" style="width: 22px; height: 22px; filter: drop-shadow(0px 4px 5px rgba(0,0,0,0.15));" />
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" style="width: 22px; height: 22px; filter: drop-shadow(0px 4px 5px rgba(0,0,0,0.15));" />
        
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" style="width: 22px; height: 22px; filter: drop-shadow(0px 4px 5px rgba(0,0,0,0.15));" />
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" style="width: 22px; height: 22px; filter: drop-shadow(0px 4px 5px rgba(0,0,0,0.15)); border-radius: 4px;" />
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nextjs/nextjs-original.svg" style="width: 22px; height: 22px; filter: drop-shadow(0px 4px 5px rgba(0,0,0,0.15)); background: white; border-radius: 50%;" />
      </div>
    </div>
  </div>

  <!-- 13. MacPaint Palette (Moved slightly left of Tech Stack so it doesn't clip polaroids on right) -->
  <div class="floating-sticker" style="bottom: 5%; right: 40%; z-index: 200 !important; transform: rotate(0deg); scale: 0.8;">
    <div class="paint-palette">
      <div class="paint-palette-header">
        <div class="paint-palette-header-stripes"></div>
      </div>
      <div class="paint-tools-grid">
        <button class="paint-tool active-tool" data-tool="cursor" title="Select Tool"><i class="fas fa-mouse-pointer"></i></button>
        <button class="paint-tool" data-tool="pencil" title="Pencil (thin)"><i class="fas fa-pencil-alt"></i></button>
        <button class="paint-tool" data-tool="brush" title="Brush (thick)"><i class="fas fa-paint-brush"></i></button>
        <button class="paint-tool" data-tool="marker" title="Marker (highlight)">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor" style="display:inline-block; vertical-align:middle;"><path d="M20.71 7.04c.39-.39.39-1.04 0-1.41l-2.34-2.34c-.37-.39-1.02-.39-1.41 0l-1.84 1.83 3.75 3.75M3 17.25V21h3.75L17.81 9.93l-3.75-3.75L3 17.25z"/></svg>
        </button>
        <button class="paint-tool" data-tool="eraser" title="Eraser"><i class="fas fa-eraser"></i></button>
        <button class="paint-tool" data-tool="clear" title="Clear Canvas" style="color:#e11d48;"><i class="fas fa-trash-alt"></i></button>
      </div>
      <div class="paint-colors-grid">
        <span class="color-swatch active-color" data-color="#111111" style="background:#111111;" title="Black"></span>
        <span class="color-swatch" data-color="#ef4444" style="background:#ef4444;" title="Red"></span>
        <span class="color-swatch" data-color="#f59e0b" style="background:#f59e0b;" title="Amber"></span>
        <span class="color-swatch" data-color="#10b981" style="background:#10b981;" title="Green"></span>
        <span class="color-swatch" data-color="#3b82f6" style="background:#3b82f6;" title="Blue"></span>
        <span class="color-swatch" data-color="#a855f7" style="background:#a855f7;" title="Purple"></span>
        <span class="color-swatch" data-color="#ffffff" style="background:#ffffff; border: 1px solid #ccc;" title="White"></span>
        <span class="color-swatch" data-color="#64748b" style="background:#64748b;" title="Gray"></span>
      </div>
    </div>
  </div>

  <!-- 14. 3 Polaroids (Far Mid Right) -->
  <div class="floating-sticker" style="top: 35%; right: 2%; width: 220px; height: 300px; z-index: 10; scale: 0.85;">
    <!-- Purple pins -->
    <div class="polaroid-collage" style="position: absolute; top: 0; left: 0; transform: rotate(-8deg); width: 120px; padding: 8px 8px 25px; background: #fff; box-shadow: 0 8px 20px rgba(0,0,0,0.08); z-index: 1;">
      <div style="position: absolute; top: 5px; right: 10px; width: 10px; height: 10px; border-radius: 50%; background: #5B2C4A; box-shadow: inset -2px -2px 4px rgba(0,0,0,0.3); z-index: 10;"></div>
      <div style="width: 104px; height: 104px; overflow: hidden; background: #ddd;">
        <img src="https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=400" alt="Sky" style="width: 100%; height: 100%; object-fit: cover;" />
      </div>
    </div>
    <div class="polaroid-collage" style="position: absolute; top: 10px; right: 0; transform: rotate(12deg); width: 110px; padding: 8px 8px 25px; background: #fff; box-shadow: 0 8px 20px rgba(0,0,0,0.08); z-index: 2;">
      <div style="position: absolute; top: 5px; left: 10px; width: 10px; height: 10px; border-radius: 50%; background: #5B2C4A; box-shadow: inset -2px -2px 4px rgba(0,0,0,0.3); z-index: 10;"></div>
      <div style="width: 94px; height: 94px; overflow: hidden; background: #ddd;">
        <img src="https://images.unsplash.com/photo-1490750967868-88cb44cb271b?q=80&w=400" alt="Flowers" style="width: 100%; height: 100%; object-fit: cover;" />
      </div>
    </div>
    <div class="polaroid-collage" style="position: absolute; top: 110px; left: 10px; transform: rotate(-3deg); width: 120px; padding: 8px 8px 35px; background: #fff; box-shadow: 0 8px 20px rgba(0,0,0,0.1); z-index: 3;">
      <div style="width: 104px; height: 120px; overflow: hidden; background: #ddd;">
        <img src="https://images.unsplash.com/photo-1542841791-1925b02a2bf5?q=80&w=400" alt="Candle Desk" style="width: 100%; height: 100%; object-fit: cover;" />
      </div>
    </div>
    <div class="polaroid-collage" style="position: absolute; top: 140px; right: 10px; transform: rotate(5deg); width: 100px; padding: 8px 8px 30px; background: #fff; box-shadow: 0 8px 20px rgba(0,0,0,0.1); z-index: 4;">
      <div style="width: 84px; height: 100px; overflow: hidden; background: #111; position: relative;">
        <img src="https://images.unsplash.com/photo-1563241527-31df95e4e76a?q=80&w=400" alt="Neon Trust the Process" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8;" />
        <div style="position: absolute; top: 40%; left: 50%; transform: translate(-50%, -50%); color: #e879f9; font-family: 'Brittany Signature', cursive !important; font-size: 18px; text-shadow: 0 0 10px #e879f9; white-space: nowrap; text-align: center; line-height: 1.2;">trust<br>the<br>process</div>
      </div>
    </div>
  </div>

  <!-- 15. Music Player (Bottom Right, safely above vinyl) -->
  <div class="floating-sticker" style="bottom: 15%; right: 10%; z-index: 25; transform: rotate(-4deg); scale: 0.9;">
    <div style="width: 190px; padding: 20px; background: rgba(235, 213, 224, 0.85); backdrop-filter: blur(10px); border-radius: 12px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); border: 1px solid rgba(255,255,255,0.4);">
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
        <span style="font-size: 10px; font-weight: 700; color: #421835; font-family: 'Manrope', sans-serif !important;">Focus Mode</span>
        <div style="font-size: 12px; color: #421835;">♡</div>
      </div>
      <div style="font-size: 16px; font-weight: 700; font-family: 'Manrope', sans-serif !important; color: #421835; margin-bottom: 2px;">lofi beats</div>
      <div style="font-size: 11px; color: #7a3a5e; font-family: 'Manrope', sans-serif !important; margin-bottom: 18px;">study chill channel</div>
      <div style="display: flex; align-items: center; justify-content: space-between; padding: 0 10px; color: #421835; margin-top: 20px;">
        <i class="fas fa-backward" style="font-size: 14px; cursor: pointer;"></i>
        <i class="fas fa-pause" style="font-size: 20px; cursor: pointer;"></i>
        <i class="fas fa-forward" style="font-size: 14px; cursor: pointer;"></i>
      </div>
    </div>
  </div>

  <!-- 16. Interactive folder (Tucked behind Music Player on the left) -->
  <div class="floating-sticker" style="bottom: 12%; right: 22%; z-index: 12; transform: rotate(-3deg); scale: 0.7;">
    <div class="master-folder-container hoverable" id="interactive-folders-wrapper">
      <a href="#projects" class="sub-folder-item" style="text-decoration: none;">
        <svg width="34" height="28" viewBox="0 0 62 52" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M4 9C4 6.8 5.8 5 8 5H22L27 12H54C56.2 12 58 13.8 58 16V43C58 45.2 56.2 47 54 47H8C5.8 47 4 45.2 4 43V9Z" fill="#884d77"/>
          <path d="M4 16H58V43C58 45.2 56.2 47 54 47H8C5.8 47 4 45.2 4 43V16Z" fill="#753c63"/>
        </svg>
        <span class="sub-folder-label" style="color: #421835;">cyber labs 🔒</span>
      </a>
      <a href="#about" class="sub-folder-item" style="text-decoration: none;">
        <svg width="34" height="28" viewBox="0 0 62 52" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M4 9C4 6.8 5.8 5 8 5H22L27 12H54C56.2 12 58 13.8 58 16V43C58 45.2 56.2 47 54 47H8C5.8 47 4 45.2 4 43V9Z" fill="#9e5684"/>
          <path d="M4 16H58V43C58 45.2 56.2 47 54 47H8C5.8 47 4 45.2 4 43V16Z" fill="#a4768f"/>
        </svg>
        <span class="sub-folder-label" style="color: #421835;">brain dumps ✩</span>
      </a>
      <a href="#skills" class="sub-folder-item" style="text-decoration: none;">
        <svg width="34" height="28" viewBox="0 0 62 52" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M4 9C4 6.8 5.8 5 8 5H22L27 12H54C56.2 12 58 13.8 58 16V43C58 45.2 56.2 47 54 47H8C5.8 47 4 45.2 4 43V9Z" fill="#602548"/>
          <path d="M4 16H58V43C58 45.2 56.2 47 54 47H8C5.8 47 4 45.2 4 43V16Z" fill="#4f2940"/>
        </svg>
        <span class="sub-folder-label" style="color: #421835;">inspiration ♡</span>
      </a>
      <div class="master-folder-3d-icon" style="width: 70px; height: 60px;">
        <svg width="70" height="60" viewBox="0 0 120 100" fill="none" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="folder-front-grad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#9e5684" />
              <stop offset="100%" stop-color="#7a3a5e" />
            </linearGradient>
            <linearGradient id="folder-back-grad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#7a3a5e" />
              <stop offset="100%" stop-color="#421835" />
            </linearGradient>
          </defs>
          <path d="M10 20 C10 17 13 15 16 15H42L49 22H104 C107 22 110 25 110 28V78 C110 81 107 83 104 83H16 C13 83 10 81 10 78V20Z" fill="url(#folder-back-grad)" />
          <g class="folder-papers-group">
            <rect x="22" y="10" width="76" height="56" rx="3" fill="#fdfaf8" transform="rotate(-1 22 10)" />
            <rect x="28" y="7" width="68" height="56" rx="3" fill="#ffffff" opacity="0.95" transform="rotate(2 28 7)" />
          </g>
          <path d="M10 32 L10 80 C10 83 13 85 16 85H104 C107 85 110 83 110 80 L110 36 C110 33 107 31 104 31H54 L46 25 H16 C13 25 10 28 10 32Z" fill="url(#folder-front-grad)" />
          <rect x="26" y="46" width="35" height="14" rx="2" fill="#ffffff" opacity="0.3" />
        </svg>
      </div>
    </div>
  </div>

  <!-- 17. Vinyl Record (Pushed fully up so it is completely visible in the bottom right corner) -->
  <div class="floating-sticker" style="bottom: -2%; right: -2%; z-index: 5; transform: rotate(15deg); scale: 0.85;">
    <div style="width: 250px; height: 250px; border-radius: 50%; box-shadow: 0 15px 40px rgba(0,0,0,0.15); overflow: hidden; position: relative;">
      <img src="https://images.unsplash.com/photo-1603048588665-791ca8aea617?q=80&w=450" alt="Vinyl" style="width: 100%; height: 100%; object-fit: cover; filter: brightness(1.2);" />
      <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 80px; height: 80px; background: #8a3359; border: 4px solid #4f2940; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
        <div style="width: 12px; height: 12px; background: #fff; border-radius: 50%;"></div>
      </div>
    </div>
  </div>

  <canvas id="drawing-canvas" style="position: absolute; inset: 0; z-index: 100; pointer-events: none;"></canvas>

</section>
"""

updated_content = re.sub(r'<section id="home".*?</section>', new_home, content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(updated_content)

print("Home layout refactored: floating animation removed, vinyl pulled fully onto screen, overlapping issues fixed.")
