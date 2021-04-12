# Creating Virtual Environments
import sys
sys.path
# Floating Point Arithmetic
format(math.pi, '.12g') # give 12 significant digits
format(math.pi, '.2f') # give two digits after the point
repr(math.pi)
round(.1 + .1 + .1, 10) == round(.3, 10)
x = 3.14159
x.as_integer_ratio()
x == 3537115888337719 / 1125899906842624
x.hex()
x == float.fromhex('0x1.921f9f01b866ep+1')
math.fsum([0.1] * 10) == 1.0
2**52 <= 2**56 // 10 < 2**53
q,r = divmod(2**56, 10)
print(r)
q + 1
7205759403792794 / 2 ** 56
3602879701896397 / 2 ** 55
0.1 * 2 ** 55
3602879701896397 * 10 ** 55 // 2 ** 55
format(0.1, '.17f')
from decimal import Decimal
from fractions import Fraction
Fraction.from_float(0.1)
(0.1).as_integer_ratio()
Decimal.from_float(0.1)
format(Decimal.from_float(0.1), '.17')
# The Interactibe Startup File
import os
filename = os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
    with open(filename) as fobj:
        startup_file = fobj.read()
    exec(startup_file)
# The Customization Module
import site
site.getusersitepackages()