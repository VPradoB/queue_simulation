import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost',
    port=5672,
    credentials=pika.PlainCredentials('user', 'password')
))
channel = connection.channel()
while True:
    channel.basic_publish(exchange='',
                          routing_key='default',
                          body='Hello World!')
    print(" [x] Sent 'Hello World!'")
