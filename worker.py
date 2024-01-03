import pika
import json
import os
import urllib.request

queue_name = "jobs_queue"
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port = 5672))
channel = connection.channel()
channel.queue_declare(queue=queue_name)

def callback(ch, method, properties, body):
    payload = json.loads(body.decode('utf-8'))
    print(f"Processing {payload}")
    os.mkdir(payload['path'])

    try:
        html_text = urllib.request.urlopen(payload['link']).read()
        with open(f"{payload['path']}/page.html", 'w') as f:
            f.write(html_text.decode('utf-8'))
    except:
        print("Error reading link")


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()