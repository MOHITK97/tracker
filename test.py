import eel
from random import randint
import requests
import json
import subprocess   
import pyautogui
import imutils
import cv2

from PIL import Image
from io import BytesIO
import time
import numpy as np
from threading import Thread
from datetime import datetime
import os
from browser_history import get_history
import ctypes

# def close_callback(route, websockets):
#     if not websockets:
#         print('Bye!')
#         exit()

# # get path Automatically
# basedir = os.path.dirname(os.path.abspath(__file__))
# categorization_file = os.path.join(basedir,'/web')
# eel.init('web')
 
# idlsttm=""


# def visitedweb():
#     old= open('data.json', 'r').read()
#     old=json.loads(old)
#     for i in old:
#         trackid=old['trackid']
#         token=old['token']
#         shiftStartAt=old['shiftStartAt']
#         shiftEndAt=old['shiftEndAt']
#         print(shiftStartAt)
#         print(shiftEndAt)
#         print(token)
#         print(trackid)


#     outputs = get_history()
#     his = outputs.histories
#     current_time = datetime.now()
#     current_time=current_time.date().strftime('%y-%m-%d')
#     shiftStartAt=shiftStartAt
#     shiftEndAt=shiftEndAt
#     z=0
#     data={}
#     data.update({"trackingId":trackid})
#     visitedSites=[]
#     for i in his:
#         try:
#             if str(current_time) in str(i[0]):
#                 ch=str(i[0]).split('+')[0].split(" ")[1].split(":")[0]
#                 st=int(shiftStartAt.split(":")[0])
#                 en=int(shiftEndAt.split(":")[0])
#                 if int(ch)>= int(st) and int(ch)<=int(en):
#                     visitedSites.append({str(i[0]).split('+')[0].split(" ")[1]:str(i[1])})
#         except:
#             pass

#     data.update({"visitedSites":visitedSites})
#     print("visitedweb---",data)

#     url = "https://timedoctor.niraginfotech.com/api/user/add/tracking/website"

#     data = {"trackingId": "63218c5b986ac3839b5f2355", "visitedSites":[
#             {
#             "time": "19:20",
#             "website": "https://v1.hdfcbank.com"
#             },
#             {
#             "time": "19:30",
#             "website": "https://youtube.com"
#             },
#             {
#             "time": "19:40",
#             "website": "https://youtube.com"
#             }
#         ]}
#     payload = json.dumps(data)
#     headers = {
#       'Authorization': 'Bearer '+token,
#       'Content-Type': 'application/json'
#     }

#     response = requests.post(url, headers=headers, data=payload)

#     print(response.text)


def sendscreenshot():
    old= open('data.json', 'r').read()
    old=json.loads(old)
    for i in old:
        trackid=old['trackid']
        token=old['token']
        print(token)
        print(trackid)
    url = "https://timedoctor.niraginfotech.com/api/user/send/screenshot"

    payload={'trackedTimeId': "63218c5b986ac3839b5f2355",
    'trackingScreenShotStartTime': "08:00:00",
    'trackingScreenShotEndTime': "19:00:00",
    'mouseActivity': "100",
    'keywordActivity': "100",
    'activityLevel': '10',
    'visitedWebsites': '[{}]'}
    files=[
      ('image',('test.png',"file+name=",'image/png'))
    ]
    headers = {
      'Authorization': 'Bearer '+token
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)

print(sendscreenshot())