import urllib.request
import re

try:
    url = "https://fonts.cdnfonts.com/css/brittany-signature"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    css = response.read().decode('utf-8')
    print("Found font CSS:")
    print(css)
except Exception as e:
    print(f"Error finding font: {e}")
