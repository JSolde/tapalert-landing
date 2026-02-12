# User Guide: TapAlert

This guide explains how to configure and use **TapAlert** on your Android or iOS device.

## 1. 🛡️ Required Permissions

Upon first launch, the app will request the following permissions:
-   **SMS (Android Only):** Needed to send direct messages from your phone's SIM card.
-   **Location:** Needed to include your GPS coordinates in the alert message.
-   **Microphone:** Needed if you use the voice recording feature to transcribe your alert message.
-   **Contacts:** Needed to easily select recipients from your phone's address book.

> [!NOTE]
> On iOS, direct SMS sending is not supported by the system for automated alerts. You must use the **Twilio** method.

## 2. 📱 Interface Modes

TapAlert offers two distinct interface modes to suit your needs. You can switch between them in **Settings > Interface Mode**.

### Panic Mode (SOS / OK)
A streamlined interface designed for maximum simplicity and accessibility, ideal for elderly users or high-stress situations.
- **Large SOS Button:** Instantly starts the countdown for an "SOS, I need help" alert.
- **I'm OK Button:** Quickly sends an "I'm OK" status update to reassure contacts.
- **Voice Buttons:** Each section has a dedicated voice button to record and send an audio transcript along with the SOS or OK status.
- **Emergency Call Button:** A dedicated button to immediately call local emergency services (e.g., 112, 911) based on your location.

### Report Mode (Tabs)
The default mode, offering flexibility with multiple message types.
- **4 Message Tabs:** Pre-configure different alerts (e.g., "Medical", "Car Trouble", "Generic").
- **Customizable Text:** Tap inside the message box to edit content on the fly.
- **Voice Transcription:** Use the microphone to dictate a custom message.

## 3. 📝 Setup Predefined Messages (Report Mode)

TapAlert comes with 4 predefined message slots (tabs) allowing you to quickly switch between different alert scenarios.

### Editing Messages
1.  **Select a Tab:** Tap on one of the numbered tabs (1-3) at the top.
2.  **Edit Text:** Tap inside the message box to type your custom alert message (e.g., "Medical Emergency", "Car Trouble"). 
3.  **Auto-Save:** Your changes are saved automatically as you type.
4.  **Dictation:** You can also use the dictation icon to dictate your message.

### 🎙️ Voice Quick Alert Message
You can use your voice to generate the alert text in real-time. This is useful for describing a specific situation quickly. The message will be saved on the 4th tab.

1.  **Tap the Microphone red button:** It will start **pulsing** when active.
2.  **Speak your message:** The status bar at the bottom will turn **light orange** and show a sound wave symbol while listening.
3.  **Automatic Update and Instant Send:** After speaking or tapping the microphone button again, the message text will be updated and the **SEND ALERT** will be triggered immediately. You can also press the **SEND ALERT** button directly while recording; the app will automatically stop the recording and save and send the transcribed message immediately.

## 4. 👥 Setup/Managing Recipients

This is done in the dedicated **Recipients Screen**, accessible from the top bar of the Home Screen:

1.  **Open Recipients:** Tap the **People/Group Icon** (👥) in the top-right toolbar.
2.  **Add Number:**
    -   Tap the **"Add"** button to manually enter a phone number.
    -   Tap the **Contact Icon** to pick a number directly from your phone's address book.
3.  **Format:** Use the **E.164 international format** (e.g., `+34600000000`) for best results.
4.  **Remove:** Tap the delete icon next to any number in the list to remove it. You can also "Delete All" using the trash bin icon at the top.

> [!TIP]
> **Can't see all your contacts?**
> - **iOS:** If you chose "Select Contacts..." (Limited Access), the app can only see the few you picked. To fix this, go to **iPhone Settings > Privacy & Security > Contacts > TapAlert** and select **"All Contacts"**.
> - **Android:** Permissions are "all-or-nothing". If you denied access, the picker will be empty. Ensure the app has "Contacts" permission in your phone's App Settings.

## 5. ⚙️ Configuration Options

Access the settings menu via the gear icon ⚙️ to further customize the alert message text and the SMS delivery method.

### SMS Sending Methods

The app supports two ways to send messages:

*   **Direct SMS (Android):** Uses your phone's SIM card. Cost depends on your mobile carrier plan.
*   **Twilio SMS (Android & iOS):** Uses the Twilio API over the internet (Wi-Fi/Data). Reliable and required for iOS.

### Smart Redundancy (Android Only)
TapAlert features a **Smart Redundancy** system that automatically switches methods if the primary one fails:
*   **No Signal?** If you try to send a Direct SMS but have no cellular coverage (e.g., inside a building), the app will automatically attempt to send via Twilio (Wi-Fi).
*   **No Data?** If you use Twilio as primary but are hiking without 4G/5G, the app will automatically fallback to sending a Direct SMS.

**To enable:** Go to Settings and turn on **"Smart Redundancy"**.

