# The concurrent.futures module provides a high-level interface for asynchronously executing callables.
# The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor.
# Both implement the same interface, which is defined by the abstract Executor class.

# ThreadPoolExecutor and the ProcessPoolExecutor.These executors maintain a pool of threads or processes.
# We submit our tasks to the pool and it runs the tasks in available thread / process.
# A Future object is returned which we can use to query and get the result when the task has completed.

from concurrent.futures import ThreadPoolExecutor
from time import sleep


def return_after_5_secs(message):
    sleep(5)
    return message


pool = ThreadPoolExecutor(3)

future = pool.submit(return_after_5_secs, "hello")  # submit(fn, *args, **kwargs)
# Schedules the callable, fn, to be executed as fn(*args **kwargs) and
#   returns a Future object representing the execution of the callable.

# future: The Future class encapsulates the asynchronous execution of a callable.
# Future instances are created by Executor.submit().
# https://docs.python.org/3/library/concurrent.futures.html#future-objects
print(future.done())
sleep(5)
print(future.done())
print(future.result())
