# International-Space-Station-Tracker
This will take your Latitude and Longitude and send you an email if:
1. The ISS is currently overhead.
2. If its currently night time where you live.

If you run the code initally, it will not work. you need to provide two emails (one to send and one to receive) and a desired location (LAT, LONG)

----PLEASE READ THIS--------

- The senders email does not have any security in place besides using a TLS connection. Only use a throw away email for the sending portion.

- If using Gmail, the senders email also needs to have an app password that is created inside the gmail account.
more info here: https://stackoverflow.com/questions/72478573/how-to-send-an-email-using-python-after-googles-policy-update-on-not-allowing-j

- For the receiving end, only the email name you provide will potentially be visible.
