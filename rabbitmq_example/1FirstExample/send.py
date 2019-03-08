# Reference: https://www.rabbitmq.com/tutorials/tutorial-one-python.html
# send.py will send a single message to the queue.

import pika

# establish a connection with RabbitMQ server.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# before sending we need to make sure the recipient queue exists.
# If we send a message to non-existing location, RabbitMQ will just drop the message.
channel.queue_declare(queue='hello')  # creating a hello queue to which the message will be delivered

# In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
# a default exchange identified by an empty string.
# This exchange is special = it allows us to specify exactly to which queue the message should go.
# The queue name needs to be specified in the routing_key parameter
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World! again')
print(" [x] Sent 'Hello World!'")

# Before exiting the program we need to make sure the network buffers were flushed
# and our message was actually delivered to RabbitMQ. We can do it by gently closing the connection.
connection.close()
