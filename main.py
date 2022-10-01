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
from dateutil import tz
import logging
from datetime import timedelta


from_zone = tz.tzutc()
to_zone = tz.tzlocal()

global stop_call

def close_callback(route, websockets):
    try:
        if not websockets:
            print('Bye!')
            exit()
    except:
        s.close()


#get local time function

def local_time(shiftStartAt, shiftEndAt):
    now = datetime.now()
    start_time = now.strftime("%Y-%m-%d %H:%M:%S")
    shiftStartAt =shiftStartAt.replace("T"," ")
    shiftEndAt =shiftEndAt.replace("T"," ")


    shiftStartAt = shiftStartAt.split('.')[0]
    shiftEndAt = shiftEndAt.split('.')[0]
    format  = "%Y-%m-%d %H:%M:%S"

    shiftStartAt = datetime.strptime(shiftStartAt, format)
    shiftEndAt = datetime.strptime(shiftEndAt, format)

    shiftStartAt = shiftStartAt.replace(tzinfo=from_zone)
    shiftEndAt = shiftEndAt.replace(tzinfo=from_zone)

    shiftStartAt = shiftStartAt.astimezone(to_zone)
    shiftEndAt = shiftEndAt.astimezone(to_zone)
    data={
        "shiftStartAt":shiftStartAt,
        "shiftEndAt":shiftEndAt
    }
    return data


def main():
    olddate=""
    trackid=""
    token=""
    old= open('data.json', 'r').read()
    old=json.loads(old)
    for i in old:
        shiftStartAt=old['shiftStartAt']
        shiftEndAt=old['shiftEndAt']

    now = datetime.now()
    current_time =now.strftime("%Y-%m-%d %H:%M:%S")
    time = local_time(shiftStartAt,shiftEndAt)
    start_time = time['shiftStartAt']
    end_time = time['shiftEndAt']


    if str(current_time) >= str(start_time):
        shift_start = Thread (target = start_thread)
        shift_start.start()

    if str(current_time) >= str(end_time):
        shift_end=  Thread (target = stop)
        shift_end.stop()

# get path Automatically
basedir = os.path.dirname(os.path.abspath(__file__))
categorization_file = os.path.join(basedir,'/web')
eel.init('web')
 
idlsttm=""

# Exposing the random_python function to javascript
@eel.expose    
def visitedweb():
    old= open('data.json', 'r').read()
    old=json.loads(old)
    for i in old:
        trackid=old['trackid']
        token=old['token']
        shiftStartAt=old['shiftStartAt']
        shiftEndAt=old['shiftEndAt']

    outputs = get_history()
    his = outputs.histories
    current_time = datetime.now()
    current_time=current_time.date().strftime('%y-%m-%d')
    shiftStartAt=shiftStartAt
    shiftEndAt=shiftEndAt
    z=0
    data={}
    data.update({"trackingId":trackid})
    visitedSites=[]
    for i in his:
        try:
            if str(current_time) in str(i[0]):
                ch=str(i[0]).split(':')[0]
                st=shiftStartAt.replace("T"," ")
                en=shiftEndAt.replace("T"," ")
                st = st.split(':')[0]
                en = st.split(':')[0]
                print(en,st)
                if str(ch) >= str(st) or str(ch) <=str (en):
                    visitedSites.append({"time":str(i[0]).split('+')[0],
                                        "url":str(i[1])})
        except:
            pass
    visitedSites = json.dumps(visitedSites)
    data.update({"visitedSites":visitedSites})

    url = "https://timedoctor.niraginfotech.com/api/user/add/tracking/website"
    payload = json.dumps(data)
    headers = {
      'Authorization': 'Bearer '+token,
      'Content-Type': 'application/json'
    }

    try:
        response = requests.request('POST',url, headers=headers, data=payload)
    except requests.exceptions.ConnectionError:
        # 👇️ handle error here or use a `pass` statement
        print('connection error occurred')
        visitedweb()
    print("++++++++++++++++++++++++++++++++++++++++++++++ visitedweb +++++++++++++++++++++++++++++++++++++++++++++++++++")