### Email Redundancy (Wi-Fi Fallback)
If you have no cellular signal but are connected to Wi-Fi, TapAlert can send your alert via email.
- **Setup:** Go to **Settings > Email Redundancy**. For detailed instructions, see **Chapter 6: Configuring Email Redundancy**.
- **Automatic Fallback:** When enabled, the app will attempt to send an email alert if both Direct SMS and Twilio (cellular) fail.

### Trigger Method (Tap vs. Hold)
Prevent accidental triggers by changing how the alert is activated in **Settings > Trigger Method**:
- **Tap to Send (Default):** A single tap on the alert button triggers the countdown.
- **Press & Hold (5s):** You must hold the alert button for 5 continuous seconds to trigger the countdown. This is recommended to avoid false alarms.

> [!IMPORTANT]
> **iOS Users:** You must configure a Twilio account.
> 
> 👉 **For detailed Twilio setup instructions, please see the separate "Twilio Guide" in the Help menu.**

### Auto-Start on Launch
Automatically start the alert countdown immediately when the app opens.
*   **Useful for:** Creating a physical panic button (using hardware key remapping) or a quick-launch shortcut.
*   **Warning:** When enabled, opening the app will always trigger the countdown. You can cancel it during the delay period.

### Message Location
-   **Include Location:** Append GPS coordinates to the message.
-   **Include Address:** Attempt to convert coordinates into a human-readable address.

### Additional Settings
-   **Sender Identity:** (Twilio Only) Choose the name or number that appears as the sender (e.g., "Alert" or your specific Twilio number).
-   **Appearance:** Toggle between Light Mode, Dark Mode, or follow System Settings.
-   **App Language:** Manually override the app's language (default: System Language).
-   **Region and formatting:** Set your region to ensure phone numbers are formatted correctly (e.g., auto-adding country codes).
-   **Notification sound:** Choose the alert sound that plays after a successful message delivery.

## 6. 📧 Configuring Email Redundancy

If you have no cellular signal but are connected to Wi-Fi, TapAlert can send your alert via email.

### Setup Instructions
1.  **Open Settings:** Tap the gear icon ⚙️ and select **Email Redundancy**.
2.  **Enable the feature:** Toggle **Enable Email Redundancy** to ON.
3.  **SMTP Configuration:** Enter your email provider's SMTP details:
    - **SMTP Host:** (e.g., `smtp.gmail.com` for Gmail, `smtp-mail.outlook.com` for Outlook).
    - **SMTP Port:** (e.g., `587` or `465`).
    - **Username / Email:** Your full email address.
    - **Password / App Password:** Your email password or a dedicated App Password.

### ⚡ Quick Setup (Common Providers)
TapAlert includes preset buttons for popular email providers. Simply tap a preset button to auto-fill the SMTP host and port settings:

- **Gmail** (smtp.gmail.com:587)
- **Outlook** (smtp-mail.outlook.com:587)
- **Yahoo** (smtp.mail.yahoo.com:587)
- **iCloud** (smtp.mail.me.com:587)

After tapping a preset, you only need to enter your email address and app password (see below).

> [!IMPORTANT]
> **App Passwords Are Provider-Specific**
>
> Each email provider has its own app password system. You cannot use a Gmail app password with Outlook, or vice versa. You must generate an app password specific to the provider you're using.

### 🔒 Using App Passwords (Recommended)
For security and reliability, we strongly recommend using an **App Password** instead of your primary password.
- **Why?** It bypasses 2-Factor Authentication and keeps your main account secure.
- **How to generate:**

