import os
import re
import requests

# === CONFIGURATION ===
# html_file = 'your_html_file.html'  # Replace with your actual HTML file
html_file = 'rv_service.html'  # Replace with your actual HTML file
url_page = 'rv-service'        # Folder name for Hugo static path
base_save_path = f'static/{url_page}'

# These images will be ignored and treated as separators
start_sequence = [
    'src="https://cabear.com/wp-content/uploads/2024/07/cabear-e1720298696709.png"',
    'src="https://cabear.com/wp-content/uploads/2024/08/bearpawCircle-1.png"',
    'src="https://cabear.com/wp-content/uploads/2024/08/bearCircle.png"',
]

# === FUNCTION TO DOWNLOAD IMAGE ===
def download_image(url, save_path):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/123.0.0.0 Safari/537.36"
        )
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"✓ Saved: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"✘ Failed to download {url}: {e}")

# === MAIN PROCESSING ===
def extract_and_download_images():
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Extract all image URLs from HTML
    image_urls = re.findall(r'src="([^"]+)"', html_content)

    groups = []
    current_group = []

    for url in image_urls:
        tag = f'src="{url}"'
        if tag in start_sequence:
            if current_group:
                groups.append(current_group)
                current_group = []
        else:
            current_group.append(url)

    if current_group:
        groups.append(current_group)

    # Save each group to its own folder
    for i, group in enumerate(groups, 1):
        group_folder = os.path.join(base_save_path, f'slider_{i}')
        os.makedirs(group_folder, exist_ok=True)
        print(f"\nSaving Group {i} ({len(group)} images) to: {group_folder}")

        for img_url in group:
            filename = os.path.basename(img_url.split("?")[0])  # remove query params
            save_path = os.path.join(group_folder, filename)
            download_image(img_url, save_path)

if __name__ == '__main__':
    extract_and_download_images()
