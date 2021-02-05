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

li = [{"_t": "mt","title":"Avengers: Endgame","release_year":2019,"total_sales":856980506},
    {"_t": "mt","title":"Captain Marvel","release_year":2019,"total_sales":426829839},
    {"_t": "mt","title":"Toy Story 4","release_year":2019,"total_sales":401486230},
    {"_t": "mt","title":"The Lion King","release_year":2019,"total_sales":385082142},
    {"_t": "mt","title":"Black Panther","release_year":2018,"total_sales":700059566},
    {"_t": "mt","title":"Avengers: Infinity War","release_year":2018,"total_sales":678815482},
    {"_t": "mt","title":"Deadpool 2","release_year":2018,"total_sales":324512774},
    {"_t": "mt","title":"Beauty and the Beast","release_year":2017,"total_sales":517218368},
    {"_t": "mt","title":"Wonder Woman","release_year":2017,"total_sales":412563408},
    {"_t": "mt","title":"Star Wars Ep. VIII: The Last Jedi","release_year":2017,"total_sales":517218368}
    ]

for i in li:

    p.poll(0)
    
    p.produce('streams-minmax-input', key="", value=json.dumps(i))
    time.sleep(1)
   

p.flush()