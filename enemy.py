import random

class Enemy:
  def __init__(self):
    self.enemylist = ["troll ", "criminal ", "young dragon ", "wolf ", "knight ", "cultist "]
    self.enemy = None
    self.prize = None

  #creates a random enemy, and adds [gp, xp] as self.prize
  def setEnemy(self):
    x = random.randint(0, 5)
    
    self.enemy = self.enemylist[x]
    if self.enemy == self.enemylist[0]:
      self.prize = [random.randint(10, 15), 10]
    elif self.enemy == self.enemylist[1]:
      self.prize = [random.randint(5, 10), 10]
    elif self.enemy == self.enemylist[2]:
      self.prize = [random.randint(15, 20), 15]
    elif self.enemy == self.enemylist[3]:
      self.prize = [random.randint(1, 3), 5]
    elif self.enemy == self.enemylist[4]:
      self.prize = [random.randint(13, 17), 10]
    elif self.enemy == self.enemylist[5]:
      self.prize = [random.randint(3, 5), 5]