#!/usr/bin/python
# coding:utf-8

import os
import argparse
import subprocess
from datetime import datetime
import time

# clipboard
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

# file info

def getFileInfo(path):
    mtime = os.path.getmtime(path)
    print(formatTimestamp(mtime))
    print(os.stat(path))
    print(formatTimestamp(os.stat(path).st_atime))
    print(formatTimestamp(os.stat(path).st_mtime))
    print(formatTimestamp(os.stat(path).st_ctime))

# format timestamp
def formatTimestamp(timestamp):
    print(timestamp)
    time_local = time.localtime(timestamp)
    #转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

    print(dt)

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--type", required=True,
	help="which type")
ap.add_argument("-e", "--extra", required=False,
	help="extra param")
args = vars(ap.parse_args())


def switch(case, extra=None):
    states = {
        'savedate':saveCurrentTimeToCp,
        'fileinfo':getFileInfo
    }
    if states.has_key(case):
        if extra is not None:
             states[case](extra)
        else:
            states[case]()
        
    else:
        print('no key:'+case)

switch(args['type'], args['extra'])
