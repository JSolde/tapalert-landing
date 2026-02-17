# TapAlert Troubleshooting Guide

This guide covers common issues and solutions for TapAlert on both Android and iOS.

---

## 1. SMS Sending Issues

### 1.1 Direct SMS Not Sending (Android)

**Symptom:** You tap "Send Alert" but the SMS fails. The alert history shows an error for one or more recipients.

**Possible causes and solutions:**

- **No cellular signal:** Check the status bar on your phone. If you have no bars, move to an area with better coverage. The Status page in the app shows your current cellular status.
- **No SIM card inserted:** Direct SMS requires a working SIM card. Go to the Status page to check your SIM status.
- **SMS permission denied:** Go to your phone's **Settings > Apps > TapAlert > Permissions** and ensure **SMS** is set to "Allow".
- **Carrier credit exhausted:** If you are on a prepaid plan, ensure you have sufficient credit to send SMS messages. Each recipient costs one SMS.
- **OEM permission blocking (Vivo, Xiaomi, Oppo, etc.):** Some phone manufacturers have additional security layers that block SMS permissions, especially for sideloaded apps. If you see a message like "App was denied access to SMS", go to your phone's security settings and manually approve the permission. Installing from the Google Play Store avoids this issue.
- **Invalid phone number format:** Ensure recipient numbers are in international format with country code (e.g., `+34600123456`). Go to **Recipients** and verify each number.
- **Message too long:** SMS messages over 160 characters are split into multiple segments. Very long messages with location data might fail on some carriers. Try shortening your custom message.

### 1.2 Twilio SMS Not Sending

**Symptom:** Alert fails with a Twilio error message. The error details may include HTTP response codes or Twilio error messages.

**Possible causes and solutions:**

