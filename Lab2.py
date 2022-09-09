print('**** Welcome to the LAB grade calculator! ****')
#allows for someone to input the name of person and numbers to be calculated
name = input('Who are you calculating grades for? ==> ')
Lab_grade = float(input('Enter the labs grade? ==> '))
Exam_grade = float(input('Enter the Exams grade? ==> '))
Attend_grade = float(input('Enter the Attendance grade? ==> '))
#line for calculations of users inputs for grades
gpa = round((Lab_grade * 0.7) + (Exam_grade * 0.2) + (Attend_grade * .1),2)
#Output of the GPA
print(f'The weighted grade for {name} is {gpa}')
#Finds what his grade will be depending on his Gpa avg
if total <= 100:
    letter = 'A'
if total <=89:
    letter = 'B'
if total <=79:
    letter = 'C'
if total <= 69:
    letter = 'D'
if total <=59:
    letter = 'F'
#Output of the letter grade for users Gpa
print(f'{name} has a letter grade of {letter}')
