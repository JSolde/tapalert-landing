import json
import re

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
    print(f"Added {len(new_en)} keys to locales")

en_keys = {
    "contact_title": "Contact Support",
    "contact_h1": "Contact Support",
    "contact_intro": "We're here to help.",
    "contact_h2_1": "1. App Issues & Technical Support",
    "contact_p1": 'If you are experiencing issues with <span class="notranslate" translate="no">TapAlert</span> or have questions about how a feature works, please check our <a href="index.html#guides">Guides & FAQ</a> first. If you still need help, you can reach out directly via:',
    "contact_email": '<strong>Email:</strong> <a href="mailto:support@tapalert.app">support@tapalert.app</a>',
    "contact_h2_2": "2. Feedback & Feature Requests",
    "contact_p2": 'We are constantly looking to improve <span class="notranslate" translate="no">TapAlert</span>. If you have any suggestions, we\'d love to hear from you at <a href="mailto:feedback@tapalert.app">feedback@tapalert.app</a>.',
    "contact_h2_3": "3. Business Inquiries",
    "contact_p3": 'For partnerships, media, or other business-related matters, please contact <a href="mailto:business@tapalert.app">business@tapalert.app</a>.',

    "er_title": "Email Redundancy Guide",
    "er_h1": "Setting Up Email Redundancy",
    "er_h2_why": "Why Enable Email Redundancy?",
    "er_p_why_1": "Email redundancy is a crucial backup system.",
    "er_why_li1": '<strong>Zero Cellular Signal:</strong> If you are deep inside a building or in a remote area with Wi-Fi but absolutely no cellular coverage, standard SMS and <span class="notranslate" translate="no">Twilio</span> SMS might fail.',
    "er_why_li2": '<strong>International Travel:</strong> When traveling abroad without a roaming plan, SMS might be disabled, but hotel/cafe Wi-Fi can still send your alert.',
    "er_why_li3": '<strong>Carrier Outages:</strong> Protects against rare but possible cellular network outages.',
    "er_p_why_2": '<strong>How it works:</strong> First, the app attempts to send via <span class="notranslate" translate="no">Direct SMS</span> or <span class="notranslate" translate="no">Twilio</span>. If the device detects that these cellular methods have failed (or are impossible due to no signal), it will automatically attempt to send your alert via email.',
    "er_h2_how": "How to Configure It",
    "er_p_how_1": 'Email redundancy uses your existing email account (Gmail, Outlook, Yahoo, iCloud, etc.) to send the message. This requires <strong>SMTP settings</strong>.',
    "er_important_h4": "IMPORTANT: Use an \"App Password\"",
    "er_important_p": 'For security reasons, practically all major email providers now require you to use an <strong>App Password</strong> rather than your standard email password. An App Password is a unique 16-character code that allows a specific app (like <span class="notranslate" translate="no">TapAlert</span>) to send email without needing your main password or bypassing Two-Factor Authentication (2FA).',
    "er_h3_gmail": "Setup for Gmail Users",
    "er_gmail_step1": '<strong>Prerequisite:</strong> You must have <a href="https://myaccount.google.com/security" target="_blank">2-Step Verification</a> enabled on your Google Account.',
    "er_gmail_step2": "<strong>Generate App Password:</strong>",
    "er_gmail_step2_li1": 'Go to your <a href="https://myaccount.google.com/apppasswords" target="_blank">Google Account App Passwords</a> page.',
    "er_gmail_step2_li2": "If prompted, sign in.",
    "er_gmail_step2_li3": 'In the \'App name\' field, type <strong><span class="notranslate" translate="no">TapAlert</span></strong> and click <strong>Create</strong>.',
    "er_gmail_step2_li4": "A modal will appear with a 16-character password.",
    "er_gmail_step3": '<strong>Configure in <span class="notranslate" translate="no">TapAlert</span>:</strong>',
    "er_gmail_step3_li1": 'Open <span class="notranslate" translate="no">TapAlert</span> > <strong>Settings</strong> > <strong>Email Redundancy</strong>.',
    "er_gmail_step3_li2": "Toggle <strong>Enable Email Redundancy</strong> ON.",
    "er_gmail_step3_li3": "Tap the <strong>Gmail</strong> quick configuration button (this auto-fills Host to <code>smtp.gmail.com</code> and Port to <code>587</code>).",
    "er_gmail_step3_li4": "<strong>Username/Email:</strong> Enter your full Gmail address.",
    "er_gmail_step3_li5": "<strong>Password:</strong> Enter the 16-character App Password generated in Step 2. (Spaces don't matter).",
    
    "er_h3_outlook": "Setup for Outlook / Hotmail Users",
    "er_outlook_step1": "<strong>Prerequisite:</strong> Enable Two-Step Verification on your Microsoft Account.",
    "er_outlook_step2": "<strong>Generate App Password:</strong>",
    "er_outlook_step2_li1": 'Go to your <a href="https://account.live.com/proofs/manage/additional" target="_blank">Microsoft Account Security settings</a>.',
    "er_outlook_step2_li2": "Scroll down to <strong>App passwords</strong> and click <strong>Create a new app password</strong>.",
    "er_outlook_step2_li3": "Copy the generated password.",
    "er_outlook_step3": '<strong>Configure in <span class="notranslate" translate="no">TapAlert</span>:</strong>',
    "er_outlook_step3_li1": "Tap the <strong>Outlook</strong> quick config button in the app.",
    "er_outlook_step3_li2": "Enter your email and the generated App Password.",
    
    "er_h3_icloud": "Setup for iCloud Users",
    "er_icloud_step2_li1": 'Go to <a href="https://appleid.apple.com/account/manage" target="_blank">appleid.apple.com</a> and sign in.',
    "er_icloud_step2_li2": "In the Sign-In and Security section, click <strong>App-Specific Passwords</strong>.",
    "er_icloud_step2_li3": "Click <strong>Generate an app-specific password</strong> or the <strong>+</strong> button.",
    "er_icloud_step2_li4": 'Name it <strong><span class="notranslate" translate="no">TapAlert</span></strong> and click Create.',
    "er_icloud_step3_li1": "Tap the <strong>iCloud</strong> quick config button in the app.",
    
    "er_h3_yahoo": "Setup for Yahoo Users",
    "er_yahoo_step2_li1": 'Go to your <a href="https://login.yahoo.com/account/security" target="_blank">Yahoo Account Security page</a>.',
    "er_yahoo_step2_li2": "Click <strong>Generate app password</strong> or <strong>Manage app passwords</strong>.",
    "er_yahoo_step2_li3": "Select 'Other App' and name it <strong>TapAlert</strong>.",
    "er_yahoo_step2_li4": "Click Generate.",
    "er_yahoo_step3_li1": "Tap the <strong>Yahoo</strong> quick config button in the app.",
    
    "er_h2_ensure": "Ensuring Recipients Receive It",
    "er_p_ensure_1": 'If your recipients do not see the alert email, it might have been filtered into their <strong>Spam/Junk folder</strong>.',
    "er_ensure_li1": 'Ask your recipients to check their Spam folder.',
    "er_ensure_li2": 'Tell them to mark the email as <strong>"Not Spam"</strong>.',
    "er_ensure_li3": 'Have them add your sending email address to their contacts/VIP list.',
    "er_h2_test": "Testing the Connection",
    "er_p_test_1": "Before closing the settings, it is highly recommended to test your configuration:",
    "er_test_li1": "Tap the <strong>Test Connection</strong> button.",
    "er_test_li2": "Enter an email address to send a test message to.",
    "er_test_li3": 'If successful, you will see a "Connection Successful" message. If not, double-check your App Password and settings.'
}

