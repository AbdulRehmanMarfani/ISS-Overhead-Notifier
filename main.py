import requests
from datetime import datetime
import smtplib

MY_LAT = 00.000000 
MY_LONG = 00.000000 

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


def is_iss_overhead():
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False


if is_iss_overhead():
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user="your_email_here", password="your_app_password_here")
            connection.sendmail(
                from_addr="your_email_here",
                to_addrs="recipient_email_here",
                msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
            )
