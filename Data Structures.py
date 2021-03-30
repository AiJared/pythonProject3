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





