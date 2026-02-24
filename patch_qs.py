import json

with open('locales/en.json', 'r') as f:
    en = json.load(f)

with open('locales/es.json', 'r') as f:
    es = json.load(f)

# Updates for EN
en["qs_step3_h"] = "3. Connectivity & <span class=\"notranslate\" translate=\"no\">fallback</span>s"
en["qs_step3_p1_new"] = "Verify if <strong>Wifi calls</strong> are enabled on your phone. If your carrier doesn't support it, consider using a <strong><span class=\"notranslate\" translate=\"no\">Twilio</span> account</strong> as a <span class=\"notranslate\" translate=\"no\">fallback</span> for Wifi-only situations. <span class=\"notranslate\" translate=\"no\">Twilio</span> is free to start and provides reliable SMS delivery without a cell signal."
en["qs_step3_p2_new"] = "You can also enable <strong>Email redundancy</strong> in <span class=\"notranslate\" translate=\"no\">TapAlert</span> to ensure your loved ones are notified via multiple channels."

en["qs_step4_h"] = "4. Perform a Test Alert"
en["qs_step4_p"] = "Test your setup by sending an <strong>‘I’m OK’</strong> message. Tap the button once (or hold for 5s if configured). A countdown will appear, giving you time to cancel or send immediately. Letting it expire sends the alert automatically!"

en["qs_step5_h"] = "5. Explore Navigation"
en["qs_step5_p"] = "Swipe <strong>Left</strong> to access your preconfigured custom messages for specific situations. Swipe <strong>Right</strong> to activate the <strong>Check-in Timer</strong> (Dead Man's Switch), which auto-alerts if you don't check in by a certain time."

en["qs_step6_h"] = "6. Setup for Others"
en["qs_step6_p"] = "If you’re setting this phone up for someone else (like a senior relative), take a moment to preconfigure their custom alerts (Swipe Left) so they have the most relevant messages ready at their fingertips."

# Updates for ES
es["qs_step3_h"] = "3. Conectividad y <span class=\"notranslate\" translate=\"no\">fallback</span>s"
es["qs_step3_p1_new"] = "Verifica si las <strong>Llamadas Wi-Fi</strong> están habilitadas en tu teléfono. Si tu operador no lo soporta, considera usar una cuenta de <strong><span class=\"notranslate\" translate=\"no\">Twilio</span></strong> como <span class=\"notranslate\" translate=\"no\">fallback</span> para situaciones de solo Wi-Fi. <span class=\"notranslate\" translate=\"no\">Twilio</span> es gratis para empezar y proporciona una entrega de SMS confiable sin señal celular."
es["qs_step3_p2_new"] = "También puedes habilitar la <strong>Redundancia por correo electrónico</strong> en <span class=\"notranslate\" translate=\"no\">TapAlert</span> para garantizar que tus seres queridos sean notificados a través de múltiples canales."

es["qs_step4_h"] = "4. Realiza una Alerta de Prueba"
es["qs_step4_p"] = "Prueba tu configuración enviando un mensaje de <strong>‘Estoy OK’</strong>. Toca el botón una vez (o mantenlo presionado 5s si así lo configuraste). Aparecerá una cuenta regresiva dándote tiempo para cancelar o enviar inmediatamente. ¡Dejar que termine envía la alerta automáticamente!"

es["qs_step5_h"] = "5. Explora la Navegación"
es["qs_step5_p"] = "Desliza a la <strong>Izquierda</strong> para acceder a tus mensajes personalizados para situaciones específicas. Desliza a la <strong>Derecha</strong> para activar el <strong>Temporizador de Control</strong>, que envía automáticamente una alerta si no te reportas a una hora establecida."

es["qs_step6_h"] = "6. Configuración para Otros"
es["qs_step6_p"] = "Si configuras este teléfono para otra persona (como un familiar mayor), tómate un momento para preconfigurar sus alertas personalizadas (Desliza a la Izquierda) y tener listos los mensajes más relevantes."

with open('locales/en.json', 'w') as f:
    json.dump(en, f, indent=4)

with open('locales/es.json', 'w') as f:
    json.dump(es, f, indent=4)

print("Updates applied to JSON files.")
