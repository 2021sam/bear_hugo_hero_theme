import os
import shutil
import re
import requests
import yaml
from bs4 import BeautifulSoup

# ====== CONFIGURATION ======
html_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "html", "truck-services.html"))
url_page = "truck-service"
base_save_path = os.path.join("static", "images", url_page)
output_yaml = f"{url_page}.yaml"
start_group = 2

start_sequence = ['class="kb-gallery-ul']

# ====== UTILITIES ======
def delete_slider_folders(base_dir):
    if not os.path.isdir(base_dir):
        return
    for folder in os.listdir(base_dir):
        if re.match(r"slider_\d+", folder):
            shutil.rmtree(os.path.join(base_dir, folder), ignore_errors=True)
            print(f"✓ Deleted: {folder}")

def load_html_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return BeautifulSoup(f, 'html.parser')

def extract_image_groups(soup, start_sequence):
    img_sets = []
    current_set = []
    all_elements = soup.find_all(['div', 'img'])

    for tag in all_elements:
        if tag.name == 'div' and any(marker in str(tag) for marker in start_sequence):
            if current_set:
                img_sets.append(current_set)
                current_set = []
        elif tag.name == 'img':
            src = tag.get('src')
            if src:
                current_set.append(src)
    if current_set:
        img_sets.append(current_set)
    return img_sets

def download_images(image_groups, base_path, start_index=1):
    image_groups = image_groups[start_index - 1:]
    all_local_paths = []

    for i, group in enumerate(image_groups, start=1):
        slider_folder = f"slider_{i}"
        group_folder = os.path.join(base_path, slider_folder)
        os.makedirs(group_folder, exist_ok=True)
        local_paths = []

        print(f"\nSaving Group {i} -> {slider_folder}")
        for url in group:
            filename = os.path.basename(url.split("?")[0])
            local_path = f"images/{url_page}/{slider_folder}/{filename}"
            local_paths.append(local_path)

            filepath = os.path.join(group_folder, filename)
            try:
                headers = {'User-Agent': 'Mozilla/5.0'}
                r = requests.get(url, headers=headers)
                r.raise_for_status()
                with open(filepath, 'wb') as f:
                    f.write(r.content)
                print(f"✓ {filename}")
            except Exception as e:
                print(f"✘ Failed to download {url}: {e}")

        all_local_paths.append(local_paths)
    return all_local_paths

def write_yaml(image_groups, output_path):
    data = {}
    for idx, group in enumerate(image_groups, start=1):
        data[f"swiper_images_{idx}"] = {
            "header": f"TODO Header {idx}",
            "description": f"TODO Description {idx}",
            "images": group
        }

    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True)

    print(f"\n✅ YAML written to {output_path} with {len(image_groups)} groups")

# ====== MAIN ======
def main():
    delete_slider_folders(base_save_path)
    soup = load_html_file(html_file)
    image_groups = extract_image_groups(soup, start_sequence)
    local_image_paths = download_images(image_groups, base_save_path, start_group)
    write_yaml(local_image_paths, output_yaml)

if __name__ == "__main__":
    main()
