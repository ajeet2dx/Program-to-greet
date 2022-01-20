import datetime
currentTime = datetime.datetime.now()
c = (currentTime.strftime("%Y-%m-%d   %H:%M:%S"))
print("Current date and time : ")
print(c)
if 6 <= currentTime.hour < 12:
    print('Good morning.')
if 12 <= currentTime.hour < 17:
    print('Good afternoon.')
if 17 <= currentTime.hour < 20:
    print('Good evening.')