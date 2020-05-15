from Game_user import InputUser, ComputeUser
import random

class Game():

  def __init__(self,player):
    self.player = player
    self.numb = random.randint(0,100)


  def play(self,maxTurn = 9999):
    inp = -1
    for x in range(maxTurn):
      inp = self.player.play()
      if inp == self.numb: break
      isUnder = False
      if inp > self.numb:isUnder = True 
      self.player.result(isUnder)
    if inp == self.numb:
      self.player.win()
      return True
    else:
      self.player.loose()
      return False



g = Game(InputUser())
g.play()