import sorting
import random
import timeit
import matplotlib.pyplot as plt

def sim_sort(n, niter = 100): # sim_sort takes argument nsim--the number of sample-- and niter--the number of simulation iterations-- set 100 as default.
 time_selection = []
 time_merge = []
 avg_selection = []
 avg_merge = []
 for i in range(1, n+1):
  random_num = random.sample(range(1, i+1), i) # Create a sample of i random numbers
  time_selection = timeit.Timer('sorting.selection(%s)' %(random_num), 'from __main__ import sorting').timeit(niter)
  time_merge = timeit.Timer('sorting.merge_sort(%s)' %(random_num), 'from __main__ import sorting').timeit(niter)
  avg_selection.append(time_selection/niter)
  avg_merge.append(time_merge/niter)
 return [avg_selection, avg_merge]

data = sim_sort(500)
plt.plot(data[0], label="selection sorting")
plt.plot(data[1], label="merge sorting")
plt.ylabel("Runtime")
plt.xlabel("Size of set to sort")
plt.legend(loc = "lower right", numpoints = 1)
plt.show()
plt.savefig('runtime.pdf')