import os
import re
import yaml

# ====== Configuration ======
page_name = "truck-service"  # Set to match your Hugo folder
base_dir = os.path.join("static", "images", page_name)
output_yaml = "truck-service.yaml"  # Output file
default_header = "Header goes here"
default_description = "Description goes here"

# ====== Build swiper_images_X for each slider group ======
slider_data = {}

# Match folders like slider_1, slider_2, ...
for idx, folder in enumerate(sorted(os.listdir(base_dir)), start=1):
    if re.match(r"slider_\d+", folder):
        folder_path = os.path.join(base_dir, folder)
        if os.path.isdir(folder_path):
            images = sorted([
                f"images/{page_name}/{folder}/{img}"
                for img in os.listdir(folder_path)
                if img.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif'))
            ])
            key = f"swiper_images_{idx}"
            slider_data[key] = {
                "header": default_header,
                "description": default_description,
                "images": images
            }

# ====== Write to YAML ======
with open(output_yaml, 'w', encoding='utf-8') as f:
    yaml.dump(slider_data, f, allow_unicode=True, sort_keys=False)

print(f"✅ {output_yaml} generated with {len(slider_data)} image groups.")
