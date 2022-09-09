print('**** Welcome to the LAB grade calculator! ****')
#allows for someone to input the name of person 
name = input('Who are you calculating grades for? ==> ')
#asking user about grades and attendance and letting them know if its between the acceptable range
Lab_grade = float(input('Enter the labs grade? ==> '))
if Lab_grade > 100:
    Lab_grade = 100
    print('The Lab value should have been 100 or less.It has been changed to 100.')
if Lab_grade < 0:
    print('The lab value should have been zero or greater. it had been changed to zero')
Exam_grade = float(input('Enter the Exams grade? ==> '))
if Exam_grade < 0: 
    Exam_grade = 0
    print('The Exam value should have been zero or greater. it had been changed to zero')
if Exam_grade > 100:
    Exam_grade = 100
    print('The Exam value should have been 100 or less.It has been changed to 100.')
Attend_grade = float(input('Enter the Attendance grade? ==> '))
if Attend_grade < 0:
    Attend_grade = 0
    print('The Attendance value should have been zero or greater. it had been changed to zero')
if Attend_grade > 100:
    Attend_grade = 100
    print('The Attendance value should have been 100 or less.It has been changed to 100.')   
#line for calculations of users inputs for grades
gpa = round((Lab_grade * 0.7) + (Exam_grade * 0.2) + (Attend_grade * .1),2)
#Output of the GPA
print(f'The weighted grade for {name} is {gpa}')
#Finds what his grade will be depending on his Gpa avg
if gpa <= 100:
    letter = 'A'
if gpa <=89:
    letter = 'B'
if gpa <=79:
    letter = 'C'
if gpa <= 69:
    letter = 'D'
if gpa <=59:
    letter = 'F'
#Output of the letter grade for users Gpa
print(f'{name} has a letter grade of {letter}')
print('**** Thanks for using the Lab grade calculator ****') 
