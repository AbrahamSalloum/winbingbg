import ctypes
import re
import urllib
import os
import string
SPI_SETDESKWALLPAPER = 0x14
SPIF_UPDATEINIFILE = 0x1
SPIF_SENDWININICHANGE = 0x2
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

imgpath = os.getcwd()+"\\" +  filename
print imgpath
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, imgpath, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
