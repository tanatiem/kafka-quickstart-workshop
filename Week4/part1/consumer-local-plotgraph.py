from confluent_kafka import Consumer

c = Consumer({
    'bootstrap.servers': 'localhost:9092,localhost:9192,localhost:9292',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['streams-pageviewstats-typed-output'])

import matplotlib.pyplot as plt
#from matplotlib.pyplot import figure
#figure(num=None, figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
#plt.ion()
lr = {}

import json

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    value = msg.value()
    kvalue = msg.key().decode('utf-8')
    x = json.loads(kvalue)
    y = json.loads(value)
    print('Received message: {0} , {1}'.format(x["windowStart"], y["count"]))
   
    plt.bar(y["region"], y["count"],color='r')
    plt.pause(0.1)
    

plt.show(block=True)
c.close()

