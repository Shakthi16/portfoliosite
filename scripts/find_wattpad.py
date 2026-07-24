import os

files = os.listdir('.')
wattpad_files = [f for f in files if 'wattpad' in f.lower()]
print("Wattpad files found:", wattpad_files)

# Check all png/jpg/jpe files
img_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.jpe'))]
print("All image files:", img_files)
