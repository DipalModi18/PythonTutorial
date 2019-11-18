import time
import datetime
import calendar

# Get the current date and time
print("Current time: {}".format(datetime.datetime.now()))

# Get just the current time
print("Current time: {}".format(datetime.datetime.now().time()))

# Freeze the program for a set period of time
print("Feeling sleepy, let me sleep for 5 sec")
time.sleep(5)

# Measure runtime of a python command
start = time.time()
a = 100 / 5
end = time.time()
print(end-start)
