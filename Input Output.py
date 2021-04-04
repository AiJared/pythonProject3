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
# The String format() method
print('We are the {} who say "{}"!'.format('knights', 'Ni'))
print('{0}' and '{1}'.format('spam', 'eggs'))
print('{1}' and '{0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(
    food='spam', adjective='absolutely horrible'
))
# Positional and keyword arguments can be arbitrarily combined
print('The story of {0}, {1} and {other}.'.format('Bill', 'Manfred', other='George'))
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ' 'Dcab: {0[Dcab]:d'.format(table))
# Using '**' notation to pass the table as keyword arguments
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
# Manual String Formatting
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end='')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
# str.zfill() method
'12'.zfill(5)
'-3.14'.zfill(7)
'3.14159265359'.zfill(5)
# The Old String Formatting
import math
print('The value of pi is approximately %5.3f.' %math.pi)
# Reading and writing files
f = open('workfile', 'w')
with open('workfile') as f:
    read_data = f.read()
    f.closed
# Methiods of file objects
f.read()
f.read()
f.readline()
f.readline()
f.readline()
# Looping over the file object
for line in f:
    print(line, end='')
f.write('This is a test \n')
# Converting objects either to string(in text mode) or bytes(in binary mode)
value = ('The answer', 42)
s = str(value) # convert the tuple to string
f.write(s)
# from_what arguments
f = open('workfile', 'rb+')
f.write(b'012345678abcdef')
f.seek(5) # Go to the 6th byte in the file
f.read(1)
f.seek(-3, 2) # Go to the 3rd value before the end
f.read(1)
# Saving structured data with json
import json
json.dumps([1, 'simple', 'list'])
# dump() serializes the object to a text file
json.dump(x, f)
x = json.load(f)