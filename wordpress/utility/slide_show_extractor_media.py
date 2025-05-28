# /Users/2021sam/apps/BEAR/hugo/05_05_wp_conv/bear/wordpress/utility/image_group_extractor.py

import os
import shutil
import re
import requests
from bs4 import BeautifulSoup

# ========== Configuration ==========
# html_file = "rv_service.html"         # Path to your local HTML file
html_file = os.path.join(os.path.dirname(__file__), "..", "html", "truck-services.html")
html_file = os.path.abspath(html_file)  # resolves ".." to absolute path

url_page = "truck-service"               # Used for directory: static/{url_page}/slider_#
# base_save_path = os.path.join("static", url_page)


base_save_path = os.path.join("static", "images", url_page)

start_group = 2                       # Skip first N-1 groups

# Images that mark the start of a new group (also to be excluded)
start_sequence = [
    'class="kb-gallery-ul'
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

# def extract_image_groups(soup, start_sequence):
#     """Group images by markers from start_sequence, excluding those markers."""
#     all_imgs = soup.find_all('img')
#     img_sets = []
#     current_set = []

#     for img in all_imgs:
#         tag_str = str(img)
#         img_url = img.get('src', '')
#         if any(start in tag_str for start in start_sequence):
#             if current_set:
#                 img_sets.append(current_set)
#             current_set = []
#         else:
#             if img_url:
#                 current_set.append(img_url)

#     if current_set:
#         img_sets.append(current_set)

#     return img_sets


def extract_image_groups(soup, start_sequence):
    """
    Group images that follow div markers.
    """
    img_sets = []
    current_set = []

    # Flatten the HTML into tags only
    all_elements = soup.find_all(['div', 'img'])

    for tag in all_elements:
        if tag.name == 'div' and any(start in str(tag) for start in start_sequence):
            if current_set:
                img_sets.append(current_set)
                current_set = []
        elif tag.name == 'img':
            src = tag.get('src', '')
            if src:
                current_set.append(src)

    if current_set:
        img_sets.append(current_set)

    return img_sets




def download_images(image_groups, base_path, start_index=1):
    """Download images into slider_N folders starting from the given index."""
    image_groups = image_groups[start_index - 1:]

    for i, group in enumerate(image_groups, start=1):
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
