#class Senator():
 #def __init__(self, name):
  #self.name = name
 
 #def vote(self, bill, choice):
 # bill.votes[choice].append(self) # the value of choice: yes, no, abstain
  
 
#class Bill():
 #def __init__(self, title):
 # self.title = title
 # self.votes = {"yes" => [], "no" => [], "abstain" => []} # distionaries


# Polymorphism

class Animal(object):
 def __init__(self, name):
  self.name = name
  
 def talk(self):
  raise NotImplementedError # if any of subclass of Animal doesn't define talk method, it wil raise error
  
class Cat(Animal):
 def talk(self):
  return self.meow()
 def meow(self):
  return 'Meow!'
  
cat = Cat('Ulrika')
print cat.talk()