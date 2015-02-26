#!/opt/local/bin/python2.7
import glob
import random
import subprocess
import re
import urllib
import os
import string
 
from AppKit import NSWorkspace, NSScreen
from Foundation import NSURL

bingindex = urllib.URLopener()
bingindex.retrieve("http://www.bing.com/", "index")
index =open('index','r')
for line in index:
    imgmatch = re.search(r'\/az\/hprichbg\/[\w\d\/\_\-]*.jpg', line)
    if imgmatch:
        break
    
filenameReg = re.search(r'[A-Z0-9a-z\-\_]*.jpg',imgmatch.group(0))
filepath = string.replace(imgmatch.group(0), "1366x768", "1920x1080", 1)
filename = string.replace(filenameReg.group(0), "1366x768", "1920x1080", 1)
if os.path.isfile(filename) is not True:
    bingindex.retrieve("http://www.bing.com/"+filepath,filename)

 
macbingbg = glob.glob(filename)
filepath = random.choice(macbingbg)
imgurl = NSURL.fileURLWithPath_(filepath)
options = {}
ws = NSWorkspace.sharedWorkspace()
for screen in NSScreen.screens():
    (result, error) = ws.setDesktopImageURL_forScreen_options_error_(
                imgurl, screen, options, None)
