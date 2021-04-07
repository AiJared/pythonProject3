# Scopes and Name space Example
def scope_test():
    def do_local():
        spam = "local spam"

        def do_nonlocal():
            nonlocal spam
            spam = "nonlocal spam"

        def do_global():
            global spam
            spam = "global spam"

        spam = "test spam"
        do_local()
        print("After local assignment:", spam)
        do_nonlocal()
        print("After nonlocal assignment:", spam)
        do_global()
        print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
# Class Objects
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i
# Instance Objects
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
    print(x.counter)
    del x.counter
# Method Objects
xf = x.f
while True:
    print(xf())
# Class and Instance Variables
class Dog:

    kind = 'canine' # class variable shared by all instances

    def __init__(self, nsme):
        self.name = name # instance variable unique to each instance
    d = Dog('Fido')
    e = Dog('Buddy')
    d.kind                 # shared by all dogs
    e.kind                  # shared by all dogs
    d.name                  # Unique to d
    e.name                  # Unique to e

class Dog:

    tricks = []         # mistaken use of a class variable
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)
    d = Dog('Fido')
    e = Dog('Buddy')
    d.add_trick('roll over')
    e.add_trick('play dead')
    d.tricks              # unexpectedly shared by all dogs
# Correct design of a class should ude an instance variable instead
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = [] # creates a new empty list of each dog
    def add_trick(self, trick):
        self.tricks.append(trick)
    d = Dog('Fido')
    e = Dog('Buddy')
    d.add_trick('roll over')
    e.add_trick('play dead')
    d.tricks
    e.tricks
# Random Remarks
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)
class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
# Methods may call other methods by using method attributes of self argument
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
# Private Variables
class Mapping:
    def __init__(self, iterable):
        self.items_lists = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_lists.append(item)

    __update = update # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for updates()
        # but does not break __init__()
        for items in zip(keys, values):
            self.items_lists.append(item)
# Odds and Ends
class Employee:
    pass

john = Empoyee() # create an empty employee record

# Fill the fields of Employee
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
# Iterators
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')

s = 'abc'
it = iter(s)
it
next(it)
next(it)
next(it)
next(it)

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self,):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
    self.index = self.index - 1
    return self.data[self.index]
rev = Reverse(spam)
iter(rev)
for char in rev:
    print(char)
# Generators
def reverse(data):
    for index in range(len(data) -1, -1, -1):
        yield data[index]
    for char in reverse('golf'):
        print(char)
# Generator Expressions
sum(i*i for i in range(10)) #sum of squares
xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec)) # dot product
from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
unique_words = set(word for line in page for word in line.split())
valedictorian = max((student.gpa, student.name) for students in graduates)
data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))