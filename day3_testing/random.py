class School:
    db = 2
 
class school:
    school = School()
 
    def __init__(self):
        self.school.db = 1

c = School()
db = School()
print c.school.db 