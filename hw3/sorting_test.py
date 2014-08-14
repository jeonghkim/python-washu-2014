# testing file for sorting.py

from sorting import *
import random
import unittest

class SortingTest(unittest.TestCase):
 def setup(self):
  pass
   
 def test_selection(self):
  self.assertEqual([8, 19, 27, 34, 53], selection([53, 8, 27, 34, 19]))
  self.assertEqual([11, 30, 40, 64, 71], merge_sort([71, 30, 64, 11, 40]))
  self.assertEqual([3, 9, 45, 75], quick_sort([9, 45, 75, 3])) 
if __name__=='__main__':
 unittest.main()