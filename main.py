import requests
from datetime import datetime
import smtplib

MY_LAT = 24.860735 
MY_LONG = 67.001136 

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
            connection.login(user="abdulrehmanmarfani84@gmail.com", password="ojmvxdpzqqvbewyo")
            connection.sendmail(
                from_addr="abdulrehmanmarfani84@gmail.com",
                to_addrs="abdulrehmanmarfani84@gmail.com",
                msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
            )