es_keys = {
    "contact_title": "Contactar con Soporte",
    "contact_h1": "Contactar con Soporte",
    "contact_intro": "Estamos aquí para ayudar.",
    "contact_h2_1": "1. Problemas de la App y Soporte Técnico",
    "contact_p1": 'Si tiene problemas con <span class="notranslate" translate="no">TapAlert</span> o tiene preguntas sobre cómo funciona una función, consulte primero nuestras <a href="index.html#guides">Guías y Preguntas Frecuentes</a>. Si aún necesita ayuda, puede contactarnos directamente a través de:',
    "contact_email": '<strong>Correo:</strong> <a href="mailto:support@tapalert.app">support@tapalert.app</a>',
    "contact_h2_2": "2. Comentarios y Solicitudes de Funciones",
    "contact_p2": 'Buscamos mejorar constantemente <span class="notranslate" translate="no">TapAlert</span>. Si tiene alguna sugerencia, nos encantaría escucharla en <a href="mailto:feedback@tapalert.app">feedback@tapalert.app</a>.',
    "contact_h2_3": "3. Consultas Comerciales",
    "contact_p3": 'Para asociaciones, medios u otros asuntos relacionados con negocios, contáctenos en <a href="mailto:business@tapalert.app">business@tapalert.app</a>.',

    "er_title": "Guía de Redundancia de Correo",
    "er_h1": "Configurando la Redundancia de Correo",
    "er_h2_why": "¿Por qué Habilitar la Redundancia de Correo?",
    "er_p_why_1": "La redundancia de correo es un sistema de respaldo crucial.",
    "er_why_li1": '<strong>Sin Señal Celular:</strong> Si te encuentras en el interior de un edificio o en un área remota con Wi-Fi pero sin cobertura celular, el SMS estándar y el SMS de <span class="notranslate" translate="no">Twilio</span> pueden fallar.',
    "er_why_li2": '<strong>Viaje Internacional:</strong> Si viajas al extranjero sin un plan de roaming, los SMS podrían estar desactivados, pero el Wi-Fi de un hotel/cafetería aún puede enviar tu alerta.',
    "er_why_li3": '<strong>Cortes del Operador:</strong> Te protege contra cortes raros pero posibles en la red celular.',
    "er_p_why_2": '<strong>Cómo funciona:</strong> Primero, la aplicación intenta enviar por <span class="notranslate" translate="no">SMS Directo</span> o <span class="notranslate" translate="no">Twilio</span>. Si el dispositivo detecta que estos métodos celulares han fallado (o son imposibles por falta de señal), automáticamente intentará enviar la alerta por correo.',
    "er_h2_how": "Cómo Configurar",
    "er_p_how_1": 'La redundancia de correo utiliza tu cuenta de correo existente (Gmail, Outlook, Yahoo, iCloud, etc.) para enviar el mensaje. Esto requiere <strong>configuraciones SMTP</strong>.',
    "er_important_h4": "IMPORTANTE: Usa una \"Contraseña de Aplicación\"",
    "er_important_p": 'Por razones de seguridad, prácticamente todos los principales proveedores de correo ahora requieren el uso de una <strong>Contraseña de Aplicación</strong> en lugar de tu contraseña de correo estándar. Una Contraseña de Aplicación es un código único de 16 caracteres que permite a una aplicación específica (como <span class="notranslate" translate="no">TapAlert</span>) enviar correo sin necesitar tu contraseña principal ni eludir la Autenticación de Dos Factores (2FA).',
    "er_h3_gmail": "Configuración para Usuarios de Gmail",
    "er_gmail_step1": '<strong>Requisito previo:</strong> Debes tener habilitada la <a href="https://myaccount.google.com/security" target="_blank">Verificación en dos pasos</a> en tu Cuenta de Google.',
    "er_gmail_step2": "<strong>Generar Contraseña de Aplicación:</strong>",
    "er_gmail_step2_li1": 'Ve a la página de <a href="https://myaccount.google.com/apppasswords" target="_blank">Contraseñas de Aplicación de tu Cuenta de Google</a>.',
    "er_gmail_step2_li2": "Si se te solicita, inicia sesión.",
    "er_gmail_step2_li3": 'En el campo \'Nombre de la aplicación\', escribe <strong><span class="notranslate" translate="no">TapAlert</span></strong> y haz clic en <strong>Crear</strong>.',
    "er_gmail_step2_li4": "Aparecerá una ventana con una contraseña de 16 caracteres.",
    "er_gmail_step3": '<strong>Configurar en <span class="notranslate" translate="no">TapAlert</span>:</strong>',
    "er_gmail_step3_li1": 'Abre <span class="notranslate" translate="no">TapAlert</span> > <strong>Ajustes</strong> > <strong>Redundancia de correo</strong>.',
    "er_gmail_step3_li2": "Activa <strong>Activar redundancia de correo</strong>.",
    "er_gmail_step3_li3": "Toca el botón de configuración rápida de <strong>Gmail</strong> (esto completará automáticamente el Host como <code>smtp.gmail.com</code> y el Puerto como <code>587</code>).",
    "er_gmail_step3_li4": "<strong>Nombre de usuario/Correo:</strong> Ingresa tu dirección de correo de Gmail completa.",
    "er_gmail_step3_li5": "<strong>Contraseña:</strong> Ingresa la Contraseña de Aplicación de 16 caracteres generada en el Paso 2. (Los espacios no importan).",
    
    "er_h3_outlook": "Configuración para Usuarios de Outlook / Hotmail",
    "er_outlook_step1": "<strong>Requisito previo:</strong> Habilita la Verificación en dos pasos en tu Cuenta de Microsoft.",
    "er_outlook_step2": "<strong>Generar Contraseña de Aplicación:</strong>",
    "er_outlook_step2_li1": 'Ve a la configuración de <a href="https://account.live.com/proofs/manage/additional" target="_blank">Seguridad de tu Cuenta de Microsoft</a>.',
    "er_outlook_step2_li2": "Desplázate hacia abajo hasta <strong>Contraseñas de aplicaciones</strong> y haz clic en <strong>Crear una nueva contraseña de aplicación</strong>.",
    "er_outlook_step2_li3": "Copia la contraseña generada.",
    "er_outlook_step3": '<strong>Configurar en <span class="notranslate" translate="no">TapAlert</span>:</strong>',
    "er_outlook_step3_li1": "Toca el botón de configuración rápida de <strong>Outlook</strong> en la aplicación.",
    "er_outlook_step3_li2": "Ingresa tu correo y la Contraseña de Aplicación generada.",
    
    "er_h3_icloud": "Configuración para Usuarios de iCloud",
    "er_icloud_step2_li1": 'Ve a <a href="https://appleid.apple.com/account/manage" target="_blank">appleid.apple.com</a> e inicia sesión.',
    "er_icloud_step2_li2": "En la sección Inicio de sesión y seguridad, haz clic en <strong>Contraseñas específicas de aplicaciones</strong>.",
    "er_icloud_step2_li3": "Haz clic en <strong>Generar una contraseña específica de aplicación</strong> o en el botón <strong>+</strong>.",
    "er_icloud_step2_li4": 'Noómbrala <strong><span class="notranslate" translate="no">TapAlert</span></strong> y haz clic en Crear.',
    "er_icloud_step3_li1": "Toca el botón de configuración rápida de <strong>iCloud</strong> en la aplicación.",
    
    "er_h3_yahoo": "Configuración para Usuarios de Yahoo",
    "er_yahoo_step2_li1": 'Ve a la página de <a href="https://login.yahoo.com/account/security" target="_blank">Seguridad de la cuenta de Yahoo</a>.',
    "er_yahoo_step2_li2": "Haz clic en <strong>Generar contraseña de aplicación</strong> o <strong>Gestionar contraseñas de aplicación</strong>.",
    "er_yahoo_step2_li3": "Selecciona 'Otra aplicación' y nómbrala <strong>TapAlert</strong>.",
    "er_yahoo_step2_li4": "Haz clic en Generar.",
    "er_yahoo_step3_li1": "Toca el botón de configuración rápida de <strong>Yahoo</strong> en la aplicación.",
    
    "er_h2_ensure": "Asegurar Que los Destinatarios lo Reciban",
    "er_p_ensure_1": 'Si tus destinatarios no ven el correo de alerta, podría haber sido filtrado en su <strong>carpeta de Correo no deseado/Spam</strong>.',
    "er_ensure_li1": 'Pide a tus destinatarios que revisen su carpeta de Spam.',
    "er_ensure_li2": 'Diles que marquen el correo como <strong>"No es spam"</strong>.',
    "er_ensure_li3": 'Pídeles que agreguen tu dirección de correo electrónico de envío a su lista de contactos/VIP.',
    "er_h2_test": "Probando la Conexión",
    "er_p_test_1": "Antes de cerrar los ajustes, es muy recomendable probar tu configuración:",
    "er_test_li1": "Toca el botón <strong>Probar Conexión</strong>.",
    "er_test_li2": "Ingresa una dirección de correo para enviar un mensaje de prueba.",
    "er_test_li3": 'Si tiene éxito, verás un mensaje de "Conexión Exitosa". Si no, vuelve a verificar tu Contraseña de Aplicación y configuraciones.'
}