- **No internet connection:** Twilio requires Wi-Fi or cellular data. Check that you have an active internet connection.
- **Wrong credentials:** Go to **Settings > Twilio** and verify your Account SID, Auth Token, and Twilio phone number are correct. Use the **Test** button to verify.
- **Twilio trial account limitations:** Trial accounts can only send to verified phone numbers. Add recipient numbers to your Twilio verified list at [twilio.com/console](https://twilio.com/console).
- **Twilio balance depleted:** Check your Twilio account balance. Top up your account if the balance is zero.
- **Invalid "From" number:** Your Twilio phone number must be an active number in your Twilio account. If using a Sender Name (alphanumeric ID), some countries don't support it or require pre-registration.
- **Recipient number not in E.164 format:** Twilio requires numbers in full international format (e.g., `+14155551234`). Verify your recipients list.
- **Credential fields have extra spaces:** When copying credentials from Twilio console, invisible whitespace characters may be included. Delete the content and retype it manually.
- **After changing credentials, test again:** If you change any Twilio credential, the previous test result is invalidated. Always re-test after making changes.

### 1.3 iOS SMS Composer Issues

**Symptom:** On iPhone, the SMS composer opens but the message doesn't actually get delivered.

**Possible causes and solutions:**

- **No cellular signal:** The iOS Messages app needs cellular network to send SMS. If you only have Wi-Fi, the message may be queued but not delivered. The app will show an orange warning "SMS Sent - Please Verify" if it detects no cellular after sending.
- **WiFi Calling may or may not work:** When cellular is off but WiFi is on, the app allows you to try the SMS composer because WiFi Calling might route the SMS. However, delivery is uncertain. Check your Messages app to confirm delivery.
- **User cancelled the composer:** If you tap Cancel in the SMS composer, the alert is cancelled entirely. This is by design.
- **Invalid recipient number:** If the number is wrong, iOS will silently queue the message and it will fail. Check your Messages app for failed messages (they appear with a red exclamation mark).

### 1.4 Smart Redundancy Not Working (Android)

**Symptom:** The primary SMS method fails but the fallback doesn't kick in.

**Possible causes and solutions:**

- **Twilio not configured:** For Direct SMS to fall back to Twilio, you must have Twilio configured in Settings. Without it, there is no fallback.
- **Both methods failing:** If Direct SMS fails because there's no signal AND Twilio fails because there's no internet, no fallback is possible. Consider configuring Email Redundancy for these scenarios.

---

## 2. Email Redundancy Issues

### 2.1 Email Test Fails

**Symptom:** Tapping "Test Connection" in Email settings shows an error.

**Possible causes and solutions:**

- **Wrong SMTP settings:** Double-check the host and port. Common configurations:
  - Gmail: `smtp.gmail.com`, port `587`
  - Outlook/Hotmail: `smtp-mail.outlook.com`, port `587`
  - Yahoo: `smtp.mail.yahoo.com`, port `587`
  - iCloud: `smtp.mail.me.com`, port `587`
- **Using your regular password instead of an App Password:** Most email providers require an App Password when 2-factor authentication is enabled. Generate one in your email provider's security settings. See the User Guide Chapter 6 for step-by-step instructions.
- **App Password from wrong provider:** A Gmail App Password only works with Gmail SMTP. An Outlook App Password only works with Outlook SMTP. Make sure they match.
- **2-Factor Authentication not enabled:** Some providers (like Gmail) require 2FA to be enabled before you can generate App Passwords. Enable 2FA first, then generate the App Password.
- **No internet connection:** Email sending requires Wi-Fi or cellular data.
- **Port blocked by network:** Some corporate or hotel Wi-Fi networks block SMTP ports. Try a different network.
- **Wrong port/SSL combination:** Port 465 uses implicit SSL. Port 587 uses STARTTLS. The app handles this automatically, but if you're using a custom port, ensure it matches your provider's requirements.

### 2.2 Email Sends But Recipients Don't Receive It

**Possible causes and solutions:**

- **Check spam/junk folder:** Alert emails may be filtered as spam, especially if sent from a new email address.
- **No email address on recipient:** Email is only sent to recipients that have an email address saved. Go to **Recipients**, edit each contact, and add their email.
- **Email is a backup channel:** Email redundancy runs in parallel with SMS. It's a "fire and forget" backup. Check the snackbar notification at the bottom of the screen to see if it succeeded or failed.

---

## 3. Location Issues

### 3.1 Location Not Included in Alert

**Symptom:** The alert message is sent but doesn't include GPS coordinates or a map link.

**Possible causes and solutions:**

- **Location permission denied:** Go to your phone's **Settings > Apps > TapAlert > Permissions** and ensure **Location** is set to "Allow" or "While Using the App".
- **Location permanently denied:** If you previously selected "Don't ask again", you must manually go to your phone settings to re-enable it. On iOS: **Settings > Privacy & Security > Location Services > TapAlert**.
- **GPS/Location services disabled:** Make sure your phone's Location/GPS is turned on in the system quick settings panel.
- **Location disabled in app settings:** Check **Settings** in the app and ensure **Include Location** is toggled ON.
- **Poor GPS reception:** Indoors or in urban canyons, GPS may time out (10-second limit). The alert will still be sent without location rather than failing entirely.

### 3.2 Address Not Included (Only Coordinates)

**Symptom:** The alert includes coordinates and a map link, but no street address.

**Possible causes and solutions:**

- **Address resolution timed out:** Address lookup has a 5-second timeout. If the geocoding service is slow, only coordinates will be included. This is normal behavior to avoid delaying the alert.
- **No internet for geocoding:** Address resolution requires an internet connection. If you're sending via Direct SMS without data, coordinates will be included but not the address.
- **Include Address disabled:** Check **Settings** and ensure **Include Address** is toggled ON.

---

## 4. Connectivity and Status Issues

### 4.1 Status Screen Shows Wrong Connectivity

**Symptom:** The status page shows red (no cellular) even though your phone has signal, or vice versa.

**Possible causes and solutions:**

- **Delay after airplane mode toggle:** After turning airplane mode off, it may take a few seconds for the cellular radio to reconnect. The status page refreshes every 3 seconds automatically. Wait 5-10 seconds.
- **iOS cellular detection limitations:** On iOS, the app uses `CTTelephonyNetworkInfo` to detect cellular radio. In rare cases, this API may report stale information. Leave the status page and return to force a fresh check.
- **Pull to refresh:** On the Status page, wait a few moments for the automatic refresh cycle to pick up the change.

### 4.2 Shield Icon Color Meaning

The shield icon on the home screen indicates your alert readiness:

- **Green:** SMS delivery is reliable. You have cellular signal (for Direct SMS or iOS Messages) or Twilio is configured with internet access.
- **Orange:** Uncertain delivery. You have WiFi but no cellular and no Twilio. WiFi Calling might enable SMS but this cannot be verified by the app. Or you're in email-only fallback mode.
- **Red:** No connectivity at all. Alerts cannot be sent. Both cellular and WiFi are off.

### 4.3 Buttons Disabled / "Service Unavailable"

**Symptom:** The SOS and alert buttons are greyed out or show a service unavailable message.

**Possible causes and solutions:**

- **No connectivity:** The app disables alert buttons when there is no cellular AND no WiFi connection. Restore at least one connection.
- **No recipients configured:** You need at least one recipient to send an alert. Go to **Recipients** and add phone numbers.

---

## 5. Check-in Timer (Dead Man's Switch) Issues

### 5.1 Timer Doesn't Fire an Alert

**Symptom:** The timer reaches zero but no alert is sent.

**Possible causes and solutions:**

- **App was force-closed:** If you swipe the app away from the recent apps list, the in-app timer is killed. On Android, a foreground service keeps the timer alive. On iOS, a local notification is scheduled. You must tap the notification to trigger the alert when the app isn't in the foreground.
- **Notifications disabled:** The timer expiration notification requires notification permission. Go to your phone's **Settings > Apps > TapAlert > Notifications** and ensure they are enabled.
- **Battery optimization killing the app (Android):** Some phones aggressively kill background apps. Go to **Settings > Battery > TapAlert** and select "Unrestricted" or "Don't optimize". The app provides a shortcut in Settings to disable battery optimization.
- **iOS notification not tapped:** On iOS, when the timer expires while the app is in the background, a notification is shown. You must tap it to open the app and trigger the actual alert sending. iOS does not allow apps to send SMS from the background.
- **No connectivity when timer expires:** If you lose all connectivity before the timer expires, the alert cannot be sent. The app will attempt to send when it can.

### 5.2 Timer Resets Unexpectedly

**Symptom:** The timer seems to restart or lose its countdown.

**Possible causes and solutions:**

- **App went to background and resumed:** The timer state is synchronized between the Dart layer and native platform. When the app resumes, it recovers the timer state from the native side. The remaining time should be accurate.
- **Phone was restarted:** Restarting the phone cancels all pending notifications and timers. You would need to start the timer again.

### 5.3 Timer Warning About SMS Unavailability

**Symptom:** When starting the timer, a warning appears that SMS is unavailable.

**This is informational:** The app warns you if SMS is currently not possible (no cellular, no Twilio configured). The timer will still run, but when it expires, it may only be able to send via email (if configured) or may fail entirely. For best results, ensure you have cellular signal or Twilio configured before relying on the timer.

---

## 6. Voice-to-Text Issues

### 6.1 Voice Recognition Not Working

**Symptom:** You tap the microphone button but nothing happens or it doesn't recognize your speech.

**Possible causes and solutions:**

- **Microphone permission denied:** Go to your phone's **Settings > Apps > TapAlert > Permissions** and ensure **Microphone** is allowed.
- **Speech recognition permission denied (iOS):** iOS requires a separate Speech Recognition permission. Go to **Settings > Privacy & Security > Speech Recognition > TapAlert** and enable it.
- **No internet connection:** Some speech recognition engines require an internet connection for processing. Ensure you have WiFi or cellular data.
- **Speaking too softly or too far from the microphone:** Speak clearly and hold the phone within arm's length.
- **Background noise:** Excessive background noise can prevent accurate recognition. Move to a quieter environment.
- **Wrong language:** The voice recognition uses the app's current language setting. If you're speaking a different language than the app is set to, recognition will be poor. Change the app language in **Settings > Language**.
- **Timeout:** Voice recognition has a 60-second listening window and stops after 5 seconds of silence. If you pause too long, it may stop listening.

### 6.2 Voice Text Sends Immediately

**This is by design:** In Panic Mode, voice-recorded messages are sent immediately after recording completes. In Report Mode, the voice transcription is saved to Tab 4 and the alert is triggered automatically. If you want to review before sending, use Report Mode and edit the text in Tab 4 before pressing "Send Alert".

---

## 7. Contacts and Recipients Issues

### 7.1 Cannot See Contacts (iOS)

**Symptom:** The contact picker is empty or shows only a few contacts.

**Solution:** During the initial permissions request, if you chose **"Select Contacts..."** (Limited Access), the app can only see the contacts you specifically selected. To fix this:
1. Go to **iPhone Settings > Privacy & Security > Contacts > TapAlert**.
2. Change to **"All Contacts"**.

### 7.2 Cannot See Contacts (Android)

**Symptom:** The contact picker shows no contacts.

**Solution:** Go to **Settings > Apps > TapAlert > Permissions** and ensure **Contacts** is set to "Allow".

### 7.3 Phone Number Format Issues

**Symptom:** Messages fail because of invalid phone numbers.

**Possible causes and solutions:**

- **Missing country code:** All numbers should include the country code with a `+` prefix (e.g., `+1` for US, `+44` for UK, `+34` for Spain).
- **Wrong region setting:** Go to **Settings > Region** and set your correct region. This helps the app auto-format local numbers.
- **Special characters in number:** Remove spaces, dashes, or parentheses from phone numbers. Only digits and the leading `+` should remain.

### 7.4 Recipient Limit Reached

**Symptom:** You can't add more than 6 recipients.

**Solution:** The free tier allows up to 6 recipients. To add unlimited recipients, purchase the Premium upgrade from **Settings > Upgrade** (one-time purchase, no subscription).

---

## 8. In-App Purchase Issues

### 8.1 Purchase Button Not Working

**Symptom:** The upgrade screen shows "Product not available" or the purchase button doesn't respond.

**Possible causes and solutions:**

- **No internet connection:** In-app purchases require an active internet connection.
- **App Store / Play Store not signed in:** Ensure you are signed into your Apple ID (iOS) or Google account (Android).
- **Parental controls or restrictions:** Check if purchase restrictions are enabled on your device.
- **Store outage:** Occasionally, the App Store or Play Store may have temporary issues. Try again later.

### 8.2 Purchased But Still Shows Free

**Symptom:** You completed the purchase but the app still limits you to 6 recipients.

**Possible causes and solutions:**

- **Tap "Restore Purchases":** In the Upgrade screen, tap the restore button. This re-validates your purchase with the store.
- **Different account:** Ensure you're signed in with the same Apple ID or Google account you used for the original purchase.
- **App reinstall:** If you reinstalled the app, you need to restore purchases. The purchase is tied to your store account, not the device.

---

## 9. Widget Issues (Android Only)

### 9.1 Widget Not Appearing

**Symptom:** You can't find the TapAlert widget in the widget picker.

**Possible causes and solutions:**

- **App not installed from Play Store:** Some launchers only show widgets for Play Store-installed apps. Try adding the widget from **Settings > Widget > Add** within the app instead of from the home screen long-press menu.
- **Device doesn't support widget pinning:** Some older Android devices (below Android 8.0) may not support programmatic widget pinning. Try adding the widget manually: long-press your home screen, select "Widgets", and find TapAlert.

### 9.2 Widget Tap Doesn't Work

**Symptom:** Tapping the widget opens the app but doesn't start the countdown.

**Possible causes and solutions:**

- **App was updated:** After an app update, widgets may need to be re-added. Remove the old widget and add a new one.
- **Battery optimization:** Aggressive battery optimization may prevent the widget from launching the app correctly. Disable battery optimization for TapAlert.

---

## 10. Notification Issues

### 10.1 No Sound After Sending Alert

**Symptom:** The alert is sent successfully but you don't hear the confirmation sound.

**Possible causes and solutions:**

- **Phone is on silent/vibrate:** The notification sound respects your phone's volume settings. Increase the media volume.
- **Notification sound set to "None":** Go to **Settings > Notification Sound** and select a sound.
- **Do Not Disturb enabled:** DND may suppress sounds. Add TapAlert as an exception in your DND settings.

### 10.2 Recipients Not Noticing the Alert SMS

**Symptom:** You sent the alert successfully but your recipients didn't notice it on their phones.

**Solutions for recipients:**

- **iPhone recipients:** Open the contact entry for your TapAlert number, tap **Edit > Text Tone**, and enable **Emergency Bypass**. This makes the SMS audible even in Silent or Do Not Disturb mode.
- **Android recipients:** In the Messages app, open the conversation, tap **Details > Notifications**, set priority to **"High"** or **"Urgent"**, and enable **"Ignore Do Not Disturb"**.
- **Twilio sender number:** If using Twilio, recipients receive messages from your Twilio number (or sender name). They must add this number to their contacts for custom notification rules to work.

---

## 11. App Behavior Issues

### 11.1 Alert Fires Immediately on App Open

**Symptom:** Every time you open the app, the countdown starts automatically.

**Cause:** You have **Auto-Start on Launch** enabled. This is designed for use with physical panic buttons or quick-launch shortcuts.

**Solution:** Go to **Settings** and disable **Auto-Start on Launch**.

### 11.2 Accidental Alert Triggers

**Symptom:** You accidentally send alerts too easily.

**Solution:** Change the trigger method to **Press & Hold** in **Settings > Trigger Method**. This requires holding the button for 5 seconds before the countdown begins.

### 11.3 App Closes After Sending

**Symptom:** The app closes automatically after an alert is sent.

**Cause:** This happens when the app is launched from a widget or with Auto-Start on Launch enabled. It's by design to return you to the home screen after the alert is sent.

**Solution:** If you opened the app normally (not from a widget), this should not happen. If it persists, check that Auto-Start on Launch is disabled.

### 11.4 Countdown Timer Too Short / Too Long

**Solution:** Adjust the countdown duration in **Settings > Countdown Duration**. You can set it from 0 seconds (immediate send) up to 30 seconds. A longer countdown gives you more time to cancel accidental alerts.

---

## 12. iOS-Specific Issues

### 12.1 "Twilio Not Configured" Error

**Symptom:** On iOS, you see an error saying Twilio must be configured.

**Explanation:** iOS does not allow apps to send SMS programmatically. You have two options:
1. **Configure Twilio** (recommended): Set up a Twilio account and enter credentials in **Settings > Twilio**. This allows automatic, silent SMS sending over internet.
2. **Use iOS Messages (Manual):** In **Settings > Twilio > iOS SMS Method**, select "iOS Messages". This opens the native Messages composer where you tap Send manually.

### 12.2 iOS SMS Method Choice

**When to choose Twilio (Automatic):**
- You want fully automatic sending (no manual interaction needed).
- You have reliable internet (Wi-Fi or cellular data).
- You are comfortable with a small per-SMS cost from Twilio.

**When to choose iOS Messages (Manual):**
- You don't want to set up a Twilio account.
- You have cellular service and don't mind tapping Send in the composer.
- You want SMS sent from your personal phone number.

### 12.3 Orange "SMS Sent - Please Verify" Warning

**Symptom:** After sending via iOS Messages, you see an orange warning instead of a green success.

**Explanation:** The app detected that your phone had no cellular signal when the SMS was submitted to the Messages app. The message was queued but may not have been delivered. Open your **Messages** app and check if the message shows a red exclamation mark (failed) or was sent successfully. If WiFi Calling is active, the message may have been delivered despite no cellular signal showing in the app.

---

## 13. Android-Specific Issues

### 13.1 Battery Optimization Killing Background Features

**Symptom:** The check-in timer stops working, or the app gets killed in the background.

**Solution:**
1. Go to **Settings** in the app and tap the battery optimization option.
2. In your phone's system settings, find **Battery > TapAlert** and set to **"Unrestricted"** or **"No restrictions"**.
3. On some manufacturers (Xiaomi, Huawei, Samsung), there are additional battery settings:
   - **Xiaomi:** Settings > Battery > App battery saver > TapAlert > No restrictions
   - **Huawei:** Settings > Battery > App launch > TapAlert > Manage manually > Allow all
   - **Samsung:** Settings > Battery > Background usage limits > Never sleeping apps > Add TapAlert

### 13.2 Foreground Service Notification

**Symptom:** A persistent notification appears when the check-in timer is active.

**Explanation:** This is required by Android for background services. The notification shows the timer status and cannot be dismissed while the timer is running. It ensures the system doesn't kill the timer process. The notification disappears when you stop or reset the timer.

---

## 14. General Tips

### Before Relying on TapAlert in an Emergency

1. **Send a test alert** to yourself or a trusted contact to verify everything works.
2. **Test the Twilio connection** using the Test button in Settings if you use Twilio.
3. **Test the email connection** using the Test button in Email Settings if you use email redundancy.
4. **Check the Status page** to see a summary of your connectivity and configured methods.
5. **Ensure permissions are granted** for SMS (Android), Location, Microphone, Contacts, and Notifications.
6. **Verify recipient phone numbers** are in the correct international format with country code.

### If Nothing Works

1. **Restart the app:** Close TapAlert completely and reopen it.
2. **Restart your phone:** This resets all network connections and system services.
3. **Check for app updates:** Ensure you have the latest version from the App Store or Play Store.
4. **Reinstall the app:** As a last resort, uninstall and reinstall. You will need to reconfigure your settings and recipients. If you purchased Premium, use "Restore Purchases" to recover it.
5. **Check the Help section:** The app includes detailed guides accessible from the menu (three dots icon) > Help.
