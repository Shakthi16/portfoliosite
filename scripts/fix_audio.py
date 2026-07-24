import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add audio element and ids for JS
content = content.replace(
    '<div style="font-size: 16px; font-weight: 700; font-family: \'Manrope\', sans-serif !important; color: #421835; margin-bottom: 2px;">lofi beats</div>',
    '<div style="font-size: 16px; font-weight: 700; font-family: \'Manrope\', sans-serif !important; color: #421835; margin-bottom: 2px;">lofi beats</div>\n      <audio id="lofi-audio" src="https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3?filename=lofi-study-112191.mp3" loop></audio>'
)

content = content.replace(
    '<i class="fas fa-pause" style="font-size: 20px; cursor: pointer;"></i>',
    '<i class="fas fa-play" id="play-pause-btn" style="font-size: 20px; cursor: pointer;" title="Play/Pause"></i>'
)

# 2. Add id to vinyl to control spinning, and default it to paused
content = content.replace(
    'class="spin-cd" />',
    'class="spin-cd" id="vinyl-record" style="animation-play-state: paused;" />'
)

# 3. Add JS script before </body>
script_block = """
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const audio = document.getElementById('lofi-audio');
    const playBtn = document.getElementById('play-pause-btn');
    const vinyl = document.getElementById('vinyl-record');
    
    if(audio && playBtn) {
      playBtn.addEventListener('click', function() {
        if(audio.paused) {
          audio.play();
          playBtn.classList.remove('fa-play');
          playBtn.classList.add('fa-pause');
          if(vinyl) vinyl.style.animationPlayState = 'running';
        } else {
          audio.pause();
          playBtn.classList.remove('fa-pause');
          playBtn.classList.add('fa-play');
          if(vinyl) vinyl.style.animationPlayState = 'paused';
        }
      });
    }
  });
</script>
</body>"""

content = content.replace('</body>', script_block)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Audio functionality added successfully.")
