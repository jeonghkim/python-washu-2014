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
  self.History = []
  
 def __str__(self):
  assets = "cash: $%r\n" % (self.cash)
  assets += "stock: %r\n" %(self.stock)
  assets += "mutual funds: %r" %(self.mutualfunds)
  return assets
       
 def addCash(self, amount):
  self.cash += amount
  self.transaction = "added $%r" % (amount)
  self.History.append(self.transaction)
  return self.cash 

 def withdrawCash(self, amount):
  if amount > self.cash:
   print "Transaction unavailable: Cash will be overdrawn."
  else:
   self.cash -= amount
   self.transaction = "withdrew $%r" % (amount)
   self.History.append(self.transaction)
  return self.cash 
  
 def buyStock(self, share, stock, price): 
  self.ticker = stock.ticker
  if self.ticker in self.stock:
   self.stock[self.ticker] += share
  else:
   self.stock[self.ticker] = share
  self.price = random.uniform(0.5*price, 1.5*price)
  self.cash -= self.price * share
  self.transaction = "bought %r share of %r" % (share, self.ticker)
  self.History.append(self.transaction)
  
 def sellStock(self, share, ticker, price):
  self.ticker = ticker
  try: 
   self.stock[self.ticker] -= share
  except:
   return "No stock named %s" %ticker
  self.price = random.uniform(0.5*price, 1.5*price)
  self.cash += self.price * share
  self.transaction = "sold %r share of %r" % (share, self.ticker)
  self.History.append(self.transaction)
     
 def buyMutualFund(self, share, mutualfunds):
  self.symbol = mutualfunds.symbol
  if self.symbol in self.mutualfunds:
   self.mutualfunds[self.symbol] += share
  else: 
   self.mutualfunds[self.symbol] = share
  self.price = random.uniform(0.9, 1.2)
  self.cash -= self.price * share
  self.transaction = "bought %r share of %r" % (share, self.symbol)
  self.History.append(self.transaction)

 def sellMutualFund(self, symbol, share):
  self.symbol = symbol
  try: 
   self.mutualfunds[self.symbol] -= share
  except:
   return "No stock named %s" %symbol
  self.price = random.uniform(0.9, 1.2)
  self.cash += self.price * share
  self.transaction = "sold %r share of %r" % (share, self.symbol)
  self.History.append(self.transaction)

 def history(self):
  return self.History
    
class Stock():
 def __init__(self, price, ticker):
  self.price = price
  self.ticker = ticker

class MutualFund():
 def __init__(self, symbol):
  self.symbol = symbol
  

    
portfolio = Portfolio()
portfolio.addCash(300.50)
portfolio.withdrawCash(400)
s = Stock(20, "HFH")

portfolio.buyStock(5, s, 1)
portfolio.sellStock(3,"HHH", 1)

mf1= MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2)

print(portfolio)
print portfolio.history()