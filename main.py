from turn import Turn

class Game:
	def __init__(self):
		self.turn = Turn()
		self.running = True
		
	#intro and setup
	def intro(self):    
		print("Welcome to the continent of Jenor.")
		print("War has broken out between the elves and the humans.")
		print("Humans have decided to fight for their freedom.")
		print("Elves claim to just want peace, however that may be achieved.")
		print("Meanwhile, the dwarves are divided on the side they fight for.\n")
		
		while True:
			print("What race do you want to be?")
			print("(Your choice will affect story and stats)\n")
			print("Elf\nHuman\nDwarf\n")
			choice = input(": ")
			try:
				self.turn.setup(choice.lower().strip())
				break
			except:
				print('"{}" is not a valid race.'.format(choice))
	
	def run(self):
		self.intro()
		self.turn.player.save()
		while self.running:
			self.running = self.turn.run()

if __name__ == "__main__":
	game = Game()
	game.run()