update_locales(en_keys, es_keys)

def replace_in_file(filepath, replacements):
    with open(filepath, 'r') as f:
        content = f.read()
    for old, new in replacements:
        content = content.replace(old, new)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated {filepath}")

contact_replacements = [
    (
        "<title>Contact Support - TapAlert</title>",
        "<title>{{ contact_title }} - TapAlert</title>"
    ),
    (
        '<h1 class="guide-title">Contact Support</h1>',
        '<h1 class="guide-title">{{ contact_h1 }}</h1>'
    ),
    (
        '<p class="guide-intro">We\'re here to help.</p>',
        '<p class="guide-intro">{{ contact_intro }}</p>'
    ),
    (
        '<h2>1. App Issues & Technical Support</h2>',
        '<h2>{{ contact_h2_1 }}</h2>'
    ),
    (
        '<p>If you are experiencing issues with <span class="notranslate" translate="no">TapAlert</span> or have questions about how a feature works, please check our <a href="index.html#guides">Guides & FAQ</a> first. If you still need help, you can reach out directly via:</p>',
        '<p>{{ contact_p1 }}</p>'
    ),
    (
        '<li><strong>Email:</strong> <a href="mailto:support@tapalert.app">support@tapalert.app</a></li>',
        '<li>{{ contact_email }}</li>'
    ),
    (
        '<h2>2. Feedback & Feature Requests</h2>',
        '<h2>{{ contact_h2_2 }}</h2>'
    ),
    (
        '<p>We are constantly looking to improve <span class="notranslate" translate="no">TapAlert</span>. If you have any suggestions, we\'d love to hear from you at <a href="mailto:feedback@tapalert.app">feedback@tapalert.app</a>.</p>',
        '<p>{{ contact_p2 }}</p>'
    ),
    (
        '<h2>3. Business Inquiries</h2>',
        '<h2>{{ contact_h2_3 }}</h2>'
    ),
    (
        '<p>For partnerships, media, or other business-related matters, please contact <a href="mailto:business@tapalert.app">business@tapalert.app</a>.</p>',
        '<p>{{ contact_p3 }}</p>'
    )
]

