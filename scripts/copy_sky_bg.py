import shutil, os

src = r"C:\Users\sssum\.gemini\antigravity-ide\brain\7394872a-c4c7-4df7-8be9-a014f3404d19\sky_clouds_bg_1784617028496.png"
dst = r"e:\portfoliosite\sky_clouds_bg.png"

if os.path.exists(src):
    shutil.copy(src, dst)
    print("Successfully copied sky clouds image to e:\\portfoliosite\\sky_clouds_bg.png")
else:
    print("Source image not found.")
