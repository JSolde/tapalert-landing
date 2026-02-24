import os

os.makedirs('src', exist_ok=True)
html_files = [f for f in os.listdir('.') if f.endswith('.html') and os.path.isfile(f)]

for file in html_files:
    if file == 'index.html':
        continue 
    with open(file, 'r') as f:
        content = f.read()
    with open(f'src/{file}', 'w') as f:
        f.write(content)

print("Copied all HTML files to src/")

with open('index.html', 'r') as f:
    text = f.read()

subs = [
    # Nav
    ("Install", "{{ nav_download }}"),
    ("Contact", "{{ nav_contact }}"),
    ("Philosophy", "{{ nav_philosophy }}"),
    ("Troubleshooting", "{{ nav_troubleshooting }}"),
    
    # Hero
    ("Real. Urgent. Reliable.", "{{ hero_tagline }}"),
    ("Redefining", "{{ hero_title }}"),
    ("Emergency Alerting", "{{ hero_title2 }}"),
    ("No Subscription", "{{ hero_title3 }}"),
    ("An Open Source panic button for critical situations. Fast. Simple. Reliable.", "{{ hero_subtitle }}"),
    ("Bypass Silent / Do Not Disturb filters to wake your contacts up, when it matters. Works even without Internet Access.", "{{ hero_sub_text }}"),
    ("Protect your older adults and loved ones with one tap.", "{{ hero_protect }}"),
    ("subscriptions, no tracking, no accounts required, no ads.", "{{ hero_no_subs }}"),
    ("Get TapAlert", "{{ btn_get }}"),
    ("Source Code", "{{ btn_source }}"),
    
    # Use cases
    ("Use Cases", "{{ uc_title }}"),
    ("Older Adults", "{{ uc_1_title }}"),
    ("& Caregivers", "{{ uc_caregivers }}"),
    ("A simple panic button that bypasses 'Silent' or 'Do Not Disturb' to alert family instantly - even in dead zones using cellular backup.", "{{ uc_desc1 }}"),
    ("A discreet way to send immediate alerts with real-time location and audio to a predefined emergency contact list, without needing to make a phone call.", "{{ uc_desc2 }}"),
    ("Enable the Quick Settings tile or a launcher shortcut for instant access to coordinate help and share location when separated or in need of immediate assistance.", "{{ uc_desc3 }}"),
    
    # Tables & headings
    ("Alerting", "{{ table_r1c1 }}"),
    ("Privacy", "{{ table_r2c1 }}"),
    ("Feature", "{{ android_table_th1 }}"),
    ("Android", "{{ android_table_th2 }}"),
    ("iOS", "{{ android_table_th3 }}"),
    
    # Features
    ("Offline Reliability", "{{ feat_1_title }}"),
    ("When the internet goes down, TapAlert steps up. Send critical alerts via 4G/5G cellular networks using Direct SMS, ensuring your message gets through even during network outages, natural disasters, or in areas with poor data coverage.", "{{ feat_1_desc }}"),
    ("Location Tracking", "{{ feat_2_title }}"),
    ("If enabled, your real-time GPS coordinates are automatically embedded in every alert message. Help your emergency contacts find you faster with pinpoint accuracy.", "{{ feat_2_desc }}"),
    ("Audio Capture", "{{ feat_3_title }}"),
    ("Not just text. TapAlert can surreptitiously record a 10s audio clip of your surroundings and include it in your alert, providing crucial context to your emergency contacts.", "{{ feat_3_desc }}"),
    ("Multiple Delivery Paths", "{{ feat_4_title }}"),
    ("Why rely on one method? Configure primary and failback options: Direct SMS, Twilio integration (for data-only situations or SIM failure), and Email fallbacks. If one fails, TapAlert automatically tries the next.", "{{ feat_4_desc }}"),
    ("Custom Triggers", "{{ feat_5_title }}"),
    ("Launch an alert your way. Map TapAlert to your Android Quick Settings tile, or long-press the app icon for a permanent launcher shortcut to trigger an SOS.", "{{ feat_5_desc }}"),
    ("Senior & Accessible", "{{ feat_6_title }}"),
    ("Designed with a massive, high-contrast SOS button. Fully compatible with screen readers (TalkBack/VoiceOver), respects system text scaling, and requires zero technical knowledge to operate once set up. See the Accessiblity Guide.", "{{ feat_6_desc }}"),
    ("Multi-Language", "{{ feat_lang_title }}"),
    ("Supports multiple languages for broader accessibility. Use", "{{ feat_lang_p }}"),
    ("or other translation platforms to propose new languages.", "{{ feat_lang_desc }}"),
    ("Geo-links", "{{ feat_location_title }}"),
    ("Location links are universally formatted for Google Maps, ensuring they open seamlessly on any device your recipient uses.", "{{ feat_location_desc }}"),
    ("Custom Warning", "{{ feat_quick_title }}"),
    ("Set a custom warning message for your contacts. This lets them know it's a real emergency and not spam.", "{{ feat_quick_desc }}"),
    
    # Philosphy section
    (">Our<", ">{{ phil_h2 }}<"),
    ("& Design Principles", "{{ phil_h2_suffix }}"),
    (">First<", ">{{ phil_priv_first }}<"),
    ("to use the app", "{{ phil_priv_li1 }}"),
    ("built-in", "{{ phil_priv_li2 }}"),
    ("or hidden fees", "{{ phil_priv_li4 }}"),
    ("Open Source", "{{ phil_priv_li5 }}"),
    ("so anyone can verify the code", "{{ phil_priv_li6 }}"),
    ("accounts required", "{{ phil_priv_no_accounts }}"),
    ("tracking or analytics", "{{ phil_priv_no_tracking }}"),
    (">ads<", ">{{ phil_priv_no_ads }}<"),
    (">subscriptions<", ">{{ phil_priv_no_subs }}<"),
    
    ("SMS-First Architecture", "{{ phil_sms_title }}"),
    ("Internet connections fail. Wi-Fi drops. That's why TapAlert prioritizes SMS:", "{{ phil_sms_desc1 }}"),
    ("Works on the cellular network when data/Wi-Fi is down", "{{ phil_sms_li1 }}"),
    ("Bypasses internet censorship and network congestion", "{{ phil_sms_li2 }}"),
    ("app installation required on the recipient's end", "{{ phil_no_install }}"),
    ("Guaranteed delivery to any mobile phone, anywhere", "{{ phil_sms_li3 }}"),
    
    ("Smart Redundancy", "{{ phil_red_title }}"),
    ("When you have a data or Wi-Fi connection, the app will try to send an email via", "{{ phil_wifi_1 }}"),
    ("(if configured). This provides a secondary delivery path when the primary SMS channel is unavailable.", "{{ phil_red_p1 }}"),
    ("Likewise, in a situation with only cellular service (no Wi-Fi and no internet), if the", "{{ phil_red_p2 }}"),
    ("fails for some reason (defective or no SIM,...)", "{{ phil_red_p3 }}"),
    ("(if configured) will act as", "{{ phil_red_p4 }}"),
    ("as it can also use the cellular network (via 4G/5G) to send the message as a last resort.", "{{ phil_red_p5 }}"),
    
    ("High contrast UI with a single massive ", "{{ phil_sen_li1 }}"),
    (" button", "{{ phil_sen_li2 }}"),
    ("Support for system-wide font scaling", "{{ phil_sen_li3 }}"),
    ("Can be triggered via ", "{{ phil_sen_li4 }}"),
    ("Quick Settings tile", "{{ phil_sen_li5 }}"),
    ("No complex menus or onboarding flows", "{{ phil_sen_li6 }}"),
    ("Available in 10+ languages (and growing)", "{{ phil_sen_li7 }}"),
    ("Detailed ", "{{ phil_sen_li8 }}"),
    ("Screen reader support — fully compatible with TalkBack", "{{ phil_screen_reader }}"),
    ("and VoiceOver", "{{ phil_screen_reader2 }}"),
    ("; buttons are labelled and outcomes are announced aloud", "{{ phil_screen_reader3 }}"),

    # Comparison table
    ("Emergency Alerts", "{{ plat_cmp_1 }}"),
    ("(via ", "{{ plat_cmp_2 }}"),
    (", background execution)", "{{ plat_cmp_3 }}"),
    ("Twilio Integration", "{{ plat_cmp_4 }}"),
    ("(Requires background SMS sending which", "{{ plat_cmp_5 }}"),
    ("blocks)", "{{ plat_cmp_6 }}"),
    ("Email Trigger", "{{ plat_cmp_7 }}"),
    ("API)", "{{ plat_cmp_8 }}"),
    ("Automatic Send (Timer)", "{{ plat_timer_1 }}"),
    ("(Sends automatically when timer ends)", "{{ plat_timer_2 }}"),
    ("integration, the timer acts as a reminder before triggering the compose sheet.", "{{ plat_timer_4 }}"),
    (">Fallback<", ">{{ term_fallback }}<"),
    (">Direct SMS<", ">{{ term_direct_sms }}<"),
    ("Failback", "{{ term_failback }}"),
    
    ("iOS Messages", "{{ term_ios_messages }}"),
    ("requires user interaction)", "{{ plat_requires_interaction }}"),
    ("user interaction needed", "{{ plat_no_interaction }}"),
    ("always requires tapping Send", "{{ plat_ios_always_tap }}"),
    ("when internet available)", "{{ plat_when_internet }}"),
    (">Limitations<", ">{{ plat_limitations }}<"),
    ("(compared to", "{{ plat_compared_to }}"),
    ("preference requires the user to physically tap Send", "{{ plat_ios_tap_send }}"),
    (">Advantages<", ">{{ plat_advantages }}<"),
    
    ("Apple prohibits background SMS sending to prevent spam. All text messages MUST be manually confirmed by the user via the native Messages app.", "{{ ios_lim1 }}"),
    ("Because background requests are blocked, we cannot implement the ", "{{ ios_lim2 }}"),
    ("Without background SMS capabilities, the countdown timer can only open the compose menu, not send the message automatically. Wait for the timer to finish, then hit the Send button.", "{{ ios_lim3 }}"),
    
    ("Tap once, and the alert is sent in the background immediately.", "{{ android_adv1 }}"),
    ("No ", "{{ android_adv2 }}"),
    ("integration provides a rock-solid secondary delivery path.", "{{ android_adv3 }}"),
    ("The countdown timer natively triggers the alert when it hits zero.", "{{ android_adv4 }}"),
    (" Fallback logic automatically switches to cellular networks if Wi-Fi / Data fails.", "{{ android_adv5 }}"),
    ("Why we support both", "{{ both_plat_title }}"),
    (", TapAlert still provides a unified, cross-platform interface for configuring contacts and standardizing your emergency message format.", "{{ both_plat2 }}"),
    ("If Apple ever relaxes their background SMS restrictions, TapAlert will implement the same seamless experience available on Android immediately.", "{{ both_plat3 }}"),
    ("Despite the limitations and lack of", "{{ plat_same_1 }}"),

    # Pricing
    ("Simple, Honest", "{{ pricing_h2 }}"),
    (">Pricing<", ">{{ footer_price }}<"),
    ("No subscriptions. No hidden fees. Period.", "{{ price_pro_sub }}"),
    (">Free<", ">{{ price_free_title }}<"),
    (">Forever<", ">{{ price_free_note }}<"),
    ("Basic offline SOS alerts", "{{ price_free_d1 }}"),
    ("5 Emergency Contacts", "{{ price_free_d3 }}"),
    ("Countdown Timer", "{{ price_free_d4 }}"),
    ("Email fallback", "{{ price_free_d5 }}"),
    (">Pro<", ">{{ price_pro_title }}<"),
    ("One-time payment", "{{ price_pro_note }}"),
    ("Twilio integration (Global SMS)", "{{ price_pro_d1 }}"),
    ("Live Location Tracking", "{{ price_pro_d2 }}"),
    ("10s Audio Recording", "{{ price_pro_d3 }}"),
    ("Unlimited Contacts", "{{ price_pro_d4 }}"),
    ("Desktop Shortcut execution", "{{ price_pro_d5 }}"),
    (">All<", ">{{ price_all }}<"),
    (">features<", ">{{ price_features }}<"),
    
    ("Wait, what about Twilio fees?", "{{ twilio_fees_title }}"),
    ("is a 3rd party service. Your $4.99 goes to TapAlert development. If you choose to configure", "{{ twilio_fees_1 }}"),
    ("(totally optional), you pay", "{{ twilio_fees_2 }}"),
    ("directly for your usage.", "{{ twilio_fees_3 }}"),
    ("How much?", "{{ twilio_fees_4 }}"),
    ("SMS pricing depends on the country, but it's incredibly cheap.", "{{ twilio_fees_5 }}"),
    ("Example:", "{{ twilio_fees_6 }}"),
    ("A US phone number costs $1.15/month, and sending an SMS costs $0.0079. If you trigger an alert to 5 contacts once a month, your total cost is about $1.19/month.", "{{ twilio_fees_7 }}"),
    ("Read our guide on ", "{{ price_disclaimer }}"),
    ("How to set up Twilio", "{{ price_disclaimer2 }}"),
    (" as a ", "{{ price_disclaimer3 }}"),
    
    # footer
    (">Product<", ">{{ footer_product }}<"),
    (">Support<", ">{{ footer_support }}<"),
    (">Legal<", ">{{ footer_legal }}<"),
    (">Download App<", ">{{ footer_download }}<"),
    (">Contact Us<", ">{{ footer_contact }}<"),
]

text = text.replace('translate="no">Direct\n                                        SMS</span>', 'translate="no">{{ term_direct_sms }}</span>')

for i, sub in enumerate(subs):
    if len(sub) == 2:
        old, new_ = sub
        text = text.replace(old, new_)

with open('src/index.html', 'w') as f:
    f.write(text)

print("Created src/index.html with template string injection!")
