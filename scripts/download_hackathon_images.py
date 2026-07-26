import urllib.request
import re
import json

url_page = 'https://www.linkedin.com/posts/shakthisri_activity-7390039189452615680-s7dW'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

req = urllib.request.Request(url_page, headers=headers)
html = urllib.request.urlopen(req).read().decode('utf-8')

# Search for image URLs in og:image or JSON metadata inside page
matches = re.findall(r'https://media\.licdn\.com/dms/image/[^\s"\'<>]+', html)

img_urls = []
for m in matches:
    clean = m.replace('&amp;', '&')
    if clean not in img_urls and 'profile-displayphoto' not in clean and 'company-logo' not in clean:
        img_urls.append(clean)

print(f"Found {len(img_urls)} post images!")
for i, url in enumerate(img_urls):
    print(f"Image #{i+1}: {url}")
    out_path = f"e:/portfoliosite/vibe_hackathon_img_{i+1}.jpg"
    
    img_req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Referer': 'https://www.linkedin.com/'
    })
    try:
        data = urllib.request.urlopen(img_req).read()
        with open(out_path, 'wb') as f:
            f.write(data)
        print(f"Successfully downloaded {out_path} ({len(data)} bytes)!")
    except Exception as e:
        print(f"Error downloading #{i+1}: {e}")
