# Hugo CI/CD Deployment with GitHub Actions to Bluehost

This setup describes how to deploy a Hugo site hosted on GitHub to a subfolder on Bluehost using SSH and GitHub Actions. It also includes instructions for overriding a theme partial to enable SASS support during build.

---

## 📁 Project Structure Notes

* Hugo repo: `bear_hugo_hero_theme`
* Theme: Git submodule at `themes/hugo-arcana`
* Deployment folder: `public_html/hugo/` on Bluehost

---

## ✅ GitHub Action Workflow (`.github/workflows/deploy.yml`)

```yaml
yaml
name: Deploy to Bluehost via SSH

on:
  push:
    branches:
      - master

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Install Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: '0.125.4'
          extended: true

      - name: Build site
        run: hugo --baseURL "https://cabear.com/hugo/"

      - name: Deploy to Bluehost via SSH
        run: |
          mkdir -p ~/.ssh
          echo "${{ secrets.SSH_PRIVATE_KEY }}" > ~/.ssh/id_ed25519
          chmod 600 ~/.ssh/id_ed25519
          ssh-keyscan cabear.com >> ~/.ssh/known_hosts
          rsync -avz --delete public/ eogoaomy@cabear.com:~/public_html/hugo/
```

---

## 🔐 SSH Key Setup

1. Generate a new SSH key pair (or use existing)
2. Add the public key (`id_ed25519.pub`) to `~/.ssh/authorized_keys` on Bluehost
3. Add the **private key** to GitHub Secrets as `SSH_PRIVATE_KEY`

---

## 🧠 Overriding Theme Partial for SASS Compatibility

The Arcana theme uses a Hugo SASS pipeline in `head.html`. If you override this in your local repo to fix build errors, place this at:

```bash
layouts/partials/head/head.html
```

And use:

```go
{{ $options := (dict "targetPath" "style.css" "outputStyle" "compressed" "enableSourceMap" .Site.Params.enableSourceMaps) }}
{{ $style := resources.Get "sass/main.scss" | resources.ExecuteAsTemplate "main.scss" . | resources.ToCSS $options }}
<link rel="stylesheet" href="{{ $style.RelPermalink }}" />
```

> Ensure the full path to your `sass/main.scss` exists under `themes/hugo-arcana/assets/` or is overridden locally.

---

## 🌐 Deployment Target

Final site will be live at:

```
https://cabear.com/hugo/
```

You can later move the baseURL to `/` if deploying to root.

---

## 📝 Notes

* Git submodules must be initialized in the GitHub Action environment
* CI/CD triggers on `git push` to `master`
* `.gitignore` should exclude `/public` and `resources/`

---

Let me know if you want this documented for the root domain or if you're ready to add live preview deploys or Netlify fallback.
