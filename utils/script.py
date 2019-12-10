import os
import json
import subprocess

from PIL import Image

# set working directory to be the wallpapers folder and list out all the files
os.chdir("../walls/")
files = os.listdir(os.getcwd())

# sort the directory by when the file was last accessed (i.e. when I put the file in the folder)
files.sort(key=os.path.getatime, reverse=1)

# open the javascript file
scriptFile = open("../script.js", "r")

fileStr = str(scriptFile.read())

scriptFile.close();

openBracket = fileStr.find("[")
closeBracket = fileStr.find("]")

walls = fileStr[openBracket+1:closeBracket]

walls = walls.replace("\n", "");
walls = walls.replace(" ", "");
walls = walls.split(",")

wall = walls[0]
wall = wall[1:-1]

print(wall)

newWalls = []

size = 900,900

for file in files:
	if(file != wall):
		newWalls.append(file)
		img = Image.open("../walls/" + file)
		if img.mode != "RGB":
			img = img.convert("RGB")
		img.thumbnail(size)
		img.save("../thumbs/" + file, "JPEG", quality=50)
		print("saving: " + file)
	else:
		break


for pape in walls:
	if(pape != ""):
		newWalls.append(pape[1:-1])


# open the script.js file for writing and write new info
scriptFile = open("../script.js", "w")
scriptFile.write(fileStr[0:openBracket] + str(newWalls) + fileStr[closeBracket+1:])
scriptFile.close();

subprocess.call(['./gitHelp.bat'], shell=True)

