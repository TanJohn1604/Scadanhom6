
from os import system
from pyasn1.type.univ import Null
import pyrebase
from random import seed
from random import randint
import time
from datetime import datetime
from collections import OrderedDict

flag=0
now = datetime.now()
data={}

def stream_handler(message):

    
    # if flag==0:
    #     UpdateBackup(message["data"][1])
    # if flag!=0:
    #     UpdateBackup(message["data"])
    # if message["data"][0]==Null:
    if message["data"] =="1":
        print(message["data"])
    #     UpdateBackup(message["data"][1])
    # else:
        bb="Có nhân viên không mang khẩu trang !!!"
        UpdateBackup(bb)
        db.child('/node_backup').update(data)

    if message["data"] =="0":
        print(message["data"])
    #     UpdateBackup(message["data"][1])
    # else:
        bb="Đã nhắc nhở nhân viên"
        UpdateBackup(bb)
        db.child('/node_backup').update(data)




def UpdateBackup(x):
    now = datetime.now()
    temp={
            'time':now.strftime("%m/%d/%Y, %H:%M:%S"),
            'value':x
        }
    for i in range(19,0,-1):

        
        data[str(i)]=data[str(i-1)]
    data['0']=temp


def FirstUpdate():
    for i in range(20):
        temp=db.child('/node_backup/'+str(i)).get().val()
        data[str(i)]=temp

firebaseConfig = {
    'apiKey': "AIzaSyC3WbK4Z7-c_t5RtbBi9SwOUM-jwAbUuPY",
  'authDomain': "client-9828d.firebaseapp.com",
  'databaseURL': "https://client-9828d-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "client-9828d",
  'storageBucket': "client-9828d.appspot.com",
  'messagingSenderId': "586283574928",
  'appId': "1:586283574928:web:c423412325ae6011591a15",
  'measurementId': "G-HTCCK9PBZ1"
   }
firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()



FirstUpdate()


# for i in range(19,-1,-1):
#     print(data[str(i)])
tem=0
my_stream = db.child("/node3/mask").stream(stream_handler)

while tem<100:
    tem=tem+1
    print(tem)
    time.sleep(0.5)
my_stream.close()


