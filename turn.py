from player import Player
from shop import Shop
from gear import Gear
from quest import Quest

class Turn:
	def __init__(self):
		self.running = True
		
		self.choice_list = [
			"Shop --- to visit the local shop", "Quest --- to venture on a small quest", "Rest --- to rest and restore health",
			"Talk --- to speak to locals", "Observe --- to look around the town and the scnerey", "Travel --- to travel to a different location",
			"Location --- to check your current location", "Gear --- to review your current gear", "Stats --- to review your character stats", 
			"Save --- save the game locally", "Help --- to get tips on how to play the game", "End --- to end the game"]
		
		#set all gear
		self.dagger = Gear("weapon", "dagger", [1, 4], 0, 0, 1, 0, 5)
		self.rapier = Gear("weapon", "rapier", [3, 6], 0, 0, 0, 0, 9)
		self.shortSword = Gear("weapon", "short sword", [4, 7], 0, 0, 0, 0, 16)
		self.longSword = Gear("weapon", "long sword", [10, 13], 0, 1, 0, 0, 25)
		self.greatSword = Gear("weapon", "great sword", [15, 18], 0, 2, 0, 0, 64)
		self.oneHandAxe = Gear("weapon", "one hand axe", [2, 5], 0, 0, 0, 0, 7)
		self.warAxe = Gear("weapon", "war axe", [9, 12], 0, 1, 0, 0, 20)
		self.greatAxe = Gear("weapon", "great axe", [9, 12], 0, 2, 0, 0, 81)
		
		self.leatherArmor = Gear("armor", "leather armor", 0, 0, 0, 0, 1, 5)
		self.studdedLeather = Gear("armor", "studded leather armor", 0, 0, 0, 1, 2, 13)
		self.hideArmor = Gear("armor", "hide armor", 0, 0, 0, 2, 2, 18)
		self.scaleMail = Gear("armor", "scale mail armor", 0, 1, 0, 0, 4, 20)
		self.breastPlate = Gear("armor", "breast plate armor", 0, 2, 0, 0, 5, 28)
		self.halfPlate = Gear("armor", "half plate armor", 0, 2, 0, 0, 6, 25)
		self.chainMail = Gear("armor", "chain main armor", 0, 0, 1, 0, 8, 63)
		self.splintMail = Gear("armor", "splint mail armor", 0, 0, 2, 0, 9, 79)
		self.fullPlate = Gear("armor", "full plate armor", 0, 0, 2, 0, 10, 94)
		
		self.healthPotion = Gear("potion", "health potion", 0, [3, 7], 0, 0, 0, 10)
		
		#city npc talk 3d matrix
		#[city][race][dailogue num]
		self.dialoguematrix = [
			[
				['An Elf tells you, "The war is going good, my friend. Soon we will restore peace to Jenor."',
				 'An Elf tells you, "We hope to one day make this town into a great metropolis!"',
				 'An Elf tells you, "Do you think that our war effort is for the greater good?"',
				 'An Elf tells you, "Those humans have no idea what they are doing. They deserve to be slaves!"',
				 'An Elf tells you, "Some people fight for power, some for peace. I wish we all fought only for peace."'],
				['An elf tells you, "Your people will lose this war. Soon peace will be restored to Jenor."',
				 'An elf tells you, "We hope to one day make this town into a great metropolis!"',
				 'An elf tells you, "What do your people fight for, Human?"',
				 'An elf tells you, "You Humans desrve to be slaves!"',
				 'An elf tells you, "You and I are not much different, Human. I hope more people think the same."'],
				['An Elf tells you, "This war is close. Soon the Elves will restore peace to Jenor."',
				 'An Elf tells you, "We hope to one day make this town into a great metropolis!"',
				 'An Elf tells you, "Do you think what us Elves are fighting for is the right thing?"',
				 'An Elf tells you, "Those humans have no idea what they are doing. They deserve to be slaves!"',
				 'An Elf tells you, "Some Elves fight for power, some for peace. I wish we all fought only for peace."']],
			[
				['An Elf tells you, "Today we win the war! I know I always say that, but I can feel it this time!"',
				 'An Elf tells you, "This ancient city has all sorts of Elven history!"',
				 'An Elf tells you, "Have you ever wondered how the Elves arrived on Jenor?"',
				 'An Elf tells you, "One day we will control those damn humans and use this as our capital city!"',
				 'An Elf tells you, "I wish this war would end before any more damage is done."'],
				['An elf tells you, "Today we will defeat your people! I know I always say that, but I can feel it this time!"',
				 'An elf tells you, "This ancient city has all sorts of elven history!"',
				 'An elf tells you, "Have you ever wondered how the elves arrived on Jenor?"',
				 'An elf tells you, "One day we will control you people and use this as our capital city!"',
				 'An elf tells you, "I wish this war would end before any more damage is done."'],
				['An Elf tells you, "Today we win the war! I know I always say that, but I can feel it this time!"',
				 'An Elf tells you, "This ancient city has all sorts of Elven history!"',
				 'An Elf tells you, "Have you ever wondered how the Elves arrived on Jenor?"',
				 'An Elf tells you, "One day we will control those damn Humans and use this as our capital city!',
				 'An Elf tells you, "I wish this war would end before any more damage is done."']],
			[
				['A Dwarf tells you, "This war is insane! I wonder who will win in the end."',
				 'A Dwarf tells you, "This city is rich with the history of the Dwarves!',
				 'A Dwarf tells you, "Which side do you think will win in the end?"',
				 'A human tells you, "Damn you Elves. You want nothing but control."',
				 'An Elf tells you, "We can\'t let a beautiful city like this get destroyed by war!"'],
				['A Dwarf tells you, "This war is insane! I wonder who will win in the end."',
				 'A Dwarf tells you, "This city is rich with the history of the Dwarves!"',
				 'A Dwarf tells you, "Which side do you think will win in the end?',
				 'An elf tells you, "Damn you Humans. You want nothing but chaos."',
				 'A Humans tells you, "We can\'t let a beautiful city like this get destroyed by war!"'],
				['A Dwarf tells you, "This war is insane! I wonder who will win in the end."',
				 'A Dwarf tells you, "This city is rich with the history of us Dwawrves!',
				 'A Dwarf tells you, "Which side do you think will win in the end?"',
				 'An Elf tells you, "Damn those Humans. They want nothing but chaos."',
				 'A Human tells you, "Damn those Elves. They want nothing but control."']],
			[
				['A Dwarf tells you, "I hope the horror of war never reaches this city."',
				 'A human tells you, "This city is the best city for trade in all of Jenor!"',
				 'An Elf tells you, "How old do you think this great metropolis is?"',
				 'A human tells you, "I wish the war would end so I could finally leave this city."',
				 'An Elf tells you, "This is the perfect safe haven from the war."'],
				['A Dwarf tells you, "I hope the horror of war never reaches this city."',
				 'An elf tells you, "This city is the best city for trade in all of Jenor!"',
				 'A Human tells you, "How old do you think this great metropolis is?"',
				 'An elf tells you, "I wish the war would end so I could finally leave this city."',
				 'A Human tells you, "This is the perfect safe haven from the war."'],
				['A Dwarf tells you, "I hope the horror of war never reaches this city."',
				 'A Dwarf tells you, "This city is the best city for trade in all of Jenor!"',
				 'A Dwarf tells you, "How old do you think this great metropolis is?"',
				 'An Elf tells you, "I wish the war would end so I could finally leave this city."',
				 'A Human tells you, "This is the perfect safe haven from the war."']],
			[
				['A human tells you, "How dare you show your face here, Elf."',
				 'A human tells you, "What are you doing here? This is a war torn city!"',
				 'An Elf tells you, "We will take this city soon!"',
				 'A human tells you, "You Elves will perish!"',
				 'An Elf tells you, "The humans will preish!"'],
				['An elf tells you, "How dare you show your face here, Human."',
				 'An elf tells you, "What are you doing here? This is a war torn city!"',
				 'A Human tells you, "We will take this city soon!"',
				 'An elf tells you, "You Humans will perish!"',
				 'A Human tells you, "The elves will preish!"'],
				['An Elf tells you, "What are you doing here Dwarf?"',
				 'A Dwarf tells you, "What are you doing here? This is a war torn city!"',
				 'An Human tells you, "We will take this city soon!"',
				 'A Human tells you, "The Elves will perish!"',
				 'An Elf tells you, "The Humans will preish!"']]]
		
		#observing the surrounding area using a 2d matrix
		#[city][scene num]
		self.observematrix = [
			["Outside of the town, you can see the great Lake, which leads into a River in the distant west, and an ocean to the east.",
			 "You can see a River, which comes from a far Mountain Range, lead into the great Lake.",
			 "The town is beautiful and peaceful, with not much happening and not much to do."],
			["Out of the town, you can see nothing but plains for miles.",
			 "The town has many districts, all showing different architectual time periods of the Elves.",
			 "The town isn't too big, but is greatly populated, with so much happening that you may need a second to take a break."],
			["Most of the town is built in caves from more ancient Dwarven cultures, but the newer town has flatened the mountains to make room for modern homes.",
			 "Right on the edge of town, you can see an entire mountain range that spans for miles.",
			 "The town is small and restricted since it is built on mountains, but the population is plenty for it's size."],
			["The city is split in two, a northern and southern half, divided by a small river that leads to two different oceans.",
			 "To the north of the city, you can see many mountains with snowy tops, but if you ever venture there, beware the Brinskla.",
			 "The city is a great center for trade, and all kinds of races can be found here, leading some to belive that this can become a great metropolis some day."],
			["The entire town is in ruins, as the war has not been kind to this town.",
			 "The town is next to a great mountain range, one that contrasts the ugly nature of the town.",
			 "The town is nothing but a risky shortcut to certain parts of the continent, but since so much war has destroyed this town, it is usually too risky to move through"]]
		
		#set city shop lists
		self.mythweapondict = {
			"d": self.dagger,
			"r": self.rapier,
			"ss": self.shortSword,
			"ls": self.longSword,
			"gs": self.greatSword,
			"oha": self.oneHandAxe,
			"wa": self.warAxe,
			"ga": self.greatAxe
		}
		self.mytharmordict = {
			"la": self.leatherArmor,
			"sla": self.studdedLeather,
			"ha": self.hideArmor,
			"sma": self.scaleMail,
			"bpa": self.breastPlate,
			"hpa": self.halfPlate,
			"cma": self.chainMail,
			"sma": self.splintMail,
			"fpa": self.fullPlate
		}
		self.mythpotiondict = {
			"hp": self.healthPotion
		}
		
		#set city shops
		self.mythshop = Shop(self.mythweapondict, self.mytharmordict, self.mythpotiondict)
		
		#begin player instance
		self.player = Player()
		
		#game stats
		self.player.equiped_weapon = self.dagger
		self.player.equiped_armor = self.leatherArmor
		self.citylist = ["myth", "faera", "kal'ein", "alura", "rithar"]
		
	def turn(self, choice):
		if choice.lower().strip() == "shop":
			self.mythshop.displaygear(self.player)
			shopchoice = input(":: ")
			if shopchoice.lower().strip() == "exit":
				pass
			else:
				isavailable = self.mythshop.checkavailability(shopchoice.lower().strip())
				if isavailable == "weapon":
					self.player.equiped_weapon = self.mythshop.buygear(shopchoice.lower().strip(), isavailable, self.player.GP)
				elif isavailable == "armor":
					self.player.equiped_armor = self.mythshop.buygear(shopchoice.lower().strip(), isavailable, self.player.GP)
				elif isavailable == "potion":
					potiontoadd = self.mythshop.buygear(shopchoice.lower().strip(), isavailable, self.player.GP)
					self.player.potion_list.append(potiontoadd)
				else:
					print('"{}" is not available in this shop.'.format(shopchoice))
			return True
		elif choice.lower().strip() == "quest":
			quest = Quest()
			quest.generate()
			while True:
				print("Will you accept the quest? (yes/no)")
				questchoice = input(":: ")
				if questchoice.lower().strip() == "yes":
					questresult, earnedgp, earnedxp = quest.run(self.player)
					break
				elif questchoice.lower().strip() == "no":
					break
				else:
					print('"{}" is not a valid command'.format(questchoice))
			if questresult == "victory":
				self.player.GP += earnedgp
				self.player.XP += earnedxp
				print("You won! Earned {0} GP and {1} XP!".format(earnedgp, earnedxp))
			elif questresult == "ran":
				print("You ran and earned nothing.")
			elif questresult == "death":
				self.death()
			return True
		elif choice.lower().strip() == "rest":
			self.player.curHP = self.player.maxHP
			return True
		elif choice.lower().strip() == "talk":
			self.player.talk(self.dialoguematrix)
			return True
		elif choice.lower().strip() == "observe":
			self.player.observe(self.observematrix)
			return True
		elif choice.lower().strip() == "travel":
			print("Where do you want to travel to")
			for i in self.citylist: print(i.capitalize())
			print("(type \"none\" to exit)")
			print("")
			destination = input(":: ")
			if destination.lower().strip() == "none":
				print("You stay in your current location.")
				pass
			else:
				self.player.travel(destination.lower().strip(), self.citylist)
				return True
		elif choice.lower().strip() == "location":
			self.player.location(self.citylist)
			return True
		elif choice.lower().strip() == "gear":
			self.player.gear()
			return True
		elif choice.lower().strip() == "stats":
			self.player.stats()
			return True
		elif choice.lower().strip() == "save":
			self.player.save()
			return True
		elif choice.lower().strip() == "help":
			print("Help")
			return True
		elif choice.lower().strip() == "end":
			print("Thank you for playing!")
			return False
		else:
			print('The command "{}" is not available.\n'.format(choice))
			return True
			
	def death(self):
		pass
		
	#setup for into
	def setup(self, race):
		stats = self.player.setRace(race)
		self.player.setStats(stats)
		if race == "elf" or race == "elven":
			print("You are an Elf supporting your side in the war...")
		elif race == "human":
			print("You are a Human supporting your side in the war...")
		elif race == "dwarf" or race == "dwarven":
			while True:
				print("You are a Dwarf, pick your side in the war...")
				print("(Elven or Human)")
				choice = input()
				try:
					choice = choice.replace("side", "")
				except:
					pass
				try:
					self.player.setSide(choice.lower().strip())
					break
				except:
					print('"{}" is not a valid side.'.format(choice))
					
	def run(self):
		print("\nWhat do you want to do?")
		for i in self.choice_list: print(i)
		self.running = self.turn(input(": "))
		return self.running