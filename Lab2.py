print('**** Welcome to the LAB grade calculator! ****')
#allows for someone to input the name of person and numbers to be calculated
name = input('Who are you calculating grades for? ==> ')
lgrade = float(input('Enter the labs grade? ==> '))
Egrade = float(input('Enter the Exams grade? ==> '))
Agrade = float(input('Enter the Attendance grade? ==> '))
#line for calculations of users inputs for grades
total = round((lgrade * 0.7) + (Egrade * 0.2) + (Agrade * .1),2)
#Output of the GPA
print(f'The weighted grade for {name} is {total}')
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
