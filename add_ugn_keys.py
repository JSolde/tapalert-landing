"""
Inserts all ugn_* (user guide new) keys into en.json,
then runs Google Translate for every other locale file.
"""
import json, os, time, concurrent.futures

UGN_KEYS = {
    # Intro & TOC
    "ugn_intro": "A personal safety app that sends SMS and email alerts to your emergency contacts with your GPS location — with a single tap.",
    "ugn_toc_title": "Contents",
    "ugn_toc_1": "First Launch: Permissions",
    "ugn_toc_2": "Home Screen Overview",
    "ugn_toc_3": "Panic Mode",
    "ugn_toc_4": "Standard Mode",
    "ugn_toc_5": "Managing Recipients",
    "ugn_toc_6": "Sending an Alert",
    "ugn_toc_7": "Countdown Dialog",
    "ugn_toc_8": "Check-in Timer (Premium)",
    "ugn_toc_9": "Alert History",
    "ugn_toc_10": "Settings",
    "ugn_toc_11": "Home Screen Widget (Android)",
    "ugn_toc_12": "Making Alerts Stand Out on Recipients' Phones",
    "ugn_toc_13": "Remote Setup (Magic Link)",
    "ugn_toc_14": "Premium Upgrade",
    "ugn_toc_15": "Troubleshooting",
    # Section 1
    "ugn_s1_h2": "1. First Launch: Permissions",
    "ugn_s1_p1": "On first launch, TapAlert will walk you through a permissions setup screen. Grant the following for full functionality:",
    "ugn_s1_th1": "Permission",
    "ugn_s1_th2": "Why it's needed",
    "ugn_s1_r1c1": "Location",
    "ugn_s1_r1c2": "Includes your GPS coordinates and address in alerts",
    "ugn_s1_r2c1": "Microphone / Speech",
    "ugn_s1_r2c2": "Allows voice-to-text for custom alert messages",
    "ugn_s1_r3c1": "Contacts",
    "ugn_s1_r3c2": "Lets you pick recipients from your phone's address book",
    "ugn_s1_r4c1": "Notifications",
    "ugn_s1_r4c2": "Shows confirmation when an alert is sent",
    "ugn_s1_r5c1": "SMS (Android only)",
    "ugn_s1_r5c2": "Sends alerts directly from your SIM card",
    "ugn_s1_r6c1": "Phone State (Android only)",
    "ugn_s1_r6c2": "Detects cellular availability for smart fallback",
    "ugn_s1_p2": "You can grant or skip any permission during setup and adjust them later in your device's system settings.",
    # Section 2
    "ugn_s2_h2": "2. Home Screen Overview",
    "ugn_s2_p1": "The home screen has three pages you can navigate by swiping left or right:",
    "ugn_s2_th1": "Page",
    "ugn_s2_th2": "Name",
    "ugn_s2_th3": "Description",
    "ugn_s2_r1c1": "Left",
    "ugn_s2_r1c2": "Check-in Timer",
    "ugn_s2_r1c3": "Dead man's switch timer (Premium only)",
    "ugn_s2_r2c1": "Center",
    "ugn_s2_r2c2": "Panic Mode",
    "ugn_s2_r2c3": "Large SOS and I'm OK buttons — the default",
    "ugn_s2_r3c1": "Right",
    "ugn_s2_r3c2": "Standard Mode",
    "ugn_s2_r3c3": "Pre-configured alert message slots",
    "ugn_s2_p2": "The app always opens on Panic Mode (center page).",
    # Section 3
    "ugn_s3_h2": "3. Panic Mode",
    "ugn_s3_p1": "The central page is designed for maximum simplicity — ideal for emergencies and senior users.",
    "ugn_s3_li1": "SOS button — sends an \"SOS, I need help\" alert with your location.",
    "ugn_s3_li2": "I'm OK button — sends a reassuring \"I'm OK\" status to all contacts.",
    "ugn_s3_li3": "Voice buttons — tap the microphone icon next to SOS or I'm OK to record a voice message. Your speech is transcribed to text and included in the alert.",
    "ugn_s3_li4": "Emergency Call button — dials your local emergency number (e.g., 112, 911) immediately, based on your country setting.",
    # Section 4
    "ugn_s4_h2": "4. Standard Mode",
    "ugn_s4_p1": "Swipe right from Panic Mode to access Standard Mode. This page shows a list of pre-configured alert slots.",
    "ugn_s4_li1": "Text slots — up to 7 customizable message slots (default: 3). Tap any slot to edit the message. Tap the emoji icon to change its button icon.",
    "ugn_s4_li2": "Voice slot — always available as the last slot. Tap it to record a voice message in real time; the transcribed text is sent as the alert.",
    "ugn_s4_p2": "The number of visible text slots can be adjusted in Settings > Number of configured alerts.",
    # Section 5
    "ugn_s5_h2": "5. Managing Recipients",
    "ugn_s5_p1": "Tap the people icon in the top toolbar to open the Recipients screen.",
    "ugn_s5_li1": "Add manually — tap Add and enter a phone number in international format (e.g., +31600000000).",
    "ugn_s5_li2": "Add from Contacts — tap the contacts icon to pick directly from your phone's address book.",
    "ugn_s5_li3": "Add email — optionally add an email address to each recipient for email redundancy.",
    "ugn_s5_li4": "Remove — swipe or tap the delete icon next to any contact.",
    "ugn_s5_note1": "Free tier: up to 1 recipient. Premium: up to 50 recipients.",
    "ugn_s5_note2": "iOS tip: If you only see a few contacts, go to Settings > Privacy > Contacts > TapAlert and select All Contacts.",
    # Section 6
    "ugn_s6_h2": "6. Sending an Alert",
    "ugn_s6_li1": "Open the app (or tap your home screen widget).",
    "ugn_s6_li2": "Tap the alert button (SOS, I'm OK, or a Standard Mode slot).",
    "ugn_s6_li3": "If a countdown is configured, a dialog appears giving you time to cancel.",
    "ugn_s6_li4": "The app fetches your current GPS location and builds the message.",
    "ugn_s6_li5": "The alert sound plays while sending.",
    "ugn_s6_li6": "A status report is shown with per-recipient success or failure details.",
    "ugn_s6_p2": "The alert message includes:",
    "ugn_s6_li7": "Your name (if set in Settings)",
    "ugn_s6_li8": "The message text",
    "ugn_s6_li9": "A Google Maps link to your current location",
    "ugn_s6_li10": "Your battery level",
    # Section 7
    "ugn_s7_h2": "7. Countdown Dialog",
    "ugn_s7_p1": "Before sending, TapAlert shows a countdown to prevent accidental alerts.",
    "ugn_s7_li1": "Default duration: 10 seconds. Adjustable from 0 (immediate) to 30 seconds in Settings > Countdown Duration.",
    "ugn_s7_li2": "Cancel: Tap CANCEL any time during the countdown to abort.",
    "ugn_s7_li3": "Send immediately: Tap SEND NOW to skip the remaining delay.",
    # Section 8
    "ugn_s8_h2": "8. Check-in Timer (Premium)",
    "ugn_s8_p1": "The Check-in Timer is a dead man's switch: if you don't cancel it in time, TapAlert automatically sends an alert. Useful for hiking, traveling alone, or any situation where you want someone notified if you stop responding.",
    "ugn_s8_h3_start": "To start:",
    "ugn_s8_start_li1": "Swipe left to the Check-in Timer page.",
    "ugn_s8_start_li2": "Use the wheel pickers to set a duration (hours and minutes).",
    "ugn_s8_start_li3": "Optionally type a custom message.",
    "ugn_s8_start_li4": "Tap Start Timer.",
    "ugn_s8_h3_running": "While running:",
    "ugn_s8_run_li1": "The timer counts down on screen.",
    "ugn_s8_run_li2": "When less than 5 minutes remain, TapAlert plays a warning sound and shows a dialog:",
    "ugn_s8_run_li2a": "Cancel — dismiss the warning and let the timer continue.",
    "ugn_s8_run_li2b": "Stop — abort the timer (no alert will be sent).",
    "ugn_s8_run_li2c": "Restart — reset the timer to the original duration.",
    "ugn_s8_run_li3": "If the timer reaches zero without being stopped or reset, the alert is sent automatically.",
    "ugn_s8_note1": "Android: The timer runs as a foreground service and remains active when the app is in the background or the screen is off.",
    "ugn_s8_note2": "iOS: The timer may not fire if the app is force-closed. Keep the app running in the background.",
    # Section 9
    "ugn_s9_h2": "9. Alert History",
    "ugn_s9_p1": "Tap the clock icon in the top toolbar to view your alert history.",
    "ugn_s9_li1": "Shows timestamp, message, and delivery method for each alert.",
    "ugn_s9_li2": "Tap any entry for per-recipient success/failure details and error information.",
    "ugn_s9_li3": "Free tier: stores the last 20 alerts. Premium: stores up to 200.",
    "ugn_s9_li4": "Delete individual entries or clear all history from the trash icon.",
    # Section 10
    "ugn_s10_h2": "10. Settings",
    "ugn_s10_p1": "Tap the gear icon to open Settings.",
    "ugn_s10_h3_sms": "SMS Method",
    "ugn_s10_h4_android": "Android:",
    "ugn_s10_sms_li1": "Direct SMS — sends via your SIM card, no internet needed. Preferred when cellular is available.",
    "ugn_s10_sms_li2": "Twilio — sends via the Twilio API over internet (Wi-Fi or data). Used as automatic fallback if Direct SMS fails.",
    "ugn_s10_h4_ios": "iOS:",
    "ugn_s10_sms_li3": "iOS Messages (Manual) — opens the native Messages app pre-filled. You tap Send manually. No Twilio account needed.",
    "ugn_s10_sms_li4": "Twilio (Automatic) — sends automatically via the Twilio API. Requires a Twilio account.",
    "ugn_s10_twilio_note": "For Twilio setup instructions, see the Twilio Guide in the Help menu.",
    "ugn_s10_h3_email": "Email Redundancy",
    "ugn_s10_email_p1": "Configure SMTP email to send alerts via email in addition to SMS. Useful when SMS is unavailable but Wi-Fi is connected.",
    "ugn_s10_email_li1": "Go to Settings > Email Redundancy.",
    "ugn_s10_email_li2": "Enable Email Redundancy.",
    "ugn_s10_email_li3": "Select a preset provider (Gmail, Outlook, Yahoo, iCloud) or enter custom SMTP details.",
    "ugn_s10_email_li4": "Enter your email address and an App Password (recommended over your main password).",
    "ugn_s10_email_li5": "Tap Test Email Connection to verify before relying on it.",
    "ugn_s10_email_p2": "Emails are sent to any recipient in your list who has an email address saved.",
    "ugn_s10_h3_loc": "Location",
    "ugn_s10_loc_li1": "Include Location — appends GPS coordinates (Google Maps link) to every alert.",
    "ugn_s10_loc_li2": "Include Address — also attempts to resolve a street address from your coordinates.",
    "ugn_s10_h3_trigger": "Trigger Method",
    "ugn_s10_trigger_li1": "Tap to Send — a single tap starts the countdown.",
    "ugn_s10_trigger_li2": "Press and Hold (5s) — you must hold the button for 5 seconds. Recommended to prevent accidental sends.",
    "ugn_s10_h3_countdown": "Alert Countdown",
    "ugn_s10_countdown_p1": "Set the delay before the alert sends (0–30 seconds). A longer countdown gives you more time to cancel if triggered by mistake.",
    "ugn_s10_h3_sound": "Sound Settings",
    "ugn_s10_sound_li1": "Choose between Plain Sounds or Rich Sounds (or None).",
    "ugn_s10_sound_li2": "Sound Pattern — select from Fast Alert, Short Beeps, Musical Chime, Wailing Siren, Pulse Ringing, Pipe Organ, Metallic Ring, or Electronic Hive.",
    "ugn_s10_sound_li3": "Sound Pitch — Low, Standard, or High.",
    "ugn_s10_sound_li4": "Volume — adjust with the slider.",
    "ugn_s10_sound_li5": "SOS and I'm OK alerts have independent sound patterns.",
    "ugn_s10_h3_other": "Other Settings",
    "ugn_s10_other_li1": "Your Name — included in outgoing messages so recipients know who sent the alert.",
    "ugn_s10_other_li2": "Countdown Duration — delay before sending (see above).",
    "ugn_s10_other_li3": "Number of configured alerts — how many text slots appear in Standard Mode (3–7).",
    "ugn_s10_other_li4": "Auto-Start on Launch — triggers the countdown immediately when the app opens. Only enable this if you launch TapAlert via a physical button shortcut.",
    "ugn_s10_other_li5": "Flash on Alert — flashes the screen and torch when an alert is sent.",
    "ugn_s10_other_li6": "Home Country — ensures local phone numbers are formatted correctly.",
    "ugn_s10_other_li7": "App Language — override the interface language (default: device language).",
    "ugn_s10_other_li8": "App Theme — Light, Dark, or System Default.",
    # Section 11
    "ugn_s11_h2": "11. Home Screen Widget (Android)",
    "ugn_s11_p1": "Add a TapAlert widget to your Android home screen for one-tap access without opening the app.",
    "ugn_s11_h3_add": "To add:",
    "ugn_s11_add_li1": "Go to Settings > Widget > Add Widget.",
    "ugn_s11_add_li2": "Choose Standard (1x1) for a compact icon or Large (2x2) for higher visibility.",
    "ugn_s11_add_li3": "Follow the on-screen instructions to place it on your home screen.",
    "ugn_s11_h3_how": "How it works:",
    "ugn_s11_how_li1": "Tapping the widget opens the app and immediately starts the alert countdown.",
    "ugn_s11_how_li2": "The sound plays and the countdown dialog appears — you can still cancel if triggered by mistake.",
    # Section 12
    "ugn_s12_h2": "12. Making Alerts Stand Out on Recipients' Phones",
    "ugn_s12_p1": "Your recipients can configure their phones to give TapAlert messages a special ringtone or bypass Do Not Disturb.",
    "ugn_s12_h3_iphone": "iPhone recipients:",
    "ugn_s12_iphone_li1": "Open Contacts and find your entry.",
    "ugn_s12_iphone_li2": "Tap Edit > Text Tone.",
    "ugn_s12_iphone_li3": "Enable Emergency Bypass — this bypasses Silent mode and Do Not Disturb.",
    "ugn_s12_iphone_li4": "Choose a loud, distinctive tone.",
    "ugn_s12_h3_android": "Android recipients:",
    "ugn_s12_android_li1": "Open the Messages app and find the conversation.",
    "ugn_s12_android_li2": "Tap the menu > Details > Notifications.",
    "ugn_s12_android_li3": "Set priority to High or Urgent.",
    "ugn_s12_android_li4": "Enable Override Do Not Disturb.",
    "ugn_s12_tip": "Using Twilio? Your contacts will receive messages from your Twilio number or sender ID (e.g., TapAlert). They should add that number/ID to their contacts for the above settings to apply.",
    # Section 13
    "ugn_s13_h2": "13. Remote Setup (Magic Link)",
    "ugn_s13_p1": "A family member or caregiver can configure TapAlert on your device remotely using a Magic Link.",
    "ugn_s13_p2": "The caregiver opens TapAlert, selects Set Up for Someone Else, fills in the contacts, message templates, and optional Twilio/email credentials, then generates a setup link. When you tap that link on your device, TapAlert applies the full configuration automatically.",
    "ugn_s13_p3": "This means a tech-savvy family member can set everything up without needing to be present — you just tap a link.",
    # Section 14
    "ugn_s14_h2": "14. Premium Upgrade",
    "ugn_s14_p1": "Some features require a one-time Premium upgrade (no subscription):",
    "ugn_s14_th1": "Feature",
    "ugn_s14_th2": "Free",
    "ugn_s14_th3": "Premium",
    "ugn_s14_r1c1": "Recipients",
    "ugn_s14_r1c2": "1",
    "ugn_s14_r1c3": "Up to 50",
    "ugn_s14_r2c1": "Alert history",
    "ugn_s14_r2c2": "20 entries",
    "ugn_s14_r2c3": "200 entries",
    "ugn_s14_r3c1": "Check-in Timer",
    "ugn_s14_r3c2": "—",
    "ugn_s14_r3c3": "Included",
    "ugn_s14_p2": "Tap Upgrade from the recipients screen or the timer page. If you have already purchased Premium on another device, tap Restore Purchases.",
    # Section 15
    "ugn_s15_h2": "15. Troubleshooting",
    "ugn_s15_th1": "Problem",
    "ugn_s15_th2": "Solution",
    "ugn_s15_r1c1": "Alert not sending (Direct SMS)",
    "ugn_s15_r1c2": "Check cellular signal and SIM credits",
    "ugn_s15_r2c1": "Alert not sending (Twilio)",
    "ugn_s15_r2c2": "Check internet connection and Twilio credentials in Settings",
    "ugn_s15_r3c1": "Location missing",
    "ugn_s15_r3c2": "Enable GPS in system settings and grant Location permission to TapAlert",
    "ugn_s15_r4c1": "Address not showing",
    "ugn_s15_r4c2": "Enable Include Address in Settings; requires internet for geocoding",
    "ugn_s15_r5c1": "Contacts not appearing (iOS)",
    "ugn_s15_r5c2": "Settings > Privacy > Contacts > TapAlert > All Contacts",
    "ugn_s15_r6c1": "Contacts not appearing (Android)",
    "ugn_s15_r6c2": "Settings > Apps > TapAlert > Permissions > enable Contacts",
    "ugn_s15_r7c1": "Timer not firing (iOS)",
    "ugn_s15_r7c2": "Keep TapAlert open in the background; the timer may not fire if the app is force-closed",
    "ugn_s15_r8c1": "Wrong language shown",
    "ugn_s15_r8c2": "Settings > App Language — select your preferred language manually",
}