@eel.expose    
def random_python():
    print("Random function running")
    return randint(1,100)

@eel.expose
def take_screenshot(res):
    if res == "done":
        eel.say_hello_js(res)
        pass
    else:
        res = "error"
        eel.say_hello_js(res)
        
# eel.start('traker.html')



@eel.expose
def sendscreenshot(start_time,end_time,cll,kss,body):
    print("++++++++++++++++++++++++++++++++++ screeen short working ++++++++++++++++++++++++++++++++++")
    old= open('data.json', 'r').read()
    old=json.loads(old)
    for i in old:
        trackid=old['trackid']
        token=old['token']
        shiftStartAt=old['shiftStartAt']
        shiftEndAt=old['shiftEndAt']
    url = "https://timedoctor.niraginfotech.com/api/user/send/screenshot"

    outputs = get_history()
    his = outputs.histories
    current_times = datetime.now()
    current_times=current_times.date().strftime('%y-%m-%d')
    shiftStartAt=shiftStartAt
    shiftEndAt=shiftEndAt
    z=0
    visitedSites=[]
    for i in his:
        try:
            if str(current_times) in str(i[0]):
                ch=str(i[0]).split(':')[0]
                st=shiftStartAt.replace("T"," ")
                en=shiftEndAt.replace("T"," ")
                st = st.split(':')[0]
                en = st.split(':')[0]
                print(en,st)
                if str(ch) >= str(st) or str(ch) <=str (en):
                    visitedSites.append({str(i[0]).split('+')[0]:str(i[1])})
        except:
            pass
    payload={'trackedTimeId': trackid,
    'trackingScreenShotStartTime': str(start_time),
    'trackingScreenShotEndTime': str(end_time),
    'mouseActivity': cll,
    'keywordActivity': kss,
    'activityLevel': '10',
    'visitedWebsites': visitedSites
    }
    files=[
      ('image',('test.png',body,'image/png'))
    ]
    headers = {
      'Authorization': 'Bearer '+token
    }
    # print("--------------- screent short",files)
    try:
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        data = response.json()
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",data)
        if files:
            res = "done"
            td = Thread (target = take_screenshot(res))
            td.start()  
    except requests.ConnectionError as e:
        print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
        print(str(e))   
        sendscreenshot(start_time,end_time,cll,kss,body)         
    except requests.Timeout as e:
        print("OOPS!! Timeout Error")
        print(str(e))
        sendscreenshot(start_time,end_time,cll,kss,body)
    print("+++++++++++++++++++++++++++++++++++++++++++++++ screenshot +++++++++++++++++++++++++++++++++++++++++++++++")


@eel.expose    
def random_login(email,password):
    # try:
    final={}
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

    response = requests.post(url, headers=headers, data=payload)
    data=response.json()

    if email == "" and password == "":
        done="email & password"
        return done

    elif email == "":
        done="email"
        return done

    elif password == "":
        done="password"
        return done
    else:

        try:
            if data['success'] == False:
                if  data['msg'] == "Email or Password is Incorrect":
                    done = data['msg']
                    return done
        except:
            if  data['errors']:
                done = "Email is Invalid"
                return done
        else:
            now = datetime.now()
            current_time =now.strftime("%Y-%m-%d %H:%M:%S")
            check=data['success']
            checks=data['token']
            shiftStartAt=data['user']['shiftStartAt']
            shiftEndAt=data['user']['shiftEndAt']
            time = local_time(shiftStartAt,shiftEndAt)
            start_time = time['shiftStartAt']
            end_time = time['shiftEndAt']
            # end_time = 
            breakTime = data['user']['breakTime']
            screenshotInterval =  data['user']['screenshotInterval']
            idealTimeInterval =   data['user']['idealTimeInterval']
            print(str(current_time))
            print(str(start_time))
            print(str(shiftEndAt))
            if str(current_time) <= str(start_time) :
                done="Your shift is not started"
                return done
            elif str(current_time) >= str(end_time) :
                done= "Your shift is ended"
            final.update({"token":checks,"trackid":"-","date":"-","start_time":str(start_time),"end_time":str(end_time),"shiftStartAt":shiftStartAt,"shiftEndAt":shiftEndAt,"break":breakTime,
                            "screenshotInterval":screenshotInterval,"idealTimeInterval":idealTimeInterval})
            if check==True:
                json_object = json.dumps(final, indent=1)
            
                # Writing to sample.json
                with open("data.json", "w") as outfile:
                    outfile.write(json_object)
                done="success"

                try:
                    value = main()
                except:
                    pass
                return done
            else:
                done="error"
                return done

