import os
import requests
from datetime import datetime
import smtplib

MY_LOC = (, ) #--------------------------------------------------------------Your Latitude and longitude as floats
SENDER_EMAIL = "" #-This is how the code will send the email. Dont use an email that has sensitive info tied to it
PASSWORD = "" #---------------------------------------------------------This is the password for the senders email
RECIEVER_EMAIL = "" #--------------------------- This is the email that you would like to receive the notification

#----------------------------------------------------------------------------CHECKING IF ISS IS OVERHEAD CURRENTLY
def iss_is_overhead():
  response = requests.get(url="http://api.open-notify.org/iss-now.json")
  response.raise_for_status()
  iss_data = response.json()

  iss_longitude = float(iss_data["iss_position"]["longitude"])
  iss_latitude = float(iss_data["iss_position"]["latitude"])
  iss_position = (iss_longitude, iss_latitude)

  if (MY_LOC[0]-5 <= iss_latitude <= MY_LOC[0]+5 and 
      MY_LOC[1]-5 <= iss_longitude <= MY_LOC[1]+5):
        print("The ISS is currently overhead.")
        return True
  else:
    print(f"ISS is not overhead.\nYour location: {MY_LOC}\nISS Location: {iss_position}")
    return False

#-------------------------------------------------------------------------------CHECKING IF ISS IS VISIBLE OR NOT
def is_night():
  parameters = {
  "lat": MY_LOC[0],
  "lng": MY_LOC[1],
  "formatted": 0,
}

  response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
  response.raise_for_status()
  sun_data = response.json()
    
  sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
  sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
  
  time_now = datetime.now().hour
  
  if time_now <= sunrise and time_now >= sunset:
    print("It is night time in your area.")
    return True
  else:
    print("It is day time in your area.")
    return False

#-------------------------------------------------------------------------SENDING NOTIFICATION TO PROVIDED EMAIL
def send_notification():
  print("Sending Notification.")
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=SENDER_EMAIL, password=PASSWORD)
    connection.sendmail(
      from_addr=SENDER_EMAIL, 
      to_addrs=RECIEVER_EMAIL, 
      msg="Subject:ISS\n\nThe International Space Station is overhead!")

#-----------------------------------------------------------------------------------------------MAIN CODE TO RUN
if iss_is_overhead() and is_night():
  send_notification()
  
