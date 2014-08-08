#def ordinal(n):
 #if n==1:
  #return "1st"
 #elif n==2:
  #return "2nd"
 #else:
 # return "3rd"
  
 ## refactoring 
def ordinal(n):
# if (type(n) == int) & (type(n) == float):
 # pass
 #else: 
  #return "Improper Input"
 try: # try this, and
  n = int(n)
 except: # if an error occurred, return this (more efficient than just checking the type, since handles all kinds of errors)
  return "Improper Input"
# n = str(n)
 last_digit = n % 10
 second_to_last_digit = (n %100) / 10
 endings = {1: "st", 2: "nd", 3: "rd"}
 ending = "th"
 if second_to_last_digit !=1 and last_digit in endings.keys() :
  ending = endings[last_digit]
 elif last_digit == 1:
  ending = "st"
 elif last_digit ==2:
  ending = "nd"
 elif last_digit ==3:
  ending = "rd"
  
 return str(n) + ending
  
  