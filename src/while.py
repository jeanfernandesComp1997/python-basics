number = 1

while number <= 3:
    print(number)
    number = number + 1

inputNumber = int(input('Enter a number: '))

total = 0

while inputNumber != 0:
    total += inputNumber
    inputNumber = int(input('Enter a number: '))

print('The sum is: ', total)
