squares = [1,4,9,16,25] # list of comma separated values between square brackets
print(squares)
# indexing lists
squares[0] # indexing returns the term
print(squares[0])
print(squares[-3])
print(squares[-3:]) # slicing returns a new list
squares[:] # returns a new shallow copy of the list
print(squares[:])
# lists also support operations like concatenation
print(squares + [36,49,64,81,100])
# lists are mutable, i.e, their contents can be changed
cubes = [1,8,27,65,125]
cubes[3] = 64
print(cubes)
# new items can be added and the end of the list using append()
cubes.append(216) # add the cube of 6
cubes.append(7 ** 3) # add the cube of 7
print(cubes)
# slicing to change the size of list or clear it entirely
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E'] # replace some values
print(letters)
letters[2:5] = [] # now remove them
print(letters)
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)
letters = ['a', 'b', 'c', 'd']
print(len(letters))
# it is possible to nest lists (create lists containing other lists)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
