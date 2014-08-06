class School():
 def __init__(self, name):
  self.name = name
  
 def db(self, student, grade):
  self.student = student
  self.grade = grade
  self.roster = {}
  for i in grade:
   self.roster['%d'] = [] % i
  return self.roster

 def add(self, student, grade):
  self.student = student
  self.grade = grade
  return "Add %s to grade %d. \nOK." %(student, grade)

 @classmethod
 def school(cls,name="Haleakala Hippy School"):
  return cls(name)
 
hippy = School("hippy")
print hippy.school().add("Jim",2)
#print hippy.school.add("Jim", 2)
print hippy.school().db("Jim", 2)

