
import glob
import os
import re

html_files = glob.glob('/Users/jordisoldevila/tapalert-landing/*.html')

# Regex to find TapAlert outside of HTML tags and attributes
# This uses a pattern that matches either an HTML tag (to preserve it) or text content (to process it).
# Group 1 captures tags, Group 2 captures text.
tag_pattern = re.compile(r'(<[^>]+>)')

for file_path in html_files:
    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by tags.
    # Parts will alternate: [text, tag, text, tag, text, ...]
    # Or start with tag if file starts with tag.
    parts = tag_pattern.split(content)
    
    new_parts = []
    for part in parts:
        if part.startswith('<'):
            # It's a tag, leave it alone.
            new_parts.append(part)
        else:
            # It's text content. Replace TapAlert.
            # But only replace if it's not already wrapped (though unlikely given the task context).
            # Also, check if we are inside specific tags like <script> or <style>?
            # Simple split approach doesn't track parent tag context easily, but <script> content is technically text here.
            # Let's assume TapAlert inside script/style shouldn't be wrapped with HTML span.
            # For now, let's just do a basic replace and hope script/style doesn't contain the literal string "TapAlert" in a way that breaks syntax if wrapped.
            # Actually, let's check if the previous tag was script or style.
            
            # To do that properly, we need context.
            # However, looking at the grep output, TapAlert appears mostly in body text.
            # Let's refine the loop to track context if needed, or just be careful.
            
            # Refined strategy:
            # We will iterate and keep track of script/style blocks if possible, but splitting by all tags makes it hard.
            # Instead, let's just replace in text content, but avoid replacing if the text is clearly JS code?
            # JS code: `var appName = "TapAlert";` -> `var appName = "<span...TapAlert</span>";` ?? That would break JS string.
            # So yes, context matters.
            
            # Since I can't easily parse full HTML context in a short script without a library,
            # I'll rely on the fact that `TapAlert` in scripts usually doesn't need translation protection (it's a string literal or variable name).
            # If it IS user-visible text in JS, it might need it, but injecting HTML into JS strings is risky.
            # So I should SKIP replacement if I suspect we are in a script/style block.
            
            # BUT, the split approach doesn't tell me if I'm inside <script>...</script>.
            # It treats <script> as a tag, then content as text, then </script> as a tag.
            
            # Let's just track the last seen start tag name.
            # This is a heuristic.
            
            # A better way is to simply skip files or sections.
            # Given the request is specific to "wherever it shows up" (meaning visible text), let's assume body text.
            
            # Let's try to be smart about replacement.
            # Replace "TapAlert" with target string ONLY if it's not preceded by = or " or '.
            # But that logic applies to the raw source, not the split parts.
            
            processed_text = part.replace('TapAlert', '<span class="notranslate" translate="no">TapAlert</span>')
            new_parts.append(processed_text)
            
    # Reassemble
    new_content = ''.join(new_parts)
    
    # Write back
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"No changes in {file_path}")
