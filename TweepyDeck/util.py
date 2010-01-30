#!/usr/bin/env python
from __future__ import with_statement

import os
import sys
import time
import urllib2

def __global_prefix(key):
    return '_TweepyDeck_%s' % key

def set_global(key, value):
    setattr(sys, __global_prefix(key), value)
def get_global(key):
    return getattr(sys, __global_prefix(key), None)

def readable_time():
    return time.strftime('%H:%M:%S', time.localtime())

def cachedImagePath(who):
    return '/tmp/tweepydeck_%s.png' % who

def saveImageToFile(who, img_url):
    img = cachedImagePath(who)
    if os.path.exists(img):
        return img

    try:
        web_fd = urllib2.urlopen(img_url)
        data = web_fd.read()
        web_fd.close()
    except urllib2.HTTPError:
        # Damnits.
        return

    if not data:
        return

    with open(img, 'w') as fd:
        fd.write(data)
    return img
