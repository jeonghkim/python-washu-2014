## tests 

import unittest
import Portfolio


class PortfolioTest(unittest.TestCase):
 def setup(self):
  self.portfolio = Portfolio()
 
 def test_add_cash(self):
  self.portfolio.addCash(300.50)
  self.assertEqual(300.50, self.portfolio.cash)

if __name__ == '__main__':
  unittest.main()