import os
import re

# ====== Configuration ======
page_name = "welcome"  # Update this per page
base_dir = os.path.join("static", "images", page_name)
output_md = f"{page_name}.md"
title = "Welcome Page"
layout = "welcome"

# ====== Helper: Collect valid image paths ======
def collect_images_in_folder(folder_path, prefix_path):
    return sorted([
        os.path.join(prefix_path, img).replace("\\", "/")
        for img in os.listdir(folder_path)
        if img.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif'))
    ])

# ====== Determine grouping strategy ======
slider_groups = []
subfolders = sorted([
    f for f in os.listdir(base_dir)
    if re.match(r"slider_\d+", f) and os.path.isdir(os.path.join(base_dir, f))
])

if subfolders:
    # ✅ Case 1: Use each slider_# folder as its own group
    for folder in subfolders:
        folder_path = os.path.join(base_dir, folder)
        prefix_path = f"/images/{page_name}/{folder}"
        images = collect_images_in_folder(folder_path, prefix_path)
        if images:
            slider_groups.append(images)
else:
    # ✅ Case 2: Flat folder — treat all images as one group
    images = collect_images_in_folder(base_dir, f"/images/{page_name}")
    if images:
        slider_groups.append(images)

# ====== Write to Markdown ======
with open(output_md, 'w', encoding='utf-8') as f:
    f.write("+++\n")
    f.write(f'title = "{title}"\n')
    f.write(f'layout = "{layout}"\n')

    for idx, group in enumerate(slider_groups, start=1):
        f.write(f"swiperImages{idx} = [\n")
        for img in group:
            f.write(f'  "{img}",\n')
        f.write("]\n")

    f.write("+++\n\n")
    f.write("Welcome to the Gallery!\n")

print(f"✅ {output_md} generated with {len(slider_groups)} image group(s).")
