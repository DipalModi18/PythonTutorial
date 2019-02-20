# Using thread module

import _thread
import time


def printTime(threadName, delay):
    print("In printTime with ", threadName)
    for i in range(1, 6):
        time.sleep(delay)
        print(threadName, " - ", time.ctime(time.time()))


try:
    _thread.start_new_thread(printTime, ("Thread 1", 1))
    _thread.start_new_thread(printTime, ("Thread 2", 2))
except:
    print("Error while starting the thread")

while 1:
    pass

