
from os import system
import pyrebase
from random import seed
from random import randint
import cv2
import time

def stream_handler(message):
    print(message["data"][1])

    
    
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

# while True:
    
#     a=db.child("mode2").get().val()

#     print(a)
    
b=0

my_stream = db.child("node").stream(stream_handler)

my_stream.close()
  
  
  
  
