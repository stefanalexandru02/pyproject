import pika
import json

queue_name = "jobs_queue"
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port = 5672))
channel = connection.channel()
channel.queue_declare(queue=queue_name)

def publish_msg(payload):
    channel.basic_publish(exchange='',
        routing_key=queue_name,
        body=json.dumps(payload)
    )