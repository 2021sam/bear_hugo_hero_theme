import os
import shutil
import re
import requests
from bs4 import BeautifulSoup

# ========== Configuration ==========
html_file = "rv_service.html"                     # Path to your local HTML file
page_name = "rv-service"                    # Page name for static/{page_name}/slider_#
base_static_path = os.path.join("static", page_name)
start_group_index = 1                       # Index to start slider groups
skip_images = [
    'src="https://cabear.com/wp-content/uploads/2024/07/cabear-e1720298696709.png"',
    'src="https://cabear.com/wp-content/uploads/2024/07/cabear-e1720298696709.png"',
    'src="https://cabear.com/wp-content/uploads/2024/08/bearpawCircle-1.png"',
    'src="https://cabear.com/wp-content/uploads/2024/08/bearCircle.png"',
]

# ========== Functions ==========

def delete_slider_folders(base_dir):
    """Delete all slider_# folders in the given base directory."""
    if not os.path.isdir(base_dir):
        return
    for folder in os.listdir(base_dir):
        if re.match(r"slider_\d+", folder):
            full_path = os.path.join(base_dir, folder)
            if os.path.isdir(full_path):
                shutil.rmtree(full_path)
                print(f"✓ Deleted old folder: {full_path}")

def extract_image_groups(html_content, skip_list):
    """Extract groups of image URLs from HTML, separated by starting images."""
    soup = BeautifulSoup(html_content, "html.parser")
    img_tags = soup.find_all("img")

    groups = []
    current_group = []

    for tag in img_tags:
        tag_str = str(tag)
        if tag_str.strip() in skip_list:
            if current_group:
                groups.append(current_group)
                current_group = []
        else:
            src = tag.get("src")
            if src:
                current_group.append(src)

    if current_group:
        groups.append(current_group)

    return groups

def save_image(url, folder_path):
    """Download and save an image to a given folder."""
    filename = os.path.basename(url.split("?")[0])
    filepath = os.path.join(folder_path, filename)

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"✓ Saved: {filepath}")
    except requests.exceptions.RequestException as e:
        print(f"✘ Failed to download {url}: {e}")

# ========== Main Script ==========

# Step 1: Delete old folders
delete_slider_folders(base_static_path)

# Step 2: Read HTML content
with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

# Step 3: Extract image groups
groups = extract_image_groups(html, skip_images)

# Step 4: Save image groups to folders
for i, group in enumerate(groups, start=start_group_index):
    folder = os.path.join(base_static_path, f"slider_{i}")
    os.makedirs(folder, exist_ok=True)
    print(f"\nSaving Group {i} ({len(group)} images) to: {folder}")
    for img_url in group:
        save_image(img_url, folder)
