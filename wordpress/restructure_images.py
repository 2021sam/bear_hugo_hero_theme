import os
import shutil
import re
import requests
from bs4 import BeautifulSoup

# ========== Configuration ==========
html_file = "rv_service.html"         # Path to your local HTML file
url_page = "rv-service"               # Used for directory: static/{url_page}/slider_#
# base_save_path = os.path.join("static", url_page)
base_save_path = os.path.join("static", "images", url_page)

start_group = 1                       # Skip first N-1 groups

# Images that mark the start of a new group (also to be excluded)
start_sequence = [
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

def load_html_file(path):
    """Load and parse the HTML file with BeautifulSoup."""
    with open(path, 'r', encoding='utf-8') as f:
        return BeautifulSoup(f, 'html.parser')

def extract_image_groups(soup, start_sequence):
    """Group images by markers from start_sequence, excluding those markers."""
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

    return img_sets

def download_images(image_groups, base_path, start_index=1):
    """Download images into slider_N folders starting from the given index."""
    image_groups = image_groups[start_index - 1:]

    for i, group in enumerate(image_groups, start=start_index):
        group_folder = os.path.join(base_path, f'slider_{i}')
        os.makedirs(group_folder, exist_ok=True)
        print(f"\nSaving Group {i} ({len(group)} images) to: {group_folder}")

        for url in group:
            filename = os.path.basename(url.split("?")[0])
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

# ========== Main Execution ==========

def main():
    delete_slider_folders(base_save_path)
    soup = load_html_file(html_file)
    image_groups = extract_image_groups(soup, start_sequence)
    download_images(image_groups, base_save_path, start_group)

if __name__ == "__main__":
    main()
