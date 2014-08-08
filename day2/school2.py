class School:
 def __init__(self, schoolname):
  self.schoolname = schoolname
  self.studentname = []
  self.grades = []
  self.db = {}
  
 def add(self, student, grade):
  self.studentname.append(student)
  self.grades.append(grade)
  self.db = dict(zip(self.grades, self.studentname))
  self.db = self.db.update(self.grades : self.studentname)
 
 #def grade(self, key): # method to call values corresponding to key
  #self.key = key
  #return self.db.get(self.key, "None")
  
school = School("Haleakala Hippy School")
school.add("James", 2)
school.add("Blair", 2)
school.add("Paul", 2)

print school.db

print school.db[2]
