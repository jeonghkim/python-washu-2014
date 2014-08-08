class School:
 def __init__(self, schoolname): # initialize: it takes the argument "schoolname"
  self.schoolname = schoolname # the element schoolname will be the input for the argument schoolname
  self.db = {} # the element "db" will be an empty dictionary.
  
 def add(self, student, grade): # add method takes the argument "student" and "grade"
  if grade in self.db: # if the input of grade already exists as a key in dict self.db:
   self.db[grade].add(student) # it will add the student name to the value for that key
  else: 
   self.db[grade] = {student} # Otherwise, it will add a new key with and the matching value 


 def grade(self, key): # grade method is to call values corresponding to key
  return self.db.get(key, None) # It will return the default value None, if key is not available. Otherwise, it returns a value for a given key
  
 def sort(self): # sort is a method to return a dictionary where values are sorted (and in the form of tuple). It doesn't take any argument
  sorted_students = {} # create an empty dictionary 
  for key in self.db.keys(): # 
   sorted_students[key] = tuple(sorted(self.db.get(key))) # Add a key to the dict sorted_student and assign matching values in self.db.
   # it is sorted and tupled.
  return sorted_students
  
# school = School("Haleakala Hippy School")
# # school.add("James", 2)
# # school.add("Blair", 2)
# # school.add("Paul", 2)
# 
# school.add("Jennifer", 4)
# school.add("Kareem", 6)
# school.add("Christopher", 4)
# school.add("Kyle", 3)


# print school.db
# print school.grade(4)
# print school.sort()