import random

class Player:
  def __init__(self):
    self.race = None
    self.side = None
    
    self.equiped_weapon = None
    self.equiped_armor = None
    self.potion_list = []
    
    self.save_weapon = None
    self.save_weapon = None
    self.save_potion =[] 
    
    #player stats
    self.story = 0
    self.maxHP = 0
    self.curHP = 0
    self.STR = 0
    self.DEX = 0
    self.AC = 0
    self.XP = 0
    self.level = 1
    self.GP = 0
    self.city = 1
     
    #save stats
    self.saveStory = 0
    self.saveMaxHP = 0
    self.saveCurHP = 0
    self.saveSTR = 0
    self.saveDEX = 0
    self.saveAC = 0
    self.saveXP = 0
    self.saveLevel = 0
    self.saveGP = 0
    self.saveCity = 1
  
  #note: stats include the modifiers from gear
  #to check stats plainly through print statements
  def stats(self):
    print("This is your current stats:\n")
    print("Max Health      " + str(self.maxHP + self.equiped_armor.health) + "\nCurrent Health  " + str(self.curHP))
    print("Strength        " + str(self.STR + self.equiped_weapon.strength + self.equiped_armor.strength))
    print("Dexterity       " + str(self.DEX + self.equiped_weapon.dexterity + self.equiped_armor.dexterity))
    print("Armor Class     " + str(self.AC + self.equiped_armor.ac) + "\nXP              " + str(self.XP))
    print("Level           " + str(self.level))
  
  #to check all gear and upgrades to stats
  def gear(self):
    print("You current weapon is: " + self.equiped_weapon.name)
    print("Your weapon does between {} and {} damage".format(str(self.equiped_weapon.attack[0]), str(self.equiped_weapon.attack[1])))
    
    if self.equiped_weapon.dexterity > 0:
      print("Your weapon adds {} to your dexterity".format(str(self.equiped_weapon.dexterity)))
    if self.equiped_weapon.strength > 0:
      print("You weapon adds {} to your strength".format(str(self.equiped_weapon.strength)))
    
    print("")
    
    print("Your current armor is: " + self.equiped_armor.name)
    print("Your armor adds {} to your armor stat".format(str(self.equiped_armor.ac)))
    
    if self.equiped_armor.dexterity > 0:
      print("Your armor adds {} to your dexterity".format(str(self.equiped_armor.dexterity)))
    if self.equiped_armor.health > 0:
      print("Your armor adds {} to your health".format(str(self.equiped_armor.health)))
    if self.equiped_armor.strength > 0:
      print("Your armor adds {} to your strength".format(str(self.equiped_armor.strength)))
    
    if len(self.potion_list) > 0:
      print("Your current potions are:\n")
      for i in self.potion_list: print(i.name.capitalize())
  
  #to talk to locals
  #uses 3d matrix to automatically get a dialogue
  def talk(self, matrix):
    if self.race == "elf":
      racenum = 0
    elif self.race == "human":
      racenum = 1
    elif self.race == "dwarf":
      racenum = 1
    x = random.randint(0, 4)
    print(matrix[self.city - 1][racenum][x])
  
  #to look at the scenery
  #uses a 2d matrix to automatically get the descriptions
  def observe(self, matrix):
    x = random.randint(0, 2)
    print(matrix[self.city - 1][x])
  
  #to figure out your location
  def location(self, citylist):
    print("You are currently at {}".format(citylist[self.city - 1]))
  
  #to travel to a new location
  def travel(self, destination, citylist):
    if destination in citylist:
      if destination == citylist[self.city - 1]:
        print("You are already in {}".format(destination))
      elif destination == citylist[0]:
        print("You are in the village of Myth")
        self.city = 1
      elif destination == citylist[1]:
        print("You are in the village of Faera")
        self.city = 2
      elif destination == citylist[2]:
        print("You are in the city of Kal'ein")
        self.city = 3
      elif destination == citylist[3]:
        print("You are in the metropolis Alura")
        self.city = 4
      elif destination == citylist[4]:
        print("You are in the city of Rithar")
        self.city = 5
    else:
        print("The city \"{}\" is not available".format(destination))
  
  #to save stats
  def save(self):
    self.save_weapon = self.equiped_weapon
    self.save_armor = self.equiped_armor
    self.save_potion = self.potion_list
    
    self.saveStory = self.story
    self.saveCity = self.city
    self.saveMaxHP = self.maxHP
    self.saveCurHP = self.curHP
    self.saveSTR = self.STR
    self.saveDEX = self.DEX
    self.saveAC = self.AC
    self.saveXP = self.XP
    self.saveLevel = self.level
    self.saveGP = self.GP
    self.saveCity = self.city
  
  #setup for intro
  def setStats(self, newstatlist):
    if len(newstatlist) <= 6:
      self.maxHP = newstatlist[1] if len(newstatlist) >= 2 else 0
      self.STR = newstatlist[2] if len(newstatlist) >= 3 else 0
      self.DEX = newstatlist[3] if len(newstatlist) >= 4 else 0
      self.AC = newstatlist[4] if len(newstatlist) >= 5 else 0
      self.GP = newstatlist[5] if len(newstatlist) >= 6 else 0
        
      self.curHP = self.maxHP
    else:
      raise ValueError("list must be a length of 6")
  
  def setSide(self, race):
    if race == "elf" or race == "elven":
      self.side = "elf"
      print("You support the Elven side in the war.")
    elif race == "human":
      self.side = "human"
      print("You support the Human side in the war.")
    else:
      raise ValueError("str must be elf or human")
  
  def setRace(self, race):
    if isinstance(race, (str)):
      self.race = race
      if race == "elf" or race == "elven":
        self.side = "elf"
        return ["elf", 8, 8, 12, 10, 15]
      elif race == "human":
        self.side = "human"
        return ["human", 10, 12, 10, 8, 5]
      elif race == "dwarf" or race == "dwarven":
        return ["dwarf", 12, 10, 8, 12, 10]
      else:
        raise ValueError("str must be elf, human, or dwarf")
    else:
      raise TypeError("object must be str type")