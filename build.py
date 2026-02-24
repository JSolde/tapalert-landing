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
    
    # We do NOT rewrite .html links here anymore. 
    # Relative .html links naturally point to translations within the current dir (e.g., es/quickstart_android.html).

    # Fix same-language switcher links: href="es/page.html" → href="page.html"
    html = re.sub(
        r'href="' + re.escape(lang) + r'/([a-zA-Z_0-9][^"]*)"',
        r'href="\1"',
        html
    )
    return html


def generate_lang_switcher(current_lang, html_file):
    """Generate language switcher HTML for insertion into the nav."""
    
    LANG_SWITCHER_CSS = """
<style>
.lang-dropdown { position: relative; display: inline-block; margin-left: 20px; }
.lang-dropbtn { background: rgba(255, 255, 255, 0.8); color: #2c3e50; padding: 8px 16px; font-size: 0.85rem; font-weight: 700; border: 1px solid rgba(102, 126, 234, 0.2); border-radius: 50px; cursor: pointer; display: flex; align-items: center; gap: 8px; transition: all 0.3s ease; text-transform: uppercase; }
.lang-dropbtn:hover { background: white; border-color: #667eea; box-shadow: 0 4px 12px rgba(102, 126, 234, 0.15); }
.lang-dropbtn::after { content: '▾'; font-size: 0.7rem; opacity: 0.5; }
.lang-dropdown-content { display: none; position: absolute; right: 0; top: calc(100% + 10px); background-color: white; min-width: 120px; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12); border-radius: 12px; z-index: 1001; overflow: hidden; border: 1px solid rgba(0, 0, 0, 0.05); animation: fadeInDown 0.3s ease-out; }
@keyframes fadeInDown { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
.lang-dropdown:hover .lang-dropdown-content { display: block; }
.lang-dropdown-content a { color: #4a5568; padding: 10px 16px; text-decoration: none; display: flex; align-items: center; justify-content: space-between; font-size: 0.85rem; font-weight: 600; transition: background 0.2s; text-transform: uppercase; }
.lang-dropdown-content a:hover { background-color: #f7fafc; color: #667eea; }
.lang-dropdown-content a.active { color: #667eea; background-color: #edf2f7; }
.lang-dropdown-content a.active::after { content: '✓'; color: #667eea; font-size: 0.8rem; }
@media (max-width: 768px) {
    .lang-dropdown { margin: 15px 0 0 0; }
    .lang-dropdown-content { position: static; display: flex; flex-direction: row; background: none; box-shadow: none; border: none; justify-content: center; gap: 10px; }
    .lang-dropbtn { display: none; }
    .lang-dropdown-content { display: flex; }
    .lang-dropdown-content a { padding: 6px 12px; border: 1px solid rgba(102, 126, 234, 0.2); border-radius: 50px; background: white; }
}
</style>
"""

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
        LANG_SWITCHER_CSS,
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
