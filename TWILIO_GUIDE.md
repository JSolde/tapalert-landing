# Twilio Guide


## 💡 What is Twilio Configuration?

**What you'll be setting up:** Twilio configuration connects TapAlert to Twilio's cloud SMS service, allowing the app to send SMS messages even when your phone's cellular service is unavailable (but you have Wi-Fi).

**Why it matters:** By configuring Twilio credentials in the app, you enable a reliable fallback method for sending alerts. This is especially important during international travel, in buildings with poor cellular reception, or as a mandatory option for iPhone users who cannot send SMS directly from apps.

**Why Twilio?**
TapAlert uses Twilio because it's the most widely used SMS service in the world — trusted by companies like Uber and Airbnb. There are no monthly fees: you only pay a few cents per message actually sent. For an emergency app that sends alerts rarely, this means near-zero cost. Setup requires copying just three values into the app, and thousands of online tutorials exist if you need help.

**What you need:** A Twilio account with authentication credentials (Account SID and Auth Token), and either an alphanumeric sender ID or a purchased Twilio phone number.

- ✅ Trial account sends real SMS: A family member can test the entire setup with Twilio's free trial (sends to verified numbers) before spending any money. 

## 📖 About the Service

The option provided in TapAlert of using Twilio (cloud) as a mechanism to send SMS provides ultimate reliability in particular in international travel where roaming SMS often fails. Twilio can send SMS to over 180 countries. However, the method you can use varies by country. Some countries support Twilio phone numbers, others only support Alphanumeric Sender IDs, and some require specific local regulations to be met. 

### Why use Twilio on Android? (Smart Redundancy)
Even if you have a SIM card, setting up Twilio is highly recommended for **Redundancy**:
- **Scenario:** You are in a building with Wi-Fi but **zero cellular signal**.
- **Result:** Direct SMS fails.
- **Solution:** TapAlert will automatically switch to Twilio and send the alert via Wi-Fi. 

Please note that to use this feature, which is mandatory for iPhone users, you'll need to have a Twilio account ID. The cost of sending messages will be the same as if you were doing it manually from Twilio. No extra costs will be added by the app. 

### Twilio Sender Options

You can choose between 2 options to send SMS's with Twilio:

**OPTION A: Use Alphanumeric Sender ID (Recommended for Europe)**
- ✅ **Benefit:** No need to buy a phone number (Save monthly costs! depending on the number of messages you send).
- ✅ **Benefit:** Recipients see a name (e.g., "TapAlert" or your name) instead of a random number.
- ⚠️ **Note:** One-way only (no replies) and not supported in some countries (like USA).
- [Learn more about Alphanumeric Sender ID](https://help.twilio.com/articles/223181348-Alphanumeric-Sender-ID-for-Twilio-Programmable-SMS)

**OPTION B: Buy a Twilio Phone Number**
- ✅ **Benefit:** Works worldwide (including USA).
- ⚠️ **Cost:** Requires purchasing a number (approx. $1/mo).

## 💰 Potential Hidden Costs & Pricing Factors

While Twilio generally offers low-cost messaging, the final price per SMS can be higher than the base rate due to several factors. It is important to review these to avoid unexpected charges.

### 1. Destination Country Pricing
Twilio pricing varies significantly depending on the **destination country** of the message.
- The lowest advertised rates (e.g., around $0.0075) often apply to messages sent to the **USA**.
- Sending to other countries (e.g., in Europe or Asia) can be significantly more expensive.
- **Action:** Always check the specific pricing for the country you intend to send alerts to.

### 2. Carrier & Regulatory Fees
In addition to Twilio's base price, many countries and local carriers impose **surcharges** or "pass-through fees."
- These are unavoidable fees added by the telecom providers, not Twilio.
- They can sometimes double the effective cost per message in certain regions.

### 3. Message Segmentation (Long Messages)
SMS billing is based on "segments."
- A standard SMS segment is **160 characters**. 
- If your message exceeds this limit, it is split into multiple parts, and you are charged for **each segment**. TapAlert SMS messages with **Location info** exceed this limit. To minimize Twilio costs, avoid enabling **Location Settings** (or just disable the **Include Address** option in the settings). You can check the actual message length of each sent message in the **Alert History** screen.
- **Important:** Using emojis or special non-Latin characters (Unicode) reduces the segment limit to just **70 characters**, potentially tripling the cost of a single alert. 

### 4. Phone Number Rental Fees
If you choose to buy a phone number (Option B above):
- You pay a **monthly rental fee** for the number itself (typically $1.00 - $4.00 USD/month depending on the country).
- This is a recurring fixed cost, regardless of whether you send any messages.
- Some specific numbers (like Spanish mobile numbers capable of SMS) are "Exclusive" and require a manual request process and higher fees.

### 5. Currency Conversion & Taxes
- Your final bill may include local taxes (like VAT).
- If your card is in a different currency than your Twilio account, your bank or Twilio may apply currency conversion fees.

💡 **Recommendation:** We strongly advise checking the [Official Twilio Pricing Page](https://www.twilio.com/sms/pricing) and selecting your target country to see the full breakdown of costs.


## ⚙️ Configuration Steps

To set up Twilio in the app, follow these steps:

### 1️⃣ Step 1: Get your Twilio Credentials
1.  Create an account at [Twilio.com](https://www.twilio.com/).
2.  Go to the [Twilio Console](https://console.twilio.com/) to find your **Account SID** and **Auth Token**.
3.  **Choose your sender method** (Option A or B above).

### 2️⃣ Step 2: Enter Credentials in the App
1.  Open the App **Settings**.
2.  Enable the **"Use Twilio"** switch.
3.  Enter your **Account SID** and **Auth Token**.
4.  **Configure the sender:**
    - **If using Option A (Name):** Enable **"Use Alphanumeric Sender ID"**, then type your desired name (max 11 chars) in the **Sender Name** field.
    - **If using Option B (Number):** Leave "Use Alphanumeric Sender ID" **OFF** and enter your purchased Twilio number in the **Twilio Phone Number** field.

### 3️⃣ Step 3: Summary of Alphanumeric Sender ID
- **What is it?** It lets you use a name (like "MyHomeAlert") instead of a number.
- **Trust:** Recipients see your name immediately, which ensures your alert stands out.
- **No Replies:** Note that recipients cannot reply to a name.


