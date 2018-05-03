#!/usr/bin/python
# coding:utf-8

import os
import sys
import argparse
import subprocess
from datetime import datetime
import time

# date


def getDate(format='%Y-%m-%d %H:%M:%S'):
    date_object = datetime.now()
    current_time = date_object.strftime(format)
    return current_time

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
    setClipboardData(getDate())

# file info


def getFileInfo(path):
    mtime = os.path.getmtime(path)
    print(formatTimestamp(mtime))
    print(os.stat(path))
    print(formatTimestamp(os.stat(path).st_atime))
    print(formatTimestamp(os.stat(path).st_mtime))
    print(formatTimestamp(os.stat(path).st_ctime))


def newDraft(filename):
    arr = filename.split()
    filename = '-'.join(arr)
    filename = './_drafts/' + filename + '.md'
    try:
        file = open(filename, 'w')   # Trying to create a new file or open one
        file.write("""---
layout: post
title:  "title"
excerpt: >-
    excerpt
comments: true
---

""")
        file.close()
        print('create '+filename)
    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0)  # quit Python

# format timestamp


def formatTimestamp(timestamp):
    print(timestamp)
    time_local = time.localtime(timestamp)
    # 转换成新的时间格式(2016-05-05 20:28:54)
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
        'savedate': saveCurrentTimeToCp,
        'fileinfo': getFileInfo,
        'newdraft': newDraft
    }
    if states.has_key(case):
        if extra is not None:
            states[case](extra)
        else:
            states[case]()

    else:
        print('no key:' + case)


switch(args['type'], args['extra'])
