## HW 3: Implement two different sorting algorithms. 
# Jeong

import random
# 1. selection sorting algorithm: The complexity class of selection sorting algorithm is O(n^2)

def selection(list=[]): # selection function takes an argument of list
 for i in range(0, len(list)-1): # Define the first through the last-1 index in list: (Notice that we don't need to go over the last element)
  min_index = i # as "min_index"
  for j in range(i+1, len(list)): # Loop j from the next to the last element index in list,
   if list[j] < list[min_index]: # if the j-th element of list is smaller than min_index element of list,
    min_index = j # now min_index becomes j
  if i < min_index: # if i is less than min_index, 
    list[min_index], list[i] = list[i], list[min_index] # swap the min_index element and the i-th element of the list. 
 return list 
 

# 2. merge_sort algorithm: The complexity class of merge_sort algorithm is O(nlogn)

def merge_sort(list=[]): 
 if len(list) <=1: return list
 left = list[:len(list)/2]
 right = list[len(list)/2 : len(list)]
 left = merge_sort(left) # recursion takes place
 right = merge_sort(right)
 return merge(left, right)

def merge(left, right):
 i = 0
 j = 0
 merged = [] 
 while len(merged) < len(left) + len(right):
  if i < len(left) and j < len(right):
   if left[i] < right[j]:
    merged.append(left[i])
    i += 1
   else:
    merged.append(right[j])
    j += 1
  if i == len(left):
   merged.extend(right[j:])
  if j == len(right):
   merged.extend(left[i:])
 return merged

 # 3. quick_sort algorithm
def quick_sort(myList):
 if len(myList) <= 1: return myList
 else:
	i = random.sample(range(len(myList)), 1)[0] # Choose a random pivot such that pivot = myList[i].
	pivot = myList.pop(i) # Now, myList excludes pivot.
	left = [] # An empty list that will contain the values smaller than pivot.
	right = [] # An empty list that will contain the values greater than pivot.
	for j in range(len(myList)):
	 if myList[j] <= pivot:
	  left.append(myList[j])
	 else:
	  right.append(myList[j])
	left = quick_sort(left) # By recursion, we keep selecting a random pivot and partitioning myList.  
	right = quick_sort(right)
	left.append(pivot) # Add the initial pivot to the left list.
	return left + right