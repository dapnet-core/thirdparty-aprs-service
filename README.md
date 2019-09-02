# thirdparty-aprs-service
Third party service to send paging calls also via APRS messaging

Pseudo-Code to get the calls:

connection = amqp.Connection("dapnetdc2.db0sda.ampr.org")
channel = connection.channel()
aprs_queue = channel.queue_declare("aprs_queue")
channel.queue_bind(exchange="thirdparty.aprs", queue=bm_queue)
channel.basic_consume(queue=aprs_queue, on_message_callback=callback)

def callback(ch, method, properties, body):
    print(body)
    
Also check https://github.com/rabbitmq/rabbitmq-tutorials/blob/master/python/receive_logs_topic.py

For credentials see https://amqp.readthedocs.io/en/latest/reference/amqp.connection.html
