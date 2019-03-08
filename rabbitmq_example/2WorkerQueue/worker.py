# One of the advantages of using a Task Queue is the ability to easily parallelise work.
# If we are building up a backlog of work, we can just add more workers and that way, scale easily.
import pika
import time

# Run two or more instance of worker.py
# By default, RabbitMQ will send each message to the next consumer, in sequence.
# On average every consumer will get the same number of messages.
# This way of distributing messages is called round-robin.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
