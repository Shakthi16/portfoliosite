import re

with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Update Patent item in achData with exact Application No 202541069996 A and all 5 nanosafe gallery images
old_patent_block = '''{
          category: "Intellectual Property",
          title: "Patent\\nFiled",
          subtitle: "NanoSafe Cloak — Privacy Innovation",
          desc: "Developed and filed a technology patent for the NanoSafe Cloak — a wearable device generating an on-demand nano-fog privacy shield using advanced nanomaterials and smart electronics. The cloak creates a visual distortion barrier effective against hidden cameras while remaining transparent to the human eye, addressing critical privacy concerns across hospitality, retail, and personal safety sectors.",
          bg: "linear-gradient(135deg, #3b0764 0%, #1e1b4b 100%)",
          charImg: "patent.png",
          gallery: ["patent.png"],
          meta: [
            "<strong>Inventor:</strong> Shakthi Sri T S",
            "<strong>Patent Type:</strong> Technology Utility Patent",
            "<strong>Filed under:</strong> MSME Hackathon 5.0",
            "<strong>Status:</strong> Registered & Filed"
          ]
        }'''

new_patent_block = '''{
          category: "Intellectual Property",
          title: "Patent\\nFiled",
          subtitle: "NanoSafe Cloak — Privacy Innovation",
          desc: "Developed and filed a technology patent for the NanoSafe Cloak (Indian Patent App No: 202541069996 A) — a wearable device generating an on-demand nano-fog privacy shield using advanced nanomaterials and smart electronics to protect against hidden cameras while remaining transparent to the human eye.",
          bg: "linear-gradient(135deg, #3b0764 0%, #1e1b4b 100%)",
          charImg: "patent.png",
          gallery: [
            "nanosafe_gallery_1.jpg",
            "nanosafe_gallery_2.jpg",
            "nanosafe_gallery_3.jpg",
            "nanosafe_gallery_4.jpg",
            "nanosafe_gallery_5.jpg"
          ],
          meta: [
            "<strong>Application No:</strong> 202541069996 A (IP India)",
            "<strong>Inventor:</strong> Shakthi Sri T S",
            "<strong>Title:</strong> NANOSAFE CLOAK A SMART WEARABLE NANO FOG PRIVACY SHIELD",
            "<strong>Application Date:</strong> 23/07/2025",
            "<strong>Status:</strong> Published — MSME Hackathon 5.0"
          ]
        }'''

if old_patent_block in html:
    html = html.replace(old_patent_block, new_patent_block)
    print("Exact match replaced!")
else:
    # Regex replacement for flexibility
    pattern = r'category:\s*"Intellectual Property"[\s\S]*?status:\s*"Registered & Filed"[\s\S]*?\]\s*\}'
    html = re.sub(r'category:\s*"Intellectual Property"[\s\S]*?status:\s*"Registered & Filed"[\s\S]*?\]\s*\}', new_patent_block[1:-1], html)
    print("Regex replacement executed!")

with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESSFULLY UPDATED PATENT FILED METADATA AND GALLERY MOCKUPS IN INDEX.HTML!")
