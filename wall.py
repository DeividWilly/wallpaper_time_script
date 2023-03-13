import os
import datetime as dt
from time import sleep

################################################
#               Basic Config                   #

path_wallpaperFolder = ""
# it is not necessary to write since /home, only the normal path from ~ #

midnight = ""
morning = ""
afternoon = ""
night = ""
################################################
allWall = [midnight, morning, afternoon, night]
username = os.getlogin()
default = f"/home/{username}"

def thisPathExist(pathWallpaperFolder):
    path = f"{default}/{pathWallpaperFolder}"
    pathExist = os.path.exists(path)
    return pathExist

def gethour():
    hours = dt.datetime.now().hour
    return hours

def setWall():
    while True:
        hour = int(gethour())

        if (hour >= 0 and hour < 5):
            os.system(f"feh --bg-scale {default}/{path_wallpaperFolder}/{allWall[0]}")
            print(f"Hour: {hour}, changed to {allWall[0]}")

        if (hour >= 5 and hour < 12):
            os.system(f"feh --bg-scale {default}/{path_wallpaperFolder}/{allWall[1]}")
            print(f"Hour: {hour}, changed to {allWall[1]}")

        if (hour >= 12 and hour < 18):
            os.system(f"feh --bg-scale {default}/{path_wallpaperFolder}/{allWall[2]}")
            print(f"Hour: {hour}, changed to {allWall[2]}")

        if (hour >= 18):
            os.system(f"feh --bg-scale {default}/{path_wallpaperFolder}/{allWall[3]}")
            print(f"Hour: {hour}, changed to {allWall[3]}")
        sleep(1800) # at 30 minutes

c = thisPathExist(path_wallpaperFolder)
if c == False:
    print("ERROR !\nPROGRAM FINISHED, PLEASE SET CORRECT DIRECTORY IN 'path_wallpaperFolder'")
else:
    setWall()

