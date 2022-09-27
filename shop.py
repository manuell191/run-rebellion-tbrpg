import time

class Shop:
	def __init__(self, weapondict, armordict, potiondict):
		self.weapondict = weapondict
		self.armordict = armordict
		self.potiondict = potiondict
	
	#entire set of functions that is used for shop functionality
	def displaygear(self, player):
		print("Weapons on sale:\n")
		for i, j in self.weapondict.items():
			spaces = 25 - len(j.name)
			spaces2 = 5 - len(str(j.cost))
			spacelist = [" " for k in range(spaces)]
			spacelist2 = [" " for k in range(spaces2)]
			spacestring = "".join(spacelist)
			spacestring2 = "".join(spacelist2)
			print(j.name + str(spacestring) + "cost: " + str(j.cost) + str(spacestring2) + "attack: " + str(j.attack[0]) + "-" + str(j.attack[1]))
		print("\nArmor on sale:\n")
		
		for i, j in self.armordict.items():
			spaces = 25 - len(j.name)
			spaces2 = 5 - len(str(j.cost))
			spacelist = [" " for k in range(spaces)]
			spacelist2 = [" " for k in range(spaces2)]
			spacestring = "".join(spacelist)
			spacestring2 = "".join(spacelist2)
			print(j.name + str(spacestring) + "cost: " + str(j.cost) + str(spacestring2) + "armor: " + str(j.ac))
		print("\nPotions on sale:\n")
		
		for i, j in self.potiondict.items():
			spaces = 25 - len(j.name)
			spacelist = [" " for k in range(spaces)]
			spacestring = "".join(spacelist)
			print(j.name + str(spacestring) + "cost: " + str(j.cost))
		print("\nYou have {0} GP.\n".format(player.GP))
		
		time.sleep(0.3)
		
		print("What do you want to buy?")
		print("(type initals to buy (example: d (dagger)/sla (studded leather armor))")
		print("(type \"exit\" to exit)\n")
	
	def checkavailability(self, choice):
		if choice in self.weapondict.keys():
			return "weapon"
		elif choice in self.armordict.keys():
			return "armor"
		elif choice in self.potiondict.keys():
			return "potion"
		else:
			return False
	
	def buygear(self, choice, geartype, playergp):
		if geartype == "weapon":
			print(self.weapondict[choice].name.capitalize() + " has been equiped!")
			return self.weapondict[choice]
		elif geartype == "armor":
			print(self.armordict[choice].name.capitalize() + " has been equiped!")
			return self.armordict[choice]
		elif geartype == "potion":
			print(self.potiondict[choice].name.capitalize() + " has been added to your inventory!")
			return self.potiondict[choice]