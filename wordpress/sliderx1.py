import os
import re
import requests

# Your HTML file
html_file = "rv_service.html"

# Hugo page slug/folder
url_page = "your-page-name"  # ← CHANGE THIS to match your Hugo page

# Image group delimiters (exclude these from output)
start_sequence = [
    'src="https://cabear.com/wp-content/uploads/2024/07/cabear-e1720298696709.png"',
    'src="https://cabear.com/wp-content/uploads/2024/08/bearpawCircle-1.png"',
    'src="https://cabear.com/wp-content/uploads/2024/08/bearCircle.png"',
]

# Read HTML content
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Extract all <img src="...">
img_tags = re.findall(r'<img[^>]+src="([^"]+)"', content)

groups = []
current_group = []

for src in img_tags:
    if any(s in f'src="{src}"' for s in start_sequence):
        if current_group:
            groups.append(current_group)
            current_group = []
        continue
    current_group.append(src)

# Catch final group
if current_group:
    groups.append(current_group)

# Save images
for i, group in enumerate(groups, start=1):
    group_dir = os.path.join("static", url_page, f"slider_{i}")
    os.makedirs(group_dir, exist_ok=True)

    print(f"\nSaving Group {i} ({len(group)} images) to: {group_dir}")

    for j, url in enumerate(group, start=1):
        filename = os.path.join(group_dir, os.path.basename(url))
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            with open(filename, "wb") as img_file:
                img_file.write(response.content)
            print(f"✔ Saved: {filename}")
        except Exception as e:
            print(f"✘ Failed to download {url}: {e}")
