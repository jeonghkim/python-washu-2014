# Fibonacci number
# 0,1,1,2,3,5,8, ...
last = 0 # defined in global
second = 0

#def next_fib(): # if we run the file, we will get an error since last and second are only defined in global
 #  if last == 0:
 #   last = 1
 #   return 0

  #current = last
  #last = second + last
  #second = current
  #return current

#def next_fib(): # if we run the file, we will get an error since last and second are only defined in global
 # global last # Stay away from global function using class
  #global second
  
  #if last == 0:
   # last = 1
    #return 0

#  current = last
 # last = second + last
 # second = current
  #return current
 
#next_fib()
   
class Fib(object):
  def __init__(self):
    self.last = 0
    self.second = 0
      
  def next_fib(self):
    if self.last == 0:
      self.last = 1
      return 0
Fib1 = Fib.next_fib()
print Fib1
#    current = self.last
 #   self.last = self.second + self.last
  #  self.second = current
   # return current

# import fib  
# fib.next_fib()  
# fib1 = fib.Fib()
# fib1.next_fib()
# fib2 = fib.Fib()
# fib2.next_fib()