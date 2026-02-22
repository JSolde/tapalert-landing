# TapAlert Email Redundancy Guide

## What is the Email Redundancy Feature?
Email redundancy in TapAlert allows the app to send emergency alerts and reporting messages to your designated contacts via email, in addition to or instead of SMS. 

## What is its Purpose?
The primary purpose of email redundancy is to ensure your message gets delivered even if primary SMS channels fail or are unavailable. 

*   **Secondary Delivery Path:** If you are connected to Wi-Fi but have no cellular service (and Wi-Fi Calling is disabled or unsupported), email acts as a perfect fallback.
*   **International Travel:** When traveling abroad where SMS might be extremely expensive or unreliable, you can rely purely on Wi-Fi and send alerts via email for free.
*   **Additional Peace of Mind:** Sending alerts via both SMS and Email simultaneously ensures that if an emergency contact misses a text, they might still see the email notification.

## How to Configure Email Redundancy
1. Open the TapAlert app and go to **Settings**.
2. Scroll to the **Email Alerts** section and toggle **Enable Email Alerts** ON.
3. Select your **Email Provider** from the preset buttons (Gmail, Outlook, Yahoo, iCloud) to auto-fill the SMTP Host and Port.
4. Enter your full **Email Address**.
5. Emter your **App Password** (See the section below on what this is and how to get one).
6. Tap "Save Settings" and use the "Test Email" button to ensure it is configured correctly.

---

## What is an App Password?
An **App Password** is a randomly generated passcode that gives a third-party app (like TapAlert) permission to access your email account to send messages on your behalf. 

**Why do I need one instead of my real password?**
Modern email providers block basic password logins to protect your account from hackers. An App Password bypasses Two-Factor Authentication (2FA) for that specific app *without* giving the app your actual account password. If you ever want to revoke TapAlert's access, you simply delete the App Password in your email settings, and your main account password remains safe and unchanged.

> **Note:** To generate an App Password, almost all email providers require you to have Two-Factor Authentication (2FA) enabled on your account first.

---

## How to Create an App Password

Here are clear, step-by-step instructions for the most common email providers.

### 1. Gmail (Google Account)
1. Go to your [Google Account management page](https://myaccount.google.com/) and log in.
2. On the left navigation panel, click **Security**.
3. Under the "How you sign in to Google" section, make sure **2-Step Verification** is turned **On**. (If it's Off, you must turn it on first).
4. Click on **2-Step Verification**. Scroll to the very bottom of the page and click on **App passwords**.
5. In the "Select app" dropdown, choose *Other (Custom name)* and type **TapAlert**.
6. Click **Generate**.
7. A yellow box will appear with a 16-character code. Copy this code and paste it into the "App Password" field in the TapAlert app (you do not need to include the spaces).
8. Click **Done**.

### 2. Hotmail / Outlook (Microsoft Account)
1. Go to the [Microsoft Account Security page](https://account.microsoft.com/security) and log in.
2. Click on **Advanced security options**.
3. Under the "Additional security" section, ensure **Two-step verification** is turned **On**.
4. Scroll down to the **App passwords** section.
5. Click **Create a new app password**.
6. A new screen will appear displaying your unique App Password. 
7. Copy this password and paste it into TapAlert, then click **Done**.

### 3. Yahoo Mail
1. Go to your [Yahoo Account Security page](https://login.yahoo.com/account/security) and log in.
2. Scroll down to the bottom of the page and click on **Generate and manage app passwords**.
3. A modal window will appear. Enter **TapAlert** as the app's name.
4. Click **Generate password**.
5. Copy the 16-character password displayed on the screen and paste it into TapAlert (omitting any spaces).
6. Click **Done**.

### 4. iCloud (Apple ID)
1. Go to [appleid.apple.com](https://appleid.apple.com/) and log in with your Apple ID.
2. In the **Sign-In and Security** section, click on **App-Specific Passwords**.
3. Click the **Generate an app-specific password** or the **Add (+)** button.
4. Enter **TapAlert** when prompted for an app name, and click Create.
5. You may be asked to enter your Apple ID password again to confirm.
6. A unique app-specific password will be generated and displayed (typically in the format `xxxx-xxxx-xxxx-xxxx`). 
7. Copy this entire password and paste it into TapAlert, then click **Done**.
