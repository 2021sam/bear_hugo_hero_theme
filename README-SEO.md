Good question 👌 — the answer is **“it depends.”**

---

### 🔹 How Google chooses what to display in search results

1. **`<title>` tag (from your Hugo `title` front matter + template)**

   * This is *usually* what Google displays.
   * Example: if your template renders

     ```html
     <title>{{ .Title }} | {{ .Site.Params.brand_name }}</title>
     ```

     …then with your updated front matter you’d get:
     **RV, Truck & Auto Body Collision Repair in Hayward, CA | BEAR RV, Truck, Auto Body & Collision Repair Center**

2. **Google may rewrite it** if:

   * It thinks your title is too long (typically > 60–65 characters).
   * It thinks your title is missing relevant keywords.
   * It prefers using your H1 or anchor text from inbound links.
   * Example: in your screenshot earlier, Google was pulling **“BEAR Collision Center”** + a snippet instead of your full title.

3. **Meta description (`description` in front matter)**

   * Not a ranking factor, but controls the gray text snippet under your link (when Google chooses to use it).
   * If Google thinks another sentence on the page better matches the query, it will substitute that.

---

### 🔹 How to influence what Google shows

* Keep your **title**:

  * Under \~60 characters if possible (so it doesn’t get truncated).
  * Front-load the keywords individuals search (e.g., “RV Repair Hayward” before your brand).

* Example of a strong home title:
  **RV, Truck & Auto Body Repair in Hayward | BEAR Collision Center**
  → short, keyword-rich, still branded.

* Example of a strong RV Repair page title:
  **RV Collision Repair in Hayward, CA | BEAR RV, Truck, Auto Body & Collision Center**

* Meta description:
  Write natural, keyword-rich sentences (like we drafted earlier). Even if Google rewrites sometimes, having a good one helps.

---

✅ **Bottom line:**
Google *usually* uses your Hugo `title` (as rendered in `<title>`), but it may override it with H1 text or on-page copy if it thinks that’s clearer for the user’s search query. That’s why it’s best to **align your front matter `title`, your H1, and your intro text** so they all reinforce the same keywords/brand.

---

👉 Do you want me to propose a **title + H1 + meta description alignment** for your homepage and RV Repair page so Google has no reason to rewrite them?
