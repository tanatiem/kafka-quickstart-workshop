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

data1 = {"_t": "mt","title":"Avengers: Endgame","release_year":2019,"total_sales":856980506}
data2 = {"_t": "mt","title":"Captain Marvel","release_year":2019,"total_sales":426829839}
data3 = {"_t": "mt","title":"Toy Story 4","release_year":2019,"total_sales":401486230}
data4 = {"_t": "mt","title":"The Lion King","release_year":2019,"total_sales":385082142}
while True:

    p.poll(0)
    
    p.produce('streams-minmax-input', key="", value=json.dumps(data1))
    time.sleep(1)
    
    p.produce('streams-minmax-input', key="", value=json.dumps(data2))
    time.sleep(1)

    p.produce('streams-minmax-input', key="", value=json.dumps(data3))
    time.sleep(1)

    p.produce('streams-minmax-input', key="", value=json.dumps(data4))
    time.sleep(1)


p.flush()