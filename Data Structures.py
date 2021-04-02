# More on Lists
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.count('tangarine')
fruits.index('banana')
fruits.index('banana', 4)# Find the next banana starting a position 4
print(fruits)
fruits.reverse()
print(fruits)
fruits.append('grapes')
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()
print(fruits)
#Using Lists as Stacks
stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
stack.pop()
print(stack)
# Using Lists as queues
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry") # Terry arrives
queue.append("Graham") # Graham arrives
print(queue)
queue.popleft()
queue.popleft()
print(queue)
# List Comprehensions
squares = []
for x in range(10):
    squares.append(x**2)
    print(squares)
# The two codes below help to achieve the same task in a simpler way
square = list(map(lambda x: x**2, range(10)))
print(square)
square = [x**2 for x in range(10)]
print(square)
[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
combs = []
for x in (1,2,3):
    for y in (3,1,4):
        if x != y:
            combs.append((x,y))
print(combs)
vec = [-4, - 2, 0, 2, 4]
print(vec)
# create a new list with the values doubled
[x*2 for x in vec]
# filter the list to exclude negative numbers
[x for x in vec if x >= 0]
# apply  a function to all elements
[abs(x) for x in vec]
# call a method on each element
freshfruit = ['banana', 'loganberry', 'passion fruit']
[weapon.strip() for weapon in freshfruit]
# create a list of two tuples like (number, squares)
[(x,x**2) for x in range(6)]
# flatten a list by using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]
from math import pi
[str(round(pi, i)) for i in range(1, 6)]
# Nested List comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
[[row[i] for row in matrix] for i in range (4)]
transposed = []
for i in range(4):
    # the following three lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.apend(row[i])
        transposed.append(transposed_row)
        print(transposed)
# The zip() function
list(zip(*matrix))
# The Delete Statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print (a)
del a[2:4]
print(a)
del a[:]
print (a)
del a
# Tuples and Sequences
t = 12345, 54321, 'hello!'
t[0]
print(t)
# Tuples may be Nested
u = t, (1, 2 , 3, 4)
print(u)
# Tuples are immutable
t[0] = 88888
# but the can also contain mutable objects
v = ([1, 2, 3], [3, 2, 1])
print(v)
# Sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
'orange' in basket            # fast membership
'crabgrass' in basket
# Demonstrates set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a) # unique letters in a
print(b) # unique letters in b
print(a-b) # letters in a but not in b
print(a | b) # letters in a, b or both
print(a & b) # letters in both a and b
print(a ^ b) # letters a or b but not both
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
# Dictionaries
tel = {'jack': 4098, 'sap': 4139}
tel['guido'] = 4127
print(tel)
tel['jack']
del tel['sape']
tel['irv'] = 4127
list(tel)
sorted(tel)
'guido' in tel
'jack' not in tel
# The dict() constructor builds dictionaries directly from the sequence of key value pairs
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{x: x ** 2 for x in (2, 4, 6)}
dict(sape = 4139, guido = 4127, jack = 4098)
# Looping Techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k,v)
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i,v)
# Looping over two or more sequences using zip() function
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))
# To loop over a sequence of reverse call the reversed() function
for i in reversed(range(1,10,2)):
    print(i)
# To loop over a sequence in sorted order using sorted() function
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
# Creating new list while looping
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)
# More on Conditions
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)
# Comparing Sequences and other types
(1, 2, 3)        <(1, 2, 4)
[1, 2, 3]        <[1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)      <(1, 2, 4)
(1, 2)            <(1, 2, -1)
(1, 2, 3)         ==(1.0, 2.0, 3.0)
(1, 2 ('aa', 'ab'))<(1, 2 ('abc', 'a'), 4)