# ── 1. Insert into en.json ──────────────────────────────────────────────────
en_path = "locales/en.json"
with open(en_path, "r", encoding="utf-8") as f:
    en_data = json.load(f)

already = sum(1 for k in UGN_KEYS if k in en_data)
print(f"Keys already present: {already}/{len(UGN_KEYS)}")
en_data.update(UGN_KEYS)
with open(en_path, "w", encoding="utf-8") as f:
    json.dump(en_data, f, indent=4, ensure_ascii=False)
print(f"en.json updated ({len(en_data)} total keys)")

# ── 2. Translate missing keys for every other locale ───────────────────────
try:
    from deep_translator import GoogleTranslator
except ImportError:
    print("deep_translator not installed — skipping translation")
    exit(0)

LANGS = ["ca", "de", "es", "eu", "fr", "gl", "it", "nl", "pt"]
LANG_CODES = {   # deep_translator language codes
    "ca": "ca", "de": "de", "es": "es", "eu": "eu",
    "fr": "fr", "gl": "gl", "it": "it", "nl": "nl", "pt": "pt",
}

def translate_one(text, target):
    if not text or not text.strip():
        return text
    try:
        return GoogleTranslator(source="en", target=target).translate(text)
    except Exception as e:
        print(f"  Error ({target}): {e}")
        return text

for lang in LANGS:
    path = f"locales/{lang}.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    missing = {k: en_data[k] for k in UGN_KEYS if k not in data}
    if not missing:
        print(f"{lang}: nothing to translate")
        continue

    print(f"{lang}: translating {len(missing)} keys…")
    target_code = LANG_CODES[lang]
    for i, (key, val) in enumerate(missing.items()):
        data[key] = translate_one(val, target_code)
        time.sleep(0.08)
        if (i + 1) % 20 == 0:
            print(f"  {lang}: {i+1}/{len(missing)}")

    # Preserve key order from en.json
    final = {k: data.get(k, en_data[k]) for k in en_data}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(final, f, indent=4, ensure_ascii=False)
    print(f"{lang}: done ✓")

print("\nAll translations complete.")
