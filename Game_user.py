



class InputUser():


  def __init__(self):
    self.turns = 0

  def reset(self):
    pass

  def result(self,isUnder):
    stri ="The result is "
    if isUnder:stri += "under !"
    else:stri += "ubove !"

    print(stri)

  def play(self):
    self.turns +=1
    inp = 0
    while inp == 0:
      try:
        inp = int(input("Vous devinez (0<x<100)=>"))
        assert (inp > 0 and inp < 100)
      except Exception:
        inp = 0
    return inp

  
  def win(self):
    print("You win in "+str(self.turns)+" turns !")
  
  
  def loose(self,ans):
    print("You loos :(\nThe truth answer was "+str(ans))




class ComputeUser():


  def __init__(self):
    self.turns = 0
    self.ub = 100
    self.db = 0
  
  def reset(self):
    self.turns = 0
    self.ub = 101
    self.db = 0

  def calcCenter(self):
    return int((self.ub-self.db)/2)+self.db

  def result(self,isUnder):
    if isUnder:
      self.ub = self.calcCenter()
    else:
      self.db = self.calcCenter()

  def play(self):
    self.turns +=1
    #print("I, robot boiii, play the "+str(self.calcCenter()))
    return self.calcCenter()

  
  def win(self):
    print("I win in "+str(self.turns)+" turns !")
  
  
  def loose(self,ans):
    print("I loost :(\nThe truth answer was "+str(ans))
    


4.8138090