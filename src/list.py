# In Python, lists allow us to store a sequence of items in a single variable.

ages = [11, 25, 27]
print(ages)

student = ['Jack', 32, 'Computer Science']
print(student)

empty_list = []
print(empty_list)

x = "axz"
result = list(x)
print(result)

# Lists are:
# Ordered - They maintain the order of elements.
# Mutable - Items can be changed after creation.
# Allow duplicates - They can contain duplicate values.

languages = ['Python', 'Swift', 'Kotlin']
print(languages[0])
print(languages[2])
print(languages[-1])
print(languages[-3])


my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']
# items from index 2 to index 4
print(my_list[2:5])
# items from index 5 to end
print(my_list[5:])
# items beginning to end
print(my_list[:])


fruits = ['apple', 'banana', 'orange']
print(f'Original list: {fruits}')
fruits.append('cherry')
print(f'Updated List: {fruits}')
fruits.insert(2, 'cherry')
print(f'Updated List: {fruits}')


numbers = [1, 3, 5]
print(f'Numbers: {numbers}')
even_numbers = [2, 4, 6]
numbers.extend(even_numbers)
print(f'Updated Numbers: {numbers}')


colors = ['Red', 'Black', 'Green']
print('Original List: ', colors)
colors[2] = 'Blue'
print('Updated List: ', colors)


numbers = [2, 4, 7, 9]
numbers.remove(4)
print(numbers)


names = ['John', 'Eva', 'Laura', 'Nick', 'Jack']
del names[1]
print(names)
del names[1: 4]
# print(names) # Error! List doesn't exist.


cars = ['BMW', 'Mercedes', 'Tesla']
print('Total Elements: ', len(cars))

fruits = ['apple', 'banana', 'orange']


for fruit in fruits:
    print(fruit)


numbers = [n**2 for n in range(1, 6)]
print(numbers)


fruits = ['apple', 'cherry', 'banana']
print('orange' in fruits)    # False
print('cherry' in fruits)    # True
