### CLASSES ###
# Student #
class Student:
  #CONSTRUCTOR | Creates 'name', 'year', 'grades' variables
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
    self.avg_score = 0
  #METHOD | Adds grade to 'grades list'
  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)
  #METHOD | Returns students average score
  def get_average(self):
    grade_count = 0
    grade_sum = 0
    for gradeIndex in range(len(self.grades)):
      grade_count += 1
      grade_sum += int(str(self.grades[gradeIndex]))
      grade_avg = grade_sum / grade_count
    return grade_avg
  #STRING REPRESENTATION | Student objects print 'name', 'year', 'grades'
  def __repr__(self):
    return "STUDENT: {name}, YEAR: {year}, GRADES: {grades}".format(name=self.name, year=self.year, grades=self.grades)

# Grade #
class Grade:
  #CONSTRUCTOR | Creates 'score' variable
  def __init__(self, score):
    self.score = score
  #METHOD | Returns if a Grade is a PASS or FAIL. 
  def is_passing(self):
    minimum_passing = 65
    if self.score >= minimum_passing:
      return "PASS"
    else:
      return "FAIL"
  #STRING REPRESENTATION | Grade objects print 'score' in a string
  def __repr__(self):
    return "{score}".format(score=self.score)
  
### DATA INGESTION ###
#Load Students
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

student_list = [roger, sandro, pieter]

#Load Grades
pieter.add_grade(Grade(100))
pieter.add_grade(Grade(93))

roger.add_grade(Grade(100))
roger.add_grade(Grade(0))

sandro.add_grade(Grade(87))
sandro.add_grade(Grade(76))

### FUCNTIONS ###
# Show Students #
def ShowStudents(students):
  for student in students:
    print(student)
    
# Show PASS or FAIL for a students grades #
def passORfail(student):
  students_grades = student.grades
  for grade in students_grades:
    tempGrade = Grade(int(str(grade)))
    print(tempGrade.is_passing())

### MAIN ###
#Show all Students
#ShowStudents(student_list)

#Show each student and their grade average
print("ALL STUDENTS:")
print("*~*~*~*~*~*~*")
      
pieters_avg = pieter.get_average()
print(pieter)
print("GRADE AVERAGE: " + str(pieters_avg))
print("____________________")

roger_avg = pieter.get_average()
print(roger)
print("GRADE AVERAGE: " + str(roger_avg))
print("____________________")

sandro_avg = sandro.get_average()
print(sandro)
print("GRADE AVERAGE: " + str(sandro_avg))
print("____________________")

