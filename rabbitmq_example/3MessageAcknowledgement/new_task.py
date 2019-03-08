# Reference: https://www.rabbitmq.com/tutorials/tutorial-two-python.html
import sys
import pika

# In order to make sure a message is never lost, RabbitMQ supports message acknowledgments.
# An ack(nowledgement) is sent back by the consumer to tell RabbitMQ that a particular message had been received,
#    processed and that RabbitMQ is free to delete it.
# If a consumer dies (its channel is closed, connection is closed, or TCP connection is lost)
#    without sending an ack, RabbitMQ will understand that a message wasn't processed fully and will re-queue it.
# If there are other consumers online at the same time, it will then quickly redeliver it to another consumer.
# That way you can be sure that no message is lost, even if the workers occasionally die.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

message = ' '.join(sys.argv[1:]) or "Hello World!"

# Manual message acknowledgments are turned on by default.
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
print(" [x] Sent %r" % message)

# To run:  python3 new_task.py First message....   ==> No. of dots specify here how long the task is
# i.e. 4 dots means it will take 4 sec to complete the work by the worker.
