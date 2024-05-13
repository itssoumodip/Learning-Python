'''
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print("Hour is   : ", timestamp)
timestamp = time.strftime('%M')
print("Minite is : ", timestamp)
timestamp = time.strftime('%S')
print("Second is : ", timestamp)
'''

import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("Enter The Time Bro : "))
print(hour)
if (hour>=0 and hour<12):
    print("Good Morning Sir !!")
elif (hour>=12 and hour<17):
    print("Good Evening Sir !!")
elif (hour>=17 and hour>0):
    print("Good Night Sir !!!")
else:
    print("Sleep !!")