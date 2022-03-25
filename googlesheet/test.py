from __future__ import print_function
from tkinter import *


from googleapiclient.discovery import build
from google.oauth2 import service_account
import time
import datetime

import pyrebase

flag = 0
now = datetime.datetime.now()
data = {}
data2 = {}


root = Tk()
canvas = Canvas(root, width=400, height= 10, bg="white")
canvas.pack()
def stream_handler(message):
    global ata
    ata= message["data"]


def stream_handler2(message):
    global error
    error = message["data"]
    if message["data"]=="1":
        bb="Lỗi xuất hiện vẫn chưa xử lý lỗi !!!"
        UpdateBackup(bb)
        db.child('/node_backup').update(data)
    if message["data"] == "0":
        bb = "Đã sữa lỗi, nhiệt độ ổn định"
        UpdateBackup(bb)
        db.child('/node_backup').update(data)

def UpdateBackup(x):
    now = datetime.datetime.now()
    temp={
        'time': now.strftime("%m/%d/%Y, %H:%M:%S"),
        'value': x
    }
    for i in range(19, 0, -1):
        data[str(i)] = data[str(i - 1)]
    data['0'] = temp

def FirstUpdate():
    for i in range(20):
        temp = db.child('/node_backup/' + str(i)).get().val()
        data[str(i)] = temp


def stream_handler3(message):
    global mask
    mask = message["data"]
    if message["data"] == "1":
        bbc = "Có nhân viên không mang khẩu trang !!!"
        UpdateBackup2(bbc)
        db.child('/nodebackup2').update(data2)
    if message["data"] == "0":
        bbc = "Đã nhắc nhở nhân viên"
        UpdateBackup2(bbc)
        db.child('/nodebackup2').update(data2)

def UpdateBackup2(x):
    now2 = datetime.datetime.now()
    temp2={
        'time': now2.strftime("%m/%d/%Y, %H:%M:%S"),
        'value': x
    }
    for i in range(19, 0, -1):
        data2[str(i)] = data2[str(i - 1)]
    data2['0'] = temp2
def FirstUpdate2():
    for i in range(20):
        temp = db.child('/nodebackup2/' + str(i)).get().val()
        data2[str(i)] = temp

