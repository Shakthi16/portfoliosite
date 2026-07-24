import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Define the new HTML for the home section
new_home = """<section id="home" style="position: relative; overflow: hidden; height: 100vh; min-height: 800px; width: 100vw; background-color: #fdfaf8; background-image: linear-gradient(#f0e9e4 1px, transparent 1px), linear-gradient(90deg, #f0e9e4 1px, transparent 1px); background-size: 50px 50px;">

  <!-- Decorative Hand-drawn Elements -->
  <div style="position: absolute; top: 12%; left: 38%; font-size: 24px; color: #a4768f; transform: rotate(15deg); font-family: 'Great Vibes', cursive;">✨</div>
  <div style="position: absolute; bottom: 25%; right: 28%; font-size: 20px; color: #a4768f; transform: rotate(-10deg); font-family: 'Great Vibes', cursive;">✨</div>
  <div style="position: absolute; top: 30%; right: 30%; font-size: 28px; color: #a4768f; transform: rotate(5deg); font-family: 'Great Vibes', cursive;">✨</div>
  <div style="position: absolute; bottom: 15%; left: 45%; font-size: 22px; color: #a4768f; transform: rotate(45deg); font-family: 'Great Vibes', cursive;">✨</div>
  <div style="position: absolute; bottom: 35%; left: 28%; font-size: 20px; color: #a4768f; font-family: 'Cormorant Garamond', serif;">☾</div>
  <div style="position: absolute; top: 55%; right: 35%; font-size: 20px; color: #a4768f; font-family: 'Cormorant Garamond', serif;">♡</div>
  <div style="position: absolute; bottom: 25%; right: 18%; font-size: 28px; color: #a4768f; font-family: 'Great Vibes', cursive;">✨</div>

  <!-- CENTER TITLE -->
  <div style="position: absolute; top: 46%; left: 50%; transform: translate(-50%, -50%); text-align: center; z-index: 1; width: 100%;">
    <h1 style="font-family: 'Alex Brush', cursive; font-size: clamp(80px, 9vw, 130px); font-weight: 400; color: #421835; margin: 0; line-height: 1;">Shakthi Sri</h1>
    <div style="font-family: 'Manrope', sans-serif; font-size: clamp(10px, 1.2vw, 14px); font-weight: 700; letter-spacing: 0.5em; text-transform: uppercase; color: #582a4b; margin-top: 25px;">DESIGN &bull; SECURE &bull; EMPOWER</div>
    <div style="font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: #7a3a5e; margin-top: 15px; letter-spacing: 0.05em; line-height: 1.6;">Crafting intuitive experiences.<br>Securing what matters.</div>
  </div>

  <!-- 1. ID CARD (Top Left) -->
  <div class="floating-sticker" style="top: -2%; left: 2%; z-index: 10; transform: rotate(-5deg);">
    <!-- Lanyard -->
    <div style="position: absolute; top: -100px; left: 50%; transform: translateX(-50%); width: 25px; height: 120px; background: #38102d; border-radius: 4px; z-index: -1;"></div>
    <div style="position: absolute; top: -10px; left: 50%; transform: translateX(-50%); width: 40px; height: 25px; background: #e2d1db; border-radius: 8px; border: 2px solid #bba3b2; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"></div>
    <div style="position: absolute; top: 12px; left: 50%; transform: translateX(-50%); width: 15px; height: 15px; background: #d0b8c6; border-radius: 50%; box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);"></div>
    
    <div style="width: 230px; height: 340px; border-radius: 12px; padding: 25px 20px; display: flex; flex-direction: column; align-items: center; text-align: center; background: linear-gradient(135deg, #4b1a37, #2d1023); box-shadow: 0 15px 35px rgba(0,0,0,0.15); border: 1px solid rgba(255,255,255,0.1); margin-top: 20px;">
      <div style="font-family: 'Manrope', sans-serif; font-weight: 600; font-size: 17px; color: #ebd5e0; margin-top: 15px;">Shakthi Sri</div>
      <div style="font-family: 'Manrope', sans-serif; font-weight: 500; font-size: 11px; margin-top: 6px; color: #c49eb3; line-height: 1.4;">UI/UX Designer<br/>Cybersecurity Enthusiast</div>
      
      <div style="width: 100px; height: 100px; border-radius: 50%; overflow: hidden; margin-top: 20px; border: 2px solid rgba(235, 213, 224, 0.4); box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
        <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&q=80" alt="Portrait" style="width: 100%; height: 100%; object-fit: cover;" />
      </div>
      
      <div style="font-family: 'IBM Plex Mono', monospace; font-size: 8px; margin-top: 40px; color: #a4768f; text-transform: uppercase; letter-spacing: 0.1em; line-height: 1.6;">
        Designing with purpose.<br/>Securing with impact.
      </div>
      <div style="color: #c49eb3; font-size: 10px; margin-top: 8px;">✦</div>
    </div>
  </div>

  <!-- 2. Desk Setup Image (Top Mid-Left) -->
  <div class="floating-sticker" style="top: 8%; left: 18%; z-index: 7; transform: rotate(2deg);">
    <div style="position: absolute; top: 10px; left: 10px; width: 14px; height: 14px; border-radius: 50%; background: #8a3359; box-shadow: inset -2px -2px 4px rgba(0,0,0,0.3); z-index: 10;"></div>
    <div class="polaroid-collage" style="width: 220px; padding: 10px 10px 24px; background: #fff; box-shadow: 0 8px 20px rgba(0,0,0,0.08);">
      <div style="width: 200px; height: 160px; overflow: hidden; background: #ddd;">
        <img src="https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?w=400&q=80" alt="Workspace" style="width: 100%; height: 100%; object-fit: cover;" />
      </div>
      <!-- Coffee mug on the desk -->
      <div style="position: absolute; bottom: 20%; left: 15%; width: 50px; height: 50px; background: url('https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=100&q=80') center/cover; border-radius: 50%; border: 2px solid #fff; box-shadow: 0 4px 6px rgba(0,0,0,0.2);"></div>
    </div>
  </div>

  <!-- 3. "Today's focus" Note (Top Middle) -->
  <div class="floating-sticker" style="top: 15%; left: 32%; z-index: 8; transform: rotate(-3deg);">
    <!-- Washi tape -->
    <div style="position: absolute; top: -5px; left: 50%; transform: translateX(-50%) rotate(-2deg); width: 60px; height: 20px; background: rgba(245, 235, 240, 0.85); box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-top: 1px solid rgba(255,255,255,0.5);"></div>
    <div class="torn-paper" style="width: 160px; padding: 25px 20px; background: #fff; box-shadow: 0 8px 15px rgba(0,0,0,0.05); border: 1px solid rgba(0,0,0,0.02); clip-path: polygon(0 0, 100% 0, 98% 100%, 0% 98%);">
      <div style="font-family: 'Alex Brush', cursive; font-size: 20px; color: #421835; text-align: center; margin-bottom: 15px;">today's focus</div>
      <ul style="list-style: none; padding: 0; margin: 0; font-size: 11px; color: #582a4b; font-family: 'Manrope', sans-serif; line-height: 2;">
        <li><span style="font-size: 10px; margin-right: 6px;">♡</span> design flow</li>
        <li><span style="font-size: 10px; margin-right: 6px;">♡</span> threat hunting</li>
        <li><span style="font-size: 10px; margin-right: 6px;">♡</span> final year project</li>
        <li><span style="font-size: 10px; margin-right: 6px;">♡</span> user research</li>
        <li><span style="font-size: 10px; margin-right: 6px;">♡</span> gym + reset</li>
      </ul>
      <div style="position: absolute; bottom: 15px; right: 15px; font-size: 14px; color: #a4768f; font-family: 'Cormorant Garamond', serif;">♡</div>
    </div>
  </div>

  <!-- 4. Design Journey Ticket (Top Right Center) -->
  <div class="floating-sticker" style="top: 6%; right: 26%; z-index: 8; transform: rotate(1deg);">
    <!-- Pink Pin -->
    <div style="position: absolute; top: 10px; left: 10px; width: 14px; height: 14px; border-radius: 50%; background: #a4768f; box-shadow: inset -2px -2px 4px rgba(0,0,0,0.2); z-index: 10;"></div>
    <div class="ticket-pass" style="width: 320px; padding: 0; background: #fffafb; display: flex; box-shadow: 0 12px 30px rgba(0,0,0,0.06); border: 1px solid rgba(0,0,0,0.03); border-radius: 6px; overflow: hidden;">
      <div style="background: #a4768f; color: #fff; width: 40px; display: flex; align-items: center; justify-content: center; writing-mode: vertical-rl; transform: rotate(180deg); font-size: 10px; font-family: 'IBM Plex Mono', monospace; letter-spacing: 0.2em; padding: 15px 0;">
        all in progress
      </div>
      <div style="padding: 20px 25px; flex: 1;">
        <div style="font-size: 13px; font-weight: 700; color: #421835; font-family: 'Manrope', sans-serif; letter-spacing: 0.05em; margin-bottom: 6px;">DESIGN JOURNEY</div>
        <div style="font-size: 9px; font-weight: 600; color: #421835; font-family: 'IBM Plex Mono', monospace; letter-spacing: 0.05em;">UI/UX • PRODUCT • SECURITY</div>
        <div style="font-size: 11px; color: #7a3a5e; margin-top: 15px; font-family: 'Manrope', sans-serif; line-height: 1.5;">Turning complexity<br>into clarity.</div>
        <div style="margin-top: 15px; font-size: 9px; font-family: 'IBM Plex Mono', monospace; color: #7a3a5e; background: #f5ebf0; display: inline-block; padding: 5px 10px; border-radius: 12px; font-weight: 600; letter-spacing: 0.05em;">EST. 2022 - PRESENT &nbsp; +</div>
      </div>
      <div style="border-left: 2px dashed #ebd5e0; width: 60px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: #fffafb;">
        <svg width="24" height="40" viewBox="0 0 28 60">
          <rect x="2" y="5" width="3" height="50" fill="#2d1023" />
          <rect x="7" y="5" width="2" height="50" fill="#2d1023" />
          <rect x="11" y="5" width="5" height="50" fill="#2d1023" />
          <rect x="18" y="5" width="2" height="50" fill="#2d1023" />
          <rect x="22" y="5" width="4" height="50" fill="#2d1023" />
        </svg>
        <span style="font-size: 9px; color: #7a3a5e; font-family: 'IBM Plex Mono', monospace; margin-top: 8px;">001</span>
      </div>
    </div>
  </div>

  <!-- 5. What Drives Me Note (Top Right) -->
  <div class="floating-sticker" style="top: 5%; right: 7%; z-index: 7; transform: rotate(-2deg);">
    <div style="width: 230px; padding: 25px; background: #fdfaf8; box-shadow: 0 8px 20px rgba(0,0,0,0.06); border: 1px solid rgba(0,0,0,0.04); clip-path: polygon(2% 0, 100% 2%, 98% 100%, 0% 98%);">
      <div style="font-family: 'Alex Brush', cursive; font-size: 22px; color: #421835; margin-bottom: 15px;">what drives me</div>
      <div style="font-size: 13px; color: #582a4b; font-family: 'Manrope', sans-serif; line-height: 1.8;">
        I blend creativity with strategy, aesthetics with logic, and empathy with security — to build digital experiences that matter.
      </div>
      <div style="position: absolute; bottom: 20px; right: 20px; font-size: 14px; color: #a4768f;">♡</div>
    </div>
  </div>

  <!-- 6. Pink Flower Branch (Top Right Corner) -->
  <div class="floating-sticker" style="top: 2%; right: -2%; z-index: 10; transform: rotate(15deg);">
    <div style="position: absolute; top: 70%; left: 40%; width: 45px; height: 16px; background: rgba(235, 190, 205, 0.8); transform: rotate(-25deg); box-shadow: 0 1px 3px rgba(0,0,0,0.1); z-index: 12;"></div>
    <img src="https://images.unsplash.com/photo-1579244033284-9a84a6fb7b3c?w=300&q=80" alt="Flowers" style="width: 180px; filter: contrast(1.1) brightness(1.1) sepia(0.2) hue-rotate(-20deg); mix-blend-mode: multiply; pointer-events: none;" />
  </div>

  <!-- 7. "currently building" Pink Note (Mid Left) -->
  <div class="floating-sticker" style="top: 48%; left: 3%; z-index: 9; transform: rotate(-4deg);">
    <div style="position: absolute; top: 20px; right: 15px; font-size: 24px; color: #7a3a5e; opacity: 0.5; transform: rotate(15deg);">📎</div>
    <div style="width: 200px; padding: 25px; background: #ebd5e0; box-shadow: 0 8px 20px rgba(0,0,0,0.06); clip-path: polygon(0% 2%, 98% 0%, 100% 98%, 2% 100%);">
      <div style="font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 18px; font-weight: 600; color: #421835; text-align: center; margin-bottom: 12px;">currently building</div>
      <div style="font-family: 'Manrope', sans-serif; font-size: 12px; color: #582a4b; text-align: center; line-height: 1.8;">
        my future<br>
        one prototype,<br>
        one packet,<br>
        one step at a time.
      </div>
      <div style="text-align: center; margin-top: 15px; font-size: 14px; color: #7a3a5e;">♡</div>
    </div>
  </div>

  <!-- 8. "LESSONS I'M STILL LEARNING" White Note (Mid Center-Left) -->
  <div class="floating-sticker" style="top: 42%; left: 20%; z-index: 7; transform: rotate(2deg);">
    <div style="position: absolute; top: -8px; left: 50%; transform: translateX(-50%); width: 45px; height: 16px; background: rgba(245, 235, 240, 0.9); box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-top: 1px solid rgba(255,255,255,0.5);"></div>
    <div style="width: 170px; padding: 30px 20px; background: #fff; box-shadow: 0 8px 15px rgba(0,0,0,0.05); border: 1px solid rgba(0,0,0,0.02);">
      <div style="font-family: 'IBM Plex Mono', monospace; font-size: 10px; font-weight: 600; color: #7a3a5e; letter-spacing: 0.1em; line-height: 1.4; margin-bottom: 20px;">LESSONS I'M STILL<br>LEARNING</div>
      <ul style="list-style: none; padding: 0; margin: 0; font-size: 10px; color: #582a4b; font-family: 'Manrope', sans-serif; line-height: 2;">
        <li style="position: relative; padding-left: 10px; margin-bottom: 10px;"><span style="position: absolute; left: 0; top: 0; color: #421835;">•</span> not everything<br>&nbsp;&nbsp;needs a solution</li>
        <li style="position: relative; padding-left: 10px; margin-bottom: 10px;"><span style="position: absolute; left: 0; top: 0; color: #421835;">•</span> it's okay to take<br>&nbsp;&nbsp;breaks</li>
        <li style="position: relative; padding-left: 10px;"><span style="position: absolute; left: 0; top: 0; color: #421835;">•</span> balance is a<br>&nbsp;&nbsp;continuous choice</li>
      </ul>
      <div style="position: absolute; bottom: 15px; right: 15px; font-size: 18px; color: #a4768f; font-family: 'Cormorant Garamond', serif;">☾</div>
    </div>
  </div>

  <!-- 9. 3 Polaroids (Mid Right) -->
  <div class="floating-sticker" style="top: 32%; right: 5%; width: 280px; height: 320px; z-index: 10;">
    
    <!-- Moon Sky (Top Left) -->
    <div class="polaroid-collage" style="position: absolute; top: 0; left: 0; transform: rotate(-8deg); width: 140px; padding: 8px 8px 25px; background: #fff; box-shadow: 0 8px 20px rgba(0,0,0,0.08); z-index: 1;">
      <div style="width: 124px; height: 124px; overflow: hidden; background: #ddd;">
        <img src="https://images.unsplash.com/photo-1534447677768-be436bb09401?w=400&q=80" alt="Sky" style="width: 100%; height: 100%; object-fit: cover;" />
      </div>
    </div>

    <!-- Purple Flowers (Top Right) -->
    <div class="polaroid-collage" style="position: absolute; top: 10px; right: 0; transform: rotate(12deg); width: 130px; padding: 8px 8px 25px; background: #fff; box-shadow: 0 8px 20px rgba(0,0,0,0.08); z-index: 2;">
      <div style="position: absolute; top: 5px; left: 10px; width: 12px; height: 12px; border-radius: 50%; background: #602548; box-shadow: inset -2px -2px 4px rgba(0,0,0,0.3); z-index: 10;"></div>
      <div style="width: 114px; height: 114px; overflow: hidden; background: #ddd;">
        <img src="https://images.unsplash.com/photo-1543788304-c5cb3673f4e2?w=400&q=80" alt="Flowers" style="width: 100%; height: 100%; object-fit: cover;" />
      </div>
    </div>

    <!-- Desk / Candle (Bottom Left) -->
    <div class="polaroid-collage" style="position: absolute; top: 120px; left: 10px; transform: rotate(-3deg); width: 140px; padding: 8px 8px 35px; background: #fff; box-shadow: 0 8px 20px rgba(0,0,0,0.1); z-index: 3;">
      <div style="width: 124px; height: 140px; overflow: hidden; background: #ddd;">
        <img src="https://images.unsplash.com/photo-1603503362142-a82f3c3065d0?w=400&q=80" alt="Candle Desk" style="width: 100%; height: 100%; object-fit: cover;" />
      </div>
    </div>

    <!-- Neon Sign (Bottom Right) -->
    <div class="polaroid-collage" style="position: absolute; top: 150px; right: 20px; transform: rotate(5deg); width: 120px; padding: 8px 8px 30px; background: #fff; box-shadow: 0 8px 20px rgba(0,0,0,0.1); z-index: 4;">
      <div style="width: 104px; height: 120px; overflow: hidden; background: #111;">
        <img src="https://images.unsplash.com/photo-1563241527-31df95e4e76a?w=400&q=80" alt="Neon Trust the Process" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8;" />
        <div style="position: absolute; top: 40%; left: 50%; transform: translate(-50%, -50%); color: #e879f9; font-family: 'Alex Brush', cursive; font-size: 22px; text-shadow: 0 0 10px #e879f9; white-space: nowrap; text-align: center; line-height: 1;">trust<br>the<br>process</div>
      </div>
    </div>

  </div>

  <!-- 10. Terminal Window (Bottom Left) -->
  <div class="floating-sticker" style="top: 72%; left: 2%; z-index: 10; transform: rotate(-2deg);">
    <div class="terminal-window" style="width: 260px; background: #fff; border-radius: 8px; box-shadow: 0 12px 30px rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.05); overflow: hidden;">
      <div style="padding: 10px 14px; background: #fdfaf8; border-bottom: 1px solid #f0e9e4; display: flex; align-items: center; justify-content: space-between;">
        <div style="display: flex; gap: 6px;">
          <span style="width: 8px; height: 8px; border-radius: 50%; background: #ff5f56; display: block;"></span>
          <span style="width: 8px; height: 8px; border-radius: 50%; background: #ffbd2e; display: block;"></span>
          <span style="width: 8px; height: 8px; border-radius: 50%; background: #27c93f; display: block;"></span>
        </div>
        <div style="font-family: 'IBM Plex Mono', monospace; font-size: 9px; color: #a4768f;">shakthi@journey:~</div>
      </div>
      <div style="padding: 15px; font-family: 'IBM Plex Mono', monospace; font-size: 9px; line-height: 1.8; color: #421835;">
        <div style="color: #a4768f; margin-bottom: 2px;">~$ whoami</div>
        <div style="font-weight: 600; margin-bottom: 12px;">designer. builder. problem-solver.</div>
        <div style="color: #a4768f; margin-bottom: 2px;">~$ focus</div>
        <div style="font-weight: 600; margin-bottom: 12px;">secure systems. seamless experiences.</div>
        <div style="color: #a4768f; margin-bottom: 2px;">~$ status</div>
        <div style="font-weight: 600;"><span style="color: #421835; font-size: 10px;">●</span> building | learning | growing</div>
      </div>
    </div>
  </div>

  <!-- 11. Dark Quote Note (Bottom Mid-Left) -->
  <div class="floating-sticker" style="top: 73%; left: 24%; z-index: 12; transform: rotate(3deg);">
    <!-- Washi tape -->
    <div style="position: absolute; top: -5px; left: 50%; transform: translateX(-50%); width: 45px; height: 14px; background: rgba(220, 200, 210, 0.9); box-shadow: 0 1px 3px rgba(0,0,0,0.1); z-index: 15;"></div>
    <div style="width: 140px; padding: 25px 20px; background: #4f2940; border-radius: 4px; box-shadow: 0 10px 25px rgba(0,0,0,0.15);">
      <div style="font-family: 'Manrope', sans-serif; font-size: 11px; font-weight: 500; line-height: 1.8; color: #fdfaf8; text-align: center;">
        "i design with empathy, i build with logic, i protect with purpose."
      </div>
      <div style="text-align: right; margin-top: 15px; font-family: 'Alex Brush', cursive; font-size: 18px; color: #c49eb3;">
        - Shakthi Sri
      </div>
      <div style="position: absolute; bottom: 15px; right: 15px; font-size: 12px; color: #c49eb3;">♡</div>
    </div>
  </div>

  <!-- 12. AGNI C2 Card (Bottom Center) -->
  <div class="floating-sticker" style="top: 66%; left: 40%; z-index: 9; transform: rotate(-1deg);">
    <div style="width: 320px; padding: 25px; background: linear-gradient(135deg, #150912, #2d1023); border-radius: 12px; box-shadow: 0 20px 40px rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.05); position: relative; overflow: hidden;">
      <!-- Nebula background effect -->
      <div style="position: absolute; top: 0; right: 0; width: 150px; height: 150px; background: radial-gradient(circle, rgba(251,113,133,0.15) 0%, transparent 70%); border-radius: 50%; filter: blur(20px);"></div>
      
      <div style="font-family: 'Manrope', sans-serif; font-size: 12px; font-weight: 700; color: #ebd5e0; letter-spacing: 0.05em; margin-bottom: 2px;">AGNI C2</div>
      <div style="font-family: 'IBM Plex Mono', monospace; font-size: 8px; color: #a4768f; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 15px;">COMMAND & CONTROL FRAMEWORK</div>
      
      <div style="display: flex; justify-content: space-between;">
        <ul style="list-style: none; padding: 0; margin: 0; font-family: 'Manrope', sans-serif; font-size: 9px; font-weight: 500; color: #d0b8c6; line-height: 2;">
          <li style="position: relative; padding-left: 10px;"><span style="position: absolute; left: 0; color: #fb7185;">•</span> Threat Simulation</li>
          <li style="position: relative; padding-left: 10px;"><span style="position: absolute; left: 0; color: #fb7185;">•</span> Real-time Monitoring</li>
          <li style="position: relative; padding-left: 10px;"><span style="position: absolute; left: 0; color: #fb7185;">•</span> Secure Communication</li>
          <li style="position: relative; padding-left: 10px;"><span style="position: absolute; left: 0; color: #fb7185;">•</span> Modular Architecture</li>
          <li style="position: relative; padding-left: 10px;"><span style="position: absolute; left: 0; color: #fb7185;">•</span> Stealth & Persistence</li>
        </ul>
        
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-right: 10px;">
          <!-- Flame Logo -->
          <svg width="45" height="55" viewBox="0 0 24 24" fill="url(#agni-grad)" style="filter: drop-shadow(0 0 5px rgba(251,113,133,0.4));">
            <defs>
              <linearGradient id="agni-grad" x1="0%" y1="100%" x2="0%" y2="0%">
                <stop offset="0%" stop-color="#be123c" />
                <stop offset="50%" stop-color="#e11d48" />
                <stop offset="100%" stop-color="#fb7185" />
              </linearGradient>
            </defs>
            <path d="M12 23c-5.52 0-10-4.48-10-10 0-4.75 3.31-8.72 7.75-9.75-.41 1.25-.62 2.62-.62 4 0 4.14 3.36 7.5 7.5 7.5.38 0 .75-.03 1.12-.09C16.92 19.34 14.67 23 12 23zm-.5-21c0 3.31 2.69 6 6 6 .68 0 1.33-.11 1.94-.31C18.66 4.09 15.61 2 12.19 2c-.23 0-.46.01-.69.03V2z" />
          </svg>
          <div style="font-family: 'Manrope', sans-serif; font-size: 14px; font-weight: 700; color: #fb7185; letter-spacing: 0.1em; margin-top: 5px;">AGNI</div>
        </div>
      </div>
      
      <div style="margin-top: 15px; font-family: 'Manrope', sans-serif; font-size: 8px; font-weight: 600; color: #ebd5e0;">Final Year Project</div>
      <div style="font-family: 'Manrope', sans-serif; font-size: 8px; color: #a4768f; line-height: 1.4; margin-top: 2px;">Built with purpose.<br>Securing systems.<br>Empowering defense.</div>
    </div>
  </div>

  <!-- 13. Tech Stack Grid (Bottom Mid-Right) -->
  <div class="floating-sticker" style="top: 66%; right: 26%; z-index: 10; transform: rotate(2deg);">
    <div style="width: 170px; padding: 20px; background: #fff; border-radius: 10px; box-shadow: 0 12px 25px rgba(0,0,0,0.06); border: 1px solid rgba(0,0,0,0.02);">
      <div style="font-family: 'Manrope', sans-serif; font-size: 10px; font-weight: 700; color: #7a3a5e; text-transform: uppercase; letter-spacing: 0.1em; text-align: center; margin-bottom: 15px;">TECH STACK</div>
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; place-items: center;">
        <img src="https://cdn.simpleicons.org/figma/F24E1E" style="width: 20px; height: 20px;" />
        <div style="width: 20px; height: 20px; background: #001e36; color: #26a5e4; font-family: 'Manrope', sans-serif; font-weight: 800; font-size: 14px; display: flex; align-items: center; justify-content: center; border-radius: 2px;">Ps</div>
        <div style="width: 20px; height: 20px; background: #330000; color: #ff9a00; font-family: 'Manrope', sans-serif; font-weight: 800; font-size: 14px; display: flex; align-items: center; justify-content: center; border-radius: 2px;">Ai</div>
        
        <img src="https://cdn.simpleicons.org/html5/E34F26" style="width: 20px; height: 20px;" />
        <img src="https://cdn.simpleicons.org/css3/1572B6" style="width: 20px; height: 20px;" />
        <div style="width: 20px; height: 20px; background: #f7df1e; color: #000; font-family: 'Manrope', sans-serif; font-weight: 800; font-size: 12px; display: flex; align-items: center; justify-content: center; border-radius: 2px;">JS</div>
        
        <img src="https://cdn.simpleicons.org/react/61DAFB" style="width: 20px; height: 20px;" />
        <img src="https://cdn.simpleicons.org/nodedotjs/339933" style="width: 20px; height: 20px;" />
        <img src="https://cdn.simpleicons.org/python/3776AB" style="width: 20px; height: 20px;" />
        
        <img src="https://cdn.simpleicons.org/github/181717" style="width: 20px; height: 20px;" />
        <div style="width: 20px; height: 20px; background: #3178c6; color: #fff; font-family: 'Manrope', sans-serif; font-weight: 800; font-size: 12px; display: flex; align-items: center; justify-content: center; border-radius: 2px;">TS</div>
        <div style="width: 35px; height: 20px; color: #000; font-family: 'Manrope', sans-serif; font-weight: 800; font-size: 10px; display: flex; align-items: center; justify-content: center;">NEXT.</div>
      </div>
    </div>
  </div>

  <!-- 14. 3 Folders (Bottom Right Center) -->
  <div class="floating-sticker" style="top: 80%; right: 25%; z-index: 11; display: flex; gap: 8px;">
    <!-- Folder 1: cyber labs -->
    <a href="#projects" style="text-decoration: none; transform: rotate(-3deg);">
      <div style="width: 70px; height: 50px; position: relative;">
        <svg width="70" height="50" viewBox="0 0 62 47" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M4 9C4 6.8 5.8 5 8 5H22L27 12H54C56.2 12 58 13.8 58 16V43C58 45.2 56.2 47 54 47H8C5.8 47 4 45.2 4 43V9Z" fill="#884d77"/>
          <path d="M4 14H58V43C58 45.2 56.2 47 54 47H8C5.8 47 4 45.2 4 43V14Z" fill="#753c63"/>
        </svg>
        <div style="position: absolute; top: 22px; left: 0; width: 100%; text-align: center; color: #ebd5e0; font-family: 'Manrope', sans-serif; font-size: 8px; font-weight: 500;">cyber labs 🔒</div>
      </div>
    </a>
    <!-- Folder 2: brain dumps -->
    <a href="#about" style="text-decoration: none; transform: rotate(2deg);">
      <div style="width: 70px; height: 50px; position: relative;">
        <svg width="70" height="50" viewBox="0 0 62 47" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M4 9C4 6.8 5.8 5 8 5H22L27 12H54C56.2 12 58 13.8 58 16V43C58 45.2 56.2 47 54 47H8C5.8 47 4 45.2 4 43V9Z" fill="#9e5684"/>
          <path d="M4 14H58V43C58 45.2 56.2 47 54 47H8C5.8 47 4 45.2 4 43V14Z" fill="#a4768f"/>
        </svg>
        <div style="position: absolute; top: 22px; left: 0; width: 100%; text-align: center; color: #fdfaf8; font-family: 'Manrope', sans-serif; font-size: 8px; font-weight: 500;">brain dumps ✩</div>
      </div>
    </a>
    <!-- Folder 3: inspiration -->
    <a href="#skills" style="text-decoration: none; transform: rotate(-2deg);">
      <div style="width: 70px; height: 50px; position: relative;">
        <svg width="70" height="50" viewBox="0 0 62 47" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M4 9C4 6.8 5.8 5 8 5H22L27 12H54C56.2 12 58 13.8 58 16V43C58 45.2 56.2 47 54 47H8C5.8 47 4 45.2 4 43V9Z" fill="#602548"/>
          <path d="M4 14H58V43C58 45.2 56.2 47 54 47H8C5.8 47 4 45.2 4 43V14Z" fill="#4f2940"/>
        </svg>
        <div style="position: absolute; top: 22px; left: 0; width: 100%; text-align: center; color: #ebd5e0; font-family: 'Manrope', sans-serif; font-size: 8px; font-weight: 500;">inspiration ♡</div>
      </div>
    </a>
  </div>

  <!-- 15. Vinyl Record (Far Right) -->
  <div class="floating-sticker" style="top: 38%; right: -5%; z-index: 5; transform: rotate(15deg);">
    <div style="width: 280px; height: 280px; border-radius: 50%; box-shadow: 0 15px 40px rgba(0,0,0,0.15); overflow: hidden; position: relative;">
      <img src="https://images.unsplash.com/photo-1603048588665-791ca8aea617?w=450&q=80" alt="Vinyl" style="width: 100%; height: 100%; object-fit: cover; filter: brightness(1.2);" />
      <!-- Center Label -->
      <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 90px; height: 90px; background: #8a3359; border: 4px solid #4f2940; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
        <div style="width: 15px; height: 15px; background: #fff; border-radius: 50%;"></div>
      </div>
    </div>
  </div>

  <!-- 16. Music Player (Bottom Right) -->
  <div class="floating-sticker" style="top: 55%; right: 4%; z-index: 15; transform: rotate(-4deg);">
    <div style="width: 220px; padding: 20px; background: rgba(235, 213, 224, 0.85); backdrop-filter: blur(10px); border-radius: 12px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); border: 1px solid rgba(255,255,255,0.4);">
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
        <span style="font-size: 10px; font-weight: 700; color: #421835; font-family: 'Manrope', sans-serif;">Focus Mode</span>
        <div style="font-size: 12px; color: #421835;">♡</div>
      </div>
      <div style="font-size: 16px; font-weight: 700; font-family: 'Manrope', sans-serif; color: #421835; margin-bottom: 2px;">lofi beats</div>
      <div style="font-size: 11px; color: #7a3a5e; font-family: 'Manrope', sans-serif; margin-bottom: 18px;">study chill channel</div>
      
      <div style="display: flex; align-items: center; justify-content: space-between; padding: 0 10px; color: #421835; margin-top: 20px;">
        <i class="fas fa-backward" style="font-size: 14px; cursor: pointer;"></i>
        <i class="fas fa-pause" style="font-size: 20px; cursor: pointer;"></i>
        <i class="fas fa-forward" style="font-size: 14px; cursor: pointer;"></i>
      </div>
    </div>
  </div>

</section>"""

# Using regex to replace the home section entirely
updated_content = re.sub(
    r'<section id="home".*?</section>', 
    new_home, 
    content, 
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(updated_content)

print("Home section perfectly rewritten!")
