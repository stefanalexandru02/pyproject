import pika
import json
import os
import urllib.request

# connect to queue
queue_name = "jobs_queue"
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port = 5672))
channel = connection.channel()
channel.queue_declare(queue=queue_name)

def callback(ch, method, properties, body):
    payload = json.loads(body.decode('utf-8'))
    try:
        # print(f"Processing {payload}")
        os.mkdir(payload['path'])

        html_text = urllib.request.urlopen(payload['link']).read()
        with open(f"{payload['path']}/page.html", 'w') as f:
            f.write(html_text.decode('utf-8'))
            
        print('Record progressed successfully')
    except Exception as e:
        print(f"Error processing {payload}: {e}")

# Connect to queue and assign consumer
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
print('Worker started')
channel.start_consuming()