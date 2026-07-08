import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove the music player block completely
# It starts with <!-- 15. Music Player and ends before <!-- 16. Interactive folder
content = re.sub(
    r'<!-- 15\. Music Player.*?<!-- 16\. Interactive folder',
    '<!-- 16. Interactive folder',
    content,
    flags=re.DOTALL
)

# 2. Replace the Vinyl Record HTML to include the audio tag and the new play/pause button
new_vinyl_record = '''<!-- 17. Vinyl Record -->
      <div class="floating-sticker" style="bottom: -5%; right: -5%; z-index: 5; transform: rotate(0deg); scale: 0.85;">
        <audio id="lofi-audio" src="https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3?filename=lofi-study-112191.mp3" loop></audio>
        <div
          style="width: 250px; height: 250px; border-radius: 50%; box-shadow: 0 15px 40px rgba(0,0,0,0.15); overflow: hidden; position: relative;">
          <img src="https://images.unsplash.com/photo-1603048588665-791ca8aea617?q=80&w=450" alt="Vinyl"
            style="width: 100%; height: 100%; object-fit: cover; filter: brightness(1.2);" class="spin-cd"
            id="vinyl-record" style="animation-play-state: paused;" />
          <div
            style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 80px; height: 80px; background: rgba(66, 24, 53, 0.85); backdrop-filter: blur(4px); border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 4px 15px rgba(0,0,0,0.4); border-radius: 50%; display: flex; align-items: center; justify-content: center; z-index: 10; transition: transform 0.2s;">
            <i class="fas fa-play" id="play-pause-btn" style="font-size: 32px; color: #fff; padding-left: 6px; cursor: pointer; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center;" title="Play/Pause"></i>
          </div>
        </div>
      </div>'''

content = re.sub(
    r'<!-- 17\. Vinyl Record -->.*?<div class="floating-sticker" style="bottom: -5%; right: -5%;[^>]*>.*?<div\s*style="position: absolute; top: 50%; left: 50%;.*?</div>\s*</div>\s*</div>',
    new_vinyl_record,
    content,
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updates applied: Removed Lofi beats player, added play button to vinyl.")
