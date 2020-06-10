import os
import json
import time
import json
from PIL import Image
from subprocess import Popen


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

    if(walls != ""):
        walls = walls.replace("\n", "")
        walls = "[" + walls + "]"
        # print(walls)
        walls = json.loads(walls)
        # get when the last wallpaper was loaded
        prevLoadTime = walls[0].get("added")
        print("prevloadTime: " + str(prevLoadTime))
    else:
        prevLoadTime = 0
        walls = []

    newWalls = []

    size = 1400, 1400

    for file in files:
        print("The most recent file is: " + file +
              " with load time: " + str(os.path.getatime("../walls/" + file)))
        if(os.path.getatime("../walls/" + file) > prevLoadTime):
            newWalls.append(
                {"filename": file, "added": os.path.getatime("../walls/" + file)})
            print("found a new wallpaper: " + file + ", generating thumbnail!")
            img = Image.open("../walls/" + file)
            if img.mode != "RGB":
                img = img.convert("RGB")

            width, height = img.size   # Get dimensions
            dim = min(width, height)

            left = (width - dim) / 2
            top = (height - dim) / 2
            right = (width + dim) / 2
            bottom = (height + dim) / 2
            # Crop the center of the image
            img = img.crop((left, top, right, bottom))

            img.thumbnail(size)

            img.save("../thumbs/" + file, "JPEG", quality=50)
            print("saving: " + file)
        else:
            break

    for wall in walls:
        wallFile = wall.get("filename").strip()
        print("wall: " + wallFile)
        if(wall != "" and os.path.isfile("../walls/" + wallFile)):
            newWalls.append({"filename": wallFile, "added": wall.get("added")})
        elif(wallFile != "" and (not os.path.isfile('../walls/' + wallFile))):
            print(
                wallFile + " has been removed as a thumbnail and from the website.")
            os.remove('../thumbs/' + wallFile)

    print(newWalls)

    newWalls = json.dumps(newWalls, sort_keys=True,
                          indent=4, separators=(',', ': '))

    # open the script.js file for writing and write new info
    scriptFile = open("../script.js", "w")
    scriptFile.write(fileStr[0:(fileStr.find("["))] +
                     str(newWalls) + fileStr[(fileStr.find("]")) + 1:])
    scriptFile.close()

    os.chdir("../utils")
    # Popen("gitHelp.bat", cwd=os.getcwd())

if __name__ == "__main__":
    handle()
