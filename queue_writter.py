"""
Helper file to write into rabbitmq
"""

import pika
import json

queue_name = "jobs_queue"
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port = 5672))
channel = connection.channel()
channel.queue_declare(queue=queue_name)

# Write into rabbitmq to the designated queue
def publish_msg(payload):
    channel.basic_publish(exchange='',
        routing_key=queue_name,
        body=json.dumps(payload)
    )