Here’s a `README.md` tailored for your Python script. This file explains the script’s purpose, usage, configuration, and prerequisites.

---

**📄 Filename:** `README.md`
**📁 Suggested Directory:** Same directory as your Python script

```markdown
# 🖼️ HTML Image Group Extractor & Downloader

This script parses a local HTML file to extract `<img>` tags, groups them based on predefined **start markers**, and downloads the resulting image sets into organized `slider_#` folders. It's ideal for preparing Swiper.js galleries for static site generators like **Hugo**.

---

## 🔧 Features

- Automatically detects new image groups via known `<img>` start markers.
- Downloads each group into its own `slider_N` folder.
- Cleans up old `slider_#` folders before processing.
- Skips N groups if desired (e.g. start from `slider_2`).

---

## 📁 Folder Structure

Example output:

```

static/
images/
rv-service/
slider\_1/
img1.jpg
img2.jpg
slider\_2/
...

````

---

## ⚙️ Configuration

Edit the variables at the top of the script:

```python
html_file = "rv_service.html"         # Your local HTML file
url_page = "rv-service"               # Used in path: static/images/{url_page}/slider_#
base_save_path = os.path.join("static", "images", url_page)

start_group = 1                       # Group index to start from

start_sequence = [
    'src="https://cabear.com/wp-content/uploads/2024/07/cabear-e1720298696709.png"',
    ...
]
````

---

## ▶️ Usage

1. **Install dependencies**

   ```bash
   pip install beautifulsoup4 requests
   ```

2. **Run the script**

   ```bash
   python your_script_name.py
   ```

3. **Check output folders**

   * Images will be in `static/images/{url_page}/slider_#`.

---

## 📦 Dependencies

* `beautifulsoup4`
* `requests`

Install via pip if needed.

---

## 🧼 Cleanup Logic

Before downloading, the script deletes all folders matching `slider_*` in the destination folder.

---

## 📄 Notes

* Start markers in `start_sequence` **define the beginning of a new group** and are excluded from the downloads.
* Non-image tags or malformed sources are ignored silently.

---

## 📂 Example Hugo Front Matter

This can be auto-generated or created manually to reference downloaded images:

```toml
+++
title = "Gallery Page"
layout = "swiper/swiper-gallery"
swiperImages1 = ["images/rv-service/slider_1/img1.jpg", ...]
swiperImages2 = ["images/rv-service/slider_2/img1.jpg", ...]
+++
```

---

## 🛠️ License

MIT or similar. You are free to adapt and use this script in your projects.

```

Let me know if you'd like this to include auto-generation of the Hugo front matter too.
```
