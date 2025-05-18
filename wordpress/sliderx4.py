import os
import shutil
import re
import requests
from bs4 import BeautifulSoup

# ========== Configuration ==========
html_file = "rv_service.html"                     # Path to your local HTML file
page_name = "rv-service"                    # Page name for static/{page_name}/slider_#
base_static_path = os.path.join("static", page_name)
# start_group_index = 1                       # Index to start slider groups

# html_file = 'rv_service.html'  # Path to your HTML file
url_page = 'rv-service'      # Subdirectory under static
base_save_path = os.path.join('static', url_page)
start_sequence = [
    'src="https://cabear.com/wp-content/uploads/2024/07/cabear-e1720298696709.png"',
    'src="https://cabear.com/wp-content/uploads/2024/08/bearpawCircle-1.png"',
    'src="https://cabear.com/wp-content/uploads/2024/08/bearCircle.png"',
]
start_group = 1  # Change to N to skip the first N-1 groups


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




# ========== Main Script ==========

# Step 1: Delete old folders
delete_slider_folders(base_static_path)




# === Load and Parse HTML ===
with open(html_file, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

all_imgs = soup.find_all('img')
img_sets = []
current_set = []

for img in all_imgs:
    tag_str = str(img)
    img_url = img.get('src', '')
    if any(start in tag_str for start in start_sequence):
        if current_set:
            img_sets.append(current_set)
        current_set = []
    else:
        if img_url:
            current_set.append(img_url)

if current_set:
    img_sets.append(current_set)

# === Filter by start_group ===
img_sets = img_sets[start_group - 1:]

# === Download Images ===
for i, group in enumerate(img_sets, start=start_group):
    group_folder = os.path.join(base_save_path, f'slider_{i}')
    os.makedirs(group_folder, exist_ok=True)
    print(f"\nSaving Group {i} ({len(group)} images) to: {group_folder}")

    for url in group:
        filename = os.path.basename(url)
        filepath = os.path.join(group_folder, filename)

        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=headers)
            r.raise_for_status()

            with open(filepath, 'wb') as f:
                f.write(r.content)
            print(f"✓ Saved: {filepath}")
        except Exception as e:
            print(f"✘ Failed to download {url}: {e}")
