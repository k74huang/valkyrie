import os
import json
import time
import json
from PIL import Image, ImageOps
from subprocess import Popen


def handle():

    # set working directory to be the wallpapers folder and list out all the
    # files
    os.chdir("../walls/")
    files = os.listdir(os.getcwd())

    # sort the directory by when the file was last accessed (i.e. when I put
    # the file in the folder)
    files.sort(key=os.path.getmtime, reverse=1)

    # open the javascript file
    scriptFile = open("../script.js", "r")
    fileStr = str(scriptFile.read())
    scriptFile.close()

    # Cut out only the wallpaper array from the script file
    walls = fileStr[(fileStr.find("[") + 1):(fileStr.find("]"))]

    print(walls)

    if (walls != "" and len(walls) > 0):
        walls = walls.replace("\n", "")
        walls = "[" + walls + "]"
        walls = json.loads(walls)
        # get when the last wallpaper was loaded
        prevLoadTime = float(walls[0].get("added")) if len(walls) > 0 else 0
        print("prevloadTime: " + str(prevLoadTime))
    else:
        prevLoadTime = 0
        walls = []

    newWalls = []

    size = 900, 900

    for file in files:
        print("The most recent file is: " + file +
              " with load time: " + str(os.path.getmtime("../walls/" + file)))
        # if(os.path.getmtime("../walls/" + file) > prevLoadTime):
        #     newWalls.append(
        #         {"filename": file, "added": os.path.getmtime("../walls/" + file)})
        #     print("found a new wallpaper: " + file + ", generating thumbnail!")
        #     print("this has mtime: " + os.path.getmtime("../walls/" + file))
        #     img = Image.open("../walls/" + file)
        #     if img.mode != "RGB":
        #         img = img.convert("RGB")
        #     img.thumbnail(size)
        #     img.save("../thumbs/" + file, "JPEG", quality=50)
        #     print("saving: " + file)
        # else:
        #     break
        newWalls.append(
            {"filename": file, "added": os.path.getmtime("../walls/" + file)})
        print("found a new wallpaper: " + file + ", generating thumbnail!")
        img = Image.open("../walls/" + file)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img.thumbnail(size)
        img = ImageOps.exif_transpose(img)
        img.save("../thumbs/" + file, "JPEG", quality=50)
        print("saving: " + file)

    for wall in walls:
        wallFile = wall.get("filename").strip()
        print("wall: " + wallFile)
        if (wall != "" and os.path.isfile("../walls/" + wallFile)):
            newWalls.append({"filename": wallFile, "added": wall.get("added")})
        elif (wallFile != "" and (not os.path.isfile('../walls/' + wallFile))):
            if (os.path.isfile('../thumbs/' + wallFile)):
                print(
                    wallFile + " has been removed as a thumbnail and from the website.")
                os.remove('../thumbs/' + wallFile)
            else:
                print(wallFile + " has already been removed as a thumbnail")

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