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
# Output Formatting
import reprlib
reprlib.repr(set('supercalifragilisticexpialidocious'))
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
 'yellow'], 'blue']]]
pprint.pprint(t, width=30)
import textwrap
doc = """ This wrap() method is just like fill() except that ot returns 
a list of strings instead of one big string with new lines to separate 
the wrapped lines"""
print(textwrap.fill(doc, width = 40))
import locale
locale.setlocale(locale.LC_ALL, 'English_United States 1252')
conv = locale.localeconv()
x = 1234567.8
locale.format("%d", x, grouping=True)
locale.format_string("%s.*f", (conv['currency_symbol'],
                               conv['frac_digits'], x), grouping=True)
# Templating
from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')
import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'
fmt = input('Enter rename style(%d-date %n-seqnum %f-format): ')

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))
# Working with Binary Data Record Layouts
import struct

with open('myfiles.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range (3):         # show the first three headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filename_size, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size  # skip to the next header
# Multi-threading
import threading, zipfile

class AsyncZip(threading.thread):
    def __init__(self, infile, outfile):
        threading.threa.__init__(self)
        self.infile = infile
        self.outfile = outfile
    def run(self):
        f = zipfile.ZipeFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)
# Logging
logging.debug('Debugging information')
logging.infor('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occured')
logging.critical('Critical error -- shutting down')
# Weak References
import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)       # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a # does not create a refrence
d['primary']  # fetch the if it is still still alive

del a       # remove the one reference
gc.collect() # run garbage collection right away
d['primary'] # entry was automatically removed
# Tools for Working with Lists
from array import array
a = array('H', [4000, 10, 700, 22222])
sum (a)
a[1:3]
from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (300, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
scores
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)           # rearrange the list into heap order
heappush(data, -5)      # add a new entry
[heappop(data) for i in range (3)] # fetch the three smallest entries
# Decimal Floating Point Arithmetic
from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)
round(.70 * 1.05, 2)
Decimal('1.00') % Decimal('.10')
Decimal('0.00')
1.00 % 0.10

sum([Decimal('0.1')] * 10) == Decimal('1.0')
sum([0.1]*10) == 1.0
getcontext.prec = 36
Decimal(1)/ Decimal(7)