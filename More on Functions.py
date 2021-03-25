def concat(*args, sep="/"):
    return sep.join(args)
concat("earth", "mars", "venus",)
concat("earth", "mars", "venus", sep=".")

# Unpacking Arguments
list(range(3, 6)) # normal call with separate arguments
args = [3, 6]
list(range(args)) # call with arguments unpacked from a list
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end='')
    print("If you put", voltage, "volts through it.", end='')
    d = {"Voltage:" "four million", "state:" "bleedin' demised", "action:" "VOOM"}
    parrot(**d)

# Lambda Expressions
def make_incrementor(n):
    return lambda x: x + n
pairs = [(1, 'one'), (2, 'two'), (3, 'three'),(4, 'four')]
pairs.soght(key=lambda pair: pair[1])
pairs

#Documentation strings
def function():
    """Identify all the objects under the function
    If any output them on the screen"""
    pass
print(function. __doc__)

#Function Annotations
def f(ham: str, eggs:str= 'eggs') -> str:
     print("Annotations:", f. __annotations__)
     print("Arguments:", ham, eggs)
     return ham + 'and' + eggs
f('spam')


