num =int(input('Enter the number :'))
if 9 < num < 99:
    print('Two digit number')
elif 99 < num < 999:
    print('Three digit number')
elif 999 < num <9999:
    print('Four digit number')
else:
    print('Number is <=9 or >=9999')