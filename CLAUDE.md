# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A static landing site for the TapAlert app (an Android emergency-alerting / panic-button app). The site is bilingual (English + Spanish) and deployed as a GitHub Pages site (`CNAME` → tapalert domain).

## Build System

Templates live in `src/` with `{{ key }}` placeholders. Translation strings live in `locales/en.json` and `locales/es.json` (and any future `locales/fr.json`, etc.). The build script auto-discovers all locale files and writes:

- English → root directory (e.g. `index.html`, `user_guide.html`, …)
- Other languages → `/{lang}/` subdirectory (e.g. `es/index.html`, …)

**Build the site:**
```bash
python3 build.py
```

`build.py` handles:
- Relative-path fixups for subdirectory languages (prefixing `../` to internal links and `media/` asset references)
- Injecting `{{ html_lang }}` (the current language code for `<html lang="">`)
- Injecting `{{ hreflang_tags }}` (SEO `<link rel="alternate">` tags in `<head>`)
- Injecting `{{ lang_switcher }}` (language switcher links in the nav)

**To add a new language** (e.g. French): create `locales/fr.json` with the same keys as `en.json` and run `build.py`. A `fr/` directory will be generated automatically.

## Editing Content

**Always edit the template in `src/`, never the output files in the root or `es/`.** After editing a template, re-run `build.py` to regenerate all output files.

To add or change translatable text:
1. Add/update the key in **all** locale files (`locales/en.json`, `locales/es.json`, …)
2. Use `{{ key }}` in the `src/*.html` template
3. Run `python3 build.py`

### Special build-time placeholders (injected by `build.py`, not in locale files)
| Placeholder | Purpose |
|---|---|
| `{{ html_lang }}` | Language code for `<html lang="…">` |
| `{{ hreflang_tags }}` | SEO alternate link tags for `<head>` |
| `{{ lang_switcher }}` | Language switcher `<div>` for the nav |

## Recovery / Utility Scripts

- `recover_index.py` – copies root HTML files back into `src/` (used when templates need to be reconstructed from built output)
- `restore_templates.py` – back-fills `{{ key }}` placeholders into `src/` files using git HEAD as a clean source, then applies chrome key substitutions. Only applies multi-word phrases (≥ 10 chars) to avoid false matches in CSS/guide body text.

## Site Structure

All pages are self-contained HTML files (inline CSS + JS, no external build toolchain). Pages:

| File | Purpose |
|---|---|
| `index.html` | Main landing page |
| `user_guide.html` | Full app user guide |
| `quickstart_android.html` | Quick-start guide |
| `troubleshooting.html` | Troubleshooting guide |
| `twilio_guide.html` | Twilio SMS setup guide |
| `email_redundancy_guide.html` | Email redundancy setup |
| `accessibility_guide.html` | Accessibility features for seniors |
| `one_tap_alert.html` | One-tap alert feature explanation |
| `sms_stand_out.html` | SMS feature explanation |
| `contact.html` | Contact page |
| `terms.html` | Terms of service |
| `PRIVACY_POLICY.html` | Privacy policy |

Corresponding Markdown source docs (e.g. `USER_GUIDE.md`, `TROUBLESHOOTING.md`) exist as authoring sources for the HTML guides.

## Internationalization Notes

- The `es/` directory mirrors the root structure but with Spanish content.
- Language switcher links in templates use `href="es/<page>.html"` for the Spanish variant; `build.py` rewrites these to relative paths when generating the `es/` output.
- Both locale JSON files must have identical keys; missing keys will leave `{{ key }}` literals in the output.
