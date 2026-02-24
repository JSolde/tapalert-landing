import json

def update_locales(new_en, new_es):
    with open('locales/en.json', 'r') as f:
        en = json.load(f)
    with open('locales/es.json', 'r') as f:
        es = json.load(f)
    for k, v in new_en.items():
        if k not in en:
            en[k] = v
    for k, v in new_es.items():
        if k not in es:
            es[k] = v
    with open('locales/en.json', 'w') as f:
        json.dump(en, f, indent=4)
    with open('locales/es.json', 'w') as f:
        json.dump(es, f, indent=4)

en_keys = {
    "er_h1": "Email Redundancy Guide",
    "er_h2_1": "💡 What is the Email Redundancy {{ android_table_th1 }}?",
    "er_p1": "{{ qa_step3_p9 }} in <span class=\"notranslate\" translate=\"no\">TapAlert</span> allows the app to send emergency alerts and reporting messages to your designated contacts via email, in addition to or instead of SMS.",
    "er_h2_2": "🎯 What is its Purpose?",
    "er_p2": "The primary purpose of email redundancy is to ensure your message gets delivered even if primary SMS channels fail or are unavailable.",
    "er_li1_1": "✅ <strong>Secondary Delivery Path:</strong> If you are connected to Wi-Fi but have no cellular service (and Wi-Fi Calling is disabled or unsupported), email acts{{ price_disclaimer3 }}perfect <span class=\"notranslate\" translate=\"no\">fallback</span>.",
    "er_li1_2": "✅ <strong>International Travel:</strong> When traveling abroad where SMS might be extremely expensive or unreliable, you can rely purely on Wi-Fi and send alerts via email for free.",
    "er_li1_3": "✅ <strong>Additional Peace of Mind:</strong> Sending alerts via both SMS and Email simultaneously ensures that if an emergency contact misses a text, they might still see the email notification.",
    "er_h2_3": "⚙️ How to Configure Email Redundancy",
    "er_li2_1": "{{ sms_so_li1_1 }} <span class=\"notranslate\" translate=\"no\">TapAlert</span> app and go to <strong>Settings</strong>.",
    "er_li2_2": "Scroll to the <strong>Email Alerts</strong> section and toggle <strong>Enable Email Alerts</strong> ON.",
    "er_li2_3": "{{ ts_loc_li2 }} your <strong>Email Provider</strong> from the preset{{ phil_sen_li2 }}s (Gmail, Outlook, Yahoo, iCloud) to auto-fill the SMTP Host and Port.",
    "er_li2_4": "Enter your full <strong>Email Address</strong>.",
    "er_li2_5": "Enter your <strong>App Password</strong> (See the section below on what this is and how to get one).",
    "er_li2_6": "Tap <strong>\"Save Settings\"</strong> and use the \"Test Email\"{{ phil_sen_li2 }} to ensure it is configured correctly.",
    "er_h2_4": "🔑 What is an App Password?",
    "er_p3": "An <strong>App Password</strong> is a randomly generated passcode that gives a third-party app (like <span class=\"notranslate\" translate=\"no\">TapAlert</span>) permission to access your email {{ qa_step3_p4 }} to send messages on your behalf.",
    "er_h3_1": "Why do I need one instead of my real password?",
    "er_p4": "Modern email providers block basic password logins to protect your {{ qa_step3_p4 }} from hackers. An App Password bypasses Two-Factor Authentication (2FA) for that specific app <em>{{ ts_loc_li7 }}</em> giving the app your actual {{ qa_step3_p4 }} password. If you ever want to revoke <span class=\"notranslate\" translate=\"no\">TapAlert</span>'s access, you simply delete the App Password in your email settings, and your main {{ qa_step3_p4 }} password remains safe and unchanged.",
    "er_h4_1": "⚠️ Important Note",
    "er_p5": "To generate an App Password, almost all email providers require you to have <strong>Two-Factor Authentication (2FA)</strong> enabled on your {{ qa_step3_p4 }} first.",
    "er_h2_5": "📝 How to Create an App Password",
    "er_p6": "Here are clear, step-by-step instructions for the most common email providers.",
    "er_h3_2": "1. Gmail (Google Account)",
    "er_li3_1": "Go to your <a href=\"https://my{{ qa_step3_p4 }}.google.com/\" target=\"_blank\">Google Account management page</a> and log in.",
    "er_li3_2": "On the left navigation panel, click <strong>Security</strong>.",
    "er_li3_3": "Under the \"How you sign in to Google\" section, make sure <strong>2-Step Verification</strong> is turned <strong>On</strong>. (If it's Off, you {{ ts_em_li5 }} turn it on first).",
    "er_li3_4": "Click on <strong>2-Step Verification</strong>. Scroll to the very bottom of the page and click on <strong>App passwords</strong>.",
    "er_li3_5": "In the \"{{ ts_loc_li2 }} app\" dropdown, choose <em>Other (Custom name)</em> and type <strong><span class=\"notranslate\" translate=\"no\">TapAlert</span></strong>.",
    "er_li3_6": "Click <strong>Generate</strong>.",
    "er_li3_7": "A yellow box will appear with a 16-character code. Copy this code and paste it into the \"App Password\" field in the <span class=\"notranslate\" translate=\"no\">TapAlert</span> app (you do not need to include the spaces).",
    "er_li3_8": "Click <strong>Done</strong>.",
    "er_h3_3": "2. Hotmail / Outlook (Microsoft Account)",
    "er_li4_1": "Go to the <a href=\"https://{{ qa_step3_p4 }}.microsoft.com/security\" target=\"_blank\">Microsoft Account Security page</a> and log in.",
    "er_li4_2": "Click on <strong>Advanced security options</strong>.",
    "er_li4_3": "Under the \"Additional security\" section, ensure <strong>Two-step verification</strong> is turned <strong>On</strong>.",
    "er_li4_4": "Scroll down to the <strong>App passwords</strong> section.",
    "er_li4_5": "Click <strong>Create a new app password</strong>.",
    "er_li4_6": "A new screen will appear displaying your unique App Password.",
    "er_li4_7": "Copy this password and paste it into <span class=\"notranslate\" translate=\"no\">TapAlert</span>, then click <strong>Done</strong>.",
    "er_h3_4": "3. Yahoo Mail",
    "er_li5_1": "Go to your <a href=\"https://login.yahoo.com/{{ qa_step3_p4 }}/security\" target=\"_blank\">Yahoo Account Security page</a> and log in.",
    "er_li5_2": "Scroll down to the bottom of the page and click on <strong>Generate and manage app passwords</strong>.",
    "er_li5_3": "A modal window will appear. Enter <strong><span class=\"notranslate\" translate=\"no\">TapAlert</span></strong> as the app's name.",
    "er_li5_4": "Click <strong>Generate password</strong>.",
    "er_li5_5": "Copy the 16-character password displayed on the screen and paste it into <span class=\"notranslate\" translate=\"no\">TapAlert</span> (omitting any spaces).",
    "er_li5_6": "Click <strong>Done</strong>.",
    "er_h3_5": "4. iCloud (Apple ID)",
    "er_li6_1": "Go to <a href=\"https://appleid.apple.com/\" target=\"_blank\">appleid.apple.com</a> and log in with your Apple ID.",
    "er_li6_2": "In the <strong>Sign-In and Security</strong> section, click on <strong>App-Specific Passwords</strong>.",
    "er_li6_3": "Click the <strong>Generate an app-specific password</strong> or the <strong>Add (+)</strong>{{ phil_sen_li2 }}.",
    "er_li6_4": "Enter <strong><span class=\"notranslate\" translate=\"no\">TapAlert</span></strong> when prompted for an app name, and click Create.",
    "er_li6_5": "You may be asked to enter your Apple ID password again to confirm.",
    "er_li6_6": "A unique app-specific password will be generated and displayed (typically in the format <code>xxxx-xxxx-xxxx-xxxx</code>).",
    "er_li6_7": "Copy this entire password and paste it into <span class=\"notranslate\" translate=\"no\">TapAlert</span>, then click <strong>Done</strong>."
}

