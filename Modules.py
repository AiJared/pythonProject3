# Fibonacci numbers module
def fib(n):             # write fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end='')
        a, b = b, a + b
    print()
def fib2(n):            # return fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
        return result
import fibo
fibo.fib(1000)
fibo.fib2(100)
fibo.__name__
fib = fibo.fib
fib(500)
# More on Modules
from fibo import fib, fib2
fib(500)
print(fib)
# There is a variant to import all names that a module defines
from fibo import *
fib(500)
# Module name followed by 'as'
import fibo as fib
fib(500)
# It can also be used when utilizing from with similar effects
from fibo import fib as fibonacci
fibonacci(500)
# Executing Modules as scripts
if __name__ == '__main__':
    import sys
    fib (int(sys.argv[1]))
# Standard Modules
import sys
sys.ps1
sys.ps2
sys.ps1 = 'C >'
C > print('Yulk!')
import sys
sys.path.append('/ufs/guido/lib/python')
# The dir() function
# it is used to find out which names a module defines.
# Returns a sorted list of strings
import fibo, sys
dir(fibo)
dir(sys)
# Without arguments, dir() lists the names you have defined currently
a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
dir()
import builtins
dir(builtins)
# Packages
# Users of the package can import individual modules from the package
import sound.effects.echo
sound.effects.echo.echofilter(input, output, delay = 0.7, atten = 4)
# An alternative way of importing submodules
from sound.effects import echo
echo.echofilter(input, output, delay = 0.7, atten = 4)
# Importing the desired function or variable directly
from sound.effects.echo import echofilters
echofilters(input, output, delay = 0.7, atten = 4)
# Import * from a package
__all__ = ["echo", "surround", "reverse"]
import sound.effects.echo
import sound.effects.surround
import sound.effects
# Intra-package reference
from . import echo
from .. import formats
from ..filters import equalizer




