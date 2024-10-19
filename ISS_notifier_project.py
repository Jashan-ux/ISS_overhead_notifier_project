import requests
from sunrise_set import sunrise_time_ist ,sunset_time_ist
from datetime import datetime
import smtplib
import time
MY_LAT = 30.670067
MY_LONG = 76.664383
MY_EMAIL = "jashananeja777@gmail.com"
PASSWORD = "nvjkitfmqrvgafkw"

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data =response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
def ISS_overhead():
    if MY_LAT-5 < iss_latitude < MY_LAT+5 and MY_LONG-5 < iss_longitude < MY_LONG+5 :
        return True
def is_night() :
    if sunset_time_ist.strftime('%I')<  datetime.now().hour  < sunrise_time_ist.strftime('%I'):
        return True
while True : 
    time.sleep(60)  
    if ISS_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection :
            connection.starttls()
            connection.login(MY_EMAIL,PASSWORD)

            connection.sendmail(
                from_addr= MY_EMAIL,
                to_addrs= "jashaninsan777@gmail.com",
                msg= "Subject:Look Up.\n\nThe ISS is above you in the sky."
                )


    