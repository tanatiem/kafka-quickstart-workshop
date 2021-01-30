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

uList = ["a"]
pList = ["11"]
rList = ["AB"]

#r1 = {"_t": "pv", "user":"2", "page":"22", "timestamp":1435278177777}
#r2 = {"_t": "up", "region":"CA","timestamp":1435278177777} 

import json
import random

# Trigger any available delivery report callbacks from previous produce() calls
# p.poll(0)
i = 0
while True:
    user = random.choice(uList)
    page = random.choice(pList)
    region = random.choice(rList)
    r1 = {"_t": "pv", "user":user, "page":page, "timestamp": int(time.time() * 1000)}
    print(r1)
    user = random.choice(uList)
    region = random.choice(rList)
    r2 = {"_t": "up", "region":region, "timestamp": int(time.time() * 1000)}
    print(r2)
    p.produce('streams-pageview-input', key=user, value=json.dumps(r1))
    p.produce('streams-userprofile-input', key=user, value=json.dumps(r2))
    time.sleep(1)
    #i = i+1
    #if i == 5:
    #    break

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()