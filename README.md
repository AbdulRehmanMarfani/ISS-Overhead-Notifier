---

# ISS Overhead Notifier 🚀

A Python script that alerts you via email when the International Space Station (ISS) is above your location *and* it's currently dark outside, so you can look up and see it!

---

## Features 🌌

* **Real-Time ISS Tracking**: Fetches the ISS's current position using the Open Notify API.
* **Sunlight Check**: Uses Sunrise-Sunset API to determine if it's dark at your location.
* **Email Notification**: Sends you an email if the ISS is overhead and visible.
* **Smart Geolocation Filter**: Only alerts when ISS is within ±5° of your coordinates.

---

## Requirements 🛠️

* Python 3.6+
* `requests` module (`pip install requests`)
* A Gmail account with **App Passwords enabled**
* Internet connection

---

## Files Included 📂

1. **`main.py`**: The core logic — fetches API data, checks conditions, and sends emails.

---

## How to Use? 🧭

1. Clone the repository or download the source code.

2. Replace the placeholder values in `main.py`:

   ```python
   MY_LAT = 00.000000       # Your latitude
   MY_LONG = 00.000000      # Your longitude

   connection.login(user="your_email_here", password="your_app_password_here")
   connection.sendmail(
       from_addr="your_email_here",
       to_addrs="recipient_email_here",
       msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
   )
   ```

3. Make sure `requests` is installed:

   ```bash
   pip install requests
   ```

4. Run the script:

   ```bash
   python main.py
   ```

---

## ⚠️ Using Gmail? Read This First

Gmail no longer allows less secure apps to send emails using your normal password.
You need to use an **App Password** instead.

🔐 Follow this official guide to set it up:
👉 [How to Generate a Gmail App Password](https://support.google.com/accounts/answer/185833)

---

## Goal 🎯

* You’ll get an email **only** when:

  * The ISS is within ±5° of your location
  * It’s currently dark at your coordinates (before sunrise or after sunset)

---

## Future Enhancements 🚀

* Automate the script to run every 60 seconds
* Use environment variables to hide email and password
* Host the script on a cloud service for 24/7 alerts
* Add SMS or push notifications instead of email

---

## Developer Note 🧑‍💻

> This was my **first real automation script using multiple APIs**. I learned how to:
>
> * Work with REST APIs
> * Parse real-time JSON data
> * Handle geolocation filtering and time-based logic
> * Automate email notifications using SMTP

It was a fun step forward from GUI apps into real-world automation.

---

## Credits ✨

* **Programming**: Abdul Rehman Marfani
* **APIs Used**: Open Notify, Sunrise-Sunset
* **Email**: Gmail SMTP with TLS

---
