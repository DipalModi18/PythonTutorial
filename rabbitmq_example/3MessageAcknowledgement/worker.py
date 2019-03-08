import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received " + str(body))
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    # If forgot the basic_ack, Messages will be redelivered when your client quits
    #   (which may look like random redelivery),
    # but RabbitMQ will eat more and more memory as it won't be able to release any unacked messages.
    # In order to debug this kind of mistake you can use rabbitmqctl to print the messages_unacknowledged field:
    # sudo rabbitmqctl list_queues name messages_ready messages_unacknowledged


channel.basic_consume(callback,
                      queue='hello')
# Acknowledgement must be sent on the same channel that received the delivery.
# Attempts to acknowledge using a different channel will result in a channel-level protocol exception.

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
# Using this code we can be sure that even if you kill a worker using CTRL+C while it was processing a message,
#    nothing will be lost. Soon after the worker dies all unacknowledged messages will be redelivered.

