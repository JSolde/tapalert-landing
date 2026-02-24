import json

with open('locales/en.json', 'r') as f:
    en = json.load(f)

with open('locales/es.json', 'r') as f:
    es = json.load(f)

# Updates for EN
en["ag_h1"] = "Accessibility Features for Seniors"
en["ag_meta"] = "<span class=\"notranslate\" translate=\"no\">TapAlert</span> is designed to be usable by everyone, including people with hearing loss, low vision, tremors, or other age-related conditions. This guide explains each accessibility feature and how to get the most out of it."

en["ag_step1_h"] = "1. Large Text Support"
en["ag_step1_who"] = "People with low vision or difficulty reading small text."
en["ag_step1_p1"] = "<span class=\"notranslate\" translate=\"no\">TapAlert</span> respects the font size you set in your phone's system settings. If you increase the text size in <strong>Settings > Display > Font Size</strong> (Android) or <strong>Settings > Accessibility > Display & Text Size > Larger Text</strong> (iOS), all text in <span class=\"notranslate\" translate=\"no\">TapAlert</span> will grow accordingly — buttons, labels, menus, and messages."
en["ag_step1_alert_h"] = "No action needed inside the app"
en["ag_step1_alert_p"] = "Just set your preferred font size in your phone settings and <span class=\"notranslate\" translate=\"no\">TapAlert</span> will follow it automatically."

en["ag_step2_h"] = "2. Screen Reader Support (TalkBack / VoiceOver)"
en["ag_step2_who"] = "People with severe vision impairment who use a screen reader."
en["ag_step2_p1"] = "<span class=\"notranslate\" translate=\"no\">TapAlert</span> works natively with:"
en["ag_step2_li1"] = "<strong>TalkBack</strong> on Android (Settings > Accessibility > TalkBack)"
en["ag_step2_li2"] = "<strong>VoiceOver</strong> on iPhone (Settings > Accessibility > VoiceOver)"
en["ag_step2_p2"] = "When a screen reader is active:"
en["ag_step2_li3"] = "The <strong><span class=\"notranslate\" translate=\"no\">SOS</span></strong> and <strong>I'm OK</strong> buttons are announced with their names and current state (enabled or disabled)."
en["ag_step2_li4"] = "When you start a countdown before sending an alert, the screen reader counts down the remaining seconds aloud so you always know how long you have before the alert is sent."
en["ag_step2_li5"] = "After an alert is sent, the screen reader announces <strong>\"Alert sent\"</strong> or <strong>\"Alert failed\"</strong> so you know the outcome without needing to look at the screen."

en["ag_step3_h"] = "3. Haptic Feedback (Phone Vibration)"
en["ag_step3_who"] = "People with hearing loss who cannot hear the countdown sound, or anyone who prefers tactile confirmation."
en["ag_step3_p1"] = "<span class=\"notranslate\" translate=\"no\">TapAlert</span> uses your phone's vibration motor to give you physical feedback at key moments:"
en["ag_step3_th1"] = "Moment"
en["ag_step3_th2"] = "Vibration"
en["ag_step3_tr1_1"] = "Countdown tick"
en["ag_step3_tr1_2"] = "One firm pulse per second — you can feel the countdown in your hand"
en["ag_step3_tr2_1"] = "Alert sent successfully"
en["ag_step3_tr2_2"] = "Three strong pulses in quick succession"
en["ag_step3_tr3_1"] = "Alert failed"
en["ag_step3_tr3_2"] = "Two rapid buzzes"
en["ag_step3_tr4_1"] = "Countdown cancelled"
en["ag_step3_tr4_2"] = "Two medium pulses — confirms you cancelled, not sent"
en["ag_step3_tr5_1"] = "No recipients configured"
en["ag_step3_tr5_2"] = "One long vibration (error)"
en["ag_step3_alert_h"] = "No action needed"
en["ag_step3_alert_p"] = "Haptic feedback works automatically as long as vibration is enabled on your phone (check your phone's silent/vibration switch)."