firebaseConfig = {
    'apiKey': "AIzaSyBxVYFuyDvE-e483uOA3xTGmobp6XsP398",
  'authDomain': "scadanhom6.firebaseapp.com",
  'databaseURL': "https://scadanhom6-default-rtdb.firebaseio.com",
  'projectId': "scadanhom6",
  'storageBucket': "scadanhom6.appspot.com",
  'messagingSenderId': "430018421762",
  'appId': "1:430018421762:web:7dec4d8d2f48d6772b331b",
  'measurementId': "G-MFYG5E494T"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()



FirstUpdate()
FirstUpdate2()

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'key2.json'
credentials = None
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
SAMPLE_SPREADSHEET_ID = '12DJKvTfYvqmio0-kq3R3uRXRlqb_JauKwUKmkAzCCOA'
service = build('sheets', 'v4', credentials=credentials)

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sca!A1:G16").execute()
values = result.get('values', [])

# request = service.spreadsheets().values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                                                  range="sca!A2",
#                                                  valueInputOption="USER_ENTERED",
#                                                  insertDataOption="INSERT_ROWS",
#                                                  body={"values":aoa})
# response = request.execute()


b = datetime.datetime.now()

my_stream = db.child("/node/1").stream(stream_handler)

my_stream2 = db.child("/node2/error").stream(stream_handler2)

my_stream3 = db.child("/node3/mask").stream(stream_handler3)

ata = 0
error = 0
mask=0
aoa=[]
temp=0



def handleBW():
    global flag2,apiKey,authDomain,databaseURL,projectId,storageBucket,messagingSenderId,appId,measurementId
    apiKey = str(txt1.get())
    authDomain = str(txt2.get())
    databaseURL = str(txt3.get())
    projectId = str(txt4.get())
    storageBucket = str(txt5.get())
    messagingSenderId = str(txt6.get())
    appId = str(txt7.get())
    measurementId = str(txt8.get())

    flag2=str(1)



def tick():
    global temp4, flag2,b
    global apiKey, authDomain, databaseURL, projectId, storageBucket, messagingSenderId, appId, measurementId
    global firebaseConfig
    global firebase
    global db
    global my_stream
    global my_stream2
    global my_stream3

    if flag2=="0":
        # vong lap
        print(temp4)
        if error == str(0):
            if mask == str(0):
                aoa = [[ata, "Nhiệt độ ổn định", "Nhân viên vẫn mang khẩu trang ", str(b)]]
            if mask == str(1):
                aoa = [[ata, "Nhiệt độ ổn định", "Có nhân viên không mang khẩu trang !!!", str(b)]]
        if error == str(1):
            if mask == str(0):
                aoa = [[ata, "Lỗi xuất hiện vẫn chưa xử lý lỗi !!!", "Nhân viên vẫn mang khẩu trang ", str(b)]]
            if mask == str(1):
                aoa = [[ata, "Lỗi xuất hiện vẫn chưa xử lý lỗi !!!", "Có nhân viên không mang khẩu trang !!!", str(b)]]

        request = service.spreadsheets().values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                         range="sca!A8",
                                                         valueInputOption="USER_ENTERED",
                                                         insertDataOption="INSERT_ROWS",
                                                         body={"values": aoa})
        response = request.execute()

        temp4 = temp4 + 1
        b = datetime.datetime.now()

        #vong lap
    if flag2=="1":
        # cai dat firebase

        firebaseConfig = {
            'apiKey': apiKey,
            'authDomain': authDomain,
            'databaseURL': databaseURL,
            'projectId': projectId,
            'storageBucket': storageBucket,
            'messagingSenderId': messagingSenderId,
            'appId': appId,
            'measurementId': measurementId
        }
        my_stream.close()
        my_stream2.close()
        my_stream3.close()

        firebase = pyrebase.initialize_app(firebaseConfig)
        db = firebase.database()


        my_stream = db.child("/node/1").stream(stream_handler)

        my_stream2 = db.child("/node2/error").stream(stream_handler2)

        my_stream3 = db.child("/node3/mask").stream(stream_handler3)
        # as
        flag2="0"
    root.after(1000,tick)

lbl1 = Label(root, text="apiKey", fg="red", font=("Arial", 10))
lbl1.pack()
txt1 = Entry(root, width=20)
txt1.pack()


lbl2 = Label(root, text="authDomain", fg="red", font=("Arial", 10))
lbl2.pack()
txt2 = Entry(root, width=20)
txt2.pack()

lbl3 = Label(root, text="databaseURL", fg="red", font=("Arial", 10))
lbl3.pack()
txt3 = Entry(root, width=20)
txt3.pack()

lbl4 = Label(root, text="projectId", fg="red", font=("Arial", 10))
lbl4.pack()
txt4 = Entry(root, width=20)
txt4.pack()

lbl5 = Label(root, text="storageBucket", fg="red", font=("Arial", 10))
lbl5.pack()
txt5 = Entry(root, width=20)
txt5.pack()

lbl6 = Label(root, text="messagingSenderId", fg="red", font=("Arial", 10))
lbl6.pack()
txt6 = Entry(root, width=20)
txt6.pack()

lbl7 = Label(root, text="appId", fg="red", font=("Arial", 10))
lbl7.pack()
txt7 = Entry(root, width=20)
txt7.pack()

lbl8 = Label(root, text="measurementId", fg="red", font=("Arial", 10))
lbl8.pack()
txt8 = Entry(root, width=20)
txt8.pack()




button = Button(root,text = "Ok", command=handleBW)
button.pack()

temp4=0

flag2="0"
apiKey=""
authDomain=""
databaseURL=""
projectId=""
storageBucket=""
messagingSenderId=""
appId=""
measurementId=""

root.after(1000, tick)
root.mainloop()