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