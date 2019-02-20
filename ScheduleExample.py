# pip3 install schedule
# Schedule lets you run Python functions( or any other callable) periodically at pre - determined intervals
# Reference: https://schedule.readthedocs.io/en/stable/

import schedule
import time


def job():
    print("I'm working at..." + str(time.ctime()))


# schedule.every(): Schedule a new periodic job.
#
# Parameters:	interval – A quantity of a certain time unit
# Returns:	An unconfigured Job(class schedule.Job)
schedule.every(10).minutes.do(job)  # do(job_func, *args, **kwargs): Specifies the job_func that should be called every time the job runs.
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)  # at: Specify a particular time that the job should be run at.
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()  # Run all jobs that are scheduled to run.
    time.sleep(1)
