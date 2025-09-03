# The Leaky Wader

Welcome to the U.S. Fish & Wildlife Service's Yakima Basin newsletter site. This repository hosts the static web pages for **The Leaky Wader**, a Monthly peek behind the scenes of our fish management program.

## What you'll find here

- **Landing page** – `index.html` displays the hero image and link into the site.
- **Navigation** – `home.html` introduces the program and links to current content.
- **Metrics dashboard** – `data.html` shows basic program metrics using Chart.js.
- **Newsletter index** – `newsletter.html` lists every issue of The Leaky Wader.
- **Reports** – `reports.html` links to annual project reports and summaries.
- **Issues** – each newsletter issue lives in its own folder under `issues/`.
- **Assets** – graphics and logos are organized under `assets/`.

All links use relative paths so you can drop these files onto any web server or open them directly in your browser.

## Adding a new issue

1. Create a folder in `issues/` named for the issue (e.g. `Jan2026`).
2. Add your HTML file and any images used by that issue inside the folder.
3. Update `newsletter.html` to link to the new issue.

## Local development

Because it's a fully static site, you can preview everything with a tiny HTTP server:

```bash
# from the repository root
python3 -m http.server
```

Then visit [http://localhost:8000](http://localhost:8000) and click around!

---

Happy wading!

