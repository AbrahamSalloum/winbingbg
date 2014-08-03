import ctypes
import re
import urllib
import os
import time
filename = str(int(time.time()))+".jpg"; 
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

bingindex.retrieve("http://www.bing.com/"+imgmatch.group(0),filename)
imgpath = os.getcwd()+"\\" +  filename 
print ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, imgpath, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
