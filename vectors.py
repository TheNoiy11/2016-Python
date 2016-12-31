from SimpleGraphics import *

setAutoUpdate(False)
resize(800,800)
update()

fileOpen = open("vectors.txt","r")
fileData = fileOpen.read()
fileOpen.close()

fileData = fileData.replace("\n", "").replace("||", "|").strip("|").split("|")

for i in range(len(fileData)):
	fileData[i] = fileData[i].split(",")
for i in range(len(fileData)):
	for j in range(len(fileData[i])):
		fileData[i][j] = float(fileData[i][j])

scale = 10
for vector in fileData:
	line((vector[0] + 1)*scale, (vector[1]+1)*scale, (vector[2]+1)*scale, (vector[3]+1)*scale)
update()
print("DONE")