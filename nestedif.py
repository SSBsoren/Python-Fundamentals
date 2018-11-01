#Nested if statement
age=int(input('Enter the age'))
if age >= 18:
    print('Adult')
elif age >=60:
    print('Old')
else:
    if age >=13:
        print('Teenager')
    else:
        print('Child')
        