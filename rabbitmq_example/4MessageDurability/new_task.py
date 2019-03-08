import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# When RabbitMQ quits or crashes it will forget the queues and messages unless you tell it not to.
# Two things are required to make sure that messages aren't lost:
# we need to mark both the queue and messages as durable.
channel.queue_declare(queue='task_queue', durable=True)
# Although this command is correct by itself, it won't work in our setup.
# That's because we've already defined a queue called hello which is not durable.
# RabbitMQ doesn't allow you to redefine an existing queue with different parameters and
#   will return an error to any program that tries to do that.

message = ' '.join(sys.argv[1:]) or "Hello World!"

# mark our messages as persistent - by supplying a delivery_mode property with a value 2.
channel.basic_publish(exchange='',
                      routing_key="task_queue",
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode=2,  # make message persistent
                      ))
# Marking messages as persistent doesn't fully guarantee that a message won't be lost.
# Although it tells RabbitMQ to save the message to disk,
# there is still a short time window when RabbitMQ has accepted a message and hasn't saved it yet

print(" [x] Sent %r" % message)
