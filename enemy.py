import random

class Enemy:
	def __init__(self):
		self.enemylist = ["troll", "criminal", "young dragon", "wolf", "knight", "cultist"]
		self.enemy = None
		self.prize = None
		
		self.attack = None
		self.armor = None
		self.health = None
		
	#creates a random enemy, and adds [gp, xp] as self.prize
	def setEnemy(self):
		x = random.randint(0, len(self.enemylist) - 1)
    
		self.enemy = self.enemylist[x]
		if self.enemy == self.enemylist[0]: #troll 
			self.prize = [random.randint(10, 15), 10]
			attack = random.randint(10, 15)
			self.attack = [attack, attack + 2]
			self.armor = random.randint(10, 13)
			self.health = random.randint(10, 15)
		elif self.enemy == self.enemylist[1]: #criminal
			self.prize = [random.randint(5, 10), 10]
			attack = random.randint(6, 10)
			self.attack = [attack, attack, + 2]
			self.armor = random.randint(8, 10)
			self.health = random.randint(13, 17)
		elif self.enemy == self.enemylist[2]: #young dragon
			self.prize = [random.randint(15, 20), 15]
			attack = random.randint(20, 25)
			self.attack = [attack, attack + 5]
			self.armor = random.randint(17, 20)
			self.health = random.randint(30, 50)
		elif self.enemy == self.enemylist[3]: #wolf
			self.prize = [random.randint(1, 3), 5]
			attack = random.randint(1, 3)
			self.attack = [attack, attack + 2]
			self.armor = random.randint(3, 5)
			self.health = random.randint(5, 10)
		elif self.enemy == self.enemylist[4]: #knight
			self.prize = [random.randint(13, 17), 10]
			attack = random.randint(13, 17)
			self.attack = [attack, attack + 2]
			self.armor = random.randint(15, 17)
			self.health = random.randint(17, 27)
		elif self.enemy == self.enemylist[5]: #cultist
			self.prize = [random.randint(3, 5), 5]
			attack = random.randint(5, 7)
			self.attack = [attack, attack + 2]
			self.armor = random.randint(5, 7)
			self.health = random.randint(10, 13)