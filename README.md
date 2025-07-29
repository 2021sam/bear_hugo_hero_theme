# Bear Hugo Hero Theme 🐻🚀

A Hugo-powered static website for **Bear**, built using the [Hero theme](https://themes.gohugo.io/themes/hugo-hero-theme/).  
This site includes a large homepage slider and multiple sliders across content pages, with content migrated from WordPress XML exports to markdown.

---

## 📦 Features

- ✅ **Hero Theme** layout
- ✅ **WordPress to Hugo** content migration via `exitwp`
- ✅ Optimized **Markdown content**
- ✅ Image support and sliders
- ✅ Clean and minimal responsive design
- ✅ Git-friendly project structure

---

## 🛠️ Getting Started

```bash
git clone https://github.com/your-username/bear_hugo_hero_theme.git

git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
git submodule add https://github.com/half-duplex/hugo-arcana.git themes/hugo-arcana

cd bear_hugo_hero_theme
hugo server
hugo server -D --disableFastRender --noHTTPCache --bind 0.0.0.0
hugo server -D --noHTTPCache --bind 0.0.0.0 --port 1313 --baseURL http://10.0.0.88:1313
```

## 🛠️ Bluehost Server

```bash
hugo --baseURL="https://cabear.com/hugo/" --cleanDestinationDir
```


bear_hugo_hero_theme/
├── content/             # All page and post markdown files
├── static/              # Static assets (images, CSS, JS)
├── layouts/             # Custom Hugo layouts
├── archetypes/          # Archetype templates
├── hugo.toml            # Site configuration
├── README.md
└── .gitignore


📸 Credits

    Hero Theme

    Exitwp-for-Hugo


💡 Notes

    Be sure to name index files as _index.md for Hugo to treat them as section pages.

    Use static/images/ for local image references in markdown.

    Customize the layouts/ directory to override theme components as needed.

push excuse 2