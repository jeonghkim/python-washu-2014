# class BiologicalThing():
#  def alive(self):
#   return True
  
class Animal():
 def __init__(self, age, sex):
  self.age = age
  self.sex = sex
 def gets_energy_from_the_sun(self):
  return False

class Human(Animal): # class definition, we can leave as a black inside the parenthesis
 def __init__(self, age, sex, name): # initializer or constructor
  Animal.__init__(self, age, sex) # initialize yourself as an animal. and take care of all animal stuff
  self.name = name 
  
 def speak(self, words): 
  if self.sex == "Male":
   return words.upper()
  else:
   return words
 def introduce(self):
  return self.speak("Hello, I'm %s" % self.name)


andy = Human("21", "Male", "andy")
# print andy.gets_energy_from_the_sun()
print andy.introduce()

