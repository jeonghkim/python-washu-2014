#def ordinal(n):
 #if n==1:
  #return "1st"
 #elif n==2:
  #return "2nd"
 #else:
 # return "3rd"
  
 ## refactoring 
def ordinal(n):
 if type(n) == 'int':
  pass
 else: 
  return "Improper Input"
 n = str(n)
 ending = "th"
 last_digit = n % 10
 second_to_last_digit = (n %100) / 10
 if second_to_last_digit ==1:
  ending = "th"
 elif last_digit == 1:
  ending = "st"
 elif last_digit ==2:
  ending = "nd"
 elif last_digit ==3:
  ending = "rd"
  
 return str(n) + ending
  
  