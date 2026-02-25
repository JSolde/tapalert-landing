# User Guide: TapAlert

TapAlert is a personal safety app that sends SMS and email alerts to your emergency contacts with your GPS location — with a single tap.

---

## 1. 🛡️ First Launch: Permissions

On first launch, TapAlert will walk you through a permissions setup screen. Grant the following for full functionality:

| Permission | Why it's needed |
|---|---|
| **Location** | Includes your GPS coordinates and address in alerts |
| **Microphone / Speech** | Allows voice-to-text for custom alert messages |
| **Contacts** | Lets you pick recipients from your phone's address book |
| **Notifications** | Shows confirmation when an alert is sent |
| **SMS** *(Android only)* | Sends alerts directly from your SIM card |
| **Phone State** *(Android only)* | Detects cellular availability for smart fallback |

You can grant or skip any permission during setup and adjust them later in your device's system settings.

---

## 2. 📱 Home Screen Overview

The home screen has **three pages** you can navigate by swiping left or right:

| Page | Name | Description |
|---|---|---|
| ← Left | **Check-in Timer** | Dead man's switch timer *(Premium only)* |
| Center | **Panic Mode** | Large SOS and I'm OK buttons — the default |
| Right → | **Standard Mode** | Pre-configured alert message slots |

The app always opens on **Panic Mode** (center page).

---

## 3. 🆘 Panic Mode

The central page is designed for maximum simplicity — ideal for emergencies and senior users.

- **SOS button** — sends an "SOS, I need help" alert with your location.
- **I'm OK button** — sends a reassuring "I'm OK" status to all contacts.
- **Voice buttons** — tap the microphone icon next to SOS or I'm OK to record a voice message. Your speech is transcribed to text and included in the alert.
- **Emergency Call button** — dials your local emergency number (e.g., 112, 911) immediately, based on your country setting.

---

## 4. 📋 Standard Mode

Swipe right from Panic Mode to access Standard Mode. This page shows a list of pre-configured alert slots.

- **Text slots** — up to 7 customizable message slots (default: 3). Tap any slot to edit the message. Tap the emoji icon to change its button icon.
- **Voice slot** — always available as the last slot. Tap it to record a voice message in real time; the transcribed text is sent as the alert.

The number of visible text slots can be adjusted in **Settings → Number of configured alerts**.

---

## 5. 👥 Managing Recipients

Tap the **people icon** in the top toolbar to open the Recipients screen.

- **Add manually** — tap **Add** and enter a phone number in international format (e.g., `+31600000000`).
- **Add from Contacts** — tap the contacts icon to pick directly from your phone's address book.
- **Add email** — optionally add an email address to each recipient for email redundancy.
- **Remove** — swipe or tap the delete icon next to any contact.

> **Free tier:** up to 1 recipient. **Premium:** up to 50 recipients.

> **iOS tip:** If you only see a few contacts, go to **Settings → Privacy → Contacts → TapAlert** and select **All Contacts**.

---

## 6. 🚀 Sending an Alert

