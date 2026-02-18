
import glob
import re

html_files = glob.glob('/Users/jordisoldevila/tapalert-landing/*.html')

# Regex to find tags.
# This splits the content into [text, tag, text, tag, ...].
tag_pattern = re.compile(r'(<[^>]+>)')

def process_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = tag_pattern.split(content)
    
    new_parts = []
    
    # State tracking
    skip_mode = False # True if inside title, script, style, textarea
    
    # Simple heuristic check for tag names
    # We trigger skip on <title, <script, <style, <textarea
    # We End skip on </title, </script, </style, </textarea
    
    skip_tags_start = re.compile(r'^<((title)|(script)|(style)|(textarea))', re.IGNORECASE)
    skip_tags_end = re.compile(r'^</((title)|(script)|(style)|(textarea))', re.IGNORECASE)

    for part in parts:
        if part.startswith('<'):
            # It's a tag (or comment, or doctype)
            new_parts.append(part)
            
            # Update state
            if skip_tags_start.match(part):
                skip_mode = True
            elif skip_tags_end.match(part):
                skip_mode = False
        else:
            # It's text
            if skip_mode:
                new_parts.append(part)
            else:
                # Safe to replace
                if "TapAlert" in part:
                    # Avoid double wrapping if I ran this partially before? 
                    # User said "cannot see", so likely clean.
                    # But checking just in case:
                    if '<span class="notranslate" translate="no">TapAlert</span>' in part:
                         new_parts.append(part)
                    else:
                         replaced = part.replace('TapAlert', '<span class="notranslate" translate="no">TapAlert</span>')
                         new_parts.append(replaced)
                else:
                    new_parts.append(part)

    new_content = ''.join(new_parts)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"No changes in {file_path}")

for file in html_files:
    process_file(file)
