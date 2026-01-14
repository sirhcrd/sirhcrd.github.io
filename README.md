# Free Web Tools

🛠️ A collection of client-side file viewers that respect your privacy.

[![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-blue)](https://sirhcrd.github.io)
[![Privacy](https://img.shields.io/badge/Privacy-100%25-green)](https://sirhcrd.github.io)

## 🔒 Privacy First

All tools run **entirely in your browser**. Your files **never leave your computer**. No uploads, no servers, no tracking. Just pure client-side processing using the browser's File API.

## 🎯 Available Tools

### 📝 [Markdown Viewer](https://sirhcrd.github.io/markdown-viewer.html)

View your Markdown files with beautiful formatting and syntax highlighting.

**Features:**
- ✨ Instant markdown rendering
- 🎨 GitHub-style formatting
- 💻 Code syntax highlighting
- 📊 Table support
- 📱 Responsive design

**Usage:** Click "Browse for File", select a `.md` file from your computer, and view it instantly.

---

## 🧳 Europe Trip Itinerary (How It Works)

The itinerary page is a small “Markdown-to-HTML” renderer:

- Page: `europe_family_trip_2026.html`
- Source content: `europe_family_trip_itinerary_draft.md`

On load, the HTML page fetches the Markdown file and renders it in-browser using the `marked` library.

### Local viewing

Browsers often block `fetch()` when opening the HTML via `file://`.

Run a quick local server from the repo folder:

- `python3 -m http.server 8000`
- Visit `http://localhost:8000/europe_family_trip_2026.html`

### “Always show latest” caching behavior

GitHub Pages/CDNs/browsers can cache HTML/MD aggressively.

To avoid stale renders, the itinerary page fetches the Markdown with a cache-busting query string:

- `europe_family_trip_itinerary_draft.md?v=<timestamp>`

The homepage button also appends `?v=<timestamp>` when linking to the itinerary page.

---

## 🚀 GitHub Pages Deployment Notes (Important)

This repo is a user GitHub Pages site (`sirhcrd.github.io`). GitHub Pages deploys from whatever branch is configured in **Repo Settings → Pages**.

### Symptom we hit

- Changes were pushed to `main`, but the live site didn’t update.

### Root cause

- Pages was effectively serving from `master` (or at least not from `main`).

### Fix options

Pick one and stick to it:

1) **Make Pages deploy from `main`**
	- GitHub → Settings → Pages → Source: “Deploy from a branch” → Branch: `main` (root)

2) **Keep Pages deploying from `master` and merge `main` → `master` for releases**
	- Example commands:
	  - `git checkout master`
	  - `git merge --no-ff main -m "Merge main into master for Pages"`
	  - `git push origin master`

If the site ever “stops updating again”, the first thing to check is: **which branch Pages is deploying**.


### 📊 [JSON Log Viewer](https://sirhcrd.github.io/json-log-viewer.html)

Parse and visualize JSON log files with pretty-printing and syntax highlighting.

**Features:**
- 🎨 Pretty-print JSON formatting
- 🌈 Syntax highlighting for keys, strings, numbers, booleans
- 📖 Easy-to-read display
- 🔍 Expandable structure
- 📋 Copy-friendly output

**Usage:** Click "Browse for JSON File", select a `.json` file from your computer, and view it formatted.

---

## 🚀 Getting Started

1. Visit [https://sirhcrd.github.io](https://sirhcrd.github.io)
2. Choose the tool you need
3. Browse for your file
4. View your content instantly!

## 💡 Why Use These Tools?

- **No Installation Required** - Works directly in your browser
- **Cross-Platform** - Works on Windows, Mac, Linux
- **Offline Capable** - Save the HTML files and use them offline
- **Free Forever** - Open source and free to use
- **Secure** - No data ever leaves your machine

## 🛠️ Technical Details

These tools are built with:
- Pure HTML, CSS, and JavaScript
- No external dependencies (except CDN for markdown rendering)
- Uses browser's native File API for local file access
- Client-side processing only

## 📜 License

MIT License - Feel free to use, modify, and distribute.

## 🤝 Contributing

Found a bug or have a feature request? Feel free to open an issue or submit a pull request!

## 📞 Contact

Created by [@sirhcrd](https://github.com/sirhcrd)

---

**⭐ If you find these tools useful, consider giving this repo a star!**
