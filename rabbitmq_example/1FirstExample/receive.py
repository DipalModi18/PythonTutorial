# Reference: https://www.rabbitmq.com/tutorials/tutorial-one-python.html

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


# to see what queues RabbitMQ has and how many messages are in them.
# You can do it (as a privileged user) using the rabbitmqctl tool:
# sudo rabbitmqctl list_queues


def callback(ch, method, properties, body):
    # Receiving messages from the queue is more complex. It works by subscribing a callback function to a queue.
    # Whenever we receive a message, this callback function is called by the Pika library.
    print(" [x] Received %r" % body)


# we need to tell RabbitMQ that this particular callback function should receive messages from our hello queue
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
