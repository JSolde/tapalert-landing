"""
restore_templates.py

Restores clean guide-page templates in src/ from the git-committed HTML files.
Applies {{ key }} substitutions ONLY to text content (skips <style> and <script> blocks).
Also adds shared chrome placeholders: {{ html_lang }}, {{ hreflang_tags }}, {{ lang_switcher }}.
"""
import os
import re
import json
import subprocess

with open('locales/en.json') as f:
    en_dict = json.load(f)

# Sort keys by value length descending so longer strings match first (prevents partial overlaps)
sorted_keys = sorted(en_dict.keys(), key=lambda k: len(en_dict[k]), reverse=True)

# Files to restore from git HEAD (index.html is already properly templated — skip it)
guide_files = [f for f in os.listdir('.') if f.endswith('.html') and os.path.isfile(f) and f != 'index.html']

os.makedirs('src', exist_ok=True)


def split_on_style_script(html):
    """
    Split HTML into alternating sections: [content, style/script, content, style/script, ...]
    Returns list of (is_code_block, text) tuples.
    """
    pattern = re.compile(r'(<(?:style|script)[^>]*>.*?</(?:style|script)>)', re.DOTALL | re.IGNORECASE)
    parts = pattern.split(html)
    result = []
    for i, part in enumerate(parts):
        is_code = bool(re.match(r'<(?:style|script)', part, re.IGNORECASE))
        result.append((is_code, part))
    return result


def protect_placeholders(html):
    """Temporarily replace {{ key }} with sentinels so they aren't re-substituted."""
    sentinels = {}
    def _sub(m):
        s = f'__PLACEHOLDER_{len(sentinels)}__'
        sentinels[s] = m.group(0)
        return s
    protected = re.sub(r'\{\{[^}]+\}\}', _sub, html)
    return protected, sentinels


def restore_placeholders(html, sentinels):
    for s, orig in sentinels.items():
        html = html.replace(s, orig)
    return html


def smart_replace(html, old, new):
    """Replace old with new only in non-style/non-script HTML text content.
    Also protects existing {{ key }} placeholders from being partially matched."""
    parts = split_on_style_script(html)
    out = []
    for is_code, part in parts:
        if is_code:
            out.append(part)
        else:
            # Protect existing {{ }} from the replacement
            protected, sentinels = protect_placeholders(part)
            protected = protected.replace(old, new)
            out.append(restore_placeholders(protected, sentinels))
    return ''.join(out)


def apply_chrome_placeholders(html, filename):
    """
    Replace hardcoded chrome strings with {{ key }} placeholders:
    - <html lang="en"> → <html lang="{{ html_lang }}">
    - Insert {{ hreflang_tags }} after <meta charset>
    - Insert {{ lang_switcher }} in the header
    - Footer keys
    - Guide navigation keys
    """
    # 1. html lang attribute
    html = re.sub(r'<html lang="[^"]*">', '<html lang="{{ html_lang }}">', html)

    # 2. hreflang tags (inject after first <meta charset> tag)
    html = re.sub(
        r'(<meta charset="[^"]*">)',
        r'\1\n    {{ hreflang_tags }}',
        html, count=1
    )

    # 3. lang_switcher — inject after the "Back to Home" button in guide page headers
    # Pattern: <a href="index.html" class="btn btn-primary">...</a>  followed by </nav> or </div>
    html = re.sub(
        r'(<a href="index\.html" class="btn btn-primary">[^<]*</a>)',
        r'\1\n        {{ lang_switcher }}',
        html, count=1
    )

    # 4. Footer shared strings → keys
    replacements = [
        # Footer section headings
        ('>Product<', '>{{ footer_product }}<'),
        ('>Legal<', '>{{ footer_legal }}<'),
        ('>Support<', '>{{ footer_support }}<'),
        # Footer links
        ('>Features<', '>{{ footer_features }}<'),
        ('>Pricing<', '>{{ footer_price }}<'),
        ('>Download<', '>{{ footer_download_h }}<'),
        ('>Privacy Policy<', '>{{ footer_privacy }}<'),
        ('>Terms of Service<', '>{{ footer_terms }}<'),
        ('>Contact<', '>{{ nav_contact }}<'),
        ('>FAQ<', '>{{ footer_faq }}<'),
        ('> Step by Step\n                                Guides<', '>{{ footer_guides }}<'),
        ('> Step by Step Guides<', '>{{ footer_guides }}<'),
        ('>Accessibility Guide<', '>{{ footer_a11y }}<'),
        ('>Troubleshooting<', '>{{ nav_troubleshooting }}<'),
        ('>Contact Support<', '>{{ footer_contact_support }}<'),
        # Footer tagline
        ('Simple emergency alerts for everyone. No subscriptions, no tracking, just safety.',
         '{{ footer_tagline }}'),
        # Footer copyright
        ('All rights reserved. | Made with ❤️ for your safety',
         '{{ footer_copyright }}'),
        # Guide back links
        ('>Back to Home<', '>{{ guide_back }}<'),
        ('>← Back to Guides<', '>{{ guide_back_guides }}<'),
        # Guide page "Need more help?" footer
        ('>Need more help?<', '>{{ ts_need_more }}<'),
    ]
    for old, new in replacements:
        html = html.replace(old, new)

    # 5. Page title keys (where they match existing key values)
    title_map = {
        '>Troubleshooting Guide<': '>{{ ts_h1 }}<',
        '>Quick Start (Android)<': '>{{ qs_h1 }}<',
        '>Quickstart Guide for Android<': '>{{ quickstart_h1 }}<',
        '>How to Make SMS Alerts Stand Out<': '>{{ sms_stand_out_title }}<',
    }
    for old, new in title_map.items():
        html = html.replace(old, new)

    return html


for filename in sorted(guide_files):
    # Get clean content from git HEAD
    result = subprocess.run(['git', 'show', f'HEAD:{filename}'], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  WARNING: Could not get {filename} from git HEAD, skipping")
        continue

    html = result.stdout

    # Apply chrome placeholders first (structural, not content substitutions)
    html = apply_chrome_placeholders(html, filename)

    # Apply locale key substitutions (text content only, skip CSS/JS).
    # Only apply multi-word phrases (single words are too risky for false matches).
    for key in sorted_keys:
        val = en_dict[key]
        if not val:
            continue
        # Skip single-word values — they match too broadly in CSS class names,
        # href anchors, and generic guide body text.
        if ' ' not in val.strip():
            continue
        # Also skip short phrases under 10 chars (still risky)
        if len(val.strip()) < 10:
            continue
        html = smart_replace(html, val, f'{{{{ {key} }}}}')

    dest = os.path.join('src', filename)
    with open(dest, 'w') as f:
        f.write(html)
    print(f"  Restored {filename} → src/{filename}")

print("\nDone. Run python3 build.py to rebuild the site.")