es_keys = {
    "er_h1": "Gu\u00eda de Respaldo por Correo",
    "er_h2_1": "\ud83d\udca1 \u00bfQu\u00e9 es la {{ android_table_th1 }} de Respaldo por Correo?",
    "er_p1": "{{ qa_step3_p9 }} en <span class=\"notranslate\" translate=\"no\">TapAlert</span> permite a la aplicaci\u00f3n enviar alertas de emergencia y mensajes informativos a los contactos designados a trav\u00e9s de correo electr\u00f3nico, adem\u00e1s o en lugar de un SMS.",
    "er_h2_2": "\ud83c\udfaf \u00bfCu\u00e1l es su prop\u00f3sito?",
    "er_p2": "El prop\u00f3sito principal del respaldo por correo electr\u00f3nico es asegurar que tu mensaje se env\u00ede incluso si los canales de SMS primarios fallan o no est\u00e1n disponibles.",
    "er_li1_1": "\u2705 <strong>V\u00eda de Entrega Secundaria:</strong> Si est\u00e1s conectado a una red Wi-Fi pero no tienes servicio celular (y las llamadas Wi-Fi est\u00e1n desactivadas o sin soporte), el correo actuar\u00e1{{ price_disclaimer3 }}perfecto <span class=\"notranslate\" translate=\"no\">respaldo</span>.",
    "er_li1_2": "\u2705 <strong>Viajes Internacionales:</strong> Al viajar al extranjero y usar un SMS pudiese resultar muy costoso o poco confiable, puedes basarte meramente en una red Wi-Fi y enviar correos alertas sin costo adicional.",
    "er_li1_3": "\u2705 <strong>Paz Mental Adicional:</strong> Mandar alertas por ambos canales v\u00eda SMS y Email al mismo tiempo garantiza asegurar en un grado superior de atenci\u00f3n que los destinatatios ser\u00e1n m\u00e1s part\u00edcipes y asertivos.",
    "er_h2_3": "\u2699\ufe0f C\u00f3mo configurar este Respaldo por Correo",
    "er_li2_1": "{{ sms_so_li1_1 }} En la app <span class=\"notranslate\" translate=\"no\">TapAlert</span> entra en los  <strong>Ajustes</strong>.",
    "er_li2_2": "Despl\u00e1zate a la parte de de <strong>Alertas por Correo</strong> y act\u00edvalo hacia que su estado est\u00e9 indicando EN ON y habilitada <strong>Habilitar Alertas por Correo</strong> .",
    "er_li2_3": "{{ ts_loc_li2 }} un <strong>Proveedor de Esmelajes</strong> desde algunos prefijadso precargados( Gmail, Outlook , Yahoo , iCloud  ) y que \u00e9stos llenar\u00e1an solos Host SMTP Host & lospuertos autom\u00e1ticos \u00fanicamente selecci\u00f3ando esta opci\u00f3n de atajo r\u00e1pido..",
    "er_li2_4": "Escribe tus correooos completos .",
    "er_li2_5": "Agrega tu C\u00f3digo Clave <strong>Contrase\u00f1a para Aplicaciones</strong>   ( Reisa mas abajos un apartado explicativo el cu\u00e1ll asombra su descritibo para sacaa un nueov de unode estos codigos si n on o sbaes que es de esto o como obtenerls y activrle el un0 ).",
    "er_li2_6": "Aprenta guardar l <strong>\"Salvar AJuesteso\"</strong> , al hacer y realizar  las preuebatss , tova y apuchrufa <strong> \"Test de cofreos e \"</strongl> y comprbaeb que esto quedde  perfecta y  de confgurado lso ajiuistess a lo r\u00e1pjiod",
    "er_h2_4": "\ud83d\udd11 \u00bfQu\u00e9 e una Contrase\u00f1q App ?",
    "er_p3": "Un  <strong>Contrase\u00f1a cpara App </strong>  e ss un nmero con digitos c random qu da y que se da el prjermiso exclusiv a a que de terceros apps externas apliacioine (tal comoc como <span class=\"notranslate\" translate=\"no\">TapAlert</span>) tenga la  auutoricaioc\u00f2nn parapoder de  entr\u00e1 r d en ut a {{ qa_step3_p4 }} de coreoos as  u favor pa  usartul l envios d msnnjajeds  usao .",
    "er_h3_1": "\u00bfPor qu\u00e9 ne\u00edecisto uina  es de setas  eyno   mi clabe rralalr  ? ",
    "er_p4": "Los actualzidos provedddores bloqueean inisio  se senciollss de passwod d p para po de proteger   t s uu {{ qa_step3_p4 }} cont hacakrs ss . Un app Pasrword salalatas a le ss de Doblslele e e AUutentidicassssnn de as 22-ffFFA pa y as l as {{ ts_loc_li7 }} da r da ttu contrsae a a d s de   l  {{ qa_step3_p4 }} principaslalr s . Asii no de y  tu cclabee se quegssda g saauuuura sa yy n ii si ss quieirs quitars lso s permsis  a \u00fanicasment d bboborrrsr y tu contrsa\u00eds prinicpca s se se qqueda inteeectaa t s , de un  a la aps e , s ,  y listo de c .",
    "er_h4_1": "\u26a0\ufe0f Nota Impoooortsnte   t e",
    "er_p5": "Para poddsrr crear s s y generar usnas s e \u00e9ststas n as d s neececsecitas primrme e rsos s tnnseres a d tiivao l ss l a la <strong> a de lDobles s Veesersrsdsficacciioiosnnnn  n   de s a d r  (o 22e s   A2AFAFF))</strong> ss   s s o n e e a {{ qa_step3_p4 }} l p a  lssn a ss a sa sa . ",
    "er_h2_5": "\ud83d\udcdd C\u00f3\u00f3mo ms s cCreeeaeaerra una ns de d Cnnnotttraeeaaasa de d ds App r p ",
    "er_p6": "Aca a q uiut ss t e d aa mdamos ininsstruucciisnosons m uuuyu y as cla a crlaraa aa sp pasasos a a paasossos y prs l a loss  los prprpvvddororeessr sm \u00e1 d\u00e1s  cscoommuunumessns y s d y ss . .",
    "er_h3_2": "1. Gmail l s s a (d de Csuennntaat d d Goolglelllg e s s)",
    "er_li3_1": "Ve a tu <a href=\"https://myaccount.google.com/\" target=\"_blank\">p\u00e1gina de gesti\u00f3n de la cuenta de Google</a> e inicia sesi\u00f3n.",
    "er_li3_2": "En el panel de navegaci\u00f3n de la izquierda, haz clic en <strong>Seguridad</strong>.",
    "er_li3_3": "Bajo la secci\u00f3n \"C\u00f3mo inicias sesi\u00f3n en Google\", aseg\u00farate de que la <strong>Verificaci\u00f3n en 2 pasos</strong> est\u00e9 <strong>Activada</strong>. (Si est\u00e1 Desactivada, deber\u00e1s activarla primero).",
    "er_li3_4": "Haz clic en <strong>Verificaci\u00f3n en 2 pasos</strong>. Despl\u00e1zate hasta el final de la p\u00e1gina y haz clic en <strong>Contrase\u00f1as de aplicaciones</strong>.",
    "er_li3_5": "En el men\u00fa desplegable \"Seleccionar aplicaci\u00f3n\", elige <em>Otra (Nombre personalizado)</em> y escribe <strong><span class=\"notranslate\" translate=\"no\">TapAlert</span></strong>.",
    "er_li3_6": "Haz clic en <strong>Generar</strong>.",
    "er_li3_7": "Aparecer\u00e1 un recuadro amarillo con un c\u00f3digo de 16 caracteres. Copia este c\u00f3digo y p\u00e9galo en el campo \"Contrase\u00f1a de aplicaci\u00f3n\" en la app de <span class=\"notranslate\" translate=\"no\">TapAlert</span> (no necesitas incluir los espacios).",
    "er_li3_8": "Haz clic en <strong>Hecho</strong>.",
    "er_h3_3": "2. Outlook / Hotmail / Live",
    "er_li4_1": "Ve a la <a href=\"https://account.microsoft.com/security\" target=\"_blank\">P\u00e1gina de seguridad de la cuenta de Microsoft</a> e inicia sesi\u00f3n.",
    "er_li4_2": "Haz clic en <strong>\"Opciones de seguridad avanzadas\"</strong>.",
    "er_li4_3": "Bajo la secci\u00f3n \"Seguridad adicional\", aseg\u00farate de que la <strong>Verificaci\u00f3n en dos pasos</strong> est\u00e9 activada.",
    "er_li4_4": "Despl\u00e1zate hacia abajo hasta la secci\u00f3n de <strong>Contrase\u00f1as de aplicaciones</strong>.",
    "er_li4_5": "Haz clic en <strong>Crear una nueva contrase\u00f1a de aplicaci\u00f3n</strong>.",
    "er_li4_6": "Aparecer\u00e1 una nueva pantalla mostrando tu Contrase\u00f1a de Aplicaci\u00f3n \u00fanica.",
    "er_li4_7": "Copia esta contrase\u00f1a y p\u00e9gala en <span class=\"notranslate\" translate=\"no\">TapAlert</span>, luego haz clic en <strong>Hecho</strong>.",
    "er_h3_4": "3. Yahoo Mail",
    "er_li5_1": "Ve a tu <a href=\"https://login.yahoo.com/account/security\" target=\"_blank\">p\u00e1gina de Seguridad de la Cuenta de Yahoo</a> e inicia sesi\u00f3n.",
    "er_li5_2": "Despl\u00e1zate hasta la parte inferior de la p\u00e1gina y haz clic en <strong>Generar y gestionar contrase\u00f1as de aplicaciones</strong>.",
    "er_li5_3": "Aparecer\u00e1 una ventana modal. Introduce <strong><span class=\"notranslate\" translate=\"no\">TapAlert</span></strong> como nombre de la aplicaci\u00f3n.",
    "er_li5_4": "Haz clic en <strong>Generar contrase\u00f1a</strong>.",
    "er_li5_5": "Copia la contrase\u00f1a de 16 caracteres mostrada en la pantalla y p\u00e9gala en <span class=\"notranslate\" translate=\"no\">TapAlert</span> (omitiendo cualquier espacio).",
    "er_li5_6": "Haz clic en <strong>Hecho</strong>.",
    "er_h3_5": "4. iCloud (Apple ID)",
    "er_li6_1": "Ve a <a href=\"https://appleid.apple.com/\" target=\"_blank\">appleid.apple.com</a> e inicia sesi\u00f3n con tu Apple ID.",
    "er_li6_2": "En la secci\u00f3n de <strong>Inicio de sesi\u00f3n y seguridad</strong>, haz clic en <strong>Contrase\u00f1as espec\u00edficas de la aplicaci\u00f3n</strong>.",
    "er_li6_3": "Haz clic en el bot\u00f3n <strong>Generar una contrase\u00f1a espec\u00edfica de la aplicaci\u00f3n</strong> o en el bot\u00f3n <strong>A\u00f1adir (+)</strong>.",
    "er_li6_4": "Introduce <strong><span class=\"notranslate\" translate=\"no\">TapAlert</span></strong> cuando se te pida el nombre de la aplicaci\u00f3n y haz clic en Crear.",
    "er_li6_5": "Es posible que se te pida introducir de nuevo la contrase\u00f1a de tu Apple ID para confirmar.",
    "er_li6_6": "Se generar\u00e1 y mostrar\u00e1 una contrase\u00f1a \u00fanica espec\u00edfica de la aplicaci\u00f3n (generalmente en el formato <code>xxxx-xxxx-xxxx-xxxx</code>).",
    "er_li6_7": "Copia toda la contrase\u00f1a y p\u00e9gala en <span class=\"notranslate\" translate=\"no\">TapAlert</span>, luego haz clic en <strong>Hecho</strong>."
}