en["ag_step4_h"] = "4. Sound Alerts"
en["ag_step4_who"] = "People who need to hear when an alert is sent, including those with moderate hearing loss."
en["ag_step4_p1"] = "When an alert is sent, <span class=\"notranslate\" translate=\"no\">TapAlert</span> plays a sound on <strong>your own device</strong> to confirm the alert went out. You can customize the sound in <strong>Settings > Notification Sound</strong>:"
en["ag_step4_li1"] = "<strong>None</strong> — no sound"
en["ag_step4_li2"] = "<strong>Plain Sounds</strong> — simple, clear tones (good for most users)"
en["ag_step4_li3"] = "<strong>Rich Sounds</strong> — fuller, more musical tones"
en["ag_step4_p2"] = "Within each sound style, you can also adjust:"
en["ag_step4_li4"] = "<strong>Sound Pitch</strong> — slide left for a lower, deeper tone. Lower-pitched sounds (around 500 Hz) are easier to hear for people with age-related high-frequency hearing loss. The default is already set to a lower pitch for this reason."
en["ag_step4_li5"] = "<strong>Volume</strong> — set how loud the confirmation sound plays."

en["ag_step5_h"] = "5. Screen Flash and Torch Flash"
en["ag_step5_who"] = "People with hearing loss who may miss the sound, or anyone in a loud environment. Also useful when the phone is face-down or in a pocket."
en["ag_step5_p1"] = "When an alert is sent successfully, <span class=\"notranslate\" translate=\"no\">TapAlert</span> produces:"
en["ag_step5_li1"] = "<strong>Screen flash</strong> — the entire screen lights up white three times in quick succession."
en["ag_step5_li2"] = "<strong>Torch flash</strong> — the camera LED on the back of the phone flashes three times simultaneously, visible even when the screen faces down."
en["ag_step5_p2"] = "Both flashes run at the same time and complete in under one second."
en["ag_step5_alert_h"] = "How to turn this off"
en["ag_step5_alert_p"] = "If you have a photosensitive condition, go to <strong>Settings → Notification Sound → Flash on Alert</strong> and switch it off."

en["ag_step6_h"] = "6. Swipe to Cancel the Countdown"
en["ag_step6_who"] = "Anyone who accidentally starts a countdown and needs to cancel it quickly."
en["ag_step6_p1"] = "When you tap the <span class=\"notranslate\" translate=\"no\">SOS</span> button, a countdown dialog appears before the alert is sent. You can cancel it in two ways:"
en["ag_step6_li1"] = "Tap the <strong>Cancel</strong> button at the bottom of the dialog."
en["ag_step6_li2"] = "<strong>Swipe the dialog left or right</strong> — the dialog slides with your finger and dismisses when you release it far enough."
en["ag_step6_p2"] = "Either way, you will feel two short vibrations confirming the alert was cancelled and nothing was sent."

en["ag_step7_h"] = "7. Voice Message Composition"
en["ag_step7_who"] = "People with tremors, arthritis, or other conditions that make typing difficult."
en["ag_step7_p1"] = "Instead of typing a custom message before sending an alert, you can speak it. Tap the <strong>microphone icon</strong> in the message field and speak your message. The app will transcribe your words automatically. Silence for 3 seconds stops recording."
en["ag_step7_p2"] = "This works on the home screen message input and in the dead man's timer dialog."

en["ag_step8_h"] = "8. Hold-to-Send Mode"
en["ag_step8_who"] = "People who are prone to accidentally tapping the <span class=\"notranslate\" translate=\"no\">SOS</span> button."
en["ag_step8_p1"] = "By default, the <span class=\"notranslate\" translate=\"no\">SOS</span> button requires only a single tap. If accidental presses are a concern, you can switch to <strong>Hold to Send</strong> mode:"
en["ag_step8_p2"] = "Go to <strong>Settings → Trigger Method → Hold to Send</strong>."
en["ag_step8_p3"] = "In this mode, you must press and hold the button for the full hold duration before the alert is triggered, preventing accidental sends."

en["ag_step9_h"] = "9. Home Screen Widget (Android)"
en["ag_step9_who"] = "Anyone who finds it difficult to unlock their phone and open the app in an emergency."
en["ag_step9_p1"] = "On Android, you can add a <span class=\"notranslate\" translate=\"no\">TapAlert</span> widget to your home screen so the <span class=\"notranslate\" translate=\"no\">SOS</span> button is always one tap away — without opening the app at all."
en["ag_step9_p2"] = "To add the widget: <strong>Settings → Home Screen Widget → Add Widget</strong>."
en["ag_who_it_helps"] = "Who it helps:"

