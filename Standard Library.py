# Operating System Interface
import os
os.getcwd()         # Return the current working directory
os.chdir('/server/accesslogs') # change current working directory
os.system('mkdir today') # Run the command mkdir in the system shell
import os
dir(os)
help(os)
# shutil module provides a higher level interface that is easier to use
import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')
# File Wildcards
import glob
glob.glob('*.py')
# Command Line Arguments
import sys
print(sys.argv)
# Error Output Redirection and Program Termination
sys.stderr.write('Warning, log file not found starting a new one\n')
# String Pattern matching
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+)\1', r'\1', 'cat in the hat')
'tea for too'.replace('too', 'two')
# Mathematics
import math
math.cos(math.pi / 4)
math.log(1024, 2)
import random
random.choice(['apple', 'pear', 'banana'])
random.sample(range(100), 10) # sampling without replacement
random.random() # random float
random.randrange(6) # random integer chosen from range(6)
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
statistics.median(data)
statistics.variance(data)
# Internet Access
from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as responce:
    for line in responce:
        line = line.decode('utf-8') # decoding the binary to test
        if 'EST' in line or 'EDT' in line: # look for Eastern Time
            print(line)

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
 From: soothsayer@example.org

 Beware the Ides of March.
 """)
server.quit()
# Dates and Times
# Dates are easily constructed and formatted
from datetime import date
now = date.today()
print(now)
now.strftime("%m-%d-%y. %d %b %Y, is a %A on the %d day of %B.")
# Dates support calender Arithmetic
birthday = (1964, 7, 31)
age = now - birthday
age.days
import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
# Performance Measurement
from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
# Quality Control
def average(values):
    """Computes the arithmetic mean of numbers.

    print(average([20, 30, 70]))
    40.0
    """
    return sum(values)/ len(values)

import doctests
doctests.testmod() # automatically validate the embeded tests
# The unittests module
import unittest

class testStatisitcalFunctions(unittest.Testcase):

    def test_average(self):
        self.assertEqual(average[20, 30, 70], 40.0)
        self.assertEqual(round(average[1, 5, 7], 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 40)

unittest.main() # calling from command line invokes all tests