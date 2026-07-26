import urllib.request
import os

img_url = 'https://i.pinimg.com/1200x/80/34/20/80342049d1cf6ba4adffa608a009adee.jpg'
dest_path = 'e:/portfoliosite/best_outgoing_award.jpg'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

req = urllib.request.Request(img_url, headers=headers)

try:
    data = urllib.request.urlopen(req).read()
    with open(dest_path, 'wb') as f:
        f.write(data)
    print(f"SUCCESSFULLY DOWNLOADED {dest_path} ({len(data)} bytes)!")
except Exception as e:
    print(f"Error downloading image: {e}")
