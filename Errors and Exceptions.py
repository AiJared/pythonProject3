# Handling Exceptions
while True:
    try:
        x = int(input("Please enter the number:"))
        break
    except ValueError:
        print("Oops! That's no a valid number. Try again...")
    except (RuntimeError, TypeError, NameError):
        pass
    class B(Exception):
        pass
    class C(B):
        pass
    class D(C):
        pass
    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print("D")
        except C:
            print("C")
        except B:
            print("B")

import sys

try:
    f = open('My file.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info[0])
    raise
# try... except statement has an optional else clause which when present must follow all except clauses
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
# Initiating an exception first before raising it
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst)) # the exception instance
    print(inst.args) # arguments stored in .args
    print(inst) # __str__ allows args to printed directly
                # but maybe overridden in exception subclasses
    x, y = inst.args # unpack args
    print('x =', x)
    print('y =', y)
# Handling exceptions if they occur in functions even indirectly in the try clause
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
# User-defined Exceptions
class Error(Exception):
    """Base class exceptions for this module."""
    pass
class inputError(Error):
    """Exceptions raised for errors in the input.

    Attributes:
    expression--input expression in which the error occurred
    message--explanation if the error
    """

    def__init__(self, expression, message):
        self.expression = expression
        self.message = message
    class TransitionError(Error):
        """Raised when an operation attempts toa satae transition that is not
        allowed.

        Attributes:
            previous -- state at beginning of transition
            next -- attempted new state
            message -- explanation of why the specific transition is not allowed
            """
    def__init__(self, previous, next, message):
        self.previoius = previous
        self.next = next
        self.message = message
    # Defining clean-up actions
    try:
        raise KeyboardInterrupt
    finally:
        print('Goodbye, world!')
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by zero!")
    else:
        print("result is", result)
    finally:
        print("Executing finally clause")
    divide(2, 1)
    divide(2, 0)
    divide("2", "1")
# Predefined clean-up actions
for line in open("myfile.txt"):
    print(line, end="")
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")


