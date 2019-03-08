import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)


# in a situation with two workers, when all odd messages are heavy and even messages are light,
#   one worker will be constantly busy and the other one will do hardly any work.
# Well, RabbitMQ doesn't know anything about that and will still dispatch messages evenly.
#
# This happens because RabbitMQ just dispatches a message when the message enters the queue.
# It doesn't look at the number of unacknowledged messages for a consumer.
# It just blindly dispatches every n-th message to the n-th consumer.
# we can use the basic.qos method with the prefetch_count=1 setting.
# This tells RabbitMQ not to give more than one message to a worker at a time.
# Or, in other words, don't dispatch a new message to a worker until it has processed and acknowledged the previous one.
# Instead, it will dispatch it to the next worker that is not still busy.
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()
