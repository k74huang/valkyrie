import os
import json
from subprocess import Popen

from PIL import Image


def handle():

    # set working directory to be the wallpapers folder and list out all the
    # files
    os.chdir("../walls/")
    files = os.listdir(os.getcwd())

    # sort the directory by when the file was last accessed (i.e. when I put
    # the file in the folder)
    files.sort(key=os.path.getatime, reverse=1)

    # open the javascript file
    scriptFile = open("../script.js", "r")
    fileStr = str(scriptFile.read())
    scriptFile.close()

    # Cut out only the wallpaper array from the script file
    walls = fileStr[(fileStr.find("[") + 1):(fileStr.find("]"))]
    walls = walls.replace("\n", "").split(",")

    # get the first wallpaper in the script file's list
    firstWall = walls[0][1:-1]

    newWalls = []

    size = 900, 900

    for file in files:
        print("The most recent file is: " + file)
        if(file != firstWall):
            newWalls.append(file)
            print("found a new wallpaper: " + file + ", generating thumbnail!")
            img = Image.open("../walls/" + file)
            if img.mode != "RGB":
                img = img.convert("RGB")
            img.thumbnail(size)
            img.save("../thumbs/" + file, "JPEG", quality=50)
            print("saving: " + file)
        else:
            break

    for wall in walls:
        wall = wall.strip()
        print("wall: |" + wall)
        if(wall != "" and os.path.isfile("../walls/" + wall[1:-1])):
            newWalls.append(wall[1:-1])
        elif(wall != "" and (not os.path.isfile('../walls/' + wall[1:-1]))):
            print(
                wall[1:-1] + " has been removed as a thumbnail and from the website.")
            os.remove('../thumbs/' + wall[1:-1])

    # open the script.js file for writing and write new info
    scriptFile = open("../script.js", "w")
    scriptFile.write(fileStr[0:(fileStr.find("["))] +
                     str(newWalls) + fileStr[(fileStr.find("]")) + 1:])
    scriptFile.close()

    os.chdir("../utils")
    Popen("gitHelp.bat", cwd=os.getcwd())

if __name__ == "__main__":
    handle()
