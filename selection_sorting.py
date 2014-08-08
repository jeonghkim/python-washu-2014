# Recursion case: Fibonacci numbers

def fib(n):
 if n <=1: # base case
  return n
  return fib(n-1) + fib(n-2)

# bubbling up to the top!
# fib(4) = fib(3) + fib(2) = 3
# fib(3) = fib(2) + fib(1) = 2 
# fib(2) = fib(1) + fib(0) = 1
# fib(1) = 1
# fib(0) = 0


for i in range(10):
 print "{0} : {1} ".format(i, fib(i)) # return fibonacci number of numbers in the range 0:9
 
  