er_replacements = [
    (
        "<title>Email Redundancy Guide - TapAlert</title>",
        "<title>{{ er_title }} - TapAlert</title>"
    ),
    (
        '<h1 class="guide-title">Setting Up Email Redundancy</h1>',
        '<h1 class="guide-title">{{ er_h1 }}</h1>'
    ),
    (
        '<h2>Why Enable Email Redundancy?</h2>',
        '<h2>{{ er_h2_why }}</h2>'
    ),
    (
        '<p>Email redundancy is a crucial backup system.</p>',
        '<p>{{ er_p_why_1 }}</p>'
    ),
    (
        '<li><strong>Zero Cellular Signal:</strong> If you are deep inside a building or in a remote area with Wi-Fi but absolutely no cellular coverage, standard SMS and <span class="notranslate" translate="no">Twilio</span> SMS might fail.</li>',
        '<li>{{ er_why_li1 }}</li>'
    ),
    (
        '<li><strong>International Travel:</strong> When traveling abroad without a roaming plan, SMS might be disabled, but hotel/cafe Wi-Fi can still send your alert.</li>',
        '<li>{{ er_why_li2 }}</li>'
    ),
    (
        '<li><strong>Carrier Outages:</strong> Protects against rare but possible cellular network outages.</li>',
        '<li>{{ er_why_li3 }}</li>'
    ),
    (
        '<p><strong>How it works:</strong> First, the app attempts to send via <span class="notranslate" translate="no">Direct SMS</span> or <span class="notranslate" translate="no">Twilio</span>. If the device detects that these cellular methods have failed (or are impossible due to no signal), it will automatically attempt to send your alert via email.</p>',
        '<p>{{ er_p_why_2 }}</p>'
    ),
    (
        '<h2>How to Configure It</h2>',
        '<h2>{{ er_h2_how }}</h2>'
    ),
    (
        '<p>Email redundancy uses your existing email account (Gmail, Outlook, Yahoo, iCloud, etc.) to send the message. This requires <strong>SMTP settings</strong>.</p>',
        '<p>{{ er_p_how_1 }}</p>'
    ),
    (
        '<h4>IMPORTANT: Use an "App Password"</h4>',
        '<h4>{{ er_important_h4 }}</h4>'
    ),
    (
        '<p>For security reasons, practically all major email providers now require you to use an <strong>App Password</strong> rather than your standard email password. An App Password is a unique 16-character code that allows a specific app (like <span class="notranslate" translate="no">TapAlert</span>) to send email without needing your main password or bypassing Two-Factor Authentication (2FA).</p>',
        '<p>{{ er_important_p }}</p>'
    ),
    (
        '<h3>Setup for Gmail Users</h3>',
        '<h3>{{ er_h3_gmail }}</h3>'
    ),
    (
        '<p><strong>Prerequisite:</strong> You must have <a href="https://myaccount.google.com/security" target="_blank">2-Step Verification</a> enabled on your Google Account.</p>',
        '<p>{{ er_gmail_step1 }}</p>'
    ),
    (
        '<p><strong>Generate App Password:</strong></p>',
        '<p>{{ er_gmail_step2 }}</p>'
    ),
    (
        '<li>Go to your <a href="https://myaccount.google.com/apppasswords" target="_blank">Google Account App Passwords</a> page.</li>',
        '<li>{{ er_gmail_step2_li1 }}</li>'
    ),
    (
        '<li>If prompted, sign in.</li>',
        '<li>{{ er_gmail_step2_li2 }}</li>'
    ),
    (
        '<li>In the \'App name\' field, type <strong><span class="notranslate" translate="no">TapAlert</span></strong> and click <strong>Create</strong>.</li>',
        '<li>{{ er_gmail_step2_li3 }}</li>'
    ),
    (
        '<li>A modal will appear with a 16-character password.</li>',
        '<li>{{ er_gmail_step2_li4 }}</li>'
    ),
    (
        '<p><strong>Configure in <span class="notranslate" translate="no">TapAlert</span>:</strong></p>',
        '<p>{{ er_gmail_step3 }}</p>'
    ),
    (
        '<li>Open <span class="notranslate" translate="no">TapAlert</span> > <strong>Settings</strong> > <strong>Email Redundancy</strong>.</li>',
        '<li>{{ er_gmail_step3_li1 }}</li>'
    ),
    (
        '<li>Toggle <strong>Enable Email Redundancy</strong> ON.</li>',
        '<li>{{ er_gmail_step3_li2 }}</li>'
    ),
    (
        '<li>Tap the <strong>Gmail</strong> quick configuration button (this auto-fills Host to <code>smtp.gmail.com</code> and Port to <code>587</code>).</li>',
        '<li>{{ er_gmail_step3_li3 }}</li>'
    ),
    (
        '<li><strong>Username/Email:</strong> Enter your full Gmail address.</li>',
        '<li>{{ er_gmail_step3_li4 }}</li>'
    ),
    (
        '<li><strong>Password:</strong> Enter the 16-character App Password generated in Step 2. (Spaces don\'t matter).</li>',
        '<li>{{ er_gmail_step3_li5 }}</li>'
    ),
    (
        '<h3>Setup for Outlook / Hotmail Users</h3>',
        '<h3>{{ er_h3_outlook }}</h3>'
    ),
    (
        '<p><strong>Prerequisite:</strong> Enable Two-Step Verification on your Microsoft Account.</p>',
        '<p>{{ er_outlook_step1 }}</p>'
    ),
    (
        '<p><strong>Generate App Password:</strong></p>',
        '<p>{{ er_outlook_step2 }}</p>'
    ),
    (
        '<li>Go to your <a href="https://account.live.com/proofs/manage/additional" target="_blank">Microsoft Account Security settings</a>.</li>',
        '<li>{{ er_outlook_step2_li1 }}</li>'
    ),
    (
        '<li>Scroll down to <strong>App passwords</strong> and click <strong>Create a new app password</strong>.</li>',
        '<li>{{ er_outlook_step2_li2 }}</li>'
    ),
    (
        '<li>Copy the generated password.</li>',
        '<li>{{ er_outlook_step2_li3 }}</li>'
    ),
    (
        '<p><strong>Configure in <span class="notranslate" translate="no">TapAlert</span>:</strong></p>',
        '<p>{{ er_outlook_step3 }}</p>'
    ),
    (
        '<li>Tap the <strong>Outlook</strong> quick config button in the app.</li>',
        '<li>{{ er_outlook_step3_li1 }}</li>'
    ),
    (
        '<li>Enter your email and the generated App Password.</li>',
        '<li>{{ er_outlook_step3_li2 }}</li>'
    ),
    (
        '<h3>Setup for iCloud Users</h3>',
        '<h3>{{ er_h3_icloud }}</h3>'
    ),
    (
        '<li>Go to <a href="https://appleid.apple.com/account/manage" target="_blank">appleid.apple.com</a> and sign in.</li>',
        '<li>{{ er_icloud_step2_li1 }}</li>'
    ),
    (
        '<li>In the Sign-In and Security section, click <strong>App-Specific Passwords</strong>.</li>',
        '<li>{{ er_icloud_step2_li2 }}</li>'
    ),
    (
        '<li>Click <strong>Generate an app-specific password</strong> or the <strong>+</strong> button.</li>',
        '<li>{{ er_icloud_step2_li3 }}</li>'
    ),
    (
        '<li>Name it <strong><span class="notranslate" translate="no">TapAlert</span></strong> and click Create.</li>',
        '<li>{{ er_icloud_step2_li4 }}</li>'
    ),
    (
        '<li>Tap the <strong>iCloud</strong> quick config button in the app.</li>',
        '<li>{{ er_icloud_step3_li1 }}</li>'
    ),
    (
        '<h3>Setup for Yahoo Users</h3>',
        '<h3>{{ er_h3_yahoo }}</h3>'
    ),
    (
        '<li>Go to your <a href="https://login.yahoo.com/account/security" target="_blank">Yahoo Account Security page</a>.</li>',
        '<li>{{ er_yahoo_step2_li1 }}</li>'
    ),
    (
        '<li>Click <strong>Generate app password</strong> or <strong>Manage app passwords</strong>.</li>',
        '<li>{{ er_yahoo_step2_li2 }}</li>'
    ),
    (
        '<li>Select \'Other App\' and name it <strong>TapAlert</strong>.</li>',
        '<li>{{ er_yahoo_step2_li3 }}</li>'
    ),
    (
        '<li>Click Generate.</li>',
        '<li>{{ er_yahoo_step2_li4 }}</li>'
    ),
    (
        '<li>Tap the <strong>Yahoo</strong> quick config button in the app.</li>',
        '<li>{{ er_yahoo_step3_li1 }}</li>'
    ),
    (
        '<h2>Ensuring Recipients Receive It</h2>',
        '<h2>{{ er_h2_ensure }}</h2>'
    ),
    (
        '<p>If your recipients do not see the alert email, it might have been filtered into their <strong>Spam/Junk folder</strong>.</p>',
        '<p>{{ er_p_ensure_1 }}</p>'
    ),
    (
        '<li>Ask your recipients to check their Spam folder.</li>',
        '<li>{{ er_ensure_li1 }}</li>'
    ),
    (
        '<li>Tell them to mark the email as <strong>"Not Spam"</strong>.</li>',
        '<li>{{ er_ensure_li2 }}</li>'
    ),
    (
        '<li>Have them add your sending email address to their contacts/VIP list.</li>',
        '<li>{{ er_ensure_li3 }}</li>'
    ),
    (
        '<h2>Testing the Connection</h2>',
        '<h2>{{ er_h2_test }}</h2>'
    ),
    (
        '<p>Before closing the settings, it is highly recommended to test your configuration:</p>',
        '<p>{{ er_p_test_1 }}</p>'
    ),
    (
        '<li>Tap the <strong>Test Connection</strong> button.</li>',
        '<li>{{ er_test_li1 }}</li>'
    ),
    (
        '<li>Enter an email address to send a test message to.</li>',
        '<li>{{ er_test_li2 }}</li>'
    ),
    (
        '<li>If successful, you will see a "Connection Successful" message. If not, double-check your App Password and settings.</li>',
        '<li>{{ er_test_li3 }}</li>'
    )
]

replace_in_file('src/contact.html', contact_replacements)
replace_in_file('src/email_redundancy_guide.html', er_replacements)
