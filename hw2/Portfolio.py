## HW 2: Build a piece of software for a financial institution to model one of their clients' portfolios. 
# Jeong

# A portfolio can consist of 3 types of items:
# 1. Cash
# 2. Stock
# 3. Mutual Funds
# + Bonds

import random

class Portfolio():
 def __init__(self):
  self.cash = 0
  self.stock = {}
  self.mutualfunds = {}
  self.assets = {"cash" : self.cash , "stock" : self.stock, "mutualfunds" : self.mutualfunds}
  self.history = []
  
 def __str__(self):
  assets = "cash: $%r\n" % (self.assets["cash"])
  assets += "stock: %r\n" %(self.assets["stock"])
  assets += "mutual funds: %r" %(self.assets["mutualfunds"])
  return assets
       
 def addCash(self, amount):
  self.assets["cash"] += amount
  self.transaction = "added $%r" % (amount)
  self.history.append(self.transaction)
  return self.assets["cash"] 
  
 def buyStock(self, share, stock, price): 
  self.ticker = stock.ticker
  if self.ticker in self.stock:
   self.stock[self.ticker] += share
  else:
   self.stock[self.ticker] = share
  self.price = random.uniform(0.5*price, 1.5*price)
  self.assets["cash"] -= self.price * share
  
 def sellStock(self, share, ticker, price):
  self.ticker = ticker
  try: 
#   if self.ticker in self.stock:
   self.stock[self.ticker] -= share
  except:
   return "No stock named %s" %s
  self.price = random.uniform(0.5*price, 1.5*price)
  self.assets["cash"] += self.price * share
     
 def buyMutualFund(self, share, symbol):
  self.share = share
  self.symbol = symbol
  self.mutualfunds = self.mutualfunds
  return self.mutualfunds

#  def sellMutualFund(self, symbol, share):
#   self.symbol = symbol
#   self.share = share
#   self.mutualfunds = 
   
class Stock():
 def __init__(self, price, ticker):
  self.price = price
  self.ticker = ticker

class MutualFund():
 def __init__(self, symbol):
  self.symbol = symbol
  

    
portfolio = Portfolio()
portfolio.addCash(300.50)
s = Stock(20, "HFH")

portfolio.buyStock(5, s, 1)
portfolio.sellStock(3,"HFH", 1)

# mf1= MutualFund("BRT")
# mf2 = MutualFund("GHT")
# portfolio.buyMutualFund(10.3, mf1)
# portfolio.buyMutualFund(2, mf2)

  
print(portfolio)
print portfolio.history