# Updates for ES
es["ag_h1"] = "Funciones de accesibilidad para personas mayores"
es["ag_meta"] = "<span class=\"notranslate\" translate=\"no\">TapAlert</span> est\u00e1 dise\u00f1ado para ser utilizable por todos, incluyendo personas con p\u00e9rdida de audici\u00f3n, baja visi\u00f3n, temblores u otras afecciones relacionadas con la edad. Esta gu\u00eda explica cada funci\u00f3n de accesibilidad y c\u00f3mo sacarle el m\u00e1ximo provecho."

es["ag_step1_h"] = "1. Soporte de texto grande"
es["ag_step1_who"] = "Personas con baja visi\u00f3n o dificultad para leer texto peque\u00f1o."
es["ag_step1_p1"] = "<span class=\"notranslate\" translate=\"no\">TapAlert</span> respeta el tama\u00f1o de fuente que configure en la configuraci\u00f3n del sistema de su tel\u00e9fono. Si aumenta el tama\u00f1o del texto en <strong>Configuraci\u00f3n > Pantalla > Tama\u00f1o de fuente</strong> (Android) o <strong>Configuraci\u00f3n > Accesibilidad > Pantalla y tama\u00f1o de texto > Texto m\u00e1s grande</strong> (iOS), todo el texto en <span class=\"notranslate\" translate=\"no\">TapAlert</span> crecer\u00e1 en consecuencia: botones, etiquetas, men\u00fas y mensajes."
es["ag_step1_alert_h"] = "No es necesaria ninguna acci\u00f3n dentro de la aplicaci\u00f3n"
es["ag_step1_alert_p"] = "Simplemente configure su tama\u00f1o de fuente preferido en la configuraci\u00f3n de su tel\u00e9fono y <span class=\"notranslate\" translate=\"no\">TapAlert</span> lo seguir\u00e1 autom\u00e1ticamente."

es["ag_step2_h"] = "2. Compatibilidad con el lector de pantalla (TalkBack / VoiceOver)"
es["ag_step2_who"] = "Personas con discapacidad visual severa que utilizan un lector de pantalla."
es["ag_step2_p1"] = "<span class=\"notranslate\" translate=\"no\">TapAlert</span> funciona de forma nativa con:"
es["ag_step2_li1"] = "<strong>TalkBack</strong> en Android (Configuraci\u00f3n > Accesibilidad > TalkBack)"
es["ag_step2_li2"] = "<strong>VoiceOver</strong> en iPhone (Ajustes > Accesibilidad > VoiceOver)"
es["ag_step2_p2"] = "Cuando un lector de pantalla est\u00e1 activo:"
es["ag_step2_li3"] = "Los botones <strong><span class=\"notranslate\" translate=\"no\">SOS</span></strong> y <strong>Estoy bien</strong> se anuncian con sus nombres y estado actual (activado o desactivado)."
es["ag_step2_li4"] = "Cuando inicia una cuenta regresiva antes de enviar una alerta, el lector de pantalla cuenta los segundos restantes en voz alta para que siempre sepa cu\u00e1nto tiempo le queda antes de que se env\u00ede la alerta."
es["ag_step2_li5"] = "Despu\u00e9s de que se env\u00eda una alerta, el lector de pantalla anuncia <strong>\"Alerta enviada\"</strong> o <strong>\"Alerta fallida\"</strong> para que conozca el resultado sin necesidad de mirar la pantalla."

