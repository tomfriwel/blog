#!/usr/bin/python
# coding:utf-8

import subprocess
from datetime import datetime


def getClipboardData():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

def setClipboardData(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()

def saveCurrentTimeToCp():
    date_object = datetime.now()
    current_time = date_object.strftime('%Y-%m-%d %H:%M:%S')
    setClipboardData(current_time)

saveCurrentTimeToCp()

