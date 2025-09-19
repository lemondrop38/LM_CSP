# LM 6th Time of Day

import datetime

time = int(input("What time is it (military time)?"))

if time <= 11:
    print("Good Morning!")
elif time <= 17:
    print("Good Afternoon!")
elif time <= 24:
    print("Good Evening!")
else:
    print("That's more hours than exist in a day.")