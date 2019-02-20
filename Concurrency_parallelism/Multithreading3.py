# Synchronizing Threads

import threading
import time

threadLock = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self, threadID, threadName, counter):
        threading.Thread.__init__(self)
        self.threadId = threadID
        self.threadName = threadName
        self.counter = counter

    def print_time(self):
        print("Acquired the lock for: ", self.threadName)
        time.sleep(self.counter)
        print("Releasing the lock: ", self.threadName)

    def run(self):
        print("In the run for: " + self.name)
        # acquire(blocking) - If blocking is set to 0,
        # the thread returns immediately with a 0 value if the lock cannot be acquired and with a
        # 1 if the lock was acquired.
        # If blocking is set to 1, the thread blocks and wait for the lock to be released.
        threadLock.acquire(1)
        self.print_time()
        threadLock.release()


thread1 = MyThread(1, "Thread-1", 3)
thread2 = MyThread(2, "Thread-2", 2)

threads = list()
threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Main completed")
