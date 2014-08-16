## HW 4: Singly Linked List 
# Jeong

class Node:
 def __init__(self, _value=None, _next=None):
  self.value = _value
  self.next = _next
  
 def __str__(self):
  return str(self.value) # returns string representation of value

class LinkedList:
 def __init__(self, value):
  '''takes a number and sets it as the value at the head of the List'''
  self.value = value
  self.head = Node(_value = value, _next = None)
  self.tail = self.head
  self.length = 1

 def length(self): # Returns the length of the list
  return self.length
  
 def addNode(self, new_value): 
  '''takes a number and adds it to the end of the list'''
  node_to_add = Node(new_value)
  current = self.head
  if current.next != None:
   current = current.next
   current.next = node_to_add
  else:
   self.head.next = node_to_add.value
   self.tail = node_to_add
  self.length += 1 # Complexity class: O(1)
 
 def addNodeAfter(self, new_value, after_node): 
  '''takes a number and adds it after the after_node'''
  new_node = Node(new_value)
  current = self.head
  while str(current) != str(after_node):
   current = current.next
  if str(current) == str(after_node):
   current = new_node
   self.length +=1 # Complexity class: O(n)

   
 def addNodeBefore(self, new_value, before_node):
  '''takes a value and adds before the before_node'''
  new_node = Node(new_value)
  current = self.head
  while str(current) != str(before_node):
   current = current.next
  if str(current) == str(before_node):
   self.length +=1
   self.head = Node(new_value, current) # Complexity class: O(n)
    
 def removeNode(self, node_to_remove):
  '''removes a node from the list'''
  current = self.head
  while str(current) != str(node_to_remove):
   current = current.next
  if str(current) == str(node_to_remove):
   self.length -=1 # Complexity class: O(n)
   
 def removeNodesByValue(self, value):
  '''takes a value, removes all nodes with that value'''
  current = self.head
  while str(current) != str(value):
   current = current.next
  if str(value) == str(current):
   self.length -=1
   current = Node(current.next, current.next.next)
   return self.current # Complexity class: O(n)
   
 def reverse(self):
  '''Reverses the order of the linked list'''
  temp = self.head
  current = Node(self.head)
  while str(temp.next) != None: 
   temp = temp.next 
   current = Node(temp, current) # reverse the order by setting current as the next node
   return self.head # Complexity class: O(n)
 
 def __str__(self):
  '''Displays the list in some reasonable way'''
  current = self.head
  print_this = "LinkedList: "
  print_this += str(current.value)
  while current.next != None:
   current = current.next
   print_this += "->" + str(current.value)
  return print_this
   
# MyList = LinkedList(2)
# 
# MyList.addNode(5) 
# print MyList.length # check whether it returns 2
# 
# MyList.addNodeAfter(9, MyList.head)
# print MyList.length # Now, check whether it returns 3.
# 
# MyList.addNodeBefore(6, 5)
# print MyList.length # Now, check whether it returns 4.
# 
# MyList.removeNode(MyList.head)
# print MyList.length # Now, check whether it returns 3.
# 
# MyList.removeNodesByValue(6)
# print MyList.length # now, check whether it returns 2. 
# # 
# # # MyList.reverse() 
# print MyList

