Class CustomException(Exception):
 def __init__(self, value):
  self.value = value
 def __str__(self):
  return self.value

def i_call_a_function_with_errors():
 try:
  print "Calling a function.."
  print "Tada!"
 except CustomException as inst # as gives us access to the exception
  print "Custom Error Caught: Error({0})".format(inst.value)
 except: # any exception is caught
  print "Default Error Caught!"
 else: # If nothing broke
  print "Nothing"
 finally: # is always run
  print "Goodbye"