
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

data2={}

def stream_handler(message):

    
    # if flag==0:
    #     UpdateBackup(message["data"][1])
    # if flag!=0:
    #     UpdateBackup(message["data"])
    # if message["data"][0]==Null:
    if message["data"] =="1":
    
    #     UpdateBackup(message["data"][1])
    # else:
        bb="Lỗi xuất hiện vẫn chưa xử lý lỗi !!!"
        UpdateBackup(bb)
        db.child('/node_backup').update(data)

    if message["data"] =="0":
    
    #     UpdateBackup(message["data"][1])
    # else:
        bb="Đã sữa lỗi, nhiệt độ ổn định"
        UpdateBackup(bb)
        db.child('/node_backup').update(data)

def stream_handler2(message):

    
    # if flag==0:
    #     UpdateBackup(message["data"][1])
    # if flag!=0:
    #     UpdateBackup(message["data"])
    # if message["data"][0]==Null:
    if message["data"] =="1":
        
    #     UpdateBackup(message["data"][1])
    # else:
        bbc="Có nhân viên không mang khẩu trang !!!"
        UpdateBackup2(bbc)
        db.child('/nodebackup2').update(data2)

    if message["data"] =="0":
        
    #     UpdateBackup(message["data"][1])
    # else:
        bbc="Đã nhắc nhở nhân viên"
        UpdateBackup2(bbc)
        db.child('/nodebackup2').update(data2)

def UpdateBackup2(x):
    now = datetime.now()
    temp={
            'time':now.strftime("%m/%d/%Y, %H:%M:%S"),
            'value':x
        }
    for i in range(19,0,-1):

        
        data2[str(i)]=data2[str(i-1)]
    data2['0']=temp

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
def FirstUpdate2():
    for i in range(20):
        temp=db.child('/nodebackup2/'+str(i)).get().val()
        data2[str(i)]=temp

firebaseConfig = {
    'apiKey': "AIzaSyBkkn-3nnCLQpMpKL_Tf12-LU5UTGzzofk",
  'authDomain': "scada-9f22b.firebaseapp.com",
  'databaseURL': "https://scada-9f22b-default-rtdb.firebaseio.com",
  'projectId': "scada-9f22b",
  'storageBucket': "scada-9f22b.appspot.com",
  'messagingSenderId': "634112793504",
  'appId': "1:634112793504:web:883c9e04a81803b2bd62c5",
  'measurementId': "G-X40DQWY6F6"
   }
firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()



FirstUpdate()
FirstUpdate2()

# for i in range(19,-1,-1):
#     print(data[str(i)])
tem=0
my_stream = db.child("/node2/error").stream(stream_handler)#error

my_stream2 = db.child("/node3/mask").stream(stream_handler2) #mask

while tem<3600:
    tem=tem+1
    print(tem)
    time.sleep(1)
my_stream.close()
my_stream2.close()

