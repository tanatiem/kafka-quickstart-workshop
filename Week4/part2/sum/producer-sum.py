from confluent_kafka import Producer
import time

p = Producer({'bootstrap.servers': 'localhost:9092,localhost:9192,localhost:9292'})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


import json

print("Start producer...")
data = {"_t": "pv","title":"Die Hard","ticket_total_value":12}
while True:

    p.poll(0)
    
    p.produce('streams-numbers-input', key="", value=json.dumps(data))
    
    time.sleep(1)

p.flush()