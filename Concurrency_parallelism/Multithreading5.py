# Running method with multiple threads
# Reference: http://masnun.rocks/2016/10/06/async-python-the-different-forms-of-concurrency/
import threading
import time
import random


def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print("I am Worker {}, I slept for {} seconds".format(number, sleep))


for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()

print("All Threads are queued, let's see when they finish!")

# The GIL(Global Interpreter Lock) is a locking mechanism that the Python interpreter runs only one thread at a time.
# That is only one thread can execute Python byte code at any given time.
# This GIL makes sure that multiple threads DO NOT run in parallel.
# Quick facts about the GIL:
#   One thread can run at a time.
#   The Python Interpreter switches between threads to allow concurrency.
