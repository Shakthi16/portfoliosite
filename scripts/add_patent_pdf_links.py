import shutil
import os
import re

# 1. Copy PDF files to clean root web paths
shutil.copy('e:/portfoliosite/nanosafe/msme hackathon 5.0.pdf', 'e:/portfoliosite/nanosafe_msme_hackathon.pdf')
shutil.copy('e:/portfoliosite/nanosafe/nano.pdf', 'e:/portfoliosite/nanosafe_cloak_patent_doc.pdf')

print("Copied PDF files to root directory!")

# 2. Update index.html to add pdfs array to Patent Filed achData and render interactive PDF links in FLIP detail modal
with open('e:/portfoliosite/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Add pdfs array to Patent Filed achData
old_patent_meta = '"<strong>Status:</strong> Published — MSME Hackathon 5.0"\n          ]'
new_patent_meta = '"<strong>Status:</strong> Published — MSME Hackathon 5.0"\n          ],\n          pdfs: [\n            { name: "MSME Hackathon 5.0 Proposal.pdf", url: "nanosafe_msme_hackathon.pdf" },\n            { name: "NanoSafe Cloak Patent Specification.pdf", url: "nanosafe_cloak_patent_doc.pdf" }\n          ]'

html = html.replace(old_patent_meta, new_patent_meta)

# Update JS in FLIP detail modal to render clickable PDF document buttons
js_target = "galleryGrid.appendChild(thumb);\n              });"
js_replacement = """galleryGrid.appendChild(thumb);
              });
            } else {
              galleryGrid.innerHTML = '<p class="text-xs text-gray-500 italic">No additional gallery photos available</p>';
            }

            // Render PDF Document Links if available
            let pdfContainer = document.getElementById('detail-pdf-container');
            if (!pdfContainer) {
              pdfContainer = document.createElement('div');
              pdfContainer.id = 'detail-pdf-container';
              pdfContainer.className = 'detail-text-reveal border-t border-white/10 pt-4 md:pt-6 mt-4 md:mt-6';
              galleryGrid.parentElement.after(pdfContainer);
            }

            if (data.pdfs && data.pdfs.length > 0) {
              let pdfHTML = '<h5 class="text-xs uppercase tracking-widest text-purple-400 font-bold mb-3 font-sans">Official Patent Documents & PDFs</h5><div class="flex flex-wrap gap-2.5">';
              data.pdfs.forEach(pdf => {
                pdfHTML += `<a href="${pdf.url}" target="_blank" rel="noopener noreferrer" class="px-3.5 py-2 bg-purple-950/80 hover:bg-purple-900 text-purple-200 border border-purple-400/40 rounded-xl text-xs font-bold flex items-center gap-2 transition-all hover:scale-105 shadow-md">
                  <i class="fas fa-file-pdf text-rose-400 text-sm"></i>
                  <span>${pdf.name} ↗</span>
                </a>`;
              });
              pdfHTML += '</div>';
              pdfContainer.innerHTML = pdfHTML;
              pdfContainer.style.display = 'block';
            } else if (pdfContainer) {
              pdfContainer.style.display = 'none';
            }"""

html = html.replace("galleryGrid.appendChild(thumb);\n              });", js_replacement)

with open('e:/portfoliosite/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESSFULLY INTEGRATED INTERACTIVE PATENT PDF LINKS INTO INDEX.HTML!")
