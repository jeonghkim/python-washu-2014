class List():
 def __init__(self):
  self.head = None
  self.next = None
   
l = List()
l.head = 1


# queue: not a native data structure; first in first out method
from Queue import Queue
q = Queue()
q.put(1)
q.put(2)
q.get() # it returns 1
