import os
import json
from subprocess import Popen

from PIL import Image

def handle():

	# set working directory to be the wallpapers folder and list out all the files
	os.chdir("../walls/")
	files = os.listdir(os.getcwd())

	print("files: " + str(files));

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

	newWalls = []

	size = 900,900

	for file in files:
		print("The most recent file is: " + file)
		if(file != wall):
			newWalls.append(file)
			print("found a new wallpaper: " + file + ", generating thumbnail!");
			img = Image.open("../walls/" + file)
			if img.mode != "RGB":
				img = img.convert("RGB")
			img.thumbnail(size)
			img.save("../thumbs/" + file, "JPEG", quality=50)
			print("saving: " + file)
		else:
			break


	for pape in walls:
		if(pape != "" and os.path.isfile("../walls/" + pape[1:-1])):
			newWalls.append(pape[1:-1])
			print("Confirmed that " + pape[1:-1] + " is still in the wallpapers folder.")
		elif(pape != "" and (not os.path.isfile('../walls/' + pape[1:-1]))):
			print(pape[1:-1] + " has been removed as a thumbnail and from the website.")
			os.remove('../thumbs/' + pape[1:-1])


	print("Wallpaper Listing: ")
	print(str(newWalls))

	# open the script.js file for writing and write new info
	scriptFile = open("../script.js", "w")
	scriptFile.write(fileStr[0:openBracket] + str(newWalls) + fileStr[closeBracket+1:])
	scriptFile.close();

	os.chdir("../utils")
	# print(os.getcwd())

	# Popen("gitHelp.bat", cwd=os.getcwd())

if __name__ == "__main__":
    handle()
