import ctypes
import re
import urllib
import os 
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
filename = re.search(r'[A-Z0-9a-z\-\_]*.jpg',imgmatch.group(0))

if os.path.isfile(filename.group(0)) is not True:
    bingindex.retrieve("http://www.bing.com/"+imgmatch.group(0),filename.group(0))

imgpath = os.getcwd()+"\\" +  filename.group(0)
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, imgpath, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