#### Gmail
  1. Go to your **Google Account > Security** or [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
  2. Search for **"App passwords"** (requires 2-step verification enabled).
  3. Generate a new password for "Other" and call it "TapAlert".
  4. Use the 16-character code provided in TapAlert (blanks included).

#### Outlook / Hotmail / Live
  1. Go to **Microsoft Account > Security > Advanced security options** or [https://account.live.com/names/manage](https://account.live.com/names/manage).
  2. Under **"App passwords"**, create a new app password.
  3. Select "Other" and name it "TapAlert".
  4. Use the generated password in TapAlert.

#### Yahoo
  1. Go to **Yahoo Account Security** or [https://login.yahoo.com/account/security](https://login.yahoo.com/account/security).
  2. Select **"Generate app password"**.
  3. Choose "Other App" and name it "TapAlert".
  4. Use the generated password in TapAlert.

#### iCloud
  1. Go to **appleid.apple.com > Sign-In and Security > App-Specific Passwords** or [https://appleid.apple.com/account/manage](https://appleid.apple.com/account/manage).
  2. Click the **+** button to generate a new password.
  3. Name it "TapAlert".
  4. Use the generated password in TapAlert.  

### Recipients
Emails will be sent to all contacts in your **Recipients** list who have an email address saved. To add an email to a contact:
1. Go to the **Recipients** screen.
2. Edit a contact and ensure the email field is filled.

### 🧪 Testing
Before relying on it, tap **Test Connection**. Enter an email address to receive a test message. If successful, your setup is correct.

## 7. 📱 Home Screen Widget (Android Only)

For even faster emergency alerts, you can add a widget to your Android home screen:

### Adding the Widget

1.  **Open Settings:** Tap the gear icon ⚙️ in the app.
2.  **Find Widget Section:** Scroll down to the "Widget" section.
3.  **Tap "Add":** The system will prompt you to place the widget on your home screen.
4.  **Position the Widget:** Drag it to your preferred location and release.

> [!NOTE]
> If you already have a widget on your home screen, you'll need to remove the old one before adding a new one.

### Using the Widget

-   **Tap the Widget:** Opens the app and starts the **Countdown** immediately.
-   **App Experience:** You will see the countdown dialog, ensuring the alert is intentional. You can cancel it if pressed by mistake.
-   **Sound:** The app plays an audible alert tone while counting down.

> [!TIP]
> The widget is perfect for true emergencies when you need to send an alert with a single tap, without finding the app in your drawer.

## 8. 🚀 Sending an Alert
1.  **Open the App.**
2.  **Trigger the Alert:**
    *   **In Report Mode:** Tap the large red **SEND ALERT** button. The message selected in the tabs (1-4) will be sent.
    *   **In Panic Mode:** 
        *   Tap the big red **SOS** button to send a "Help needed" alert.
        *   Tap the **Microphone icon** (bottom-right of SOS) to record and send a specific voice message with your SOS alert.
        *   Tap the green **I'm OK** button to send a reassuring "I'm OK" status.
        *   Tap the **Microphone icon** (bottom-right of I'm OK) to record and send a voice message with your OK status.
        *   Tap the **Emergency Call** button to dial local emergency services immediately.
3.  **The app will:**
    -   Fetch your current location (if configured).
    -   Show a **Countdown Dialog** (see "Countdown Dialog" below).
    -   Send the alert message to all recipients.

## 9. ⏱️ Countdown Dialog

To prevent accidental alerts, TapAlert shows a countdown before sending.

-   **Countdown Duration:** By default, the app waits **10 seconds**. You can customize this in **Settings** (from **0s** for immediate sending up to **30s**).
-   **Cancelling:** You can tap **CANCEL** during the countdown to stop the alert.

## 10. 🔔 Making Alert SMS Stand Out
To ensure your emergency contacts don't miss your alert message among other notifications, we recommend configuring their phones to treat messages from your TapAlert number differently.

### For iPhone Recipients
1. **Open Contacts:** Select your contact entry.
2. **Assign Emergency Bypass:** Tap **Edit** > **Ringtone** (or Text Tone) and toggle **Emergency Bypass** ON. This allows sounds/vibrations even if their phone is on Silent or Do Not Disturb.
3. **Custom Tone:** Choose a loud, distinct sound for your messages.

### For Android Recipients
1. **Open Messages:** Select the conversation with you.
2. **Notification Categories:** Tap **Details** > **Notifications**.
3. **Set as "Urgent":** Change the priority to **"High"** or **"Urgent"**.
4. **Override DND:** Ensure **"Ignore Do Not Disturb"** is enabled for this conversation.
5. **Custom Sound:** Pick a high-priority alert sound.

> [!NOTE]
> **Using Twilio?** If you send alerts via Twilio, your contacts will receive the message from your Twilio number or an Alphanumeric ID (e.g., "TapAlert"). They **must** add this number/ID to their contacts list for the settings above to work correctly. Otherwise, the message will still be delivered but as a standard SMS without any priority notifications.

## 11. 🕰️ Alert History

To keep track of your sent emergency alerts:
1.  **Tap the History Icon:** The clock icon 🕰️ located in the top bar.
2.  **View Recent Alerts:** The app maintains a log of the last **50 alerts** sent.
3.  **Check Status:** Tap any entry to see exactly which recipients received the message successfully and which failed (with error details).
4.  **Clear History:** You can delete all logs by tapping the trash icon 🗑️ inside the history screen.

## 12. ❓ Troubleshooting

-   **Message not sending (Direct SMS):** Check your mobile signal and carrier credit (Android only).
-   **Message not sending (Twilio):** Verify your internet connection and double-check your credentials in the settings.
-   **Location missing:** Ensure GPS is enabled in your phone's system settings and the app has Location permission.
-   **Contacts missing (iOS):** Go to Settings > Privacy > Contacts > TapAlert and ensure **"All Contacts"** is checked.
-   **Contacts missing (Android):** Go to Settings > Apps > TapAlert > Permissions and ensure **"Contacts"** is allowed.

## 13. ⏳ Check-in Timer

The **Check-in Timer** is an "inactive" safety feature. It allows you to set a timer when starting a potentially risky activity (e.g., walking home alone, going on a hike).

1.  **Start the Timer:** Select a duration (from 5 minutes up to 24 hours) and an optional message.
2.  **The Countdown:** A persistent notification will show you the remaining time.
3.  **The Check-in:** You must return to the app and tap **"I'm OK (Reset)"** before the timer expires.
4.  **Automatic Alert:** If you *don't* reset the timer before it hits zero, TapAlert will automatically send your alert message and location to all recipients.

> [!TIP]
> This is perfect for "Dead Man's Switch" scenarios where you want an alert sent if you become incapacitated or lose access to your phone.
