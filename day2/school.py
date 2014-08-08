class School:
 def __init__(self, schoolname):
  self.schoolname = schoolname
  self.db = {}
  
 def add(self, student, grade):
  if grade in self.db:
   self.db[grade].add(student)
  else:
   self.db[grade] = {student}


 def grade(self, key): # method to call values corresponding to key
  return self.db.get(key, "None") # It will return the default value "None", if key is not available. Otherwise, it returns a value for a given key
  
school = School("Haleakala Hippy School")
school.add("James", 2)
school.add("Blair", 2)
school.add("Paul", 2)

print school.db
print school.db
print school.grade(4)

#print school.db[2]
#print school.db.values()
#print school.db.get(2, "none")
#print school.grade(2)
#print school.db.get(2,"None")