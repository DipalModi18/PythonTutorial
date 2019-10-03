import time
import calendar

# time.time() returns the current system time in ticks since 12:00am, January 1, 1970(epoch).
print("Number of ticks since 12:00am, January 1, 1970:", time.time())

print('localtime: ', time.localtime())

# readable format
localtime = time.asctime( time.localtime(time.time()))
print("Local current time :", localtime)

# Here, we print a calendar for a given month
cal = calendar.month(2016, 2)
print("Here is the calendar:")
print(cal)
