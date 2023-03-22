import os
import random
import datetime as dt
from time import sleep

#################################################
#               Basic Config                    #

path_wallpaperFolder = "Pictures/wallpapers"
time = 10

#################################################
allWall = []
username = os.getlogin()
default = f"/home/{username}"
configured_path = default + "/" + path_wallpaperFolder + "/"

for (dirpath, dirnames, filenames) in os.walk(configured_path):
  allWall.extend(filenames)
  break

def setWall():
    while True:
        n = random.randint(0,len(allWall)-1)
        os.system(f"feh --bg-scale {default}/{path_wallpaperFolder}/{allWall[n]}")
        sleep(time)

#print(allWall)
#print(default)
#print(f"{default}/{path_wallpaperFolder}/")
#print(configured_path)

setWall()
