
import time
MINUTES_PER_DEATH=3


per_hour=60/MINUTES_PER_DEATH
per_day=per_hour*24
per_year=per_day*365


print('child TB deaths (estimate)')
print(f"per hour:{per_hour:.0f}")
print(f"per day{per_day:.0f}")
print(f"per year{per_year:.0f}")


# Live counter: one Death every 3 minutes (sped up for the demo)
count=0
for minute in range(1, 61):
    if minute % MINUTES_PER_DEATH == 0:
        count += 1
        print(f"minute{minute}: total deaths so far{count}")
        






