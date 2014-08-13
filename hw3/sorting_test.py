# testing file for sorting.py

from sorting import *
import unittest

class SortingTest(unittest.TestCase):
 def setup(self):
  pass
   
 def test_selection(self):
  self.assertEqual([8, 19, 27, 34, 53], selection([53, 8, 27, 34, 19]))
  self.assertEqual([8, 19, 27, 34, 53], merge_sort([53, 8, 27, 34, 19]))
  
if __name__=='__main__':
 unittest.main()