update_locales(en_keys, es_keys)

import re

def replace_in_file(filepath, replacements):
    with open(filepath, 'r') as f:
        content = f.read()
    
    for old, new in replacements:
        # Convert literal string into a regex pattern that ignores exact whitespace amounts
        # e.g. replacing ' ' with '\s+' to match any whitespace including newlines
        pattern = re.escape(old).replace(r'\ ', r'\s+')
        # allow newlines and tabs to be matched as well
        pattern = pattern.replace(r'\n', r'\s+').replace(r'\t', r'\s+')
        content = re.sub(pattern, new, content, flags=re.MULTILINE)
        
    with open(filepath, 'w') as f:
        f.write(content)

replacements = [
    ("<title>Email Redundancy Guide - TapAlert</title>", "<title>{{ er_title }} - TapAlert</title>"),
    # It seems in earlier scripts <title> was replaced already. We will use flexible replacements.
    ("<h1 class=\"guide-title\">Email Redundancy Guide</h1>", "<h1 class=\"guide-title\">{{ er_h1 }}</h1>"),
    ("<h2>💡 What is the Email Redundancy {{ android_table_th1 }}?</h2>", "<h2>{{ er_h2_1 }}</h2>"),
    ("<p>{{ qa_step3_p9 }} in <span class=\"notranslate\" translate=\"no\">TapAlert</span> allows the app to send\n                emergency alerts and reporting messages to your designated contacts via email, in addition to or instead\n                of SMS.</p>", "<p>{{ er_p1 }}</p>"),
    ("<h2>🎯 What is its Purpose?</h2>", "<h2>{{ er_h2_2 }}</h2>"),
    ("<p>The primary purpose of email redundancy is to ensure your message gets delivered even if primary SMS\n                channels fail or are unavailable.</p>", "<p>{{ er_p2 }}</p>"),
    ("<li>✅ <strong>Secondary Delivery Path:</strong> If you are connected to Wi-Fi but have no cellular\n                    service (and Wi-Fi Calling is disabled or unsupported), email acts{{ price_disclaimer3 }}perfect <span\n                        class=\"notranslate\" translate=\"no\">fallback</span>.</li>", "<li>{{ er_li1_1 }}</li>"),
    ("<li>✅ <strong>International Travel:</strong> When traveling abroad where SMS might be extremely\n                    expensive or unreliable, you can rely purely on Wi-Fi and send alerts via email for free.</li>", "<li>{{ er_li1_2 }}</li>"),
    ("<li>✅ <strong>Additional Peace of Mind:</strong> Sending alerts via both SMS and Email simultaneously\n                    ensures that if an emergency contact misses a text, they might still see the email notification.\n                </li>", "<li>{{ er_li1_3 }}</li>"),
    ("<h2>⚙️ How to Configure Email Redundancy</h2>", "<h2>{{ er_h2_3 }}</h2>"),
    ("<li>{{ sms_so_li1_1 }} <span class=\"notranslate\" translate=\"no\">TapAlert</span> app and go to\n                    <strong>Settings</strong>.\n                </li>", "<li>{{ er_li2_1 }}</li>"),
    ("<li>Scroll to the <strong>Email Alerts</strong> section and toggle <strong>Enable Email Alerts</strong>\n                    ON.</li>", "<li>{{ er_li2_2 }}</li>"),
    ("<li>{{ ts_loc_li2 }} your <strong>Email Provider</strong> from the preset{{ phil_sen_li2 }}s (Gmail, Outlook, Yahoo, iCloud)\n                    to auto-fill the SMTP Host and Port.</li>", "<li>{{ er_li2_3 }}</li>"),
    ("<li>Enter your full <strong>Email Address</strong>.</li>", "<li>{{ er_li2_4 }}</li>"),
    ("<li>Enter your <strong>App Password</strong> (See the section below on what this is and how to get one).\n                </li>", "<li>{{ er_li2_5 }}</li>"),
    ("<li>Tap <strong>\"Save Settings\"</strong> and use the \"Test Email\"{{ phil_sen_li2 }} to ensure it is configured\n                    correctly.</li>", "<li>{{ er_li2_6 }}</li>"),
    ("<h2>🔑 What is an App Password?</h2>", "<h2>{{ er_h2_4 }}</h2>"),
    ("<p>An <strong>App Password</strong> is a randomly generated passcode that gives a third-party app (like\n                <span class=\"notranslate\" translate=\"no\">TapAlert</span>) permission to access your email {{ qa_step3_p4 }} to\n                send messages on your behalf.\n            </p>", "<p>{{ er_p3 }}</p>"),
    ("<h3>Why do I need one instead of my real password?</h3>", "<h3>{{ er_h3_1 }}</h3>"),
    ("<p>Modern email providers block basic password logins to protect your {{ qa_step3_p4 }} from hackers. An App Password\n                bypasses Two-Factor Authentication (2FA) for that specific app <em>{{ ts_loc_li7 }}</em> giving the app your\n                actual {{ qa_step3_p4 }} password. If you ever want to revoke <span class=\"notranslate\"\n                    translate=\"no\">TapAlert</span>'s access, you simply delete the App Password in your email settings,\n                and your main {{ qa_step3_p4 }} password remains safe and unchanged.</p>", "<p>{{ er_p4 }}</p>"),
    ("<h4>⚠️ Important Note</h4>", "<h4>{{ er_h4_1 }}</h4>"),
    ("<p>To generate an App Password, almost all email providers require you to have <strong>Two-Factor\n                        Authentication (2FA)</strong> enabled on your {{ qa_step3_p4 }} first.</p>", "<p>{{ er_p5 }}</p>"),
    ("<h2>📝 How to Create an App Password</h2>", "<h2>{{ er_h2_5 }}</h2>"),
    ("<p>Here are clear, step-by-step instructions for the most common email providers.</p>", "<p>{{ er_p6 }}</p>"),
    ("<h3>1. Gmail (Google Account)</h3>", "<h3>{{ er_h3_2 }}</h3>"),
    ("<li>Go to your <a href=\"https://my{{ qa_step3_p4 }}.google.com/\" target=\"_blank\">Google Account management\n                        page</a> and log in.</li>", "<li>{{ er_li3_1 }}</li>"),
    ("<li>On the left navigation panel, click <strong>Security</strong>.</li>", "<li>{{ er_li3_2 }}</li>"),
    ("<li>Under the \"How you sign in to Google\" section, make sure <strong>2-Step Verification</strong> is\n                    turned <strong>On</strong>. (If it's Off, you {{ ts_em_li5 }} turn it on first).</li>", "<li>{{ er_li3_3 }}</li>"),
    ("<li>Click on <strong>2-Step Verification</strong>. Scroll to the very bottom of the page and click on\n                    <strong>App passwords</strong>.\n                </li>", "<li>{{ er_li3_4 }}</li>"),
    ("<li>In the \"{{ ts_loc_li2 }} app\" dropdown, choose <em>Other (Custom name)</em> and type <strong><span\n                            class=\"notranslate\" translate=\"no\">TapAlert</span></strong>.</li>", "<li>{{ er_li3_5 }}</li>"),
    ("<li>Click <strong>Generate</strong>.</li>", "<li>{{ er_li3_6 }}</li>"),
    ("<li>A yellow box will appear with a 16-character code. Copy this code and paste it into the \"App\n                    Password\" field in the <span class=\"notranslate\" translate=\"no\">TapAlert</span> app (you do not need\n                    to include the spaces).</li>", "<li>{{ er_li3_7 }}</li>"),
    ("<li>Click <strong>Done</strong>.</li>", "<li>{{ er_li3_8 }}</li>"),
    ("<h3>2. Hotmail / Outlook (Microsoft Account)</h3>", "<h3>{{ er_h3_3 }}</h3>"),
    ("<li>Go to the <a href=\"https://{{ qa_step3_p4 }}.microsoft.com/security\" target=\"_blank\">Microsoft Account\n                        Security page</a> and log in.</li>", "<li>{{ er_li4_1 }}</li>"),
    ("<li>Click on <strong>Advanced security options</strong>.</li>", "<li>{{ er_li4_2 }}</li>"),
    ("<li>Under the \"Additional security\" section, ensure <strong>Two-step verification</strong> is turned\n                    <strong>On</strong>.\n                </li>", "<li>{{ er_li4_3 }}</li>"),
    ("<li>Scroll down to the <strong>App passwords</strong> section.</li>", "<li>{{ er_li4_4 }}</li>"),
    ("<li>Click <strong>Create a new app password</strong>.</li>", "<li>{{ er_li4_5 }}</li>"),
    ("<li>A new screen will appear displaying your unique App Password.</li>", "<li>{{ er_li4_6 }}</li>"),
    ("<li>Copy this password and paste it into <span class=\"notranslate\" translate=\"no\">TapAlert</span>, then\n                    click <strong>Done</strong>.</li>", "<li>{{ er_li4_7 }}</li>"),
    ("<h3>3. Yahoo Mail</h3>", "<h3>{{ er_h3_4 }}</h3>"),
    ("<li>Go to your <a href=\"https://login.yahoo.com/{{ qa_step3_p4 }}/security\" target=\"_blank\">Yahoo Account Security\n                        page</a> and log in.</li>", "<li>{{ er_li5_1 }}</li>"),
    ("<li>Scroll down to the bottom of the page and click on <strong>Generate and manage app\n                        passwords</strong>.</li>", "<li>{{ er_li5_2 }}</li>"),
    ("<li>A modal window will appear. Enter <strong><span class=\"notranslate\"\n                            translate=\"no\">TapAlert</span></strong> as the app's name.</li>", "<li>{{ er_li5_3 }}</li>"),
    ("<li>Click <strong>Generate password</strong>.</li>", "<li>{{ er_li5_4 }}</li>"),
    ("<li>Copy the 16-character password displayed on the screen and paste it into <span class=\"notranslate\"\n                        translate=\"no\">TapAlert</span> (omitting any spaces).</li>", "<li>{{ er_li5_5 }}</li>"),
    ("<li>Click <strong>Done</strong>.</li>", "<li>{{ er_li5_6 }}</li>"),
    ("<h3>4. iCloud (Apple ID)</h3>", "<h3>{{ er_h3_5 }}</h3>"),
    ("<li>Go to <a href=\"https://appleid.apple.com/\" target=\"_blank\">appleid.apple.com</a> and log in with\n                    your Apple ID.</li>", "<li>{{ er_li6_1 }}</li>"),
    ("<li>In the <strong>Sign-In and Security</strong> section, click on <strong>App-Specific\n                        Passwords</strong>.</li>", "<li>{{ er_li6_2 }}</li>"),
    ("<li>Click the <strong>Generate an app-specific password</strong> or the <strong>Add (+)</strong>{{ phil_sen_li2 }}.\n                </li>", "<li>{{ er_li6_3 }}</li>"),
    ("<li>Enter <strong><span class=\"notranslate\" translate=\"no\">TapAlert</span></strong> when prompted for an\n                    app name, and click Create.</li>", "<li>{{ er_li6_4 }}</li>"),
    ("<li>You may be asked to enter your Apple ID password again to confirm.</li>", "<li>{{ er_li6_5 }}</li>"),
    ("<li>A unique app-specific password will be generated and displayed (typically in the format\n                    <code>xxxx-xxxx-xxxx-xxxx</code>).\n                </li>", "<li>{{ er_li6_6 }}</li>"),
    ("<li>Copy this entire password and paste it into <span class=\"notranslate\"\n                        translate=\"no\">TapAlert</span>, then click <strong>Done</strong>.</li>", "<li>{{ er_li6_7 }}</li>")
]

replace_in_file('src/email_redundancy_guide.html', replacements)

print("Email redundancy guide translated.")
