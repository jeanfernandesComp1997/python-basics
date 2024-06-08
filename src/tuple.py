# A tuple is a collection similar to a Python list.
# The primary difference is that we cannot modify a tuple once it is created.

numbers = (1, 2, -5)
print(numbers)

languages = ('Python', 'Swift', 'C++')
print(languages[0])
print(languages[2])

cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
# cars[0] = 'Nissan' throw error
print(cars)

cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
print('Total Items: ', len(cars))

fruits = ('apple', 'banana', 'orange')
for fruit in fruits:
    print(fruit)

tuple_constructor = tuple(('Jack', 'Maria', 'David'))
print(tuple_constructor)

empty_tuple = ()
print(empty_tuple)

names = ('James', 'Jack', 'Eva')
print(names)
float_values = (1.2, 3.4, 2.1)
print(float_values)

mixed_tuple = (2, 'Hello', 'Python')
print(mixed_tuple)

# Tuples are:
# Ordered - They maintain the order of elements.
# Immutable - They cannot be changed after creation.
# Allow duplicates - They can contain duplicate values.

var = ('Hello',)
print(var)  # tuple


def modify_tuple(immutable_tuple, elem):
    return immutable_tuple + (elem,)


numbers = (1, 2, 3)
element = 4
print(modify_tuple(numbers, element))
