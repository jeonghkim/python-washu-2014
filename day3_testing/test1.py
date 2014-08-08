import unittest
import ordinal

class OrdinalTest(unittest.TestCase):
 
 def setup(self): #setup: set values you want to use throughout the tests
  pass
 
 def test_first(self):
  self.assertEqual("1st", ordinal.ordinal(1)) # first ordinal: module, second ordinal: method
  
 def test_second(self):
  self.assertEqual("2nd", ordinal.ordinal(2))
  
 def test_second(self):
  self.assertEqual("3rd", ordinal.ordinal(3))

 def test_second(self):
  self.assertEqual("11th", ordinal.ordinal(11))
 
 def test_string_input(self):
  self.assertEqual("Input is not a number.", ordinal.ordinal("1"))

 def test_negative_one(self):
  self.assertEqual("-1st", ordinal.ordinal(-1))
  
if __name__ == '__main__':
  unittest.main()