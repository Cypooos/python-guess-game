from Game_user import InputUser, ComputeUser
import random

class Game():

  def __init__(self,player):
    self.player = player
    self.numb = 0


  def play(self,maxTurn = 9999):
    self.numb = random.randint(0,100)
    self.player.reset()
    inp = -1
    x=0
    for x in range(maxTurn):
      inp = self.player.play()
      if inp == self.numb: break
      isUnder = False
      if inp > self.numb:isUnder = True 
      self.player.result(isUnder)
    if inp == self.numb:
      self.player.win()
      return True, x
    else:
      self.player.loose(self.numb)
      return False,x


if __name__ == "__main__":

  g = Game(ComputeUser())
  total = 0
  maxAll = 1000000
  for x in range(maxAll):
    s,count = g.play()
    total += count

  print(total/maxAll*1000000)