#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import subprocess
from threading import Thread
from datetime import datetime

def sendmessage():
    trackid=""
    token=""
    old= open('data.json', 'r').read()
    old=json.loads(old)
    for i in old:
        shiftEndAt=old['shiftEndAt']
        shiftStartAt = old['shiftStartAt']
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    shiftStartAt =shiftStartAt.replace("T"," ")
    shiftEndAt =shiftEndAt.replace("T"," ")

    shiftStartAt = shiftStartAt.split('.')[0]
    shiftEndAt = shiftEndAt.split('.')[0]

    if current_time >= shiftStartAt:
        shift_start = Thread (target = shiftstart)
        shift_start.start()

    if current_time >= shiftEndAt:
        shift_end=  Thread (target = stop)
        shift_end.start()

	subprocess.Popen(['notify-send', message])
	return

if __name__ == '__main__':
	sendmessage()


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


    if current_time >= start_time:
        shift_start = Thread (target = shiftstart)
        shift_start.start()

    if current_time >= end_time:
        shift_end=  Thread (target = stop)
        shift_end.stop()