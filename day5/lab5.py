"""Data Structures
Working with Graphs/Networks"""

# Name types of graph
# ring graph: each node has two edges
# 

def makeLink(G, node1, node2): #
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1 # (): checks the order 
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G 

# def make2Link(G, node1, node2, node3): #
#   if node1 not in G:
#     G[node1] = {}
#   (G[node1])[node2] = 1 # (): checks the order 
#   if node2 not in G:
#     G[node2] = {}
#   (G[node3])[node2] = 1
# #   if node3 not in G:
# #     G[node3] = {}
# #   (G[node3])[node2] = 1
# #   (G[node2])[node3] = 1
#   return G 
def make2Link(G, node1, node2, node3):
 if node1 not in G:
   G[node1] = {}
 (G[node1])[node2] = 1 
 if node2 not in G:
    G[node2] = {}
 (G[node2])[node1] = 1
 if node3 not in G:
    G[node2] = {}
 (G[node3])[node2] = 1
 return G 


# makeLink({}, "WashU", "Forest Park")
# 
# #this returns: {{"WashU": {""Forest Park" : 1}}
# 
# # Ring Network
# # ring = {} # empty graph 
# # 
# # n = 5 # number of nodes 
# 
# # Add in edges
# for i in range(n):
#   ring = makeLink(ring, i, (i+1))
# 
# 

n = 255
myGraph = {}

end1 = []
for i in range(n):
 if i % 16 == 15:
  end1.append(i)
  
end2 = []
for i in range(240, 255):
  end2.append(i)

for i in range(n):
 if i in end1 :
  myGraph = makeLink(myGraph, i, (i+16))
 if i in end2 :
  myGraph = makeLink(myGraph, i, (i+1))
 else :
  myGraph = make2Link(myGraph, i, (i+1), (i+16))
#  myGraph = makeLink(myGraph, i, (i+1))


  

# How many nodes?
print len(ring)
print ring
# How many edges?
print sum([len(ring[node]) for node in ring.keys()])/2 

# def makeTwoLink(G, node1, node2, node3):
#  if node1 not in G:
#    G[node1] = {}
#  (G[node1])[node2] = 1 
#  if node2 not in G:
#     G[node2] = {}
#  (G[node2])[node1] = 1
#  if node3 not in G:
#     G[node2] = {}
#  (G[node3])[node2] = 1
#  return G 

  



# Grid Network
# TODO: create a square graph with 256 nodes and count the edges # grid with 16**2 = 256
# TODO: define a function countEdges
# 
#  square = {}
#  
#  n = 4
#  
#  # Add in edges
#  for i in range(n):
#   square = makeLink(square, node1, node2)
# 
# 
# 
# Social Network
# class Actor(object):
#   def __init__(self, name):
#     self.name = name 
# 
#   def __repr__(self):
#     return self.name 
# 
# ss = Actor("Susan Sarandon")
# jr = Actor("Julia Roberts")
# kb = Actor("Kevin Bacon")
# ah = Actor("Anne Hathaway")
# rd = Actor("Robert DiNero")
# ms = Actor("Meryl Streep")
# dh = Actor("Dustin Hoffman")
# 
# movies = {}
# 
# makeLink(movies, dh, rd) # Wag the Dog
# makeLink(movies, rd, ms) # Marvin's Room
# makeLink(movies, dh, ss) # Midnight Mile
# makeLink(movies, dh, jr) # Hook
# makeLink(movies, dh, kb) # Sleepers
# makeLink(movies, ss, jr) # Stepmom
# makeLink(movies, kb, jr) # Flatliners
# makeLink(movies, kb, ms) # The River Wild
# makeLink(movies, ah, ms) # Devil Wears Prada
# makeLink(movies, ah, jr) # Valentine's Day
# 
# How many nodes in movies?
# How many edges in movies?
# 
# def tour(graph, nodes):
#   for i in range(len(nodes)):
#     node = nodes[i] 
#     if node in graph.keys():
#       print node 
#     else:
#       print "Node not found!"
#       break 
#     if i+1 < len(nodes):
#       next_node = nodes[i+1]
#       if next_node in graph.keys():
#         if next_node in graph[node].keys():
#           pass 
#         else:
#           print "Can't get there from here!"
#           break 
# 
# TODO: find an Eulerian tour of the movie network and check it 
# movie_tour = [] 
# tour(movies, movie_tour)
# 
# 
# def findPath(graph, start, end, path=[]):
#         path = path + [start]
#         if start == end:
#             return path
#         if not graph.has_key(start):
#             return None
#         for node in graph[start]:
#             if node not in path:
#                 newpath = findPath(graph, node, end, path)
#                 if newpath: return newpath
#         return None
# 
# print findPath(movies, jr, ms)
# 
# 
# TODO: implement findShortestPath()
# print findShortestPath(movies, ms, ss)
# 
# TODO: implement findAllPaths() to find all paths between two nodes
# allPaths = findAllPaths(movies, jr, ms)
# for path in allPaths:
#   print path