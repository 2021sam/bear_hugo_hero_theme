Here's a clean, user-friendly `README.md` that explains how to use the `showcase` shortcode in your Hugo site:

---

## 📸 Hugo Swiper Showcase Shortcode

This project includes a custom shortcode to display Swiper-based image galleries with animated logos, titles, and descriptions. You can now easily embed a reusable showcase slider into any markdown content.

---

### 🔧 Prerequisites

* Hugo site with this setup cloned or integrated.
* Required partials and Swiper.js integration already included.
* Your site’s data file (`data/swipers/showcase.yaml`, `.json`, or `.toml`) should be populated properly. See below for structure.

---

### 🚀 How to Use the `showcase` Shortcode

Use the following syntax in any markdown content file:

```markdown
{{< showcase index="1" data="showcase" >}}
```

#### Parameters:

* `index`: The numeric ID of the swiper set to show (e.g. `1`, `2`, `3`)
* `data`: The name of the data file to pull from in `data/swipers/` (e.g. `showcase`, `gallery`)

---

### 📁 Example Data File: `data/swipers/showcase.yaml`

```yaml
swiper_images_1:
  header: "Project One"
  description: "Description of the first showcased project."
  images:
    - "/images/showcase/project1-1.jpg"
    - "/images/showcase/project1-2.jpg"

swiper_images_2:
  header: "Project Two"
  description: "Second project's highlights."
  images:
    - "/images/showcase/project2-1.jpg"
    - "/images/showcase/project2-2.jpg"
```

---

### ✨ Example Usage in a Content File

```markdown
+++
title = "Showcase Gallery Page"
layout = "swiper-showcase"
+++

Welcome to the Showcase!

{{< showcase index="1" data="showcase" >}}
{{< showcase index="2" data="showcase" >}}
{{< showcase index="3" data="showcase" >}}
```

> 💡 The layout `swiper-showcase` automatically includes the required JavaScript from Swiper to initialize the sliders. No additional scripts are needed in your content files.

---

### 🧩 Folder Structure Overview

```
layouts/
├── shortcodes/
│   └── showcase.html
├── partials/
│   └── swiper/
│       ├── showcase.html
│       └── init.html
├── _default/
│   └── swiper-showcase.html

data/
└── swipers/
    └── showcase.yaml
```

---

### 🛠️ Customization

* Modify `partials/swiper/showcase.html` to change HTML layout, animations, or Swiper settings.
* Adjust Swiper behavior (slidesPerView, loop, etc.) in `partials/swiper/init.html`.

---

### ✅ Final Notes

* Images must be in your `static/` directory or use a full path.
* Each `index` must have a corresponding `swiper_images_<index>` block in your data file.
* This shortcode works best when Swiper styles and JS are properly loaded via CDN or locally.

---

Let me know if you want the README in plain text, or formatted for Hugo Docs-style sites!
