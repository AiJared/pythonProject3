# Fancier Output Formatting
year = 2016; event = 'Referendum'
f'Results of the {year} {event}'
yes_votes = 42_572_654 ; no_votes = 43_132_496
'{:-9} YES votes {:2.2%}' .format(yes_votes, percentage)
s = 'Hello, world.'
str(s)
repr(s)
str(1/7)
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is' + repr(x) + ', and y is' + '...'
print(s)
# The repr() of strings adds strings quotes and backslashes
hello =  'hello world \n'
hellos = repr(hello)
print(hellos)
# The argument to repr() may be any python object
repr((x, y('spam', 'eggs')))
# Formatted String Literals
import math
print(f'The value of pi is approximately{math.pi:.3f}.')
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
# Other modifiers can be used to convert the value before it is formatted
animals = 'eels'
print(f'My hovercraft is full of {animals}')
