# Reference: https://www.rabbitmq.com/tutorials/tutorial-two-python.html
import sys
import pika

# The main idea behind Work Queues (aka: Task Queues) is to avoid doing a
#   resource-intensive task immediately and having to wait for it to complete.
# We encapsulate a task as a message and send it to the queue.
# A worker process running in the background will pop the tasks and eventually execute the job.
# When you run many workers the tasks will be shared between them.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
print(" [x] Sent %r" % message)

# To run:  python3 new_task.py First message....   ==> No. of dots specify here how long the task is
# i.e. 4 dots means it will take 4 sec to complete the work by the worker.