es["ag_step3_h"] = "3. Retroalimentaci\u00f3n h\u00e1ptica (Vibraci\u00f3n del tel\u00e9fono)"
es["ag_step3_who"] = "Personas con p\u00e9rdida auditiva que no pueden escuchar el sonido de la cuenta regresiva, o cualquiera que prefiera la confirmaci\u00f3n t\u00e1ctil."
es["ag_step3_p1"] = "<span class=\"notranslate\" translate=\"no\">TapAlert</span> utiliza el motor de vibraci\u00f3n de su tel\u00e9fono para brindarle retroalimentaci\u00f3n f\u00edsica en momentos clave:"
es["ag_step3_th1"] = "Momento"
es["ag_step3_th2"] = "Vibraci\u00f3n"
es["ag_step3_tr1_1"] = "Tic de cuenta regresiva"
es["ag_step3_tr1_2"] = "Un pulso firme por segundo: puede sentir la cuenta regresiva en su mano"
es["ag_step3_tr2_1"] = "Alerta enviada con \u00e9xito"
es["ag_step3_tr2_2"] = "Tres pulsos fuertes en r\u00e1pida sucesi\u00f3n"
es["ag_step3_tr3_1"] = "Alerta fallida"
es["ag_step3_tr3_2"] = "Dos zumbidos r\u00e1pidos"
es["ag_step3_tr4_1"] = "Cuenta regresiva cancelada"
es["ag_step3_tr4_2"] = "Dos pulsos medios: confirma que cancel\u00f3, no envi\u00f3"
es["ag_step3_tr5_1"] = "No hay destinatarios configurados"
es["ag_step3_tr5_2"] = "Una vibraci\u00f3n larga (error)"
es["ag_step3_alert_h"] = "No se requiere acci\u00f3n"
es["ag_step3_alert_p"] = "La retroalimentaci\u00f3n h\u00e1ptica funciona autom\u00e1ticamente siempre que la vibraci\u00f3n est\u00e9 activada en su tel\u00e9fono (verifique el interruptor de silencio/vibraci\u00f3n de su tel\u00e9fono)."

es["ag_step4_h"] = "4. Alertas de sonido"
es["ag_step4_who"] = "Personas que necesitan escuchar cuando se env\u00eda una alerta, incluidas aquellas con p\u00e9rdida auditiva moderada."
es["ag_step4_p1"] = "Cuando se env\u00eda una alerta, <span class=\"notranslate\" translate=\"no\">TapAlert</span> reproduce un sonido en <strong>su propio dispositivo</strong> para confirmar que se emiti\u00f3 la alerta. Puede personalizar el sonido en <strong>Configuraci\u00f3n > Sonido de notificaci\u00f3n</strong>:"
es["ag_step4_li1"] = "<strong>Ninguno</strong>: sin sonido"
es["ag_step4_li2"] = "<strong>Sonidos simples</strong>: tonos simples y claros (buenos para la mayor\u00eda de los usuarios)"
es["ag_step4_li3"] = "<strong>Sonidos Ricos</strong>: tonos m\u00e1s completos y musicales"
es["ag_step4_p2"] = "Dentro de cada estilo de sonido, tambi\u00e9n puede ajustar:"
es["ag_step4_li4"] = "<strong>Tono de sonido</strong>: deslice el dedo hacia la izquierda para obtener un tono m\u00e1s bajo y profundo. Los sonidos de tono m\u00e1s grave (alrededor de 500 Hz) son m\u00e1s f\u00e1ciles de escuchar para las personas con p\u00e9rdida de audici\u00f3n de alta frecuencia relacionada con la edad. El valor predeterminado ya est\u00e1 configurado en un tono m\u00e1s bajo por este motivo."
es["ag_step4_li5"] = "<strong>Volumen</strong>: establezca el volumen con el que se reproduce el sonido de confirmaci\u00f3n."

es["ag_step5_h"] = "5. Flash de pantalla y flash de linterna"
es["ag_step5_who"] = "Personas con p\u00e9rdida de la audici\u00f3n que pueden omitir el sonido o cualquier persona en un entorno ruidoso. Tambi\u00e9n es \u00fatil cuando el tel\u00e9fono est\u00e1 boca abajo o en un bolsillo."
es["ag_step5_p1"] = "Cuando se env\u00eda una alerta con \u00e9xito, <span class=\"notranslate\" translate=\"no\">TapAlert</span> produce:"
es["ag_step5_li1"] = "<strong>Destello de la pantalla</strong>: toda la pantalla se ilumina de blanco tres veces en r\u00e1pida sucesi\u00f3n."
es["ag_step5_li2"] = "<strong>Destellos de linterna</strong>: el LED de la c\u00e1mara en la parte posterior del tel\u00e9fono parpadea tres veces simult\u00e1neamente, visible incluso cuando la pantalla est\u00e1 boca abajo."
es["ag_step5_p2"] = "Ambos destellos se ejecutan al mismo tiempo y se completan en menos de un segundo."
es["ag_step5_alert_h"] = "Como apagar esto"
es["ag_step5_alert_p"] = "Si tiene una condici\u00f3n fotosensible, vaya a <strong>Configuraci\u00f3n \u2192 Sonido de notificaci\u00f3n \u2192 Flash al recibir alerta</strong> y ap\u00e1guelo."

