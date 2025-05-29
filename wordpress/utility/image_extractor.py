# /Users/2021sam/apps/BEAR/hugo/05_05_wp_conv/bear/wordpress/utility/image_group_extractor.py

import os
import shutil
import requests
from bs4 import BeautifulSoup

# ========== Configuration ==========
# url_page = "welcome"
# base_save_path = os.path.join("static", "images", url_page)
# html_file = os.path.join(os.path.dirname(__file__), "..", "html", "welcome.html")

url_page = "about"
base_save_path = os.path.join("static", "images", url_page)
html_file = os.path.join(os.path.dirname(__file__), "..", "html", "about.html")


# ========== Functions ==========

def delete_output_folder(path):
    """Remove folder if it exists."""
    if os.path.isdir(path):
        shutil.rmtree(path)
        print(f"✓ Deleted existing folder: {path}")

def load_html_file(path):
    """Parse HTML using BeautifulSoup."""
    with open(path, 'r', encoding='utf-8') as f:
        return BeautifulSoup(f, 'html.parser')

def extract_all_image_urls(soup):
    """Return all image URLs from the HTML."""
    return [img['src'] for img in soup.find_all('img') if img.get('src')]

def download_images(image_urls, save_dir):
    """Download all images into the given directory."""
    os.makedirs(save_dir, exist_ok=True)
    print(f"Saving {len(image_urls)} images to: {save_dir}\n")

    for i, url in enumerate(image_urls, start=1):
        filename = os.path.basename(url.split("?")[0])
        filepath = os.path.join(save_dir, filename)

        # If file exists, skip
        if os.path.exists(filepath):
            print(f"• Skipped (already exists): {filename}")
            continue

        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=headers)
            r.raise_for_status()

            with open(filepath, 'wb') as f:
                f.write(r.content)
            print(f"✓ Saved: {filename}")
        except Exception as e:
            print(f"✘ Failed to download {url}: {e}")

# ========== Main ==========
def main():
    delete_output_folder(base_save_path)
    soup = load_html_file(html_file)
    image_urls = extract_all_image_urls(soup)
    download_images(image_urls, base_save_path)

if __name__ == "__main__":
    main()
