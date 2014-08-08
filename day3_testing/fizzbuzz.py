# For numbers divisible by 3, print "Fizz"
# For numbers divisible by 5, print "Buzz"
# For numbers divisible by 3 and 5, print "FizzBuzz"

def FizzBuzz(i):
 try:
#  print "I'm really trying"
  if i % 15 ==0:
   raise Exception, "Divisible by 3 and 5"
  if i % 3 == 0:
   return "Fizz"
  if i % 5 == 0:
   return "Buzz"
 except:
  if i % 15 ==0:
   return "FizzBuzz"
   pass
 else:
  return str(i)
 finally:
  print "finally"
   
for i in range(18):
 print str(i) + ":" + FizzBuzz(i)
