number = int(input('Enter a number: '))

if number > 0:
    print('Number is positive')

print('This statement always executes')

if number > 0:
    print('Positive number')
else:
    print('Negative number')

print('This statement always executes')

if number > 0:
    print('Positive number')
elif number < 0:
    print('Negative number')
else:
    print('Zero')

print('This statement always executes')

if number >= 0:
    if number == 0:
        print('Number is 0')
    else:
        print('Number is positive')
else:
    print('Number is negative')
