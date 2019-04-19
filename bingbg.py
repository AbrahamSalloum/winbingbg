# Abraham Salloum - scrapes Bing image of the day, makes bg
import ctypes
import re
import urllib.request
import os
from PIL import Image

SPI_SETDESKWALLPAPER = 0x14
SPIF_UPDATEINIFILE = 0x1
SPIF_SENDWININICHANGE = 0x2

index = urllib.request.urlopen("https://www.bing.com/").read() # downlaod index.html from bing.com 
imgmatch = re.search(r'<link id="bgLink" rel="preload" href="\/(.+\.jpg)(?=\&amp;rf=)', index.decode('utf-8')) #regex to match img 
filename = imgmatch.group(1) #extract img path from file

imgfile = re.search(r'th\?id=(.*.jpg)', imgmatch.group(1)) #regex to extract file name
bmpimg = imgfile.group(1)+".bmp" #we will convert file to bmp (for win7 compatibility), so rename now

if os.path.isfile(bmpimg) is not True: # if file already exists in fs, don't redownload
    urllib.request.urlretrieve("https://www.bing.com/"+filename,bmpimg)

imgpath = os.getcwd()+ "\\" + bmpimg #local path to file
im = Image.open(imgpath) # open file
bmpimg = im.save(imgpath, "bmp") #convert and save to bmp
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imgpath, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE) #set bg 
