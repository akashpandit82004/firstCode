# import time
# timestamp=time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp=time.strftime('%H')
# print(timestamp)
# timestamp=time.strftime('%M')
# print(timestamp)
# timestamp=time.strftime('%S')
# print(timestamp)

# import datetime

# # Get today's date
# today = datetime.date.today()
# print("Today's Date:", today)

# # Get current date and time
# now = datetime.datetime.now()
# print("Current Date & Time:", now)

# # Access individual parts
# print("Year:", today.year)
# print("Month:", today.month)
# print("Day:", today.day)

# # Custom formatting
# formatted = now.strftime("%d-%m-%Y %H:%M:%S")
# print("Formatted Date & Time:", formatted)

import datetime
today=datetime.date.today()
print("today day date",today)

now =datetime.datetime.now()
print("current date &time",now)

formatted=now.strftime("%d-%m-%Y %H:%M:%S")
print("formatted date &time:",formatted)