@eel.expose
def breakend():
    now = datetime.now()
    current_time =now.strftime("%H:%M:%S")
    trackid=""
    token=""
    old= open('data.json', 'r').read()
    old=json.loads(old)
    for i in old:
        token=old['token']

        olddate=old['date']
        br=old['break']
        trackid=old['trackid']
        start_time = old ['start_time']
        end_time = old ['end_time']


    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    end_time =  end_time.split(" ")[1]
    end_time = end_time.split('+')[0]
    end_time = datetime.strptime(end_time, "%H:%M:%S") - timedelta(hours=1, minutes=0)
    end_time = end_time.strftime("%H:%M:%S")

    if current_time >= end_time:
        msg = "end"
        time = cant_take_break_1_hour(msg)
        return msg

    url = "https://timedoctor.niraginfotech.com/api/user/break/tracking/time/end"

    payload = json.dumps({
      "breakTimeEndsAt": current_time,
      "trackedTimeId": trackid
    })
    headers = {
      'Authorization': 'Bearer '+token,
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print("+++++++++++++++++++++++++++++++++++++++ breakend +++++++++++++++++++++++++++++++++++")
    print(response)

    old= open('data.json', 'r').read()
    old=json.loads(old)
    old.update({"break":"-"})
    json_object = json.dumps(old, indent=1)
    # Writing to sample.json
    with open("data.json", "w") as outfile:
        outfile.write(json_object)

# @eel.expose
# def popup():
#     print("go")



@eel.expose
def shiftstart():
    url = "https://timedoctor.niraginfotech.com/api/user/start/tracking/time"
    now = datetime.now()
    current_time =now.strftime("%Y-%m-%d %H:%M:%S")
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

@eel.expose
def get_mouse_and_keyboard_movement(key_press,mouse_click):
    print("@@@@@@@@@@@@@@@@@@@ click getting from new function keyboard",key_press)
    print("@@@@@@@@@@@@@@@@@@@ click getting from new function mouse click",mouse_click)
    
    if ((key_press == 0 ) and (mouse_click == 0 )):
        print("+++++++ in main if ockntin------------------")
        eel.get_timer_js(key_press,mouse_click)
        print("++++++ funtion run successfully")
        
        
        # return True
    # return False


@eel.expose
def cant_take_break_1_hour(msg):
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++ user cannot take break 1 hour before and after")
    eel.one_hour_break(msg)
        
        # return True
    # return False

@eel.expose
def write_feature():
    print("started")

    # strat time and tracking id get karne vala code...............
    today = datetime.now()
    newdate = today.strftime("%d/%m/%Y")
    olddate=""
    trackid=""
    token=""
    old= open('data.json', 'r').read()
    old=json.loads(old)
    for i in old:
        token=old['token']
        olddate=old['date']
        br=old['break']
        trackid=old['trackid']
        screenshotTime =old['screenshotInterval']
        idealTimeInterval =old['idealTimeInterval']

    if br=="true":
        # break end thread
        t = Thread (target = breakend)
        t.start()


    # url = "https://timedoctor.niraginfotech.com/api/user/getUserSettings"
    # payload = ""
    # headers = {
    #   'Authorization': 'Bearer '+token,
    # }
    # response = requests.request("GET", url, headers=headers, data=payload)
    # idldata=response.json()
    # idealTimeIntervalInMinutes=idldata['userSetting']['idealTimeInterval']
    # screenshotTimeIntervalInMinutes=idldata['userSetting']['screenshotInterval'] 
    try:
        idealTimeIntervalInMinutes= int(idealTimeInterval)
    except:
        idealTimeIntervalInMinutes = 1
    try:
        screenshotTimeIntervalInMinutes= int(screenshotTime)
    except:
        screenshotTimeIntervalInMinutes = 1


    if olddate!=newdate:
        td = Thread (target = shiftstart)
        td.start()

    #track id and token fetch karne ka code

 
    checkidtm=0
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

        

        #phela ka time
        now = datetime.now()
        start_time = now.strftime("%Y-%m-%d %H:%M:%S")
        print(start_time,"start_timestart_time")

        for idls in range(1,screenshotTimeIntervalInMinutes+1):
            screenshotTimesleep = screenshotTimeIntervalInMinutes*60
            time.sleep(screenshotTimesleep)
        

        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        
        img = Image.fromarray(image)
        out_img = BytesIO()
        img.save(out_img, format='png')
        out_img.seek(0)
        if len(mouse_click)==0 and len(key_press) ==0:
            checkidtm=checkidtm+1
            if checkidtm==idealTimeIntervalInMinutes:
                nows = datetime.now()
                start_times = now.strftime("%H:%M")
                bb=start_times.split(":")[0]
                cc=start_times.split(":")[1]

                if cc !="00":
                    cc=int(cc)-checkidtm
                    start_times=str(bb)+":"+str(cc)
                global idlsttm
                idlsttm=start_times
                print(idlsttm,"ideal time started")
                t3 = Thread (target = popup())
                t3.start()


        else:
            checkidtm=0

        if stop == 1:
            break

        # keyboard and mouse press bejne ka code
        body=out_img.getvalue()
        cll=len(mouse_click)
        kss=len(key_press)

        now = datetime.now()
        end_time = now.strftime("%Y-%m-%d %H:%M:%S")
        print(end_time,"end_timeend_timeend_time")

        t = Thread (target = sendscreenshot(start_time,end_time,cll,kss,body))
        t.start()

        t1 = Thread (target = visitedweb())
        t1.start()

        #keyboad mouse and file send karne ka code khatam


        key_board={"keys Pressed":len(key_press)}
        #mouse
        mouse_event={"Mouse Clicks":len(mouse_click)}
        
        actual_ideal_start_time = []


        if (len(key_press) == 0 ) and (len(mouse_click) == 0):
            mouse_key = Thread( target = get_mouse_and_keyboard_movement(len(key_press),len(mouse_click)))
            # print("--------------------- function return value",mouse_key)

            timer=int(48000)
            while (timer != 0 ):
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                if len(actual_ideal_start_time) == 0:
                    actual_ideal_start_time.append(current_time)
                    print("++++++++++++++++++++++actual_ideal_start_time",actual_ideal_start_time)
                else:
                    print("++++++++++++++++++++++elsepass")
                    pass

                if (len(key_press) >= 1 ) or (len(mouse_click) >= 1):
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    actual_ideal_end_time = current_time
                    break

                timer=timer-1
                
                # actual_ideal_time = timers
                time.sleep(1)
                print("++++++++++++++++++++++++++++++++++ no movement timer",timer)
        else:
            print("i am working now")

        try:
            old= open('data.json', 'r').read()
            old=json.loads(old)
            for i in old:
                token=old['token']
                trackid=old['trackid']

            url = "https://timedoctor.niraginfotech.com/api/user/ideal/tracking/time"
            payload = json.dumps({
            "idealTimeStartAt": str(actual_ideal_start_time[0]),
            "trackedTimeId": trackid,
            "idealTimeEndsAt":str(actual_ideal_end_time)
            })
            headers = {
            'Authorization': 'Bearer '+token,
            "Content-Type": "application/json; charset=utf-8"
            }
            response =  requests.request("POST",url, headers=headers, json=payload)
            print("++++++++++++++++++++++++++++++++++++++++++++++++ Ideal Time Sent Successfully",response)
            print("+++++++++++++++++++++++++++++++++++++++++actual_ideal_time",actual_ideal_start_time[0])
            print("+++++++++++++++++++++++++++++++++++++++++actual_ideal_time",actual_ideal_end_time)
        except:
            pass
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
    shiftStartAt=""
    shiftEndAt=""
    old= open('data.json', 'r').read()
    old=json.loads(old)
    for i in old:
        shiftStartAt=old['shiftStartAt']
        shiftEndAt=old['shiftEndAt']
        token=old['token']
        trackid=old['trackid']

    url = "https://timedoctor.niraginfotech.com/api/user/start/end/time"

    payload={}
    headers = {
      'Authorization': 'Bearer '+token,
      "Content-Type": "application/json; charset=utf-8"
    }

    response = requests.get(url, headers=headers, json=payload)
    df=response.json()
    shiftStartAt=df['data']['shiftStartAt']
    shiftEndAt=df['data']['shiftEndAt']

    old= open('data.json', 'r').read()
    old=json.loads(old)
    old.update({"shiftEndAt":shiftEndAt,"shiftEndAt":shiftEndAt})
    json_object = json.dumps(old, indent=1)
    # Writing to sample.json
    with open("data.json", "w") as outfile:
        outfile.write(json_object)

    
    # shiftStartAt="17:00"
    # shiftEndAt="20:00"

    now = datetime.now()
    start_time = now.strftime("%Y-%m-%d %H:%M:%S")
    shiftStartAt =shiftStartAt.replace("T"," ")
    shiftEndAt =shiftEndAt.replace("T"," ")

    shiftStartAt = shiftStartAt.split('.')[0]
    shiftEndAt = shiftEndAt.split('.')[0]
    format  = "%Y-%m-%d %H:%M:%S"

    shiftStartAt = datetime.strptime(shiftStartAt, format)
    shiftEndAt = datetime.strptime(shiftEndAt, format)

    shiftStartAt = shiftStartAt.replace(tzinfo=from_zone)
    shiftEndAt = shiftEndAt.replace(tzinfo=from_zone)

    shiftStartAt = shiftStartAt.astimezone(to_zone)
    shiftEndAt = shiftEndAt.astimezone(to_zone)
    st= str(shiftStartAt)
    nd= str(shiftEndAt)
    n0= str(start_time)

    # if start_time>=st and start_time<nd:
    if start_time:
        global stop
        stop = 0
        # Create and launch a thread 
        t = Thread (target = write_feature)
        t.start()
    else:
        return "error"
        


@eel.expose
def breakstart():
    now = datetime.now()
    start_time = now.strftime("%H:%M:%S")
    trackid=""
    token=""
    old= open('data.json', 'r').read()
    old=json.loads(old)
    for i in old:
        token=old['token']
        trackid=old['trackid']
        shiftEndAt=old['shiftEndAt']
        shiftStartAt = old['shiftStartAt']
        start_time=old['start_time']
        end_time = old['end_time']

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    start_time =  start_time.split(" ")[1]
    start_time = start_time.split('+')[0]
    start_time = datetime.strptime(start_time, "%H:%M:%S") + timedelta(hours=1, minutes=0)
    start_time = start_time.strftime("%H:%M:%S")

    print(start_time)
    print(current_time)

    if current_time <= start_time:
        msg = "start"
        time = cant_take_break_1_hour(msg)
        return msg

    print("sucess")

    url = "https://timedoctor.niraginfotech.com/api/user/break/tracking/time/start"

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++",start_time)
    payload = json.dumps({
      "breakTimeStartAt": start_time,
      "trackedTimeId": trackid
    })
    headers = {
      'Authorization': 'Bearer '+token,
      'Content-Type': 'application/json'
    }


    response = requests.post(url, headers=headers, data=payload)
    print("+++++++++++++++++++++++++++++++++++breakstart++++++++++++++++++++++++++++++=",response)
    stop = 1


@eel.expose
def stop():
    trackid=""
    token=""
    done=""
    shiftStartAt=""
    shiftEndAt=""
    old= open('data.json', 'r').read()
    old=json.loads(old)
    for i in old:
        token=old['token']
        trackid=old['trackid']
        shiftStartAt=old['shiftStartAt']
        shiftEndAt=old['shiftEndAt']
        start_times=old['start_time']
        end_time = old['end_time']

    now = datetime.now()
    start_time = now.strftime("%Y-%m-%d %H:%M:%S")

    st= str(start_times)
    nd= str(end_time)
    n0= str(start_time)


    if n0==st or n0==nd and n0>=st and n0<=nd:
        done="noo"
        return done

    else:
        if n0>=st and n0<=nd:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Break started +++++++++++++++++++++++++++++++++++++++++++++++")
            t = Thread (target = breakstart)
            t.start()

            old= open('data.json', 'r').read()
            old=json.loads(old)
            old.update({"break":"true"})
            json_object = json.dumps(old, indent=1)
            # Writing to sample.json
            with open("data.json", "w") as outfile:
                outfile.write(json_object)
            return done
        else:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Break not started +++++++++++++++++++++++++++++++++++++++++++++++")
            done="not"
            # t = Thread (target = breakstart)
            # t.start()
            return done


@eel.expose
def logout():
    final={}
    final.update({"token":"-","trackid":"-","date":"-","break":"-","start_time":"-","end_time":"-"})
    json_object = json.dumps(final, indent=1)
 
    # Writing to sample.json
    with open("data.json", "w") as outfile:
        outfile.write(json_object)
    done="success"
    return done

@eel.expose
def breaktimeleft():
    try:
        now = datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M:%S")
        old= open('data.json', 'r').read()
        old=json.loads(old)
        for i in old:
            token=old['token']
            trackid=old['trackid']

        url = "https://timedoctor.niraginfotech.com/api/user/break/tracking/time/check"

        payload = json.dumps({
          "trackingId": trackid,
          "checkTime": time
        })
        headers = {
          'Authorization': 'Bearer '+token,
          'Content-Type': 'application/json'
        }
        print("++++++++++++++++++++++++++++++++++++++++++++ breaktimeleft +++++++++++++++++++++++++++++++++++++++++")

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

        dd=response.json()
        print("+++++++++++++++++++++++++++++++++++++++++==dd",dd)

        tleft=dd['minsLeft']

        print(tleft,type(tleft))

        if tleft==None:
            tleft="00"

        return tleft
    except:
        tleft="00"
        return tleft


@eel.expose
def reset_password(rest_mail):
    print("++++++++++++++++ email value here",rest_mail)
    old= open('data.json', 'r').read()
    old=json.loads(old)
    for i in old:
        token=old['token']
    url = "https://timedoctor.niraginfotech.com/api/user/reset-password"
    
    payload = json.dumps({
          "email": str(rest_mail),
        })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    json_response=response
    return json_response



@eel.expose
def cwwd():
    old= open('data.json', 'r').read()
    old=json.loads(old)
    for i in old:
        token=old['token']
    return str(token)

try:
    old= open('data.json', 'r').read()
    old=json.loads(old)
    for i in old:
        token=old['token']
except:
    eel.start('traker-login.html',size=(580, 490),
        position=(1000,1000), port=1111,
                        cmdline_args=[
                                '--incognito'])

# if len(token)>2:
#     eel.show("script.html")
# else:
#     pass

if len(token)>2:
    eel.start('traker.html',size=(570, 410), 
                position=(1000,1000), port=1111,
                cmdline_args=[
                                '--incognito']

                )
else:
    eel.start('traker-login.html',size=(580, 490), 
                position=(1000,1000), port=1111,
                cmdline_args=[
                                '--incognito']
                )



# Start the index.html file

    
    
     
