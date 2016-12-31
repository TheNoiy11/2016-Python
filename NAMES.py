names = [["Brian", "LeBlanc"],["Virginia", "Saurer"],["Hugh","Mungus"]]
birth = [["July","17","1998"],["May","19","1998"],["DANK","MEME","2016"]]

request = [input("Enter a first name: "), input("Enter a last name: ")]

for i in range(len(names)):
	if request == names[i]:
		print(birth[i])
		break