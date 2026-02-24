# Translation & Content Management Guide

This project uses a simple Static Site Generation (SSG) system to handle translations and content across multiple languages.

## Project Structure

- **`src/`**: Contains the source HTML templates. These files use `{{ key }}` placeholders for translatable text.
- **`locales/`**: Contains JSON files for each supported language (e.g., `en.json`, `es.json`, `ca.json`).
- **`build.py`**: The Python script that merges templates and locales to generate the final website.
- **Root directory & subdirectories**: The generated HTML files are placed in the root (for English) and in language-specific subdirectories (e.g., `/es/`, `/gl/`).

---

## How to Change Existing Text

1. **Locate the text**: Find the text you want to change in the website.
2. **Find the key**: Open `locales/en.json` (or any other locale file) and search for that text to find its corresponding **key**.
3. **Update the value**: Change the text value for that key in the relevant `.json` files in the `locales/` directory.
4. **Rebuild**: Run the build script to apply the changes:
   ```bash
   python3 build.py
   ```

---

## How to Add New Translatable Text

1. **Update the Template**: In the relevant HTML file within `src/`, add a placeholder where you want the new text to appear:
   ```html
   <p>{{ my_new_text_key }}</p>
   ```
2. **Add to Locales**: Add the new key and its translation to **every** JSON file in the `locales/` directory:
   ```json
   "my_new_text_key": "Your translated text here"
   ```
   > [!IMPORTANT]
   > Make sure to add the key to all languages to avoid "missing key" errors or empty spaces on built pages.
3. **Rebuild**: Run the build script:
   ```bash
   python3 build.py
   ```

---

## How to Add a New Language

1. **Create Locale File**: Create a new JSON file in the `locales/` directory using the ISO language code (e.g., `fr.json` for French).
2. **Translate**: Copy the contents of `en.json` into your new file and translate the values.
3. **Rebuild**: Run the build script:
   ```bash
   python3 build.py
   ```
   The script will automatically detect the new file, create a corresponding subdirectory, and generate the translated pages.

---

## Technical Details

- **Nested Keys**: The build script resolves placeholders twice, allowing you to use one key inside another (e.g., `"greeting": "Hello {{ name }}"`).
- **Path Handling**: The script automatically fixes relative paths (like images and CSS) when building pages into subdirectories.
- **Language Switcher**: The dropdown menu in the navigation is automatically generated based on the files found in `locales/`.
