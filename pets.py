class PET:
	def __init__(self, age = 0, type = "Type"):
		self.__age = age
		self.__type = type
		
	def getAge(self):
		return self.__age
		
	def getType(self):
		return self.__type

class OWNER:
	def __init__(self):
		self.__pets = {'Brian' : PET(5, "Type 1"), 'Kappa' : PET(2, "Type 2")}

	def showPets(self):
		for pet in self.__pets:
			print("Name:", pet)
			print("Type:", self.__pets[pet].getType())
			print("Age:", self.__pets[pet].getAge())
			print()
	def newPet(self, name, age, type):
		self.__pets[name] = PET(age, type)
			
new = OWNER()
print("****************************")
new.showPets()
new.newPet('DUDE', 17, 'some type')
print("****************************")
new.showPets()