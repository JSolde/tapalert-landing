
import json
import os
import concurrent.futures
from deep_translator import GoogleTranslator
import time

def translate_batch(texts, target_lang):
    translator = GoogleTranslator(source='en', target=target_lang)
    translated = []
    for text in texts:
        if not text.strip() or text.strip() == "":
            translated.append(text)
            continue
        try:
            res = translator.translate(text)
            translated.append(res)
        except Exception as e:
            print(f"Error translating '{text[:20]}...': {e}")
            translated.append(text)
        time.sleep(0.1)
    return translated

def process_lang(target_lang):
    print(f"Processing {target_lang}...")
    with open('locales/en.json', 'r') as f:
        en_data = json.load(f)
    
    out_path = f'locales/{target_lang}.json'
    if os.path.exists(out_path):
        with open(out_path, 'r') as f:
            target_data = json.load(f)
    else:
        target_data = {}

    keys_to_translate = [k for k in en_data.keys() if k not in target_data]
    if not keys_to_translate:
        print(f"No new keys to translate for {target_lang}")
        return

    print(f"Translating {len(keys_to_translate)} keys for {target_lang}...")
    
    batch_size = 10
    batches = [keys_to_translate[i:i + batch_size] for i in range(0, len(keys_to_translate), batch_size)]
    
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_batch = {executor.submit(translate_batch, [en_data[k] for k in batch], target_lang): batch for batch in batches}
        for future in concurrent.futures.as_completed(future_to_batch):
            batch_keys = future_to_batch[future]
            try:
                translated_texts = future.result()
                for i, key in enumerate(batch_keys):
                    results[key] = translated_texts[i]
            except Exception as e:
                print(f"Batch failed: {e}")
    
    target_data.update(results)
    final_data = {k: target_data.get(k, en_data[k]) for k in en_data.keys()}
    
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, indent=4, ensure_ascii=False)
    print(f"Finished {target_lang}")

if __name__ == "__main__":
    process_lang('nl')