1. Open the app (or tap your home screen widget).
2. Tap the alert button (SOS, I'm OK, or a Standard Mode slot).
3. If a **countdown** is configured, a dialog appears giving you time to cancel.
4. The app fetches your current GPS location and builds the message.
5. The alert sound plays while sending.
6. A **status report** is shown with per-recipient success or failure details.

The alert message includes:
- Your name (if set in Settings)
- The message text
- A Google Maps link to your current location
- Your battery level

---

## 7. ⏱️ Countdown Dialog

Before sending, TapAlert shows a countdown to prevent accidental alerts.

- **Default duration:** 10 seconds. Adjustable from 0 (immediate) to 30 seconds in **Settings → Countdown Duration**.
- **Cancel:** Tap **CANCEL** any time during the countdown to abort.
- **Send immediately:** Tap **SEND NOW** to skip the remaining delay.

---

## 8. ⏰ Check-in Timer *(Premium)*

The Check-in Timer is a "dead man's switch": if you don't cancel it in time, TapAlert automatically sends an alert. Useful for hiking, traveling alone, or any situation where you want someone notified if you stop responding.

**To start:**
1. Swipe left to the **Check-in Timer** page.
2. Use the wheel pickers to set a duration (hours and minutes).
3. Optionally type a custom message.
4. Tap **Start Timer**.

**While running:**
- The timer counts down on screen.
- When **less than 5 minutes remain**, TapAlert plays a warning sound and shows a dialog:
  - **Cancel** — dismiss the warning and let the timer continue.
  - **Stop** — abort the timer (no alert will be sent).
  - **Restart** — reset the timer to the original duration.
- If the timer reaches zero without being stopped or reset, the alert is sent automatically.

> **Android:** The timer runs as a foreground service and remains active when the app is in the background or the screen is off.
>
> **iOS:** The timer may not fire if the app is force-closed. Keep the app running in the background.

---

## 9. 📜 Alert History

Tap the **clock icon** in the top toolbar to view your alert history.

- Shows timestamp, message, and delivery method for each alert.
- Tap any entry for per-recipient success/failure details and error information.
- **Free tier:** stores the last 20 alerts. **Premium:** stores up to 200.
- Delete individual entries or clear all history from the trash icon.

---

## 10. ⚙️ Settings

Tap the **gear icon** to open Settings.

### SMS Method

**Android:**
- **Direct SMS** — sends via your SIM card, no internet needed. Preferred when cellular is available.
- **Twilio** — sends via the Twilio API over internet (Wi-Fi or data). Used as automatic fallback if Direct SMS fails.

**iOS:**
- **iOS Messages (Manual)** — opens the native Messages app pre-filled. You tap Send manually. No Twilio account needed.
- **Twilio (Automatic)** — sends automatically via the Twilio API. Requires a Twilio account.

> For Twilio setup instructions, see the **Twilio Guide** in the Help menu.

### Email Redundancy

Configure SMTP email to send alerts via email in addition to SMS. Useful when SMS is unavailable but Wi-Fi is connected.

1. Go to **Settings → Email Redundancy**.
2. Enable **Email Redundancy**.
3. Select a preset provider (Gmail, Outlook, Yahoo, iCloud) or enter custom SMTP details.
4. Enter your email address and an **App Password** (recommended over your main password).
5. Tap **Test Email Connection** to verify before relying on it.

Emails are sent to any recipient in your list who has an email address saved.

### Location

- **Include Location** — appends GPS coordinates (Google Maps link) to every alert.
- **Include Address** — also attempts to resolve a street address from your coordinates.

### Trigger Method

- **Tap to Send** — a single tap starts the countdown.
- **Press & Hold (5s)** — you must hold the button for 5 seconds. Recommended to prevent accidental sends.

### Alert Countdown

Set the delay before the alert sends (0–30 seconds). A longer countdown gives you more time to cancel if triggered by mistake.

### Sound Settings

- Choose between **Plain Sounds** or **Rich Sounds** (or None).
- **Sound Pattern** — select from Fast Alert, Short Beeps, Musical Chime, Wailing Siren, Pulse Ringing, Pipe Organ, Metallic Ring, or Electronic Hive.
- **Sound Pitch** — Low, Standard, or High.
- **Volume** — adjust with the slider.
- SOS and I'm OK alerts have independent sound patterns.

### Other Settings

- **Your Name** — included in outgoing messages so recipients know who sent the alert.
- **Countdown Duration** — delay before sending (see above).
- **Number of configured alerts** — how many text slots appear in Standard Mode (3–7).
- **Auto-Start on Launch** — triggers the countdown immediately when the app opens. Only enable this if you launch TapAlert via a physical button shortcut.
- **Flash on Alert** — flashes the screen and torch when an alert is sent.
- **Home Country** — ensures local phone numbers are formatted correctly.
- **App Language** — override the interface language (default: device language).
- **App Theme** — Light, Dark, or System Default.

---

## 11. 📱 Home Screen Widget *(Android)*

Add a TapAlert widget to your Android home screen for one-tap access without opening the app.

**To add:**
1. Go to **Settings → Widget → Add Widget**.
2. Choose **Standard (1×1)** for a compact icon or **Large (2×2)** for higher visibility.
3. Follow the on-screen instructions to place it on your home screen.

**How it works:**
- Tapping the widget opens the app and immediately starts the alert countdown.
- The sound plays and the countdown dialog appears — you can still cancel if triggered by mistake.

---

## 12. 🔔 Making Alerts Stand Out on Recipients' Phones

Your recipients can configure their phones to give TapAlert messages a special ringtone or bypass Do Not Disturb.

**iPhone recipients:**
1. Open **Contacts** and find your entry.
2. Tap **Edit → Text Tone**.
3. Enable **Emergency Bypass** — this bypasses Silent mode and Do Not Disturb.
4. Choose a loud, distinctive tone.

**Android recipients:**
1. Open the **Messages** app and find the conversation.
2. Tap the menu → **Details → Notifications**.
3. Set priority to **High** or **Urgent**.
4. Enable **Override Do Not Disturb**.

> **Using Twilio?** Your contacts will receive messages from your Twilio number or sender ID (e.g., "TapAlert"). They should add that number/ID to their contacts for the above settings to apply.

---

## 13. 🔗 Remote Setup (Magic Link)

A family member or caregiver can configure TapAlert on your device remotely using a **Magic Link**.

The caregiver opens TapAlert, selects **Set Up for Someone Else**, fills in the contacts, message templates, and optional Twilio/email credentials, then generates a setup link. When you tap that link on your device, TapAlert applies the full configuration automatically.

This means a tech-savvy family member can set everything up without needing to be present — you just tap a link.

---

## 14. 🌟 Premium Upgrade

Some features require a one-time Premium upgrade (no subscription):

| Feature | Free | Premium |
|---|---|---|
| Recipients | 1 | Up to 50 |
| Alert history | 20 entries | 200 entries |
| Check-in Timer | — | ✓ |

Tap **Upgrade** from the recipients screen or the timer page. If you've already purchased Premium on another device, tap **Restore Purchases**.

---

## 15. ❓ Troubleshooting

| Problem | Solution |
|---|---|
| Alert not sending (Direct SMS) | Check cellular signal and SIM credits |
| Alert not sending (Twilio) | Check internet connection and Twilio credentials in Settings |
| Location missing | Enable GPS in system settings and grant Location permission to TapAlert |
| Address not showing | Enable "Include Address" in Settings; requires internet for geocoding |
| Contacts not appearing (iOS) | Settings → Privacy → Contacts → TapAlert → **All Contacts** |
| Contacts not appearing (Android) | Settings → Apps → TapAlert → Permissions → enable **Contacts** |
| Timer not firing (iOS) | Keep TapAlert open in the background; the timer may not fire if the app is force-closed |
| Wrong language shown | Settings → App Language — select your preferred language manually |
