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



eel.init("web")  
  
# Exposing the random_python function to javascript
@eel.expose    
def random_python():
    print("Random function running")
    return randint(1,100)



@eel.expose    
def random_login(email,password):
    final={}

    print(email,"emailllllllll")
    print(password,"passwordssssss")
    print("Random function running")


    url = "https://timedoctor.niraginfotech.com/api/user/login"

    payload = json.dumps({
      # "email": "amit@gmail.com",
      # "password": "amit@1234"
      "email": email,
      "password": password
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json())
    data=response.json()
    check=data['success']
    checks=data['token']
    final.update({"token":checks,"trackid":"-","date":"-"})
    if check==True:
        json_object = json.dumps(final, indent=1)
     
        # Writing to sample.json
        with open("data.json", "w") as outfile:
            outfile.write(json_object)
        done="success"
        return done
    else:
        done="error"
        return done


@eel.expose
def write_feature():
    print("started")

    # strat time and tracking id get karne vala code...............
    today = datetime.now()
    newdate = today.strftime("%d/%m/%Y")
    olddate=""
    old= open('data.json', 'r').read()
    old=json.loads(old)
    for i in old:
        token=old['token']
        olddate=old['date']
    if olddate!=newdate:
        print("nhi mili")
        url = "https://timedoctor.niraginfotech.com/api/user/start/tracking/time"
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print("tracking current_time",current_time)
        payload = json.dumps({
          "projectName": "ss",
          "actualStartTimeOfTheShift": str(current_time)
        })
        headers = {
          'Authorization': 'Bearer '+token,
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        print(current_time)

        data=response.json()
        trackid=data['data']['_id']
        today = datetime.now()
        date = today.strftime("%d/%m/%Y")

        # json_object = json.dumps(data, indent=3)
        old= open('data.json', 'r').read()
        old=json.loads(old)
        old.update({"trackid":trackid,"date":date})
        json_object = json.dumps(old, indent=2)

        # Writing to sample.json
        with open("data.json", "w") as outfile:
            outfile.write(json_object)

    # start time or tracing id vala code khatam

    #track id and token fetch karne ka code

    old= open('data.json', 'r').read()
    old=json.loads(old)
    for i in old:
        trackid=old['trackid']
        token=old['token']
        print(token)
        print(trackid)

    while True:

        from pynput.keyboard import Key, Listener
        from pynput.mouse import Listener
        try:
            listener.stop()
            key_listener.stop()
        except:
            pass
        mouse_click=[]
        key_press=[]
        def on_click(x, y, button, pressed):
            if pressed:
                print("Mouse clicked.")
                mouse_click.append("clicked")
                return "done"
            
        from pynput import mouse
        listener= mouse.Listener(on_click=on_click)
        listener.start()

        def on_press(key):
            print("key is pressed")
            key_press.append("Key_pressed")
            return "done"

        from pynput import keyboard
        key_listener = keyboard.Listener(on_press=on_press)
        key_listener.start()

        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        
        img = Image.fromarray(image)
        out_img = BytesIO()
        img.save(out_img, format='png')
        out_img.seek(0)

        #phela ka time
        now = datetime.now()
        start_time = now.strftime("%H:%M")
        print(start_time,"start_timestart_time")

        time.sleep(60)

        #bad ka time

        now = datetime.now()
        end_time = now.strftime("%H:%M")
        print(end_time,"end_timeend_timeend_time")


        if stop == 1:
            break

        # keyboard and mouse press bejne ka code
        body=out_img.getvalue()
        cll=len(mouse_click)
        kss=len(key_press)

        url = "https://timedoctor.niraginfotech.com/api/user/send/screenshot"

        payload={'trackedTimeId': trackid,
        'trackingScreenShotStartTime': str(start_time),
        'trackingScreenShotEndTime': str(end_time),
        'mouseActivity': cll,
        'keywordActivity': kss,
        'activityLevel': '10',
        'visitedWebsites': '[{}]'}
        files=[
          ('image',('test.png',body,'image/png'))
        ]
        headers = {
          'Authorization': 'Bearer '+token
        }

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        print(response.text)

        #keyboad mouse and file send karne ka code khatam




        key_board={"keys Pressed":len(key_press)}
        #mouse
        print(key_board,"key_board")

        mouse_event={"Mouse Clicks":len(mouse_click)}
        print(mouse_event,"mouse_event")


        mouse_click=[]
        key_press=[]
        listener.stop()
        key_listener.stop()

    listener.stop()
    key_listener.stop()
           

        # return done

@eel.expose
def start_thread():
        # Assign global variable and initialize value
        global stop
        stop = 0
        # Create and launch a thread 
        t = Thread (target = write_feature)
        t.start()

@eel.expose
def stop():
    global stop
    stop = 1

  


# Start the index.html file
eel.start("traker-login.html")



