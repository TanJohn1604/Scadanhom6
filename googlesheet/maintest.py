from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
import time
import datetime

import pyrebase




def stream_handler(message):
    global ata
    ata= message["data"]


def stream_handler2(message):
    global error
    error = message["data"]

def stream_handler3(message):
    global mask
    mask = message["data"]

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
while temp<3600:
    print(temp)
    if error == str(0):
        if mask==str(0):
            aoa = [[ata, "Nhiệt độ ổn định","Nhân viên vẫn mang khẩu trang ", str(b)]]
        if mask==str(1):
            aoa = [[ata, "Nhiệt độ ổn định","Có nhân viên không mang khẩu trang !!!", str(b)]]
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
    time.sleep(1)
    temp=temp+1
    b = datetime.datetime.now()
# tem=0
# while tem<100:
#     tem=tem+1
#     print(tem)
#     print("--------------------")
#     print(data)
#     print("--------------------")
#     time.sleep(1)
# my_stream.close()
