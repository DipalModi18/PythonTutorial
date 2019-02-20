# Concurrency implies that two tasks make progress together.
# Parallelism is in fact a form of concurrency. But parallelism is hardware dependent.
# For example if there is only one core in the CPU, two operations can’t really run in parallel.
# They just share time slices from the same core. This is concurrency but not parallelism.
# But when we have multiple cores, we can actually run two or more operations (depending on the number of cores) in parallel.
# Parallelism implies Concurrency. But Concurrency doesn’t always mean Parallelism.

# Summary:
# Sync: Blocking operations.
# Async: Non blocking operations.
# Concurrency: Making progress together.
# Parallelism: Making progress in parallel.

import multiprocessing
import time
import random


def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print("I am Worker {}, I slept for {} seconds".format(number, sleep))


for i in range(5):
    t = multiprocessing.Process(target=worker, args=(i,))
    t.start()

print("All Processes are queued, let's see when they finish!")
