import microgear.client as client
import time # ใช้ในการหน่วงเวลา

appid = 'ekaratnida' # ชื่อแอพของเรา
gearkey = 'Xzmr7PkeLMPWBFt' # key
gearsecret = 'nKkMNUjdHgwH7ChMxAEyb9G3H' # secret


client.create(gearkey,gearsecret,appid,{'debugmode': True}) # สร้างข้อมูลสำหรับใช้เชื่อมต่อ

client.setalias("two") # ตั้งชื่้อ

def callback_connect() :
    print ("Now I am connected with netpie")

def callback_message(topic, message) :
    print (topic, ": ", message)

def callback_error(msg) :
    print(msg)

client.on_connect = callback_connect # แสดงข้อความเมื่อเชื่อมต่อกับ netpie สำเร็จ
client.on_message= callback_message # ให้ทำการแสดงข้อความที่ส่งมาให้
client.on_error = callback_error # หากมีข้อผิดพลาดให้แสดง
client.subscribe("/test") # ชื่อช่องทางส่งข้อมูล ต้องมี / นำหน้า และต้องใช้ช่องทางเดียวกันจึงจะรับส่งข้อมูลระหว่างกันได้
client.connect(False) # เชื่อมต่อ ถ้าใช้ False ไม่ค้างการเชื่อมต่อ

i=0
while i<10:
    client.chat("one","hello from two") # ส่งข้อมูลไปให้ one
    time.sleep(0.1) # หน่วงเวลาการส่งข้อมูล 3 วินาที
    i+=1

print("ok")