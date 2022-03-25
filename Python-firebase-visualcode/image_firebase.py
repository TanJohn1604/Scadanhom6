
import pyrebase
from random import seed
from random import randint
import time
from datetime import datetime

from pyrebase.pyrebase import Auth
now = datetime.now()


seed(1)
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

email="asd@gmail.com"
password="123456"
auth=firebase.auth()
db=firebase.database()
sto=firebase.storage()
user=auth.sign_in_with_email_and_password(email,password)

sto.child("test").put("anh_the_tan.jpg")
a=sto.child("test").get_url(user['idToken'])

db.child("node/url").set(a)




# while True:
#     temp=temp+1
#     data2=[]

#     for value in data.values():
#         data2.append(value)
        
#     data2.pop(0)
#     data2.append(randint(0, 10))
    
#     i=0
#     for key in data.keys():
        
#         data[key]=data2[i]
#         i=i+1

#     db.child("mode2").set(data)
#     if temp ==500:
#         break
    


