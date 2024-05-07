import random
import math

num1 = 5
print(num1, 'is of type', type(num1))

num2 = 5.42
print(num2, 'is of type', type(num2))

num3 = 8 + 2j
print(num3, 'is of type', type(num3))

# Number System	Prefix
# Binary	0b or 0B
# Octal	0o or 0O
# Hexadecimal	0x or 0X

print(0b1101011)

print(0xFB + 0b10)

print(0o15)

print(1 + 2.0)

num1 = int(2.3)
print(num1)

num2 = int(-2.8)
print(num2)

num3 = float(5)
print(num3)

num4 = complex('3+5j')
print(num4)

print(random.randrange(10, 20))

list1 = ['a', 'b', 'c', 'd', 'e']

print(random.choice(list1))

random.shuffle(list1)

print(list1)

print(random.random())

print(math.pi)
print(math.cos(math.pi))
print(math.exp(10))
print(math.log10(1000))
print(math.sinh(1))
print(math.factorial(6))

ages = [19, 26, 29]
print(ages)

languages = ['Python', 'Swift', 'C++']
print(languages[0])
print(languages[2])

fruits = ['apple', 'banana', 'orange']
fruits.append('cherry')
print('Updated List: ', fruits)

colors = ['Red', 'Black', 'Green']
print('Original List: ', colors)
colors[2] = 'Blue'
print('Updated List: ', colors)

numbers = [2, 4, 7, 9]
numbers.remove(4)
print(numbers)

cars = ['BMW', 'Mercedes', 'Tesla']
print('Total Elements: ', len(cars))

fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)
