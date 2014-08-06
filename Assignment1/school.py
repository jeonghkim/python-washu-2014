class School():
 def __init__(self, school="Haleakala Hippy School"):
  self.school = school
  
 def __str__(self):
  return self.school
  
# def db(self, student, grade):
 # self.student = student
  #self.grade = grade
  #self.roster = {}
  #for i in grade:
   #self.roster['%d'] = [] % i
  #return self.roster

# def add(self, student, grade):
 # self.student = student
  #self.grade = grade
  #return "Add %s to grade %d. \nOK." %(student, grade)

# def school(self,name="Haleakala Hippy School"):
 # return Self(name)
 
hippy = School("hippy school")
print hippy.school

#print hippy.school().add("Jim",2)
#print hippy.school.add("Jim", 2)
#print hippy.school().db("Jim", 2)