es["ag_step6_h"] = "6. Desliza para cancelar la cuenta regresiva"
es["ag_step6_who"] = "Cualquier persona que inicie accidentalmente una cuenta regresiva y necesite cancelarla r\u00e1pidamente."
es["ag_step6_p1"] = "Cuando toca el bot\u00f3n <span class=\"notranslate\" translate=\"no\">SOS</span>, aparece un cuadro de di\u00e1logo de cuenta regresiva antes de enviar la alerta. Puedes cancelarlo de dos maneras:"
es["ag_step6_li1"] = "Pulse el bot\u00f3n <strong>Cancelar</strong> en la parte inferior del cuadro de di\u00e1logo."
es["ag_step6_li2"] = "<strong>Desliza el dedo por el cuadro de di\u00e1logo hacia la izquierda o hacia la derecha</strong>: el cuadro de di\u00e1logo se desliza con el dedo y se descarta cuando lo sueltas lo suficiente."
es["ag_step6_p2"] = "De cualquier manera, sentir\u00e1 dos peque\u00f1as vibraciones confirmando que la alerta fue cancelada y no se envi\u00f3 nada."

es["ag_step7_h"] = "7. Composici\u00f3n de mensajes de voz"
es["ag_step7_who"] = "Personas con temblores, artritis u otras afecciones que dificultan la escritura."
es["ag_step7_p1"] = "En lugar de escribir un mensaje personalizado antes de enviar una alerta, puede hablarlo. Toque el <strong>icono del micr\u00f3fono</strong> en el campo del mensaje y pronuncie su mensaje. La aplicaci\u00f3n transcribir\u00e1 sus palabras autom\u00e1ticamente. El silencio durante 3 segundos detiene la grabaci\u00f3n."
es["ag_step7_p2"] = "Esto funciona en la entrada de mensajes de la pantalla de inicio y en el cuadro de di\u00e1logo del temporizador de control."

es["ag_step8_h"] = "8. Modo mantener presionado para enviar"
es["ag_step8_who"] = "Personas propensas a pulsar accidentalmente el bot\u00f3n <span class=\"notranslate\" translate=\"no\">SOS</span>."
es["ag_step8_p1"] = "De forma predeterminada, el bot\u00f3n <span class=\"notranslate\" translate=\"no\">SOS</span> requiere un solo toque. Si los toques accidentales son una preocupaci\u00f3n, puede cambiar al modo de <strong>Mantener pulsado para enviar</strong>:"
es["ag_step8_p2"] = "Vaya a <strong>Configuraci\u00f3n \u2192 M\u00e9todo de activaci\u00f3n \u2192 Mantener presionado para enviar</strong>."
es["ag_step8_p3"] = "En este modo, debe presionar y mantener presionado el bot\u00f3n durante todo el tiempo de espera antes de que se active la alerta, lo que evita env\u00edos accidentales."

es["ag_step9_h"] = "9. Widget de pantalla de inicio (Android)"
es["ag_step9_who"] = "Cualquiera a quien le resulte dif\u00edcil desbloquear su tel\u00e9fono y abrir la aplicaci\u00f3n en caso de emergencia."
es["ag_step9_p1"] = "En Android, puede agregar un widget de <span class=\"notranslate\" translate=\"no\">TapAlert</span> a su pantalla de inicio para que el bot\u00f3n <span class=\"notranslate\" translate=\"no\">SOS</span> est\u00e9 siempre a un toque de distancia, sin abrir la aplicaci\u00f3n en absoluto."
es["ag_step9_p2"] = "Para agregar el widget: <strong>Configuraci\u00f3n \u2192 Widget de la pantalla de inicio \u2192 Agregar widget</strong>."
es["ag_who_it_helps"] = "A qui\u00e9n ayuda:"

with open('locales/en.json', 'w') as f:
    json.dump(en, f, indent=4)

with open('locales/es.json', 'w') as f:
    json.dump(es, f, indent=4)

print("Updates applied to JSON files.")
