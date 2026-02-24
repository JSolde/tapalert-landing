import json

def update_locales(new_en, new_es):
    with open('locales/en.json', 'r') as f:
        en = json.load(f)
    with open('locales/es.json', 'r') as f:
        es = json.load(f)
    for k, v in new_en.items():
        en[k] = v
    for k, v in new_es.items():
        es[k] = v
    with open('locales/en.json', 'w') as f:
        json.dump(en, f, indent=4)
    with open('locales/es.json', 'w') as f:
        json.dump(es, f, indent=4)

en_keys = {
    "sms_so_title": "Make Your SMS Alert Stand Out",
    "sms_so_h1": "Making Alert SMS Stand Out",
    "sms_so_intro": "To ensure your emergency contacts don't miss your alert message among other notifications, we recommend configuring their phones to treat messages from your <span class=\"notranslate\" translate=\"no\">TapAlert</span> number differently.",
    "sms_so_h3_and": "For {{ android_table_th2 }} Recipients",

    "terms_p_last": "Last Updated: February 13, 2026",
    "terms_p1": "This app is not a replacement for emergency services. Message delivery and response depend on network availability and recipient action.",
    "terms_h2_1": "Delivery & availability disclaimer",
    "terms_p2": "Message delivery times may vary depending on carrier availability, recipient device status, network conditions, and geographic location. While SMS is a highly reliable communication channel, delivery cannot be guaranteed in all circumstances.",
    "terms_h2_2": "Emergency use disclaimer",
    "terms_p3": "This service is not a replacement for emergency services. In case of an emergency, users should contact local emergency authorities through official channels.",
    "terms_h2_3": "Consent & compliance",
    "terms_p4": "Users are responsible for ensuring they have obtained all necessary consents from recipients prior to sending SMS messages and for complying with applicable laws and regulations, including data protection and anti-spam requirements."
}

es_keys = {
    "sms_so_title": "Haz Que Tu SMS de Alerta Resalte",
    "sms_so_h1": "Haciendo Que tu SMS de Alerta Resalte",
    "sms_so_intro": "Para asegurarte de que tus contactos de emergencia no se pierdan tu mensaje de alerta entre otras notificaciones, recomendamos configurar sus teléfonos para que traten los mensajes de tu número de <span class=\"notranslate\" translate=\"no\">TapAlert</span> de manera diferente.",
    "sms_so_h3_and": "Para Destinatarios con {{ android_table_th2 }}",

    "terms_p_last": "Última Actualización: 13 de Febrero, 2026",
    "terms_p1": "Esta aplicación no reemplaza a los servicios de emergencia. La entrega de mensajes y la respuesta dependen de la disponibilidad de la red y de la acción del destinatario.",
    "terms_h2_1": "Descargo de responsabilidad de entrega y disponibilidad",
    "terms_p2": "Los tiempos de entrega de mensajes pueden variar dependiendo de la disponibilidad del operador, el estado del dispositivo del destinatario, las condiciones de la red, y la ubicación geográfica. Aunque el SMS es un canal de comunicación altamente confiable, su entrega no se puede garantizar en todas las circunstancias.",
    "terms_h2_2": "Descargo de responsabilidad por uso de emergencia",
    "terms_p3": "Este servicio no es un reemplazo a los servicios de emergencia. En caso de una emergencia real, los usuarios deben contactar a las autoridades locales de emergencia a través los canales oficiales.",
    "terms_h2_3": "Consentimiento y cumplimiento",
    "terms_p4": "Los usuarios son responsables de asegurarse de haber obtenido todos los consentimientos necesarios de los destinatarios antes de enviar mensajes SMS, y de cumplir con las leyes y regulaciones aplicables, incluidas las relativas a la protección de datos y requisitos contra el spam."
}

update_locales(en_keys, es_keys)

def replace_in_file(filepath, replacements):
    with open(filepath, 'r') as f:
        content = f.read()
    for old, new in replacements:
        content = content.replace(old, new)
    with open(filepath, 'w') as f:
        f.write(content)

sms_replacements = [
    ("<title>Make Your SMS Alert Stand Out - TapAlert</title>", "<title>{{ sms_so_title }} - TapAlert</title>"),
    ("<h1 class=\"guide-title\">Making Alert SMS Stand Out</h1>", "<h1 class=\"guide-title\">{{ sms_so_h1 }}</h1>"),
    ("<p>To ensure your emergency contacts don't miss your alert message among other notifications, we recommend\n            configuring their phones to treat messages from your <span class=\"notranslate\"\n                translate=\"no\">TapAlert</span> number differently.</p>", "<p>{{ sms_so_intro }}</p>"),
    ("<h3>For {{ android_table_th2 }} Recipients</h3>", "<h3>{{ sms_so_h3_and }}</h3>")
]

terms_replacements = [
    ("<p><strong>Last Updated: February 13, 2026</strong></p>", "<p><strong>{{ terms_p_last }}</strong></p>"),
    ("<p>This app is not a replacement for emergency services. Message delivery and response depend on network\n            availability and recipient action.</p>", "<p>{{ terms_p1 }}</p>"),
    ("<h2>Delivery & availability disclaimer</h2>", "<h2>{{ terms_h2_1 }}</h2>"),
    ("<p>Message delivery times may vary depending on carrier availability, recipient device status, network\n            conditions, and geographic location. While SMS is a highly reliable communication channel, delivery cannot\n            be guaranteed in all circumstances.</p>", "<p>{{ terms_p2 }}</p>"),
    ("<h2>Emergency use disclaimer</h2>", "<h2>{{ terms_h2_2 }}</h2>"),
    ("<p>This service is not a replacement for emergency services. In case of an emergency, users should contact local\n            emergency authorities through official channels.</p>", "<p>{{ terms_p3 }}</p>"),
    ("<h2>Consent & compliance</h2>", "<h2>{{ terms_h2_3 }}</h2>"),
    ("<p>Users are responsible for ensuring they have obtained all necessary consents from recipients prior to sending\n            SMS messages and for complying with applicable laws and regulations, including data protection and anti-spam\n            requirements.</p>", "<p>{{ terms_p4 }}</p>")
]

replace_in_file('src/sms_stand_out.html', sms_replacements)
replace_in_file('src/terms.html', terms_replacements)
print("Updated sms_stand_out.html and terms.html")
