from os import getenv
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=getenv('RABBITMQ_HOST'),
    port=int(getenv('RABBITMQ_PORT')),
    credentials=pika.PlainCredentials(
        getenv('RABBITMQ_USER'),
        getenv('RABBITMQ_PASSWORD')
    )
))
channel = connection.channel()
channel.queue_declare(queue='default')

if __name__ == '__main__':
    while True:
        channel.basic_publish(exchange='',
                              routing_key='default',
                              body='Hello World!')
        print(" [x] Sent 'Hello World!'")
