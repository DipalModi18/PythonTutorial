# Multithreaded Priority Queue

import queue
import threading
import time

exitFlag = 0
queueLock = threading.Lock()
workQueue = queue.Queue(10)


class MyThread(threading.Thread):
    def __init__(self, threadID, threadName, q):
        threading.Thread.__init__()
        self.threadID = threadID
        self.threadName = threadName
        self.q = q

    def run(self):
        print("Starting: ", self.threadName)
        process_data(self.threadName, self.q)
        print("Exiting: ", self.threadName)


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("Processing ", threadName, " data ", data)
        else:
            queueLock.release()
            time.sleep(1)


threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4"]
nameList = ["One", "Two", "Three", "Four"]
threads = list()
threadId = 1

for tname in threadList:
    thread = MyThread(threadId, tname, workQueue)
    thread.start()
    threads.append(thread)
    threadId += 1

queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()

print("Exiting main thread")

