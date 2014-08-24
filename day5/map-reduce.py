# setup
items = range(1, 5)

def sqr(x): return x**2

def cub(x): return x**3

<<<<<<< HEAD
# mapping: can be run in different machines in parallel, can be summed by using reduce().
for x in items: sqr(x)

print items
print map(sqr, items)
print list(map((lambda x: x **2), items)) # create a function lambda and map this into items
# 
=======
# mapping
for x in items sqr(x)
map(sqr, items)
list(map((lambda x: x **2), items))

>>>>>>> upstream/master
funcs = [sqr, cub]
for i in items:
    value = map(lambda x: x(i), funcs)
    print value
<<<<<<< HEAD
# 
=======

>>>>>>> upstream/master
def mymap(aFunc, aSeq):
  result = []
  for x in aSeq: result.append(aFunc(x))
  return result
<<<<<<< HEAD
# 
print mymap(sqr, [1,2,3])
# 
# reducing and filtering
# range(-5, 5)
# filter((lambda x: x < 0), range(-5,5))
# 
# from functools import reduce
# reduce( (lambda x, y: x * y), items ) # summing
# 
# def myreduce(fnc, seq):
#   total_so_far = seq[0]
#   for next in seq[1:]:
#     total_so_far = fnc(total_so_far, next)
#   return total_so_far
# 
# L = ['Testing ', 'shows ', 'the ', 'presence', ', ','not ', 'the ', 'absence ', 'of ', 'bugs']
# reduce( (lambda x,y:x+y), L)
# 
# reduce( (lambda x,y:x+y), map(len, L))
# 
# reduce( (lambda x,y:x+y), map(sqr, items)) # returns sum of squares
=======

mymap(sqr, [1,2,3])

# reducing and filtering
range(-5, 5)
filter((lambda x: x < 0), range(-5,5))

from functools import reduce
reduce( (lambda x, y: x * y), items )

def myreduce(fnc, seq):
  total_so_far = seq[0]
  for next in seq[1:]:
    total_so_far = fnc(total_so_far, next)
  return total_so_far

L = ['Testing ', 'shows ', 'the ', 'presence', ', ','not ', 'the ', 'absence ', 'of ', 'bugs']
reduce( (lambda x,y:x+y), L)


reduce( (lambda x,y:x+y), map(sqr, items))
>>>>>>> upstream/master
