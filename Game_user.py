



class InputUser():


  def __init__(self):
    self.turns = 0

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
    