import urllib.request
import re
import os

url = 'https://www.linkedin.com/feed/update/urn:li:activity:7390039189452615680/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

req = urllib.request.Request(url, headers=headers)
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Find all media image links
    matches = re.findall(r'https://media\.licdn\.com/dms/image/[^\s"\'<>]+', html)
    unique_urls = []
    for u in matches:
        u_clean = u.replace('&amp;', '&')
        if u_clean not in unique_urls:
            unique_urls.append(u_clean)

    print(f"Found {len(unique_urls)} unique LinkedIn image URLs:")
    saved_files = []
    for idx, u in enumerate(unique_urls):
        print(f"{idx+1}: {u[:100]}...")
        out_name = f"e:/portfoliosite/hackathon_winner_{idx+1}.jpg"
        urllib.request.urlretrieve(u, out_name)
        saved_files.append(out_name)
        print(f"Saved to {out_name}")

except Exception as e:
    print(f"Error: {e}")
