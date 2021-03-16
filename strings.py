'Spam_eggs' # single quote
print('Spam eggs')
'doesn\'t' # use \' to escape the single quote
print('doesn\'t')
"doesn't" # use double quote
print("doesn't")
'"Yes," they said.'
print('"Yes," they said.')
"\"Yes,\" they said."
print("\"Yes,\" they said.")
'"Isn\'t," they said.'
print('"Isn\'t," they said.')
s = 'First Line.\nSecond Line.' # \n means newline
print(s)
print('C:\ some\name')# here \n means new line
print(r'C:\ some\name') # r before the quote makes it a raw string
print("""\
usage: thingy [OPTIONS]
-h              Display this usage message
-H hostname     Hostname to connect to
""") # Multiple lines
# 3 times 'un' followed by 'ium'
print(3 * 'un' + 'ium') # concatenate using + operator and repeat using *
print('py' 'thon') # automatic concatenation
text = ('Put several strings within parenthesis '
        'to have them joined together') # when you want to break long strings
print(text)
prefix = 'py'
print(prefix + 'thon') # use + to concatenate variables or a variable and a literal
word = 'python'
print(word[0]) # indexing strings with the first character having index 0
print(word[5]) # character in position 5
print(word[-1]) # last character
print(word[-2]) # second last character
# In addition to indexing, slicing is also supported. Slicing a lows you to obtain substrings
print(word[0:2]) # characters from position 0 included to position 2 excluded
print(word[2:5]) # characters from position 2 included to position 5 exclude
# joining slices to form string
print(word[:2] + word[2:])
print(word[:4] + word[4:])
print(word[:2]) # characters from the beginning to position 2 (excluded)
print(word[4:]) # characters from position 4 (included) to end
print(word[-2]) # characters from second last (included) to the end
print('J' + word[1:]) # creating a new string
s = 'supercalifragilisticexpialidocious'
len(s) # returns the length of the string
print(len(s))









