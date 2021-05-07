import time 
from datetime import datetime

now = datetime.now()
USER_DATA = input("how much time?: ")

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print('Suprise in', USER_DATA)
while True:
  time.sleep(int(USER_DATA))
  print('You look great today')
  print('Suprise in', USER_DATA)
