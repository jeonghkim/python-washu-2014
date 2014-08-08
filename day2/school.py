class School:
 def __init__(self, schoolname):
  self.schoolname = schoolname
  self.db = {}
  self.students = []
  self.grades = []
  
 def add(self, student, grade):
  self.student = student
  self.grade = grade
  self.students.append(self.student)
  self.grades.append(self.grade)
  #self.db = dict(zip(self.grades, self.students))
  self.db.setdefault(self.grade, {})
 # self.db[self.grade].append(self.students)
  self.db.update({self.grade: self.student})
 

 def grade(self, key): # method to call values corresponding to key
  self.key = key
  return self.db.get(self.key, "None")
  
school = School("Haleakala Hippy School")
school.add("James", 2)
school.add("Blair", 2)
school.add("Paul", 3)

print school.db
print school.db[2]
#print school.db[2]
#print school.db.values()
#print school.db.get(2, "none")
#print school.grade(2)
#print school.db.get(2,"None")