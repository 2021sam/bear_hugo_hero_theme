import os
import re

# ====== Configuration ======
# page_name = "rv-service"  # Set to match your Hugo folder
page_name = "welcome"  # Set to match your Hugo folder
base_dir = os.path.join("static", "images", page_name)
output_md = "welcome.md"
title = "Welcome Page"
layout = "welcome"

# ====== Build swiperImagesX for each slider group ======
slider_groups = []

# Match folders like slider_1, slider_2, ...
for folder in sorted(os.listdir(base_dir)):
    if re.match(r"slider_\d+", folder):
        folder_path = os.path.join(base_dir, folder)
        if os.path.isdir(folder_path):
            images = sorted([
                f"/images/{page_name}/{folder}/{img}"
                for img in os.listdir(folder_path)
                if img.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif'))
            ])
            slider_groups.append(images)

# ====== Write to Markdown ======
with open(output_md, 'w', encoding='utf-8') as f:
    f.write("+++\n")
    f.write(f'title = "{title}"\n')
    f.write(f'layout = "{layout}"\n')

    for idx, images in enumerate(slider_groups, start=1):
        f.write(f"swiperImages{idx} = [\n")
        for img in images:
            f.write(f'  "{img}",\n')
        f.write("]\n")

    f.write("+++\n\n")
    f.write("Welcome to the Gallery!\n")

print(f"✅ gallery.md generated with {len(slider_groups)} image groups.")
