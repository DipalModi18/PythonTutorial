# workerpool: This module facilitates distributing simple operations into jobs that are sent to worker threads,
#   maintained by a pool object.

# It consists of these components:
# 1) Jobs, which are single units of work that need to be performed.
# 2) Workers, who grab jobs from a queue and perform them.
# 3) Worker pool, which keeps track of workers and the job queue.


import os
import time
import random
import workerpool


class SleepJob(workerpool.Job):
    """Job for couting numbers."""

    def __init__(self, count, jobname):
        self.count = count
        self.jobname = jobname

    def run(self):
        print(self.jobname + ' is going to sleep for ' + str(self.count) + ' seconds')
        time.sleep(self.count)
        print(self.jobname + ' completed')


# Initialize a pool, 5 threads in this case
pool = workerpool.WorkerPool(size=5)

for i in range(1, 11):  # Creating 10 jobs
    job = SleepJob(random.randrange(1, 10), "Job " + str(i))
    pool.put(job)

# Send shutdown jobs to all threads, and wait until all the jobs have been completed
pool.shutdown()
pool.wait()

# Reference: https://github.com/shazow/workerpool/wiki/Mass-Downloader
