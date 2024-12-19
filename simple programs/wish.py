import time
ts = time.strftime('%H:%M:%S')
print("Current Time:", ts)

h = int(time.strftime('%H')) 
if 5 <= h < 12:
    print("Good Morning!")
elif 12 <= h < 17:
    print("Good Afternoon!")
elif 17 <= h < 21:
    print("Good Evening!")
else:
    print("Good Night!")
