import os
import json
import re

BASE_URL = "https://tapalert.app"

# Auto-discover all locale files
locales_dir = 'locales'
locales = {}
for fname in sorted(os.listdir(locales_dir)):
    if fname.endswith('.json'):
        lang = fname[:-5]
        with open(os.path.join(locales_dir, fname)) as f:
            locales[lang] = json.load(f)

if 'en' not in locales:
    print("Error: locales/en.json not found")
    exit(1)

all_langs = sorted(locales.keys())
other_langs = [l for l in all_langs if l != 'en']

# Ensure output directories exist for non-English languages
for lang in other_langs:
    os.makedirs(lang, exist_ok=True)

src_dir = 'src'
if not os.path.exists(src_dir):
    print(f"Error: Directory '{src_dir}' not found.")
    exit(1)

html_files = sorted([f for f in os.listdir(src_dir) if f.endswith('.html')])
print(f"Found {len(html_files)} HTML files. Languages: {', '.join(all_langs)}")


def fix_paths_for_subdir(html, lang):
    """Fix relative paths for pages built into a language subdirectory."""
    # Fix media asset references
    html = html.replace('src="media/', 'src="../media/')
    html = html.replace('href="media/', 'href="../media/')
    # Fix .html page links (skip anchors, external URLs, and already-prefixed paths)
    html = re.sub(
        r'href="(?!#|https?://|\.\./|' + re.escape(lang) + r'/)([a-zA-Z_0-9]+\.html[^"]*)"',
        r'href="../\1"',
        html
    )
    # Fix same-language switcher links: href="es/page.html" → href="page.html"
    html = re.sub(
        r'href="' + re.escape(lang) + r'/([a-zA-Z_0-9][^"]*)"',
        r'href="\1"',
        html
    )
    return html


def generate_lang_switcher(current_lang, html_file):
    """Generate language switcher HTML for insertion into the nav."""
    links = []
    for lang in all_langs:
        is_active = (lang == current_lang)
        active_class = " class=\"active\"" if is_active else ""
        
        if lang == 'en':
            href = f"../{html_file}" if current_lang != 'en' else f"{html_file}"
        else:
            href = f"../{lang}/{html_file}" if current_lang != 'en' else f"{lang}/{html_file}"
        
        links.append(f'<a href="{href}" hreflang="{lang}"{active_class}>{lang.upper()}</a>')
        
    dropdown_html = [
        '<div class="lang-dropdown">',
        f'    <button class="lang-dropbtn">{current_lang.upper()}</button>',
        '    <div class="lang-dropdown-content">',
        '        ' + '\n        '.join(links),
        '    </div>',
        '</div>'
    ]
    return '\n'.join(dropdown_html)


def generate_hreflang_tags(html_file):
    """Generate hreflang link tags for SEO, to be placed in <head>."""
    tags = []
    for lang in all_langs:
        if lang == 'en':
            url = f'{BASE_URL}/{html_file}'
        else:
            url = f'{BASE_URL}/{lang}/{html_file}'
        tags.append(f'<link rel="alternate" hreflang="{lang}" href="{url}">')
    tags.append(f'<link rel="alternate" hreflang="x-default" href="{BASE_URL}/{html_file}">')
    return '\n    '.join(tags)


def build_page(template_html, html_file, lang, translations):
    html = template_html

    # Inject build-time template variables (not in locale files)
    html = re.sub(r'\{\{\s*html_lang\s*\}\}', lang, html)
    html = re.sub(r'\{\{\s*hreflang_tags\s*\}\}', generate_hreflang_tags(html_file), html)
    html = re.sub(r'\{\{\s*lang_switcher\s*\}\}', generate_lang_switcher(lang, html_file), html)

    # Fix relative paths for subdirectory builds
    if lang != 'en':
        html = fix_paths_for_subdir(html, lang)

    # Apply locale substitutions
    for key, value in translations.items():
        html = re.sub(r'\{\{\s*' + re.escape(key) + r'\s*\}\}', str(value), html)

    return html


for html_file in html_files:
    src_path = os.path.join(src_dir, html_file)
    with open(src_path, 'r') as f:
        template_html = f.read()

    for lang, translations in locales.items():
        out_path = html_file if lang == 'en' else os.path.join(lang, html_file)
        with open(out_path, 'w') as f:
            f.write(build_page(template_html, html_file, lang, translations))

    print(f"  Built {html_file} ({len(locales)} languages)")

print(f"\nDone! {len(html_files)} pages × {len(locales)} language(s).")
