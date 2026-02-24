import json
with open('locales/en.json') as f: en = json.load(f)
with open('locales/es.json') as f: es = json.load(f)

missing_in_es = [k for k in en if k not in es]
missing_in_en = [k for k in es if k not in en]
print("Missing in es.json:")
for k in missing_in_es: print(" -", k, "=", repr(en[k]))
print("Missing in en.json:")
for k in missing_in_en: print(" -", k, "=", repr(es[k]))
