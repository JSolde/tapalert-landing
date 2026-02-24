import json
import os

def update_locales():
    with open('locales/en.json', 'r') as f:
        en = json.load(f)
    with open('locales/es.json', 'r') as f:
        es = json.load(f)

    # List of terms the user wrapped in notranslate spans
    terms = ["TapAlert", "Twilio", "SOS", "Direct SMS", "fallback", "Premium", "Reporting mode"]
    
    for term in terms:
        span = f'<span class="notranslate" translate="no">{term}</span>'
        # we don't blind replace in keys, only in values
        for d in [en, es]:
            for k, v in d.items():
                if isinstance(v, str) and term in v and span not in v:
                    d[k] = v.replace(term, span)
                    
    # lower case terms
    smart_red = "smart redundancy"
    es_smart_red = "redundancia inteligente"
    # In english:
    for k, v in en.items():
        if isinstance(v, str):
            en[k] = v.replace("smart redundancy", '<span class="notranslate" translate="no">smart redundancy</span>')
    for k, v in es.items():
        if isinstance(v, str):
            es[k] = v.replace("redundancia inteligente", '<span class="notranslate" translate="no">redundancia inteligente</span>')

    with open('locales/en.json', 'w') as f:
        json.dump(en, f, indent=4)
        print("Updated locales/en.json")
    with open('locales/es.json', 'w') as f:
        json.dump(es, f, indent=4)
        print("Updated locales/es.json")

update_locales()
