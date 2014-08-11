## HW 2: Build a piece of software for a financial institution to model one of their clients' portfolios. 
# Jeong

# A portfolio can consist of 3 types of items:
# 1. Cash
# 2. Stock
# 3. Mutual Funds
# + Bonds

import random # import random library to use random.uniform()

class Portfolio():
 def __init__(self): # Initialize the class Portfolio
  self.cash = 0 # Specify elements of Portfolio
  self.stock = {}
  self.mutualfunds = {}
  self.History = []
  
 def __str__(self):
  assets = "cash: $%r\n" % (self.cash)
  assets += "stock: %r\n" %(self.stock)
  assets += "mutual funds: %r" %(self.mutualfunds)
  return assets
       
 def addCash(self, amount): # Define addCash methods 
  self.cash += amount # the element cash will add up the input amount
  self.transaction = "added $%r" % (amount) 
  self.History.append(self.transaction) # Append the transaction 
  return self.cash 

 def withdrawCash(self, amount): # Define withdrawCash methods
  if amount > self.cash: # if the input amount is greater than the amount of cash in portfolio:
   print "Transaction unavailable: Cash will be overdrawn." # print this message.
  else: # Otherwise, 
   self.cash -= amount # the element cash will lose the input amount
   self.transaction = "withdrew $%r" % (amount)
   self.History.append(self.transaction)
  return self.cash 
  
 def buyStock(self, share, stock): # Define buyStock method
  self.ticker = stock.ticker
  self.price = stock.price
  if self.ticker in self.stock: # if the ticker is in the dictionary self.stock in portfolio instance:
   self.stock[self.ticker] += share # add up the share
  else:
   self.stock[self.ticker] = share
  self.price = random.uniform(0.5*stock.price, 1.5*stock.price) # price is drawn from unif[0.5*price, 1.5*price]
  self.cash -= self.price * share # subtract the amount of price * share from cash
  self.transaction = "bought %r share of %r" % (share, self.ticker)
  self.History.append(self.transaction)
  
 def sellStock(self, share, stock):
  self.ticker = stock.ticker
  self.price = random.uniform(0.5*stock.price, 1.5*stock.price)
#   try: # try the following
#    self.stock[self.ticker] -= share
  if self.ticker not in self.stock: # if there's no stock named ticker:
   return "No stock named %s" %ticker # return this message
  elif self.stock[self.ticker] < share:
   print "Transaction unavailable: Not enough share"
  else:
   self.stock[self.ticker] -= share
   self.cash += self.price * share
   self.transaction = "sold %r share of %r" % (share, self.ticker)
   self.History.append(self.transaction)
     
 def buyMutualFund(self, share, mutualfunds):
  self.share = float(share) # Convert share into float since mutual funds can be only purchased as fractional shares
  self.symbol = mutualfunds.symbol
  if self.symbol in self.mutualfunds:
   self.mutualfunds[self.symbol] += self.share
  else: 
   self.mutualfunds[self.symbol] = self.share
  self.price = random.uniform(0.9, 1.2)
  self.cash -= self.price * self.share
  self.transaction = "bought %r share of %r" % (self.share, self.symbol)
  self.History.append(self.transaction)

 def sellMutualFund(self, symbol, share):
  self.share = float(share) # Convert share into float since mutual funds can be only purchased as fractional shares
  self.symbol = symbol
  try: 
   self.mutualfunds[self.symbol] -= self.share
  except:
   return "No mutual funds named %s" %symbol
  self.price = random.uniform(0.9, 1.2)
  self.cash += self.price * self.share
  self.transaction = "sold %r share of %r" % (self.share, self.symbol)
  self.History.append(self.transaction)

 def history(self): #define the method history
  return self.History
    
class Stock(): # Define class Stock
 def __init__(self, price, ticker):
  self.price = price
  self.ticker = ticker

class MutualFund(): # Define Class MutualFund
 def __init__(self, symbol):
  self.symbol = symbol
  
# Using inheritance, show how it would be easy to add a third type of investment--Bonds--to the mix.
class Bonds(MutualFund):
 def __init__(self, symbol, price):
  MutualFund.__init__(self, symbol) # initialize Bonds as a subclass of MutualFund. and take care of stuff inherited from superclass
  self.price = price
  
    
portfolio = Portfolio()
portfolio.addCash(300.50)
portfolio.withdrawCash(400)
s = Stock(20, "HFH")


portfolio.buyStock(5, s)
portfolio.sellStock(3, s)

mf1= MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2)

bond1 = Bonds("BRT", 20)
print(portfolio)
print portfolio.history()
print portfolio.stock

