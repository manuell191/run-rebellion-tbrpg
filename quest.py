from enemy import Enemy
import random
import time

class Quest:
	def __init__(self):
		self.enemy = Enemy()
		self.enemy.setEnemy()
		self.problemlist = [
			"cause a robbery.", "caused terror in the city.", "caused a murder.", "caused destruction in the city.",
			"challenged you to a duel.", "taken someone hostage.", "caused a riot."
		]
		self.problem = None
		
	def generate(self):
		x = random.randint(0, len(self.problemlist) - 1)
		
		self.problem = self.problemlist[x]
		
		print("A quest opportunity has arrised:")
		print("A {0} has {1} You will recieve {2} GP and {3} XP.".format(self.enemy.enemy, self.problem, self.enemy.prize[0], self.enemy.prize[1]))
		
	def enemyattack(self, player):
		attempt = random.randint(1, 20)
		if attempt == 20:
			damage = random.randint(self.enemy.attack[0], self.enemy.attack[1]) * 2
			player.curHP -= damage
			print("The {0} attacks and it's a critical hit! It does {1} damage. You have {2} health left.".format(self.enemy.enemy, damage, player.curHP))
		elif attempt >= player.AC + player.equiped_armor.ac:
			damage = random.randint(self.enemy.attack[0], self.enemy.attack[1])
			player.curHP -= damage
			print("The {0} attacks! It does {1} damage. You have {2} health left.".format(self.enemy.enemy, damage, player.curHP))
		else:
			print("The {} missed!".format(self.enemy.enemy))
			
	def attack(self, player):
		attempt = random.randint(1, 20)
		if attempt == 20:
			damage = random.randint(player.equiped_weapon.attack[0], player.equiped_weapon.attack[1]) * 2
			self.enemy.health -= damage
			print("You attack the {0}, and it's a critical hit! You do {1} damage. It has {2} health left.".format(self.enemy.enemy, damage, self.enemy.health))
		elif attempt >= self.enemy.armor:
			damage = random.randint(player.equiped_weapon.attack[0], player.equiped_weapon.attack[1])
			self.enemy.health -= damage
			print("You attack the {0}! You do {1} damage. It has {2} health left.".format(self.enemy.enemy, damage, self.enemy.health))
		else:
			print("You missed!")
			
	def heal(self, player):
		print("You reach in your bag to check for health potions.")
		time.sleep(0.3)
		potions = len(player.potion_list)
		for i in player.potion_list:
			if i.name == "health potion":
				heal = random.randint(i.health[0], i.health[1])
				player.curHP += heal
				print("Your health went up by {0}. You now have {1} health.".format(heal, player.curHP))
				player.potion_list.remove(i)
				break
			else:
				pass
		if potions > len(player.potion_list):\
			pass
		elif potions == len(player.potion_list):
			print("You couldn't find any potions")
			
	def run(self, player):
		while True:
			if player.curHP <= 0:
				return "death", 0, 0
			while True:
				runaway = 0
				print("It's your turn. What do you want to do?\n")
				print("Attack\nHeal\nRun\n")
				battlechoice = input("::: ")
				if battlechoice.lower().strip() == "attack":
					self.attack(player)
					break
				elif battlechoice.lower().strip() == "heal":
					self.heal(player)
					break
				elif battlechoice.lower().strip() == "run":
					runaway = random.randint(1, 20)
					if runaway >= 10:
						print("You successfully ran away.")
						return "ran", 0, 0
					else:
						print("You could not run away.")
						break
			if self.enemy.health <= 0:
				return "victory", self.enemy.prize[0], self.enemy.prize[1]
			time.sleep(0.3)
			self.enemyattack(player)
			time.sleep(0.3)