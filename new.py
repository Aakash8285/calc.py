from datetime import datetime
from playsound import playsound
alert_time = input("Enter the time of your alarm to be set:HH:MM:SS\n ")
alarm_hour=alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("setting up alarm..")
while True:
    now = datetime.now()
    current_hour = now.
