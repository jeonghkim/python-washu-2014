class Burger():
 def __init__(self, filling, doneness, size, toppings, container): # define __init__ methods with elements of states
  self.filling = filling # this will be a filling for the specific instance "self"
  self.doneness = doneness
  self.size = size
  self.toppings = self.toppings_allowed(toppings)
  self.container = container
  
 def __str__(self):
  return "I'm a %s %s burger" %(self.doneness, self.filling)
 
 def toppings_allowed(self, attempted_toppings):
  allowed_toppings =["cheese", "tomato", "onion", "lettuce"]
  toppings = []
  for topping in attempted_toppings:
   if topping in allowed_toppings:
    toppings.append(topping)
   return toppings
   
 def tastiness(self): # Now define behaviors
  if "cheese" in self.toppings:
   return "VERY GOOD"
  elif self.doneness == "raw":
   return "yuck!"
   
 def cooking_time(self): # Another behavior
  # example sizes: .25, .33, .5
  # example doneness: rare, medium-rare, medium, medium-well, well
  time_for_doneness = 0
  if self.doneness == "raw":
   time_for_doneness = 0 
  elif self.doneness == "rare":
   time_for_doneness = 5
  elif self.doneness == "medium":
   time_for_doneness = 6
  elif self.doneness == "well":
   time_for_doneness = 8
  else:
   return "UNKNOWN"
   
  return self.size * 4 * time_for_doneness 
  
rare_Burger = Burger("beef", "rare", 0.25, ["cheese"], "bread")
 
#print rare_Burger.cooking_time() 
#print type(rare_Burger)
print rare_Burger

class VeggieBurger(Burger): # create a subclass VeggieBurger of the superclass Burger
 def __init__(self, size, toppings_ordered, container):
  Burger("vegie patty", "medium", size, toppings_ordered, container) 
  self.doneness= "medium"
  self.container = container
 
 def toppings_allowed(self, attempted_toppings):
  allowed_toppings =["cheese", "tomato", "onion", "lettuce"]
  toppings = []
 for topping in attempted_toppings:
   if topping in allowed_toppings:
    toppings.append(toppings_ordered)
   return toppings

 def cooking_time(self):
  return 6
  
veggie_burger = VeggieBurger(["tomato", "bacon"], "bread")
print veggie_burger