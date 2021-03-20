def fib(n): # write fibonacci series upto n
    """ print fibonacci series upto n"""
    a, b = 0, 1
    while a < n:
        print(a, end =' ')
    a, b = b, a+b
    print()
    # Now call the fibonacci that we just defined
    fib(2000)
fib
f = fib
f(100)
def fib2(n): # returns fibonacci series upto n
    """returns a list fibonacci series upto n."""
    result = []
    a, b = 0, 1
    while a < n:
        result. append(a) # see below
        a, b = b, a+b
        return result
    f100 = fib2(100) # call it
    f100 # write the result

